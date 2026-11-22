#!/usr/bin/env python3
"""
waypoint_route.py - route with N intermediate stops that meet given criteria.

From a start system (default: current system, from the journal), optionally
through mandatory systems (--via), to a destination (--to; leave it out to
end wherever the last stop is), pick --stops stops that satisfy the criteria
and order them for the fewest jumps. Also the library behind pp_week.py.

Criteria:
  * system filters, applied by Spansh: controlling power (--power), power
    states (--states), plus any raw Spansh system filter (--filter JSON);
  * what the system must contain (--need):
      megaship        megaships to scan (see "Megaships" below) - a system
                      with 3 megaships counts as 3 stops
      station:<type>  a station of that Spansh type, e.g. "station:Outpost"
      any             no extra condition - the system filters are enough
  * systems that never count as a stop (--exclude; default Cubeo for
    megaships: Aisling's capital paid 0 merits for uplink scans, Powerplay
    Missions.md card 4.9).

Megaships - Spansh lists only DOCKABLE megaships, not the scannable ones.
Sources, best first:
  inara    Inara "Search nearest", station type "Bulk Cruiser (Scannable
           megaship)", power Aisling Duval (Controlled), states Exploited/
           Fortified/Stronghold: select the whole page, paste it into
           tools/inara_megaships.txt (default --inara file; git-ignored).
           "Seen" ages count from the file's save time.
  journal  your journals: FSSSignalDiscovered "Megaship" signals. Uplink
           scans made since the last tick (DataScanned) are subtracted
           from that system's count.
  known    systems where a scan paid merits (built-in list, card 4.9)
Megaships move at the Thursday tick: names seen since the tick count in
full; older sightings are flagged "pre-tick" and cost a 1-jump penalty.

Jumps are estimated as ceil(distance / (jump range x 0.9)) per leg - the
real plot depends on star density. Plot each leg in the galaxy map.

Data: https://spansh.co.uk (public API, EDDN-fed, power states can be a few
days old) and inara.cz (pasted by hand - Inara blocks scripts).

Usage examples:
  python tools/waypoint_route.py --via "LHS 378" --stops 8
  python tools/waypoint_route.py --to Cubeo --via "LHS 378" --stops 8 \\
      --jump 38 --detour 40
  python tools/waypoint_route.py --to Cubeo --stops 5 --need any \\
      --states Fortified          # 5 Fortified Aisling systems on the way
  python tools/waypoint_route.py --to Cubeo --stops 4 --need station:Outpost
"""

import argparse
import glob
import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

from pp_trade_routes import JOURNAL_DIR

API = "https://spansh.co.uk/api/systems/search"
STATIONS_API = "https://spansh.co.uk/api/stations/search"
UA = {"Content-Type": "application/json",
      "User-Agent": "cubeo-chronicles-waypoint-route/1.0"}
HERE = os.path.dirname(os.path.abspath(__file__))
INARA_FILE = os.path.join(HERE, "inara_megaships.txt")
CONTROL_STATES = "Exploited,Fortified,Stronghold"
JUMP_EFFICIENCY = 0.9   # real legs rarely use the full jump range
# Extra cost, in jumps, of a stop by evidence: the route only takes a stale
# or unconfirmed megaship when it saves more jumps than this.
PENALTY = {"fresh": 0.0, "pre-tick": 1.0, "unknown": 3.0}
ORDER_PENALTY = 1000.0  # a broken "A before B" constraint
END = "__END__"         # open route: free last leg
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
    """Current system, max jump range and ship name from the journals."""
    system, jump, ship = None, None, None
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
                ship = (ev.get("ShipName") or ev.get("Ship") or "").replace(
                    '"', "")
            if system and jump:
                return system, jump, ship
    return system, jump, ship


def journal_megaships(folder):
    """{system: {"names": {name: last seen}, "scans": [timestamps]}}."""
    out, names, current = {}, {}, None
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
                        label = (ev.get("SignalName_Localised") or
                                 ev.get("SignalName") or "").strip()
                        if sys_name and label:
                            rec = out.setdefault(sys_name, {"names": {},
                                                            "scans": []})
                            rec["names"][label] = max(ts, rec["names"].get(
                                label, ""))
                    elif name == "DataScanned" and current and \
                            ev.get("Type") == "$Datascan_ShipUplink;":
                        out.setdefault(current, {"names": {}, "scans": []})[
                            "scans"].append(ts)
        except OSError:
            continue
    return out


# ------------------------------------------------------------------ inara --
AGE_RE = re.compile(r"^(\d+|an?|one)\s+(minute|hour|day|week|month|year)s?"
                    r"\s+ago$", re.I)
UNIT = {"minute": 1 / 1440, "hour": 1 / 24, "day": 1, "week": 7,
        "month": 30, "year": 365}


def parse_inara(path, saved=None):
    """Inara 'Search nearest' page pasted as text.

    Returns (reference system or None, {system: {name: iso timestamp}},
    save time). Ages ("3 hours ago") count back from `saved` (default: the
    file's modification time).
    """
    saved = saved or datetime.fromtimestamp(os.path.getmtime(path),
                                            timezone.utc)
    with open(path, encoding="utf-8-sig") as fh:
        lines = [l.rstrip("\r\n") for l in fh]
    ref, ships = None, {}
    for i, line in enumerate(lines):
        if line.strip().lower() == "near star system" and i + 1 < len(lines):
            ref = ref or lines[i + 1].strip() or None
        cols = [c.strip() for c in re.split(r"\t| {2,}", line)]
        if len(cols) < 5:
            continue
        m = AGE_RE.match(cols[-1])
        if not m or not cols[-2].lower().endswith("ly"):
            continue
        qty = 1 if not m.group(1).isdigit() else int(m.group(1))
        seen = saved - timedelta(days=qty * UNIT[m.group(2).lower()])
        stamp = seen.strftime("%Y-%m-%dT%H:%M:%SZ")
        rec = ships.setdefault(cols[1], {})
        rec[cols[0]] = max(stamp, rec.get(cols[0], ""))
    return ref, ships, saved


# --------------------------------------------------------------- evidence --
def megaship_evidence(system, stations, jmega, inara, known, tick,
                      include_unknown=False):
    """(label, tier, count) for megaships still to scan in `system`.

    tier: "fresh" (seen since the tick), "pre-tick" or "unknown". None when
    nothing is known, or when this week's scans used up the known ones.
    """
    tick_s = tick.strftime("%Y-%m-%dT%H:%M:%S")
    seen = {}                        # NAME -> (timestamp, source, name)
    found = [(st["name"], st.get("updated_at") or "", "spansh")
             for st in stations or [] if st.get("type") == "Mega ship"]
    for src, names in (("journal", (jmega.get(system) or {}).get("names")),
                       ("inara", inara.get(system))):
        found += [(n, ts, src) for n, ts in (names or {}).items()]
    for n, ts, src in found:
        n = " ".join(n.split())             # journal names: double spaces
        key = n.upper()
        if key not in seen or ts > seen[key][0]:
            seen[key] = (ts, src, n)
    scans = sum(1 for ts in (jmega.get(system) or {}).get("scans", [])
                if ts >= tick_s)
    fresh = {n: v for n, v in seen.items() if v[0] >= tick_s}
    if fresh:
        left = len(fresh) - scans
        if left <= 0:
            return None
        pick, tier = fresh, "fresh"
    elif seen or system in known:
        left = max(len(seen), 1) - scans
        if left <= 0:
            return None
        pick, tier = seen, "pre-tick"
    elif include_unknown:
        return ("NO DATA - check on arrival", "unknown", 1)
    else:
        return None
    ordered = sorted(pick.items(), key=lambda kv: kv[1][0], reverse=True)
    if ordered:
        last = ordered[0][1]
        names = ", ".join(v[2] for _, v in ordered[:3])
        label = "%d to scan [%s %s]: %s" % (left, last[1], last[0][:10],
                                            names)
    else:
        label = "1 to scan [known: paid scan %s]" % known[system]
    if scans:
        label += " (%d scanned this week)" % scans
    if tier == "pre-tick":
        label += "  [pre-tick]"
    return (label, tier, left)


# ----------------------------------------------------------------- spansh --
def post(body, url=API):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers=UA)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def lookup(name):
    data = post({"filters": {"name": {"value": name}}, "size": 5})
    for r in data.get("results", []):
        if r["name"].lower() == name.lower():
            return r
    sys.exit("System not found on Spansh: %s" % name)


def system_stations(name):
    """Full station records (services, pads, faction) of one system."""
    data = post({"filters": {"distance": {"min": "0", "max": "0.1"}},
                 "reference_system": name, "size": 200}, STATIONS_API)
    return [s for s in data.get("results", [])
            if s.get("system_name", "").lower() == name.lower()]


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
    if len(points) == 1:
        return fetch_sphere(points[0], detour, filters)
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


def power_filters(power, states):
    filters = {}
    if power:
        filters["controlling_power"] = {"value": [power]}
    if states:
        filters["power_state"] = {"value": list(states)}
    return filters


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
    """Orders stops by estimated jumps.

    fixed nodes are never dropped; value[n] = how many of the wanted items
    stop n provides (3 megaships = 3); weight[n] = penalty in jumps;
    before = [(a, b)]: a must come before b. END as last node = open route.
    """

    def __init__(self, coords, jump, weight=None, value=None, fixed=(),
                 before=()):
        self.coords, self.reach, self.memo = coords, jump * JUMP_EFFICIENCY, {}
        self.weight, self.value = weight or {}, value or {}
        self.fixed, self.before = set(fixed), list(before)

    def leg(self, a, b):
        if END in (a, b):
            return 0.0
        key = (a, b) if a < b else (b, a)
        if key not in self.memo:
            d = dist(self.coords[a], self.coords[b])
            self.memo[key] = math.ceil(d / self.reach) + d / 1e4
        return self.memo[key]

    def cost(self, path):
        pos = {n: i for i, n in enumerate(path)}
        broken = sum(1 for a, b in self.before
                     if a in pos and b in pos and pos[a] > pos[b])
        return sum(self.leg(a, b) for a, b in zip(path, path[1:])) + \
            sum(self.weight.get(n, 0.0) for n in path
                if n not in self.fixed) + broken * ORDER_PENALTY

    def got(self, path):
        return sum(self.value.get(n, 0) for n in path)

    def insert_cost(self, path, node):
        best = None
        for i in range(1, len(path)):
            delta = self.leg(path[i - 1], node) + self.leg(node, path[i]) - \
                self.leg(path[i - 1], path[i]) + self.weight.get(node, 0.0)
            if best is None or delta < best[0]:
                best = (delta, i)
        return best

    def improve(self, path, pool, needed):
        """2-opt, relocate, drop and swap until nothing improves."""
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
                j = self.insert_cost(rest, node)[1]
                new = rest[:j] + [node] + rest[j:]
                if self.cost(new) < self.cost(path) - 1e-9:
                    path, better = new, True
            for i in range(len(path) - 2, 0, -1):   # drop a spare stop
                node = path[i]
                if node in self.fixed:
                    continue
                rest = path[:i] + path[i + 1:]
                if self.got(rest) >= needed and \
                        self.cost(rest) < self.cost(path) - 1e-9:
                    path, better = rest, True
            slack = self.got(path) - needed
            for i in range(1, len(path) - 1):   # swap a stop with the pool
                node = path[i]
                if node in self.fixed or node not in self.value:
                    continue
                rest = path[:i] + path[i + 1:]
                best = None
                for cand in pool:
                    if cand in path or \
                            self.value[cand] < self.value[node] - slack:
                        continue
                    j = self.insert_cost(rest, cand)[1]
                    new = rest[:j] + [cand] + rest[j:]
                    c = self.cost(new)
                    if c < self.cost(path) - 1e-9 and \
                            (best is None or c < best[0]):
                        best = (c, new)
                if best:
                    path, better = best[1], True
                    break
        return path

    def plan(self, fixed, pool, needed):
        path = list(fixed)
        free = [c for c in pool if c not in path]
        while self.got(path) < needed and free:
            short = needed - self.got(path)
            scored = [(self.insert_cost(path, c), c) for c in free]
            (delta, i), c = min(scored, key=lambda x: x[0][0] / max(
                1, min(self.value.get(x[1], 1), short)))
            path.insert(i, c)
            free.remove(c)
        return self.improve(path, pool, needed)


def last_tick(now):
    """Most recent Thursday 07:00 UTC (weekly Powerplay tick)."""
    t = now.replace(hour=7, minute=0, second=0, microsecond=0)
    t -= timedelta(days=(t.weekday() - 3) % 7)
    return t if t <= now else t - timedelta(days=7)


def load_inara(path, tick, quiet=False):
    """parse_inara() with a warning for files saved before the tick."""
    if not path or not os.path.exists(path):
        return None, {}
    ref, ships, saved = parse_inara(path)
    if not quiet:
        print("Inara: %d megaship(s) in %d system(s) from %s (saved %s UTC)%s"
              % (sum(len(v) for v in ships.values()), len(ships),
                 os.path.basename(path), saved.strftime("%d %b %H:%M"),
                 "  ** saved before the last tick - paste a fresh search **"
                 if saved < tick else ""))
    return ref, ships


# ------------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--from", dest="start", default=None,
                    help="start system (default: current, from journal)")
    ap.add_argument("--to", default=None,
                    help="destination system (default: none, open route)")
    ap.add_argument("--via", action="append", default=[],
                    help="mandatory system on the way (repeatable)")
    ap.add_argument("--stops", type=int, required=True,
                    help="number of qualifying stops (megaships) to visit")
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
    ap.add_argument("--inara", default=INARA_FILE,
                    help="pasted Inara megaship search (default "
                         "tools/inara_megaships.txt, if present)")
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

    j_sys, j_jump, _ = journal_state(args.journal_dir)
    args.start = args.start or j_sys
    if not args.start:
        ap.error("no --from given and no journal found")
    args.jump = args.jump or j_jump or 40.0
    mega = args.need == "megaship"
    if args.exclude is None:
        args.exclude = "Cubeo" if mega else ""
    excluded = {s.strip().lower() for s in args.exclude.split(",")
                if s.strip()}
    known = dict(KNOWN_UPLINKS) if mega else {}
    known.update({k.strip(): "" for k in args.known.split(",") if k.strip()})

    states = [s.strip() for s in args.states.split(",") if s.strip()]
    filters = power_filters(args.power, states)
    if args.filter:
        filters.update(json.loads(args.filter))

    names = [args.start] + args.via + ([args.to] if args.to else [])
    ends = [lookup(n) for n in names]
    points = [xyz(s) for s in ends]
    print("Route %s%s, %d stop(s) [%s], power %s %s, jump %.1f ly, detour "
          "<= %.0f ly" % (" -> ".join(s["name"] for s in ends),
                          "" if args.to else " -> (open end)", args.stops,
                          args.need, args.power or "any",
                          "/".join(states) or "any state", args.jump,
                          args.detour))
    tick = last_tick(datetime.now(timezone.utc))
    candidates = fetch_corridor(points, args.detour, filters)
    inara = {}
    if mega:
        ref, inara = load_inara(args.inara, tick)
        if inara:       # Inara systems beyond the corridor: one sphere more
            seen = {c["id64"] for c in candidates}
            centre = xyz(lookup(ref)) if ref else points[0]
            far = max((dist(centre, p) for p in points), default=0)
            for s in fetch_sphere(centre, 100 + far, filters):
                if s["name"] in inara and s["id64"] not in seen:
                    candidates.append(s)
    jmega = journal_megaships(args.journal_dir) if mega else {}

    info, coords = {}, {}
    for s in ends + candidates:
        coords[s["name"]] = xyz(s)
        info[s["name"]] = s
    scored = {}
    for c in candidates:             # ends count only if they match too
        name = c["name"]
        if name.lower() in excluded:
            continue
        if mega:
            ev = megaship_evidence(name, c.get("stations"), jmega, inara,
                                   known, tick, args.include_unknown)
        elif args.need == "any":
            ev = ("matches filters", "fresh", 1)
        else:
            kind = args.need.split(":", 1)[-1].lower()
            hits = [st["name"] for st in c.get("stations") or []
                    if (st.get("type") or "").lower() == kind]
            ev = ("%s: %s" % (args.need[8:], ", ".join(hits[:3])),
                  "fresh", 1) if hits else None
        if ev and (ev[1] == "fresh" or not args.fresh_only):
            scored[name] = ev
    print("%d system(s) match the filters, %d qualify (%d stop(s), %d from "
          "this week)\n" % (len(candidates), len(scored),
                            sum(v[2] for v in scored.values()),
                            sum(v[2] for v in scored.values()
                                if v[1] == "fresh")))

    fixed = [s["name"] for s in ends] + ([] if args.to else [END])
    bonus = {n for n in fixed if scored.get(n, ("", "", 0))[1] == "unknown"}
    for n in bonus:
        del scored[n]
    planner = Planner(coords, args.jump,
                      weight={n: PENALTY[v[1]] for n, v in scored.items()},
                      value={n: v[2] for n, v in scored.items()},
                      fixed=fixed)
    pool = [n for n in scored if n not in fixed]
    path = planner.plan(fixed, pool, args.stops)
    print_path(path, planner, info, coords, scored, args.via, excluded, bonus)
    got = planner.got(path)
    if got < args.stops:
        print("Not enough qualifying stops - try a larger --detour%s." % (
            ", a fresh Inara paste or --include-unknown" if mega else ""))
    if mega and any(scored[n][1] == "pre-tick" for n in path if n in scored):
        print("[pre-tick] = last seen before the %s tick: the megaship may "
              "have moved." % tick.strftime("%d %b"))


def print_path(path, planner, info, coords, scored, via=(), excluded=(),
               bonus=()):
    total_ly, total_j, count = 0.0, 0, 0
    real = [n for n in path if n != END]
    for i, name in enumerate(real):
        s = info[name]
        mark = "     "
        if name in scored:
            n = scored[name][2]
            mark = "%2d%s." % (count + 1, "+%d" % (n - 1) if n > 1 else "  ")
            count += n
        role = "start" if i == 0 else "end" if (i == len(real) - 1 and
                                                path[-1] != END) else \
            "via" if name in via else ""
        if i:
            d = dist(coords[real[i - 1]], coords[name])
            j = int(planner.leg(real[i - 1], name))
            total_ly += d
            total_j += j
            leg = "%6.1f ly ~%2d j" % (d, j)
        else:
            leg = " " * 15
        print("%s %s  %-28s %-5s %-10s %s" % (
            mark, leg, name, role, s.get("power_state") or "-",
            scored[name][0] if name in scored else
            "(excluded)" if name.lower() in excluded else
            "no data - check on arrival (bonus, not counted)"
            if name in bonus else ""))
    print("\n%d stop(s), %.0f ly, ~%d jumps (estimate at %.0f ly/jump)"
          % (count, total_ly, total_j, planner.reach))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
