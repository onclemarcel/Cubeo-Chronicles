#!/usr/bin/env python3
"""
pp_trade_routes.py - Powerplay 2.0 trade route finder (Spansh market data).

Finds "buy here -> sell there" trades that should earn Powerplay merits:
  * sale margin >= 40%  ((sell - buy) / buy)
  * sold in a REINFORCEMENT system (controlled by your power: Exploited /
    Fortified / Stronghold) - goods may come from anywhere, or
  * sold in an ACQUISITION system (Unoccupied, your power present) - goods
    must be bought in a Fortified system of your power within 20 ly or a
    Stronghold within 30 ly of the selling system.

Merit legs are ranked by ESTIMATED MERITS, not credits. Estimate (fitted on
our own journal sales, 29-30 Sept 2026 - provisional, 4 data points):
    merits ~= MERIT_K * tons * margin      (per single sale, rounded down)
so cheap goods at a huge margin beat expensive goods at +40%, and the hold
must be sold in ONE sale (small lots round to 0).

For each merit leg it also suggests the best return leg (credits only,
flagged "PP" if that leg earns merits too).

Data: https://spansh.co.uk (public API, fed by EDDN - prices can be hours or
days old; check the "age" column and the in-game market before loading).

Usage examples:
  python tools/pp_trade_routes.py                      # around current system
  python tools/pp_trade_routes.py --ref "Sarana" --radius 25
  python tools/pp_trade_routes.py --mode acquire --top 15
  python tools/pp_trade_routes.py --cargo 20 --pad M   # small ship
  python tools/pp_trade_routes.py --ref "Sarana" --hubs 40   # acquisition:
      # own Fortified/Stronghold systems within 40 ly of Sarana become buy
      # hubs, sell targets are searched within 20/30 ly of each hub
"""

import argparse
import glob
import json
import math
import os
import sys
import urllib.request
from datetime import datetime, timezone

API = "https://spansh.co.uk/api/stations/search"
CONTROL_STATES = ("Exploited", "Fortified", "Stronghold")
ACQ_RANGE = {"Fortified": 20.0, "Stronghold": 30.0}
MERIT_K = 0.116   # merits per (ton x margin), journal fit - see docstring
JOURNAL_DIR = os.path.join(os.path.expanduser("~"), "Saved Games",
                           "Frontier Developments", "Elite Dangerous")


# ---------------------------------------------------------------- journal --
def journal_defaults():
    """Current system and cargo capacity from the latest journal, if any."""
    system, cargo = None, None
    files = sorted(glob.glob(os.path.join(JOURNAL_DIR, "Journal.*.log")),
                   key=os.path.getmtime, reverse=True)
    for path in files[:5]:
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
            if system is None and name in ("Location", "FSDJump", "Docked",
                                           "CarrierJump"):
                system = ev.get("StarSystem")
            if cargo is None and name == "Loadout":
                cargo = ev.get("CargoCapacity")
            if system and cargo:
                return system, cargo
    return system, cargo


# ----------------------------------------------------------------- spansh --
def fetch_stations(ref, radius, pad, extra=None):
    """All stations with a market within radius ly of ref (paginated).

    extra: additional Spansh filters, e.g. system_power_state/system_power.
    """
    filters = {"distance": {"min": "0", "max": str(radius)},
               "has_market": {"value": True}}
    filters.update(extra or {})
    if pad == "L":
        filters["has_large_pad"] = {"value": True}
    stations, page, size = [], 0, 100
    while True:
        body = json.dumps({"filters": filters, "reference_system": ref,
                           "size": size, "page": page,
                           "sort": [{"distance": {"direction": "asc"}}]})
        req = urllib.request.Request(
            API, data=body.encode(), headers={
                "Content-Type": "application/json",
                "User-Agent": "cubeo-chronicles-pp-trade/1.0"})
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.load(resp)
        batch = data.get("results", [])
        stations.extend(batch)
        page += 1
        if not batch or len(stations) >= data.get("count", 0):
            break
    if pad == "M":
        stations = [s for s in stations
                    if s.get("has_large_pad") or (s.get("medium_pads") or 0)]
    return stations


# ---------------------------------------------------------------- helpers --
def age_days(stamp):
    if not stamp:
        return None
    t = datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - t).total_seconds() / 86400.0


def dist(a, b):
    return math.sqrt((a["system_x"] - b["system_x"]) ** 2 +
                     (a["system_y"] - b["system_y"]) ** 2 +
                     (a["system_z"] - b["system_z"]) ** 2)


def sell_kind(st, power):
    """'R' reinforcement, 'A' acquisition, None if no merits on sale."""
    state = st.get("system_power_state")
    if st.get("system_controlling_power") == power and state in CONTROL_STATES:
        return "R"
    if state in (None, "Unoccupied") and power in (st.get("system_power") or []):
        return "A"
    return None


def acq_source_ok(src, dst, power):
    """Acquisition rule: bought in own Fortified <=20 ly / Stronghold <=30 ly."""
    if src.get("system_controlling_power") != power:
        return False
    limit = ACQ_RANGE.get(src.get("system_power_state"))
    return limit is not None and dist(src, dst) <= limit


def est_merits(qty, margin):
    """Estimated merits for one sale of qty t at margin (provisional fit)."""
    return int(MERIT_K * qty * margin)


def best_leg(src, dst, cargo, min_margin=None):
    """Best commodity src -> dst.

    Margin-gated (merit leg): best by estimated merits, then profit.
    Otherwise (return leg): best by trip profit.
    """
    best = None
    sells = {c["commodity"]: c for c in dst.get("market") or []}
    for c in src.get("market") or []:
        buy, supply = c.get("buy_price") or 0, c.get("supply") or 0
        d = sells.get(c["commodity"])
        if buy <= 0 or supply <= 0 or not d:
            continue
        sell, demand = d.get("sell_price") or 0, d.get("demand") or 0
        if sell <= buy or demand <= 0:
            continue
        margin = (sell - buy) / buy
        if min_margin is not None and margin < min_margin:
            continue
        qty = min(cargo, supply, demand)
        leg = {"commodity": c["commodity"], "buy": buy, "sell": sell,
               "margin": margin, "qty": qty, "profit": qty * (sell - buy),
               "merits": est_merits(qty, margin)}
        if best is None or leg_score(leg, min_margin) > \
                leg_score(best, min_margin):
            best = leg
    return best


def leg_score(leg, min_margin):
    if min_margin is None:
        return (leg["profit"],)
    return (leg["merits"], leg["profit"])


def is_fresh(st, max_age):
    return bool(st.get("market")) and \
        (age_days(st.get("market_updated_at")) or 99) <= max_age


def station_key(st):
    return st.get("market_id") or (st["system_name"], st["name"])


def find_hubs(args):
    """Own Fortified/Stronghold systems within --hubs ly of --ref.

    Returns [(system_name, state, distance, [fresh stations])], nearest first.
    """
    extra = {"system_power_state": {"value": list(ACQ_RANGE)},
             "system_power": {"value": [args.power]}}
    hubs = {}
    for st in fetch_stations(args.ref, args.hubs, args.pad, extra):
        if st.get("system_controlling_power") != args.power:
            continue
        hub = hubs.setdefault(st["system_name"], {
            "state": st.get("system_power_state"),
            "dist": st.get("distance") or 0.0, "stations": []})
        if is_fresh(st, args.max_age):
            hub["stations"].append(st)
    ordered = sorted(hubs.items(), key=lambda kv: kv[1]["dist"])
    return [(name, h["state"], h["dist"], h["stations"])
            for name, h in ordered if h["stations"]]


def hub_routes(args):
    """Acquisition routes bought in each hub, sold within its range."""
    hubs = find_hubs(args)
    print("%d hub system(s) with fresh markets within %.0f ly of %s"
          % (len(hubs), args.hubs, args.ref))
    hubs = hubs[:args.max_hubs]
    extra = {"system_power_state": {"value": ["Unoccupied"]},
             "system_power": {"value": [args.power]}}
    routes, seen = [], set()
    for name, state, d_ref, srcs in hubs:
        rng = ACQ_RANGE[state]
        dsts = [s for s in fetch_stations(name, rng, args.pad, extra)
                if is_fresh(s, args.max_age)]
        print("  hub %-32s %-10s %5.1f ly from ref  %3d buy / %3d sell "
              "stations within %.0f ly" % (name, state, d_ref, len(srcs),
                                            len(dsts), rng))
        for dst in dsts:
            if sell_kind(dst, args.power) != "A":
                continue
            for src in srcs:
                key = (station_key(src), station_key(dst))
                if key in seen or not acq_source_ok(src, dst, args.power):
                    continue
                leg = best_leg(src, dst, args.cargo, args.margin)
                if leg and leg["qty"] >= min(args.min_qty, args.cargo):
                    seen.add(key)
                    routes.append((src, dst, "A", leg))
    print()
    return routes


def sphere_routes(args):
    """Original mode: every pair of stations inside --radius of --ref."""
    stations = fetch_stations(args.ref, args.radius, args.pad)
    fresh = [s for s in stations if is_fresh(s, args.max_age)]
    print("%d stations fetched, %d with fresh market data\n"
          % (len(stations), len(fresh)))
    routes = []
    for dst in fresh:
        kind = sell_kind(dst, args.power)
        if kind is None or (args.mode == "reinforce" and kind != "R") or \
                (args.mode == "acquire" and kind != "A"):
            continue
        for src in fresh:
            if src is dst:
                continue
            if kind == "A" and not acq_source_ok(src, dst, args.power):
                continue
            leg = best_leg(src, dst, args.cargo, args.margin)
            if leg and leg["qty"] >= min(args.min_qty, args.cargo):
                routes.append((src, dst, kind, leg))
    return routes


# ------------------------------------------------------------------- main --
def main():
    j_sys, j_cargo = journal_defaults()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--ref", default=j_sys,
                    help="reference system (default: current, from journal)")
    ap.add_argument("--radius", type=float, default=20.0,
                    help="search radius around --ref in ly (default 20)")
    ap.add_argument("--power", default="Aisling Duval")
    ap.add_argument("--margin", type=float, default=0.40,
                    help="minimum margin for the merit leg (default 0.40)")
    ap.add_argument("--cargo", type=int, default=j_cargo or 700,
                    help="cargo capacity (default: current ship, journal)")
    ap.add_argument("--pad", choices=("L", "M"), default="L",
                    help="landing pad needed (default L)")
    ap.add_argument("--max-age", type=float, default=3.0,
                    help="ignore markets older than N days (default 3)")
    ap.add_argument("--mode", choices=("all", "reinforce", "acquire"),
                    default="all")
    ap.add_argument("--min-qty", type=int, default=50,
                    help="ignore merit legs smaller than N t (default 50)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--hubs", type=float, default=None, metavar="LY",
                    help="acquisition hub mode: find own Fortified/Stronghold "
                         "systems within LY of --ref, then search sell "
                         "targets within 20/30 ly of each hub (ignores "
                         "--radius and --mode)")
    ap.add_argument("--max-hubs", type=int, default=8,
                    help="nearest hubs to explore in --hubs mode (default 8)")
    args = ap.parse_args()
    if not args.ref:
        ap.error("no --ref given and no journal found")

    print("Reference %s, %s, cargo %d t, pad %s, margin >= %d%%, "
          "markets <= %.0f d old" % (
              args.ref,
              "hubs within %.0f ly" % args.hubs if args.hubs is not None
              else "radius %.0f ly" % args.radius,
              args.cargo, args.pad, args.margin * 100, args.max_age))
    routes = hub_routes(args) if args.hubs is not None else sphere_routes(args)

    routes.sort(key=lambda r: (r[3]["merits"], r[3]["profit"]), reverse=True)
    if not routes:
        print("No qualifying route found - try a larger --radius, an older "
              "--max-age or a smaller --cargo.")
        return
    print("Merits are an estimate (MERIT_K=%.3f x tons x margin). Sell the "
          "whole hold in ONE sale.\n" % MERIT_K)

    for n, (src, dst, kind, leg) in enumerate(routes[:args.top], 1):
        back = best_leg(dst, src, args.cargo)
        back_pp = sell_kind(src, args.power) == "R" and back and \
            back["margin"] >= args.margin
        print("%2d. [%s] %s (%s) -> %s (%s)  %.1f ly" % (
            n, "Reinf" if kind == "R" else "Acq",
            src["name"], src["system_name"], dst["name"], dst["system_name"],
            dist(src, dst)))
        print("    MERIT LEG  %-26s %6d -> %6d CR  +%4.0f%%  %4d t  "
              "profit %s CR  ~%d merits" % (
                  leg["commodity"], leg["buy"], leg["sell"],
                  leg["margin"] * 100, leg["qty"],
                  format(leg["profit"], ","), leg["merits"]))
        if back:
            print("    return     %-26s %6d -> %6d CR  +%4.0f%%  %4d t  "
                  "profit %s CR%s" % (back["commodity"], back["buy"],
                                      back["sell"], back["margin"] * 100,
                                      back["qty"],
                                      format(back["profit"], ","),
                                      "  (PP too, ~%d merits)" % back["merits"]
                                      if back_pp else ""))
        print("    market age: buy %.1f d / sell %.1f d   states: %s -> %s" % (
            age_days(src.get("market_updated_at")),
            age_days(dst.get("market_updated_at")),
            src.get("system_power_state") or "-",
            dst.get("system_power_state") or "-"))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as exc:
        sys.exit("Spansh request failed: %s" % exc)
