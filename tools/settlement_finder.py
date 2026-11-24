#!/usr/bin/env python3
"""
settlement_finder.py - systems richest in Odyssey settlements of given types.

For on-foot farming: ranks the systems around a reference system by how many
Odyssey settlements of the wanted economies they hold (default Military,
Extraction, Industrial, High Tech), leaving out settlements whose
controlling faction is at war or in an election (settlements in conflict
can't be raided - LTT 7786, 23 Nov; HIP 118062, 24 Nov 2026).

Layouts: the pad signature narrows a settlement to one or two OMG layouts
(table tools/data/odyssey_layouts.json, checked in game, On-Foot.md 5.0 -
e.g. High Tech L1 S1 = High Tech 1, Military L1 S2 = Military 2). Two
layouts left = tell them by the in-game size marker (- tiny, + small,
++ medium). Filter with --layout "High Tech 1".

Spansh does not know settlement LAYOUTS (Voz de Carabas' Odyssey Map Guide
numbers: Military 1-4, Extraction 1-2, Industrial 1-5, High Tech 1-...).
What it gives, and what this script shows to narrow them down:
  * the landing pads of each settlement, grouped as a signature
    ("L1" = one large pad, "L1 S1", "L2 S2", "M1", "S3"...) - compare with
    the pad layout of the OMG map you want;
  * the body's gravity (on-foot comfort) and distance from the star;
  * the system's starports (concourse = mission board, bartender).
The layout itself only shows when flying over the settlement.

Faction states: Spansh's per-station state can be months old; the war check
uses the system's current faction list (updated whenever someone visits).

Data: https://spansh.co.uk (EDDN-fed).

Usage examples:
  python tools/settlement_finder.py                         # around Cubeo
  python tools/settlement_finder.py --radius 80 --min 6
  python tools/settlement_finder.py --economy Military --pads L1
  python tools/settlement_finder.py --economy "Extraction,Military" \\
      --max-gravity 1.5 --details 3
"""

import argparse
import sys
import urllib.error
from collections import Counter, defaultdict

from waypoint_route import STATIONS_API, lookup, post

ECONOMIES = "Military,Extraction,Industrial,High Tech"
# Factions in these states have their settlements shown "in conflict".
# Election too: the five High-Tech 1 sites of HIP 118062 (24 Nov 2026) were
# all in conflict while Spansh only listed elections (its states lag).
WAR_STATES = {"War", "Civil War", "Election"}
SHORT = {"Military": "Mil", "Extraction": "Ext", "Industrial": "Ind",
         "High Tech": "HT", "Agriculture": "Agri", "Tourism": "Tour"}
PORTS = ("Coriolis Starport", "Orbis Starport", "Ocellus Starport",
         "Asteroid base", "Planetary Port", "Outpost", "Planetary Outpost",
         "Dodec Starport")


def pad_sig(st):
    parts = []
    for size, key in (("L", "large_pads"), ("M", "medium_pads"),
                      ("S", "small_pads")):
        n = st.get(key) or 0
        if n:
            parts.append("%s%d" % (size, n))
    return " ".join(parts) or "no pad"


def layout_cands(st):
    """Likely OMG layouts of a settlement from economy + pads (ids)."""
    from material_finder import candidates, load_layouts
    lays = load_layouts()
    pads = {k: st.get(f) or 0 for k, f in (("L", "large_pads"),
            ("M", "medium_pads"), ("S", "small_pads"))}
    c = candidates({k: v for k, v in pads.items() if v},
                   st.get("primary_economy"), lays)
    top = max(w for _, w in c)
    return [l for l, w in sorted(c, key=lambda x: -x[1]) if w >= 0.3 * top]


def layout(st):
    from material_finder import load_layouts, tag
    lays = load_layouts()
    return "/".join(tag(l, lays) for l in layout_cands(st))


def norm(name):
    return "".join(ch for ch in name.lower() if ch.isalnum())


def fetch_settlements(ref, radius, economies):
    found, page = [], 0
    body = {"filters": {"distance": {"min": "0", "max": str(radius)},
                        "type": {"value": ["Settlement"]},
                        "primary_economy": {"value": economies}},
            "reference_system": ref, "size": 100,
            "sort": [{"distance": {"direction": "asc"}}]}
    while True:
        body["page"] = page
        data = post(body, STATIONS_API)
        batch = data.get("results", [])
        found.extend(batch)
        page += 1
        if not batch or len(found) >= data.get("count", 0):
            return found


def system_ports(name):
    data = post({"filters": {"distance": {"min": "0", "max": "0.1"},
                             "type": {"value": list(PORTS)}},
                 "reference_system": name, "size": 50}, STATIONS_API)
    return [s for s in data.get("results", [])
            if s.get("system_name", "").lower() == name.lower()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--ref", default="Cubeo", help="reference system")
    ap.add_argument("--radius", type=float, default=60.0)
    ap.add_argument("--economy", default=ECONOMIES,
                    help="comma list of settlement economies (default %s)"
                    % ECONOMIES)
    ap.add_argument("--min", type=int, default=5,
                    help="minimum matching settlements per system")
    ap.add_argument("--pads", default=None,
                    help="keep only settlements with this pad signature, "
                         "e.g. L1, 'L1 S1', M1")
    ap.add_argument("--layout", default=None,
                    help="keep only settlements that can be this OMG "
                         "layout, e.g. 'High Tech 1', 'Military 2', 'Ext 4'")
    ap.add_argument("--max-gravity", type=float, default=None,
                    help="leave out settlements on heavier bodies (g)")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--details", type=int, default=0,
                    help="list the settlements of the N best systems")
    args = ap.parse_args()

    economies = [e.strip() for e in args.economy.split(",") if e.strip()]
    want = None
    if args.layout:
        from material_finder import load_layouts, short_name
        lays = load_layouts()
        key = norm(args.layout)
        want = [l for l in lays if key in (norm(lays[l]["name"]),
                                          norm(short_name(l, lays)))]
        if not want:
            ap.error("unknown layout %r - e.g. %s" % (args.layout, ", ".join(
                lays[l]["name"] for l in sorted(lays)[:4])))
        want = want[0]
        economies = [lays[want]["economy"]]
    sets = fetch_settlements(args.ref, args.radius, economies)
    if args.pads:
        sets = [s for s in sets if pad_sig(s) == args.pads]
    if want:
        sets = [s for s in sets if want in layout_cands(s)]
    if args.max_gravity is not None:
        sets = [s for s in sets if (s.get("body_gravity") or 0)
                <= args.max_gravity]
    by_sys = defaultdict(list)
    for s in sets:
        by_sys[s["system_name"]].append(s)
    print("%d settlement(s) [%s%s] within %.0f ly of %s, in %d system(s)"
          % (len(sets), "/".join(economies),
             ", pads " + args.pads if args.pads else "", args.radius,
             args.ref, len(by_sys)))

    ranked = sorted(by_sys.items(), key=lambda kv: -len(kv[1]))
    ranked = [kv for kv in ranked if len(kv[1]) >= args.min]
    rows = []
    for name, sts in ranked[:args.top * 2]:       # war check costs a call
        rec = lookup(name)
        at_war = {f["name"] for f in rec.get("minor_faction_presences") or []
                  if f.get("state") in WAR_STATES}
        ok = [s for s in sts if s.get("controlling_minor_faction")
              not in at_war]
        if len(ok) < args.min:
            continue
        rows.append((name, rec, ok, len(sts) - len(ok), at_war))
        if len(rows) >= args.top:
            break
    rows.sort(key=lambda r: -len(r[2]))
    if not rows:
        print("No system with %d+ such settlements outside a war - try a "
              "larger --radius or a lower --min." % args.min)
        return

    print("War check: the system's current faction states (Spansh).\n")
    for i, (name, rec, ok, war_n, at_war) in enumerate(rows, 1):
        eco = Counter(SHORT.get(s.get("primary_economy"), s.get(
            "primary_economy")) for s in ok)
        bodies = len({s.get("body_name") for s in ok})
        grav = max((s.get("body_gravity") or 0) for s in ok)
        d = ok[0].get("distance") or 0
        print("%2d. %-26s %5.1f ly  %-10s %-9s  %d settlements: %s" % (
            i, name, d, rec.get("government") or "?",
            (rec.get("controlling_power") or "-")[:9], len(ok),
            ", ".join("%s %d" % kv for kv in eco.most_common())))
        for e in economies:
            sig = Counter(pad_sig(s) for s in ok
                          if s.get("primary_economy") == e)
            sig_layout = {(e, pad_sig(s)): layout(s) for s in ok
                          if s.get("primary_economy") == e}
            if sig:
                print("      %-4s pads: %s" % (SHORT.get(e, e), ", ".join(
                    "%s x%d (%s)" % (k, n, sig_layout[(e, k)])
                    for k, n in sig.most_common())))
        print("      on %d bod%s, gravity up to %.2f g%s" % (
            bodies, "y" if bodies == 1 else "ies", grav,
            "; %d more at war (%s)" % (war_n, ", ".join(sorted(at_war)))
            if war_n else ""))
        if i <= args.details:
            ports = system_ports(name)
            print("      ports: %s" % (", ".join(
                "%s (%s, %d ls)" % (p["name"], p.get("type"),
                                    p.get("distance_to_arrival") or 0)
                for p in ports[:4]) or "none"))
            for s in sorted(ok, key=lambda s: (s.get("primary_economy"),
                                               s.get("body_name") or "")):
                print("        %-4s %-34s %-7s %-16s %-18s %4.2f g %6d ls  %s" % (
                    SHORT.get(s.get("primary_economy"), "?"), s["name"][:34],
                    pad_sig(s), layout(s), (s.get("body_name") or "")[-18:],
                    s.get("body_gravity") or 0,
                    s.get("distance_to_arrival") or 0,
                    s.get("controlling_minor_faction") or ""))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
