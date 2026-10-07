#!/usr/bin/env python3
"""
combat_stats.py - Combat metrics from the Elite Dangerous journal (no API).

Rebuilds every combat instance (conflict zone, RES, nav beacon, megaship...)
from the local journal files and reports, per instance and in aggregate:
  * time in the instance, kills, kills per hour, credits (bonds + bounties);
  * gap between kills and time on target for each kill;
  * the ship type and pilot rank of each kill, and how much of it was left
    to destroy when you locked it (shield % + hull %);
  * engagements dropped without a kill (target fled, finished by someone
    else, or abandoned) and short "selection" locks;
  * shields lost, lowest hull, heat warnings, interdictions;
  * how the instance ended: clean exit, fled (shields down / hull < 50 %),
    died, or session end (logout inside the zone);
  * the weapon fit in use, so two fits (or two hulls: Pacifier now, Nemesis
    or Charybdis later) can be compared on the same indicators.

How targets are tracked (all from ShipTargeted events):
  * A "lock run" is one unbroken lock on one target, from the lock to the
    unlock or the next lock. The journal writes a ShipTargeted event on
    every lock, scan stage and subsystem change, each carrying the target's
    shield %, hull % and (for subsystems) the subsystem's health - snapshots,
    not a continuous feed. Nothing is written while you just shoot.
  * A kill clears the lock in the same second (TargetLocked: false), so a
    bond or bounty that lands while a run is open, and ends it, is a
    CONFIRMED kill of that target. Otherwise the killed ship is INFERRED
    from the last scanned target of the victim faction since the previous
    kill (FactionKillBond itself names no ship; Bounty does).
  * An "engagement" merges the runs on one target (ship type + pilot name)
    since the previous kill, as long as no lock on another target in between
    lasted 20 s or more. Time on target = kill - start of the engagement.
  * "Left to kill" = shield % + hull % at the first full scan of the
    engagement (0-200). Allies' damage before your lock shows up here: a
    target locked at 40 % shield / 90 % hull was 130, not 200.
  * "Shield back" counts engagements where a later snapshot shows the
    shield higher than an earlier one (it regenerated or was re-boosted).
  * Engagements of 20 s or more that end without a kill are "dropped": the
    target fled, was finished by an ally, or you switched. The journal can't
    tell which. Locks under 10 s are counted as target selection.
  * NPC pilots mostly share one generic name ("System Defence Force"), so
    two Eagles fought back to back can merge; treat times as approximate.
  * Cycling subsystems reveals the target's weapons, listed per ship type.
  * The bond value shown at the kill is not the value paid: CG / Powerplay
    bonuses apply at hand-in (RedeemVoucher), reported per session.
  * Heat sink launches, ammo use and pips are not logged; BuyAmmo and
    RepairAll costs are reported per session as a proxy.

Usage examples:
  python tools/combat_stats.py                          # last 7 days
  python tools/combat_stats.py --since 2026-10-06       # the CG 860 sessions
  python tools/combat_stats.py --since 2026-10-06 --kills   # one line per kill
  python tools/combat_stats.py --since 2026-10-06 --csv out/cz   # out/cz_*.csv
"""

import argparse
import csv
import datetime as dt
import glob
import json
import os
import statistics
from collections import Counter, defaultdict

JOURNAL_DIR = os.path.expandvars(
    r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
FLED_HULL = 0.50                # exit with hull below this = "fled (hull)"
INTERDICTION_S = 90             # SupercruiseExit this soon after Interdicted
ENGAGED_S = 20                  # a lock this long counts as an engagement
SELECT_S = 10                   # a lock shorter than this = target selection

SHIP_NAMES = {
    "krait_light": "Krait Phantom", "krait_mkii": "Krait Mk II",
    "viper_mkiv": "Viper Mk IV", "viper": "Viper Mk III",
    "cobramkiii": "Cobra Mk III", "cobramkiv": "Cobra Mk IV",
    "cobramkv": "Cobra Mk V", "federation_dropship": "Fed. Dropship",
    "federation_dropship_mkii": "Fed. Assault Ship",
    "federation_gunship": "Fed. Gunship", "federation_corvette": "Corvette",
    "empire_eagle": "Imp. Eagle", "empire_courier": "Imp. Courier",
    "empire_trader": "Imp. Clipper", "empire_fighter": "Imp. Fighter",
    "typex": "Alliance Chieftain", "typex_2": "Alliance Crusader",
    "typex_3": "Alliance Challenger", "type9_military": "Type-10",
    "asp": "Asp Explorer", "type9": "Type-9", "asp_scout": "Asp Scout",
    "diamondbackxl": "DB Explorer", "diamondback": "DB Scout",
    "ferdelance": "Fer-de-Lance", "mamba": "Mamba", "python": "Python",
    "python_nx": "Python Mk II", "anaconda": "Anaconda", "eagle": "Eagle",
    "vulture": "Vulture", "adder": "Adder", "sidewinder": "Sidewinder",
    "hauler": "Hauler", "dolphin": "Dolphin", "orca": "Orca",
    "belugaliner": "Beluga", "mandalay": "Mandalay", "corsair": "Corsair",
    "panthermkii": "Panther Clipper", "type8": "Type-8",
}
RANKS = ["Harmless", "Mostly Harmless", "Novice", "Competent", "Expert",
         "Master", "Dangerous", "Deadly", "Elite"]
SUBSYSTEMS = {"powerplant": "power plant", "drive": "thrusters",
              "hyperdrive": "FSD", "shieldgenerator": "shield gen",
              "lifesupport": "life support", "powerdistributor": "distributor",
              "sensors": "sensors", "cargoscanner": "manifest scanner",
              "shieldbooster": "shield booster", "chafflauncher": "chaff",
              "heatsinklauncher": "heat sink", "plasmapointdefence":
              "point defence", "cargobaydoor": "cargo hatch",
              "fsdinterdictor": "interdictor", "shieldcellbank": "SCB",
              "electroniccountermeasure": "ECM",
              "modularcargobaydoor": "cargo hatch", "dronecontrol": "limpets"}
WEAPONS = {"beamlaser": "beam", "pulselaser": "pulse",
           "pulselaserburst": "burst", "multicannon": "multi-cannon",
           "cannon": "cannon", "slugshot": "frag", "railgun": "rail",
           "plasmaaccelerator": "plasma", "dumbfiremissilerack": "missiles",
           "basicmissilerack": "seekers", "mining": "mining laser",
           "minelauncher": "mines", "advancedtorppylon": "torpedo"}


def ts(e):
    return dt.datetime.strptime(e["timestamp"], "%Y-%m-%dT%H:%M:%SZ")


def ship_name(s):
    s = (s or "?").lower()
    return SHIP_NAMES.get(s, s.replace("_", " ").title())


def zone_label(drop_type):
    """Readable label from a SupercruiseDestinationDrop 'Type' token."""
    t = drop_type or ""
    for key, label in (("Warzone_PointRace_Low", "CZ low"),
                       ("Warzone_PointRace_Med", "CZ medium"),
                       ("Warzone_PointRace_High", "CZ high"),
                       ("Warzone_TG", "AX CZ"),
                       ("ResourceExtraction_Low", "RES low"),
                       ("ResourceExtraction_High", "RES high"),
                       ("ResourceExtraction_Hazardous", "RES hazardous"),
                       ("ResourceExtraction", "RES"),
                       ("NavBeacon", "Nav beacon")):
        if key in t:
            return label
    return t.strip("$;") or "?"


def subsystem_kind(raw):
    """('weapon'|'module', readable name) from a Subsystem token."""
    t = (raw or "").lower().replace("$", "").replace(";", "")
    for prefix in ("hpt_", "int_", "ext_"):
        t = t.replace(prefix, "")
    t = t.replace("_name", "")
    head = t.split("_")[0]
    if head in WEAPONS:
        return "weapon", WEAPONS[head]
    return "module", SUBSYSTEMS.get(head, head)


def weapon_fit(loadout):
    """Compact hardpoint summary, e.g. '1x beam L(g) + 3x MC L/M(g)'."""
    kinds = defaultdict(set)
    count = Counter()
    for m in loadout.get("Modules", []):
        if "Hardpoint" not in m["Slot"] or m["Slot"].startswith("Tiny"):
            continue
        parts = m["Item"].lower().replace("hpt_", "").split("_")
        size = {"small": "S", "medium": "M", "large": "L",
                "huge": "H"}.get(parts[-1], "?")
        mount = {"fixed": "f", "gimbal": "g", "turret": "t"}.get(
            parts[1] if len(parts) > 2 else "", "")
        name = {"beamlaser": "beam", "pulselaser": "pulse",
                "pulselaserburst": "burst", "multicannon": "MC"}.get(
                    parts[0], WEAPONS.get(parts[0], parts[0]))
        count[(name, mount)] += 1
        kinds[(name, mount)].add(size)
    out = [f"{n}x {name} {'/'.join(sorted(kinds[(name, mount)], reverse=True))}"
           f"({mount})" for (name, mount), n in sorted(count.items())]
    return " + ".join(out) or "unarmed"


class Run:
    """One unbroken lock on one target."""

    def __init__(self, t, ship, pilot):
        self.start = self.end = t
        self.ship, self.pilot = ship, pilot
        self.rank = self.faction = None
        self.snaps = []            # (t, shield %, hull %)
        self.subsystems = []       # (kind, name)
        self.kill = None           # the kill dict, if this run ended in one

    @property
    def key(self):
        return (self.ship, self.pilot)

    @property
    def seconds(self):
        return (self.end - self.start).total_seconds()


class Instance:
    def __init__(self, t, label, system, ship, fit, session):
        self.start, self.end = t, None
        self.label, self.system = label, system
        self.ship, self.fit, self.session = ship, fit, session
        self.kills, self.runs = [], []
        self.dropped = []          # engagements >= ENGAGED_S without a kill
        self.selections = 0
        self.shields_lost = 0
        self.min_hull = 1.0
        self.heat = 0
        self.attacked = 0
        self.outcome = None
        self.shields_up = True
        self.hull = 1.0

    @property
    def minutes(self):
        return ((self.end or self.start) - self.start).total_seconds() / 60

    def close(self, t, how):
        self.end = t
        if how in ("died", "session end"):
            self.outcome = how
        elif not self.shields_up:
            self.outcome = "fled (shields down)"
        elif self.hull < FLED_HULL:
            self.outcome = "fled (hull)"
        else:
            self.outcome = "clean"


def engagement(runs, key):
    """Runs on `key` that make up the current engagement (newest last)."""
    out = []
    for r in reversed(runs):
        if r.key == key:
            out.append(r)
        elif r.seconds >= ENGAGED_S:
            break
    return list(reversed(out))


def summarise(runs):
    """Merged view of an engagement: start, rank, health snapshots..."""
    snaps = [s for r in runs for s in r.snaps]
    subs = [s for r in runs for s in r.subsystems]
    rank = next((r.rank for r in runs if r.rank), None)
    left = snaps[0][1] + snaps[0][2] if snaps else None
    regen = any(b[1] > a[1] + 1 for a, b in zip(snaps, snaps[1:]))
    return {"start": runs[0].start, "rank": rank, "left": left,
            "first": snaps[0] if snaps else None, "regen": regen,
            "subsystems": subs, "locks": len(runs)}


def close_instance_runs(inst):
    """After an instance: split runs into selections and dropped engagements."""
    killed = {id(r) for k in inst.kills for r in k.get("runs", [])}
    seen = set()
    groups = []
    for i, r in enumerate(inst.runs):
        if id(r) in killed or id(r) in seen:
            continue
        group = [r]
        seen.add(id(r))
        for r2 in inst.runs[i + 1:]:
            if id(r2) in killed:
                if r2.key == r.key:
                    break
                continue
            if r2.key == r.key:
                group.append(r2)
                seen.add(id(r2))
            elif r2.seconds >= ENGAGED_S:
                break
        groups.append(group)
    for g in groups:
        total = sum(r.seconds for r in g)
        if total >= ENGAGED_S and g[0].faction != "ally":
            info = summarise(g)
            info.update({"ship": ship_name(g[0].ship), "seconds": total,
                         "last": next((s for r in reversed(g)
                                       for s in reversed(r.snaps)), None)})
            inst.dropped.append(info)
        elif total < SELECT_S:
            inst.selections += 1


def journal_files(folder, since):
    files = sorted(glob.glob(os.path.join(folder, "Journal.*.log")),
                   key=os.path.getmtime)
    return [f for f in files
            if os.path.basename(f)[8:18] >= since.isoformat()]


def parse(files):
    instances, sessions = [], []
    cur, run = None, None
    ship, fit = "?", "?"
    system, last_drop = "?", None
    last_interdiction = None
    allies = set()                 # factions awarding bonds (= your side)
    sess = None

    def end_run(t):
        nonlocal run
        if run is not None:
            run.end = t
            run = None

    def close(t, how):
        nonlocal cur
        end_run(t)
        if cur is not None:
            cur.close(t, how)
            for r in cur.runs:
                if r.faction in allies:
                    r.faction = "ally"
            close_instance_runs(cur)
            if cur.kills or cur.attacked:
                instances.append(cur)
            cur = None

    for path in files:
        last_t = None
        for line in open(path, encoding="utf-8"):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            ev, t = e["event"], ts(e)
            last_t = t
            if ev == "LoadGame":
                close(t, "session end")
                sess = {"start": t, "end": t, "redeemed": 0, "ammo": 0,
                        "repair": 0, "interdicted": 0}
                sessions.append(sess)
                ship = e.get("ShipName", e.get("Ship", "?")).strip()
            if sess is not None and not sess.get("closed"):
                sess["end"] = t
            if ev == "Loadout":
                ship = (e.get("ShipName") or e.get("Ship", "?")).strip()
                fit = weapon_fit(e)
            elif ev in ("Location", "FSDJump"):
                system = e.get("StarSystem", system)
            elif ev == "SupercruiseDestinationDrop":
                last_drop = e.get("Type")
            elif ev == "SupercruiseExit":
                close(t, "left")
                if last_drop:
                    label = zone_label(last_drop)
                elif last_interdiction and \
                        (t - last_interdiction).total_seconds() < INTERDICTION_S:
                    label = "Interdiction"
                else:
                    label = e.get("Body", "?")
                cur = Instance(t, label, e.get("StarSystem", system), ship,
                               fit, sess)
                last_drop = None
            elif ev in ("SupercruiseEntry", "Docked", "StartJump"):
                close(t, "left")
            elif ev == "Died":
                close(t, "died")
            elif ev == "Shutdown":
                close(t, "session end")
                if sess is not None:
                    sess["closed"] = True
            elif ev == "Interdicted":
                last_interdiction = t
                if sess is not None:
                    sess["interdicted"] += 1
            elif ev == "RedeemVoucher" and sess is not None:
                sess["redeemed"] += e.get("Amount", 0)
            elif ev == "BuyAmmo" and sess is not None:
                sess["ammo"] += e.get("Cost", 0)
            elif ev == "RepairAll" and sess is not None:
                sess["repair"] += e.get("Cost", 0)
            if cur is None:
                continue

            if ev == "ShipTargeted":
                if not e.get("TargetLocked"):
                    end_run(t)
                    continue
                s = e.get("Ship")
                pilot = e.get("PilotName_Localised")
                if run is None or run.ship != s or (
                        pilot and run.pilot and pilot != run.pilot):
                    end_run(t)
                    run = Run(t, s, pilot)
                    cur.runs.append(run)
                if pilot and not run.pilot:
                    run.pilot = pilot
                run.end = t
                if e.get("ScanStage", 0) >= 3:
                    run.rank = e.get("PilotRank", run.rank)
                    run.faction = e.get("Faction", run.faction)
                    run.snaps.append((t, e.get("ShieldHealth", 0.0),
                                      e.get("HullHealth", 0.0)))
                if e.get("Subsystem"):
                    run.subsystems.append(subsystem_kind(e["Subsystem"]))
            elif ev == "UnderAttack" and e.get("Target") == "You":
                cur.attacked += 1
            elif ev == "ShieldState":
                cur.shields_up = e.get("ShieldsUp", True)
                if not cur.shields_up:
                    cur.shields_lost += 1
            elif ev == "HullDamage" and e.get("PlayerPilot"):
                cur.hull = e["Health"]
                cur.min_hull = min(cur.min_hull, cur.hull)
            elif ev == "HeatWarning":
                cur.heat += 1
            elif ev in ("FactionKillBond", "Bounty"):
                if ev == "FactionKillBond":
                    allies.add(e.get("AwardingFaction"))
                victim_fac = e.get("VictimFaction")
                prev = cur.kills[-1]["t"] if cur.kills else cur.start
                # confirmed: the open run is a victim-faction / bounty target
                tgt, how = None, "inferred"
                if run is not None and run.snaps and (
                        (ev == "Bounty" and run.ship == e.get("Target")) or
                        (ev == "FactionKillBond" and run.faction == victim_fac)):
                    tgt, how = run, "confirmed"
                else:
                    for r in reversed(cur.runs):
                        if r.end < prev:
                            break
                        if ev == "Bounty" and r.ship != e.get("Target"):
                            continue
                        if ev == "FactionKillBond" and r.faction != victim_fac:
                            continue
                        tgt = r
                        break
                runs = engagement(cur.runs[:cur.runs.index(tgt) + 1], tgt.key) \
                    if tgt else []
                info = summarise(runs) if runs else {}
                s = e.get("Target") if ev == "Bounty" else (tgt.ship if tgt else None)
                kill = {
                    "t": t, "kind": "bond" if ev == "FactionKillBond" else "bounty",
                    "how": how if tgt else "unknown",
                    "ship": ship_name(s) if s else "?",
                    "rank": info.get("rank") or "?",
                    "reward": e.get("Reward", e.get("TotalReward", 0)),
                    "ttk": (t - info["start"]).total_seconds() if runs else None,
                    "gap": (t - prev).total_seconds(),
                    "left": info.get("left"), "regen": info.get("regen", False),
                    "locks": info.get("locks", 0),
                    "subsystems": info.get("subsystems", []), "runs": runs,
                }
                cur.kills.append(kill)
                if tgt is not None:
                    tgt.kill = kill
                if how == "confirmed":
                    end_run(t)
        if last_t is not None:
            close(last_t, "session end")
    return instances, sessions


def fmt_s(sec):
    if sec is None:
        return "  -  "
    sec = int(round(sec))
    return f"{sec // 60}:{sec % 60:02d}"


def med(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def fmt_n(v, suffix=""):
    return "  - " if v is None else f"{v:4.0f}{suffix}"


def rate(kill):
    """Health points (shield % + hull %) removed per minute on target."""
    if kill["left"] is None or not kill["ttk"]:
        return None
    return kill["left"] / (kill["ttk"] / 60)


def report(instances, sessions, show_kills):
    print("\n=== Combat instances ===")
    print(f"{'start (UTC)':16} {'zone':12} {'ship':10} {'min':>5} {'kills':>5} "
          f"{'k/h':>5} {'1st kill':>8} {'med gap':>7} {'on tgt':>7} "
          f"{'drop':>4} {'shld':>4} {'hull':>4} {'heat':>4}  outcome")
    for i in instances:
        k = i.kills
        kph = len(k) / (i.minutes / 60) if i.minutes > 0 else 0
        first = fmt_s(k[0]["gap"]) if k else "  -  "
        print(f"{i.start:%m-%d %H:%M}      {i.label[:12]:12} {i.ship[:10]:10} "
              f"{i.minutes:5.1f} {len(k):5d} {kph:5.1f} {first:>8} "
              f"{fmt_s(med([x['gap'] for x in k[1:]])):>7} "
              f"{fmt_s(med([x['ttk'] for x in k])):>7} {len(i.dropped):4d} "
              f"{i.shields_lost:4d} {i.min_hull * 100:3.0f}% {i.heat:4d}  "
              f"{i.outcome}")
        if show_kills:
            for x in k:
                regen = " shield back" if x["regen"] else ""
                print(f"     {x['t']:%H:%M:%S} {x['kind']:6} {x['how'][:4]} "
                      f"{x['ship']:18} {x['rank']:10} left {fmt_n(x['left'])}  "
                      f"on tgt {fmt_s(x['ttk']):>5}  gap {fmt_s(x['gap']):>5}  "
                      f"{x['reward']:>9,} CR{regen}")
            for d in i.dropped:
                print(f"     {d['start']:%H:%M:%S} DROPPED {d['ship']:18} "
                      f"{d['rank'] or '?':10} left {fmt_n(d['left'])}  "
                      f"locked {fmt_s(d['seconds']):>5}")

    print("\n=== By weapon fit ===")
    by_fit = defaultdict(list)
    for i in instances:
        by_fit[(i.ship, i.fit)].append(i)
    for (ship, fit), group in by_fit.items():
        kills = [x for i in group for x in i.kills]
        mins = sum(i.minutes for i in group)
        outcomes = Counter(i.outcome for i in group)
        hours = mins / 60 if mins else 1
        print(f"{ship} - {fit}")
        print(f"   {len(group)} instances, {mins / 60:.1f} h in zone, "
              f"{len(kills)} kills = {len(kills) / hours:.1f} kills/h in zone; "
              f"median gap {fmt_s(med([x['gap'] for x in kills]))}, median "
              f"time on target {fmt_s(med([x['ttk'] for x in kills]))}, "
              f"median damage rate {fmt_n(med([rate(x) for x in kills]))} pts/min")
        print(f"   shields lost {sum(i.shields_lost for i in group)} "
              f"({sum(i.shields_lost for i in group) / hours:.1f}/h), "
              f"lowest hull {min(i.min_hull for i in group) * 100:.0f}%, "
              f"heat warnings {sum(i.heat for i in group)}; dropped "
              f"engagements {sum(len(i.dropped) for i in group)}; outcomes "
              + ", ".join(f"{k} {v}" for k, v in outcomes.most_common()))

    kills = [x for i in instances for x in i.kills]
    dropped = [d for i in instances for d in i.dropped]
    if kills:
        how = Counter(x["how"] for x in kills)
        sel = sum(i.selections for i in instances)
        print(f"\n=== Targets (kills: {how['confirmed']} confirmed by the lock, "
              f"{how['inferred']} inferred, {how['unknown']} unknown; "
              f"{sel} selection locks < {SELECT_S} s) ===")
        print("   'left' = shield % + hull % at lock (200 = untouched); 'rate' "
              "= left / time on target, in points per minute;")
        print("   'dropped' = engagements >= 20 s with no kill (fled, finished "
              "by an ally, or abandoned)")
        print(f"   {'ship':18} {'kills':>5} {'on tgt':>6} {'left':>5} "
              f"{'rate':>5} {'shld back':>9} {'dropped':>7} {'drop time':>9}")
        by_ship = defaultdict(list)
        for x in kills:
            by_ship[x["ship"]].append(x)
        drop_ship = defaultdict(list)
        for d in dropped:
            drop_ship[d["ship"]].append(d)
        for s in sorted(set(by_ship) | set(drop_ship),
                        key=lambda s: -len(by_ship.get(s, []))):
            xs, ds = by_ship.get(s, []), drop_ship.get(s, [])
            print(f"   {s:18} {len(xs):5d} {fmt_s(med([x['ttk'] for x in xs])):>6} "
                  f"{fmt_n(med([x['left'] for x in xs])):>5} "
                  f"{fmt_n(med([rate(x) for x in xs])):>5} "
                  f"{sum(x['regen'] for x in xs):9d} {len(ds):7d} "
                  f"{fmt_s(sum(d['seconds'] for d in ds)) if ds else '  -':>9}")

        print("\n=== Kills by pilot rank ===")
        by_rank = defaultdict(list)
        for x in kills:
            by_rank[x["rank"]].append(x)
        order = {r: n for n, r in enumerate(RANKS)}
        for r, xs in sorted(by_rank.items(), key=lambda kv: order.get(kv[0], 99)):
            print(f"   {r:18} {len(xs):4d}  median on target "
                  f"{fmt_s(med([x['ttk'] for x in xs])):>6}  median rate "
                  f"{fmt_n(med([rate(x) for x in xs]))} pts/min")

        subs = Counter(s for x in kills for kind, s in x["subsystems"]
                       if kind == "module")
        if subs:
            print("\n=== Subsystems you targeted (on ships later killed) ===")
            print("   " + ", ".join(f"{s} {n}" for s, n in subs.most_common()))
        seen = defaultdict(Counter)
        for i in instances:
            for r in i.runs:
                for kind, s in r.subsystems:
                    if kind == "weapon":
                        seen[ship_name(r.ship)][s] += 1
        if seen:
            print("\n=== Enemy weapons seen while cycling subsystems ===")
            for s, c in sorted(seen.items()):
                print(f"   {s:18} " + ", ".join(w for w, _ in c.most_common()))

    print("\n=== Sessions (zone time vs. total, hand-ins) ===")
    for s in sessions:
        inst = [i for i in instances if i.session is s]
        if not inst:
            continue
        total = (s["end"] - s["start"]).total_seconds() / 3600
        zone = sum(i.minutes for i in inst) / 60
        n = sum(len(i.kills) for i in inst)
        print(f"   {s['start']:%m-%d %H:%M}-{s['end']:%H:%M}  {total:4.1f} h logged, "
              f"{zone:4.1f} h in zone ({zone / total * 100 if total else 0:3.0f}%), "
              f"{n:3d} kills = {n / total if total else 0:4.1f}/h overall; "
              f"redeemed {s['redeemed']:,} CR, ammo {s['ammo']:,}, "
              f"repairs {s['repair']:,}, interdicted {s['interdicted']}")


def write_csv(prefix, instances):
    os.makedirs(os.path.dirname(prefix) or ".", exist_ok=True)
    with open(prefix + "_instances.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["start_utc", "end_utc", "system", "zone", "ship", "fit",
                    "minutes", "kills", "dropped", "selections",
                    "shields_lost", "min_hull", "heat", "outcome"])
        for i in instances:
            w.writerow([i.start, i.end, i.system, i.label, i.ship, i.fit,
                        round(i.minutes, 1), len(i.kills), len(i.dropped),
                        i.selections, i.shields_lost, round(i.min_hull, 3),
                        i.heat, i.outcome])
    with open(prefix + "_kills.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["time_utc", "zone", "ship_flown", "fit", "kind", "how",
                    "target_ship", "pilot_rank", "left_at_lock",
                    "time_on_target_s", "gap_s", "shield_back", "locks",
                    "reward"])
        for i in instances:
            for x in i.kills:
                w.writerow([x["t"], i.label, i.ship, i.fit, x["kind"],
                            x["how"], x["ship"], x["rank"],
                            None if x["left"] is None else round(x["left"], 1),
                            x["ttk"], x["gap"], x["regen"], x["locks"],
                            x["reward"]])
    with open(prefix + "_dropped.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["start_utc", "zone", "ship_flown", "target_ship",
                    "pilot_rank", "left_at_lock", "locked_s"])
        for i in instances:
            for d in i.dropped:
                w.writerow([d["start"], i.label, i.ship, d["ship"], d["rank"],
                            None if d["left"] is None else round(d["left"], 1),
                            d["seconds"]])
    print(f"\nCSV written: {prefix}_instances.csv, {prefix}_kills.csv, "
          f"{prefix}_dropped.csv")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--since", default=(dt.date.today()
                                        - dt.timedelta(days=7)).isoformat(),
                    help="first journal date to read, YYYY-MM-DD")
    ap.add_argument("--journal-dir", default=JOURNAL_DIR)
    ap.add_argument("--kills", action="store_true",
                    help="list every kill and dropped engagement per instance")
    ap.add_argument("--csv", metavar="PREFIX",
                    help="also write PREFIX_instances/_kills/_dropped.csv")
    args = ap.parse_args()
    since = dt.date.fromisoformat(args.since)
    instances, sessions = parse(journal_files(args.journal_dir, since))
    if not instances:
        print("No combat instance found since", since)
        return
    report(instances, sessions, args.kills)
    if args.csv:
        write_csv(args.csv, instances)


if __name__ == "__main__":
    main()
