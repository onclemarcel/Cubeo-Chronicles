#!/usr/bin/env python3
"""
pp_mining_routes.py - Powerplay 2.0 laser-mining spot finder (Spansh data).

Finds ring hotspots in systems controlled by your power, with a station in
the SAME system that buys the mined commodity:
  * PP2 reinforcement rule (Powerplay Missions.md §3): mine in a system your
    power controls and sell the mined goods in that same system.
  * Laser-minable hotspot commodities only (the Astroforge has no seismic
    charges / abrasion blaster): Platinum, Painite, Low Temperature Diamonds,
    Osmium, Palladium, Gold, Bertrandite, Bromellite by default.

Ranking: estimated value of one full hold sold at the best in-system station
(cargo x sell price, capped by demand), then hotspot count on the ring (2+ =
possible overlap), then Pristine reserves, then station distance.

Merit estimate - HYPOTHESIS, NOT MEASURED: the trade formula
    merits = floor( tons x (sell - 1.4 x buy) x 156 / 1,000,000 )
with buy = 0 for mined goods gives tons x sell x 156 / 1M. Verify with a
first sale (journal MarketSell + PowerplayMerits) before trusting it.
Strongholds paid 0 merits for TRADE; whether that holds for mining is
unknown, so they are listed but flagged (--skip-states to drop them).

Data: https://spansh.co.uk (public API, EDDN-fed). Ring hotspots come from
players' DSS scans; prices can be days old - check the "age" column and the
in-game market before mining.

Usage examples:
  python tools/pp_mining_routes.py                       # around current system
  python tools/pp_mining_routes.py --ref Cubeo --radius 40
  python tools/pp_mining_routes.py --minerals Platinum --cargo 128
  python tools/pp_mining_routes.py --skip-states Stronghold
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

from pp_trade_routes import (CONTROL_STATES, EXCLUDED_TYPES, age_days,
                             journal_defaults)

BODIES_API = "https://spansh.co.uk/api/bodies/search"
STATIONS_API = "https://spansh.co.uk/api/stations/search"
UA = {"Content-Type": "application/json",
      "User-Agent": "cubeo-chronicles-pp-mining/1.0"}
LASER_MINERALS = ("Platinum", "Painite", "Low Temperature Diamonds",
                  "Osmium", "Palladium", "Gold", "Bertrandite", "Bromellite")
MERITS_PER_MCR = 156.0          # trade fit, reinforcement - unverified here
RESERVE_RANK = {"Pristine": 3, "Major": 2, "Common": 1, "Low": 0,
                "Depleted": -1}


def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def fetch_hotspot_bodies(ref, radius, mineral):
    """Bodies within radius whose rings carry >= 1 hotspot of mineral."""
    bodies, page, size = [], 0, 100
    while True:
        data = post(BODIES_API, {
            "filters": {"distance": {"min": 0, "max": radius},
                        "ring_signals": [{"name": mineral,
                                          "comparison": "<=>",
                                          "value": [1, 99]}]},
            "reference_system": ref, "size": size, "page": page,
            "sort": [{"distance": {"direction": "asc"}}]})
        batch = data.get("results", [])
        bodies.extend(batch)
        page += 1
        if not batch or len(bodies) >= data.get("count", 0):
            return bodies


def fetch_system_stations(system):
    """Stations with a market in one system (exact system-name match)."""
    data = post(STATIONS_API, {
        "filters": {"system_name": {"value": [system]},
                    "has_market": {"value": True}},
        "size": 100, "page": 0})
    return [s for s in data.get("results", [])
            if s.get("system_name") == system and
            s.get("type") not in EXCLUDED_TYPES]


def pad_ok(st, pad):
    if pad == "L":
        return bool(st.get("has_large_pad"))
    return bool(st.get("has_large_pad") or st.get("medium_pads"))


def best_outlet(stations, mineral, cargo, pad):
    """Best in-system station buying mineral: (station, sell, demand, value)."""
    best = None
    for st in stations:
        if not pad_ok(st, pad):
            continue
        for c in st.get("market") or []:
            if c.get("commodity") != mineral:
                continue
            sell, demand = c.get("sell_price") or 0, c.get("demand") or 0
            if sell <= 0 or demand <= 0:
                continue
            value = min(cargo, demand) * sell
            if best is None or value > best[3]:
                best = (st, sell, demand, value)
    return best


def main():
    j_sys, j_cargo = journal_defaults()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--ref", default=j_sys,
                    help="reference system (default: current, from journal)")
    ap.add_argument("--radius", type=float, default=30.0,
                    help="search radius around --ref in ly (default 30)")
    ap.add_argument("--power", default="Aisling Duval")
    ap.add_argument("--cargo", type=int, default=j_cargo or 128,
                    help="cargo capacity (default: current ship, journal)")
    ap.add_argument("--pad", choices=("L", "M"), default="L",
                    help="landing pad needed (default L, Clipper)")
    ap.add_argument("--minerals", default=",".join(LASER_MINERALS),
                    help="comma list of hotspot commodities to look for")
    ap.add_argument("--skip-states", default="",
                    help="comma list of own control states to drop "
                         "(e.g. Stronghold; default: none, flagged instead)")
    ap.add_argument("--max-age", type=float, default=7.0,
                    help="flag markets older than N days (default 7)")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()
    if not args.ref:
        ap.error("no --ref given and no journal found")
    minerals = [m.strip() for m in args.minerals.split(",") if m.strip()]
    skip = {s.strip() for s in args.skip_states.split(",") if s.strip()}

    print("Reference %s, radius %.0f ly, power %s, cargo %d t, pad %s" % (
        args.ref, args.radius, args.power, args.cargo, args.pad))

    # 1. hotspot rings in systems the power controls
    spots = []          # (system, body, ring, mineral, count, reserve, dist)
    for mineral in minerals:
        for b in fetch_hotspot_bodies(args.ref, args.radius, mineral):
            state = b.get("system_power_state")
            if b.get("system_controlling_power") != args.power or \
                    state not in CONTROL_STATES or state in skip:
                continue
            for ring in b.get("rings") or []:
                for sig in ring.get("signals") or []:
                    if sig.get("name") == mineral:
                        spots.append((b, ring, mineral, sig.get("count", 0)))
    if not spots:
        print("No hotspot found in %s systems - try a larger --radius." %
              args.power)
        return

    # 2. same-system outlet for each spot
    station_cache, rows = {}, []
    for b, ring, mineral, count in spots:
        system = b["system_name"]
        if system not in station_cache:
            station_cache[system] = fetch_system_stations(system)
        outlet = best_outlet(station_cache[system], mineral, args.cargo,
                             args.pad)
        rows.append((b, ring, mineral, count, outlet))

    def key(r):
        b, ring, mineral, count, outlet = r
        return (outlet[3] if outlet else 0, count,
                RESERVE_RANK.get(b.get("reserve_level"), 0),
                -(b.get("distance_to_arrival") or 0))
    rows.sort(key=key, reverse=True)

    print("Merits/hold = cargo x sell x %d / 1M  (HYPOTHESIS from the trade "
          "formula with buy = 0 - verify on the first sale)\n" %
          MERITS_PER_MCR)
    for n, (b, ring, mineral, count, outlet) in enumerate(rows[:args.top], 1):
        state = b.get("system_power_state")
        print("%2d. %-24s %dx hotspot  %s  (%s, %s)  %.1f ly" % (
            n, mineral, count, ring["name"], b["system_name"], state,
            b.get("distance") or 0))
        print("    ring %s, reserves %s, body at %.0f ls%s" % (
            ring.get("type") or "?", b.get("reserve_level") or "?",
            b.get("distance_to_arrival") or 0,
            "   [Stronghold: trade paid 0 merits here]"
            if state == "Stronghold" else ""))
        if outlet:
            st, sell, demand, value = outlet
            age = age_days(st.get("market_updated_at"))
            print("    sell at %s (%.0f ls, %s pad): %s CR/t, demand %d t%s"
                  "  -> hold %s CR, ~%d merits?%s" % (
                      st["name"], st.get("distance_to_arrival") or 0,
                      "L" if st.get("has_large_pad") else "M",
                      format(sell, ","), demand,
                      "  LOW DEMAND" if demand < args.cargo else "",
                      format(value, ","),
                      int(value / 1e6 * MERITS_PER_MCR),
                      "  (market %.1f d old%s)" % (
                          age, ", STALE" if age > args.max_age else "")
                      if age is not None else ""))
        else:
            print("    no in-system station buys %s (pad %s) - no merits" %
                  (mineral, args.pad))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
