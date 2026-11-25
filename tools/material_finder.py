#!/usr/bin/env python3
"""
material_finder.py - where to farm a given Odyssey item (goods or data).

Give it one or more on-foot items (Inara names, partial names work) and it
ranks the settlements around a reference system by how much of that item a
landing should yield, leaving out settlements whose controlling faction is
at war (ground conflict zones can't be looted - the LTT 7786 lesson).

How it reasons, from three data sources:
  1. data/odyssey_items.tsv - Inara's item list: type (Goods/Data), number
     of engineer blueprints using it ("used"; 0 = sell it), and where it
     drops (building codes: CMD, HAB, RES, IND, EXT, AGRI, STO, PWR, MED).
  2. data/odyssey_layouts.json - the 28 settlement layouts of Odyssey Site
     Maps (Voz DeCarabas): buildings and data ports per building, pads read
     from the map images (tools/build_layouts.py regenerates it).
  3. Spansh - the real settlements nearby: economy, pads, body, faction.
A settlement's layout is not on Spansh. The script narrows it from the
economy (Military -> Military 1-5...) and the pad signature ("L1", "L1 M2"),
then scores the candidate layouts:
  * Data  -> data ports in the buildings where the item drops;
  * Goods -> number of such buildings (a proxy for lockers: a small HAB has
    about two, a big one more - the maps don't show lockers).
"Settlements" (any building) counts 1 everywhere. Several items: each one
is scaled to its best layout, then added, so they weigh the same.
Your own loot corrects the building model: the journals (read by
../elite-loot/loot_stats.py) give, per settlement economy, how often the
item turned up per visit; the score is multiplied by that rate relative to
the average, smoothed so that a few visits weigh little (an economy with no
visit keeps x1). Inara's buildings alone put Manufacturing Instructions in
tourist HABs - 0 found in 14 tourist visits, 2 in 6 industrial ones. An
economy where the item turned up although Inara lists none of its
buildings counts at least 1. --no-history turns it off. French item names
from the journals are accepted too ("Guides industriels").
The layout guess is shown with each settlement, with the in-game size
marker of each candidate (- tiny, + small, ++ medium): column "aim" says
which marker to look for next to the name in the nav panel to land on the
best one. Pad table and checks: On-Foot.md §5.0.

Data: https://spansh.co.uk (EDDN-fed; faction states as of the last visit
by someone running an EDDN client).

Usage examples:
  python tools/material_finder.py "Manufacturing Instructions"
  python tools/material_finder.py "weapon schem" --ref Cubeo --radius 50
  python tools/material_finder.py "Patrol Routes,Weapon Test Data" --pad L
  python tools/material_finder.py "Ionised Gas" --info     # offline card
  python tools/material_finder.py --locker                  # what to sell
  python tools/material_finder.py --survey "HIP 1914"       # pads/layouts
  python tools/material_finder.py "Guides industriels"      # French name
"""

import argparse
import csv
import difflib
import json
import os
import re
import sys
import urllib.error
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_FILE = os.path.join(HERE, "data", "odyssey_items.tsv")
LAYOUTS_FILE = os.path.join(HERE, "data", "odyssey_layouts.json")
DEFAULT_REF = "Cubeo"
PAD_RANK = {"S": 1, "M": 2, "L": 3}
NOT_SETTLEMENT = ("Irregular markers", "Crashed satellite",
                  "Surface crash site", "Mission reward", "Thargoid site")
CODE = {"MED room": "MED", "Settlements": "*"}
# In-game size marker next to the settlement name (nav panel, system map)
MARK = {"tiny": "-", "small": "+", "medium": "++"}
# Loot history: ../elite-loot/loot_stats.py (sibling of this repo)
LOOT_DIR = os.path.join(os.path.dirname(os.path.dirname(HERE)), "elite-loot")
LOCKERS_SINCE = "2026-11-07"   # lockers looted from then on (goods)
ECO_LOOT = {"Agri": "Agriculture", "Extraction": "Extraction",
            "HighTech": "High Tech", "Industrial": "Industrial",
            "Military": "Military", "Tourism": "Tourism"}
SMOOTH = 3.0                   # pseudo-visits at the average rate


# ----------------------------------------------------------------- data --
def key(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def load_items():
    items = {}
    with open(ITEMS_FILE, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            locs = [l.strip() for l in (row["Location"] or "").split(",")
                    if l.strip()]
            codes = set()
            for l in locs:
                if l in CODE:
                    codes.add(CODE[l])
                elif l.endswith(" buildings"):
                    codes.add(l.split()[0])
            items[key(row["Item"])] = {
                "key": key(row["Item"]),
                "name": row["Item"], "type": row["Type"],
                "used": int(row["Used"] or 0), "locations": locs,
                "codes": codes,
                "other": [l for l in locs if l in NOT_SETTLEMENT]}
    return items


def load_layouts():
    with open(LAYOUTS_FILE, encoding="utf-8") as fh:
        return json.load(fh)["layouts"]


def resolve(query, items, local=None):
    """Item from an Inara name or a localised journal name, partial ok."""
    k = key(query)
    local = {key(loc): items[n] for n, loc in (local or {}).items()
             if loc and n in items}
    if k in items:
        return items[k]
    if k in local:
        return local[k]
    hits = [v for kk, v in items.items() if k in kk]
    if not hits:
        hits = list({v["key"]: v for kk, v in local.items()
                     if k in kk}.values())
    if len(hits) == 1:
        return hits[0]
    if not hits:
        close = difflib.get_close_matches(k, items.keys(), n=5, cutoff=0.6)
        hits = [items[c] for c in close]
        if len(hits) == 1:
            return hits[0]
    sys.exit("'%s' is %s: %s" % (
        query, "ambiguous" if hits else "unknown",
        ", ".join(h["name"] for h in hits) or "no close match"))


def load_history(folder):
    """(visits, localised names) from the journals via loot_stats.py."""
    if not os.path.isdir(folder) or not os.path.isdir(LOOT_DIR):
        return None, {}
    sys.path.insert(0, LOOT_DIR)
    try:
        import loot_stats
        return loot_stats.parse(folder)
    except (ImportError, SystemExit):
        return None, {}


def eco_factors(item, visits):
    """{economy: (factor, visits with the item, visits)}: how often the item
    turned up per visit in each settlement economy, against the average,
    smoothed with SMOOTH visits at the average. {} = never found."""
    vs = [v for v in visits or [] if v["settlement_economy"] in ECO_LOOT
          and (item["type"] == "Data" or v["start"] >= LOCKERS_SINCE)]
    total = sum(v["loot"][item["key"]] for v in vs)
    if not total:
        return {}
    avg = total / len(vs)
    out = {}
    for code, eco in ECO_LOOT.items():
        grp = [v for v in vs if v["settlement_economy"] == code]
        found = sum(v["loot"][item["key"]] for v in grp)
        rate = (found + SMOOTH * avg) / (len(grp) + SMOOTH)
        out[eco] = (rate / avg, sum(1 for v in grp if v["loot"][item["key"]]),
                    len(grp))
    return out


# -------------------------------------------------------------- scoring --
def layout_yield(item, lay):
    """Ports (data) or buildings (goods) where the item drops."""
    source = lay["data_ports"] if item["type"] == "Data" else lay["buildings"]
    n = sum(source.get(c, 0) for c in item["codes"] if c != "*")
    if "*" in item["codes"]:
        n = max(n, 1)
    return n


def layout_scores(items, layouts, factors=None):
    """{layout_id: (score, [per-item yield])}, items scaled to their best.
    factors: per item, {economy: (factor, ...)} from the loot history."""
    factors = factors or [{}] * len(items)
    raw = {lid: [layout_yield(it, lay) for it in items]
           for lid, lay in layouts.items()}
    eff = {}
    for lid, ys in raw.items():
        eco = layouts[lid]["economy"]
        eff[lid] = []
        for y, fac in zip(ys, factors):
            f = fac.get(eco, (1.0,))[0] if fac else 1.0
            if not y and fac and fac.get(eco, (0, 0))[1]:
                y = 1          # found there although Inara lists no building
            eff[lid].append(y * f)
    best = [max(eff[lid][i] for lid in eff) or 1 for i in range(len(items))]
    out = {}
    for lid, ys in eff.items():
        score = ys[0] if len(items) == 1 else sum(
            y / b for y, b in zip(ys, best))
        out[lid] = (score, raw[lid])
    return out


def parse_pads(sig):
    """'L1 S1' -> ([{'L': 1, 'S': 1}], True); 'M1|S1?' -> ([{M1}, {S1}],
    False): a layout whose pads are one of several, not yet known."""
    alts = [{m.group(1): int(m.group(2))
             for m in re.finditer(r"([LMS])(\d+)", alt)}
            for alt in (sig or "").replace("?", "").split("|")]
    return [a for a in alts if a], "?" not in (sig or "?")


def candidates(st_pads, economy, layouts):
    """Layouts a settlement can be, with a weight from the pad match:
    1 = confirmed pads; 0.5 = unsure pads (0.25 if a confirmed layout
    already has them); no match = 0, or a small weight for unsure layouts
    with the same number of pads."""
    out = []
    total = sum(st_pads.values())
    fam = [(lid,) + parse_pads(lay["pads"]) for lid, lay in layouts.items()
           if lay["economy"] == economy]
    owned = any(sure and st_pads in alts for _, alts, sure in fam)
    for lid, alts, sure in fam:
        if st_pads in alts:
            w = 1.0 if sure else 0.25 if owned else 0.5
        elif sure or owned:
            w = 0.0
        elif total and any(sum(a.values()) == total for a in alts):
            w = 0.2
        else:
            w = 0.02
        if w:
            out.append((lid, w))
    if not out:   # pad table wrong or settlement odd: keep the whole family
        out = [(lid, 0.01) for lid, lay in layouts.items()
               if lay["economy"] == economy]
    return out


def short_name(lid, layouts):
    n = layouts[lid]["name"]
    return n.replace("Agriculture", "Agri").replace("Extraction", "Ext") \
        .replace("Industrial", "Ind").replace("Military", "Mil") \
        .replace("High Tech", "HT").replace("Tourist", "Tour") \
        .replace(" ", "")


def tag(lid, layouts):
    return "%s(%s)" % (short_name(lid, layouts),
                       MARK.get(layouts[lid]["size"], "?"))


def guess_text(cands, layouts, n=3):
    wsum = sum(w for _, w in cands)
    txt = ", ".join("%s%s" % (tag(l, layouts), "" if len(cands) == 1 else
                              " %d%%" % round(100 * w / wsum))
                    for l, w in cands[:n])
    return txt + (" +%d" % (len(cands) - n) if len(cands) > n else "")


def aim(cands, scores, layouts):
    """Size marker(s) of the best-yield layouts among the likely ones."""
    top = max(w for _, w in cands)
    likely = [l for l, w in cands if w >= 0.3 * top]
    marks = {MARK.get(layouts[l]["size"], "?") for l in likely}
    best = max(scores[l][0] for l in likely)
    good = {MARK.get(layouts[l]["size"], "?") for l in likely
            if scores[l][0] >= best - 1e-9}
    return "any" if good == marks else "/".join(sorted(good, key=len))


def survey(names, layouts):
    from waypoint_route import system_stations
    from settlement_finder import pad_sig
    for name in names:
        sts = [s for s in system_stations(name)
               if s.get("type") == "Settlement"]
        print("\n== %s: %d settlement(s)" % (name, len(sts)))
        print("   %-34s %-22s %-8s %s" % ("settlement", "body", "pads",
                                          "layout(size marker) by pads"))
        sts.sort(key=lambda s: (s.get("primary_economy") or "", pad_sig(s),
                                s.get("body_name") or "", s["name"]))
        eco = None
        for st in sts:
            if st.get("primary_economy") != eco:
                eco = st.get("primary_economy")
                print("  %s" % eco)
            pads = {k: st.get(f) or 0 for k, f in (
                ("L", "large_pads"), ("M", "medium_pads"),
                ("S", "small_pads"))}
            cands = candidates({k: v for k, v in pads.items() if v}, eco,
                               layouts)
            cands.sort(key=lambda c: -c[1])
            print("   %-34s %-22s %-8s %s" % (
                st["name"][:34], (st.get("body_name") or "")
                .replace(name, "").strip()[:22], pad_sig(st),
                guess_text(cands, layouts, 5) if cands else "-"))
    print("\nIn game, note the size marker next to each name (- tiny, "
          "+ small, ++ medium) and compare.")


# ---------------------------------------------------------------- views --
def print_card(items, layouts, scores, factors=None, local=None):
    factors = factors or [{}] * len(items)
    for it, fac in zip(items, factors):
        loc = (local or {}).get(it["key"])
        print("%s%s - %s, %s" % (it["name"], " (%s)" % loc if loc and
                                 key(loc) != it["key"] else "", it["type"],
                                 "used in %d blueprint(s): keep" % it["used"]
                                 if it["used"] else "no blueprint: sell it"))
        print("  drops in: %s" % (", ".join(it["locations"]) or
                                  "not lootable (mission reward / trade only)"))
        if fac:
            print("  your loot (journals%s): %s" % (
                "" if it["type"] == "Data" else ", since %s" % LOCKERS_SINCE,
                ", ".join("%s %d/%d visits x%.1f" % (e, h, n, f) for e, (
                    f, h, n) in sorted(fac.items(), key=lambda kv: -kv[1][0])
                    if n)))
    ranked = sorted(scores.items(), key=lambda kv: -kv[1][0])
    ranked = [kv for kv in ranked if kv[1][0] > 0]
    if not ranked:
        print("\nNo settlement layout holds it.")
        return
    unit = "data ports" if all(i["type"] == "Data" for i in items) else \
        "buildings" if all(i["type"] == "Goods" for i in items) else "score"
    if any(factors):
        unit += " x your loot factor"
    print("\nBest layouts (%s; OMG maps; pads from the images "
          "+ Spansh census, '?' = unsure):" % (unit if len(items) == 1 else
                              "score, each item scaled to its best layout"))
    for lid, (score, ys) in ranked[:12]:
        lay = layouts[lid]
        print("  %-15s %-6s %-9s %5s   %s" % (
            lay["name"], lay["size"], lay["pads"],
            ("%d" % score) if len(items) == 1 and not any(factors)
            else "%.1f" % score,
            "  ".join("%s %d" % (it["name"][:18], y)
                      for it, y in zip(items, ys)) if len(items) > 1 else
            ", ".join("%s %d" % kv for kv in sorted(
                (lay["data_ports"] if items[0]["type"] == "Data"
                 else lay["buildings"]).items())
                if kv[0] in items[0]["codes"])))


def print_locker(items, folder):
    path = os.path.join(folder, "ShipLocker.json")
    try:
        data = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        sys.exit("No ShipLocker.json in %s (journal folder; --journal)" % folder)
    sell, keep, unknown = [], [], []
    for group in ("Items", "Data"):
        for e in data.get(group) or []:
            name = e.get("Name_Localised") or e.get("Name")
            it = items.get(key(name)) or items.get(key(e.get("Name", "")))
            row = (name, e.get("Count", 0), it)
            (unknown if not it else keep if it["used"] else sell).append(row)
    print("Ship locker (%s)\n" % data.get("timestamp", "?"))
    print("No blueprint uses them - sell to a bartender:")
    for n, c, it in sorted(sell, key=lambda r: -r[1]):
        print("  %4d  %-34s %s" % (c, n, it["type"]))
    print("\nUsed by engineer blueprints - keep:")
    for n, c, it in sorted(keep, key=lambda r: -r[2]["used"]):
        print("  %4d  %-34s %-5s %d blueprint(s)" % (c, n, it["type"],
                                                     it["used"]))
    if unknown:
        print("\nNot in the Inara list: %s" % ", ".join(
            "%s ×%d" % (n, c) for n, c, _ in unknown))


# ----------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("items", nargs="?", default="",
                    help="comma list of items, e.g. 'Weapon Schematic, "
                         "Patrol Routes' (partial names accepted)")
    ap.add_argument("--ref", default=None,
                    help="reference system (default: current system from "
                         "the journal, else %s)" % DEFAULT_REF)
    ap.add_argument("--radius", type=float, default=40.0)
    ap.add_argument("--pad", choices=("S", "M", "L"), default=None,
                    help="your ship's pad size: leave out settlements "
                         "without a pad that fits")
    ap.add_argument("--max-gravity", type=float, default=None)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--systems", type=int, default=40,
                    help="war check: how many best systems to look up")
    ap.add_argument("--info", action="store_true",
                    help="item card and best layouts only (no Spansh)")
    ap.add_argument("--locker", action="store_true",
                    help="read ShipLocker.json: what to sell, what to keep")
    ap.add_argument("--journal", default=None, help="journal folder")
    ap.add_argument("--no-history", action="store_true",
                    help="ignore your loot history (journals)")
    ap.add_argument("--survey", default=None, metavar="SYSTEMS",
                    help="list the settlements of these systems (comma "
                         "list) with their pads and possible layouts - for "
                         "checking the layout table in game")
    args = ap.parse_args()

    items_db = load_items()
    from pp_trade_routes import JOURNAL_DIR
    folder = args.journal or JOURNAL_DIR
    if args.locker:
        print_locker(items_db, folder)
        return
    if args.survey:
        survey([s.strip() for s in args.survey.split(",") if s.strip()],
               load_layouts())
        return
    if not args.items:
        ap.error("give at least one item (or --locker / --survey)")
    visits, local = (None, {}) if args.no_history else load_history(folder)
    wanted = [resolve(q, items_db, local) for q in args.items.split(",")
              if q.strip()]
    layouts = load_layouts()
    factors = [eco_factors(it, visits) for it in wanted]
    scores = layout_scores(wanted, layouts, factors)
    print_card(wanted, layouts, scores, factors, local)
    if args.info:
        return
    if all(s == 0 for s, _ in scores.values()):
        return

    from settlement_finder import fetch_settlements, pad_sig, WAR_STATES
    from waypoint_route import journal_state, lookup
    ref = args.ref
    if not ref and os.path.isdir(folder):
        ref = journal_state(folder)[0]
    ref = ref or DEFAULT_REF
    economies = sorted({layouts[l]["economy"] for l, (s, _) in scores.items()
                        if s > 0})
    sets = fetch_settlements(ref, args.radius, economies)
    rows = []
    for st in sets:
        pads = {k: st.get(f) or 0 for k, f in (("L", "large_pads"),
                ("M", "medium_pads"), ("S", "small_pads"))}
        pads = {k: v for k, v in pads.items() if v}
        if args.pad and not any(PAD_RANK[k] >= PAD_RANK[args.pad]
                                for k in pads):
            continue
        if args.max_gravity is not None and \
                (st.get("body_gravity") or 0) > args.max_gravity:
            continue
        cands = candidates(pads, st.get("primary_economy"), layouts)
        if not cands:
            continue
        wsum = sum(w for _, w in cands)
        exp = sum(scores[l][0] * w for l, w in cands) / wsum
        if exp <= 0:
            continue
        cands.sort(key=lambda c: -c[1])
        rows.append((exp, st, pad_sig(st), cands))
    print("\n%d settlement(s) within %.0f ly of %s may hold it%s." % (
        len(rows), args.radius, ref,
        " (pad %s+)" % args.pad if args.pad else ""))
    if not rows:
        return

    # War check, by system (one Spansh call each), best systems first.
    by_sys = defaultdict(list)
    for r in rows:
        by_sys[r[1]["system_name"]].append(r)
    order = sorted(by_sys, key=lambda s: -max(r[0] for r in by_sys[s]))
    info, dropped = {}, 0
    for name in order[:args.systems]:
        rec = lookup(name)
        war = {f["name"] for f in rec.get("minor_faction_presences") or []
               if f.get("state") in WAR_STATES}
        info[name] = (rec, war)
    ok = []
    for r in rows:
        name = r[1]["system_name"]
        if name not in info:
            continue
        if r[1].get("controlling_minor_faction") in info[name][1]:
            dropped += 1
            continue
        ok.append(r)
    ok.sort(key=lambda r: (-round(r[0], 2), r[1].get("distance") or 0,
                           r[1].get("distance_to_arrival") or 0))
    unit = ("ports" if all(i["type"] == "Data" for i in wanted) else
            "bldgs" if all(i["type"] == "Goods" for i in wanted) else "score")
    if len(wanted) > 1 or any(factors):
        unit = "score"
    print("War check on the %d best systems: %d settlement(s) left out "
          "(faction at war). Expected yield = average over the layouts the "
          "economy + pads allow, weighted by how well the pads match.\n"
          % (min(len(order), args.systems), dropped))
    print(" #  %-5s %-30s %-24s %6s  %-8s %-40s %-4s %5s %6s  %s" % (
        unit, "settlement", "system", "ly", "pads", "layout guess (size)",
        "aim", "g", "ls", "government / power"))
    for i, (exp, st, sig, cands) in enumerate(ok[:args.top], 1):
        rec = info[st["system_name"]][0]
        guess = guess_text(cands, layouts)
        print("%2d  %5.1f %-30s %-24s %6.1f  %-8s %-40s %-4s %5.2f %6d  "
              "%s / %s" % (
            i, exp, st["name"][:30], st["system_name"][:24],
            st.get("distance") or 0, sig, guess[:40],
            aim(cands, scores, layouts),
            st.get("body_gravity") or 0, st.get("distance_to_arrival") or 0,
            rec.get("government") or "?",
            (rec.get("controlling_power") or "-")))
    # Systems with several good settlements: one trip, several landings.
    multi = defaultdict(list)
    for r in ok:
        multi[r[1]["system_name"]].append(r)
    multi = sorted(((s, rs) for s, rs in multi.items() if len(rs) > 1),
                   key=lambda kv: -sum(r[0] for r in kv[1]))
    if multi:
        print("\nSeveral in one system (total expected yield):")
        for s, rs in multi[:5]:
            print("  %-26s %5.1f ly  %d settlements, total %.1f" % (
                s, rs[0][1].get("distance") or 0, len(rs),
                sum(r[0] for r in rs)))
    print("\naim = the size marker to look for next to the settlement's name "
          "in game (- tiny, + small, ++ medium): it picks the best layout "
          "among those the pads allow; 'any' = they all yield the same.")
    other = sorted({o for it in wanted for o in it["other"]})
    if other:
        print("\nAlso from: %s." % ", ".join(other))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
