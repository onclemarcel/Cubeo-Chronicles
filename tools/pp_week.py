#!/usr/bin/env python3
"""
pp_week.py - one route for the week's Powerplay assignments.

Reads the "THIS WEEK" table of Powerplay Missions.md (§1) - one row per
assignment, filled in after the Thursday tick:

  | # | Assignment | Card | System(s) | Status | Merits |
  | 2 | Scan megaships | 4.9 | reinforcement | 3 / 11 | 2,400 |

  Card       the mission card (§4) - it gives the kind of work:
             4.1 rare goods, 4.2 ship scans, 4.5 bounties, 4.6/4.7
             holoscreens, 4.9 megaships (others are listed, not routed)
  System(s)  a system name, or a condition: reinforcement (Aisling-
             controlled), undermining (controlled by another Power)
  Status     "done / target" ("0 / 357,941 CR" works); "✔" = finished

and plans one route from the current system (journal) through:
  * every system named by an open assignment, with its tasks and the
    useful stations (Spansh);
  * a rival-controlled system with an orbital station for holoscreens
    "undermining" - a system already on the route if one qualifies;
  * the megaships still to scan (waypoint_route.py: Inara paste in
    tools/inara_megaships.txt, journals, known paid systems);
  * the rare-goods source (--rare-source), placed before the sale system.
Spansh has no rare-goods data: find the source yourself (Inara commodity
search) and pass it with --rare-source "System".

Usage examples:
  python tools/pp_week.py
  python tools/pp_week.py --rare-source "Karsuki Ti" --to Cubeo
  python tools/pp_week.py --jump 38          # plan for the Dart
"""

import argparse
import os
import re
import sys
import urllib.error
from datetime import datetime, timezone

from waypoint_route import (CONTROL_STATES, END, INARA_FILE, JOURNAL_DIR,
                            KNOWN_UPLINKS, PENALTY, Planner, dist,
                            fetch_corridor, fetch_sphere, journal_megaships,
                            journal_state, last_tick, load_inara, lookup,
                            megaship_evidence, power_filters, system_stations,
                            xyz)

HERE = os.path.dirname(os.path.abspath(__file__))
MISSIONS_MD = os.path.join(HERE, os.pardir, "Powerplay Missions.md")
POWER = "Aisling Duval"
POWERS = ("A. Lavigny-Duval", "Aisling Duval", "Archon Delaine",
          "Denton Patreus", "Edmund Mahon", "Felicia Winters",
          "Jerome Archer", "Li Yong-Rui", "Nakato Kaine", "Pranav Antal",
          "Yuri Grom", "Zemina Torval")
CARD_KIND = {"4.1": "rare", "4.2": "shipscan", "4.5": "bounty",
             "4.6": "holo", "4.7": "holo", "4.9": "megaship"}
ROUTED = set(CARD_KIND.values())
ORBITAL = ("Coriolis Starport", "Orbis Starport", "Ocellus Starport",
           "Dodec Starport", "Asteroid base", "Outpost")
MEGASHIP_EXCLUDE = {"cubeo"}       # 0 merits for uplink scans (card 4.9)


# ------------------------------------------------------------ assignments --
def clean(cell):
    return re.sub(r"[*`_]", "", cell).strip()


def read_week(path):
    """Rows of the §1 table as dicts; done/target parsed from Status."""
    rows, header = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("|"):
                if header and rows:
                    break
                continue
            cells = [clean(c) for c in line.strip().strip("|").split("|")]
            if header is None:
                if "Assignment" in cells and "Card" in cells:
                    header = cells
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            row = dict(zip(header, cells))
            if not row.get("Assignment"):
                continue
            status = row.get("Status", "")
            nums = [int(n.replace(",", "").replace(" ", ""))
                    for n in re.findall(r"\d[\d, ]*\d|\d", status)]
            row["finished"] = "✔" in status or "done" in status.lower()
            row["done"], row["target"] = (nums + [0, 0])[:2] \
                if len(nums) >= 2 else (0, nums[0] if nums else 0)
            row["left"] = max(0, row["target"] - row["done"])
            card = re.match(r"\d+\.\d+", row.get("Card", ""))
            row["card"] = card.group(0) if card else ""
            row["kind"] = CARD_KIND.get(row["card"], "other")
            where = row.get("System(s)", "")
            row["cond"] = next((c for c in ("reinforcement", "undermining",
                                            "acquisition")
                                if c in where.lower()), None)
            row["system"] = None if row["cond"] or where in ("", "-", "—") \
                else where
            rows.append(row)
    if header is None:
        sys.exit("No 'THIS WEEK' table found in %s" % path)
    return rows


# ---------------------------------------------------------------- helpers --
def is_rival(s):
    p = s.get("controlling_power")
    return bool(p) and p != POWER and \
        s.get("power_state") in CONTROL_STATES.split(",")


def orbitals(stations):
    return [st for st in stations or [] if st.get("type") in ORBITAL]


def station_txt(st):
    pads = "L" if st.get("has_large_pad") else \
        "M" if st.get("medium_pads") else "S"
    return "%s (%s, %d ls, pad %s, %s)" % (
        st["name"], st.get("type"), st.get("distance_to_arrival") or 0, pads,
        st.get("controlling_minor_faction") or "?")


def merits(row):
    m = re.sub(r"\D", "", row.get("Merits", ""))
    return int(m) if m else 0


# -------------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--from", dest="start", default=None,
                    help="start system (default: current, from journal)")
    ap.add_argument("--to", default=None,
                    help="end system (default: open route)")
    ap.add_argument("--rare-source", action="append", default=[],
                    help="system where the rare goods are bought")
    ap.add_argument("--file", default=MISSIONS_MD,
                    help="markdown file holding the THIS WEEK table")
    ap.add_argument("--inara", default=INARA_FILE)
    ap.add_argument("--jump", type=float, default=None,
                    help="jump range (default: current ship, journal)")
    ap.add_argument("--detour", type=float, default=30.0,
                    help="megaship search corridor half-width, ly")
    ap.add_argument("--journal-dir", default=JOURNAL_DIR)
    args = ap.parse_args()

    rows = read_week(args.file)
    open_rows = [r for r in rows if not r["finished"] and
                 (r["left"] or not r["target"])]
    j_sys, j_jump, ship = journal_state(args.journal_dir)
    start = args.start or j_sys
    if not start:
        ap.error("no --from given and no journal found")
    jump = args.jump or j_jump or 40.0
    tick = last_tick(datetime.now(timezone.utc))

    print("Week of the %s tick - %d open assignment(s), %s merits on the "
          "table. Ship: %s, %.1f ly" % (
              tick.strftime("%d %b"), len(open_rows),
              format(sum(merits(r) for r in open_rows), ","),
              ship or "?", jump))

    # ---- fixed stops: start, rare sources, named systems, end
    named = []
    for r in open_rows:
        if r["system"] and r["kind"] in ROUTED and r["system"] not in named:
            named.append(r["system"])
    names = [start] + [s for s in args.rare_source if s not in named] + \
        [n for n in named if n != start]
    if args.to and args.to not in names:
        names.append(args.to)
    recs, canon = {}, {}
    for n in names:
        rec = lookup(n)
        recs[rec["name"]], canon[n.lower()] = rec, rec["name"]
    fixed = [canon[n.lower()] for n in names] + ([] if args.to else [END])
    coords = {n: xyz(r) for n, r in recs.items()}
    sale = [canon[r["system"].lower()] for r in open_rows
            if r["kind"] == "rare" and r["system"]]
    before = [(canon[s.lower()], t) for s in args.rare_source for t in sale]
    tasks = {n: [] for n in recs}
    stations = {}

    def stations_of(n):
        if n not in stations:
            stations[n] = system_stations(n)
        return stations[n]

    # ---- holoscreens in undermining systems: pick one rival system
    for r in open_rows:
        if r["kind"] != "holo" or r["cond"] != "undermining":
            continue
        pick = None
        for n in fixed:
            if n != END and is_rival(recs[n]) and orbitals(stations_of(n)):
                pick = n
                break
        if pick is None:
            rivals = [p for p in POWERS if p != POWER]
            pts = [coords[n] for n in fixed if n != END]
            cands = [c for c in fetch_corridor(pts, 25.0, power_filters(
                None, CONTROL_STATES.split(","))) if is_rival(c) and
                orbitals(c.get("stations"))]
            cands = [c for c in cands if c["controlling_power"] in rivals]
            if cands:
                tmp = Planner(dict(coords, **{c["name"]: xyz(c)
                                              for c in cands}), jump)
                path = tmp.plan(fixed, [], 0)
                best = min(cands, key=lambda c: tmp.insert_cost(
                    path, c["name"])[0])
                pick = best["name"]
                recs[pick], coords[pick] = best, xyz(best)
                fixed.insert(len(fixed) - 1, pick)   # before the end
                tasks[pick] = []
        if pick is None:
            print("  ! no rival-controlled system with an orbital station "
                  "near the route for: %s" % r["Assignment"])
            continue
        tasks[pick].append((r, "undermining"))

    for r in open_rows:
        if r["system"] and r["kind"] in ROUTED:
            tasks[canon[r["system"].lower()]].append((r, None))
    for s in args.rare_source:
        tasks[canon[s.lower()]].append(({"kind": "rare-buy",
                                         "left": sum(r["left"] for r in
                                                     open_rows if r["kind"]
                                                     == "rare"),
                                         "sale": sale}, None))

    # ---- megaships
    mega_rows = [r for r in open_rows if r["kind"] == "megaship"]
    needed = sum(r["left"] for r in mega_rows)
    scored = {}
    if needed:
        filters = power_filters(POWER, CONTROL_STATES.split(","))
        pts = [coords[n] for n in fixed if n != END]
        cands = {c["name"]: c for c in fetch_corridor(pts, args.detour,
                                                      filters)}
        ref, inara = load_inara(args.inara, tick)
        if inara:
            centre = xyz(lookup(ref)) if ref else pts[0]
            far = max(dist(centre, p) for p in pts)
            for c in fetch_sphere(centre, 100 + far, filters):
                if c["name"] in inara:
                    cands.setdefault(c["name"], c)
        jmega = journal_megaships(args.journal_dir)
        for n, c in cands.items():
            if n.lower() in MEGASHIP_EXCLUDE:
                continue
            ev = megaship_evidence(n, c.get("stations"), jmega, inara,
                                   KNOWN_UPLINKS, tick)
            if ev:
                scored[n] = ev
                coords[n] = xyz(c)
                recs.setdefault(n, c)

    planner = Planner(coords, jump,
                      weight={n: PENALTY[v[1]] for n, v in scored.items()},
                      value={n: v[2] for n, v in scored.items()},
                      fixed=fixed, before=before)
    path = planner.plan(fixed, [n for n in scored if n not in fixed], needed)

    # ---- print the itinerary
    print()
    real = [n for n in path if n != END]
    total_ly = total_j = scans = 0
    hacks = 0
    for i, n in enumerate(real):
        rec = recs[n]
        head = "%2d. %-26s" % (i + 1, n)
        if i:
            d = dist(coords[real[i - 1]], coords[n])
            j = int(planner.leg(real[i - 1], n))
            total_ly += d
            total_j += j
            head += " %6.1f ly ~%d j" % (d, j)
        else:
            head += " %-13s" % "start"
        ctrl = rec.get("controlling_power") or "-"
        print("%s   %s %s, %s security" % (
            head, ctrl, rec.get("power_state") or "", rec.get("security")
            or "?"))
        for r, why in tasks.get(n, []):
            kind = r["kind"]
            if kind == "rare-buy":
                print("      - BUY %d rare goods here (not from %s) for the "
                      "rare-goods sale" % (r["left"], ", ".join(r["sale"])))
                continue
            card = "card %s" % r["card"]
            if kind == "holo":
                hacks += r["left"]
                orb = orbitals(stations_of(n))
                rivals = [p for p in rec.get("power") or [] if p != POWER]
                print("      - Holoscreens: %d hacks (%s%s). Recon limpets; "
                      "each hack is a fine to the station's faction" % (
                          r["left"], card, ", rival system" if why else ""))
                if not why:
                    print("        Aisling system: only screens hijacked by "
                          "a rival can be hacked - rivals present: %s" % (
                              ", ".join(rivals) or "NONE - none hackable"))
                for st in orb[:3]:
                    print("        at %s" % station_txt(st))
            elif kind == "shipscan":
                print("      - Scan %d ships / wakes (%s). High-energy wakes "
                      "need an FSD wake scanner. Hand the data in at any "
                      "Aisling system%s" % (
                          r["left"], card, " - this one is"
                          if rec.get("controlling_power") == POWER else ""))
            elif kind == "bounty":
                print("      - Bounties: %s CR of vouchers (%s) - combat "
                      "hull, nav beacon / RES; vouchers need not be cashed"
                      % (format(r["left"], ","), card))
            elif kind == "rare":
                mk = [st for st in stations_of(n) if st.get("has_market")
                      and st.get("type") != "Drake-Class Carrier"]
                print("      - Sell %d rare goods (%s), bought in another "
                      "system%s" % (r["left"], card, "" if args.rare_source
                                    else " - SOURCE NOT GIVEN "
                                    "(--rare-source)"))
                for st in mk[:3]:
                    print("        at %s" % station_txt(st))
            else:
                print("      - %s (%s)" % (r["Assignment"], card))
        if n in scored:
            scans += scored[n][2]
            print("      - Megaships: %s" % scored[n][0])
    print("\n~%d jumps, %.0f ly (estimate at %.0f ly/jump)%s" % (
        total_j, total_ly, planner.reach,
        "" if args.to else ", open end"))
    if needed:
        print("Megaships: %d / %d on the route%s" % (
            min(scans, needed), needed,
            "" if scans >= needed else " - paste a wider Inara search"))
    if hacks:
        print("Recon limpets: %d hacks planned - carry at least %d" % (
            hacks, hacks + 4))
    other = [r for r in open_rows if r["kind"] not in ROUTED or
             (r["kind"] in ROUTED and not r["system"] and not r["cond"])]
    for r in other:
        print("Not routed: %s (card %s, %s)" % (
            r["Assignment"], r["card"] or "?", r.get("System(s)") or "?"))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
