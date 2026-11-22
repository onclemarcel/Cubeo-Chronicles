#!/usr/bin/env python3
"""
waypoint_route.py - route with N intermediate stops that meet given criteria.

From a start system (default: current system, from the journal) to a
destination, optionally through one or more mandatory systems (--via), pick
--stops systems that satisfy the criteria and order them so the trip costs
as few jumps as possible.

Criteria:
  * system filters, applied by Spansh: controlling power (--power), power
    states (--states), plus any raw Spansh system filter (--filter JSON);
  * what the system must contain (--need):
      megaship        a megaship is known there (see "Megaships" below)
      station:<type>  a station of that Spansh type, e.g. "station:Outpost"
      any             no extra condition - the system filters are enough
  * systems that never count as a stop (--exclude; default Cubeo for
    megaships: Aisling's capital paid 0 merits for uplink scans, Powerplay
    Missions.md card 4.9). Excluded systems can still be the start, the
    destination or a --via, but never count towards --stops.

The start, the destination and the --via systems count as stops when they
meet the criteria themselves (e.g. a megaship at the via system).

Megaships - Spansh lists only DOCKABLE megaships. Ordinary megaships, the
ones with a datalink to scan, are missing there, so a system is a megaship
stop if any of these sources knows one:
  spansh   a dockable megaship in Spansh's station list
  journal  your own journals: FSSSignalDiscovered "Megaship" signals, and
           DataScanned $Datascan_ShipUplink; (an uplink scanned there)
  known    systems where a scan paid merits (built-in list, Powerplay
           Missions.md card 4.9), plus --known "Sys A,Sys B"
Megaships can move at the Thursday tick: a sighting older than the last tick
is flagged "pre-tick". --include-unknown also lets systems with no evidence
fill the route (flagged "check on arrival").

Jumps are estimated as ceil(distance / (jump range x 0.9)) per leg - the
real plot depends on star density. Plot each leg in the galaxy map.

Data: https://spansh.co.uk (public API, EDDN-fed, power states can be a few
days old).

Usage examples:
  python tools/waypoint_route.py --to Cubeo --via "LHS 378" --stops 8
  python tools/waypoint_route.py --from Tripitaka --to Cubeo \\
      --via "LHS 378" --stops 8 --jump 45 --detour 40
  python tools/waypoint_route.py --to Cubeo --stops 5 --need any \\
      --states Fortified          # 5 Fortified Aisling systems on the way
  python tools/waypoint_route.py --to Cubeo --stops 4 --need station:Outpost
  python tools/waypoint_route.py --to Cubeo --stops 6 --power "" \\
      --states "" --need any --filter '{"allegiance":{"value":["Empire"]}}'
"""

import argparse
import glob
import json
import math
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

from pp_trade_routes import JOURNAL_DIR

API = "https://spansh.co.uk/api/systems/search"
UA = {"Content-Type": "application/json",
      "User-Agent": "cubeo-chronicles-waypoint-route/1.0"}
CONTROL_STATES = "Exploited,Fortified,Stronghold"
JUMP_EFFICIENCY = 0.9   # real legs rarely use the full jump range
# Extra cost, in jumps, of a stop by evidence: the route only takes a stale
# or unconfirmed megaship when it saves more jumps than this.
PENALTY = {"fresh": 0.0, "pre-tick": 1.0, "unknown": 3.0}
# Uplink scans that paid merits (Powerplay Missions.md card 4.9, 1 + 30 Oct
# 2026). Megaships may move at a tick - treated as pre-tick evidence.
KNOWN_UPLINKS = {
    "Primi": "2026-10-30", "Lambda-1 Tucanae": "2026-10-30",
    "Osane": "2026-10-30", "Karsuki Ti": "2026-10-30",
    "Fire Fade": "2026-10-30", "HIP 7142": "2026-10-30",
    "Jaroahy": "2026-10-30", "Ehlanda": "2026-10-01",
}


# ---------------------------------------------------------------- journal --
def journal_files(folder):
    return sorted(glob.glob(os.path.join(folder, "Journal.*.log")),
                  key=os.path.getmtime)


def journal_state(folder):
    """Current system and max jump range from the latest journals."""
    system, jump = None, None
    for path in reversed(journal_files(folder)[-5:]):
        try:
            with open(path, encoding="utf-8") as fh:
                lines = fh.readlines()
        except OSError:
            continue
        for line in reversed(lines):
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            name = ev.get("event")
            if system is None and name in ("Location", "FSDJump",
                                           "CarrierJump"):
                system = ev.get("StarSystem")
            if jump is None and name == "Loadout":
                jump = ev.get("MaxJumpRange")
            if system and jump:
                return system, jump
    return system, jump


def journal_megaships(folder):
    """{system: (timestamp, label)} for megaships seen or scanned."""
    seen, names, current = {}, {}, None
    keys = ('"FSSSignalDiscovered"', '"DataScanned"', '"FSDJump"',
            '"Location"', '"CarrierJump"')
    for path in journal_files(folder):
        try:
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    if not any(k in line for k in keys):
                        continue
                    try:
                        ev = json.loads(line)
                    except ValueError:
                        continue
                    name, ts = ev.get("event"), ev.get("timestamp", "")
                    if name in ("FSDJump", "Location", "CarrierJump"):
                        current = ev.get("StarSystem")
                        names[ev.get("SystemAddress")] = current
                    elif name == "FSSSignalDiscovered" and \
                            ev.get("SignalType") == "Megaship":
                        sys_name = names.get(ev.get("SystemAddress"), current)
                        label = ev.get("SignalName_Localised") or \
                            ev.get("SignalName") or "megaship"
                        note(seen, sys_name, ts, "seen: " + label)
                    elif name == "DataScanned" and \
                            ev.get("Type") == "$Datascan_ShipUplink;":
                        note(seen, current, ts, "uplink scanned")
        except OSError:
            continue
    return seen


def note(store, system, ts, label):
    if system and (system not in store or ts >= store[system][0]):
        store[system] = (ts, label)


# ----------------------------------------------------------------- spansh --
def post(body):
    req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                 headers=UA)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def lookup(name):
    data = post({"filters": {"name": {"value": name}}, "size": 5})
    for r in data.get("results", []):
        if r["name"].lower() == name.lower():
            return r
    sys.exit("System not found on Spansh: %s" % name)


def fetch_sphere(center, radius, filters):
    found, page, size = [], 0, 100
    body = {"filters": dict(filters, distance={"min": "0",
                                               "max": str(radius)}),
            "reference_coords": {"x": center[0], "y": center[1],
                                 "z": center[2]},
            "size": size, "sort": [{"distance": {"direction": "asc"}}]}
    while True:
        body["page"] = page
        data = post(body)
        batch = data.get("results", [])
        found.extend(batch)
        page += 1
        if not batch or len(found) >= data.get("count", 0):
            return found


def fetch_corridor(points, detour, filters):
    """Systems matching filters within `detour` ly of the polyline."""
    systems = {}
    for a, b in zip(points, points[1:]):
        length = dist(a, b)
        steps = max(1, int(math.ceil(length / detour)))
        radius = detour * 1.15 + length / steps / 2
        for i in range(steps):
            t = (i + 0.5) / steps
            c = tuple(a[k] + (b[k] - a[k]) * t for k in range(3))
            for r in fetch_sphere(c, radius, filters):
                systems[r["id64"]] = r
    return [s for s in systems.values()
            if min(seg_dist(xyz(s), a, b)
                   for a, b in zip(points, points[1:])) <= detour]


# ---------------------------------------------------------------- geometry --
def xyz(s):
    return (s["x"], s["y"], s["z"])


def dist(a, b):
    return math.sqrt(sum((a[k] - b[k]) ** 2 for k in range(3)))


def seg_dist(p, a, b):
    ab = [b[k] - a[k] for k in range(3)]
    n = sum(v * v for v in ab)
    t = 0.0 if n == 0 else max(0.0, min(1.0, sum(
        (p[k] - a[k]) * ab[k] for k in range(3)) / n))
    return dist(p, tuple(a[k] + ab[k] * t for k in range(3)))


# ------------------------------------------------------------------ route --
class Planner:
    """Orders stops by estimated jumps; fixed nodes are never dropped."""

    def __init__(self, coords, jump, weight, fixed):
        self.coords, self.reach, self.memo = coords, jump * JUMP_EFFICIENCY, {}
        self.weight, self.fixed = weight, set(fixed)

    def leg(self, a, b):
        key = (a, b) if a < b else (b, a)
        if key not in self.memo:
            d = dist(self.coords[a], self.coords[b])
            self.memo[key] = math.ceil(d / self.reach) + d / 1e4
        return self.memo[key]

    def cost(self, path):
        return sum(self.leg(a, b) for a, b in zip(path, path[1:])) + \
            sum(self.weight.get(n, 0.0) for n in path if n not in self.fixed)

    def insert_cost(self, path, node):
        best = None
        for i in range(1, len(path)):
            delta = self.leg(path[i - 1], node) + self.leg(node, path[i]) - \
                self.leg(path[i - 1], path[i]) + self.weight.get(node, 0.0)
            if best is None or delta < best[0]:
                best = (delta, i)
        return best

    def improve(self, path, pool, scored):
        """2-opt, relocate and swap-with-pool until nothing improves."""
        better = True
        while better:
            better = False
            n = len(path)
            for i in range(1, n - 2):           # 2-opt, ends fixed
                for j in range(i + 1, n - 1):
                    new = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                    if self.cost(new) < self.cost(path) - 1e-9:
                        path, better = new, True
            for i in range(1, len(path) - 1):   # relocate one node
                node = path[i]
                rest = path[:i] + path[i + 1:]
                if node in (path[0], path[-1]):
                    continue
                delta, j = self.insert_cost(rest, node)
                new = rest[:j] + [node] + rest[j:]
                if self.cost(new) < self.cost(path) - 1e-9:
                    path, better = new, True
            for i in range(1, len(path) - 1):   # swap a stop with the pool
                if path[i] not in scored or path[i] in self.fixed:
                    continue
                rest = path[:i] + path[i + 1:]
                base = self.cost(rest)
                old = self.cost(path) - base
                best = None
                for cand in pool:
                    if cand in path:
                        continue
                    delta, j = self.insert_cost(rest, cand)
                    if delta < old - 1e-9 and (best is None or
                                               delta < best[0]):
                        best = (delta, j, cand)
                if best:
                    delta, j, cand = best
                    path = rest[:j] + [cand] + rest[j:]
                    better = True
                    break
        return path

    def plan(self, fixed, pool, needed, scored):
        path = list(fixed)
        free = [c for c in pool if c not in path]
        for _ in range(needed):
            if not free:
                break
            best = min(((self.insert_cost(path, c), c) for c in free),
                       key=lambda x: x[0][0])
            (delta, i), c = best
            path.insert(i, c)
            free.remove(c)
        return self.improve(path, pool, scored)


# ------------------------------------------------------------------- main --
def last_tick(now):
    """Most recent Thursday 07:00 UTC (weekly Powerplay tick)."""
    t = now.replace(hour=7, minute=0, second=0, microsecond=0)
    t -= timedelta(days=(t.weekday() - 3) % 7)
    return t if t <= now else t - timedelta(days=7)


def evidence_for(s, args, jmega, tick):
    """(label, tier) describing why s qualifies, or None.

    tier: "fresh", "pre-tick" (seen before the last tick) or "unknown".
    """
    need = args.need
    if need == "any":
        return ("matches filters", "fresh")
    stations = s.get("stations") or []
    if need.startswith("station:"):
        kind = need.split(":", 1)[1].lower()
        hits = [st["name"] for st in stations
                if (st.get("type") or "").lower() == kind]
        return ("%s: %s" % (need[8:], ", ".join(hits[:3])), True) \
            if hits else None
    found = []
    for st in stations:
        if st.get("type") == "Mega ship":
            found.append(("spansh: %s (dockable)" % st["name"],
                          st.get("updated_at") or ""))
    if s["name"] in jmega:
        ts, label = jmega[s["name"]]
        found.append(("journal %s, %s" % (ts[:10], label), ts))
    if s["name"] in args.known:
        ts = args.known[s["name"]]
        found.append(("known: paid scan %s" % ts if ts else "known (--known)",
                      ts or datetime.now(timezone.utc).isoformat()))
    if not found:
        return ("NO DATA - check on arrival", "unknown") \
            if args.include_unknown else None
    label, ts = max(found, key=lambda f: f[1])
    if ts >= tick.strftime("%Y-%m-%dT%H:%M:%S"):
        return (label, "fresh")
    return (label + "  [pre-tick]", "pre-tick")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--from", dest="start", default=None,
                    help="start system (default: current, from journal)")
    ap.add_argument("--to", required=True, help="destination system")
    ap.add_argument("--via", action="append", default=[],
                    help="mandatory system on the way (repeatable)")
    ap.add_argument("--stops", type=int, required=True,
                    help="number of qualifying systems to visit")
    ap.add_argument("--need", default="megaship",
                    help="megaship | station:<type> | any (default megaship)")
    ap.add_argument("--power", default="Aisling Duval",
                    help="controlling power ('' = no power filter)")
    ap.add_argument("--states", default=CONTROL_STATES,
                    help="comma list of power states ('' = any; default "
                         "%s)" % CONTROL_STATES)
    ap.add_argument("--filter", default=None, metavar="JSON",
                    help="extra raw Spansh system filters, merged in")
    ap.add_argument("--exclude", default=None,
                    help="comma list of systems that never count as a stop "
                         "(default: Cubeo with --need megaship)")
    ap.add_argument("--known", default="",
                    help="comma list of systems with a known megaship")
    ap.add_argument("--include-unknown", action="store_true",
                    help="megaship mode: systems with no evidence may fill "
                         "the route (to check on arrival)")
    ap.add_argument("--fresh-only", action="store_true",
                    help="megaship mode: ignore pre-tick evidence")
    ap.add_argument("--jump", type=float, default=None,
                    help="jump range in ly (default: current ship, journal, "
                         "else 40)")
    ap.add_argument("--detour", type=float, default=30.0,
                    help="max distance of a stop from the straight route, "
                         "ly (default 30)")
    ap.add_argument("--journal-dir", default=JOURNAL_DIR)
    args = ap.parse_args()

    j_sys, j_jump = journal_state(args.journal_dir)
    args.start = args.start or j_sys
    if not args.start:
        ap.error("no --from given and no journal found")
    args.jump = args.jump or j_jump or 40.0
    if args.exclude is None:
        args.exclude = "Cubeo" if args.need == "megaship" else ""
    excluded = {s.strip().lower() for s in args.exclude.split(",")
                if s.strip()}
    known = dict(KNOWN_UPLINKS) if args.need == "megaship" else {}
    known.update({k.strip(): "" for k in args.known.split(",") if k.strip()})
    args.known = known

    filters = {}
    if args.power:
        filters["controlling_power"] = {"value": [args.power]}
    states = [s.strip() for s in args.states.split(",") if s.strip()]
    if states:
        filters["power_state"] = {"value": states}
    if args.filter:
        filters.update(json.loads(args.filter))

    ends = [lookup(n) for n in [args.start] + args.via + [args.to]]
    points = [xyz(s) for s in ends]
    print("Route %s, %d stop(s) [%s], power %s %s, jump %.1f ly, detour "
          "<= %.0f ly" % (" -> ".join(s["name"] for s in ends), args.stops,
                          args.need, args.power or "any",
                          "/".join(states) or "any state", args.jump,
                          args.detour))
    candidates = fetch_corridor(points, args.detour, filters)
    jmega = journal_megaships(args.journal_dir) \
        if args.need == "megaship" else {}
    tick = last_tick(datetime.now(timezone.utc))

    info, coords = {}, {}
    for s in ends + candidates:
        coords[s["name"]] = xyz(s)
        info[s["name"]] = s
    matching = {c["name"]: c for c in candidates}
    scored = {}
    for name, s in matching.items():   # ends count only if they match too
        if name.lower() in excluded:
            continue
        ev = evidence_for(s, args, jmega, tick)
        if ev and (ev[1] == "fresh" or not args.fresh_only):
            scored[name] = ev
    print("%d system(s) match the filters in the corridor, %d qualify as "
          "stops (%d with evidence from this week)%s\n" % (
              len(candidates), len(scored),
              sum(1 for v in scored.values() if v[1] == "fresh"),
              "" if args.need != "megaship" else
              ", journal megaship sightings: %d" % len(jmega)))

    fixed = [s["name"] for s in ends]
    # A fixed stop with no evidence is a bonus to check, not a counted stop.
    bonus = {n for n in fixed if scored.get(n, ("", ""))[1] == "unknown"}
    for n in bonus:
        del scored[n]
    have = sum(1 for n in fixed if n in scored)
    weight = {n: PENALTY[v[1]] for n, v in scored.items()}
    planner = Planner(coords, args.jump, weight, fixed)
    pool = [n for n in scored if n not in fixed]
    path = planner.plan(fixed, pool, args.stops - have, set(scored))
    got = sum(1 for n in path if n in scored)

    total_ly, total_j, count = 0.0, 0, 0
    for i, name in enumerate(path):
        s = info[name]
        mark = "   "
        if name in scored:
            count += 1
            mark = "%2d." % count
        role = "start" if i == 0 else "end" if i == len(path) - 1 else \
            "via" if name in args.via else ""
        if i:
            d = dist(coords[path[i - 1]], coords[name])
            j = int(planner.leg(path[i - 1], name))
            total_ly += d
            total_j += j
            leg = "%6.1f ly ~%2d j" % (d, j)
        else:
            leg = " " * 15
        print("%s %s  %-30s %-5s %-10s %s" % (
            mark, leg, name, role, s.get("power_state") or "-",
            scored[name][0] if name in scored else
            "(excluded)" if name.lower() in excluded else
            "no data - check on arrival (bonus, not counted)"
            if name in bonus else ""))
    print("\n%d / %d stops, %.0f ly, ~%d jumps (estimate at %.0f ly/jump)"
          % (got, args.stops, total_ly, total_j, args.jump * JUMP_EFFICIENCY))
    if got < args.stops:
        print("Not enough qualifying systems - try a larger --detour%s." % (
            ", --include-unknown or --known" if args.need == "megaship"
            else ""))
    if args.need == "megaship" and any(scored[n][1] == "pre-tick"
                                       for n in path if n in scored):
        print("[pre-tick] = last seen before the %s tick: the megaship may "
              "have moved." % tick.strftime("%d %b"))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
