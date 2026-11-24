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
The layout guess is shown with each settlement; fly over it to confirm.

Data: https://spansh.co.uk (EDDN-fed; faction states as of the last visit
by someone running an EDDN client).

Usage examples:
  python tools/material_finder.py "Manufacturing Instructions"
  python tools/material_finder.py "weapon schem" --ref Cubeo --radius 50
  python tools/material_finder.py "Patrol Routes,Weapon Test Data" --pad L
  python tools/material_finder.py "Ionised Gas" --info     # offline card
  python tools/material_finder.py --locker                  # what to sell
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
                "name": row["Item"], "type": row["Type"],
                "used": int(row["Used"] or 0), "locations": locs,
                "codes": codes,
                "other": [l for l in locs if l in NOT_SETTLEMENT]}
    return items


def load_layouts():
    with open(LAYOUTS_FILE, encoding="utf-8") as fh:
        return json.load(fh)["layouts"]


def resolve(query, items):
    k = key(query)
    if k in items:
        return items[k]
    hits = [v for kk, v in items.items() if k in kk]
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


# -------------------------------------------------------------- scoring --
def layout_yield(item, lay):
    """Ports (data) or buildings (goods) where the item drops."""
    source = lay["data_ports"] if item["type"] == "Data" else lay["buildings"]
    n = sum(source.get(c, 0) for c in item["codes"] if c != "*")
    if "*" in item["codes"]:
        n = max(n, 1)
    return n


def layout_scores(items, layouts):
    """{layout_id: (score, [per-item yield])}, items scaled to their best."""
    per = {lid: [layout_yield(it, lay) for it in items]
           for lid, lay in layouts.items()}
    best = [max(per[lid][i] for lid in per) or 1 for i in range(len(items))]
    out = {}
    for lid, ys in per.items():
        score = ys[0] if len(items) == 1 else sum(
            y / b for y, b in zip(ys, best))
        out[lid] = (score, ys)
    return out


def parse_pads(sig):
    """'L1 M2?' -> ({'L': 1, 'M': 2}, sure?)"""
    pads = {m.group(1): int(m.group(2))
            for m in re.finditer(r"([LMS])(\d+)", sig or "")}
    return pads, "?" not in (sig or "?")


def candidates(st_pads, economy, layouts):
    """Layouts a settlement can be, with a weight from the pad match."""
    out = []
    total = sum(st_pads.values())
    for lid, lay in layouts.items():
        if lay["economy"] != economy:
            continue
        lp, sure = parse_pads(lay["pads"])
        if lp == st_pads:
            w = 1.0
        elif sum(lp.values()) == total and total:
            w = 0.4 if not sure else 0.15
        else:
            w = 0.0 if sure else 0.05
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


# ---------------------------------------------------------------- views --
def print_card(items, layouts, scores):
    for it in items:
        print("%s - %s, %s" % (it["name"], it["type"],
                               "used in %d blueprint(s): keep" % it["used"]
                               if it["used"] else "no blueprint: sell it"))
        print("  drops in: %s" % (", ".join(it["locations"]) or
                                  "not lootable (mission reward / trade only)"))
    ranked = sorted(scores.items(), key=lambda kv: -kv[1][0])
    ranked = [kv for kv in ranked if kv[1][0] > 0]
    if not ranked:
        print("\nNo settlement layout holds it.")
        return
    unit = "data ports" if all(i["type"] == "Data" for i in items) else \
        "buildings" if all(i["type"] == "Goods" for i in items) else "score"
    print("\nBest layouts (%s; OMG maps; pads from the images "
          "+ Spansh census, '?' = unsure):" % (unit if len(items) == 1 else
                              "score, each item scaled to its best layout"))
    for lid, (score, ys) in ranked[:12]:
        lay = layouts[lid]
        print("  %-15s %-6s %-9s %5s   %s" % (
            lay["name"], lay["size"], lay["pads"],
            ("%d" % score) if len(items) == 1 else "%.2f" % score,
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
    args = ap.parse_args()

    items_db = load_items()
    from pp_trade_routes import JOURNAL_DIR
    folder = args.journal or JOURNAL_DIR
    if args.locker:
        print_locker(items_db, folder)
        return
    if not args.items:
        ap.error("give at least one item (or --locker)")
    wanted = [resolve(q, items_db) for q in args.items.split(",") if q.strip()]
    layouts = load_layouts()
    scores = layout_scores(wanted, layouts)
    print_card(wanted, layouts, scores)
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
    if len(wanted) > 1:
        unit = "score"
    print("War check on the %d best systems: %d settlement(s) left out "
          "(faction at war). Expected yield = average over the layouts the "
          "economy + pads allow, weighted by how well the pads match.\n"
          % (min(len(order), args.systems), dropped))
    print(" #  %-5s %-30s %-24s %6s  %-8s %-36s %5s %6s  %s" % (
        unit, "settlement", "system", "ly", "pads", "layout guess", "g",
        "ls", "government / power"))
    for i, (exp, st, sig, cands) in enumerate(ok[:args.top], 1):
        rec = info[st["system_name"]][0]
        top = cands[:3]
        wsum = sum(w for _, w in cands)
        guess = ", ".join("%s%s" % (short_name(l, layouts),
                                    "" if len(cands) == 1 else
                                    " %d%%" % round(100 * w / wsum))
                          for l, w in top) + (" +%d" % (len(cands) - 3)
                                              if len(cands) > 3 else "")
        print("%2d  %5.1f %-30s %-24s %6.1f  %-8s %-36s %5.2f %6d  %s / %s" % (
            i, exp, st["name"][:30], st["system_name"][:24],
            st.get("distance") or 0, sig, guess[:36],
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
    other = sorted({o for it in wanted for o in it["other"]})
    if other:
        print("\nAlso from: %s." % ", ".join(other))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
