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
4. A community tool shows the exact alarm panel and data port locations for each settlement
   layout: **Odyssey Site Maps** (§5, link there). Worth using for planning instead of
   learning each site by dying in it.
5. **No stun/incapacitation tool exists in the game** — confirmed, not a gear gap to engineer
   around.

**Play-tested 21 Oct 2026 — Techno Defence Facility (Tucanae Sector BV-X b1-1 5), Power data
for a PP assignment (`Powerplay Missions.md` card 4.11).** Two ways tried, both worked:
- **Brute force:** walk into the bar (no clearance needed), download at its data port — the
  alarm goes off — combat shields up, run back to the Dart under fire.
- **Discreet:** into the command building (one `onFoot_trespass` fine), up to the **alarm
  console**, alarm off. Result: no base-wide response — **turrets and drones stay quiet, the
  ship isn't attacked**. But each NPC who **sees** the download still reacts on their own and
  opens fire (`onFoot_dataTransfer` fine), even from far away across the room.
- **Why (as far as we can tell):** the alarm console only stops the *settlement's* alarm. The
  download itself remains a crime, and any NPC with a line of sight is a witness. Disabling the
  alarm limits the response; it doesn't make you invisible.
- **So, for a clean download:** pick a port no one can see — check every NPC's position and
  patrol first, wait until they turn away or leave the room, crouch. It can be done: the last
  two items (11:48) came with **no fine at all**.
- **Simplest in practice (21 Oct):** one item per landing, then lift off and drop back in. The
  settlement resets each time (9 items in 9 drops on 21 Oct). **Superseded on 2 Nov**, see below.

**Method since 2 Nov 2026 — settle in before downloading (Ferenczi-houlden Extraction Exchange,
`Powerplay Missions.md` §3 and card 4.8).** On landing, first switch the settlement's **alarms
off** and its **authorisation scans off**. One level-3 profile clone gets you to the two
switches. After that, every building can be entered with no further credentials. Then walk all
the data ports at leisure: 8 ports and about 10 units per landing instead of one, and ~15,000
merits/h instead of ~2,800. NPCs who see a download can still fine you (one or two 500 CR
fines per session), so the witness rule above still applies. The full route is in §5.1.

**Download time depends on the data type** (Tonton Marcel, 3 Nov): anything from 10 to 30 s.
**Classified Power data always takes 30 s**, and research data seems to take 20 s. The NPC's
patrol has to leave you that much time. A long download is also a longer exposure: two long
ones in a row are where an NPC walking back past the port catches the hack.

**Never run past a guard who is scanning you**, even when clean. Running off a scan is a crime
in itself (`onFoot_failureToSubmitToPolice`, 500 CR): logged on 2 Nov 11:18 and 3 Nov 18:56.
Stop and let the scan finish. **If you are carrying a cloned profile, drop the credentials
before the scan** to avoid the fine, then re-clone another NPC afterwards (learned at Kewell's
Club, §5.2).

**Scans — what they check, and how to live with them** (Tonton Marcel, 11 Nov; journal-checked)
- **On-foot scans check the backpack**, and they happen almost every time a guard is nearby, so
  hide-and-seek with guards is the rule. **Ship scans check the cargo hold only, not the ship
  locker**: scanned arriving at The Jackrabbit (11 Nov) with Hush, Lazarus and Push in the
  locker — all clear.
- **Never get scanned with stolen goods or Power malware in the backpack.** Take only the malware
  the run needs from the locker (4 at a time at Techno Defence): a failed scan then costs less.
  Journal: the scanned run of 6 Nov ended in an identity theft fine and an attack; the three
  clean runs of 7 Nov carried malware and stolen data with no fine at all.
- **Scan-cooldown trick for narrow spots** where you can't hide: walk past the guard openly
  with no credentials (clean scan), go back to the level-3 NPC and clone them, then pass the
  guard again openly — guards usually don't scan twice in a short time. "Short" is short:
  30 s is already long. Only works with nothing stolen in the backpack.
- **Coded lockers fill the backpack fast** (7–8 Nov, Maverick G2): goods stop at **40** and
  components at **60** per landing. Pick what you loot (§2.1 shopping list) instead of emptying
  everything.

**Settlement type and risk** (journal, Sept–Nov 2026, on-foot crimes per visit; small samples,
and the looting style changed on 7 Nov)

| Settlement type | Visits | Crimes per visit | Who's inside |
|---|---|---|---|
| **Extraction** | 17 | **0.29** | Few guards, many workers and technicians who don't scan — the easiest raids |
| Agricultural | 16 | 0.44 | Scientists and technicians; one or two guards (§5.3) |
| Tourism | 10 | 0.60 | Guards, pilots, mercenaries in the HABs — someone is always nearby (§5.2, §5.5) |
| Military | 17 | 0.71 | Many guards, restricted zones, small rooms, turrets/drones/ships on alarm (§5.4) |

High-tech (4 visits, 4.5 per visit) is skewed by one massacre mission (15 murders, 29 Sept).

**Where this fits in the plan:** the zero-risk steps (1–2, still pending — the 21 Sept session
played wreck-salvage and settlement-collect missions instead, see §4) sit in **Phase 1** alongside
the other risk-free grinding, since they need no rank/gear and plausibly feed the same
engineer-discovery pattern as the ship side (§5.4). The first real on-foot risk (step 3,
cut-the-reactor) sits in **Phase 3**, timed to match the rising ship-combat confidence built there
— deliberately not before confidence is re-established either way (§5.4).

---

## 2. GEAR

- **On-foot gear** (suit/weapon engineering follows a track separate from ship engineering):
  - **Artemis** for exobiology (Phase 2, §5.4) — in use: G1, loadout "EXOBIO SANS ARME",
    Genetic Sampler, first species sampled 9 Nov 2026 (`Powerplay Missions.md` card 4.15);
  - **Maverick** for sabotage and PP data;
  - **Dominator** for on-foot combat (Phase 3, §5.4).

### 2.1 Heist Maverick — roadmap to G5 (planned 3 Nov 2026)

*For PP downloads, uploads and thefts (`Powerplay Missions.md` cards 4.8, 4.11, 4.14) and heist
missions (card 4.3). Unarmed for now: no armed PP assignment has come up for Aisling yet.
Engineer unlock steps are ticked in `Engineers & Materials.md` §3, not here.*

**Starting point (journal, 3 Nov 18:59):** one Maverick, **Grade 2, no mods** (loadout "maverick
NON armee", no weapons). 5.2 bn CR, so credits are no constraint; micro-resources are.

**Rules that shape the plan**
- One mod slot per grade above 1: G2 = 1 slot, G3 = 2, G4 = 3, **G5 = 4**.
- **A mod is permanent**: it can't be removed or replaced. Fill slots in order of certainty.
- Grades are bought or raised at **Pioneer Supplies** (credits + micro-resources). Mods are
  applied **on foot at the engineer's base**. Odyssey engineers have no grades: once unlocked,
  they apply all their mods.
- Pioneer Supplies sometimes sells **pre-upgraded / pre-engineered** gear. Stock is limited and
  refreshes weekly (Thursday). Worth checking before raising grades by hand.

**Target build: 4 mods**

*Build revised the same day by Tonton Marcel: Improved Jump Assist replaces Enhanced Tracking
(roof-to-roof movement without draining the sprint meter), and Improved Battery Capacity
replaces Reduced Tool Battery Consumption (the arc cutter is rarely used, so a bigger battery
is worth more than cheaper tools).*

| Slot | Mod | Why it matters for a heist | Engineer |
|---|---|---|---|
| 1 | **Extra Backpack Capacity** | More data, items and assets per landing | Domino Green |
| 2 | **Improved Jump Assist** | Roof-to-roof routes over the settlement, out of NPC sight lines, without spending the sprint meter | Yarden Bond (also Hero Ferrari) |
| 3 | **Quieter Footsteps** | Footstep noise is a detection input. Fewer witnesses for downloads (the 21 Oct lesson, §1) | Yarden Bond |
| 4 | **Improved Battery Capacity** | +50 % suit battery: longer stays on site, more margin for the tools and shields on the way out | Oden Geiger (also Wellington Beck) |

- **Order of the slots:** each mod goes in as soon as its engineer is unlocked. Battery comes
  last because Oden Geiger is at the end of the longest chain.
- **Dropped:** Enhanced Tracking and Reduced Tool Battery Consumption, both Domino Green.
  **Night Vision** (Oden Geiger) is out of the build too. If cutting the reactor (§1 step 3)
  becomes the standard approach, it could take slot 4 instead of the battery. Decide when the
  suit reaches G5.
- **Escape mods** (Combat Movement Speed, Increased Sprint Duration, Damage Resistance) belong on
  the Dominator, not here.

**Roadmap**
- [ ] **Stage A — Domino Green, slot 1 (now).** ✔ Domino Green **unlocked** (12 Nov). Next:
      apply **Extra Backpack Capacity** to the current G2. Cheapest step, and it pays off at once
      on PP download runs. **Blocked on two data items: Weapon Inventory and Digital Designs**
      (Tonton Marcel, 11 Nov) — never found yet in any settlement visit (`../elite-loot/
      loot_stats.py --item weaponinventory`). Next tries: other settlement types in HR 5295,
      every data port even without Power data, bartender stock.
- [ ] **Stage B — G3 and G4, slots 2–3.** Raise the suit to G3, then G4, at Pioneer Supplies.
      A bought suit starts with no mods, so raising the modded one is better. Once the Domino
      Green → Kit Fowler → Yarden Bond chain is done (`Engineers & Materials.md` §3), apply
      **Improved Jump Assist** and **Quieter Footsteps** at Yarden Bond, in one visit.
- [ ] **Stage C — G5, slot 4.** Raise the suit to G5. Once the Jude Navarro → Terra Velasquez →
      Oden Geiger chain is done (`Engineers & Materials.md` §3), apply **Improved Battery
      Capacity**, or Night Vision (see above).
- [ ] **Stage D — later, only if armed PP assignments appear:** a suppressed sidearm. Stealth
      mods for it: **Audio Masking** (Yarden Bond), **Noise Suppressor** (Hero Ferrari, Terra
      Velasquez).

**Micro-resource shopping list**
- **Grade raises** (exact counts are shown by the Pioneer Supplies storekeeper): before Update
  18.08, the G5 step alone cost 15 each of **Suit Schematic, Health Monitor, Power Regulator,
  Manufacturing Instructions**, with smaller amounts for the lower steps. Community reports say
  18.08 cut Odyssey upgrade costs to about a quarter. Stock on 12 Nov (ship locker): Suit
  Schematic **1**, Health Monitor **10**, Power Regulator 3, Manufacturing Instructions **2**.
  **Suit Schematics are the real gap** (Tonton Marcel: mostly data and suit schematics missing
  for the four suits to G5).
  - ⚠ **Don't sell Health Monitors:** 39 went to the Akers Station bartender on 9 Nov with the
    surplus — they're one of the four grade-raise items. Keep all four kinds out of bartender
    sales.
- **Mods:** about 500,000–750,000 CR each, plus materials. Improved Battery Capacity, for
  example: 5 Reactor Output Review, 8 Maintenance Logs, 3 Ion Battery, 5 Micro Supercapacitor,
  5 Electrical Wiring, 750,000 CR (wiki figure, possibly from before 18.08). Stock on 3 Nov:
  the components are covered (Ion Battery 4, Micro Supercapacitor 22, Electrical Wiring 20).
  The two data items, Reactor Output Review and Maintenance Logs, are at 0.
- **Planning tool:** *Elite Dangerous Odyssey Materials Helper* (EDOMH, GitHub
  `jixxed/ed-odyssey-materials-helper`) reads the same journal files and turns a wishlist
  (suit grades + mods) into an exact shopping list, including which settlement type drops what.
  Simpler than keeping counts here by hand.

**Where the materials come from** (cheapest first)
1. **Mission rewards, materials option:** on-foot missions already paid Weapon Schematics and
   Chemical Patents this way (cards 4.1, 4.5). Sort the board by material rewards, and check
   several stations.
2. **Reactivation / restore missions** (§1 step 1, §3 Phase 1): zero risk. Ten of them also
   unlock **Jude Navarro**, the start of the Night Vision branch. Two objectives in one.
3. **Settlement data ports and lockers** during the PP download runs already planned: grab
   ordinary data and items while you're inside, once the Power data is in the backpack (only
   with no witnesses, §1). Suit Schematics come from lockers; Manufacturing Instructions
   from data ports, mostly at industrial settlements. **Our finds so far** (journal, script
   `../elite-loot/loot_stats.py`): the only kept Suit Schematic and both Manufacturing
   Instructions came from **Fry Agricultural Hub** (Senones, anarchy, 9 Nov); a second Suit
   Schematic, from Hakimi Manufacturing (industrial), was a heist-mission item and went to the
   client. A settlement keeps giving the same locker loot visit after visit (Techno Defence,
   §5.4), so new items mean new settlements, not more visits.
4. **Bartender:** barter surplus components (Circuit Switch 38, Metal Coil 34, Memory Chip 29
   are well stocked) for the missing ones. Selling data to a bartender is also how several
   engineers unlock (`Engineers & Materials.md` §3).

---

## 3. PROGRESSION BY PHASE

**Phase 1 — zero-risk** (moved from §5.4)
- [ ] **Abandoned-settlement reactivation** mission — zero NPCs, zero alarms. Gathers
      micro-resources and is the on-foot equivalent of the Low RES/PP loops (`Powerplay Missions.md` §3): safe, and a
      real data point for what it actually yields.
- [ ] **Data recovery** mission at a powered-down site — same risk profile, more data-type
      materials.

**Phase 2** (moved from §5.4)
- [x] On-foot gear: Artemis suit + Genetic Sampler (exobiology) — in use since 9 Nov 2026,
      5 species sampled that day (`Powerplay Missions.md` card 4.15).

**Phase 3 — first real risk** (moved from §5.4)
- [ ] On-foot: **Frontline conflict zones** first (§5.2 step 5) — allies nearby, free respawns,
      failure costs nothing. Safe combat practice, mirroring the ship-side ramp (Pacifier Low RES
      → Nemesis HazRES) with the same "prove it safely before it counts" logic.
- [ ] On-foot: **cut-the-reactor infiltration** at an active settlement (§5.2 step 3) — the first
      real on-foot risk, timed to match the combat confidence built on the ship side (§5.4). Still untried as of
      23 Sept (§4).
- [ ] Dominator suit (combat) for Dart's missions. The upgraded Maverick (sabotage, PP data)
      moved forward on 3 Nov 2026 and now has its own roadmap (§2.1), run alongside Phase 1.

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

- **Stats:** 4 runs · 1 failed, 3 success · last: 4 Nov, two covert heists
  (`Mission_OnFoot_Heist_Covert_MB`): a personal computer from **Vannier Drilling Rigs** (HIP
  5623, extraction), for Medupe City, 66,585 CR (21:12); a **Suit Schematic** from **Hakimi
  Manufacturing** (Guuguyni, industrial), for Shen Terminal, 177,843 CR (22:46) — the stolen item
  goes to the client. Three covert heists done in all — they may count toward Terra Velasquez's 6
  (`Engineers & Materials.md` §3). 29 Sept, **Simon Biochemical Forum**
  (Sarana 6 b, high-tech, anarchy faction) — covert variant (`Mission_OnFoot_Heist_Covert_MB`),
  biological samples stolen, 191,735 CR + data materials (offer 314,235 CR; the difference is
  the materials reward option).

### 4.4 Settlement reactivation / data recovery

- Not yet played — §1 steps 1–2, Phase 1 in §3 above.

### 4.5 On-foot massacre (`Mission_OnFoot_MassacreIllegal_MB`)

- **Recognise it:** kill N members of a named faction's personnel at a settlement.
- **Run:**
  - [ ] Use the SRV to come and go (in and out of the settlement several times on 29 Sept).
  - [ ] While the site is cleared, open its data ports: Power data, possibly classified
        (`Powerplay Missions.md` 4.8).
- **Pitfalls:** each kill logs `onFoot_murder` with a 1,000 CR bounty from the target faction,
  even in an anarchy system — check your status/bounties before docking elsewhere. Killing far
  more than required (about 45 for 11) adds bounties but no pay.
- **Stats:** 1 run, success · last: 29 Sept, **Sharma Analytics Installation** (Sarana 6 a,
  high-tech) for The Eldaren — 18,863 CR + 14× Weapon Schematic (offer 308,863 CR; the
  materials option was taken again).

---

## 5. SETTLEMENT ROUTES

*Added 3 Nov 2026. One card per settlement worth repeating: the layout, the route through it,
and where the NPCs are. Odyssey settlements reportedly come in about 28 layout types, and
settlements that share a type share a layout, so a route learned here should work at any
settlement of the same type. Same growth rule as §4: refine in place.*

**Map reference: Odyssey Site Maps** (CMDR DeCarabas and CMDR Thing Fish, updated Oct 2026):
<https://voz-decarabas.github.io/Odyssey-Site-Maps/browser.html>. One annotated map per layout
(the 28 = 4 tourist, 5 agricultural, 5 military, 5 industrial, 5 extraction, 4 high-tech), with
airlocks and their access level, data ports, terminals, alarm panel, PP containers, and hints on
where to scan. **There is no marker for the authorisation switch**, so that's the one thing to
note from play. Maps can miss things: Extraction 2 lacks a data port on the first floor of CMD
(§5.1). And a marker's text label can be wrong even when its position on the image is right
(Agriculture 1's alarm, §5.3). Go by the image. Data-port counts can differ between settlements of the same layout (forum
reports), so check them on the first visit.

### 5.1 Ferenczi-houlden Extraction Exchange (extraction layout)

- **Where:** Crucis Sector OY-R b4-4 C 3, unoccupied system. Used for the Power data raid
  (`Powerplay Missions.md` §3, card 4.8). Hand-in at Hale Gateway, Tripitaka.
- **Layout:** simple. CMD (command), HAB ×2, STO (storage), PWR (power), EXT (extraction).
  **8 data ports** in all. Journal: 7–9 downloads and 9–13 units per landing over 9 landings,
  2–3 Nov.
- **Arrival:** dock on the settlement's own pad.
- **Map: "Extraction 2 – small (+)"** on Odyssey Site Maps (recognised on sight by Tonton
  Marcel, 3 Nov). Two HABs. The map shows the alarm panel next to a data port (the CMD switch
  room, step 2), a "possible scan through window" hint (step 1) and 2 PP containers. **It lists
  only 7 data ports: it misses the one on the first floor of CMD** (step 3), so there are 8 in
  play. *(Extraction 1 – medium also has 8 ports with the alarm next to one, which is why it
  looked like the match from the map data alone.)*

**Route** (Tonton Marcel, 3 Nov)
1. **Rooftops to the level-3 NPC.** Off the ship, jump across the HAB, STO, PWR and CMD roofs.
   The level-3 NPC stands near a window on the CMD rooftop. Scan them (Profile Analyser clone).
2. **CMD, ground floor: the switch room.** Enter, walk past a level-2 NPC, into an **empty,
   unguarded room** (restricted zone). It holds **the alarm switch, the authorisation scan
   switch and a data port**. Switch both off, download (**port 1**).
3. **CMD, upstairs.** A restricted room with one NPC patrolling a simple back-and-forth line.
   Reach the port as soon as their back is turned, start the download, hide behind a crate
   (**port 2**).
4. **HAB next door:** empty, one port, wait inside while it downloads (**port 3**).
5. **EXT, across the settlement, upstairs:** one port, one NPC on a 3-point patrol. There's no
   way out during the download, so circle the big round pillar, keeping it between you and the
   NPC (**port 4**).
6. **Second HAB:** empty, one port (**port 5**).
7. **STO:** 2 ports. Easy: hide behind the crates while each downloads (**ports 6–7**).
8. **PWR, last: the difficult one.** 2 NPCs in a small area, on two different patrol cycles.
   It's where most of the catches (download or trespass) happen (**port 8**).
9. Back to the ship, lift off, come straight back for the next landing.

**Pitfalls and fixes**
- **PWR timing:** the tempting moment, both backs turned, often comes when one of them has
  already had their back turned for a while, so they turn around mid-download. Better: wait
  until the NPC with the *longer* cycle has *just* turned away, then start. If that NPC's cycle
  is shorter than the download (up to 30 s for classified data, §1), wait for the next window.
- **Download times vary** (10–30 s by type, §1). In patrolled rooms (CMD upstairs, EXT, PWR)
  you can't know the type before you start, so count on the full 30 s.
- **Two long downloads in a row** can catch you: an NPC walking back past the port notices the
  hack, turns hostile in their area and starts searching. Break line of sight, then hide or
  leave the building.
- **Don't run past a guard who is scanning you** (§1): it's a fine even when you're clean.

**Heist Maverick payoff** (§2.1): this route is why **Improved Jump Assist** (the rooftop
approach in step 1, the jump across in step 5) and **Quieter Footsteps** (EXT pillar, PWR) are
in the build.

**Stats:** 9 full landings (2 Nov noon and evening, 3 Nov) · 13–26 min per landing (most
13–17; the first landing of a session runs longest), first to last download in 9–22 min · fines:
2 data transfer (2 Nov noon), 2 failure to submit (2 Nov 11:18 on the first scouting landing,
3 Nov 18:56), none on 2 Nov evening (4 landings).

### 5.2 Kewell's Club (tourist layout)

- **Where:** Reorte 5 a, Nakato Kaine Exploited (Mahon and Kaine present, no Aisling). Used for
  the **tracing malware** uploads (`Powerplay Missions.md` card 4.14).
- **Layout:** a big central **HAB on two floors**, **5 small HABs**, a **bar** and a **PWR**.
  8 data ports (card 4.14).
- **Map: "Tourist 4 – small (+)"** on Odyssey Site Maps (confirmed by Tonton Marcel, 3 Nov).
  It shows **8 data ports** (the site lists 9, but two share
  the same spot) and the **alarm panel at the very top of the central building**, which fits
  the second-floor find in step 1. The map's hint: an L3 sometimes comes up onto the roof for an
  easy scan. The other tourist layouts don't fit: Tourist 2 and 3 have the alarm in the reactor
  room, and Tourist 1 has only 2 data ports.
- **Population: the hard part.** Full of guards, pilots and travellers, and almost **all of
  them may ask to scan you**. The big HAB holds several of them, and their patrols take the
  stairs up and down on different paths, so the gaps for slipping through are short.

**Route** (Tonton Marcel, 3 Nov; learned over several sessions with re-logs to watch the place)
1. **Alarm switch: big HAB, second floor.** Spotted by chance **through a window** of one of the
   second-floor rooms. A **level-2 NPC can be scanned from the window of the next room**, which
   gives you the clone without going inside.
2. **Into the alarm room.** Another NPC is in the room: wait until they turn their back, then
   switch the alarm off.
3. **No authorisation switch found.** It may be in PWR, not yet checked. So the clearance
   checks stay on for the rest of the run.
4. **Data ports in the small HABs.** Move between the HABs avoiding the patrols that cross the
   rooms, circle the furniture when the room allows it, upload, and re-clone an NPC each time
   the credentials have had to be dropped (below).

**Pitfalls and fixes**
- **When a guard is about to scan you with a cloned profile, drop the credentials** to avoid
  the fine, then re-scan another NPC afterwards (§1). At this settlement that happens over and
  over, which is what makes it slow.
- **Next visit:** look for the authorisation switch in PWR. If it's there, this settlement
  becomes a run like Ferenczi-houlden (§5.1): no more credentials to manage once it's off.
- **Not a place to steal goods** (card 4.12): too many potential scans in almost every
  building.
- Doable, but it takes patience and observation, much more than the extraction layout.

**Stats** (journal): 8 tracing-malware uploads, 195 merits each, the assignment's 5,200 paid on
the 8th (2 Nov 09:59).
- **31 Oct 16:16–16:39:** first look. Injection malware didn't work here (card 4.14).
- **1 Nov 18:32–19:24:** 3 landings, 2 uploads.
- **2 Nov 07:33–08:00:** 5 uploads in 25 min, once the route was known. A 6th at 09:51–09:59.
- **Fines:** 1 failure to submit (1 Nov 18:58), 2 data transfer (1 Nov 19:22, 2 Nov 07:58).

### 5.3 Baker's Plantation (agricultural layout)

- **Where:** Crucis Sector OY-R b4-4 C 2, the same system as Ferenczi-houlden (§5.1). Tried
  before the extraction site, for the classified Power data (`Powerplay Missions.md` card 4.8).
- **Map: "Agriculture 1 – small (+)"** on Odyssey Site Maps (recognised by Tonton Marcel,
  3 Nov). The map shows **7 data ports**, 2 PP containers and the hint "scan L3 through the roof
  while crouching". **The map image is right**: its alarm marker sits in the big AGRI building,
  where Tonton Marcel found the switch. PWR is a small building in the middle of the map, with
  no alarm marker. Only the marker's text label is wrong ("in the unrestricted area of the
  power building"). Lesson for this site: **trust the map image over the label text** (data
  read 3 Nov, image checked by Tonton Marcel).
- **Population: easy.** Lots of NPCs, but only scientists and technicians, **nobody who asks for
  a scan** (no pilots, travellers or guards inside), apart from one guard at the front door of
  the big building.

**Route** (Tonton Marcel, 3 Nov)
1. **Roof of the big agricultural building** near the large landing pad: watch from there. A
   **level-3 NPC wanders on the roof**: scan them.
2. **In by the back door**, into the building's storage area, climb up: **the alarm switch** is
   there. Switch it off.
3. **Data ports:** STO, the agricultural building with the glass domes, and the HABs all have
   one. The port **at the entrance of the big building** is the hard one, right next to the
   front-door guard.

**Verdict:** the easiest alarm of the three sites so far, and few scans. But **no classified
Power data** in 5 downloads (2 Nov: 5 industrial, 1 association), against about 1 in 8 at the
extraction site (card 4.8). Too few downloads to call it, but the extraction site won on
results.

**Stats** (journal): 30 Oct 21:14, first landing (scouting) · 31 Oct 10:33–11:06: no data, but
2 Power goods (data storage device, military plan, handed in for 92 merits each on 2 Nov) and
consumables from lockers; 1 failure-to-submit fine (11:05) · 2 Nov 10:08–10:34: 5 downloads, 6
units, all common data.

### 5.4 Techno Defence Facility (military layout)

- **Where:** Tucanae Sector BV-X b1-1 5, **unoccupied** (only Aisling present), one jump from
  Cubeo. Owner: **HIP 1914 Imperial Society** — a Navy-rank faction, so every fine hurts a
  relationship you're building. Used for Power data (`Powerplay Missions.md` cards 4.8, 4.11)
  and injection malware (card 4.14).
- **Map: "Military 3"** on Odyssey Site Maps (chosen by Tonton Marcel, 6–7 Nov): **5 data
  ports**.
- **Population: the hardest so far.** More guards, more restricted zones, smaller rooms; outside
  turrets, drones and ships swarm when the alarm goes off. The bar's data port needs no clearance
  (21 Oct).
- **Alarm:** console in the command building (21 Oct, §1 "Play-tested"). With the alarm off,
  turrets, drones and ships stay quiet; NPCs who see a download still fire.

**Yield per landing** (journal, 9 landings 6–8 Nov): **5–7 Power data** (52 in all: association
13, political 12, industrial 11, **classified 9**, research 7), plus ordinary data (shareholder
information, patient history, medical records, political affiliations, pharmaceutical patents,
faction donator lists), and from coded lockers the backpack's **40 goods / 60 components**.
Locker loot is **the same set every visit**: ion batteries, graphene, memory chips, circuit
switches, optical lenses, epoxy, metal coils; compact libraries, personal computers, Insight
goods, G-Meds, health monitors; **Surveillance Equipment** (7 so far, Kit Fowler's referral
item, `Engineers & Materials.md` §3).

**Stats** (journal): 6 Nov evening, 2 landings (data, one upload lost to a crash ≈23:00) · 7 Nov
10:19–11:44, 3 landings,
**undetected**, 11 malware uploads (assignment paid) · 7 Nov 16:13–17:37, 3 landings with
locker looting — property theft (17:09) and failure to submit (17:28), 500 CR each · 8 Nov
10:29–10:50 and 16:58–17:26, 2 landings, alarms off, no fine.

### 5.5 Anarchy loot sites — Senones and HR 5295

*Push and illegal goods hunt, 9–11 Nov (`Engineers & Materials.md` §3). Anarchy stations have
bartenders who buy stolen and illegal goods (Akers Station, 9 and 11 Nov).*

- **Kolsuk Agricultural Centre** (Senones 1, Diamond Frogs): very small; guards wait in the
  corners while you wait for a level-3 NPC to turn their back. 2 visits, 12 items. Not worth it.
- **Fry Agricultural Hub** (Senones 1, Diamond Frogs): **many lockers** — 2 visits, ≈120 items:
  12 Hush, 5 Lazarus, 1 **Suit Schematic**, 2 **Manufacturing Instructions**, Power goods, no
  Push.
- **Barbier Tourism Complex** (HR 5295, anarchy, every settlement run by a local militia):
  picked for its **HAB building lockers** — **5 Push** in one visit (11 Nov), plus 5 Hush and 4
  Lazarus. Tourism population: guards, pilots, mercenaries in the HABs, a scan risk everywhere
  (§1).
- **HR 5295 has several settlement types** — raid each in turn to learn what it drops (the
  script records it). The system has its own bartender: sell the surplus there instead of
  flying to **Akers Station, Senones** (anarchy, bartender used 9 and 11 Nov).
- Papacosta Horticultural Exchange (Rata Bares, anarchy) was visited on 9 Nov: no loot logged.
