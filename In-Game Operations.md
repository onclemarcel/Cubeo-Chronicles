# OPERATIONAL GUIDE — CMDR ONCLEMARCEL
## Campaign memory — status as of 25 September 2026 (3312), journal read through 25 Sept 07:47 UTC

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Restructured 23 September 2026 per Tonton Marcel's review (`Reviews.md`): fleet table
> simplified, superseded rules and stale session logs removed, §§6–10 and the old §13 folded
> into a single Roadmap section, and a new phased Gutamaya-fleet plan merged in (translated
> from French — see the note at the end of §5).
> Corrected the same day after a direct Journal check (see `CLAUDE.md` §5.3, which this first
> pass skipped): treasury, the Dart's ownership and the Pacifier's Hot flag were all stale or
> wrong — see §4 for the 23 Sept session log this surfaced.
> Split 25 September 2026 per Tonton Marcel's request: §5 (Roadmap) keeps the main line —
> phases, milestones, checkpoints — and its detailed checklists moved to four satellite files:
> `Powerplay Missions.md`, `Shipyard.md`, `Engineers & Materials.md`, `On-Foot.md` (see §5).

---

## 1. COMMANDER SHEET

| | |
|---|---|
| CMDR | Onclemarcel |
| Inara role | Freelancer / Scientist |
| Squadron | EliteCommanders |
| Trade rank | **Elite** (earned 16 Sept 2026) |
| Combat rank | **Novice** |
| Explorer rank | **Ranger** |
| Exobiologist rank | **Directionless** |
| Mercenary rank | **Defenceless** |
| Imperial Navy rank | **Viscount** |
| Power | Aisling Duval — pledged, **Rank 12 / 74,756 merits** (1 Oct, 17:21 UTC) |
| Home port | Cubeo — Medupe City |
| Treasury | **≈2,224,588,122 CR** (1 Oct 2026, 15:47 UTC, journal `LoadGame`) |
| Game mode | Solo |
| Expansions | Horizons + Odyssey |
| Absence | ~4 years (last memory: Thargoid war, Colonia CG) |

---

## 2. THE FLEET

Simplified per Tonton Marcel's review: one row per ship, modules listed compactly, engineering
grade/experimental effect inline. "To fix" items are removed from here — they live in the
Roadmap (§5) as phase-gated tasks, since bridge ships (The Brick, Hyperion) get no further
engineering investment under the Gutamaya-only goal (§3): what's already fitted stays fitted,
nothing more is added.

| Ship | Hull | Modules (class/grade + engineering + experimental effect) |
|---|---|---|
| **Astroforge** (mining Clipper, `CL-002`, ShipID 10) | Imperial Clipper | *Journal `Loadout` 1 Oct 09:00 + `EngineerCraft` 09:13–09:49 (Farseer, Deciat).* Cargo rack 7E (128 t) · 2× Collector Limpet Controller 3A · Prospector Limpet Controller 1A · Refinery 4A · Fuel Scoop 4A · Shield Cell Bank 2A · 2× Mining Laser 2D (Fixed) · 1× Beam Laser (Large, Gimballed) · 1× Multi-Cannon (Large, Gimballed) · **4× Shield Booster 0A, Heavy Duty G1 + Super Capacitors** · **Shield 6A, Reinforced G5** · **Thrusters 6A, Dirty Drive G3 + Drag Drives** · **Power Plant 6A, Overcharged G1 + Monstered** · **Distributor 6A, High Capacity G5** · **FSD 5A SCO, Increased Range G5 + Mass Manager** (32.8 ly before Mass Manager) · DSS Expanded G3 · Sensors 5D · Life Support 5D · Fuel Tank 4C · Armour grade 1. No chaff/ECM any more. Merits/h of the PP mining loop still to measure (Checkpoint 1). |
| **Pacifier** (combat Clipper, `MA-10E`, ShipID 2) | Imperial Clipper | *Current fit confirmed from the journal `Loadout`, 23 Sept 18:20:33 UTC (see §4 — supersedes the 19 Sept Inara-export description below, which turns out not to match that day's actual journal `Loadout` either).* 2× Beam Laser (Large, Gimballed) · 2× Multi-Cannon (Medium, Turret) · 2× Shield Booster 0A · 2× Chaff Launcher · Cargo rack 7E (128 t, only cargo left) · Shield 6A · 2× Hull Reinforcement 4D · Module Reinforcement 1D · Multi-drone Controller (Operations) 3C · Fuel Scoop 3A · FSD Interdictor 2D · Planetary hangar 2D · Power Plant 6A · Thrusters 6A · Distributor 6A · Sensors 5D · Life Support 5D · Fuel Tank 4C · Armour grade 3 · **FSD 5A, Faster Boot Sequence g5** (only engineered module on the hull — shield/boosters/KWS from annex A3 still not applied). **Impound cleared 23 Sept** (`ClearImpound`, resolves the old "Hot: true" mystery) — `StoredShips` now shows **Hot: false**. |
| **Dart** (Imperial Courier, ShipID 12, CO-01) | Imperial Courier | Bought 21 Sept 2026, 07:29:47 UTC (`ShipyardBuy`, 2,479,358 CR) — confirmed owned. *Refit + first engineering 1 Oct (journal `Loadout` 17:15 UTC).* 2× Pulse Laser (Medium, Gimballed) · Dumbfire Missile Rack (Medium) · Point Defence · Chaff · 2× Shield Booster 0A (stock) · **Shield 3A, Reinforced G4** (Lei Cheung) · **FSD 3A SCO, Increased Range G4** (Farseer) · **Distributor 3A, High Capacity G2** (The Dweller) · Power Plant 4A · Thrusters 3A (stock) · Life Support 1E · Sensors 2D · Fuel Tank 3C · Fuel Scoop 2A · Planetary hangar 2D · Recon Limpet Controller 1E · Detailed Surface Scanner · 14 t cargo racks · Armour grade 1. **26.3 ly unladen**, 91.6 t, Rebuy 349,958 CR. Next steps and target build: `Shipyard.md`, Dart card. ⚠ The 17:15 `Loadout` shows the thrusters switched **off**. Check the Modules panel. |
| **The Brick** (Type-9, `ON-16T`, ShipID 11) | Type-9 Heavy | 758 t cargo · 26.49 ly · FSD 6B, Increased Range g5 + Deep Charge · Power Plant 6A · Thrusters 6A · Distributor 6A · Shield 5A · Sensors 4E · 3 medium + 2 small gimballed weapons · Armour grade 1. **Stored, not flown, since 19 Sept** (rule 6, §3) — bridge ship for bulk trade until the Cornucopia (Phase 5, §5). **V2 refit done 30 Sept** (`Shipyard.md`, annex A5): the loadout above is the *original* one. The V2 fit (no weapons, 7A Dirty Drive thrusters, 6A SCO FSD G5, 35.2 ly) is in the Shipyard card. |
| **Hyperion** (Asp Explorer, `MA-07A`, ShipID 4) | Asp Explorer | **FSD upgraded to G5 today** (23 Sept, Felicity Farseer at Deciat, `EngineerCraft`): Increased Range g5 + Deep Charge (up from g4/43.08 ly — new jump range not yet re-read from a fresh `Loadout`/Inara export). **Thrusters partially engineered today too:** Tuned g1 → **Dirty Drive Tuning g3 + Overloaded** experimental (not full g5 yet — annex A4 still calls for g5). DSS 1I g5, Expanded Probe Scanning Radius (Lei Cheung, unchanged) · Fuel Scoop 6A · Power Plant 5A, Armoured g1 (unchanged) · Planetary hangar 2D · Shield 5D · 20 t cargo racks · Collector Limpet Controller 3A · Life Support 4D · Distributor 4D · Sensors 5D · 4× Heat Sink Launcher (all tiny hardpoints). Still carrying the rescue-run weapons (2× pulse laser, 4× dumbfire missile rack, collector limpet controller) as of the 23 Sept `Loadout` — strip again before the *Long range* loadout is saved. SCO FSD 5A bought and tested (18 Sept), reverted, stored free at the same station. **Stored, not flown, between sessions** (rule 6) — bridge ship for exploration/exobiology until Marco Polo (Phase 6, §5); her DSS and FSD migrate to that hull. |

**In storage:** Modified Mining Laser 1A, pre-engineered grade 5, at LHS 3872 [Curbeam Hub] —
Class 1 hardpoint (incompatible with any Clipper); to retrieve when a compatible hull is fitting
out.

---

## 3. ESTABLISHED GROUND RULES

**Goal (decided 19 September 2026).** She flies Gutamaya hulls exclusively — Imperial Eagle /
Courier / Clipper / Cutter, Gutamaya Corsair. Non-Gutamaya hulls (Asp, Type-9) are **stored, not
sold** (rule 1). She works mainly for Aisling Duval; the exception is trips to farm G5
materials/data/components to engineer the Gutamaya fleet — the exception covers *who she works
for*, not *what she flies* (still open, see §5.6). Consequences: the Type-11 + Rhino and the
Mandalay are shelved as *her* hulls (no Gutamaya hull carries a Rhino) — **one story exception:**
for missions that need surface mining, a Type-11 + Rhino may enter the fleet as *someone else's
ship, on loan* (`Guidelines.md`, Ch. III); some missions will be hard until each hull is properly
engineered — that is intended. Story reason: `Guidelines.md`, Through-Line, Ch. III. Fleet plan
and engineering work order: §5.

1. **Never sell.** Ship and module storage are free and unlimited. (A single starport's ship
   hangar is capped at 40 ships — doesn't change the rule, ships beyond that just live at a
   different port.)
2. **One ship, two FSDs:** one long-range engineered, one SCO. Swap in minutes at the hangar.

---

## 4. SESSION LOGS

> Raw play log, not yet folded into `Logbook.md` prose. Entries dated before 18 September have
> already been used in the story and are removed from this file (`CLAUDE.md` §4) — the Ega CG
> narrative is covered through the 17 Sept entries. The "recommendation" paragraph that used to
> close this section is removed too: its still-open items now live in the Roadmap (§5).

**CG 859 — "Wreaken Calls for Sourced Materials for Output Comparison Tests"** (Metz Enterprise,
Ega). Closed 18 September 2026. Final result (journal-verified): **15,918 units contributed,
Top 25% bracket, 170,000,000 CR paid.**

- **18 Sept — CG closed, final result (journal-verified):** docked at Metz Enterprise 07:18:29
  UTC; the `CommunityGoal` read moments later confirms **CGID 859 `IsComplete: true`**, final
  `PlayerContribution` **15,918**, `PlayerPercentileBand` **25** — the **Top 25% bracket** stands
  as the definitive result (supersedes the 17 Sept 50%-band expectation). `CommunityGoalReward`
  fired at 07:18:48 UTC for **170,000,000 CR** — exactly the live `Bonus` figure already spotted
  17 Sept, confirming the payout held steady into close.
- **18 Sept — fleet regrouped at Medupe City (journal-verified):** swapped to the Asp at Metz
  Enterprise (`ShipyardSwap`, 07:19:32), flew Ega → Cubeo (5 jumps, ~43 ly/jump unladen), docked
  Medupe City 07:29:52. `ShipyardTransfer` brought the Type-9 home the same session (§2). Combat
  and mining Clippers were already in storage there — all four hulls sat at the same station for
  the first time this campaign.
- **18 Sept — Tritium supply mission, Prismatic Imperium (journal-verified):** picked up
  `Mission_Collect_Industrial` at Medupe City (72 t Tritium, offered reward 8,190,042 CR, expiry
  19 Sept), swapped into the combat Clipper for the run (440 m/s boost), bought 128 t Tritium at
  **Cellarius Beacon** (Tucanae Sector CG-W b2-0, 50,118 CR/t), delivered 72 t at Medupe City.
  Actual `MissionCompleted` reward: **3,380,042 CR + 12× Antimony**, plus Reputation ++ and
  Influence ++ with Prismatic Imperium. No interdiction either way. Sold the 56 t leftover
  Tritium locally afterward for +3,016,048 CR. The Antimony batch is tied in-session to an
  outfit-upgrade checklist noted on Roskam's workbench — raw material for a future `Logbook.md`
  day, not yet drafted (see `characters.md`, Roskam sheet).
- **18 Sept — Asp refit, first pass (journal-verified, see §2):** stripped both missile racks, all
  four beam lasers and both shield boosters (+1,341,400 CR module sale); fitted heat sink
  launchers to all four tiny hardpoints (−13,652 CR). Bought an FSD (SCO) to test (−5,971,625 CR),
  judged the range loss too steep against the grade-4 engineered FSD's ~43 ly unladen range, and
  swapped back — the SCO is now in storage at Medupe City (free), the engineered FSD stays fitted.
- **18 Sept — treasury resync (journal-verified):** `Status.json` reads **1,824,833,287 CR** at
  08:31 UTC — cross-checked against `LoadGame` (1,661,100,215 CR) plus this session's transactions
  (CG reward, ship transfer, mission, trading, refit) to within 1,462 CR of the live balance; the
  small residual is an untracked minor fee, not a data error. **Current figure in §1.**

### 18 September — Aisling's Five Gating Missions (journal-verified)

Source: journal files of 18 Sept, 10:26–19:57 UTC (all times UTC). **Result: Powerplay Rank
0 → 5, merits 0 → 16,424** — the `PowerplayRank` event (Rank 5) fired at 19:47:50, seconds after
the fifth mission paid out. Merits had been accruing the whole day while the rank stayed 0
(5,708 by 12:02, 9,401 by 14:07, 13,117 by 19:30), then posted at once: the gating mechanic works exactly as documented. Per-mission merit awards below are the round-number jumps in
`PowerplayMerits`.

| # | Mission | Where | Ship | Merits | Notes |
|---|---|---|---|---|---|
| 1 | Rare material → unexploited system | **Karsuki Ti** (West Market: 18× Karsuki Locusts @ 915 CR, 10:37) → **HIP 7311** (Fan Base, unoccupied, 10:49) | Asp | +3,600 | Clean. |
| 2 | Ship scans, reinforcement | **HIP 3254** (Aisling Stronghold, heavy undermining) — nav beacon scan 11:18 | combat Clipper | +2,000 | First visit 11:12–11:24 (scan done). Second visit 14:20 after the refit below: shields dropped 14:23, hull 79.9% at 14:25 (`HullDamage`), shields back 14:26, jumped home 14:26. Pirates thick around the beacon. |
| 3 | Aisling Programme → undermine an exploited system | **Vargerson** (Browncoat Refuge; exploited by *A. Lavigny-Duval* + Aisling) — 15× `aislingpromotionalmaterials` collected at Cubeo 12:03, delivered 12:21 | combat Clipper | +3,600 | Route out via Ehlanda / Gliese 54.3 / Tehuenef, back via HIP 6616 / Kaukamal / Hernovacle. Easy. Note the irony: ALD is a ZYADA ally on paper (`Galaxy Chronicles.md`), yet this mission undermines her hold. |
| 4 | Rescue — wreckage / black boxes | **Lambda Hydri** (Hansteen Depot, pop. 2,490, exploited) | Clipper (first pass, 18:01) → **Asp** (from 18:38) | +2,800 | See mechanics below. Three more runs after the first hand-in. |
| 5 | Bounty hunting, reinforced system | **Chinovane** (pop. 2,133, exploited) — nav beacon, 19:42–19:48 | combat Clipper | +3,200 | Easier than expected; wanted pilots found by scanning at the beacon. Rank 5 posts here. |

**Rescue mission — how it actually works:** moved to `Powerplay Missions.md`, card 4.4.

**Combat Clipper refit between the two HIP 3254 visits:** multi-cannon turrets, chaff and a module
reinforcement went in at 12:06–12:11, after the first visit. The journal logs no damage on that
first visit; the only `HullDamage` is on the second.

**Raw material for future `Logbook.md` days** (real play, not yet drafted): falling out of power
in the combat Clipper during a pirate engagement — the "what it cost me" of a bad
power-distribution policy (see the still-open task in §5.1); the Clipper's speed as the escape;
wreckage and black boxes recovered from other pilots' dead ships, handed to a stranger on a pad the
Clipper wouldn't fit; a second, easier bounty run that ends with the rank arriving unannounced.

### 21 September — Roskam Visit, Prismatic Imperium Supply Run, On-Foot Salvage Deaths (journal-verified)

Source: journal files of 21 Sept, 08:05–18:28 UTC (morning and evening sessions).

**Roskam Enterprise visit confirmed:** the controlling minor faction on the ground there is
**Cubeo Patron's Principles** (Patronage government, Empire allegiance) — matches Tonton Marcel's
read of it as "traditional imperialist."

**Prismatic Imperium supply-mission run (08:05–11:50 UTC):** ~20 `Mission_Collect_CivilLiberty`
missions ("Fournisseur en quête de...") run back-to-back — commodities (Surface Stabilisers,
Silver, Gold, Palladium) delivered **to Roskam Enterprise**, all correctly accepted **for
Prismatic Imperium** (the `Faction` field on each `MissionAccepted`) — the intended target
faction. Individual rewards ranged 10k–30M CR; combined well over 400M CR across the run. Every
`MissionCompleted` fired an `Influence` gain of `"+++"` to `"+++++"` for **Prismatic Imperium**.

**Why Prismatic Imperium's own influence barely moved — confirmed with a multi-day trend, not a
targeting mistake:** `Location` events across this session put Prismatic Imperium's Cubeo
influence at **46.26% at session start (07:06 UTC) and 45.56% at session end (12:42 UTC)** — flat
to slightly down, despite ~20 completed missions each individually flagged `"+++"`/`"+++++"`.
Pulling the same reading from the 18 Sept session's journal shows **46.2%** that day too — the
number has sat within a fraction of a point of 46% across at least three real-world days (18, then
21 Sept) of heavy trading and mission-running for this exact faction. Two real ED mechanics
explain this, not a targeting error:
1. **BGS influence updates on a periodic daily tick, not live.** The `"+++"`/`"+++++"` tags on
   each `MissionCompleted` are that mission's contribution *queued toward the next tick* — they
   are not an immediate change to the `Influence` value read back in `Location`/`Docked` events,
   which instead reflects the last tick that already happened.
2. **Cubeo's population is enormous (10,016,390,018, per the `Location` event) and hosts 7 minor
   factions.** BGS influence swing per mission is diluted by total system economic activity.

**Implication:** this is not "Prismatic Imperium can't take Roskam from Cubeo Patron's Principles
via missions," it's "one session isn't the right unit of measurement." BGS takeover of a rival
minor faction's stations requires influence to climb consistently across many ticks, and note this
is a **separate mechanic from Powerplay control** (Aisling Duval's Stronghold status over Cubeo): growing Prismatic Imperium's BGS influence doesn't itself change
`PowerplayStateControlProgress`; the two systems run in parallel and are tracked separately in the
journal (`Factions[].Influence` vs. `PowerplayState`/`PowerplayStateControlProgress`).

**Narrative hook confirmed:** this run gives Ch. III's Roskam thread its opening (Marcella looking
into Roskam Enterprise) without yet surfacing anything about cyborgs there — raw material, not yet
drafted.

**On-foot salvage missions — two failed runs (12:10–12:42 UTC):**
- Two `Mission_OnFoot_Salvage_MB` missions accepted from **Cubeo Patron's Principles** (ship
  schematic recovery from a ground wreck), ~84k CR reward each.
- **12:31:33 — Died**, killed by "Saniyah Flynn" (`assaultsuitai_class1`); mission failed on the
  spot.
- **12:41:20 — Died** on the retry, killed by "Nancy Goodman" (`rangedsuitai_class1`); second
  mission failed the same way.
- Both resurrections were free (`Resurrect`, `Option: "rejoin"`, `Cost: 0`) — no credit lost, but
  both missions were gone for good.
- Matches Tonton Marcel's account: rushed by several hostiles converging on an open wreck site
  with no cover taken. These salvage-wreck sites are **not** the "zero NPC, zero alarm" case in
  §5.2 step 1 — they can spawn armed guards, and the base loadout (Maverick suit, no
  ranged-combat prep) didn't survive the encounter twice in a row. **Folded into the on-foot
  protocol as a new sub-step, §5.2.**

**Evening session, 15:07–18:28 UTC (journal-verified) — zero-threat on-foot missions succeed, the
heist fails:**
- **Salvage, Nexus Heavy Industries** (vehicle schematic from a wreck, accepted 15:14, completed
  15:55) — the salvage type that killed her twice that morning, this time clean. Paid Chemical
  Patents ×4 (data micro-resource).
- **Three Prismatic Imperium on-foot missions** accepted together at Medupe City 15:58 — two
  *"Sécurisation d'un colis"* (target carriers Zachary Hogan / Flora Guthrie at **Kohli
  Cultivation Base** and **Kapoor Agricultural Biome**) and one *Insight data bank* collect at
  **Daramy Botanical Habitat** — ~56–58k CR offered each. All three completed 17:40–17:41.
- **The heist — failed.** `Mission_OnFoot_Heist_MB` ("theft, no violence": a synthetic genome from
  an installation), accepted from Prismatic Imperium 17:55, worked at **Kohli Cultivation Base**
  (Cubeo Patron's Principles' settlement, so a Prismatic job run against the rival faction's
  site). Tonton Marcel's account: scanned one guard successfully, taken afterwards. Journal:
  **18:13:23 `CommitCrime` `onFoot_failureToSubmitToPolice`, 500 CR fine, victim Willard Mendoza,
  faction Cubeo Patron's Principles**; **18:14:55 Died — killed by a `skimmerdrone`** (a security
  drone, not a guard); mission failed the same second.
- **Rebuy 500 CR** (`Resurrect`, option `recover`, cost 500), respawned aboard **The Sepulchre**, a
  megaship in **Col 285 Sector YU-F c11-1**, five jumps from Cubeo (18:17 embark → 18:23 Cubeo →
  docked Medupe City 18:26).

**Mechanics worth keeping:** moved to `On-Foot.md`, card 4.3 (heist).

### 23 September — Deciat Engineering Run, Pacifier Refit, Treasury Correction (journal-verified)

Source: journal file of 23 Sept, 17:21–18:35 UTC. **Why this entry exists:** the first pass of
this file's 23 Sept restructuring (same day, earlier) skipped the direct Journal check that
`CLAUDE.md` §5.3 calls for, and carried forward stale numbers instead — Tonton Marcel caught it;
this entry is the correction, done properly this time.

- **Treasury:** `LoadGame` reads 2,094,004,961 CR at 17:21:40 UTC (session start); known session
  expenses (5× `RefuelAll` ≈432 CR, `RepairAll` 13,479 CR, `BuyAmmo` 111 CR, `ModuleBuy` 880,381
  CR) bring it to **≈2,093,110,558 CR** by `Shutdown` (18:35:42 UTC) — the current figure in §1.
  *(The `Statistics` event's `Bank_Account.Current_Wealth`, 2,474,145,877 CR, is a lifetime
  net-worth stat — credits plus ship/module asset value — not the liquid balance; don't confuse
  the two again.)*
- **17:24:50** — `ShipyardSwap` from Dart to Hyperion (Asp) at Medupe City, storing the Dart.
- **17:35–17:59** — travelled to **Farseer Inc** (Deciat 6 a) and had Felicity Farseer engineer
  Hyperion's thrusters to **Dirty Drive Tuning G3 + Overloaded** and her FSD to **Increased Range
  G5 + Deep Charge** (up from G4) — see §2, §5.4.
- Between the two Deciat visits: a heavy exploration leg in the Asp — 14 `FSDJump`s, extensive FSS
  scanning, fuel-scooping, and a materials trade (6 Selenium → 9 Arsenic) at a material trader.
- **18:16:52** — `ShipyardSwap` from Hyperion back to the Pacifier at Medupe City, storing the Asp.
- **18:16:40** — `ClearImpound` fires on the Pacifier the moment she boards her — the ship had
  been **impounded**, not merely "Hot" as this file previously (and incorrectly) speculated.
  Confirmed clear afterward (`StoredShips`: Hot: false).
- **18:18–18:20** — six `ModuleRetrieve` calls pull stored hull/module reinforcements, an FSD
  interdictor, a planetary hangar and a multi-drone (Operations) controller onto the Pacifier,
  each swapped in for a cargo rack; one `ModuleBuy` adds a 3A fuel scoop the same way. Cargo
  capacity drops from 186 t to 128 t (all of it now the one 7E rack) — see §2.
- **Powerplay:** 5× `PowerplayMerits` ticks of +7 each (18:25–18:31 UTC) bring the Aisling total
  from 16,424 to **16,459** merits, rank unchanged at 5.
- `Statistics` snapshot (read once, at session start, for context — not for the treasury figure,
  see above): `Owned_Ship_Count: 5` (matches Astroforge/Pacifier/Dart/The Brick/Hyperion, §2);
  lifetime `Time_Played` 1,409,520 s (≈391.5 h); 1,089 systems visited; one organic species already
  logged for exobiology (pre-dates this session — no `ScanOrganic`/`CodexEntry` event fired today,
  so nothing new for the Directionless rank, §1).

**Roadmap impact:** two Phase 1 checklist items move from open to done/partial (§5.4). The
Dart-ownership and Pacifier-Hot open items from the first restructuring pass are both resolved
(§2, §5.6).

### 27 September — Gabraceni, the Classified Data That Never Drops (journal-verified)

Source: journal files of 27 Sept, 09:15–18:11 UTC. Weekly assignment "Power classified data"
(card 4.8 in `Powerplay Missions.md`), still not completed.

- **Where:** **Gabraceni** — Aisling **Stronghold**, with five rival Powers also listed in the
  system (A. Lavigny-Duval, Mahon, Winters, Grom, Torval) and heavily undermined by the Federation side.
  Many settlements; six of them run by a Federation minor faction, so no reputation to protect there.
- **Settlements raided on foot:** Sklyarenko's Edge (Gabraceni 9 h, tourism, Fathers of Nontime,
  3 passes 09:24 / 11:03 / 12:28), Hammond Military Site (9 a, military, Gabraceni Empire
  Assembly, 16:55), Pidgaiko's Joy (9 i, tourism, Terra-EX Astro Corp, Federation, 17:49–18:03).
- **Data downloaded:** about 20 items, all association, industrial or political data —
  **no classified data, and no research data either.**
- **Handed in anyway** at the Power contact: 2+2 at 09:34, 1+1 at 16:42, 1+3 at 18:10 →
  **+1,404 merits** for the 16:42 and 18:10 hand-ins (32,869 → 34,273); rank 7.

**Raw material for future `Logbook.md` days:** the same settlements plundered again and again in
a system the Federation is eating away at — every port gives up the wrong secrets.

### 29 September — Sarana on Foot, the First Classified Data, and a Merit-Poor Trade Loop (journal-verified)

Source: journal files of 29 Sept, 11:56–19:22 UTC. Merits 34,507 → **34,892** (rank 7).

- **Covert heist, Sarana (success):** `Mission_OnFoot_Heist_Covert_MB` for Workers of Sarana for
  Equality — steal biological samples from **Simon Biochemical Forum** (Sarana 6 b, high-tech,
  run by Explorers of the Anarchy). On the ground 12:16–13:01, sample taken 12:58, handed in at
  Blaha Dock 13:06: **191,735 CR** + data materials, reputation and influence ++ (offered
  314,235 CR — the difference, exactly 122,500, suggests a materials reward option was picked).
- **On-foot massacre, Sarana (success):** `Mission_OnFoot_MassacreIllegal_MB` for The Eldaren —
  11 kills of Workers of Sarana for Equality personnel. Done at **Sharma Analytics Installation**
  (Sarana 6 a, high-tech, democracy-run faction inside an anarchy system), 15:38–16:42 via the
  SRV, about 45 `onFoot_murder` entries (1,000 CR bounty each, Workers faction) plus minor fines.
  Paid at 16:48: **18,863 CR + 14× Weapon Schematic** (offered 308,863 — again exactly 290,000
  less, same materials-option pattern).
- **First Power classified data:** downloaded at Sharma Analytics at 16:41, handed in at Blaha
  Dock (Sarana, Aisling **Stronghold**) 16:49 → **+187 merits**. Also picked up and still in the
  ship locker: 2+2 industrial, 1 research, 1 political, 1 association Power data — not handed in.
- **Engineering at Blaha Dock:** 14 `EngineerCraft` rolls on the Asp's 5A FSD (Overcharged),
  18:40–18:41.
- **Move to Col 285:** Asp flown Sarana → **Col 285 Sector YA-K b23-10** (Aisling Exploited,
  The Wayward Star). The **Type-9 was transferred there from Cubeo** (971,372 CR, ~25 min).
  Exploration data sold at The Wayward Star 18:53–18:54 → **+184 merits** in small chunks.
- **Trade loop, Asp (20 t):** YA-K b23-10 ↔ **ZA-K b23-1** (Kozyry Prospect, *Unoccupied*,
  Aisling acquisition target, conflict progress 0.0), three round trips 18:52–19:20:
  - medicines bought at YA-K (203) sold at ZA-K (4,643) in lots of 1/2/4/13, then 20 → **0 merits**;
  - cobalt bought at ZA-K (807) sold at YA-K (4,738) in lots of 1/2/16/1 → **9 merits** (all
    on the 16 t lot);
  - uraninite bought at ZA-K (1,081) sold at YA-K (3,401), 20 t → **5 merits**.
  About 340k CR profit for 14 merits. Analysis and rules in `Powerplay Missions.md` §3.
- **19:21** — picked up `Mission_Collect_Industrial` from Blackhawk Corporation at The Wayward
  Star: 90 t Palladium.
- **Palladium run, Type-9 (19:42–19:51):** bought 758 t at Kozyry Prospect (47,138 CR/t,
  35.7M CR), delivered 90 t for the Blackhawk mission, sold the other 668 t at The Wayward Star
  (59,250 CR/t, lots of 1/10/100/557) → ~8.1M CR trade profit, **0 merits** (margin +25.7%,
  under the 40% PP threshold).

**Raw material for future `Logbook.md` days:** the Viscountess going into a settlement twice in
one day — once as a thief, once as an executioner — and walking out with the one secret the
Gabraceni ports never gave up.

### 30 September — The PP Trade Formula, The Brick V2, and the Pyrophyllite Loop (journal-verified)

Source: journal files of 30 Sept, 06:03–18:05 UTC. Merits 34,892 → **51,790** (+16,898;
**rank 7 → 8**).

- **Trade-merit tests, morning (Asp then Type-9):** eight test sales to work out the PP trade
  rule (HIP 3254, Fefra's Legacy, Primi, Luphis, Kurosawa Gateway). Result, exact on every sale
  since: **merits = floor(tons × (sell − 1.4 × buy) × 156 / 1M)** into Exploited/Fortified,
  ~48 instead of 156 into acquisition systems, 0 into Strongholds. Only the profit above the 40%
  line counts. Full data and rules: `Powerplay Missions.md` §3.
- **The Brick V2 refit, 10:29–12:36** (`Shipyard.md`): weapons and chaff sold at Kenig City,
  7A thrusters + 6A SCO FSD + 5C tank + 4D sensors bought; FSD G5 at Paola Prospect / Farseer,
  Dirty Drive G3, High Capacity G5 at The Dweller, Reinforced G5 + boosters G3 at Lei Cheung.
  Lei Cheung unlocked at 11:22 without the planned gold donation. Max jump 26.5 → 35.2 ly.
- **Cryolite / silver runs, 12:36–13:12:** cryolite Gottlob Frege Point (Ehlanda) → Kurosawa
  Gateway (Tucanae Sector UT-Z b5) → 1,669 and 1,462 merits; silver at +45% → only 209.
- **Pyrophyllite loop, 14:44–18:03:** 7 runs Gottlob Frege Point → Kurosawa Gateway (16.9 ly,
  one jump each way), 758 t per sale, **11,430 merits and 93.9M CR profit**. Merits per run fell
  1,784 → 1,450 as the buy price rose 8,994 → 10,629 CR (+~320 CR per purchase; barely
  recovered over a 2 h break). Benchmark in Checkpoint 1 (§5.4).
- **Donations, 18:03:** two Adamantine Union altruism missions, 1.75M CR → 154 merits (~88 per
  1M CR *spent* — a trade run *earns* ~13M CR for ~1,600 merits).
- **One interdiction escaped** on a loaded run — the V2 shields did their job.

### 1 October — Astroforge and Dart Engineering, Four of Five Assignments (journal-verified)

Source: journal files of 1 Oct, 08:59–17:22 UTC (Thursday, first day after the weekly tick).
Merits 51,734 → **74,756** (+23,022; **rank 9 → 12**: 10 at 12:11, 11 at 14:51, 12 at 17:21).

- **Astroforge engineering, Deciat (Farseer Inc), 09:13–09:49:** Power Plant Overcharged G1 +
  Monstered, DSS Expanded G3, Dirty Drive G3 + Drag Drives, FSD G5 + Mass Manager, 4 shield
  boosters Heavy Duty G1 + Super Capacitors. Material trader stops at Bernoulli Vision,
  Chandler Ring and Zahn Enterprise between two visits to Farseer. Fit in §2.
- **Dart refit, Medupe City, 10:01–10:12:** missile rack, point defence and chaff added, shield
  3A moved to the size-3 slot, fuel scoop fitted. Remote engineering: FSD Increased Range G4
  (Farseer), Shield Reinforced G4 (Lei Cheung), Distributor High Capacity G2 (The Dweller).
  At Kenig City (11:41–11:45): 2 shield boosters, sensors 2D, recon limpet controller.
- **Assignment 1 — rare goods:** Karsuki Locusts bought at West Market (Karsuki Ti), sold at
  Fefra's Legacy (Tucanae Sector WO-Z b0, unoccupied) 12:11 → **+3,600**.
- **Holoscreens:** Swift Landing (Ross 279) 10:52, Heinkel Observatory (Shui Wei Sector UJ-Q
  b5-4) 13:30 and 13:31 → 3 × 126 merits.
- **Assignment 2 — megaship datalink scans (Dart):** 10 uplink scans. 8 paid 468 merits each
  (Karsuki Ti ×2, Primi, Lambda-1 Tucanae, Osane, Ehlanda, Fire Fade, HIP 7142). The 2 in
  **Cubeo** (13:40, 13:46) paid **nothing**. Assignment complete 14:27 → **+2,400**.
- **Assignment 3 — Aisling sealed contracts:** 12 collected at Medupe City 14:44, delivered at
  Roelofs Station (Wababa) 14:51 → **+2,000** (+37). One association data item from the locker
  handed in there too → only 187 merits.
- **Assignment 4 — Power data, on foot at Irush (unoccupied):** Ganguly's Garden and Ma
  Hydroponics Hub (Irush A 3 a), 15:09–17:15. Many short take-offs and landings around the
  settlements, plus two re-logs (15:47, 16:07). Collected 5 association, 3 political and 2
  research data. Handed in at Jones Hub (Kapoongzi, Stronghold) 17:20: 2,700 + 1,620 + 720,
  assignment **+5,600**.
- **Fifth assignment** not started.
- Merit rates for these loops: `Powerplay Missions.md` §3.

---

## 5. ROADMAP

Consolidated 23 September 2026: this section now absorbs the old §§8–10 (Imperial rank, on-foot protocol, engineering) and
the old §13 (Gutamaya Programme), plus a new
phased fleet plan Tonton Marcel wrote in French (`Reviews.md`) and asked to be merged in here as
a single set of tasks/checkpoints. Translated to English for consistency with the rest of this
file — ship names, module codes and engineer names are untouched; see the translation note at the
top of `Shipyard.md` §3 for the source.

**Split into satellite files (25 September 2026).** This section is now the main line: phase
goals, milestones and checkpoints. Each milestone points to the satellite file that holds its
detailed checklist; each checkbox lives in one place only (the main line ticks the milestone, the
satellite ticks the steps).

| File | Holds |
|---|---|
| `Powerplay Missions.md` | This week's 5 assignments, the weekly loop, merit loops, one card per mission type |
| `Shipyard.md` | One card per ship (current and future): upgrade checklists, The Brick V2 plan, build specs (old annex §5.7) |
| `Engineers & Materials.md` | Engineer roster and unlock chains, priorities, materials and farms (old §5.3) |
| `On-Foot.md` | Odyssey protocol (old §5.2), gear, progression, one card per ground mission type |

### 5.0 Guiding principles

**Gauges to raise**

| Gauge | Status | Target | Unlocks |
|---|---|---|---|
| Imperial Navy | Viscount | Duke (4 promotions) | Imperial Cutter |
| Aisling rank | Rank 8 / 51,790 merits | Rank 34 (≈247,000 merits) | Prismatic Shields |
| Engineering | FSD G5 accessible | Combat and defence engineers at G5, Guardian tech | All target builds, §5.7 |
| Combat piloting | Novice | Comfortable in HazRES and conflict zones | Actually usable TTK |
| On-foot gear | Defenceless | Better suits and weapons | Ground missions, §5.2 |

**Rules of conduct**

- [ ] Validate every build in EDSY or Coriolis before any purchase. Export the Inara loadout
      after every hull purchase.
- [ ] Bridge ships (The Brick, Hyperion): store at the Medupe City museum once their modules are
      emptied out.
- [ ] Bridge ship (Astroforge): sell once the Hephaestus is operational.
- [x] Settle the Pacifier's bounties before any activity in secure space — turned out to be an
      **impound**, not just a Hot flag; cleared 23 Sept (`ClearImpound`, §2, §4).

### 5.1 Weekly routine

- [ ] **Thursday (PP2 tick):** Aisling assignments — `Powerplay Missions.md` §1–§2.
- [ ] **Every week:** check the active CGs and pick the ship via the target-fleet table (§5.5).
- [ ] **Materials:** one farming session per week, geared toward the current phase (§5.4).
- [ ] **Measurement log:** profit/h, merits/h, TTK per ~1h session. *(Answered: `MarketBuy`/
      `MarketSell` deltas, `MissionCompleted` rewards and `PowerplayMerits` jumps are all
      timestamped in the journal, so profit/h and merits/h can be computed directly from a
      session's log slice. TTK is less direct — approximate it from the gap between the first
      hostile-contact event and the `Bounty`/`FactionKillBond`/`Died` that ends the fight, per
      target.)*
- [ ] **Power distribution policy on the combat Clipper** — lost power mid-fight at HIP 3254
      (§4). Review the priority groups (weapons/shields/thrusters/FSD) before the next combat
      sortie.
- [ ] **Operations:** from Phase 3 onward, solo only.

### 5.2 On-foot mission protocol (Odyssey)

Moved to `On-Foot.md` §1 (25 Sept 2026).

### 5.3 Engineering & materials

Moved to `Engineers & Materials.md` (25 Sept 2026).

### 5.4 The Gutamaya fleet plan — phases 1–6

**Current fleet → optimised Gutamaya fleet**

| Ship | Hull | Current role | Fate |
|---|---|---|---|
| Astroforge | Imperial Clipper | Mining | Sold in Phase 5 (replaced by Hephaestus) |
| Pacifier | Imperial Clipper | Combat / trade | Combat trainer, then becomes the Diplomat in Phase 6 |
| Dart | Imperial Courier | Taxi | Kept (Dart v2) |
| The Brick | Type-9 Heavy | Trade CGs | Bridge ship, stored at the museum in Phase 5 (replaced by Cornucopia) |
| Hyperion | Asp Explorer | Exploration | Bridge ship, stored at the museum in Phase 6 (replaced by Marco Polo) |

> Bridge "The Brick" → Cornucopia: The Brick covers trade CGs until the Cornucopia arrives.
> Bridge "Pacifier" → Diplomat: the Pacifier covers bounty hunting and transforms into the Diplomat.
> Bridge "Hyperion" → Marco Polo: the Hyperion covers exploration and the Guardian quest until the Marco Polo arrives.

#### Phase 1 — Trade and mining first, learn combat

**Goal:** accelerate Aisling merits using current strengths (trade and mining), and start combat
risk-free.

**Ships** → `Shipyard.md`
- [~] Astroforge v2 (annex A1) — engineering 1 Oct (power plant, thrusters, FSD, boosters);
      PP mining merits/h still to measure.
- [~] Dart v2 (annex A2) — refit and first engineering 1 Oct (FSD G4, shield G4,
      distributor G2); thrusters and boosters next.
- [~] Pacifier v2 (annex A3) — impound cleared and refit done 23 Sept; 7A Shield + 6A SCB and
      Kill Warrant Scanner swap remaining.
- [x] The Brick V2 — "90 %" plan (annex A5) — done 30 Sept, plus a 6A SCO FSD.
- [~] Hyperion — FSD G5 done 23 Sept; thrusters at G3 of G5.

**Powerplay** → `Powerplay Missions.md` — ≈172,000 merits remaining to rank 34 (1 Oct:
74,756 of ≈247,000 — about 23 h of The Brick's trade loop at ~7,600 merits/h)
- [ ] Weekly assignments, every Thursday tick.
- [~] Three merit loops run and measured: **PP trade (The Brick) ✔ 30 Sept** (~7,600
      merits/h, Checkpoint 1 below), PP mining (Astroforge), Low RES (Pacifier).
      Also measured 1 Oct with the Dart: **megaship scans ~3,100–4,300 merits/h** and
      **Power data on foot ~2,100–3,300 merits/h** (rough; `Powerplay Missions.md` §3).

**Imperial Navy: Viscount → Duke** — remaining: Count → Earl → Marquis → Duke. Duke rank unlocks
the **Imperial Cutter**. Method: rank up to **Allied** with an Imperial faction in a dense system
(Aisling's +100% rep-gain perk applies in ducal territory) → "Imperial Navy" missions start
appearing on the board → stack them. Ranks are never lost, one rank per session, in parallel with
merit grinding.
- [ ] Push reputation with one Imperial faction in a dense system to **Allied**.
- [ ] Missions for minor Imperial factions in Aisling space (stacks PP and Navy progress); trade
      and delivery missions count too.
- [ ] Accept promotion missions as soon as they appear; stack them toward **Count → Earl →
      Marquis → Duke**.

**On-foot** → `On-Foot.md`
- [ ] Zero-risk steps done: abandoned-settlement reactivation, data recovery.

**Engineers** → `Engineers & Materials.md`
- [ ] Tod McQuinn unlocked (unclaimed bounty-voucher donation — prerequisite: the Low RES loop).
- [x] Lei Cheung unlocked (via The Dweller) — 30 Sept 11:22, rank 5 the same day; the gold
      donation of step 5 wasn't needed.

**📍 Checkpoint 1 — the merit engines are running**
- [~] Merits/h measured for The Brick, Astroforge and Pacifier. Pick the best loop.
      **The Brick ✔ (30 Sept)** — benchmark below; Astroforge and Pacifier still to measure.

  **Benchmark — PP trade, The Brick V2** (Type-9, 758 t, engineered; baseline for the future
  Cornucopia and for the other loops). Route: Pyrophyllite, Gottlob Frege Point (Ehlanda,
  Stronghold) → Kurosawa Gateway (Tucanae Sector UT-Z b5, Fortified), 16.9 ly = one jump each
  way, stations at 24 ls and 442 ls. Source: journal, 30 Sept.

  | Metric | Value | Notes |
  |---|---|---|
  | Round trip (sale to sale) | **~11.3 min** (10.9–11.6) | 14.9 min once, when the route plotted 3 jumps |
  | Merits per run | 1,784 → 1,450 | Falls ~65 per run as the buy price climbs |
  | Profit per run | 14.2M → 12.5M CR | |
  | **Merits/h — full session** | **~7,640** | 17:01 login → 18:03 last sale: 5 runs, 7,897 merits |
  | **Credits/h — full session** | **~63.7M CR** | 65.8M CR profit over the same 62 min |
  | Merits/h — steady cycle | ~7,600 | 4 cycles in 48.9 min, 6,188 merits |
  | Best case (fresh price, 11 min cycle) | ~9,500 | First run's 1,784 merits × 5.3 runs/h |

  How to compare another ship or loop: **merits/h = runs per hour × tons × (sell − 1.4 × buy)
  × 156 / 1M**. The Brick's levers are tonnage (758 t) and a one-jump route; for the
  Cornucopia, compare the same route with its cargo and its round-trip time. The route itself
  wears out: each purchase raises the buy price ~320 CR, so rotate commodities/sources
  (`tools/pp_trade_routes.py` ranks them with the formula).
- [ ] Pacifier: 10 Low RES sessions with no losses, combat rank at least Competent.
- [ ] Hyperion's FSD at G5, Pacifier's boosters and shield at G3+.

#### Phase 2 — Guardian expedition with Hyperion, no purchase

**Goal:** unlock Guardian technology for the whole fleet, and start exobiology (currently
Directionless), which funds what follows.

**Preparation**
- [ ] Hyperion v2 (annex A4) → `Shipyard.md`.
- [ ] On-foot gear: Artemis suit + Genetic Sampler → `On-Foot.md`.

**Expedition**
- [ ] Guardian sites: blueprints and materials.
- [ ] Tech Broker: Guardian FSD Booster (5H for Corsair and Cutter, 4H possible for the Clipper).
- [ ] Tech Broker: Guardian Shield Reinforcement (for the Nemesis).
- [ ] Exobiology en route, targeting high-value species.
- [ ] Sell the data at an Aisling system for exploration and exobiology merits.

**Meanwhile**
- [ ] The Brick stays available for any trade CG that starts up.

**📍 Checkpoint 2 — Guardian technology is unlocked**
- [ ] Guardian FSD Booster and shield reinforcement unlocked.
- [ ] Exobiologist rank progressing, expedition income logged.

#### Phase 3 — Combat, with Corsair #1 "Nemesis"

**Goal:** replace the Pacifier with a proper combat platform, now that piloting has improved.

**Engineers and materials** → `Engineers & Materials.md`
- [ ] Combat engineers: The Dweller to G5, Zacariah Nemo, Professor Palin, McQuinn G5.
- [ ] Materials farmed toward shields, Frags and thrusters.

**Nemesis** → `Shipyard.md`
- [ ] Corsair #1 bought, named Nemesis (annex B2), engineered in order.

**Missions**
- [ ] On-foot Phase 3 steps (Frontline CZs, cut-the-reactor, Dominator suit) → `On-Foot.md`.
- [ ] First solo Operations — needs both tracks ready: ship (Nemesis or Pacifier) and on-foot
      (Frontline CZs at minimum).

**📍 Checkpoint 3 — combat is validated**
- [ ] Nemesis at G5; reference TTK measured in HazRES.
- [ ] Combat rank Expert or above (indicative).
- [ ] At least one combat or bounty-hunting CG played.

#### Phase 4 — Prismatic and Spectre (in parallel)

- [ ] Aisling rank 34: buy and store the Prismatics — 8A for Charybdis; 6A for Cornucopia; 6A for
      Hephaestus; optional for Nemesis.
- [ ] Engineer: Reinforced + Hi-Cap (Lei Cheung).
- [ ] Buy Courier #2 (≈2.4M CR). Name her Spectre (annex B3, §5.7).
- [ ] Useful engineer for utilities and limpets: Ram Tah (conditions to verify).

**📍 Checkpoint 4 — the exclusive modules are in stock**
- [ ] Prismatics stored at the home port.
- [ ] Spectre operational.

#### Phase 5 — Duke and the Cutter family

Reminder: class-6 FSD, class-7 distributor. Slot plan to confirm from the Inara export on first
purchase.

- [ ] Reach Duke rank.
- [ ] Cutter #1: Cornucopia (annex B6, §5.7). Run a full trade CG with her, then sell The Brick.
- [ ] Cutter #2: Hephaestus (annex B7, §5.7), Rhino optional. Sell Astroforge once the
      Hephaestus beats her on profit/h and merits/h.
- [ ] Cutter #3: Charybdis (annex B8, §5.7).

**📍 Checkpoint 5 — the big Gutamaya haulers are running**
- [ ] The Brick retired to the museum and Astroforge sold.
- [ ] Cornucopia, Hephaestus and Charybdis measured on their key indicator.

#### Phase 6 — 100% Gutamaya completion

- [ ] Corsair #2 "Marco Polo" (annex B1, §5.7). Starts directly with FSD G5 and the Guardian
      booster.
- [ ] Store Hyperion at the museum once Marco Polo's range beats hers.
- [ ] Pacifier → Diplomat (annex B4, §5.7): FSD re-engineered to Increased Range, Military Grade
      armour stored.
- [ ] Corsair #3 "Soteria" (annex B5, §5.7).
- [ ] *(Optional)* Corsair #4 "Aegis" (annex B9, §5.7).

**📍 Final checkpoint — 100% Gutamaya fleet**
- [ ] No non-Gutamaya ship left, except Hyperion and The Brick at the Medupe City museum.
- [ ] 10 ships (11 with Aegis), all at G5 on their critical modules.
- [ ] The target-fleet table (§5.5) fully checked.

**Long-term, beyond the Gutamaya plan**
- [ ] Claim a system and Architect status, on the Imperial frontier.
- [ ] Fleet Carrier.
- [ ] Deep-space expedition / exobiology.

**Deliberately not on this list:** no trip to **LHS 3447**. It's her departure system, currently
Fortified under Yuri Grom with no rival Power contest live (checked 18 Sept, `Galaxy
Chronicles.md`) — routing a supply, explo, or CG run through it by accident would spend a beat
that isn't due for a while. Two candidate reasons for an eventual deliberate visit are on record
(`Guidelines.md`, Through-Line Ch. VIII) — neither is a live trigger yet. Plot a wide berth around
it until one is.

### 5.5 Target fleet — end state

| Name | Hull | Pad | Role | Key indicator | Origin |
|---|---|---|---|---|---|
| Dart | Imperial Courier | S | Odyssey taxi, pre-landing support | Survival, speed | Existing (to confirm, §2) |
| Spectre | Imperial Courier | S | Stealth, smuggling, scans, holo-screens | Thermal signature | Phase 4 |
| Diplomat | Imperial Clipper | L | Fast PP logistics | t/trip, PP goods carried | Ex-Pacifier |
| Nemesis | Corsair | M | Bounties, assassinations, massacres, Operations, PP combat | TTK | Phase 3 |
| Marco Polo | Corsair | M | Exploration, exobiology, cartography | Range | Phase 6 (replaces Hyperion) |
| Soteria | Corsair | M | Pad-M freight, passengers, salvage | Profit/h | Phase 6 |
| Aegis *(opt.)* | Corsair | M | AX | AX TTK | Phase 6 |
| Cornucopia | Imperial Cutter | L | Bulk trade, CGs, colonisation | Profit/h | Phase 5 (replaces The Brick) |
| Hephaestus | Imperial Cutter | L | Laser / core / surface mining | Profit/h, merits/h | Phase 5 (replaces Astroforge) |
| Charybdis | Imperial Cutter | L | Conflict zones | Survival, obligations/h | Phase 5 |

**Coverage by activity: today vs. at completion**

| Activity | Context | Today | At completion |
|---|---|---|---|
| Bulk trade | Missions, CGs, colonisation, PP | The Brick | Cornucopia |
| Pad-M freight | Missions, colonisation | Hyperion (limited) | Soteria |
| Power goods | PP2 | Pacifier / The Brick | Diplomat |
| Laser & core mining | Missions, CGs, PP2 | Astroforge | Hephaestus |
| Surface mining (Rhino) | Since 09/2026 | — | Hephaestus |
| Bounties, assassinations, massacres | Missions, CGs, PP2 | Pacifier (Low RES) | Nemesis |
| Space conflict zones | BGS, PP CZ, CGs | — | Charybdis |
| PP combat | PP2 | Pacifier | Nemesis |
| Operations | 2026, PP variants | — | Nemesis (backup: Charybdis) |
| Exploration, cartography | Missions, CGs, PP2 | Hyperion | Marco Polo |
| Exobiology | CGs, PP2 | Hyperion | Marco Polo |
| Passengers | Missions, CGs | Pacifier (cabins) | Soteria |
| Salvage | Missions, PP2 | Astroforge (collectors) | Soteria |
| Scans (megaships, datalinks) | Missions, PP2 | Dart | Spectre |
| Holo-screens | PP2 | — | Spectre |
| Smuggling | Missions | Dart | Spectre |
| On-foot missions | Missions, on-foot PP2 | Dart + Scorpion | Dart + Scorpion |
| On-foot conflict zones | BGS, CGs | Dart (taxi) | Dart (taxi) |
| AX | One-off CGs | — | Aegis |

**CG type ↔ ship correspondence (at completion; "bridge" = in the meantime)**

| CG type | Ship | Bridge |
|---|---|---|
| Delivery, construction, colonisation | Cornucopia (L) or Soteria (M) | The Brick |
| Minerals | Hephaestus | Astroforge |
| Bounty hunting | Nemesis | Pacifier |
| Combat obligations | Charybdis | Nemesis |
| Exploration or exobiology data | Marco Polo | Hyperion |
| Salvage | Soteria | Astroforge |
| Passengers, evacuations | Soteria or Cornucopia (cabins) | Pacifier |
| On foot | Dart | — |
| AX | Aegis | — |

### 5.6 Open items

- **Farming-trip exception (rule 6, §3):** whether a farming trip may use a non-Gutamaya hull
  (e.g. the mining Clipper while she's still in the fleet) or only a non-Aisling employer.
  Default until decided: the exception covers *who she works for*, not *what she flies*.
- ~~Dart ownership~~ — **resolved 23 Sept** by a direct journal check: bought 21 Sept 2026,
  07:29:47 UTC for 2,479,358 CR (§2, §4).
- **Juri Ishmaak** — already **Unlocked, Grade 1** (`EngineerProgress`, 23 Sept, §5.4) but not
  mentioned anywhere in this plan. Role/priority not yet decided.

### 5.7 Annex — ship build specs (JSON)

Moved to `Shipyard.md` §3 (25 Sept 2026). Annex labels A1–A5 and B1–B9 are unchanged.

---

## 6. TOOLS

| Tool | Use |
|---|---|
| Inara | Database, live CGs, trade routes, engineers |
| EDSM | Cartography, stations, history |
| Spansh | Exobiology, material, cargo and neutron routes |
| Coriolis / EDSY | Builds before purchase |
| ED Colonisation Planner | Build order for a system |
| EDMC / EDDiscovery | Automatic journal upload, Inara sync |

**Inara note:** only the active ship reports in if the Frontier account link has expired. Relink
the account in settings, or pull each hull out of the hangar once with EDMC running.

---

*Last updated: 25 September 2026 (journal read through 25 Sept 07:47 UTC; §5 split into four
satellite files per Tonton Marcel's request). To be completed session by session.*

**Data source note:** the game writes local Journal files (`%USERPROFILE%\Saved Games\Frontier
Developments\Elite Dangerous\`) on this machine as you play — plain JSON-lines, one event per
line (`LoadGame`, `Rank`, `Progress`, `Reputation`, `Powerplay`, `CommunityGoal`, `MarketSell`,
`Statistics`, etc.). Everything marked "journal-verified" above was read directly from that
day's files, no API or login involved. This is the preferred source going forward — more
accurate than memory, no setup, no credentials. Two fallbacks exist if the journal ever isn't
available (e.g. working from a different machine): **(a)** a public Inara CMDR profile page can
be read directly if you share the URL — one-off, no API key needed; **(b)** Frontier's own
Companion API would give the same data but requires OAuth login with the actual game account,
which isn't something worth setting up for this — Frontier has also long restricted new API
client registrations. The journal folder makes both unnecessary while this session's machine is
the one being played on.
