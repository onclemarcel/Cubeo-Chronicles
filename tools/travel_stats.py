#!/usr/bin/env python3
"""
travel_stats.py - Jump and travel metrics per ship, from the Elite Dangerous journal.

For every ship flown, from FSDJump and the events around it:
  * jumps, light years travelled, average / longest jump;
  * jump cadence: time from one jump to the next inside a continuous route
    (no docking, landing or logout in between, gap < --max-gap). This is
    the "jump / scoop / jump" rhythm: FSD charge, hyperspace tunnel,
    alignment and any fuel scooping are all inside it;
  * light years per hour of route time (the travel speed that matters);
  * fuel scooping: share of jumps followed by a scoop, scoop time;
  * neutron / white dwarf supercharges (JetConeBoost) and their boost value;
  * the ship's max jump range from its last Loadout, for reference.

Ships are identified by ShipID (names change, IDs don't); the name shown is
the last one seen. A "route" breaks on Docked, Touchdown, Died, Shutdown,
LoadGame or a gap above --max-gap minutes between two jumps.

Usage examples:
  python tools/travel_stats.py                      # all journals
  python tools/travel_stats.py --since 2026-10-01
  python tools/travel_stats.py --routes             # one line per route
"""

import argparse
import datetime as dt
import glob
import json
import os
import statistics
from collections import defaultdict

JOURNAL_DIR = os.path.expandvars(
    r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
HULLS = {"empire_trader": "Imperial Clipper", "empire_courier": "Imperial Courier",
         "type9": "Type-9", "asp": "Asp Explorer", "corsair": "Corsair",
         "empire_eagle": "Imperial Eagle", "cutter": "Imperial Cutter"}


def ts(e):
    return dt.datetime.strptime(e["timestamp"], "%Y-%m-%dT%H:%M:%SZ")


class Route:
    def __init__(self, ship_id):
        self.ship_id = ship_id
        self.jumps = []            # (t, dist)
        self.scoop_s = 0.0
        self.scooped_after = 0     # jumps followed by a scoop
        self.boosts = []           # JetConeBoost values

    @property
    def seconds(self):
        return (self.jumps[-1][0] - self.jumps[0][0]).total_seconds() \
            if len(self.jumps) > 1 else 0.0


def parse(files, max_gap):
    ships = {}                     # id -> {"name", "hull", "max_jump"}
    routes = []
    cur_id, route = None, None
    scoop_start, scooped_this_leg = None, False

    def end_route():
        nonlocal route
        if route is not None and route.jumps:
            routes.append(route)
        route = None

    for path in files:
        for line in open(path, encoding="utf-8"):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            ev, t = e["event"], ts(e)
            if ev in ("LoadGame", "Loadout", "ShipyardSwap", "ShipyardNew"):
                sid = e.get("ShipID", e.get("NewShipID"))
                if sid is not None:
                    if sid != cur_id:
                        end_route()
                    cur_id = sid
                    info = ships.setdefault(sid, {"name": None, "hull": None,
                                                  "max_jump": None})
                    hull = (e.get("Ship") or e.get("ShipType") or "").lower()
                    info["hull"] = HULLS.get(hull, hull or info["hull"])
                    name = (e.get("ShipName") or "").strip()
                    if name:
                        info["name"] = name
                    if ev == "Loadout" and e.get("MaxJumpRange"):
                        info["max_jump"] = e["MaxJumpRange"]
                if ev == "LoadGame":
                    end_route()
            elif ev == "SetUserShipName" and e.get("ShipID") is not None:
                info = ships.setdefault(e["ShipID"], {"name": None, "hull": None,
                                                      "max_jump": None})
                info["name"] = (e.get("UserShipName") or "").strip() or info["name"]
            elif ev in ("Docked", "Touchdown", "Died", "Shutdown"):
                end_route()
            elif ev == "FSDJump" and cur_id is not None:
                if route is not None and route.jumps and \
                        (t - route.jumps[-1][0]).total_seconds() > max_gap * 60:
                    end_route()
                if route is None:
                    route = Route(cur_id)
                if scooped_this_leg and route.jumps:
                    route.scooped_after += 1
                scooped_this_leg = False
                route.jumps.append((t, e.get("JumpDist", 0.0)))
            elif ev == "FuelScoop" and route is not None:
                scooped_this_leg = True
                if scoop_start is None:
                    scoop_start = t
                route.scoop_s += 5   # FuelScoop is written about every 5 s
            elif ev == "ReservoirReplenished":
                pass
            elif ev == "JetConeBoost" and route is not None:
                route.boosts.append(e.get("BoostValue", 0.0))
    end_route()
    return ships, routes


def fmt_s(sec):
    if sec is None:
        return "  -  "
    sec = int(round(sec))
    return f"{sec // 60}:{sec % 60:02d}"


def report(ships, routes, show_routes, min_jumps):
    by_ship = defaultdict(list)
    for r in routes:
        by_ship[r.ship_id].append(r)
    print(f"\n{'ship':22} {'hull':17} {'max':>5} {'jumps':>5} {'ly':>7} "
          f"{'avg':>5} {'best':>5} {'cadence':>7} {'ly/h':>6} {'scoop':>6} "
          f"{'boosts':>6}")
    rows = []
    for sid, rs in by_ship.items():
        info = ships.get(sid, {})
        jumps = [d for r in rs for _, d in r.jumps]
        # cadence and ly/h only from routes long enough to mean something
        long_rs = [r for r in rs if len(r.jumps) >= min_jumps]
        gaps = [(b[0] - a[0]).total_seconds() for r in long_rs
                for a, b in zip(r.jumps, r.jumps[1:])]
        route_s = sum(r.seconds for r in long_rs)
        route_ly = sum(d for r in long_rs for _, d in r.jumps[1:])
        scooped = sum(r.scooped_after for r in long_rs)
        legs = sum(len(r.jumps) - 1 for r in long_rs)
        boosts = [b for r in rs for b in r.boosts]
        rows.append((route_ly / (route_s / 3600) if route_s else 0, sid, info,
                     jumps, gaps, scooped, legs, boosts))
    for lyh, sid, info, jumps, gaps, scooped, legs, boosts in sorted(
            rows, key=lambda r: -r[0]):
        name = info.get("name") or f"(unnamed, id {sid})"
        mj = info.get("max_jump")
        print(f"{name[:22]:22} {(info.get('hull') or '?')[:17]:17} "
              f"{mj if mj is None else round(mj, 1):>5} {len(jumps):5d} "
              f"{sum(jumps):7.0f} {statistics.mean(jumps):5.1f} {max(jumps):5.1f} "
              f"{fmt_s(statistics.median(gaps) if gaps else None):>7} "
              f"{lyh:6.0f} {(scooped / legs * 100 if legs else 0):5.0f}% "
              f"{len(boosts):6d}")
    print(f"\ncadence = median time from one jump to the next on routes of "
          f"{min_jumps}+ jumps (charge, tunnel, alignment, scooping);")
    print("ly/h = light years per hour of route time; scoop = share of legs "
          "with fuel scooping; boosts = neutron / white dwarf supercharges.")
    if show_routes:
        print("\n=== Routes ===")
        for r in routes:
            info = ships.get(r.ship_id, {})
            dist = sum(d for _, d in r.jumps)
            hours = r.seconds / 3600
            print(f"   {r.jumps[0][0]:%m-%d %H:%M}  "
                  f"{(info.get('name') or info.get('hull') or '?')[:20]:20} "
                  f"{len(r.jumps):3d} jumps {dist:7.1f} ly  {fmt_s(r.seconds):>6}"
                  f"  {(sum(d for _, d in r.jumps[1:]) / hours) if hours else 0:5.0f} ly/h"
                  f"  boosts {len(r.boosts)}")


def journal_files(folder, since):
    files = sorted(glob.glob(os.path.join(folder, "Journal.*.log")),
                   key=os.path.getmtime)
    return [f for f in files
            if since is None or os.path.basename(f)[8:18] >= since.isoformat()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--since", help="first journal date to read, YYYY-MM-DD")
    ap.add_argument("--journal-dir", default=JOURNAL_DIR)
    ap.add_argument("--max-gap", type=float, default=5.0,
                    help="minutes between two jumps before the route breaks")
    ap.add_argument("--min-jumps", type=int, default=3,
                    help="shortest route counted for cadence and ly/h")
    ap.add_argument("--routes", action="store_true", help="one line per route")
    args = ap.parse_args()
    since = dt.date.fromisoformat(args.since) if args.since else None
    ships, routes = parse(journal_files(args.journal_dir, since), args.max_gap)
    if not routes:
        print("No jump found.")
        return
    report(ships, routes, args.routes, args.min_jumps)


if __name__ == "__main__":
    main()
