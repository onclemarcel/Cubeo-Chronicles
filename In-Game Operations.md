# OPERATIONAL GUIDE — CMDR ONCLEMARCEL
## Campaign memory — status as of 23 September 2026 (3312), journal read through 18:35 UTC

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Restructured 23 September 2026 per Tonton Marcel's review (`Reviews.md`): fleet table
> simplified, superseded rules and stale session logs removed, §§6–10 and the old §13 folded
> into a single Roadmap section, and a new phased Gutamaya-fleet plan merged in (translated
> from French — see the note at the end of §5).
> Corrected the same day after a direct Journal check (see `CLAUDE.md` §5.3, which this first
> pass skipped): treasury, the Dart's ownership and the Pacifier's Hot flag were all stale or
> wrong — see §4 for the 23 Sept session log this surfaced.

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
| Power | Aisling Duval — pledged, **Rank 5 / 16,424 merits** |
| Home port | Cubeo — Medupe City |
| Treasury | **≈2,093,110,558 CR** (23 Sept 2026, ~18:35 UTC, journal-computed — see §4) |
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
| **Astroforge** (ex-mining Clipper, `MA-04E`, ShipID 10) | Imperial Clipper | Cargo rack 7E (128 t) · 3× Collector Limpet Controller 3A · Prospector Limpet Controller 1A · Refinery 2A · 2× Mining Laser 2D (Fixed) · 1× Beam Laser (Large, Gimballed) · 1× Multi-Cannon (Large, Gimballed) · Chaff · ECM · 2× Shield Booster · DSS 1I (unengineered) · Shield 6A · Thrusters 6A · Power Plant 6C · Distributor 6A · Fuel Scoop 4A · Sensors 5D · Life Support 5D · Armour grade 1 · **FSD 5A, unengineered** (upgraded from 5E, 18 Sept). *No engineering on any module — Phase 1 target.* |
| **Pacifier** (combat Clipper, `MA-10E`, ShipID 2) | Imperial Clipper | *Current fit confirmed from the journal `Loadout`, 23 Sept 18:20:33 UTC (see §4 — supersedes the 19 Sept Inara-export description below, which turns out not to match that day's actual journal `Loadout` either).* 2× Beam Laser (Large, Gimballed) · 2× Multi-Cannon (Medium, Turret) · 2× Shield Booster 0A · 2× Chaff Launcher · Cargo rack 7E (128 t, only cargo left) · Shield 6A · 2× Hull Reinforcement 4D · Module Reinforcement 1D · Multi-drone Controller (Operations) 3C · Fuel Scoop 3A · FSD Interdictor 2D · Planetary hangar 2D · Power Plant 6A · Thrusters 6A · Distributor 6A · Sensors 5D · Life Support 5D · Fuel Tank 4C · Armour grade 3 · **FSD 5A, Faster Boot Sequence g5** (only engineered module on the hull — shield/boosters/KWS from annex A3 still not applied). **Impound cleared 23 Sept** (`ClearImpound`, resolves the old "Hot: true" mystery) — `StoredShips` now shows **Hot: false**. |
| **Dart** (Imperial Courier, ShipID 12, CO-01) | Imperial Courier | Bought 21 Sept 2026, 07:29:47 UTC (`ShipyardBuy`, 2,479,358 CR) — confirmed owned (journal `StoredShips`/`Statistics.Owned_Ship_Count: 5`). Stock, no engineering yet (Phase 1 target, annex A2). 3× Pulse Laser (Medium, Gimballed) · Armour grade 1 · Power Plant 4A · Thrusters 3A · **FSD 3A SCO** (not yet the long-range engineered pair from rule 3) · Life Support 1E · Distributor 3A · Sensors 2E · Fuel Tank 3C · Shield Generator 2A · Planetary hangar 2D · Detailed Surface Scanner (tiny) · 14 t cargo racks. 20.9 ly unladen, Rebuy 279,921 CR. |
| **The Brick** (Type-9, `ON-16T`, ShipID 11) | Type-9 Heavy | 758 t cargo · 26.49 ly · FSD 6B, Increased Range g5 + Deep Charge · Power Plant 6A · Thrusters 6A · Distributor 6A · Shield 5A · Sensors 4E · 3 medium + 2 small gimballed weapons · Armour grade 1. **Stored, not flown, since 19 Sept** (rule 6, §3) — bridge ship for bulk trade until the Cornucopia (Phase 5, §5). |
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

**Rescue mission — how it actually works (no in-game briefing says this plainly):**
- There is **no mission board entry** — not from minor factions, not from the Imperial contact. It
  is wreckage collected in space and handed in.
- Go to a system **exploited by Aisling** where other Powers are more likely to contest it; use
  the **FSS** to find signal sources of Power-ship wreckage there.
- Recover the items with **collector limpets**; take care with **black boxes** — the authorities
  jump in quickly to check on arrivals.
- **Hand-in must be to the Imperial contact in the same system** where the items were found.
  Hansteen Depot has **no large pad**: the Clipper (large) cannot dock, so the Asp is the right
  hull for this job. Fitted for it 18:32–18:35 (collector limpet controller 3A, §2).

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

**Mechanics worth keeping:** the `Faction` on an on-foot mission does not tell you whose
settlement you are about to enter — check `ApproachSettlement`/the settlement's controlling
faction before landing. On a heist a scan alone is not stealth: being challenged and not
submitting is logged as a crime and turns the site hostile (§5.2 step 3, *cut the reactor first*,
is still the untried fix).

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

---

## 5. ROADMAP

Consolidated 23 September 2026: this section now absorbs the old §§8–10 (Imperial rank, on-foot protocol, engineering) and
the old §13 (Gutamaya Programme), plus a new
phased fleet plan Tonton Marcel wrote in French (`Reviews.md`) and asked to be merged in here as
a single set of tasks/checkpoints. Translated to English for consistency with the rest of this
file — ship names, module codes and engineer names are untouched; see the closing note in §5.7
for the source.

### 5.0 Guiding principles

**Gauges to raise**

| Gauge | Status | Target | Unlocks |
|---|---|---|---|
| Imperial Navy | Viscount | Duke (4 promotions) | Imperial Cutter |
| Aisling rank | Rank 5 / 16,424 merits | Rank 34 (≈247,000 merits) | Prismatic Shields |
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

- [ ] **Thursday (PP2 tick):** Aisling assignments.
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

Root cause of past failures identified: **the permission system**. Every door and terminal
requires level 1, 2 or 3 access, obtained by **cloning an NPC's profile with the Profile
Analyser**. Without it, every access attempt is a break-in → alarm → hostile settlement.

**Base loadout:** **Maverick** suit (not Dominator), Profile Analyser, E-Breach, Energylink.

**Progression**
1. **Abandoned settlement reactivation** missions — zero NPCs, zero alarms. Find the power
   distribution centre, insert the regulator. Learn the layout + gather micro-resources.
   - *A `Salvage`-tagged ground wreck is not this case, even though it looks similarly
     "abandoned" — see the new sub-step below (added 21 Sept, §4).*
2. **Data recovery** missions at powered-down sites.
3. **Cut the reactor** at an active settlement = alarms, lights and turrets offline. Master key
   for any infiltration. *Still untried — see §4, 21 Sept heist.* See the alarm-console note
   below — the console and the reactor usually share a building.
4. **Land more than 1 km away**, or arrive by Apex taxi. A ship landed inside the settlement
   triggers a scan, then hostility.
5. **Frontline conflict zones** before any on-foot bounty hunting: allies nearby, respawn at the
   dropship, failure costs nothing.

**New: hostile wreck salvage (added 21 Sept, §4).** A ground wreck carrying a `Salvage` mission
tag is not the "zero NPC, zero alarm" case of step 1 — it can spawn armed guards on arrival.
Treat it as contested from the start: approach from cover, engage at range, don't cross open
ground toward the objective marker. Confirmed the hard way: two deaths in a row on 21 Sept before
a third, careful attempt succeeded clean the same evening.

**Alarm console, and why "cut the reactor" isn't two problems (web-researched ahead of the
Phase 3 attempt, not yet play-tested — sources: Frontier forums stealth guide, ED Wiki).** The
alarm console is usually **inside the same Power Centre building as the reactor** (step 3) —
typically level 3 clearance — so disabling the alarm and cutting the reactor are often one
problem, not the two stacked ones they first look like. Order of leverage, cheapest first:
1. **Recon before committing** — walk/fly the perimeter, scan every NPC you can (puts them on
   radar), spot unguarded side entrances and power sockets before picking a route.
2. **Match the Profile Analyser clone's clearance** to that specific building (level 3, usually).
3. **Movement discipline over gunplay** — crouch/walk (footstep noise is a real detection input),
   use rooftops/cover to break line of sight, approach NPCs from behind (their vision cone
   doesn't cover their back).
4. A community tool, the **Odyssey Mapping Guide**, shows exact alarm-console/regulator
   locations per settlement layout — worth using for planning instead of learning each site by
   dying in it.
5. **No stun/incapacitation tool exists in the game** — confirmed, not a gear gap to engineer
   around.

**Where this fits in the plan:** the zero-risk steps (1–2, still pending — the 21 Sept session
played wreck-salvage and settlement-collect missions instead, see §4) sit in **Phase 1** alongside
the other risk-free grinding, since they need no rank/gear and plausibly feed the same
engineer-discovery pattern as the ship side (§5.4). The first real on-foot risk (step 3,
cut-the-reactor) sits in **Phase 3**, timed to match the rising ship-combat confidence built there
— deliberately not before confidence is re-established either way (§5.4).

### 5.3 Engineering & materials

Three ship-side stocks: **raw** · **manufactured** · **encoded**. Plus, separately, Odyssey
**micro-resources**.

| Category | Typical sources | Mainly used for |
|---|---|---|
| Encoded | Wake and ship scans, data sites, wrecks | FSD, shields, sensors |
| Manufactured | High-grade emissions (HGE), wrecks, combat | Weapons, distributor, armour |
| Raw | Surface prospecting in the SRV, geological formations | Thrusters, power plant, Frags |
| Guardian | Guardian sites | FSD booster, reinforcements, AX weapons |
| Conversion | Material traders (6-for-1 upward conversion — farm volume, convert afterward) | Rebalancing stock |
| Passive | Aisling PP rank rewards | Everything |

- **Farms:** HGE in boom-state systems (high-grade manufactured) · brain trees / crystalline
  shards (raw, in bulk) · abandoned settlements (micro-resources, no opposition).
- **3312 shortcut:** Operations rewards both ship **and** on-foot engineering materials, and Merc
  Coin buys modules and **engineering blueprints**.
- **Ship engineer priorities:** Farseer (FSD) · Martuuk · McQuinn or Nemo (weapons) · Qwent
  (power plant) · Vatermann (shields).
- **Odyssey engineer priorities:** Oden Geiger (data), Hero Ferrari (suit), Terra Velasquez.
- **On-foot gear** (suit/weapon engineering follows a track separate from ship engineering):
  - **Artemis** for exobiology (Phase 2, §5.4);
  - **Maverick** for sabotage and PP data;
  - **Dominator** for on-foot combat (Phase 3, §5.4).

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

**Ships**
- [ ] Astroforge v2 (annex A1, §5.7): 162 t, scoop and 3rd collector stored.
- [~] Dart v2 (annex A2) — hull bought 21 Sept (§2, §4); engineering not started.
- [x] Pacifier: bounties settled — impound cleared 23 Sept (`ClearImpound`, §4).
- [x] Pacifier: cargo racks swapped for hull/module reinforcements, an FSD interdictor, a
      planetary hangar and a multi-drone controller, plus a newly bought 3A fuel scoop (23 Sept,
      §4) — cargo down to 128 t.
- [ ] Pacifier v2 (annex A3), remaining: 7A Shield + 6A SCB, Kill Warrant Scanner swap.
- [ ] The Brick: It's the trade-merit engine. Optimize on mass, manoeuvrability, interdiction espaces

**Powerplay: ≈230,000 merits remaining to rank 34**
- [ ] PP trade with The Brick: high-margin sales in the targeted Aisling systems. Precise
      buy/sell rules to verify in the Powerplay interface.
- [ ] PP mining with Astroforge: mine and sell in the same reinforcement system.
- [ ] Light PP combat with Pacifier: Low RES in the reinforcement system. **Do not redeem the
      bounty vouchers this time** — carry them to Wolf 397 (Trophy Camp) once past 100k CR
      instead, for McQuinn's unlock donation (Engineers, below). **Expect this to be slow toward
      the 100k figure**: Low RES was chosen here for safety (Novice rank, survival-first per §2),
      not bounty density — "easier targets, lower payouts," and local security often kills wanted
      NPCs before you reach them. Treat the first session as a real data point (matches
      Checkpoint 1's "measure it" approach) rather than assuming a quick errand. If it's too slow
      and the Pacifier's shield/boosters are holding up, step up to a **regular RES** (not
      Hazardous — no security cover there, and the Pacifier isn't G3-engineered yet) for faster
      bounty income.

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

**On-foot** (protocol reference: §5.2) — same risk-free philosophy as the rest of this phase.
- [ ] **Abandoned-settlement reactivation** mission — zero NPCs, zero alarms. Gathers
      micro-resources and is the on-foot equivalent of the Low RES/PP loops above: safe, and a
      real data point for what it actually yields.
- [ ] **Data recovery** mission at a powered-down site — same risk profile, more data-type
      materials.
- Of the three Odyssey engineers named in §5.3, only **Hero Ferrari is "Known"**
  (`EngineerProgress`, 23 Sept) — Oden Geiger and Terra Velasquez aren't even that yet, the same
  situation as Vatermann/Cheung/Tani/Jean below. Whether these two on-foot missions are what
  reveals them is unconfirmed (same caveat as McQuinn) — worth re-checking `EngineerProgress`
  after running them.
- Also flagging: **Liz Ryder** (ship engineer, missile specialist — needed for the Dart's "High
  Capacity" missile blueprint, annex A2) is likewise only "Known," not yet invited.

**Engineers** — cross-checked against the journal `EngineerProgress` snapshot, 23 Sept 17:21:40
UTC (state, not the reveal *chain* — Frontier doesn't log which engineer reveals which).
- [x] Set Hyperion's FSD to G5. (Confirmed 23 Sept — Felicity Farseer, Deciat, §4.)
- [~] Hyperion thrusters G1 → G3, Dirty Drive Tuning + Overloaded (23 Sept, §4) — G5 (annex A4's
      target) not yet reached.
- [x] Elvira Martuuk — already **Unlocked, Grade 3** (`EngineerProgress`) — the "if not already
      unlocked" hedge from the first draft is resolved; access to Zacariah Nemo is open.
- [ ] **Tod McQuinn — status "Invited" (`EngineerProgress`), unlock needs 100,000 CR of
      *unclaimed* bounty vouchers donated at her base (Trophy Camp, Wolf 397) via its "donate"
      button — the normal redeem-at-a-station flow does NOT count.** Checked the journal (18–23
      Sept): she currently holds **zero unclaimed vouchers** — the three from 18 Sept
      (91,489 + 60,470 + 82,215 CR, Karsuki Ti) were already redeemed the ordinary way that same
      evening, and nothing's been earned since. So this is a **prerequisite of the Low RES task
      below, not parallel to it**: run Low RES first, this time *don't* redeem the bounty
      vouchers as usual, fly them to Trophy Camp instead once past 100k CR, and donate. First
      donation can be any faction's vouchers; later ones need his system/Alliance vouchers
      specifically (only matters once she's actually unlocked). Possibly what reveals the four
      engineers below too — unconfirmed, visit and see.
- [ ] Didi Vatermann (boosters G5), Lei Cheung (shield G5), Hera Tani (power plant G5), Selene
      Jean (hull & armour G5): **none of these four are even "Known" yet** on the engineer
      roster. Their rank conditions (Trade Merchant ✔, Navy Outsider ✔, etc.) being met isn't
      sufficient on its own — something else has to reveal them first. Re-check
      `EngineerProgress` after visiting McQuinn.

**Engineering to apply**
- [ ] Pacifier: shields and boosters to G3 minimum (Lei Cheung, Didi Vatermann).

**📍 Checkpoint 1 — the merit engines are running**
- [ ] Merits/h measured for The Brick, Astroforge and Pacifier. Pick the best loop.
- [ ] Pacifier: 10 Low RES sessions with no losses, combat rank at least Competent.
- [ ] Hyperion's FSD at G5, Pacifier's boosters and shield at G3+.

#### Phase 2 — Guardian expedition with Hyperion, no purchase

**Goal:** unlock Guardian technology for the whole fleet, and start exobiology (currently
Directionless), which funds what follows.

**Preparation**
- [ ] Hyperion v2 (annex A4, §5.7): missiles removed, AFMU 3A, FSD G5.
- [ ] On-foot gear: Artemis suit + Genetic Sampler (exobiology).

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

**Engineers**
- [~] The Dweller: already **Unlocked, Grade 1** (`EngineerProgress`, 23 Sept, §5.4) — grind to
      G5 for the distributor.
- [ ] Zacariah Nemo: Fragment Cannon G5, by Martuuk's invitation (Martuuk herself already
      unlocked, Grade 3 — see Phase 1, §5.4).
- [ ] Professor Palin: thrusters G5 (Dirty Drives).
- [ ] Tod McQuinn: Multi-Cannon G5 (useful for the Pacifier and later the Charybdis) — her base
      unlock moved up to Phase 1 (§5.4, status "Invited" as of 23 Sept); this is the later G5
      grind once the Nemesis is in the yard.

**Materials**
- [ ] Farm geared toward shields, Frags and thrusters (§5.3).

**Nemesis**
- [ ] Buy Corsair #1 (≈79.3M CR, no rank required). Name her Nemesis (annex B2, §5.7).
- [ ] Engineer in order: (1) Bi-Weave shield, boosters, Guardian reinforcements; (2) armour and
      hull; (3) distributor; (4) thrusters; (5) Frags.
- [ ] Transition: Pacifier runs Medium RES while the Nemesis is being engineered, then the
      Nemesis takes over.

**Missions**
- [ ] On-foot: **Frontline conflict zones** first (§5.2 step 5) — allies nearby, free respawns,
      failure costs nothing. Safe combat practice, mirroring the ship-side ramp (Pacifier Low RES
      → Nemesis HazRES) with the same "prove it safely before it counts" logic.
- [ ] On-foot: **cut-the-reactor infiltration** at an active settlement (§5.2 step 3) — the first
      real on-foot risk, timed to match the combat confidence built above. Still untried as of
      23 Sept (§4).
- [ ] Dominator suit (combat) or upgraded Maverick (sabotage, PP data) for Dart's missions.
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

- **A**: builds based on the real loadouts (Inara), including the bridge ships.
- **B**: target builds. The Corsair, Clipper and Courier use verified slot plans. The Cutters are
  specs whose slot plan is to be confirmed on first purchase.
- **All performance numbers still need to be computed in EDSY.**
- These JSON blocks were drafted outside EDSY and aren't EDSY-compatible as-is — adapt as needed.
- *Translated from Tonton Marcel's French draft (`Reviews.md`, 23 Sept 2026) — module codes,
  ship/engineer names and slot numbers are unchanged; only prose fields (role, principle, notes,
  checklists) were translated.*

**A1 — Astroforge v2 (Clipper, Phase 1)**

```json
{
  "ship": "Imperial Clipper",
  "name": "\"Astroforge\" CL-002",
  "role": "Laser mining, Powerplay 2.0 (Aisling, reinforcement) — Phase 1, no engineering",
  "slot_layout": "Optional slots 7/6/4/4/3/3/2/2/1 | 2L + 2M | 4 utility (slot 1 revealed by the Pacifier's export)",
  "principle": "PP2 reinforcement: mine and sell in the same system. Intra-system runs: no fuel scoop, cargo takes priority.",
  "hardpoints": [
    { "slot": "largehardpoint1", "module": "3E Beam Laser (Gimballed)" },
    { "slot": "largehardpoint2", "module": "3E Multi-Cannon (Gimballed)" },
    { "slot": "mediumhardpoint1", "module": "2D Mining Laser (Fixed)" },
    { "slot": "mediumhardpoint2", "module": "2D Mining Laser (Fixed)" }
  ],
  "utility_mounts": ["0I Chaff Launcher", "0F Electronic Countermeasure (anti hatch breakers)", "0A Shield Booster", "0A Shield Booster"],
  "core_internals": {
    "power_plant": "6C (upgrade to 6A if power saturates) — target: Overcharged",
    "thrusters": "6A — target: Dirty Drive Tuning",
    "frame_shift_drive": "5A — target: Increased Range + Mass Manager",
    "life_support": "5D", "power_distributor": "6A", "sensors": "5D",
    "fuel_tank": "4C (16 t)", "armour": "Lightweight Alloy"
  },
  "optional_internals": [
    { "slot": "size7", "module": "7E Cargo Rack (128 t)" },
    { "slot": "size6", "module": "6A Shield Generator" },
    { "slot": "size4", "module": "4E Cargo Rack (16 t)" },
    { "slot": "size4", "module": "4E Cargo Rack (16 t) — 4A scoop stored" },
    { "slot": "size3", "module": "3A Collector Limpet Controller" },
    { "slot": "size3", "module": "3A Collector Limpet Controller" },
    { "slot": "size2", "module": "2A Refinery" },
    { "slot": "size2", "module": "1A Hephaestus Limpet Controller" },
    { "slot": "size1", "module": "1E Cargo Rack (2 t) — slot currently empty" }
  ],
  "cargo_capacity": "162 t (≈20 limpets included)",
  "end_of_life": "Sold in Phase 5 once the Hephaestus beats her performance (profit/h and merits/h).",
  "variant_max_cargo": "Slot 6 as 6E Cargo (64 t) + 4A shield in slot 4: ≈208 t, quiet systems only",
  "power_priorities": { "1": "Thrusters, FSD, shield, life support, sensors", "2": "Mining lasers, limpets, refinery", "3": "Weapons, chaff, ECM" }
}
```

**A2 — Dart v2 (Courier, Phase 1)**

```json
{
  "ship": "Imperial Courier",
  "name": "\"Dart\" CO-01",
  "role": "Odyssey taxi + pre-landing support",
  "slot_layout": "Optional slots 3/3/2/2/2/1/1/1 | 3M | 4 utility",
  "hardpoints": [
    { "slot": "mediumhardpoint1", "module": "2F Pulse Laser (Gimballed)", "purpose": "Skimmers, SRV" },
    { "slot": "mediumhardpoint2", "module": "2F Pulse Laser (Gimballed)" },
    { "slot": "mediumhardpoint3", "module": "2B Missile Rack (Dumbfire)", "purpose": "Area damage against ground groups", "engineering_target": "High Capacity (Liz Ryder)" }
  ],
  "utility_mounts": ["0I Point Defence (automatic, even landed; ineffective against lasers)", "0I Chaff Launcher", "0A Shield Booster", "0A Shield Booster"],
  "core_internals": {
    "power_plant": "4A — target: Overcharged",
    "thrusters": "3A — target: Dirty Drive Tuning",
    "frame_shift_drive": "3A SCO — target: Increased Range + Mass Manager",
    "life_support": "1E", "power_distributor": "3A — target: Engine Focused",
    "sensors": "2E", "fuel_tank": "3C (8 t)", "armour": "Lightweight Alloy"
  },
  "optional_internals": [
    { "slot": "size3", "module": "3A Shield Generator" },
    { "slot": "size3", "module": "3E Cargo Rack (8 t)" },
    { "slot": "size2", "module": "2A Fuel Scoop" },
    { "slot": "size2", "module": "Planetary Vehicle Hangar + Scorpion SRV" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t)" },
    { "slot": "size1", "module": "Detailed Surface Scanner" },
    { "slot": "size1", "module": "1E Docking Computer or Supercruise Assist" },
    { "slot": "size1", "module": "1E Cargo Rack (2 t)" }
  ],
  "ground_support_doctrine": [
    "1. Support pass: lasers on skimmers and SRVs, missiles on groups",
    "2. Land out of range of defences",
    "3. Dismiss the ship to orbit during the on-foot phase",
    "4. Recall, another pass if needed, extraction"
  ]
}
```

**A3 — Pacifier v2 (Clipper, combat trainer, Phases 1–3)**

```json
{
  "ship": "Imperial Clipper",
  "name": "\"Pacifier\" CL-001",
  "role": "Combat trainer (low/medium RES, PP combat on isolated targets), then the base for the future Diplomat",
  "status": "Built from the real Inara loadout. (Was flagged Hot/impounded — cleared 23 Sept 2026, see §2, §4; no longer a blocker.)",
  "slot_layout": "Optional slots 7/6/4/4/3/3/2/2/1 | 2L + 2M | 4 utility",
  "principle": "Combat rank Novice: survival is prioritised (big shield + SCB + reinforcements) over damage. The current 186 t cargo hold is replaced with defence.",
  "changes_vs_current": [
    "6A shield moved from slot 6 to a 7A in slot 7 (purchase, ≈50M to verify); the old 6A is stored",
    "6A Shield Cell Bank in slot 6",
    "Cargo racks replaced with hull and module reinforcements",
    "One chaff launcher replaced with a Kill Warrant Scanner (bounty hunting)"
  ],
  "hardpoints": [
    { "slot": "largehardpoint1", "module": "3E Beam Laser (Gimballed)", "status": "Kept", "engineering_target": "Efficient or Short Range + Thermal Vent" },
    { "slot": "largehardpoint2", "module": "3E Beam Laser (Gimballed)", "status": "Kept", "engineering_target": "Efficient + Thermal Vent" },
    { "slot": "mediumhardpoint1", "module": "2E Multi-Cannon (Turret)", "status": "Kept", "engineering_target": "Overcharged + Corrosive Shell" },
    { "slot": "mediumhardpoint2", "module": "2E Multi-Cannon (Turret)", "status": "Kept", "engineering_target": "Overcharged + Incendiary Rounds" }
  ],
  "utility_mounts": ["0A Shield Booster (kept)", "0A Shield Booster (kept)", "0I Chaff Launcher (kept)", "0C Kill Warrant Scanner (new)"],
  "core_internals": {
    "power_plant": "6A (kept)",
    "thrusters": "6A (kept) — target: Dirty Drive Tuning",
    "frame_shift_drive": "5A Fast Boot G5 (kept; Increased Range on the switch to Diplomat)",
    "life_support": "5D", "power_distributor": "6A — target: Charge Enhanced",
    "sensors": "5D — target: Long Range", "fuel_tank": "4C",
    "armour": "Military Grade Composite (kept)"
  },
  "optional_internals": [
    { "slot": "size7", "module": "7A Shield Generator (new)" },
    { "slot": "size6", "module": "6A Shield Cell Bank (new)" },
    { "slot": "size4", "module": "4D Hull Reinforcement Package" },
    { "slot": "size4", "module": "4D Hull Reinforcement Package" },
    { "slot": "size3", "module": "3D Module Reinforcement Package" },
    { "slot": "size3", "module": "3D Hull Reinforcement Package" },
    { "slot": "size2", "module": "2A Fuel Scoop" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t) — mission salvage" },
    { "slot": "size1", "module": "1E Cargo Rack (2 t)" }
  ],
  "training_progression": [
    "1. Low RES in an Aisling reinforcement system (merits + bounties)",
    "2. Easy assassination missions, isolated PP targets",
    "3. Medium RES once shield and boosters are G3+",
    "4. Hand off to the Nemesis (Phase 3)"
  ],
  "end_of_life": "Becomes the Diplomat in Phase 6 (annex B4)."
}
```

**A4 — Hyperion v2 (Asp Explorer, exploration bridge ship, Guardian expedition)**

```json
{
  "ship": "Asp Explorer (bridge ship, non-Gutamaya)",
  "name": "\"Hyperion\" ASP-01",
  "role": "Expedition to Guardian sites (Phase 2) and exobiology, pending Marco Polo",
  "status": "Built from the real Inara loadout. No hull purchase needed.",
  "slot_layout": "Optional slots 6/5/3/3/3/2/2/1 | 2M + 4S | 4 utility",
  "changes_vs_current": [
    "Remove the 4 dumbfire missile racks (dead weight)",
    "Remove 2 of the 4 heat sink launchers",
    "FSD: Increased Range G4 → G5 (engineer already accessible, see The Brick)",
    "Add a 3A AFMU for self-sufficiency"
  ],
  "hardpoints": [
    { "slot": "mediumhardpoint1", "module": "2F Pulse Laser (Gimballed)", "status": "Kept (self-defence)" },
    { "slot": "mediumhardpoint2", "module": "2F Pulse Laser (Gimballed)", "status": "Kept" },
    { "slot": "smallhardpoint1-4", "module": "Empty" }
  ],
  "utility_mounts": ["0I Heatsink Launcher", "0I Heatsink Launcher", "empty", "empty"],
  "core_internals": {
    "power_plant": "5A Armoured G1 (kept)",
    "thrusters": "5A Clean G1 (kept)",
    "frame_shift_drive": "5A Increased Range G5 + Deep Charge",
    "life_support": "4D", "power_distributor": "4D", "sensors": "5D", "fuel_tank": "5C"
  },
  "optional_internals": [
    { "slot": "size6", "module": "6A Fuel Scoop (kept)" },
    { "slot": "size5", "module": "5D Shield Generator (kept)" },
    { "slot": "size3", "module": "3A AFMU (new)" },
    { "slot": "size3", "module": "3E Cargo Rack (8 t) — reserve for any artefacts" },
    { "slot": "size3", "module": "3A Collector Limpet Controller (kept, optional)" },
    { "slot": "size2", "module": "Planetary Vehicle Hangar + Scarab SRV (kept)" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t)" },
    { "slot": "size1", "module": "Detailed Surface Scanner — Expanded Probe Radius G5 (kept)" }
  ],
  "expedition_checklist": [
    "Artemis suit + Genetic Sampler for exobiology",
    "Unlock at the Tech Broker: Guardian FSD Booster + Guardian Shield Reinforcement",
    "Sell exploration and exobiology data in an Aisling system (merits)"
  ],
  "end_of_life": "Stored at the museum once Marco Polo v2 beats her range (Phase 6)."
}
```

**A5 — The Brick (Type-9, trade bridge ship)**

```json
{
  "ship": "Type-9 Heavy (bridge ship, non-Gutamaya)",
  "name": "\"The Brick\" T9-01",
  "role": "PP merit engine through trade, and trade/colonisation CGs, until the Cornucopia arrives",
  "status": "Current loadout kept: ≈758 t, 5A shield, FSD 6B Increased Range G5 + Deep Charge",
  "recommendations": [
    "No major changes: the ship is headed for retirement",
    "Option: FSD 6A SCO if the targeted CGs have stations far from the star (notable time save)",
    "Weapons left in place (deterrence) or removed for a little extra range"
  ],
  "end_of_life": "Stored at the Medupe City museum after a full trade CG run with the Cornucopia (Phase 5)."
}
```

**B1 — Marco Polo (Corsair, exploration)**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Marco Polo",
  "role": "Long-range exploration, exobiology, cartography",
  "replaces": "Hyperion (Asp Explorer) — retired once Marco Polo v2 beats her range",
  "kpi": "Jump range (reference value to measure in EDSY; the 81.5 ly of the initial build is to be confirmed)",
  "slot_layout": "Optional slots 6/6/6/5/5/5/4/3/2/1 | 3L + 3M | 4 utility | Core: PP7 T7 FSD5 LS4 PD7 S6 Fuel5",
  "versions": {
    "v1": "Straight away with FSD G5 and 5H Guardian booster (unlocked in Phase 2 by Hyperion)",
    "v2": "Full engineering"
  },
  "hardpoints": "Empty",
  "utility_mounts": ["0I Heatsink Launcher (Lightweight / Ammo Capacity)", "empty", "empty", "empty"],
  "core_internals": {
    "power_plant": "3A — Low Emissions + Stripped Down (check the power budget)",
    "thrusters": "7D — Dirty Drive Tuning + Stripped Down",
    "frame_shift_drive": "5A SCO — Increased Range + Mass Manager",
    "life_support": "4D Lightweight", "power_distributor": "5D Engine Focused + Stripped Down",
    "sensors": "6D Lightweight", "fuel_tank": "5C (32 t)", "armour": "Lightweight Alloy Heavy Duty + Deep Plating"
  },
  "optional_internals": [
    { "slot": "size6", "module": "6A Fuel Scoop" },
    { "slot": "size6", "module": "6A AFMU" },
    { "slot": "size6", "module": "5A AFMU (the two AFMUs repair each other)" },
    { "slot": "size5", "module": "5H Guardian FSD Booster (from v1.5)" },
    { "slot": "size5", "module": "5D Shield Generator — Enhanced Low Power + Stripped Down" },
    { "slot": "size5", "module": "Empty (or a small cargo hold)" },
    { "slot": "size4", "module": "4D Hull Reinforcement — Lightweight" },
    { "slot": "size3", "module": "Planetary Vehicle Hangar + Scarab SRV" },
    { "slot": "size2", "module": "1E Supercruise Assist" },
    { "slot": "size1", "module": "Detailed Surface Scanner — Expanded Probe Radius" }
  ]
}
```

**B2 — Nemesis (Corsair, combat)**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Nemesis",
  "role": "Bounties, assassinations, massacres, Operations, PP combat",
  "kpi": "TTK on a reference target class (HazRES) + survival",
  "slot_layout": "Optional slots 6/6/6/5/5/5/4/3/2/1 | 3L + 3M | 4 utility",
  "versions": {
    "v1": "Identical modules, no engineering: low/medium RES, isolated targets",
    "v2": "Engineering in order: shield, boosters, armour/hull, distributor, thrusters, Frags"
  },
  "hardpoints": [
    { "slot": "Large x2", "module": "3C Fragment Cannon (Gimballed) — Overcharged + Screening Shell" },
    { "slot": "Large x1", "module": "3C Fragment Cannon (Gimballed) — Overcharged + Incendiary Rounds" },
    { "slot": "Medium x2", "module": "2C Fragment Cannon (Gimballed) — Overcharged + Screening Shell" },
    { "slot": "Medium x1", "module": "2C Fragment Cannon (Gimballed) — Overcharged + Corrosive Shell" }
  ],
  "ammo_note": "6 Frags: short ammo endurance, plan for resupply or synthesis",
  "utility_mounts": ["0A Shield Booster — Heavy Duty + Super Capacitors", "0A Shield Booster — Resistance Augmented + Thermo Block", "0A Shield Booster — Thermal Resistant + Force Block", "0C Kill Warrant Scanner — Fast Scan"],
  "core_internals": {
    "power_plant": "7A Armoured + Thermal Spread",
    "thrusters": "7A Dirty Drive Tuning + Drag Drives",
    "frame_shift_drive": "5A SCO Increased Range + Mass Manager",
    "life_support": "4D Lightweight",
    "power_distributor": "7A Charge Enhanced + Super Conduits",
    "sensors": "6D Long Range",
    "armour": "Military Grade Composite Heavy Duty + Deep Plating"
  },
  "optional_internals": [
    { "slot": "size6", "module": "6C Bi-Weave — Thermal Resistant + Fast Charge (option: Prismatic after Aisling rank 34)" },
    { "slot": "size6", "module": "5D Guardian Shield Reinforcement" },
    { "slot": "size6", "module": "5D Guardian Shield Reinforcement" },
    { "slot": "size5", "module": "5A Shield Cell Bank" },
    { "slot": "size5", "module": "5D Hull Reinforcement — Heavy Duty + Deep Plating" },
    { "slot": "size5", "module": "4D Module Reinforcement" },
    { "slot": "size4", "module": "4D Hull Reinforcement — Heavy Duty" },
    { "slot": "size3", "module": "3D Module Reinforcement" },
    { "slot": "size2", "module": "2A Fuel Scoop" },
    { "slot": "size1", "module": "Empty or 1E Cargo" }
  ]
}
```

**B3 — Spectre (Courier, stealth)**

```json
{
  "ship": "Imperial Courier",
  "name": "Spectre",
  "role": "Smuggling, stealth missions, scans (datalinks, megaships), PP2 holo-screen piracy",
  "kpi": "Thermal signature, escape speed, t of contraband",
  "slot_layout": "Optional slots 3/3/2/2/2/1/1/1 | 3M | 4 utility",
  "hardpoints": [
    { "slot": "mediumhardpoint1", "module": "2F Pulse Laser (Gimballed) — Efficient" },
    { "slot": "mediumhardpoint2", "module": "Empty (weight / heat)" },
    { "slot": "mediumhardpoint3", "module": "Empty" }
  ],
  "utility_mounts": ["0I Heatsink Launcher — Ammo Capacity", "0I Heatsink Launcher — Ammo Capacity", "0I Chaff Launcher", "Data Link Scanner"],
  "core_internals": {
    "power_plant": "4A Low Emissions + Thermal Spread",
    "thrusters": "3A Dirty Drive Tuning + Drag Drives",
    "frame_shift_drive": "3A SCO Increased Range + Mass Manager",
    "life_support": "1E", "power_distributor": "3A Engine Focused",
    "sensors": "2E", "fuel_tank": "3C", "armour": "Lightweight Alloy Heavy Duty"
  },
  "optional_internals": [
    { "slot": "size3", "module": "3A Shield Generator (shut down under silent running)" },
    { "slot": "size3", "module": "3E Cargo Rack (8 t)" },
    { "slot": "size2", "module": "2A Fuel Scoop" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t)" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t)" },
    { "slot": "size1", "module": "Recon Limpet Controller (holo-screens, to verify in game)" },
    { "slot": "size1", "module": "1E Docking Computer" },
    { "slot": "size1", "module": "1E Cargo Rack (2 t)" }
  ],
  "cargo_capacity": "18 t"
}
```

**B4 — Diplomat (Clipper ex-Pacifier, PP logistics, Phase 6 target)**

```json
{
  "ship": "Imperial Clipper",
  "name": "Diplomat (ex-Pacifier)",
  "role": "Fast Powerplay logistics, escape",
  "kpi": "t/trip and laden jump range",
  "slot_layout": "Optional slots 7/6/4/4/3/3/2/2/1 | 2L + 2M | 4 utility (verified)",
  "inherited_from_pacifier": "6A power plant and 6A thrusters kept; Fast Boot G5 FSD to be re-engineered to Increased Range; Military Grade armour stored, replaced with Lightweight.",
  "corrections_vs_initial": "No size-5 slot and only one size-6 slot: impossible to combine 192 t cargo, a 6A scoop and a 5H booster. The max Guardian booster here is size 4, at the cost of the scoop or the shield.",
  "hardpoints": "Empty",
  "utility_mounts": ["0I Heatsink Launcher", "0I Chaff Launcher", "empty", "empty"],
  "core_internals": {
    "power_plant": "4A Low Emissions + Stripped Down",
    "thrusters": "6A Dirty Drive Tuning + Drag Drives",
    "frame_shift_drive": "5A SCO Increased Range + Mass Manager",
    "life_support": "5D Lightweight", "power_distributor": "5A Engine Focused + Super Conduits",
    "sensors": "5D Lightweight", "armour": "Lightweight Alloy Heavy Duty + Deep Plating"
  },
  "optional_internals": [
    { "slot": "size7", "module": "7E Cargo Rack (128 t)" },
    { "slot": "size6", "module": "6E Cargo Rack (64 t)" },
    { "slot": "size4", "module": "4A Fuel Scoop (or 4H Guardian FSD Booster)" },
    { "slot": "size4", "module": "4A Shield Generator — Enhanced Low Power" },
    { "slot": "size3", "module": "3E Cargo Rack (8 t)" },
    { "slot": "size3", "module": "3E Cargo Rack (8 t)" },
    { "slot": "size2", "module": "2E Cargo Rack (4 t)" },
    { "slot": "size2", "module": "1E Supercruise Assist" },
    { "slot": "size1", "module": "1E Cargo Rack (2 t)" }
  ],
  "cargo_capacity": "214 t",
  "note_pp2": "Power goods are allocated by quota: cargo capacity mostly matters for merit-generating trade."
}
```

**B5 — Soteria (Corsair, pad-M utility)**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Soteria",
  "role": "Medium-pad freight, passengers, salvage (variants stored at base)",
  "kpi": "Profit/h, t per trip",
  "slot_layout": "Optional slots 6/6/6/5/5/5/4/3/2/1 | 3L + 3M | 4 utility",
  "variants": {
    "freight": [
      "6E Cargo (64 t) x3", "5E Cargo (32 t)", "5A Shield Generator (or Prismatic 5)",
      "5E Cargo (32 t)", "4A Fuel Scoop", "3E Cargo (8 t)", "2E Cargo (4 t)", "1E Cargo (2 t)",
      "=> ≈270 t with shield and scoop (318 t max all-cargo, no shield)"
    ],
    "passengers": "Business/First cabins in slots 6 and 5 (the Corsair doesn't take Luxury cabins), 5-size shield, 4-size scoop",
    "salvage": "5A collectors in two size-5 slots, cargo in the size-6 slots, shield and scoop kept"
  },
  "hardpoints": "2 Multi-Cannons (Gimballed) in Large + the rest empty, or all empty in the pure-freight version",
  "core_internals": "7A thrusters Dirty Drives, 5A SCO Increased Range, 7A distributor Engine Focused, 7A power plant (downsize if possible)"
}
```

**B6 — Cornucopia (Cutter, bulk trade) — spec**

```json
{
  "ship": "Imperial Cutter",
  "name": "Cornucopia",
  "role": "Bulk trade, trade CGs, colonisation, PP trade",
  "replaces": "The Brick (Type-9) — retired after a full trade CG run with the Cornucopia",
  "kpi": "Profit/h",
  "slot_layout": "To confirm from the Inara export on first purchase",
  "corrections_vs_initial": [
    "Class-6 FSD (6A SCO), not 7A",
    "Number of size-5 slots to verify (the initial build counted three)"
  ],
  "key_modules": [
    "2x 8E Cargo (256 t) + cargo in every remaining available slot",
    "Prismatic 6A — Reinforced + Hi-Cap",
    "Guardian FSD Booster 5H",
    "1E Supercruise Assist",
    "Utility: Heavy Duty + Resistance Augmented boosters, Heatsink, Chaff"
  ],
  "core": "8A thrusters Dirty Drives + Drag Drives, 6A SCO Increased Range + Mass Manager, 7A distributor Engine Focused, 6A power plant Low Emissions",
  "hardpoints": "Empty"
}
```

**B7 — Hephaestus (Cutter, mining) — spec**

```json
{
  "ship": "Imperial Cutter",
  "name": "Hephaestus",
  "role": "PP2 laser mining and mining CGs; core and surface mining as variants",
  "kpi": "Profit/h, merits/h (reinforcement: mine and sell in the same system)",
  "slot_layout": "To confirm from the Inara export on first purchase",
  "key_modules": [
    "Medium mining lasers on the 4 medium hardpoints",
    "Defence weapons on the Huge and Large hardpoints",
    "Collector controllers (2 to 3), Hephaestus limpet controller, largest available refinery",
    "Prismatic 6A",
    "Cargo: 2x 8E",
    "Core variant: Pulse Wave Analyser (utility), Seismic Charges, Abrasion Blaster, Sub-Surface Displacement Missiles",
    "Surface variant: Mk II Large Planetary Vehicle Hangar + Rhino (the Cutter is compatible)"
  ],
  "note": "Surface-mining yield drops fast on the same site: deposits regenerate very slowly."
}
```

**B8 — Charybdis (Cutter, conflict zones) — spec**

```json
{
  "ship": "Imperial Cutter",
  "name": "Charybdis",
  "role": "Conflict zones (BGS, Powerplay, CGs), PvE tank",
  "kpi": "Survival in high-intensity CZs, combat obligations/h",
  "slot_layout": "To confirm from the Inara export on first purchase",
  "corrections_vs_initial": [
    "FSD 6A SCO (not 7A)",
    "Distributor 7A Charge Enhanced + Super Conduits (not 8A)",
    "The Gu-97 and the Imperial Fighter are two distinct fighters",
    "Kill Warrant Scanner useless in a CZ: a Heatsink instead (for the SCBs)"
  ],
  "key_modules": [
    "Huge: 4G Multi-Cannon (Gimballed) — Overcharged + Auto-Loader",
    "Large x2: Pulse Laser (Turret) — Long Range + Phasing Sequence",
    "Medium: 2x Multi-Cannon Incendiary, 1x Corrosive Shell (High Capacity), 1x Pulse Turret Scramble Spectrum",
    "Prismatic 8A — Reinforced + Hi-Cap",
    "SCB 8A + 6A, Heatsink",
    "Vessel Hangar (AI fighter)",
    "Guardian Shield Reinforcement, hull and module reinforcements"
  ],
  "core": "8A power plant Armoured + Thermal Spread, 8A thrusters Dirty Drives + Drag Drives, 7D sensors Long Range, Military Grade Composite"
}
```

**B9 — Aegis (Corsair, anti-Thargoid, optional) — spec**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Aegis",
  "role": "Anti-Thargoid, only for AX CGs",
  "kpi": "AX TTK, survival",
  "slot_layout": "Optional slots 6/6/6/5/5/5/4/3/2/1 | 3L + 3M | 4 utility",
  "key_modules": [
    "Guardian weapons (Tech Broker unlock, Guardian materials) and AX Multi-Cannons",
    "Decontamination and repair limpets",
    "Caustic Sink Launcher, Shutdown Field Neutraliser, Xeno Scanner as utility mounts",
    "Guardian hull and module reinforcements"
  ],
  "note": "Only take this on once every other line of the target-fleet table (§5.5) is covered."
}
```

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

*Last updated: 23 September 2026 (journal read through 21 Sept 18:28 UTC; Tonton Marcel's fleet
review and phased Gutamaya plan from `Reviews.md`, distributed into this file and cleared per
`CLAUDE.md` §3). To be completed session by session.*

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
