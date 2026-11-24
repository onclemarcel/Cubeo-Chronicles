# OPERATIONAL GUIDE — CMDR ONCLEMARCEL
## Campaign memory — status as of 19 November 2026 (3312), journal read through 19 Nov 20:56 UTC

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
> Community Goals split out 11 October 2026 per Tonton Marcel's request: standings, sources,
> cycles and forecasts moved to `Community Goals.md`; §4 and §5 keep a short summary per CG.

---

## 1. COMMANDER SHEET

| | |
|---|---|
| CMDR | Onclemarcel |
| Inara role | Freelancer / Scientist |
| Squadron | EliteCommanders |
| Trade rank | **Elite III** (rank 11, 19 Oct 2026) — **63 %** toward Elite IV (22 Nov 22:44). Elite II on 9 Oct, Elite on 16 Sept |
| Combat rank | **Expert** (since 14 Oct 2026, 23:17 UTC) — **83 %** toward Master (22 Nov 22:44) |
| Explorer rank | **Ranger** |
| Exobiologist rank | **Directionless** |
| Mercenary rank | **Mostly Defenceless** (since 29 Sept 2026) |
| Imperial Navy rank | **Marquis** (9 Nov 2026) — **92 %** toward **Duke** (22 Nov 22:44; 66 % on 19 Nov — the donation runs of 20–22 Nov) |
| Power | Aisling Duval — pledged, **Rank 56 / 428,222 merits** (22 Nov 2026, 21:37 UTC) — rank 51 on 18 Nov, 52 on 20 Nov, 53 on 21 Nov, 54–56 on 22 Nov |
| Home port | Cubeo — Medupe City |
| Treasury | **≈5,409,000,000 CR** (22 Nov 2026, 22:44 UTC `LoadGame`; ≈63M spent since 19 Nov — donations, transfers, suit grades). 19 Nov: 5,471.9M, +268M since 18 Nov, most likely the CG 866 reward. CG rewards: 859 (170M), 860 (220M), 861 (200M), 862 (310M), 863 (140M), 864 (250M), 865 (220M) — `Community Goals.md` |
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
| **Pacifier** (combat Clipper, `MA-10E`, ShipID 2) | Imperial Clipper | *Pacifier V2 refit, 6 Oct 2026; weapons changed 7 Oct (journal `Loadout` 06:57).* **Multi-Cannon (Large, Gimballed)** (stock, bought 7 Oct; replaces one beam, stored) · Beam Laser (Large, Gimballed), **Overcharged G3 + Flow Control** (The Dweller) · **2× Multi-Cannon (Medium, Gimballed)** (stock, 7 Oct; the turrets were sold) · **2× Shield Booster 0A, Heavy Duty G3 + Super Capacitors** (Lei Cheung) · **2× Heat Sink Launcher** (no chaff left since 7 Oct) · **Shield 7A, Reinforced G5 + Hi-Cap** (Lei Cheung, bought 6 Oct, 50.0M CR) · **Shield Cell Bank 6A** (bought 6 Oct, replaces the old 6A shield) · 2× Hull Reinforcement 4D · Module Reinforcement 3D + 1D · Fuel Scoop 3A · 2× Cargo Rack 2E (8 t) · **Distributor 6A, High Capacity G5 + Super Conduits** (The Dweller) · **Thrusters 6A, Dirty Drive G3 + Drag Drives** · **Power Plant 6A, Overcharged G1 + Thermal Spread** · **FSD 5A, Faster Boot G5 + Mass Manager** (Farseer) · Sensors 5D · Life Support 5D · Fuel Tank 4C · Armour grade 3 (Military Grade). Removed 6 Oct and stored: 7E cargo rack, FSD interdictor, planetary hangar, multi-drone controller. ~784.6 t, ~17.9 ly, Rebuy ≈7.1M CR. First combat test: CG 860, Redonesses (§4, 6 Oct). |
| **Dart** (Imperial Courier, ShipID 12, CO-01) | Imperial Courier | Bought 21 Sept 2026 (`ShipyardBuy`, 2,479,358 CR). *Dart V2 Tier 1 done 5 Oct 2026 (journal `Loadout` 6 Oct 06:50).* 2× Pulse Laser (Medium, Gimballed), **Lightweight G4 + Stripped Down** · Dumbfire Missile Rack (Medium) · Heat Sink Launcher (replaces the point defence) · Chaff · **2× Shield Booster 0D, Resistance Augmented G3 + Super Capacitors** · **Shield 3D, Reinforced G5 + Hi-Cap** · **FSD 3A SCO, Increased Range G5 + Deep Charge** · **Distributor 3D, Engine Focused G5 + Super Conduits** · **Thrusters 3D, Dirty Drive G3 + Drag Drives** · **Power Plant 4D, Overcharged G1 + Stripped Down** · **Sensors 2D, Lightweight G5** (60 % roll) · Life Support 1D · Fuel Tank 2C · Fuel Scoop 3A · Planetary hangar 2G · Collector Limpet Controller 1D · DSS Expanded G3 · 10 t cargo racks · Armour grade 1. **68.76 t, 38.8 ly unladen**, Rebuy ≈231k CR. Engineered A-rated modules stored, not sold. Note: every `Loadout` since 1 Oct reports the thrusters as switched off (`On: false`), yet the Dart has flown ~150 jumps since — most likely a journal/Inara reporting quirk, not a real fault. |
| **The Brick** (Type-9, `ON-16T`, ShipID 11) | Type-9 Heavy | 758 t cargo · 26.49 ly · FSD 6B, Increased Range g5 + Deep Charge · Power Plant 6A · Thrusters 6A · Distributor 6A · Shield 5A · Sensors 4E · 3 medium + 2 small gimballed weapons · Armour grade 1. **Back at Medupe City since 29 Oct** (CG 864 at Homer Platform, AD Leonis, 24–29 Oct) — bridge ship for bulk trade until the Cornucopia (Phase 5, §5). **V2 refit done 30 Sept** (`Shipyard.md`, annex A5): the loadout above is the *original* one. The V2 fit (no weapons, 7A Dirty Drive thrusters, 6A SCO FSD G5, 35.2 ly) is in the Shipyard card. **Since 9 Oct:** back to **758 t** (6E cargo rack in place of the 2 Oct fuel scoop) and a 6C fuel tank (§4). |
| **Hyperion** (Asp Explorer, `MA-07A`, ShipID 4) | Asp Explorer | **Retiring** (decided 7 Oct): the Marco Polo flies the Guardian expedition. **DSS removed and moved to the Marco Polo, 8 Oct.** Last `Loadout` (8 Oct): **53.6 ly**. FSD 5A Increased Range G5 + Deep Charge · Thrusters Dirty Drive G3 + Overloaded · Power Plant 5A Armoured G1 · Fuel Scoop 6A · Planetary hangar 2D · Shield 5D · 20 t cargo · Collector Limpet Controller 3A · Life Support 4D · Distributor 4D · Sensors 5D · 4× Heat Sink Launcher; rescue-run weapons possibly still fitted (2× pulse laser, dumbfire racks — check before storing). Next: strip and store at the Medupe City museum (`Shipyard.md`). |
| **Marco Polo** (Corsair, `MA-08C`, ShipID 16) | Corsair | **Bought 8 Oct 2026** at Crevenna's Folly (Col 285 Sector AC-H b12-1), 77,322,128 CR; engineered the same morning (journal `Loadout` 10:00). Named **"MARCO POLO"** in game on 8 Oct 10:15 (`SetUserShipName`). **Power Plant 4D, Overcharged G1 + Stripped Down** (Farseer) · **Thrusters 5D, Dirty Drive G3 + Drag Drives** (Farseer) · **FSD 5A SCO, Increased Range G5 + Mass Manager** (Farseer) · **Distributor 5D, High Capacity G5 + Stripped Down** (The Dweller) · **Sensors 6D, Lightweight G5** (Lei Cheung) · **Shield 5D, Reinforced G5 + Stripped Down** (Lei Cheung) · Life Support 4D · Fuel Tank 4C (16 t) · Fuel Scoop 6A · **2× AFMU 6A** · Hull Reinforcement 4D · Planetary hangar 2D · **DSS Expanded G5 (the Hyperion's, moved 8 Oct)** · Heat Sink Launcher · 72 t cargo racks (2× 5E + 3E) · Lightweight Alloy armour. **63.4 ly**, 339.5 t, Rebuy ≈7.0M CR. ⚠ Power: the second AFMU can't be powered with the G1 power plant (Shipyard card). **19 Oct `Loadout`:** 208 t of cargo racks, 6A fuel scoop, multi-drone controller, planetary hangar, DSS Expanded G5, FSD Increased Range G5 — **341.5 t, 66.5 ly**. |
| **Nemesis** (Corsair, ShipID 18) | Corsair | **Bought 15 Oct 2026** at Kenig City (ICZ EG-O b6-2), 74,961,584 CR hull; outfitted and engineered the same night (journal `Loadout` 15 Oct 03:09). *Refitted 19 Oct (journal `Loadout` 11:54 + `EngineerCraft` 12:01–12:32); Prismatic and limpets 13 Nov (journal `Loadout` 14 Nov 14:12).* **Multi-Cannon (Large, Gimballed), Overcharged G5 + Auto Loader** (McQuinn) · **2× Pulse Laser (Large, Gimballed), Overcharged G4 + Oversized** (The Dweller) · **3× Multi-Cannon (Medium, Gimballed), Overcharged G5** — 2× Corrosive Shell + 1× Incendiary (McQuinn, experimentals 19 Oct) · **3× Shield Booster 0A, Heavy Duty G3 + Super Capacitors** (Lei Cheung) · Heat Sink Launcher · **Prismatic Shield 6A, Reinforced G5 + Hi-Cap** (bought 13 Nov at Hencke Orbital, 23,662,565 CR; the old 6A Reinforced G5 + Hi-Cap shield is stored there) · **Shield Cell Bank 6A** (back in its slot 24 Oct, in place of the 19 Oct fuel scoop) · **3× Hull Reinforcement 5D** · **Module Reinforcement 5E + 4E** · **Cargo Racks 3E + 2E (12 t) + Collection Limpet Controller 1B** (refit 20 Nov at Roentgen Orbital, HR 5632, for PP rescue drops and convoys — journal `Loadout` 17:06; the Recon Limpet Controller 3E of 13 Nov is stored at Medupe City; **868.8 t, 17.8 ly**) · **Distributor 7A, High Capacity G5 + Cluster Capacitors** (The Dweller) · **Thrusters 7A, Dirty Drive G3 + Drag Drives** (Farseer) · **Power Plant 7A, Overcharged G1 + Monstered** (Farseer) · **FSD 5A SCO, Faster Boot G5 + Double Braced** (Martuuk, 19 Oct; the Increased Range FSD is back on the Marco Polo) · **Sensors 6A, Lightweight G3** · Life Support 4A · Fuel Tank 5C · Mirrored Surface Composite armour. **776.8 t, 17.3 ly** before the Faster Boot pass (11:54 `Loadout`). 842.8 t on 15 Oct → 810.8 t on 16 Oct → 776.8 t. |

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

### 18 September — CG 859 Closed, Fleet Regrouped (journal-verified)

- **18 Sept — CG 859 closed (Metz Enterprise, Ega):** **15,918 units, Top 25 %, 170,000,000 CR**
  collected on the spot (07:18). Card: `Community Goals.md`.
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
Merits 51,734 → **75,257** (+23,523; **rank 9 → 12**: 10 at 12:11, 11 at 14:51, 12 at 17:21).

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
- **First PP mining test, Astroforge, 18:46–20:17:** 88 limpets bought at Kenig City. HIP 5700
  (Stronghold): dropped into a Hazardous RES of the A 2 A Ring, not the Platinum hotspot (ring
  not mapped with the DSS). 29 t refined (silver, gold, coltan…), sold at Kaiser's Journey →
  **381 merits**. ICZ DG-O b6-3 (Exploited): 25 t (tritium, ices…), sold at Noel Station →
  **120 merits**. 61 asteroids prospected, no Platinum, no LTD. Result: **merits =
  floor(sale / 2,560)** and Strongholds pay for mining (`Powerplay Missions.md` §3). Merits
  74,756 → 75,257.

### 2 October — Second Mining Test, the Gallium Contract (journal-verified)

Source: journal file of 2 Oct, 06:31–11:28 UTC. Merits unchanged (75,257).

- **Astroforge, HIP 32674 A 10 B Ring (Stronghold), 06:31–08:20:** a second mining session, with
  the first Low Temperature Diamonds of the campaign. One wanted Krait Phantom destroyed on the
  way (200 CR bounty). Sold at **Raimi Hub (HIP 11402, also a Stronghold)** 08:27: 2 LTD at
  379,672 CR, 24 silver, 15 gold, 2 gallite, 3 water → ≈2.8M CR, **0 merits**. Mined in one
  system and sold in another, so this confirms the "mine and sell in the same system" rule
  (`Powerplay Missions.md` §3).
- **Gallium contract, Prismatic Imperium (10:18–11:26):** `Mission_Collect_Industrial`, 980 t of
  Gallium for Medupe City (offered 50M CR). The Brick: a 6A fuel scoop replaces a 6E cargo rack
  (28.0M CR, cargo 758 → 694 t). Two runs to **News Germany - A 3** (Col 285 Sector OX-Q a48-0),
  694 t bought each time at 2,413 CR. Delivered 980 t: **46M CR + 10 Imperial Shielding** (the
  4M CR gap is the materials option). Sold the 408 t surplus at Medupe City at 26,779 CR →
  ≈9.9M CR profit. Imperial Navy progress 86 % → 87 %.

### 3 October — Donations to the Empire, a Black Box, First HGE Farming (journal-verified)

Source: journal files of 3 Oct, 08:16–14:35 UTC. Merits 75,257 → **75,458** (rank 12).

- **Imperial Navy push — eight altruism donations:** four for Prismatic Imperium at Medupe City
  (08:17, 3.575M CR) and four at **Olahus Hub (Kou Hua)** for Kou Hua Empire League and
  Heaven's Judgment (10:10, 3.025M CR). Navy progress 87 % → 91 % → **95 %** toward Count. The
  Cubeo batch paid no merits; the Kou Hua batch paid **+194**.
- **Dart, illegal salvage at HIP 3254 (08:18–10:01):** `MISSION_Salvage_Illegal` from Prismatic
  Imperium, a black box. Collector limpet controllers fitted for the job. One NPC interdiction
  escaped on the way (08:25). High Grade Emissions there → **81 Imperial Shielding**. Paid
  75,991 CR + 6 Hybrid Capacitors (offered 535,991 — materials option again).
- **Olahus Hub, manufactured trader:** 100 Imperial Shielding → 15 Proprietary Composites, 20
  Configurable Components, 15 Conductive Polymers.
- **Afternoon:** the Dart gets an SRV hangar and the DSS back; an HGE at **Shapsugabus** → 90
  Proto Heat Radiators. First Dart V2 pass at **Farseer Inc** (14:29): Dirty Drive G3 + Drag
  Drives, FSD G4 + Deep Charge, boosters and power plant G1 + experimentals, DSS started.

### 4–5 October — Raw and Encoded Materials, Dart V2 Tier 1 Completed (journal-verified)

Source: journal files of 4 Oct, 06:15–15:43 UTC, and 5 Oct, 12:27–18:39 UTC. No merits.

- **Raw materials, Koli Discii C 6 a (4 Oct, plus 5 Oct morning):** the Dart landed next to a
  crashed ship at 07:59, then SRV farming over five game sessions (re-logs to respawn the
  deposits): **204 raw** — 42 zirconium, 27 tungsten, 42 tellurium, 30 ruthenium, 63 antimony.
- **Material traders, 5 Oct:** Zahn Enterprise (Cennicenino, raw): 28 antimony → **42 Arsenic**,
  10 ruthenium → **30 Cadmium**, plus manganese, zinc, germanium, boron, mercury. Bernoulli
  Vision (Caeritis, encoded): Datamined Wake Exceptions. Chandler Ring (Karka, manufactured):
  **8 Improvised Components**, 27 Heat Resistant Ceramics, Thermic Alloys, Biotech Conductors.
  The two big Dart V2 shortfalls (Arsenic ×9, Cadmium ×9) are now covered several times over.
- **Dart V2 Tier 1, 13:21–18:19:** FSD G5 at Farseer; D-rated modules bought at Farseer Inc,
  Garay Terminal (Deciat) and Elvey Platform (HIP 38236), engineered A-rated modules stored;
  The Dweller (Black Hide): pulse lasers Lightweight G4 + Stripped Down, distributor Engine
  Focused G5 + Super Conduits; Lei Cheung (Trader's Rest): sensors Lightweight G5, shield
  Reinforced G5 + Hi-Cap, boosters Resistance Augmented G3 + Super Capacitors. Jump range
  **23.6 → 38.8 ly**. One NPC interdiction escaped (17:53). Fit in §2.
- **Encoded materials, Jameson crash site (HIP 12099 1 b), 5 Oct evening and 6 Oct morning:**
  SRV runs → 282 Encryption Archives, 195 Adaptive Encryptors, 45 Modified Consumer Firmware,
  57 Cracked Industrial Firmware. Traded down at **Ray Gateway (Diaguandri)** and **Smoot
  Station (Chona)**: Datamined Wake Exceptions, Security Firmware Patches, Shield Frequency
  Data, Classified Scan Fragments and more. A 2,000 CR fine to Aisling's Angels paid at Smoot.

### 6 October — Pacifier V2 and a First Combat CG, Redonesses (journal-verified)

Source: journal files of 6 Oct, 06:15–15:04 UTC. No merits.

- **Materials, morning (Dart):** HGE at Shapsugabus → 81 Proto Heat Radiators; Olahus Hub →
  12 Proto Light Alloys, 10 Proto Radiolic Alloys (the two Dart/Marco Polo shortfalls).
- **Pacifier V2 refit (07:34–12:13):** at Kenig City, 7A shield (50.0M CR) in place of the 7E
  cargo rack, 6A shield cell bank in place of the old 6A shield (3.4M CR), heat sink in place of
  one chaff; FSD interdictor, planetary hangar and multi-drone controller stored, module and
  hull reinforcements added. HGE at HIP 3254 in the Pacifier (09:51) → 102 Imperial Shielding.
  Engineers: Lei Cheung (shield Reinforced G5 + Hi-Cap, boosters Heavy Duty G3 + Super
  Capacitors), The Dweller (distributor High Capacity G5 + Super Conduits, beams Overcharged
  G3 + Flow Control), Farseer (Dirty Drive G3 + Drag Drives, FSD Faster Boot G5 + Mass
  Manager, power plant Overcharged G1 + Thermal Spread); the shield's last G5 rolls done
  remotely from Chandler Ring at 12:13. Fit in §2.
- **CG 860, Redonesses, 12:38–15:02 — the first combat CG:** bounty hunting at a prison megaship
  (13 wanted ships, 5.07M CR — bounties turned out not to count), then four low-intensity and one
  medium-intensity conflict zone for Redonesses Defence Party (20 kill bonds, 2.59M CR). Shields
  lost six times, lowest hull **58 %**, three heat warnings, no death. Tonton Marcel's account:
  the beams run the capacitor dry, the turreted multi-cannons barely scratch. Bracket Top 75 %.
  Details: `Community Goals.md`, CG 860.

**Raw material for future `Logbook.md` days** (real play, not yet drafted): the Viscountess
paying her way back into the Navy's good graces with charity; a black box pulled from a wreck
for her own faction, with "illegal" written on the contract; days spent on the ground beside a
dead ship at Koli Discii and at Jameson's grave, picking up what's left; the Pacifier fitted
for survival, then her first real fight — a prison ship full of wanted pilots, then a conflict
zone where the shields go down six times and hold.


### 7 October — CG 860, the New Fit Works (journal-verified)

Source: journal file of 7 Oct, 06:15–15:45 UTC. No merits.

- **Weapons reworked, 06:19–06:57:** at Sword of Iustitia, the two turreted medium
  multi-cannons sold and replaced with **gimballed** ones (55,575 CR each); at Crevenna's Folly
  (Col 285 Sector AC-H b12-1), one large beam stored and replaced with a **large gimballed
  multi-cannon** (563,976 CR); the last chaff swapped for a second heat sink launcher (two heat
  sinks synthesised as well). Result: one beam for shields, three multi-cannons for hull.
  Tonton Marcel's verdict: the change works.
- **CG 860, ~9.5 h on and off:** 18 low-intensity and 2 medium-intensity conflict zones,
  **107 kill bonds** cashed in 12 trips to Sword of Iustitia (13.58M CR). Bracket **Top 75 % →
  Top 25 %** (details: `Community Goals.md`, CG 860).
- **Damage:** shields lost six times, lowest hull **58 %** (14:54), no death. Repairs and ammo
  ≈166k CR. Four interdictions by the other side (Redonesses Gold Comms Services, mostly its
  system defence force): three submitted, none lost.
- **Combat rank:** progress toward Expert 9 % → 25 % (6 Oct session) → **83 %** (this one).
- **Evening session, 17:15–18:33:** four more low-intensity zones, 24 kill bonds. Closest call
  of the CG: hull **35 %** at 18:29 before jumping out. Still Top 25 %.
- **Metrics:** every zone of the CG rebuilt from the journal with `tools/combat_stats.py` —
  summary in Checkpoint 1 (§5.4).

**Raw material for future `Logbook.md` days:** the day the Pacifier learns to fight — the beam
kept for shields, the guns swapped for ones that actually track, and a hundred kills in one
long shift. The CG bracket climbing from the bottom quarter to the top quarter of 8,000 pilots.


### 8 October — The Marco Polo, Bought and Engineered in a Morning (journal-verified)

Source: journal files of 8 Oct, 06:15–10:01 UTC. No merits.

- **Purchase, 06:23:** Corsair bought at **Crevenna's Folly** (Col 285 Sector AC-H b12-1) for
  **77,322,128 CR**, the Pacifier stored there. Stock core swapped for D-rated modules, the 5A
  SCO FSD (5.97M CR), a 6A fuel scoop (28.0M CR), **two 6A AFMUs (14.9M CR each)**, a 5D
  shield, a 4D hull reinforcement, an SRV hangar, a DSS and a heat sink launcher; 72 t of cargo
  racks. First `Loadout`: 38.3 ly before engineering.
- **Material trades:** Hale Port (G 180-18, manufactured): Chemical Manipulators ×2, Military
  Supercapacitors ×4; Gooch Terminal (LHS 246, raw): Chromium ×6, Manganese ×12 — the four
  Tier 1 shortfalls covered, at traders on the way instead of Zahn / Olahus Hub.
- **Engineering, 06:57–09:33:** The Dweller (distributor High Capacity G5 + Stripped Down), Lei
  Cheung (shield Reinforced G5 + Stripped Down, sensors Lightweight G5), Farseer (thrusters
  Dirty Drive G3 + Drag Drives, FSD Increased Range G5 + Mass Manager, power plant Overcharged
  G1 + Stripped Down). Jump range **38.3 → 58.6 ly** after the Dweller and Lei Cheung, **63.4 ly**
  at the end.
- **Home, 09:57:** docked at Medupe City; the Pacifier transferred back from Crevenna's Folly
  (3.27M CR, ~70 min). The **Hyperion's DSS** (Expanded G5) moved to the Marco Polo, the
  bought one stored.
- **Travel benchmark:** 16 jumps, 791 ly, average **49.5 ly**, best 60.9 ly; about **3,200 ly per
  hour** of route time — 1.5× the Hyperion, 3× the Dart (`tools/travel_stats.py`, card in
  `Shipyard.md`).
- **CG 860** ended 8 Oct 10:00 UTC — **Top 25 %** (`Community Goals.md`).
- **10:15–10:39, first long trip:** ship named "MARCO POLO", then Cubeo → Redonesses → Cubeo to
  collect the CG reward: **7 jumps / ~400 ly each way, about 5 minutes of jumping each way**
  (≈4,000 ly/h), 24 minutes dock to dock including the stop. Nothing to collect yet: the CG
  was not finalised.

**Raw material for future `Logbook.md` days:** the first Corsair — a Gutamaya hull, not a bridge
ship — bought, stripped to the bone and rebuilt by three engineers before lunch; the Hyperion
giving up her surface scanner, the first sign she's being let go.


### 8–10 October — CG 860 Paid, CG 861 Hauled (journal-verified)

Source: journal files of 8 Oct (20:11–22:11 UTC), 9 Oct and 10 Oct (to 23:36 UTC). No merits.

- **8 Oct evening, Marco Polo:** flew to **Zero Squared (HIP 74116)**, then HR 5518 (Grushin
  Prospect), where she requested The Brick's transfer from Medupe City (5.42M CR, ~78 min).
  On to Redonesses meanwhile: **CG 860 reward collected, 220,000,000 CR** (Top 25 %, 21:26).
  Back at Grushin Prospect for the night.
- **9 Oct, The Brick back to 758 t:** the 6A fuel scoop swapped back for a 6E cargo rack.
- **CG 861 — "Brewer Corporation Jump Satellite Initiative", 9–10 Oct:** The Brick hauls
  Superconductors to the megaship **Zero Squared (HIP 74116)** — 14 runs from Thorn
  Constructions (HR 5518) on 9 Oct morning, until other commanders had emptied its market, then
  21 runs from **Vercher Survey** (Col 285 Sector US-B b29-3), topping up with Power Generators
  once Superconductors only trickled back between visits. **35 runs of 758 t, ≈13 min each,
  ≈1.36 billion CR of trade profit**; six sessions, the last one 21:25–23:36 on 10 Oct.
- **Along the way:** two near-empty fuel arrivals on 9 Oct → a 6C fuel tank fitted at Vercher
  (`Shipyard.md`, The Brick); four NPC interdictions, none costly.
- **Result: 26,530 t, Top 25 %** — the bracket went back and forth with the night shifts of
  thousands of pilots. Standings, sources and forecasts: `Community Goals.md`, CG 861.

**Raw material for future `Logbook.md` days:** a 220-million reward cashed on the way to the next
job; a heavy hauler shuttling between an outpost and a megaship all morning, emptying a market
alongside thousands of other pilots for a corporation's satellite programme.


### 11 October — CG 861 Paid, Back in the Marco Polo (journal-verified)

Source: journal file of 11 Oct, 13:47–13:59 UTC. No merits.

- **CG 861 complete** (200M target met overnight, 11,810 contributors): Onclemarcel finishes
  **Top 25 %** — the third Top 25 % in three CGs since the return. Reward **200,000,000 CR**
  collected aboard The Brick at Zero Squared (13:48). The SCO FSD rewards are not in storage
  yet (open item, `Community Goals.md`).
- **The Brick stood down:** two jumps to Grushin Prospect (HR 5518), swapped into the Marco
  Polo (13:57); The Brick stays stored there.

**Raw material for future `Logbook.md` days:** a third reward from a third campaign, collected in
the hold of the ship that earned it; the heavy hauler left at an outpost, the Corsair taken back.

### 12–13 October — Four Assignments in One Night, the Alpha Centauri Wreck Left Alone (journal-verified)

Source: journal file of 12–13 Oct, 23:28–03:17 UTC. PP week of the 8 Oct tick —
detail in `Powerplay Missions.md` §1. **+17,452 merits** (75,433 → 92,885), **Rank 12 → 14**.

- **Rare goods, Marco Polo:** out of Grushin Prospect (HR 5518) at 23:38, back into Aisling
  space; 18 Karsuki Locusts at West Market (Karsuki Ti), sold at Fan Base (HIP 7311) 23:56 —
  **+3,600, Rank 13**.
- **Alpha Centauri, given up:** via Khepri (Banks Port, refit 00:07–00:10) to Alpha Centauri
  (Aisling Stronghold, six Powers present); limpets bought at al-Din Prospect (00:18). The
  salvageable wreckage lay **≈800,000 Ls** out — not worth a 2,800-merit assignment. Back to
  Khepri at 00:30.
- **Sealed contracts:** 30 collected at Wheelock Settlement (Zeaex), delivered at Banks Port
  (Khepri, undermined) 00:48 — **+2,000**.
- **Holoscreens:** 7 hacks at Newton Port (Khepri) for loose merits (126 each), then the
  assignment proper at **Wilson Stop, Chinga** (Lavigny-Duval): 9 hacks (8 paid), nine 2,000 CR fines,
  **+4,800 and Rank 14** at 01:48.
- **Navy donations at Medupe City:** four at 01:19–01:20 (3.575M CR) and eight at 03:15 (7M CR)
  for Cubeo Patron's Principles and Nexus Heavy Industries — ≈10.6M CR toward Count (§5.4).
- **On foot, the Dart:** Power containers emptied at **Savko Nutrition Habitat** (Kremovi,
  Lavigny-Duval) — an 800 CR trespass fine on the first approach at Verne Landing. Two trips to
  Reid Gateway (Oshanla): 7 items (02:46), then 5 more (03:08) — **+4,800**. (The journal
  wrote a second +4,800 there; the next login's total shows it was a duplicate line.)
- Logged off at Medupe City, 03:17.

**Raw material for future `Logbook.md` days:** a night of small errands for Aisling across the
border — locusts, sealed contracts, rival adverts hijacked under the nose of Lavigny's Legion,
goods lifted from a Lavigny settlement on foot; a wreck at humanity's oldest neighbour star left
where it lay because it was too far out; ten million credits given away to buy the Navy's notice.

### 13–14 October — The Navy Bar Full, Count at Last (journal-verified)

Source: journal files of 13 Oct (22:21–23:12 UTC) and 14 Oct (02:23–04:12 UTC).

- **13 Oct evening, The Brick:** Imperial Navy bar at **100 %** at login. Six industrial supply
  missions for Cubeo Patron's Principles and Nexus Heavy Industries (gold, superconductors,
  tritium, steel, insulating membrane), bought at McQuarrie Landing and Fefra's Legacy, handed in
  at Medupe City 22:55 — **≈25.5M CR**. Then the Marco Polo to Zero Squared; 29,437 CR of fines
  paid (23:11).
- **14 Oct night, Marco Polo:** two donations, then a megaship-uplink hack for Prismatic
  Imperium (Silinqang, 1.49M CR, +936 merits). Cargo racks and a multi-drone controller fitted
  back at Medupe City.
- **Promotion to Count, 03:03:** Prismatic Imperium offered the promotion mission — a courier
  run for the Imperial fleet intelligence service to Sellers Vista (Shui Wei Sector DG-O b6-4).
- **Afterwards:** a black box recovered at Iktock for Prismatic Imperium (0.40M CR); three
  delivery missions at Sellers Vista (gold, indium, tritium — ≈35.4M CR); about **28M CR** of
  donations to five Imperial factions (Hernovacle Crimson Galactic's civil-unrest appeals
  among them), starting the climb toward Earl.

**Raw material for future `Logbook.md` days:** the bar full at last, and the promotion arrives
not as a ceremony but as a sealed envelope carried to an outpost for Naval Intelligence; a
Countess by the morning, already paying for the next title.

### 14–15 October — Osane Pirates, the Pacifier Outgunned, the Nemesis Born (journal-verified)

Source: journal files of 14 Oct 22:03 → 15 Oct 03:57 UTC (two sessions).

- **Donations at Kessel Platform (HIP 3254):** ten more (≈7.4M CR) — **Aisling Rank 15**
  (22:22).
- **Massacre stack, Osane (Aisling Stronghold):** five wing-massacre missions against the
  pirates of the Family of Osane — Cubeo Patron's Principles (35, 30 kills) and Prismatic
  Imperium (56, 25, 35); **≈87.3M CR** in all.
- **Pacifier, 22:33–00:10:** ten "Target" signals at Osane 1 — each an Anaconda whose
  escorts (4–5 Eagles and Cobras) all jump in at once when it's attacked. 37 kills, hull down
  to 40 % twice; three stops at Kemurdzhian Terminal (HIP 1914), a 3A shield cell bank bought
  there (23:37). **Combat rank Expert at 23:17.** The first mission (Cubeo, 35 kills) paid
  16.9M CR at 00:26; **6.38M CR of bounties redeemed** at Kessel Platform.
- **The Nemesis, 00:31–03:09:** a second Corsair bought at Kenig City (ICZ EG-O b6-2), fitted out on
  the spot, then a tour of the engineers: Lei Cheung (shield G5, boosters G3), The Dweller
  (distributor G5, lasers G4 + Oversized — The Dweller now **G5**), Farseer (thrusters G3,
  power plant, sensors). Fit in §2.
- **Nemesis first sortie, 03:17–03:51, Osane:** four Target signals, 17 kills, no hull alarm.
  Firepower good; **handling poor** — the Eagles keep turning inside her. **3.47M CR of bounty
  vouchers left unclaimed.** Logged off at Kessel Platform. Four massacre missions still open
  (expire ≈21 Oct).
- **Tonton Marcel's own conclusions:** improve the Nemesis's handling if possible, and change
  technique — no turning fights; boost away, flip (FA off), and come back head-on at the
  Eagles. Detail in `Shipyard.md`, Nemesis card.

**Raw material for future `Logbook.md` days:** the old Clipper trapped among a pirate lord's
escorts, swarming out of nowhere; a new Gutamaya hull bought the same night and taken to three
engineers before dawn; the first sortie in her, every gun landing and every Eagle still slipping
behind her.

### 16–17 October — The Nemesis Finds Her Stride; Rival Power Hunting (journal-verified)

Source: journal files of 16 Oct (01:07–04:09 UTC) and 17 Oct (11:18–18:04 UTC, three sessions).

- **Nemesis refit, 16 Oct 01:09:** first steps of the handling plan — second shield cell bank,
  planetary hangar and DSS out, a 4D hull reinforcement and two small module reinforcements in;
  the large multi-cannon moved to the first large hardpoint. 842.8 → 810.8 t.
- **New technique works:** boost away, flip, come back head-on (`Shipyard.md`, Nemesis card).
  Osane massacre stacks re-taken twice (16 and 17 Oct, Prismatic Imperium, Cubeo Patron's
  Principles, HIP 1914 Imperial Society), plus two assassinations (Stuart Swarbrick, Alexis).
  Since 15 Oct: **13 massacre/assassination missions paid ≈119.8M CR** and **228 bounties
  ≈39.0M CR**. No ship lost. Combat 2 % → 32 % toward Master; Navy 57 % → **93 %** toward Earl.
- **Merits along the way:** +7 per ship scanned in Aisling space — the week's ship-scan
  assignment paid itself in Osane (+2,000, 16 Oct 01:36). **Aisling Rank 16** (17 Oct 12:13).
- **Bounties:** ≈17.6M CR redeemed on 16 Oct (HIP 1914 Imperial Society, at Digges Park and
  Kessel Platform) — the 15 Oct vouchers kept for McQuinn went with them. 17 Oct's ≈24.9M
  still unclaimed.
- **Rival Power hunting, 17 Oct afternoon:**
  - **HIP 3254** (14:52–16:06, then 16:30–16:39): weapons-fire signals, a trade beacon, convoy
    dispersal and Power wreckage — only minor-faction pirates and Imperial ships. No rival
    Power ships: the system lists only Aisling.
  - **Shui Wei Sector VT-R b4-5** (Lavigny-Duval, 16:09–16:24): a Power convoy distress
    signal — five Lavigny-Duval ships destroyed (Dolan, Durzo Blint, Turner, Cuvelier, Barrel
    Roll), +230 merits each, and five murder bounties (25,000 CR) with The 10th Legion. A second
    signal at 16:20 (Anacondas, Type-9s), left after a look. Interdicted there later by an
    Imperial Python (16:47).
- **Donations:** ≈40M CR across nine Imperial factions (Osane, HIP 3254, Wonomi, Huang Gun).
- **Evening:** three megaship-uplink missions for Prismatic Imperium (Huang Gun done, Segnir and
  HIP 7869 open); the Marco Polo transferred from Kenig City to Medupe City (18:03, 142k CR).

**Raw material for future `Logbook.md` days:** the duellist's lesson learned — stop turning, run,
flip and face them; a pirate family bled for three days at the Navy's request; then the first
deliberate killing of another Power's pilots, in Lavigny-Duval's own space, with murder written
against her name in that system.

### 17 October, evening — Earl, McQuinn, and the Rival Kills Paid (journal-verified)

Source: journal file of 17 Oct, 18:46–21:16 UTC. **+13,023 merits** (110,205 → 123,228),
**Aisling Rank 16 → 18**.

- **Megaship uplinks, Marco Polo:** six Prismatic Imperium hack missions (Huang Gun, HIP 7869,
  Boloine, Clido Pi, Koyans; Segnir abandoned) — ≈3.0M CR, and nine datalink scans at 468 merits
  that completed the week's megaship assignment (+2,400, 20:25). Rank 17 at 19:09.
- **Tod McQuinn unlocked, 19:33:** 100,000 CR of bounty vouchers donated at Trophy Camp
  (Wolf 397) — the multi-cannon engineer, and the road to Selene Jean and Didi Vatermann, open
  (`Engineers & Materials.md`).
- **Promotion to Earl, 20:43:** Cubeo Patron's Principles' promotion mission — 63 superconductors
  for the Imperial fleet, bought at Fefra's Legacy, delivered at Medupe City (3.86M CR). Plus
  ≈11.2M CR of donations to four Cubeo and Nexus factions.
- **Rival Power kills, Nemesis, 20:48–21:03:** back in Shui Wei Sector VT-R b4-5 — a Power
  weapons-fire signature, then two convoy signals: six more Lavigny-Duval ships destroyed.
  The **10th kill paid the assignment (+4,800, 21:02) — Rank 18**. Six more murders on her
  record there.
- **Bounties:** the remaining ≈24.9M CR redeemed at Medupe City (21:15). Logged off there.

**Raw material for future `Logbook.md` days:** an Earl's coronet won with a hold of
superconductors, the same evening a Wolf 397 engineer finally opens her door to bounty paper;
then back across the border to finish a killing contract in Lavigny-Duval's space.

### 19 October — Engineers by Day, The Brick by Afternoon; Trade Elite III (journal-verified)

Source: journal files of 19 Oct (06:39–10:44, 11:54–16:34, 17:48–18:43 UTC). +902 merits; no
weekly assignment progress.

- **Morning refit, Nemesis at Kenig City:** an unengineered 5A SCO FSD retrieved, a 6A fuel
  scoop in the shield cell bank's slot, a 3A collector limpet controller and a 5D hull
  reinforcement. Donations at Olahus Hub (Kou Hua) and Paola Prospect (Kuki An).
- **Engineering tour, 10:17–13:51:** the Marco Polo flew to Ballard Survey (Suhte, Pranav Antal
  space) and had the Nemesis transferred there as a forward base. In the Nemesis:
  - **Elvira Martuuk** (Long Sight Base, Khun): FSD **Faster Boot G5 + Double Braced** —
    Martuuk now **G5**.
  - **Tod McQuinn** (Trophy Camp, Wolf 397), two days after the unlock: large and three medium
    multi-cannons **Overcharged G5** — McQuinn **G5** in 10 minutes. **Selene Jean** and
    **Petra Olmanova** now *Invited*.
  - Back to Suhte, the Marco Polo home to Medupe City, the Nemesis transferred back.
- **The Brick, Cubeo supply missions, 14:12–18:26:** eleven industrial missions for Prismatic
  Imperium, Nexus Heavy Industries and Cubeo Purple Deeds — among them two of **50M CR** each
  from Prismatic Imperium (**1,152 t of gold**, **477 t of palladium**). Bought at McQuarrie
  Landing (Lambda-2 Tucanae) and Fefra's Legacy; **≈222.9M CR** of rewards. **Trade rank
  Elite III** at 18:11. Thirty donations along the way (26.2M CR); Navy 7 % → 30 % toward
  Marquis.
- **Last flight, Dart:** to Tucanae Sector BV-X b1-1 — landed at **Techno Defence Facility**
  (planet 5) and stepped out at 18:40; logged off three minutes later.

**Raw material for future `Logbook.md` days:** a day split in two — the gunsmith of Wolf 397
finally at her bench, the Corsair's cannons overcharged one after another; then the old Type-9
hauling a fortune in gold for the Princess's own house, a Princess's Earl turned merchant again.

### 19–21 October — Power Data at Techno Defence Facility; the Week Closed (journal-verified)

Source: journal files of 19 Oct (18:31–18:43 UTC) and 21 Oct (07:05–08:34, 11:11–12:01 UTC).
**+10,404 merits** (124,130 → 134,534), **Aisling Rank 19**.

- **Target:** Techno Defence Facility (Tucanae Sector BV-X b1-1 5, unoccupied, owned by HIP
  1914 Imperial Society), for the week's last assignment — Power association or political data.
  First landing on 19 Oct evening, then two sessions on 21 Oct, all in the Dart.
- **Two methods** (Tonton Marcel's account, `On-Foot.md` §1):
  - **Brute force** through the bar: download, alarm, shields up, run.
  - **Discreet:** through the command building to the alarm console, alarm off — turrets,
    drones and the ship left alone, but any NPC who saw a download still opened fire.
- **Rhythm:** one item per landing, then lift off and drop back in. 21 Oct morning: 3
  association items (07:41–08:02), handed in at Roelofs Station, Wababa (+1,620). Afternoon: 4
  more association items and 2 political (11:20–11:48), handed in at 11:54 — **+3,240 and the
  assignment +5,600; Rank 19**. Only the last two items came without a fine.
- **Cost:** 8 on-foot fines (3,750 CR, unpaid) with HIP 1914 Imperial Society; three energy
  cells and a medkit used.
- **Week of the 15 Oct tick closed: 4 of 5 assignments** (ship scans, rival kills, megaship
  scans, Power data); the HIP 3254 rival-kill assignment couldn't be done in Solo.
- Four donations at Medupe City (3.5M CR) before logging off; Navy 38 % toward Marquis.

**Raw material for future `Logbook.md` days:** an Earl in a borrowed technician's routine — in
through the bar, out under fire; later the quiet way, the alarm silenced by her own hand, yet
every pair of eyes in the room still turning on her. Nine trips to the same facility, nine
files lifted.

### 21 October, afternoon — The Pyrophyllite Loop (journal-verified)

Source: journal file of 21 Oct, 14:49–15:26 UTC. **+5,153 merits**, **Aisling Rank 20** (15:02).

- **The Brick** out of Medupe City for the route found that morning (`Powerplay Missions.md`
  §3): pyrophyllite bought at **Temple Works** (HIP 5623, Fortified), sold at **Spitzer
  Gateway** (Col 285 Sector WO-O b20-1, Exploited), 7.8 ly.
- Three full holds, 14:57–15:24: 1,642, 1,643 and 1,644 merits, ≈13.7M CR profit each. A round
  trip in ≈11.5 min — **~8,600 merits/h, ~71M CR/h**, the best Powerplay rate so far. The buy
  price didn't rise between trips. Logged off docked at Spitzer Gateway.

**Raw material for future `Logbook.md` days:** the old Type-9 back on a short shuttle, a mineral
nobody else wants carried eight light-years for the Princess — eleven minutes a trip.

### 24 October — Four CGs in One Week, the Fleet Spread Out (journal-verified)

Source: journal files of 24 Oct (08:34–08:42, 09:18–11:08, 14:57–15:39 UTC). No merits.
Detail per CG: `Community Goals.md`, CG 863–865.

- **Prep at Medupe City (08:40):** the Marco Polo's two 6A AFMUs and the Nemesis's 6A shield
  cell bank and a 3D module reinforcement taken back out of storage. A 400 CR fine for a
  collision at speed in the no-fire zone (08:36).
- **Fleet deployment, Marco Polo as taxi (09:20–09:54):** three Faulcon DeLacy CGs, three
  stations about two jumps apart — signed up at each and transferred a ship to each from Cubeo:
  **Nemesis → Bowen Dock, HR 8061** (military, CG 865), **The Brick → Homer Platform, AD Leonis**
  (trade, CG 864), **Astroforge → Davies High, Reorte** (mining, CG 863). Transfers 8.95M CR.
- **CG 865, Nemesis (10:08–11:07):** massacre missions from Noblemen of LHS 475 at Old Sharlayan
  (Thuleppa) against the AY Indi and Anekaliti pirates — 5.85M CR of mission value, **Top 50 %**;
  27 bounties (3.7M CR). Lesson: this CG counts mission value, not bounties. Nemesis left at
  Thuleppa, the Marco Polo brought over.
- **CG 864, The Brick (15:05–15:33):** uranium from Wang City (Duamta) and Schirra Dock
  (Coriccha) at 7,241 CR, sold at 57,104 CR — two runs, **1,516 t, Top 50 %**, ≈63M CR profit.
- **CG 863:** the Marco Polo flew on to Reorte; logged off aboard the Astroforge at Davies High
  (15:39), not yet mining.
- Navy 43 % → 45 %, combat 33 % → 36 %.

**Raw material for future `Logbook.md` days:** a Viscountess-turned-Earl dispatching her ships like
a fleet admiral — a gunship, a freighter and a miner sent to three stations of the same
corporation's campaign, and herself ferrying between them in the explorer.

### 25–27 October — Five Assignments, Four Faulcon DeLacy CGs (journal-verified)

Source: journal files of 25 Oct (07:05 → 23:16 UTC), 26 Oct and 27 Oct (to 18:25 UTC). Detail:
`Powerplay Missions.md` §1, `Community Goals.md` CG 862–865.

- **Weekly assignments, 5 of 5** (25 Oct evening, 26 Oct morning): holoscreens at Bowen Beacon
  (ICZ OX-U c2-15), Power wreckage rescued at Col 285 Sector WO-O b20-1, Power goods stolen at
  Heath's Quarry (Shui Wei Sector VT-R b4-4), **a new one — Power malware uploaded at Heath's
  Quarry** (collected at Bessel Dock, Munshin), holoscreens at Amaneque. **+24,000 merits,
  Aisling Rank 20 → 23.**
- **CG 863, mining:** 109 t of Osmium from LTT 5058, sold at Davies High at ×6 (264,306 CR/t,
  28.8M CR) — Top 75 %.
- **CG 864, trade:** The Brick's uranium runs to Homer Platform — **6,064 t** in all (plus
  liquid oxygen), ≈364M CR of sales — Top 50 %.
- **CG 865, combat:** **16.7M CR** of mission value — Top 25 %.
- **CG 862, exploration:** signed up at Magrathea II (HD 232819) on 26 Oct 12:36, ≈14.0M CR of
  data sold — **Top 25 %**. All four Initiatives contributed → golden decal.
- Treasury past **4 billion CR**; Navy 45 % → 48 %, combat 36 % → 41 %. Logged on 27 Oct at Homer
  Platform in The Brick.

**Raw material for future `Logbook.md` days:** a week of a corporation's campaigns run in
parallel — osmium cut from a pristine ring, uranium by the thousand tonnes, a pirate clan
thinned out for a shipbuilder's trials, and a long run to the Elysian Shore; meanwhile, for
Aisling, malware slipped into a Lavigny-Duval quarry under the guards' noses.

### 27–29 October — Four CGs Closed, 920 Million, Home to Medupe City (journal-verified)

Source: journal files of 27 Oct (17:58–18:25), 28 Oct (08:52–10:05, 12:40–15:25) and 29 Oct
(20:52–23:28 UTC). No merits. Detail: `Community Goals.md`, CG 862–865.

- **Last pushes:** seven more uranium runs for CG 864 (27–28 Oct, now from Bloomfield Station,
  OU Geminorum — ≈43M CR a hold) → **9,836 t**; a second Osmium trip in the Astroforge (119 t,
  28 Oct) → **228 t**.
- **Results (all closed 29 Oct):** exploration **Top 25 %** (310M CR), trade **Top 25 %** (250M),
  combat **Top 25 %** (220M), mining **Top 50 %** (140M) — **920,000,000 CR**, plus the golden
  Faulcon DeLacy decal for contributing to all four.
- **Collection tour, 29 Oct evening:** Astroforge at Davies High (20:53), then the Marco Polo to
  Homer Platform (21:01), Bowen Dock (21:08) and Magrathea II (22:48), home to **Medupe City**
  (23:23). The Astroforge, The Brick and the Nemesis transferred back from Reorte, AD Leonis and
  Thuleppa (9.4M CR). The whole fleet is home.
- Treasury **≈5.23 billion CR**; trade 37 % → 62 % toward Elite IV.

**Raw material for future `Logbook.md` days:** four stations, four envelopes from the same
shipbuilder in one evening's flight, and the fleet called home — the Earl back at Medupe City
richer by nearly a billion.

### 30 October – 1 November — The Week's Assignments, Two Still Open (journal-verified)

Source: journal files of 30 Oct (15:26–21:39), 31 Oct (10:28–11:40, 16:16–16:39) and 1 Nov
(18:32–19:25 UTC). **+14,487 merits** (164,825 → 179,312), **Aisling Rank 23 → 25**. Detail:
`Powerplay Missions.md` §1.

- **Done, 30 Oct (Marco Polo):** Aisling press dossiers to Martinez City (Col 285 Sector AV-M
  b21-0, +3,600, Rank 24); eight megaship scans ending at Jaroahy (+2,400 — Cubeo's megaship
  doesn't pay). The Nemesis and the Dart transferred to **Chamitoff Horizons, Jaroahy** as a
  forward base.
- **Done, 30 Oct evening (Nemesis):** rival Power ships in **Gadagombiri** — a Power weapons fire
  signature and two convoy distress signals; most rivals Wanted, so legal kills (+3,200, Rank
  25 at 20:42).
- **Open — classified data (Dart):** Baker's Plantation (Crucis Sector OY-R b4-4), one landing
  on 30–31 Oct — only common data.
- **Open — malware uploads (Dart):** injection malware (for acquisition) tried at Reorte (31 Oct)
  without effect; tracing malware (for undermining) collected at Herreshoff Prospect (Kherthaje) on 1 Nov and uploaded at **Kewell's
  Club, Reorte** — 2 uploads (195 merits each) among the guards. Four *failure to submit to police*
  crimes over the two days (31 Oct ×3, 1 Nov ×1).

**Raw material for future `Logbook.md` days:** an Earl running Aisling's errands across
her own contested border — press dossiers, megaships, a convoy fight among five Powers' pilots —
then a long, patient game of hide-and-seek in a resort full of guards, a tracer in her pocket.

### 2 November — Malware Done, Classified Data at Last (journal-verified)

Source: journal files of 2 Nov (07:31–19:37 UTC, four sessions). **+24,198 merits**
(179,312 → 203,510), **Aisling Rank 25 → 28**.

- **Tracing malware, Kewell's Club (Reorte):** the last uploads among the guards — assignment
  paid **+5,200** at 09:59, **Rank 26**.
- **Classified data, Crucis Sector OY-R b4-4:** a second look at Baker's Plantation, then the
  find of the week — **Ferenczi-houlden Extraction Exchange**, raided in ≈20-minute round trips
  (dock, download, leave, return). 68 downloads over three sessions, **8 of them classified**.
- **Hand-ins at Hale Gateway, Tripitaka (Stronghold):** 10:40 (common data, +2,340) and 13:18 —
  5 classified + 29 common data items, **+15,120 merits, Rank 27 and 28** within ten seconds.
  The classified assignment hasn't paid yet; 4 more classified units and the evening's data
  still in the backpack.
- Odds per download, from the journal: `Powerplay Missions.md` card 4.8.

**Raw material for future `Logbook.md` days:** the same extraction outpost robbed again and
again in one day, the guards never learning; the rarest file finally turning up, eight times —
patience as a weapon.

### 3–4 November — Classified Data Paid, Rank 33, Two Theft Contracts (journal-verified)

Source: journal files of 3 Nov (18:29–19:16) and 4 Nov (18:30–23:01 UTC, six sessions).
**+39,082 merits** (203,510 → 242,592), **Aisling Rank 28 → 33**.

- **Last raids at Ferenczi-houlden:** 20 downloads on 3 Nov (2 classified), 12 on 4 Nov
  (2 classified). One *failure to submit to police* on 3 Nov.
- **Hand-in at Hale Gateway, Tripitaka, 4 Nov 19:00–19:01:** 73 Power data units in one go
  (18 industrial, 9 research, **8 classified**, 19 association, 19 political). The classified
  assignment paid **+5,600**; **Rank 29, 30, 32 and 33 within 20 seconds**.
- **Fleet home:** the Dart and the Nemesis transferred back from Chamitoff Horizons, Jaroahy, to
  Medupe City (≈4M CR).
- **Two covert heist contracts:** a personal computer from **Vannier Drilling Rigs** (HIP 5623,
  for Medupe City, 66,585 CR) and a **suit schematic** from **Hakimi Manufacturing** (Guuguyni,
  for Shen Terminal, 177,843 CR) — the schematic was the mission item, handed in, not kept.
- **Donations:** six donation missions at Medupe City (5.75M CR).
- **Three game crashes** (18:32, 21:50, 22:36 UTC) — see 7 Nov for cause and fix.

**Raw material for future `Logbook.md` days:** a whole week of stolen files emptied onto one
counter, the ranks clicking past faster than she can read them; then a schematic lifted from a
factory floor for someone else's suit.

### 5–6 November — CG 866 at Sorbago, a New Week at Techno Defence (journal-verified)

Source: journal files of 5 Nov (17:16–18:56) and 6 Nov (17:06–18:09, 20:32–22:59 UTC).
**+457 merits** (242,592 → 243,049). Detail: `Community Goals.md`, CG 866.

- **CG 866 — "Défendez Sorbago Mastopolos Mining Inc"** (combat, Hencke Orbital, Sorbago; ends
  **19 Nov, 11:00 UTC**): the Nemesis in the conflict zone, 1.35M + 1.40M CR in combat bonds on
  5 Nov (Top 50 %), then **6.77M by 6 Nov 18:08 — Top 25 %**. Imperial side only — Tonton
  Marcel's choice: no other CG this cycle.
- **Donations, 6 Nov evening:** ≈20.8M CR of donation missions for Imperial factions in
  Dounthiassi, Sorbago and HIP 1914.
- **New assignments (tick of 5 Nov):** injection malware uploads **and** Power data downloads at
  **Techno Defence Facility** (Tucanae Sector BV-X b1-1, military, the "military 3" layout with
  5 data ports) — more guards, restricted zones, turrets, drones and ships on alarm. First run
  with the Dart: data downloaded, 4 malware taken, one upload done as the alarm went off — then
  **a crash to desktop (≈23:00 UTC)**. The upload was never recorded; all 12 malware were still in
  the locker at the next login.
- Two crashes that evening (20:47 and ≈23:00 UTC).

**Raw material for future `Logbook.md` days:** a Viscountess turned soldier for an Imperial
mining company; then a fortress full of guards, the alarm, the upload — and the world going black.

### 7 November — The Crashes Fixed; Malware Done, Data Sold in the Wrong System (journal-verified)

Source: journal files of 7 Nov (09:14–09:19, 10:15–11:53, 16:06–16:39, 16:49–17:40 UTC).
**+19,470 merits** (243,049 → 262,519), **Aisling Rank 33 → 35**.

- **Crash fix (technical):** six of the seven unclean exits since 24 Oct matched a Windows
  "low virtual memory" event (EliteDangerous64 at 7–12 GB). The page file sat on the 10 GB E:
  partition, 1–4 GB. Moved to **C:, 16–32 GB** on 7 Nov morning — commit limit 16.7 → 31.7 GB. No
  memory warning and no crash in any session since (7–12 Nov).
- **Malware, Techno Defence (morning):** three runs, **undetected**, 11 injection uploads (250
  each); the assignment paid **+5,200** with the 11th — **Rank 34** (Prismatic Shields threshold).
- **The mistake:** all the Techno data sold at **Medupe City** (+11,520 merits, Rank 35) — but the
  second assignment wanted **industrial or research data from that system, sold only in Wababa**.
  Restarted from zero: **9 needed**.
- **Afternoon:** three more runs, now also looting coded lockers — **5 of 9** data, goods and
  components to the backpack limits (40 / 60). Two fines (property theft, failure to submit),
  1,000 CR, paid.

**Raw material for future `Logbook.md` days:** the same fortress, three times, and nobody sees
her; then the haul handed to the wrong buyer, and the whole job to do again.

### 8 November — Wababa Delivered, Holoscreens, Rank 38 (journal-verified)

Source: journal files of 8 Nov (10:25–10:51, 16:56–18:26 UTC). **+23,282 merits**
(262,519 → 285,801), **Aisling Rank 35 → 38**.

- **Techno Defence, two more runs:** alarms off, 9 of 9 reached.
- **Wababa (Stronghold), Roelofs Station, 17:32:** 27 data units, **+17,300** including the
  **+5,600** assignment bonus — Rank 36, 37 and 38.
- **Holoscreens (Dart):** two hacks at Wilson Stop, **Chinga** (Lavigny-Duval, Fortified) — the
  Dart, which had left the station to hack its screen, then **destroyed by the station itself**
  (small rebuy — the reason the Dart flies these jobs). Then six hacks in **HIP 95350** (Torval
  Stronghold) — assignment **+4,800**. Fines 10,000 CR.
- Back to Medupe City; a new exobiology assignment taken: sell **390,000 CR** of organic data in
  a reinforcement system.

**Raw material for future `Logbook.md` days:** a rival station's own guns answering a hacked
screen; a cheap ship lost on purpose, a plan that had already counted the loss.

### 9 November — First Exobiology, 50 Million in Species; Marquis (journal-verified)

Source: journal files of 9 Nov (04:15–06:00, 07:52–08:42, 08:59–11:19, 11:50–12:48 UTC).
**+5,674 merits** (285,801 → 291,475), **Aisling Rank 39**. **Imperial Navy: Marquis.**

- **Looking for the unknown (Marco Polo):** 48 jumps, up to ≈1,380 ly from Cubeo — all 256 bodies
  scanned already discovered.
- **HIP 12013 B 5 and B 6** (a Spansh pick): two **Stratum Tectonicas**, sold at Medupe City —
  **19,010,800 CR each (38.0M)**, no first-logged bonus. Assignment **+5,600**, **Rank 39**.
- **LTT 5058 1 c** (222 ly, already discovered and mapped by XCaliber_Elite): **Frutexa Acus**
  (7,774,700), **Tussock Ventusa** (3,227,700), **Bacterium Aurasus** (1,000,000) — **12.0M CR** at
  Kenig City, no bonus. The planet card names another CMDR who sampled first; **the journal's
  `WasFootfalled` flag said "false" anyway — not reliable**, the planet card is.
- **Imperial Navy rank mission:** 45 Indium to Medupe City, **4.63M CR** → **Marquis** (Earl →
  Marquis; one step from Duke).
- **CG 866:** 2.09M CR of combat bonds → **8.86M**, back to **Top 50 %** (contributors 1,826 →
  3,917).

**Raw material for future `Logbook.md` days:** the first time she kneels to touch something
alive on a dead world — and every world already has someone else's footprint. A new title the
same morning.

### 9 November, afternoon — Hunting Push in Anarchy Space (journal-verified)

Source: journal files of 9 Nov (13:24–13:45, 14:51–16:06, 16:19–16:46, 18:22–19:44,
22:15–23:20 UTC). No merits.

- **CG 866 first:** 1,167,166 CR of bonds at Hencke Orbital (13:44) → **10.03M**, Top 50 %.
- **Goal:** 5 Push for Domino Green's referral to Kit Fowler.
- **Papacosta Horticultural Exchange** (Rata Bares, anarchy) visited, no loot logged; then
  theft runs at **Kolsuk Agricultural Centre** and **Fry Agricultural Hub** (Senones, anarchy,
  Diamond Frogs). Kolsuk is small with guards in every corner; Fry has many lockers — **12 Hush, 5 Lazarus, 1 suit schematic, 2 manufacturing
  instructions**, but no Push.
- First visit to **The Jackrabbit** (Orishis) — Domino Green still *Invited* (5 Push needed).
- **Akers Station** (Senones, anarchy) bartender: surplus sold, **4.04M CR** — including the 12
  tracer malware and the Hush and Lazarus. Fines paid: 7,500 CR.

**Raw material for future `Logbook.md` days:** a noblewoman picking locks in pirate country for a
drug she doesn't take, to buy an introduction.

### 11–12 November — Push at Last, Domino Green Unlocked (journal-verified)

Source: journal files of 11 Nov (06:38–08:04) and 12 Nov (10:21–10:41 UTC). **+285 merits**
(291,475 → 291,760).

- **HR 5295** (anarchy, all settlements run by a local militia, several settlement types — a
  system to raid regularly to learn its loot): **Barbier Tourism Complex** first, for its HAB
  lockers — **5 Push**, plus 5 Hush and 4 Lazarus.
- **The Jackrabbit, Orishis:** 5 Push to Domino Green → **Domino Green Unlocked**, **Kit Fowler
  Known** (journal, 12 Nov).
- Surplus sold (1.62M CR). Next time, use the bartender in HR 5295.
- **Still missing for the extra backpack modification:** weapon inventory and digital designs —
  never found in any visit so far (script, §6).
- **CG 866:** 891,566 CR more on 12 Nov → **10.92M**, still **Top 50 %** (5,266 contributors,
  Tier 2). Ends 19 Nov 11:00 UTC.
- Ship scans don't check the ship locker (scanned at The Jackrabbit with drugs in the locker:
  clean). On-foot scans do check the backpack.

**Raw material for future `Logbook.md` days:** the right building, the right lockers, and the
drug finally in her hand — traded the same day for a name.

### 13–14 November — The Prismatic Fitted, Medium Conflict Zones, Holoscreens at Dalgarno Colony (journal-verified)

Source: journal files of 13 Nov (20:33–21:41 and 21:43–22:47 UTC) and 14 Nov (14:11–14:46 UTC),
plus Tonton Marcel's report of 14 Nov. **+5,863 merits** (291,703 → 297,566), **Aisling Rank 40**
(14 Nov 14:16). The 12 Nov total of 291,760 was 57 too high: the 13 Nov `Powerplay` login line
says 291,703 (one donation counted twice, the same journal glitch as cards 4.12/4.13).

- **The Prismatic, 13 Nov:** bought at **Hencke Orbital** (Sorbago), 23.66M CR, fitted in the
  Marco Polo for the trip (in place of an AFMU). Reinforced G1–G4 applied on the spot (remote
  workshop, Lei Cheung's blueprint); materials traded at **Cassidy Orbital, Wulganda**
  (manufactured trader, mostly for Improvised Components); **G5 + Hi-Cap at Trader's Rest**
  (Laksak, 20:58–20:59). Strength 150 → 219.4 MJ (base), kinetic 49.9 %, thermal −0.2 %,
  explosive 58.3 %. Back at Hencke Orbital (21:09), the Prismatic moved into the **Nemesis**.
- **Medium-intensity conflict zones, Sorbago A 1** (first time in medium CZs with the Nemesis):
  three sorties on 13 Nov (21:12–21:20, 21:24–21:38, 22:10–22:30) and one on 14 Nov
  (14:19–14:43), **37 kill bonds**, 4.52M CR redeemed. **The shields never fell in combat.**
  Tonton Marcel: the Nemesis can hold a medium CZ and win it for her side, as long as kills come
  fast enough.
  - Tactic: small targets first, to cut the enemy count; big ships after. Two drawbacks: fewer
    enemies brings reinforcements into the zone, and big ships nearby sometimes open fire on her
    while she chases the small, fast ones.
  - **The Vultures** (59 scanned, 34 of them Elite; many in "Escadrille de forces spéciales"
    wings): fast, quick shield regeneration, shield cell banks, lots of chaff — and a weapon
    whose hits get through her shields to the hull or modules. Meanwhile her side's NPCs die, so
    she breaks off, kills one or two easy targets to rebalance the zone, then goes back to the
    Vulture.
  - Bonds per sortie: 146k (8 min), 823k (14 min), 1.89M (20 min), 1.66M (24 min) — **≈4M CR of
    bonds an hour** once settled in. Best single bond: 176,851 CR.
- **Rival hunting, 13 Nov 21:48–22:08, Shui Wei Sector MI-S b4-3** (Aisling, Lavigny-Duval, Grom
  and Torval present): a weapons-fire signal and a convoy dispersal gave two **Wanted pirates**
  (The Sovereign Justice Collective, bounties 272,391 + 39,933 CR, +69 and +10 merits); two Power
  wreckage signatures, empty. **No Power convoy distress or weapons-fire signal** — the week's
  "kill rival ships" assignment is stuck there (Tonton Marcel).
- **Holoscreens at Dalgarno Colony** (Sorbago — Torval Exploited, Aisling present): a recon
  limpet controller and a 16 t rack fitted to the Nemesis in place of two module
  reinforcements (13 Nov 22:35), 16 limpets. **10 hacks × 67 merits** in 5 drops of 2
  (13 Nov 22:40–22:46 and 14 Nov 14:14–14:17); the assignment paid **+4,800 on the 9th hack**
  (14 Nov 14:16) — Rank 40 on the same line. Ten 1,000 CR fines to Magnates of Cemiess, paid
  14 Nov.
- **Donations at Hencke Orbital:** 2M CR on 12 Nov (Magnates of Cemiess), 5.5M CR on 14 Nov to
  both sides of the Sorbago civil war (Sorbago Imperial Society, MLC Incorporated) and to
  Magnates of Cemiess — 57 merits per 1M, 43 per 750k.
- **CG 866:** 4.52M CR of bonds → **15.44M**, **Top 25 %** (5,878 contributors, Tier 2, 58.8 bn).
  Ends **Thursday 19 Nov 11:00 UTC**. Detail: `Community Goals.md`.
- **The week's assignments all sit around Sorbago** — it is a Torval Exploited system with all
  four imperial Powers present (reinforcement 23,743 vs undermining 20,395, 14 Nov), so Aisling
  points her pilots at it. Handy: one hop between a PP job and the CZ. Done: holoscreens. Open:
  rival kills (no Power signals), and three settlement jobs (data port downloads — classified,
  research or political Power data — and malware uploads). `Powerplay Missions.md` §1.

**Raw material for future `Logbook.md` days:** a shield only Aisling's loyal may buy, fitted the
same evening; the first battle where her side wins because she is in it; the Vultures — Elite
pilots in special-forces wings, a weapon that reaches through her shield — and the choice,
again and again, between the duel and the people on her side who are dying while she has it.

### 15 November — On Foot in Sorbago, Rank 41 at Marki (journal-verified)

Source: journal files of 15 Nov (17:41–18:35, 19:29–20:25, 20:55–21:11 UTC) and screenshots of
the Powerplay screen (21:07–21:08). **+9,631 merits** (297,566 → 307,197), **Aisling Rank 41**
(21:03).

- **Ships:** the Nemesis all day, landing at the settlements; the Dart sent from Cubeo to
  Sorbago (`ShipyardTransfer`, 117 ly, 17:44).
- **Donations:** 2M CR to Sorbago Imperial Society, 9.25M CR to Magnates of Cemiess (at Dias's
  Territory), 2M CR to Daily Routine Incorporated (Marki) — 754 merits for 13.25M CR.
- **Raids on foot, Maverick "NON armee", Sorbago A 2:** a first stop at Nnamani Mineralogic
  Station (Sorbago Mastopolos Mining Inc — the CG faction; nothing taken), then **Dias's
  Territory** (extraction, Magnates of Cemiess) twice: 18:03–18:34 and 19:55–20:24. 18 Power
  data downloads (1 classified, 6 association, 5 political, 4 industrial, 2 research), Power
  goods from the containers (inventory, extraction, equipment, agriculture, experiment…), 79
  goods and 75 components in all (`loot_stats.py`). Two *failure to submit to police* and one
  data-transfer fine (1,500 CR, paid at Plumb's Chase).
- Between the raids: **Plumb's Chase** (Sorbago A 1, tourism) — on foot 19:35–19:45 with a relog,
  nothing taken; **Seidel Cultivation Holding** refused docking four times.
- **Hand-in at Crossfield Market, Marki** (Aisling Stronghold, two jumps via Kuan Ti): 26 Power
  data units (18 fresh + 8 from the locker) → **8,877 merits**, Rank 41; the bounties of 13 Nov
  (312,324 CR) redeemed. The Power goods stayed in the backpack.
- **The week's assignments, from the screenshots** (`Powerplay Missions.md` §1): classified data
  1/10 — Sorbago counts; association + political **0/8** — Sorbago data doesn't count, it's a
  rival **Exploited** system and the assignment wants an unoccupied or contested one; malware
  0/10 in Shui Wei Sector MI-S b4-1; rival kills 0/8 in MI-S b4-3; holoscreens done. About 3
  days 10 hours left (tick ≈ Thu 19 Nov 07:00 UTC).

**Raw material for future `Logbook.md` days:** the woman who fights for Sorbago's mining company
by day goes back at night, unarmed, to rob a settlement of the faction she paid nine million to
the same afternoon — and the haul is weighed in a Stronghold two jumps away, where only part of
it is the right kind of secret.

### 15–16 November — Malware and Data Done at Xiao Chemical, Classified Hunt, Rank 46 (journal-verified)

Source: journal files of 15 Nov (21:19–22:10 UTC) and 16 Nov (08:48–09:28, 09:51–10:18,
11:38–17:27 UTC), plus Tonton Marcel's report of 16 Nov. **+39,462 merits** (307,197 →
346,659), **Aisling Rank 46** (five ranks on 16 Nov).

- **Malware, 15 Nov evening:** 10 injection malware collected at Crossfield Market, **Marki**;
  three jumps to **Shui Wei Sector MI-S b4-1** (unoccupied; Aisling, Patreus, Grom and Torval
  present). Target: **Xiao Chemical Enterprise** (A 8, industrial, Sorbago Imperial Society),
  docked on its own pad. A first look on foot that evening (Power goods only, one fine).
- **16 Nov, four landings at Xiao Chemical** (08:52–12:52): **10 injection uploads × 250**, the
  assignment paid **+5,200 on the 10th** (12:48) — Rank 42. 13 Power data downloads on the way
  (association, political, industrial, research). Fines with Sorbago Imperial Society
  (trespass, failure to submit, data transfer, two property thefts — 2,750 CR, paid each time),
  while 11.5M CR went to the same faction in donations (15–16 Nov).
- **Hand-in at Marki, 12:58:** 18 data units → 8,280 merits — the association + political
  data from MI-S b4-1 (unoccupied) **completed the association/political assignment, +5,600**.
  Ranks 43 and 44.
- **Classified hunt in the Dart** (swapped at Hencke Orbital, 13:20):
  - **LPM 26** (Yuri Grom Exploited, dictatorship): **Schwarz Landing** (military, 1 a,
    13:59–14:44) 3 downloads, 1 classified; **Varma's Consulting** (5 d) nothing but a trespass
    fine; **Uduike Excavation Complex** (extraction, 2 a, 15:03–15:33) 4 downloads, **2
    classified**, plus Power goods. 3 classified in 7 downloads.
  - **Dias's Territory, Sorbago**, three raids (15:41–16:02, 16:06–16:22, 16:38–16:55): 21
    downloads (7 per raid, one per data port), **1 classified**. 9.75M CR donated to Magnates
    of Cemiess around the raids.
- **Hand-in at Marki, 17:01:** 43 data units → **16,927 merits**, Ranks 45–46. The 3 LPM 26
  classified **counted for the assignment** although Tonton Marcel expected Marki to be too far
  from LPM 26 — the undermining version has no range limit. Classified **5/10**.
- **Malarhones** (Torval Exploited), **Prabhune Keep** (military, A 8 b): 6M CR donated to Daily
  Routine Incorporated, then on foot 17:13–17:27 — one download. Tonton Marcel: a pure military
  settlement is a pain, guards everywhere asking for scans.
- **Evening (18:34–19:38):** relog at Prabhune Keep and away; a short stop at Schwarz Landing
  (LPM 26, no download); then **two more Dias's Territory raids** (18:54–19:15, 19:18–19:37): 14
  downloads, **1 classified** (in the backpack, not handed in yet → 6/10 once delivered).
  5.75M CR more to Magnates of Cemiess. Tonton Marcel: "not just bad luck" — and the numbers
  now agree (`Powerplay Missions.md` card 4.8).
- **Night (20:35–21:40), the Dart:** **ICZ FB-X c1-25** (Torval Exploited, one jump from
  Sorbago; Daily Routine Incorporated): **Shepherd Command Point** (military, 20:44–21:05) — 3
  downloads, no classified; **Schofield Munitions Stockade** (military) — 3 minutes on foot, a
  failure-to-submit fine, nothing taken; two *fire in no-fire zone* fines (100 CR) on lift-off.
  Then one more **Dias's Territory** raid (21:20–21:34): 6 downloads, no classified — but the
  first **Weapon Inventory** and **Digital Designs** ever found came out of its ports (21:25,
  21:26): the two data items blocking the Maverick's first mod (`On-Foot.md` §2.1, now 1/5
  each). Tonton Marcel: "completely unfruitful" — for classified data, yes.
- **Late night (22:28–23:36), the Dart:** **LHS 480** (Grom Exploited, six Powers present),
  **Yan Metallurgic Station** (extraction, A 4, 22:46–23:07): 8 downloads, no classified; then
  **Uduike Excavation Complex** again (LPM 26, 23:14–23:35): 3 downloads, no classified.
  Tonton Marcel: "without success" — and the question whether some data ports never give
  classified data (`Powerplay Missions.md` card 4.8).
- **Hand-in at Marki, 21:39:** 32 data units → **11,877 merits**, the evening's classified
  among them → **6/10**. Ranks 47–48. 9.75M CR of donations that night (Daily Routine
  Incorporated, Magnates of Cemiess, NLTT 4671 Dynasty).
- **The hunt paid anyway** (Tonton Marcel: "more merits than the PP mission reward"): Power data
  hand-ins brought **≈46,000 merits** over 15–16 Nov (8,877 + 8,280 + 16,927 + 11,877) against
  the 5,600 the classified assignment pays. Since the 12 Nov tick: **≈+67,800 merits**, Rank 39
  → 48.
- **CG 866:** no bonds since 14 Nov; still **Top 25 %** at 15.44M (6,567 contributors,
  73.2 bn, 16 Nov 21:39). ≈2M more bonds still planned before 19 Nov 11:00 UTC.

**Raw material for future `Logbook.md` days (15–16 Nov):** the day she becomes, in one sitting, five grades
more trusted by Aisling's people; the same faction thanked with eleven million and robbed in its
own corridors the same morning; and the rarest secret, never where she expects it — three from
a dictator's rock she thought too far to count, one from the place she had chosen for its seven
doors.

---

### 17–18 November — Angi: Same Layout, Classified Only in CMD and EXT; Assignment Done, Rank 51 (journal-verified)

Source: journal files of 17 Nov (19:20–20:04 UTC) and 18 Nov (07:59–09:20 UTC), plus Tonton
Marcel's report of 18 Nov. **+26,727 merits** (359,471 → 386,198), **Aisling Rank 51**.

- **17 Nov, Dias's Territory once more** (19:27–19:36, the Dart): 4 downloads, no classified.
  4M CR donated to Magnates of Cemiess first.
- **Looking for the Ferenczi-houlden layout elsewhere** (Tonton Marcel's method): Inara search
  for **extraction settlements with a large pad**, then the in-game size marker **(+)** — that
  narrows the layout to two types. Pick: **Auclair Metallurgic Base**, Angi A 3 a (The Order of
  Mobius; **Angi is Torval Exploited**, so its data counts for undermining). First approach
  17 Nov evening, a relog on foot overnight.
- **18 Nov, four runs at Auclair** (08:04–09:11), with notes taken building by building:
  - **Full run** (08:04–08:33): CMD → HAB → EXT → HAB → STO → STO → PWR, 7 downloads — **one
    classified, in CMD** (the first download).
  - **Three short runs** (08:35–08:43, 08:46–08:57, 09:00–09:11): **CMD → HAB → EXT → HAB**
    only, then lift off and land again. 14 downloads, **3 classified — from CMD and EXT only**
    (Tonton Marcel). The last two runs show 5 downloads: in EXT a technician patrols the port's
    room and she can stay hidden only ≈40 s, so she **split the EXT download in two** (#3 and
    #4, 64–96 s apart in the journal).
  - **Per building at Auclair:** CMD **2 / 4**, EXT **2 / 6**, HAB 0 / 8, STO + PWR 0 / 3.
  - In all: **21 downloads, 4 classified (19 %)**; the three short runs alone gave 3 in 14 in
    36 minutes.
- **Hand-in at Crossfield Market, Marki, 09:16:** 51 Power data units, **4 classified →
  assignment complete, +5,600** — ≈20,900 merits for the data. Ranks 49, 50 and 51 in a minute.
- **The week:** four assignments of five done (holoscreens, malware, association/political,
  classified); only the rival kills in Shui Wei Sector MI-S b4-3 are left (0/8). Tick ≈ Thu
  19 Nov 07:00 UTC.
- **CG 866:** still no bonds since 14 Nov — 15.44M, **Top 25 %** on 18 Nov 09:15, but 6,849
  contributors and 80.2 bn; the line is closing in. **Ends 19 Nov 11:00 UTC.**

**Raw material for future `Logbook.md` days:** after days of rolling dice she stops trusting
luck and starts reading buildings — the same settlement drawn twice in two systems, the same
two rooms that keep secrets — and the classified files finally come, four in a morning.

---

### 18 November, afternoon — CG 866 Secured; Five Concourse Missions Paid in Materials (journal-verified)

Source: journal file of 18 Nov (10:16–16:15 UTC) and Tonton Marcel's report. **+891 merits**
(386,198 → 387,089, donations only).

- **CG 866, two medium-CZ sorties** in the Nemesis (Sorbago A 1, 10:48–11:08 and 11:12–11:31):
  **2.75M CR of bonds** (1,250,907 + 1,495,050) → **18.19M**, **Top 25 %** (6,880 contributors,
  81.1 bn). Tonton Marcel: should be safe by now. Ends 19 Nov 11:00 UTC.
- **New strategy for the Maverick: missions that pay in materials.** Base: **Krenkel Terminal,
  Calea** (Aisling Stronghold), in the Dart. Five on-foot missions in ≈3 h (13:04–16:14), the
  materials option taken each time (it costs most of the credit reward):
  - **Wreck salvage** (Daily Routine Incorporated; wreck on Calea AB 1 c) → **3 Suit
    Schematics**.
  - **Package delivery to a contact**, Justine Mckee at Collinson Arms Base (Calea AB 3 b,
    military; one failure-to-submit fine) → **2 Suit Schematics**.
  - **Covert assassination**, Alex Reilly at Oladoyinbo Nurseries (Jeterait A 2 a, agricultural,
    Jeterait Cartel; Torval Stronghold), 14:06–14:44 → **15 Digital Designs**.
  - **Heist from a secret cache** (Calea Imperial Society; ICZ KC-U b3-4 6 a), 15:03–15:09 →
    **12 Tactical Plans** — never found in any settlement before.
  - **Covert production sabotage** at Biggs Chemical Assembly (ICZ FB-X c1-25 3, industrial,
    NLTT 4671 Dynasty; Torval Exploited), 15:38–16:09 → **12 Suit Schematics**.
- **Result:** Suit Schematic 5 → **22**, Digital Designs 1 → **19**, Tactical Plans 0 → **13** —
  three of the Maverick's biggest gaps closed in an afternoon (`On-Foot.md` §2.1).
- Tonton Marcel: efficient, but more stressful — **one attempt per mission**: caught means the
  mission is lost; and the target settlements are often ones where the alarm is hard to switch
  off. "No stress, no fun."
- Donations: 10.75M CR to Daily Routine Incorporated, 2M CR to NLTT 4671 Dynasty.

**Raw material for future `Logbook.md` days:** contracts, not luck — a dead man in a nursery, a
cache nobody was meant to find, a chemical plant left silent; each job one chance only, each
paid not in credits but in the plans and designs she needs to rebuild the suit she hides in.

---

### 18 November, evening — Weapon Inventory from a Labyrinth; Off to Domino Green (journal-verified)

Source: journal file of 18 Nov (18:25–19:42 UTC) and Tonton Marcel's report.

- **Sabotage mission for Weapon Inventory** — the Maverick's last blocker for its first mod.
  Taken at Krenkel Terminal (Calea) from Samebito Purple Advanced Company: *disrupt production at
  **Zambo Horticultural Biosphere*** (Marki 2, agricultural, Daily Routine Incorporated — in
  Aisling's own Stronghold), 18:27.
- **A new layout for her:** agricultural, size **(++)**, Odyssey Site Maps' **Agriculture 3** —
  "a big labyrinth" (Tonton Marcel). **Three landings** (18:33–18:42, 18:45–19:05,
  19:08–19:25): caught several times (one identity-theft fine), but this **non-covert**
  sabotage didn't fail when she was seen, so she came back and retried until she found a
  patient path to the alarm switch, then to the biological area to plant the pathogen.
- **Paid at Krenkel Terminal, 19:30:** **15 Weapon Inventory** (79,065 CR with the materials
  option) → **16/5**. 2M CR donated to Daily Routine Incorporated before going in — the
  faction whose crops she then poisoned.
- **Then straight to Orishis** for Domino Green (The Jackrabbit): swapped to the Marco Polo at
  Hencke Orbital (19:35), four jumps via Arth, Ross 486 and Lindol; logged off on arrival
  (19:42). Next: **Extra Backpack Capacity**, the Maverick's first mod.
- CG 866: 18.19M, Top 25 % (6,889 contributors, 81.6 bn, 19:41).

**Raw material for future `Logbook.md` days:** a garden that is a maze; caught, out, back in,
three times, until patience finds the way to the alarm and to the beds where the blight goes —
in a Stronghold of her own Power, against a faction she had paid two million an hour before.

---

### 19 November — The First Suit Mod, CG 866 Paid, the Fleet Home (journal-verified)

Source: journal file of 19 Nov (20:29–20:56 UTC) and Tonton Marcel's report.

- **Extra Backpack Capacity** applied by **Domino Green** at The Jackrabbit, Orishis
  (20:32–20:35, on foot) — the Heist Maverick's **first mod** (`SuitLoadout` → `SuitMods:
  suit_backpackcapacity`). Stage A of the suit plan done (`On-Foot.md` §2.1).
- **CG 866 closed, Top 25 %** (Tonton Marcel). Final contribution **18,185,623 CR** of bonds.
  The treasury went from 5,203.9M (18 Nov 18:25 login) to **5,471.9M** (19 Nov 20:29 login) with
  no session in between: +268M, most likely the reward — no `CommunityGoalReward` event was
  written.
- **Home:** back through Sorbago (4M CR more to Magnates of Cemiess and MLC Incorporated at
  Hencke Orbital), then to **Medupe City, Cubeo** in the Marco Polo; the **Dart** and the
  **Nemesis** transferred from Hencke Orbital (117 ly, 24.5 min, 2.74M CR). All ships home.
- **The 12 Nov Powerplay week closed** (tick 19 Nov ≈07:00): 4 of 5 assignments — holoscreens,
  malware, association/political data, classified data; the rival kills in MI-S b4-3 never
  had a Power signal. Rank 51, 387,458 merits.
- **Next for the suit:** **5 Opinion Polls** sold to bartenders, to invite **Kit Fowler** —
  never found yet.

**Raw material for future `Logbook.md` days:** home at last, every hull back in its berth at
Medupe City; a quiet tailor at the Jackrabbit makes her suit carry more — the first thing she
has changed about herself in a long time, chosen and paid for.

---

### 20 November — Powerplay Calls: Donations, Contracts, Locusts, Rescue and Rival Ships (journal-verified)

Source: journal file of 20 Nov (13:06–17:06 UTC) and Tonton Marcel's report. The on-foot
material and mission run was paused: PP duty took over — **ship work only**, none of the ten
assignments needed boots on the ground.

- **Maverick raised G2 → G3 → G4** at Medupe City (13:08, 6.75M CR) — Stage B of the suit plan,
  mods still to come (`On-Foot.md` §2.1).
- **Nemesis refit** at Medupe City then Roentgen Orbital, HR 5632 (17:04): collection limpets in
  place of the recon controller, 12 t of cargo, module reinforcements — **868.8 t, 17.8 ly**
  (§2).
- **Sealed contracts** (card 4.10): 10 collected at Medupe City (13:17), delivered at **Kessel
  Platform, HIP 3254** (13:32, after a "no space" denial) — **+2,000**.
- **Rare goods** (card 4.1): 9 **Karsuki Locusts** at West Market, Karsuki Ti (732 CR) → sold at
  **Tsiolkovsky Ring, Fire Fade** (1,210) — **+2,000** at 13:51, **Rank 52**.
- **Donations — 24 missions, 23.5M CR:** Karsuki Ti (Prismatic Imperium, Karsuki Ti Patrons of
  Law, 4M), HIP 3254 (Prismatic Imperium, HIP 6161 Empire League — an outbreak, 5.75M), Fire Fade
  Exchange (2M), HIP 1914 (Imperial Society, Purple Universal, 4M), **Nexus Heavy Industries** at
  Medupe City (7.75M). 56–168 merits each on top. Interdicted by an Imperial military ship in
  HIP 1914 (14:05, submitted).
- **Rescue** (card 4.4): a Power emission drop at HIP 3254 in the Nemesis (pods, wreckage, a
  black box → Kessel Platform, 360k CR, +982 merits); then, in the Marco Polo (collection
  controller fitted at Hale Gateway), one at HR 5632, handed in at Tripitaka. The **Nemesis
  transferred Cubeo → Tripitaka** (180 ly, 4.12M CR, 35 min) and took over at 16:06.
- **HR 5632, Nemesis, 16:11–17:03:** four emission drops and a convoy distress signal — shields
  down once (16:15) and a reboot-repair (16:25), 41k CR of repairs; four rival Power ships killed
  (Torval, Grom ×2, Mahon). Rescue items handed in at **Roentgen Orbital**: assignment
  **+2,800** (17:03). One Lavigny-Duval holoscreen hacked there in passing.
- **Megaships** (card 4.9): **three uplink scans at HR 5632** in the Marco Polo (15:50–16:00,
  468 each) — 3 of the 11.
- **Merits:** 387,401 → 398,744 (`Powerplay` at the next login); 5,464.9M → 5,431.7M CR.

**Raw material for future `Logbook.md` days:** a day of giving — twenty-four purses handed over
in five systems, an outbreak among them; locusts bought at Karsuki and sold under Aisling's flag;
escape pods pulled out of a Power's wreckage field while rival hunters circle; the warship
brought up the line to finish what the trader started.

---

### 21 November — Rival Ships at HR 5632, Rank 53 (journal-verified)

Source: journal file of 21 Nov (11:29–12:03 UTC).

- **Nemesis back at HR 5632:** a Power emission drop, then a **convoy distress signal** — four
  more rival ships, all wanted: Lavigny-Duval Viper and Anaconda (11:37, 11:41 — **Rank 53**),
  Torval Anaconda ×2 (11:53–11:54). Rival-kills assignment **+3,200** at 11:54 (card 4.13): 8
  kills over the two days.
- Heat sinks synthesised once mid-fight (Basic); 3 Unidentified Scan Archives picked up.
- **Tripitaka, Hale Gateway (12:02):** back into the Marco Polo, the **Nemesis stored there**;
  2,800 CR of bounty vouchers cashed.
- **Week status:** 4 of 10 assignments done — sealed contracts, rare goods, rescue, rival kills.
- **Merits:** 398,744 → 402,934 (next login, 22 Nov).

**Raw material for future `Logbook.md` days:** a convoy under attack and four rival flags struck
in a quarter of an hour; the warship left in the dock at Tripitaka, as if she meant to come back
for it.

---

### 22 November — Three Assignments in Forty Minutes, a Whisky for LP 684-17 (journal-verified)

Source: journal files of 22 Nov (16:08–16:16 and 17:49–18:55 UTC) and Tonton Marcel's report.
At Hale Gateway first (16:08): the week's assignments read from the Powerplay screen
(screenshots), recon limpet controller back on the Marco Polo, jump to Ao. First route
planned with `tools/pp_week.py` (`Powerplay Missions.md` §1). Marco Polo, recon limpets fitted.

- **Ao, Avicenna Hub (Archer Fortified) — undermining holoscreens:** 8 screens per drop,
  12 hacks × 48 in two drops (17:52–18:05); assignment **+4,800** at 18:04, **Rank 54**. Fines
  12,400 CR to Bollwerk Mercenary Corporate, paid on docking.
- **LHS 378 (Aisling Exploited):** 8 ships targeted (nav beacon, McCoy Platform) — scans
  assignment **+2,000** at 18:15, in 4 min. Holoscreens: **one** hijacked screen in the whole
  system (Ericsson Beacon, Mahon) — 11 hacks × 65 by **relogging** at the station between hacks,
  18:19–18:33; **+2,400**, no fines.
- **Wolf 587, Reamy City:** the **Nemesis** called from Tripitaka (80 ly, 1.88M CR, 18 min) — the
  nearest shipyard to LP 684-17 (LHS 378 has none).
- **Rare goods:** Aganippe Rush out of stock at Julian Market; **12 Eranin Pearl Whisky** bought
  at Azeban City, Eranin (2,310 CR each), back at Reamy City at 18:54.
- **Open:** swap to the Nemesis at Reamy City — the 12 rares move with the swap (cargo
  transfer up to the smaller hold, 12 t) — then rares and bounties in LP 684-17 in one trip
  (357,941 CR); 8 megaships on the way home (Tripitaka ×2, Sitakapa ×3, Ruwachis ×3 → Medupe
  City).
- **Merits:** 402,934 → **413,481** (+10,547 in 41 min).

**Raw material for future `Logbook.md` days:** a station's adverts rewritten screen by screen
under Archer's flag; a lone billboard in LHS 378 that keeps falling back to Mahon — and she keeps
taking it back; a bottle of Eranin's whisky bought to be sold, not drunk.

---

### 22 November, evening — The Week Closed 10 of 10; a Quiet Kill for Kit Fowler (journal-verified)

Source: journal file of 22 Nov (20:42–23:05 UTC) and Tonton Marcel's report.

- **Reamy City, Wolf 587:** into the Nemesis, the 12 Eranin Pearl Whisky carried across in the
  swap. **LP 684-17:** rares sold at Planck Horizons (2,541 each) — **+3,600**, **Rank 55**
  (20:47); then three weapons-fire signals near the star, a wanted ship in each (Diamondback,
  Eagle, Krait Mk II — 598,069 CR of vouchers): bounty assignment **+4,800** at 20:56, five
  minutes of fighting.
- **Home run in the Marco Polo:** megaships at **Tripitaka ×2, Sitakapa ×3, Ruwachis ×3**
  (21:06–21:37), **Rank 56** at 21:10, assignment **+2,400** at 21:37 — **the week closed, 10 of
  10.** Docked at Medupe City 21:42; the **Nemesis transferred home** from Wolf 587 (239 ly,
  5.46M CR, 45 min). Tonton Marcel: Aisling now asks **ten assignments a week**.
- **Donations — 18 missions, 17.75M CR** at Medupe City (Cubeo Purple Deeds, Cubeo Patron's
  Principles, Nexus Heavy Industries) and Lambda-2 Tucanae (Empire League). **Imperial Navy:
  92 % toward Duke** (66 % on 19 Nov).
- **The assassination (on foot):** from Medupe City's concourse board, Prismatic Imperium —
  *Éliminer Bruno Cameron*, Navarro Botanical Base, **Lambda-2 Tucanae** (Aisling Stronghold,
  one jump). In the Dart, unarmed Maverick: one discharge in passing, somewhere out of sight —
  **no crime logged**. 21:56–22:23 on site; paid at Medupe City 22:27: **8 Opinion Polls** +
  144,114 CR (`On-Foot.md` §4).
- **Kit Fowler:** 5 Opinion Polls sold at Medupe City's bar (22:33) → *Invited*; to Capoya in
  the Marco Polo (recon controller swapped for a cargo rack first), **The Last Call** 22:49 →
  **Unlocked**; 5 Surveillance Equipment handed over → **Yarden Bond Known**. Fowler's own mods
  (melee, ammo) are of no use to her. Back at Medupe City 23:01.
- **Next — Yarden Bond's gate:** 5 **Smear Campaign Plans** (1 in stock). Medupe City's
  bartender won't buy them: a black-market item, most likely. Plan: data ports at **tourism
  settlements in an anarchy system** — three days before the 26 Nov tick.
- **Merits:** 413,481 → **428,222** (+14,741). Treasury 5,409.0M CR (22:44).

**Raw material for future `Logbook.md` days (Tonton Marcel's own words, to keep):** *"ce n'est
pas à quelques jours d'être adoubée Duchesse qu'il faut faillir à l'Empire"*; eight opinion polls
for a life — absurd, paper for a man, but the reward opens a door and removing the target serves
the Empire's interests. **Lambda-2 Tucanae, an allied station:** a man she knows
nothing about, *"et ce n'est pas plus mal"*. No weapon — a single discharge in passing, a
discreet corner out of sight: *"pas de bruit, pas de détonation, pas de spectacle, une veuve
noire qui ne faisait que passer…"* Kit Fowler: weapons-obsessed, suspicious of everything, of no
interest to her — only a name to trade for Yarden's. Smear campaigns, refused at her own bar:
she'll dig them out of the silicon of an anarchy where tourists — *"zèbres"* — pass in
numbers. Three days' grace before duty calls again.

---

### 23 November — The Diamond Frogs' Smear Campaign: Yarden Bond Unlocked (journal-verified)

Source: journal files of 23 Nov (18:22–23:21 UTC) and Tonton Marcel's report. Marco Polo,
unarmed Maverick G4.

- **LTT 7786** (anarchy, 80+ settlements, a dozen tourism ones): no landing — two of its
  factions are **at war** (Posse of Niflheimri, LTT 7786 Major Group), their settlements are
  ground conflict zones. On to **Ascella**: **Aloisio Lodges** unpowered and empty (18:36–18:40);
  **Kaur's Link** (18:43–19:15) — the Smear Campaign port guarded by three NPCs in one room;
  another port gave Tax Records and 2 Power propaganda data.
- **Tutunnyk's Resort, LPM 746** (anarchy tourism, Diamond Frogs): three landings (19:23–21:54),
  **4 Smear Campaign Plans** and a haul of HAB data (Kompromat, Campaign Plans, Digital Designs,
  12 Power data units). With the one in stock: 5.
- **Akers Station, Senones** (anarchy Orbis): the 5 sold at the bar, 130,000 CR (22:11) — Medupe
  City's bartender had refused them. **Yarden Bond Invited**; **Salamander Bank, Bayan**, 22:27 →
  **Unlocked**, **Improved Jump Assist applied** (Heist Maverick slot 2).
- **First rooftop test, Kwon Metallurgic Enterprise, Bayan** (extraction, Alliance): Weapon
  Inventory, Power research data, a Power extraction sample (500 CR theft fine, The Academy),
  Insight data banks, components. Then **Richelieu's Barracks, HIP 48391** (military, 23:06–23:21):
  nothing logged.
- **Next:** Quieter Footsteps needs **2 Patrol Routes** (3 of 5) — military-type CMD/SEC data
  ports; candidate systems from `tools/settlement_finder.py`.

**Raw material for future `Logbook.md` days:** *"la calomnie des grenouilles diamantées"* — a
resort full of tourists and secrets, its data ports emptied three times over; a war that closes
a whole system to her; an abandoned settlement, dark and silent; a bartender at her own port who
won't touch what an anarchy bar buys without a question.

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
| `Community Goals.md` | CG results, CG playbook (sources, bracket forecast, rewards), one card per CG (11 Oct 2026) |

### 5.0 Guiding principles

**Gauges to raise**

| Gauge | Status | Target | Unlocks |
|---|---|---|---|
| Imperial Navy | **Marquis** (9 Nov) | Duke (1 promotion) | Imperial Cutter |
| Aisling rank | **Rank 51 / 386,198 merits** (18 Nov) — rank 34 reached 7 Nov | ~~Rank 34 (≈247,000 merits)~~ ✔ | Prismatic Shields |
| Engineering | FSD G5 accessible | Combat and defence engineers at G5, Guardian tech | All target builds, §5.7 |
| Combat piloting | Expert (14 Oct) | Comfortable in HazRES and conflict zones | Actually usable TTK |
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
- [ ] **Every week:** check the active CGs and pick the ship via the target-fleet table (§5.5) —
      playbook in `Community Goals.md` §2.
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
| Hyperion | Asp Explorer | Exploration | Bridge ship, stored at the museum **once the Marco Polo's exploration kit is fitted** (decided 7 Oct) |

> Bridge "The Brick" → Cornucopia: The Brick covers trade CGs until the Cornucopia arrives.
> Bridge "Pacifier" → Diplomat: the Pacifier covers bounty hunting and transforms into the Diplomat.
> Bridge "Hyperion" → Marco Polo: the Hyperion covers exploration until the Marco Polo arrives; the Guardian expedition is flown by the Marco Polo (decided 7 Oct 2026).

#### Phase 1 — Trade and mining first, learn combat

**Goal:** accelerate Aisling merits using current strengths (trade and mining), and start combat
risk-free.

**Ships** → `Shipyard.md`
- [~] Astroforge v2 (annex A1) — engineering 1 Oct (power plant, thrusters, FSD, boosters);
      mining lasers 2D → 2B to do; PP mining formula found 1 Oct, hotspot merits/h still to
      measure.
- [x] Dart v2 Tier 1 (annex A2) — done 5 Oct, 38.8 ly; DSS G5 and Tiers 2–3 remain
      (`Shipyard.md`).
- [x] Pacifier v2 (annex A3) — done 6 Oct, weapons reworked 7 Oct (1 beam + 3 gimballed
      multi-cannons), validated in CG 860. No weapon engineering on her (decision 7 Oct): that
      goes to the Corsairs — `Shipyard.md`.
- [x] **CG 861 — "Brewer Corporation Jump Satellite Initiative"** (Zero Squared, HIP 74116,
      8–11 Oct) — **26,530 t, Top 25 %**, reward 200M CR collected 11 Oct; the four SCO FSDs
      (sizes 4–7) still to locate. Card: `Community Goals.md`.
- [x] CG 860 — Top 25 %, reward 220,000,000 CR collected 8 Oct (`Community Goals.md`).
- [~] **Corsair series started with the Marco Polo** (decided 7 Oct, bought 8 Oct): Tier 1
      engineering done, 63.4 ly; power for the second AFMU and the rest of the exploration kit
      still open — `Shipyard.md`, Marco Polo card. Nemesis and Soteria follow, depending on
      missions, Powerplay and CGs.
- [x] The Brick V2 — "90 %" plan (annex A5) — done 30 Sept, plus a 6A SCO FSD.
- [x] Hyperion — FSD G5 done 23 Sept; thrusters stay at G3 (no more engineering: she retires
      once the Marco Polo is equipped, decided 7 Oct).

**Powerplay** → `Powerplay Missions.md` — ≈150,000 merits remaining to rank 34 (15 Oct:
96,987 of ≈247,000 — about 20 h of The Brick's trade loop at ~7,600 merits/h)
- [ ] Weekly assignments, every Thursday tick.
- [~] Three merit loops run and measured: **PP trade (The Brick) ✔ 30 Sept** (~7,600
      merits/h, Checkpoint 1 below), PP mining (Astroforge), Low RES (Pacifier).
      Also measured 1 Oct with the Dart: **megaship scans ~3,100–4,300 merits/h** and
      **Power data on foot ~2,100–3,300 merits/h** (rough; `Powerplay Missions.md` §3).

**Imperial Navy: Viscount → Duke** — remaining: Marquis → Duke (Count ✔ 14 Oct, Earl ✔ 17 Oct). Duke rank unlocks
the **Imperial Cutter**. Method: rank up to **Allied** with an Imperial faction in a dense system
(Aisling's +100% rep-gain perk applies in ducal territory) → "Imperial Navy" missions start
appearing on the board → stack them. Ranks are never lost, one rank per session, in parallel with
merit grinding.
- *Progress:* 86 % → **95 %** toward Count (2–3 Oct: Gallium contract + eight altruism
      donations, §4). Still 95 % at the 12 Oct 23:35 login; twelve more donations on 13 Oct
      (≈10.6M CR, Cubeo Patron's Principles and Nexus Heavy Industries, §4) — read the
      `Progress` line at next login.
- [x] **Count — 14 Oct 2026, 03:03 UTC.** The bar read 100 % at the 13 Oct 22:21 login; the
      promotion mission came from **Prismatic Imperium** (Medupe City): a courier run for the
      Imperial fleet intelligence service to Sellers Vista (Shui Wei Sector DG-O b6-4), 5 min.
      Lesson: once the bar is full, check the Allied Imperial factions' boards for a
      `Mission_*_RankEmp` mission.
- [x] **Earl — 17 Oct 2026, 20:43 UTC**, three days after Count. Bar at 47 % (14 Oct) → 93 %
      (17 Oct 17:47) on massacre stacks and donations, then 100 %; the promotion mission was a
      **delivery**: 63 superconductors for the Imperial fleet (`Mission_Collect_RankEmp`, Cubeo
      Patron's Principles), bought at Fefra's Legacy, 11 min.
- *Next: Marquis.* Same method — check the boards for a `RankEmp` mission once the bar is full.
- [ ] Push reputation with one Imperial faction in a dense system to **Allied**.
- [ ] Missions for minor Imperial factions in Aisling space (stacks PP and Navy progress); trade
      and delivery missions count too.
- [ ] Accept promotion missions as soon as they appear; stack them toward **Count → Earl →
      Marquis → Duke**.

**On-foot** → `On-Foot.md`
- [ ] Zero-risk steps done: abandoned-settlement reactivation, data recovery.
- [ ] Heist Maverick at G5 with 4 mods (added 3 Nov 2026): roadmap in `On-Foot.md` §2.1, engineer
      unlocks (Domino Green first) in `Engineers & Materials.md` §3.

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
- [~] Pacifier: 10 Low RES sessions with no losses, combat rank at least Competent — rank
      Competent since 29 Sept; 2 sessions so far, no loss (6 and 7 Oct, CG 860, low/medium CZs).
  **Benchmark — combat, Pacifier V2** (CG 860, Redonesses, 6–7 Oct; baseline for the Nemesis
  and the Charybdis). Source: `python tools/combat_stats.py --since 2026-10-06`. Same shield,
  boosters and engineering in both rows; only the weapons changed.

  | Metric | 2 beams + 2 turreted MCs (6 Oct) | 1 beam + 3 gimballed MCs (7 Oct) |
  |---|---|---|
  | Zones fought / time in zone | 5 CZ + 2 megaship, 1.8 h | 26 (mostly low CZ), 6.1 h |
  | **Kills per hour in zone** | 18.4 | **22.1** |
  | Median gap between kills | 2:16 | 2:07 |
  | Time on target / damage rate, low CZs only | 2:01 / 68 pts/min | 1:58 / 71 pts/min |
  | **Engagements dropped without a kill, per hour** | 9.4 | **4.3** |
  | Shields lost per hour | 2.2 | **1.3** |
  | Heat warnings | 3 | 0 |
  | Zones left with shields up | 3 of 7 | **20 of 26** |
  | Lowest hull | 58 % | 35 % (once) |
  | Kills per logged hour (commute and hand-ins included) | ~10 | ~12 (18 in the short evening session) |

  Reading: in the same kind of zone, the new fit doesn't kill a target faster (damage rate
  68 → 71 points of shield % + hull % per minute). What changed is staying power: half as
  many engagements dropped, fewer shield collapses, no more empty weapon capacitor. 167 of the
  168 kills are confirmed by the lock (a kill clears the lock in the same second).

  **Target difficulty** (both fits, median; "rate" = shield % + hull % removed per minute,
  "shield back" = the target's shield recovered during the fight):

  | Target | Kills | Time on target | Rate | Shield back | Dropped |
  |---|---|---|---|---|---|
  | Eagle | 24 | 1:15 | 123 | 2 | 2 |
  | Viper Mk III | 21 | 1:42 | 91 | 2 | 4 |
  | Vulture | 21 | 1:49 | 84 | 1 | 3 |
  | Viper Mk IV | 14 | 2:08 | 79 | 2 | **8** |
  | Asp Explorer | 15 | 2:06 | 70 | 2 | 4 |
  | Cobra Mk III | 17 | 2:51 | 58 | 1 | 5 |
  | Python | 24 | 2:49 | 41 | **7** | 6 |
  | Anaconda | 8 | 2:56 | 30 | **6** | 3 |
  | Alliance Challenger / Crusader / Chieftain | 5 | 3:32–6:22 | 17–30 | 2 | 5 |

  Viper Mk IV: the most dropped target — fast, and quick to flee at ~15 % hull (Tonton
  Marcel); some were also dropped on purpose when a bigger ship attacked from behind.
  Pilot rank changes little (Competent 78, Elite 63 points/min). The power plant was the
  subsystem most often targeted (24 kills), then thrusters (19). Full detail:
  `python tools/combat_stats.py --since 2026-10-06 --kills`.
- [x] Hyperion's FSD at G5, Pacifier's boosters and shield at G3+ (Pacifier: G3 boosters,
      G5 shield, 6 Oct).

#### Phase 2 — Guardian expedition with the Marco Polo

*Changed 7 Oct 2026:* the expedition was planned on the Hyperion with no purchase; the Marco
Polo (first Corsair, bought in Phase 1) flies it instead, in her exploration configuration, and
the Hyperion retires early.

**Goal:** unlock Guardian technology for the whole fleet, and start exobiology (currently
Directionless), which funds what follows.

**Preparation**
- [ ] Marco Polo exploration configuration (Stage 3 of her build plan) → `Shipyard.md`.
- [ ] Hyperion stripped and stored at the museum; her DSS (Expanded G5) transferred to the
      Marco Polo.
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
- [~] Combat engineers: The Dweller to G5 ✔ (15 Oct), McQuinn G5 ✔ (19 Oct); Zacariah Nemo,
      Professor Palin still to do.
- [ ] Materials farmed toward shields, Frags and thrusters.

**Nemesis** → `Shipyard.md`
- [x] Corsair #1 bought and named Nemesis — 15 Oct 2026, Kenig City; first engineering pass the
      same night (Deciat / Wyrd / Laksak, §2).
- [ ] Handling fixed for small, fast targets (thrusters G5, weight) — `Shipyard.md`, Nemesis card.

**Missions**
- [ ] On-foot Phase 3 steps (Frontline CZs, cut-the-reactor, Dominator suit) → `On-Foot.md`.
- [ ] First solo Operations — needs both tracks ready: ship (Nemesis or Pacifier) and on-foot
      (Frontline CZs at minimum).

**📍 Checkpoint 3 — combat is validated**
- [ ] Nemesis at G5; reference TTK measured in HazRES.
- [x] Combat rank Expert or above (indicative) — **Expert, 14 Oct 2026**.
- [ ] At least one combat or bounty-hunting CG played.

#### Phase 4 — Prismatic and Spectre (in parallel)

- [~] Aisling rank 34: buy and store the Prismatics — 8A for Charybdis; 6A for Cornucopia; 6A for
      Hephaestus; optional for Nemesis. **Nemesis done first: 6A bought 13 Nov 2026** (Hencke
      Orbital, Sorbago, 23.66M CR) and fitted (§2, §4).
- [~] Engineer: Reinforced + Hi-Cap (Lei Cheung) — Nemesis's 6A done 13 Nov.
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

- [x] ~~Corsair #2 "Marco Polo"~~ — moved forward: first Corsair, Phase 1 (decided 7 Oct);
      the Hyperion's retirement moves with her (Phase 2).
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
| Marco Polo | Corsair | M | Long-range taxi; exploration, exobiology, cartography, Guardian expedition | Range | Phase 1 (first Corsair; replaces Hyperion) |
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
| `tools/travel_stats.py` | Jump metrics per ship from the journal: jumps, ly, average / best jump, jump cadence, ly per hour of route time, scooping, neutron boosts (`--since`, `--routes`) |
| `tools/pp_week.py` | One route for the week's Powerplay assignments, read from `Powerplay Missions.md` §1: named systems with their tasks and stations, a rival system for undermining work, megaships still to scan, rare-goods source before the sale (`--rare-source`, `--to`, `--jump`). Built 22 Nov 2026 |
| `tools/waypoint_route.py` | Route through N systems meeting criteria (megaships to scan, station type, power state), optional via/destination; megaships from a pasted Inara search (`tools/inara_megaships.txt`) and the journals. Built 22 Nov 2026 |
| `tools/settlement_finder.py` | Systems richest in Odyssey settlements of given economies (default Military, Extraction, Industrial, High Tech) around a system, factions at war left out; pad signatures per economy to match against the Odyssey Map Guide layouts (`--radius`, `--min`, `--pads`, `--max-gravity`, `--details`). Built 24 Nov 2026 |
| `tools/material_finder.py` | Where to farm one or more on-foot items (goods or data): Inara item list (`tools/data/odyssey_items.tsv`: type, blueprints using it, buildings where it drops) × the 28 Odyssey Site Maps layouts (`tools/data/odyssey_layouts.json`: buildings, data ports per building, pads) × nearby Spansh settlements (layout guessed from economy + pads), factions at war left out. `--info` = item card and best layouts, offline; `--locker` = ShipLocker split into sell (no blueprint) / keep; `--survey SYSTEMS` = a system's settlements with pads and possible layouts; `aim` column = in-game size marker (−/+/++) to look for (`On-Foot.md` §5.0); `--pad`, `--radius`, `--max-gravity`. Layout table rebuilt by `tools/build_layouts.py` from a clone of the maps repo. Pads from a Spansh census, `?` = to confirm in play. Built 24 Nov 2026 |
| `tools/combat_stats.py` | Combat metrics from the journal: zones, kills/h, gap and time on target, ship types and pilot ranks killed, shields lost, outcomes, per weapon fit (`--kills`, `--csv`) |
| `../elite-loot/loot_stats.py` | Settlement loot from the journal: every on-foot visit's goods, components and data against the settlement's and system's economy, government, faction state, security… Shows where an item drops (`--item suitschematic`, `--by settlement_economy`, `--since`, `--csv`). Built 10 Nov 2026, outside this repo |
| ED Colonisation Planner | Build order for a system |
| EDMC / EDDiscovery | Automatic journal upload, Inara sync |

**Inara note:** only the active ship reports in if the Frontier account link has expired. Relink
the account in settings, or pull each hull out of the hangar once with EDMC running.

---

*Last updated: 24 November 2026 (journal read through 23 Nov 23:21 UTC; session logs 20–23 Nov
added). To be completed session by session.*

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
