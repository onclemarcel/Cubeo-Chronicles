# ON-FOOT — CMDR ONCLEMARCEL
## Odyssey playbook: protocol, gear, progression, mission type cards

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Satellite of `In-Game Operations.md` §5 (Roadmap): the main line there holds phases and
> checkpoints; this file holds the on-foot work. Created 25 September 2026 when §5 was split into
> satellite files (content moved, not rewritten). Same growth rule as `Powerplay Missions.md`:
> cards are refined in place; what *happened* in a session still goes to `In-Game Operations.md` §4.
> **References:** a bare `§N` points to `In-Game Operations.md`, except "§5.2 step N", which now
> means §1 of this file (the protocol moved here). "Engineers" = `Engineers & Materials.md`.

---

## 1. PROTOCOL

*Moved from the old §5.2.*

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

---

## 2. GEAR

- **On-foot gear** (suit/weapon engineering follows a track separate from ship engineering):
  - **Artemis** for exobiology (Phase 2, §5.4);
  - **Maverick** for sabotage and PP data;
  - **Dominator** for on-foot combat (Phase 3, §5.4).

---

## 3. PROGRESSION BY PHASE

**Phase 1 — zero-risk** (moved from §5.4)
- [ ] **Abandoned-settlement reactivation** mission — zero NPCs, zero alarms. Gathers
      micro-resources and is the on-foot equivalent of the Low RES/PP loops (`Powerplay Missions.md` §3): safe, and a
      real data point for what it actually yields.
- [ ] **Data recovery** mission at a powered-down site — same risk profile, more data-type
      materials.

**Phase 2** (moved from §5.4)
- [ ] On-foot gear: Artemis suit + Genetic Sampler (exobiology).

**Phase 3 — first real risk** (moved from §5.4)
- [ ] On-foot: **Frontline conflict zones** first (§5.2 step 5) — allies nearby, free respawns,
      failure costs nothing. Safe combat practice, mirroring the ship-side ramp (Pacifier Low RES
      → Nemesis HazRES) with the same "prove it safely before it counts" logic.
- [ ] On-foot: **cut-the-reactor infiltration** at an active settlement (§5.2 step 3) — the first
      real on-foot risk, timed to match the combat confidence built on the ship side (§5.4). Still untried as of
      23 Sept (§4).
- [ ] Dominator suit (combat) or upgraded Maverick (sabotage, PP data) for Dart's missions.

---

## 4. MISSION TYPE CARDS

*Seeded from the 21 September 2026 sessions (`In-Game Operations.md` §4 keeps the day's log and
story material).*

### 4.1 Wreck salvage (`Mission_OnFoot_Salvage_MB`)

- **Recognise it:** recover a ship or vehicle schematic from a ground wreck.
- **Run:**
  - [ ] Treat the site as contested (hostile wreck salvage, §1): approach from cover.
  - [ ] Engage at range; don't cross open ground toward the objective marker.
- **Pitfalls:** the wreck can spawn armed guards on arrival — it is not a "zero NPC" site.
- **Stats:** 3 runs · 2 deaths, 1 success · last: 21 Sept — morning, 2× Cubeo Patron's
  Principles (~84k CR each), both failed on deaths; evening, Nexus Heavy Industries, clean (paid
  Chemical Patents ×4).

### 4.2 Package securing / data bank collect

- **Recognise it:** "Sécurisation d'un colis" (target carrier at a settlement) or a data bank
  collect.
- **Run:**
  - [ ] Check the settlement's controlling faction before landing (see 4.3 pitfalls).
- **Pitfalls:** none met so far.
- **Stats:** 3 runs, all completed · ~56–58k CR each · last: 21 Sept, Prismatic Imperium — Kohli
  Cultivation Base, Kapoor Agricultural Biome, Daramy Botanical Habitat (completed 17:40–17:41).

### 4.3 Heist, no violence (`Mission_OnFoot_Heist_MB`)

- **Recognise it:** steal an item from an installation without violence.
- **Run:**
  - [ ] Cut the reactor first (§1 step 3) — still untried.
  - [ ] Match the Profile Analyser clone's clearance to the building.
- **Pitfalls** (moved verbatim from the 21 Sept log, §4):

**Mechanics worth keeping:** the `Faction` on an on-foot mission does not tell you whose
settlement you are about to enter — check `ApproachSettlement`/the settlement's controlling
faction before landing. On a heist a scan alone is not stealth: being challenged and not
submitting is logged as a crime and turns the site hostile (§5.2 step 3, *cut the reactor first*,
is still the untried fix).

- **Stats:** 1 run, failed · last: 21 Sept, Kohli Cultivation Base (Prismatic job against a
  Cubeo Patron's Principles site) — challenged, didn't submit, killed by a security drone.

### 4.4 Settlement reactivation / data recovery

- Not yet played — §1 steps 1–2, Phase 1 in §3 above.
