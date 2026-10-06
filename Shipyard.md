# SHIPYARD — CMDR ONCLEMARCEL
## Ship cards: roles, upgrade checklists, build specs

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Satellite of `In-Game Operations.md` §5 (Roadmap): the main line there holds phases, milestones
> and checkpoints; this file holds the per-ship work. **Current fits** stay in
> `In-Game Operations.md` §2 (fleet table) and aren't repeated here. Created 25 September 2026
> when §5 was split into satellite files (content moved, not rewritten).
> **References:** a bare `§N` points to `In-Game Operations.md`; "annex A1…B9" points to §3 of
> this file; "archived in §4" points to §4 of this file (completed refit plans); "Engineers" =
> `Engineers & Materials.md`.

---

## 1. CURRENT FLEET

### Astroforge — Imperial Clipper (mining)

*Role:* laser mining, PP mining. *Fate:* sold in Phase 5 once the Hephaestus beats her. *Spec:*
annex A1.

- [x] Astroforge v2 fitted (annex A1, updated 3 Oct 2026 from the Inara export): 128 t, 4A
      refinery, prospector, SCB; shield, FSD, distributor, thrusters and boosters engineered.

**Later plan** (options in annex A1)
- [ ] 4A Fuel Scoop → 4E Cargo Rack (+16 t → 144 t); scoop stored (intra-system principle).
- [ ] *(Optional)* Boosters Heavy Duty G1 → G3 (Lei Cheung).
- [ ] *(Optional)* Max-cargo variant (≈ 192 t) if mining becomes more frequent.
- PP mining loop: `Powerplay Missions.md` §3.

### Pacifier — Imperial Clipper (combat trainer → Diplomat)

*Role:* combat trainer, bounty hunting (Low RES). *Fate:* becomes the Diplomat in Phase 6. *Spec:*
annex A3 (v2), annex B4 (Diplomat).

- [x] Pacifier: bounties settled — impound cleared 23 Sept (`ClearImpound`, §4).
- [x] Pacifier: cargo racks swapped for hull/module reinforcements, an FSD interdictor, a
      planetary hangar and a multi-drone controller, plus a newly bought 3A fuel scoop (23 Sept,
      §4) — cargo down to 128 t.
- [~] **Next refit** (5 Oct 2026). Pacifier V2 — combat-CG and Low RES build, survival first.
      Full checklist below ("Pacifier V2 — '90 %' plan"); target build in annex A3.
- [ ] *(If time allows)* Test run in a Low RES / low-intensity CZ of the current combat CG.
- [ ] Power distribution priorities reviewed (weekly-routine task, §5.1). Note: the Inara export
      of 3 Oct shows the **main thrusters switched off** — fix before anything else.

**Pacifier V2 — "90 %" plan (Clipper, solo, combat CG / Low RES)** — added 3 Oct 2026, same
model as The Brick V2. Estimated time **4–7 h** (all engineers already unlocked by The Brick V2).

*Why:* a combat-bond CG is open, and the Pacifier is the only combat ship in the fleet until the
Nemesis (Phase 3). Combat rank is still low, so survival comes before damage: a bigger shield,
an SCB and reinforcements instead of the leftover utility modules (interdictor, hangar, drones).
It also trains the CZ routine (pick a side, cash bonds often) before the Nemesis and the Charybdis.
*Why "90 %":* every engineer needed is already on the roster thanks to The Brick V2, so G5 goes
on the shield (Lei Cheung) and the distributor (The Dweller); boosters (Lei Cheung) and thrusters
(Farseer) stop at G3. Weapons stay stock in this plan. The remaining 10 % is listed under
"Beyond the 90 % plan" at the end.
*Combat rule:* low-intensity CZs and Low RES only, until step 7 is validated (annex A3,
training progression: Medium only once shield and boosters are G3+).

| Slot | Current loadout (Inara, 3 Oct) | Pacifier V2 (90 % plan) |
|---|---|---|
| Hardpoints | 2× Beam Laser (L, Gimballed), 2× Multi-Cannon (M, Turret) | Unchanged (engineering: see "Beyond") |
| Utility | 2× stock 0A Shield Booster, 2× Chaff | **2× 0A Shield Booster Heavy Duty G3** (+ Super Capacitors if offered), **1× Heatsink**, 1× Chaff |
| Power Plant | 6A stock | 6A stock (unchanged — power check in step 1) |
| Thrusters | 6A stock (**switched off** in the export) | **6A Dirty Drive G3** (+ Drag Drives if offered) |
| FSD | 5A Fast Boot G5 | Unchanged |
| Distributor | 6A stock | **6A Charge Enhanced G5 + Super Conduits** |
| Sensors / Life support / Fuel | 5D / 5D / 4C | Unchanged |
| Armour | Military Grade Composite | Unchanged |
| Slot 7 | 7E Cargo Rack (128 t) | **7A Shield Generator — Reinforced G5 + Hi-Cap** |
| Slot 6 | 6A Shield Generator | **6A Shield Cell Bank** |
| Slots 4 / 4 | 2× 4D Hull Reinforcement | Unchanged |
| Slots 3 / 3 | Multi-drone controller, 3A Fuel Scoop | **3D Module Reinforcement**, **3D Hull Reinforcement** |
| Slots 2 / 2 | FSD Interdictor, Planetary Vehicle Hangar | **2A Fuel Scoop**, 2E Cargo Rack (4 t) |
| Slot 1 | 1D Module Reinforcement | 1E Cargo Rack (2 t), as in annex A3 |

*1. Preparation (≈ 30 min)*
- [ ] Build the target in EDSY: 7A shield + 6A SCB + 2 beams on the stock 6A power plant —
      check the power draw with hardpoints deployed and the SCB firing.
- [ ] Set power priorities: thrusters, FSD, shield, life support on priority 1; SCB, weapons,
      heatsink on lower priorities so the shield never drops.
- [ ] Inara crafting lists for the 4 blueprints (shield, boosters, distributor, thrusters),
      material stock inventoried (shortfalls in step 3).

*2. Outfitting (≈ 30 min)*
- [ ] Find a station selling the 7A Shield Generator and the 6A Shield Cell Bank (Inara).
- [ ] Budget: 7A shield ≈ 50M (to verify) + SCB; the rebuy goes up accordingly (5 % of value).
- [ ] **Store** the 7E Cargo Rack (needed again for the Diplomat, annex B4) and the 6A shield.
- [ ] Sell or store the FSD interdictor, planetary hangar, multi-drone controller and 3A scoop.
- [ ] Sell one Chaff Launcher; buy a Heatsink Launcher.
- [ ] Fit the 7A shield (slot 7), 6A SCB (slot 6), 3D module and 3D hull reinforcements (slots 3),
      2A fuel scoop and 2E cargo rack (slots 2), 1E cargo rack (slot 1).
- [ ] Fire groups: SCB and heatsink on the same group as a secondary fire key.

*3. Materials (≈ 1–3 h, depending on stock left after The Brick V2)* — same rule: pick Imperial
Navy and Powerplay missions by their material rewards; trade surpluses at a Material Trader.
- [ ] Shield Reinforced G1 → G5 + Hi-Cap: same recipe as The Brick V2 step 5.
- [ ] Distributor Super Conduits: same recipe as The Brick V2 step 4.
- [ ] Distributor Charge Enhanced G1 → G5, boosters Heavy Duty G1 → G3, thrusters Dirty Drive
      G1 → G3: shortfalls to fill in from the Inara lists.
- [ ] Re-check the Inara lists: all green?

*4. Lei Cheung — Laksak, Trader's Rest (≈ 1 h 30)*
- Shield (7A):
  - [ ] Reinforced G1 → G5 (recipe as The Brick V2 step 5).
  - [ ] Experimental **Hi-Cap**.
- Boosters:
  - [ ] 2 boosters Heavy Duty G1 → G3.
  - [ ] **Super Capacitors** if offered (checked during The Brick V2), on both boosters.

*5. The Dweller — Wyrd, Black Hide (≈ 1 h)* — distributor
- [ ] Charge Enhanced G1 → G5.
- [ ] Experimental **Super Conduits**.

*6. Felicity Farseer — Deciat (≈ 45 min)* — thrusters
- [ ] Dirty Drive G1 → G3 on the 6A thrusters.
- [ ] **Drag Drives** if offered.

*7. Validation (≈ 30 min)*
- [ ] Export the loadout to EDSY and compare against the plan (power, shield MJ, resistances).
- [ ] Check that the thrusters are **on** and the power margin holds with hardpoints deployed.
- [ ] Test round in a Low RES: SCB + heatsink timing, shield regen, heat level.
- [ ] Decide the 4th utility: keep the chaff, or a 3rd Heavy Duty booster if heat stays low.
- [ ] First low-intensity CZ for the CG: pick a side on entry, cash the bonds regularly.

*Beyond the 90 % plan (later)*
- [ ] *(Optional)* Boosters to G5 with Didi Vatermann (Leesti) — same unlock chain as The
      Brick V2 "Beyond".
- [ ] *(Optional)* Weapons per annex A3 targets (beams Efficient + Thermal Vent, multi-cannons
      Overcharged + Corrosive / Incendiary) — engineers to identify in Engineers.
- [ ] *(Optional)* Sensors Long Range (annex A3 target).
- [ ] Medium RES / medium-intensity CZ once steps 4–7 are done; hand-off to the Nemesis in Phase 3.

### Dart — Imperial Courier (Odyssey taxi, recovery, snatch and flee)

*Role:* black-box missions (snatch and flee), material recovery (HGE, Jameson crash site, raw
materials), Odyssey taxi with pre-landing clearance and extraction. *Fate:* kept (Dart v2).
*Spec:* annex A2.

- [x] Dart V2 Tier 1 done (5 Oct 2026): 68.76 t, 38.8 ly, 10 t cargo; 3A fuel scoop kept on
      purpose. Completed plan archived in §4 ("Dart V2 — Tier 1"); target build in annex A2.

**Later plan**
- [ ] DSS Expanded G3 → G5 (Lei Cheung) — the last Tier 1 item.
- [ ] *(Optional)* Sensors Lightweight G5: re-roll to full quality (60 % today).

**Tier 2 — short unlocks (Liz Ryder, Marco Qwent)**
- [ ] Unlock Liz Ryder (only "Known" today, Engineers); missile rack Lightweight G1 → G5 + Stripped Down.
- [ ] Unlock Marco Qwent; power plant Overcharged G1 → G4 + Stripped Down (G5 is beyond
      Qwent — see Tier 3).

**Tier 3 — long unlocks (Professor Palin, Colonia engineers, others)**
- [ ] Thrusters Dirty Drive G4 → G5: Professor Palin (Arque) or a Colonia engineer.
- [ ] Pulse lasers Lightweight G5: an engineer with G5 lasers (bubble or Colonia, Engineers).
- [ ] Boosters Resistance Augmented G4 → G5: Didi Vatermann (Leesti).
- [ ] Power plant Overcharged G5: an engineer with G5 power plants (Engineers).
- [ ] Lightweight on chaff, heatsink and collector; life support, fuel scoop and Extended cargo
      racks: engineers to identify (Engineers).
- [ ] *(Optional)* Enhanced Performance Thrusters (Palin) + Drive Distributors: the 800+ m/s
      variant — check the heat and the hangar mass in EDSY first.

### The Brick — Type-9 Heavy (bulk trade, bridge ship)

*Role:* trade CGs, PP trade. *Fate:* stored at the Medupe City museum in Phase 5, replaced by the
Cornucopia. *Spec:* annex A5.

- [x] The Brick V2 — the trade-merit engine, optimised for mass, manoeuvrability and interdiction
      escapes. Completed plan archived in §4 ("The Brick V2"); target build in annex A5.
- Lightweight engineering reviewed 4 Oct 2026: not worth it (cargo dominates the laden mass).

**Later plan (beyond the 90 % plan)**
- [ ] *(Optional)* Thrusters to Dirty Drive G5 with Professor Palin (Arque):
  - [ ] Unlock chain: Martuuk → Qwent (Sirius permit, 25 Modular Terminals).
  - [ ] Palin (5,000 ly or an Unclassified Relic):
    - [ ] 25 Sensor Fragments: Solati system, planet Halla (coordinates 36.9423 / −100.2683).
- [ ] *(Optional)* Boosters to G5 with Didi Vatermann (Leesti): chain Tod McQuinn → Selene Jean
      (500 t mined, 10 Painite) → Vatermann (Merchant rank, 50 Lavian Brandy).

### Hyperion — Asp Explorer (exploration, bridge ship)

*Role:* exploration, exobiology, Guardian expedition (Phase 2). *Fate:* stored at the museum in
Phase 6 once Marco Polo's exploration configuration beats her range; her DSS migrates to that
hull (Marco Polo has her own 5A SCO FSD). *Spec:* annex A4.

- [x] Set Hyperion's FSD to G5. (Confirmed 23 Sept — Felicity Farseer, Deciat, §4.)
- [~] Hyperion thrusters G1 → G3, Dirty Drive Tuning + Overloaded (23 Sept, §4) — G5 (annex A4's
      target) not yet reached.
- [ ] Hyperion v2 (annex A4, §5.7): missiles removed, AFMU 3A, FSD G5.

### Marco Polo — Corsair (long-range taxi now, exploration later; ex-"Hermes")

*Role:* one hull, two configurations swapped at a station (same principle as the Dart):
- **Taxi configuration** (now, annex A6) — fly to a distant target (a CG, an engineer, a remote
  station), dock, then transfer the ship the job needs to that station. Transfers can only be
  requested from the station where the receiving ship is docked, so start the transfer on arrival
  and use the wait to scout, take missions or cash in.
- **Exploration configuration** (later, annex B1) — the taxi core plus the exploration kit:
  hangar + Scarab, DSS, Guardian FSD booster, second AFMU, hull reinforcement, heatsink, SCA.
*Fate:* kept; replaces the Hyperion once the exploration configuration beats her range.
*Spec:* annex A6 (taxi) and annex B1 (exploration).
*Merge (5 Oct 2026):* the "Hermes" taxi project (4 Oct) is the light version of the Marco Polo
planned in annex B1 — one Corsair instead of two. The core and all its engineering are shared;
only the optional modules change between configurations. Bought ahead of the Nemesis, so she is
the fleet's first Corsair.

- [~] Taxi configuration — added 4 Oct 2026 (EDSY target: 316.4 t unladen, **67.9 ly**, no cargo).
      Shield 5D + 6D AFMU added on 4 Oct for 1.6 ly (AFMU is massless; the shield costs 7.2 t).
- [ ] Exploration configuration (annex B1): buy and store the exploration kit; Guardian FSD
      booster once unlocked (Hyperion's Guardian expedition, Phase 2).

**Marco Polo — taxi configuration "90 %" plan (Corsair, solo, long-range taxi)** — added 4 Oct 2026, same model as
the Dart V2 (three tiers by engineer access).

*Why:* range comes from mass, as on the Dart — D-rated core, Lightweight G5 everywhere and the
SCO FSD at Increased Range G5 + Mass Manager. Speed and firepower don't matter; survival does
(interdictions near CGs, neutron boosting), hence the shield and the AFMU.
*Known limits:* no cargo; thrusters optimised for 275.6 t vs 316 t unladen (slow but fine for
a taxi); 16 t tank. AFMU off by default — switch it on only to repair (power draw while active).

**Tier 1 — reachable now (Farseer, The Dweller, Lei Cheung)**

*1. Preparation (≈ 20 min)*
- [ ] EDSY: Tier 1 fit (power plant Overcharged G1, thrusters Dirty Drive G3, life support
      stock) — note the Tier 1 range (expected a little under 67.9 ly: ≈ 4 t heavier).
- [ ] Power check with the stock 4D power plant (Overcharged only adds margin).
- [ ] Inara crafting lists "Marco Polo Tier 1" for the 6 blueprints, then add the totals to the
      Dart V2 shortfalls (both ships draw on the same stock — see step 3).

*2. Outfitting (≈ 30 min)*
- [ ] Buy and fit: 4D power plant, 4D thrusters, 5A SCO FSD, 4D life support, 5D distributor,
      6D sensors, 4C fuel tank, 6A fuel scoop, 6D AFMU, 5D shield generator, Advanced Docking
      Computer.
- [ ] *(Optional)* Supercruise Assist in a free small slot (almost no mass).
- [ ] Power priorities: everything on 1 except the AFMU (switched off when not repairing).

*3. Materials — expected (shield and sensors recipes known from the Dart V2 lists; the rest
from the Inara lists)*

| Blueprint | Expected materials (G1 → top grade) |
|---|---|
| Shield 5D Reinforced G1→G5 | Phosphorus 6, Conductive Components 5, Mechanical Components 3, Configurable Components 4, Manganese 4, Conductive Ceramics 4, **Improvised Components 5**, **Arsenic 5**, Conductive Polymers 5 (+ Stripped Down: Inara) |
| Sensors 6D Lightweight G1→G5 | Phosphorus 1, Salvaged Alloys 5, Manganese 5, Conductive Ceramics 8, Conductive Components 4, Phase Alloys 4, **Proto Light Alloys 9**, **Proto Radiolic Alloys 5** |
| FSD 5A SCO Increased Range G1→G5 + Mass Manager | Inara list (Datamined Wake Exceptions expected again at G5) |
| Distributor 5D Engine Focused G1→G5 + Stripped Down | Same G1→G5 path as the Dart V2 distributor (Inara list) |
| Thrusters 4D Dirty Drive G1→G3 + Stripped Down | Same G1→G3 path as the Dart V2 thrusters (Inara list) |
| Power plant 4D Overcharged G1 + Stripped Down | Same as the Dart V2 power plant (Inara list) |

*Combined with Dart V2 Tier 1 (stock of 3 Oct)* — what the Marco Polo adds to the shopping list:
- [ ] Arsenic: +5 (**14 missing** in total, Dart included).
- [ ] Improvised Components: +5 (**10 missing** in total).
- [ ] Proto Radiolic Alloys: +5 (**10 missing** in total).
- [ ] Proto Light Alloys: **9 missing** — the Dart V2 takes the whole stock of 18.
- [ ] Manganese: 1 missing (22 in stock, 23 needed for both ships).
- [ ] FSD, distributor, thrusters and power plant: add their Inara totals here (Cadmium and
      Datamined Wake Exceptions likely to grow).
- [ ] Re-check the Inara lists: all green?

*4. Felicity Farseer — Deciat*
- [ ] FSD Increased Range G1 → G5 + experimental **Mass Manager**.
- [ ] Thrusters Dirty Drive G1 → G3 + **Stripped Down**.
- [ ] Power plant Overcharged G1 + **Stripped Down**.

*5. The Dweller — Wyrd, Black Hide*
- [ ] Distributor Engine Focused G1 → G5 + **Stripped Down**.

*6. Lei Cheung — Laksak, Trader's Rest*
- [ ] Shield Reinforced G1 → G5 + **Stripped Down**.
- [ ] Sensors Lightweight G1 → G5.

*7. Validation*
- [ ] EDSY export vs plan (range, power margin).
- [ ] Test trip: a long route with neutron boosting, AFMU repair of the FSD on the way.

**Tier 2 — short unlocks (Marco Qwent)**
- [ ] Power plant Overcharged G1 → G4.

**Tier 3 — long unlocks / later**
- [ ] Power plant Overcharged G5 (engineer with G5 power plants, Engineers).
- [ ] Thrusters Dirty Drive G4 → G5: Professor Palin (Arque) or a Colonia engineer.
- [ ] Life support Lightweight G5: engineer to identify (Engineers) — saves 3.4 t.
- [ ] *(Optional)* Guardian FSD Booster (size 5, ≈ +10 ly) once unlocked at a Guardian tech
      broker.

---

## 2. FUTURE SHIPS

*Purchase milestones stay in the phase plan (§5.4); target roles in §5.5.*

### Nemesis — Corsair #1 (combat, Phase 3) — annex B2

- [ ] Buy Corsair #1 (≈79.3M CR, no rank required). Name her Nemesis (annex B2, §5.7).
- [ ] Engineer in order: (1) Bi-Weave shield, boosters, Guardian reinforcements; (2) armour and
      hull; (3) distributor; (4) thrusters; (5) Frags.
- [ ] Transition: Pacifier runs Medium RES while the Nemesis is being engineered, then the
      Nemesis takes over.

### Spectre — Courier #2 (stealth, Phase 4) — annex B3

### Cornucopia — Cutter #1 (bulk trade, Phase 5) — annex B6

### Hephaestus — Cutter #2 (mining, Phase 5) — annex B7

### Charybdis — Cutter #3 (conflict zones, Phase 5) — annex B8

### Marco Polo — moved to §1 (bought 4 Oct 2026 as a taxi, exploration configuration later)

### Diplomat — ex-Pacifier (PP logistics, Phase 6) — annex B4

### Soteria — Corsair #3 (pad-M utility, Phase 6) — annex B5

### Aegis — Corsair #4 (AX, optional, Phase 6) — annex B9

*Cards for future ships get their own checklists when their phase opens.*

---

## 3. ANNEX — SHIP BUILD SPECS (JSON)

*Moved from the old §5.7 of `In-Game Operations.md`.*

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
  "role": "Laser mining, Powerplay 2.0 (Aisling, reinforcement in systems under heavy undermining)",
  "revision": "3 Oct 2026 — rewritten from the Inara export (actual fit); previous A1 was the unengineered Phase 1 plan",
  "slot_layout": "Optional slots 7/6/4/4/3/3/2/2/1 | 2L + 2M | 4 utility",
  "principle": "PP2 reinforcement: mine and sell in the same system. Intra-system runs: no fuel scoop, cargo takes priority.",
  "hardpoints": [
    { "slot": "largehardpoint1", "module": "Beam Laser (L, Gimballed)", "purpose": "Deterrence" },
    { "slot": "largehardpoint2", "module": "Multi-Cannon (L, Gimballed)", "purpose": "Deterrence" },
    { "slot": "mediumhardpoint1", "module": "2D Mining Laser (Fixed)" },
    { "slot": "mediumhardpoint2", "module": "2D Mining Laser (Fixed)" }
  ],
  "utility_mounts": [
    "0A Shield Booster — Heavy Duty G1 + Super Capacitors",
    "0A Shield Booster — Heavy Duty G1 + Super Capacitors",
    "0A Shield Booster — Heavy Duty G1 + Super Capacitors",
    "0A Shield Booster — Heavy Duty G1 + Super Capacitors"
  ],
  "core_internals": {
    "power_plant": "6A — Overcharged G1 + Monstered (likely 'XXL' in the French client: the experimental that raises power output)",
    "thrusters": "6A — Dirty Drive G3 + Drag Drives",
    "frame_shift_drive": "5A SCO — Increased Range G5 + Mass Manager (SCO is what matters here: faster ring → station legs)",
    "life_support": "5D",
    "power_distributor": "6A — High Capacity G5 (no experimental)",
    "sensors": "5D",
    "fuel_tank": "4C (16 t)",
    "armour": "Lightweight Alloy"
  },
  "optional_internals": [
    { "slot": "size7", "module": "7E Cargo Rack (128 t)" },
    { "slot": "size6", "module": "6A Shield Generator — Reinforced G5" },
    { "slot": "size4", "module": "4A Refinery" },
    { "slot": "size4", "module": "4A Fuel Scoop", "planned": "→ 4E Cargo Rack (16 t), scoop stored" },
    { "slot": "size3", "module": "3A Collector Limpet Controller" },
    { "slot": "size3", "module": "3A Collector Limpet Controller" },
    { "slot": "size2", "module": "2A Shield Cell Bank" },
    { "slot": "size2", "module": "1A Prospector Limpet Controller" },
    { "slot": "size1", "module": "Detailed Surface Scanner — Expanded G3 (hotspot mapping; useless if rings are picked from Inara / EDTools)" }
  ],
  "cargo_capacity": "128 t, limpets included (144 t once the scoop is swapped for a 4E rack)",
  "notes": [
    "Mining lasers stay on the medium hardpoints: standard mining lasers only exist in small and medium (correction 3 Oct 2026)",
    "Lightweight engineering not worth it: cargo dominates the laden mass, gains of a few percent at most",
    "Option: boosters Heavy Duty G1 → G3 with Lei Cheung (already unlocked)",
    "Option: an experimental on the distributor (none fitted)"
  ],
  "variant_max_cargo": "If mining becomes more frequent: slot 6 as 6E Cargo (64 t) + 4A shield in the scoop slot (size 4) = 7E 128 t + 6E 64 t ≈ 192 t, quiet systems only. The engineered 6A Reinforced G5 shield is stored, not sold.",
  "end_of_life": "Sold in Phase 5 once the Hephaestus beats her performance (profit/h and merits/h).",
  "power_priorities": "All modules on priority 1 — the 6A Overcharged power plant covers the whole fit (3 Oct 2026)"
}
```

**A2 — Dart v2 (Courier, Phase 1)**

```json
{
  "ship": "Imperial Courier",
  "name": "\"Dart\" CO-01",
  "role": "Black-box snatch and flee, material recovery (HGE, Jameson, raw), Odyssey taxi + pre-landing support",
  "revision": "3 Oct 2026 — EDSY compromise build: D-rated core + Lightweight engineering, pulse lasers kept instead of beams (WEP drain), tiers in the Dart V2 plan",
  "edsy_target": { "unladen_mass_t": 60.92, "max_jump_ly": 43.6, "cargo_t": 18, "fuel_t": 4, "max_fuel_per_jump_t": 2.09 },
  "stripped_variant": "No hardpoints, utilities or hangar: 51.45 t, 51.3 ly — HGE / travel only (EDSY, 3 Oct 2026)",
  "slot_layout": "Optional slots 3/3/2/2/2/1/1/1 | 3M | 4 utility",
  "hardpoints": [
    { "slot": "mediumhardpoint1", "module": "2F Pulse Laser (Gimballed)", "engineering": "Lightweight G5 + Stripped Down", "purpose": "Skimmers, SRV" },
    { "slot": "mediumhardpoint2", "module": "2F Pulse Laser (Gimballed)", "engineering": "Lightweight G5 + Stripped Down" },
    { "slot": "mediumhardpoint3", "module": "2B Missile Rack (Dumbfire)", "engineering": "Lightweight G5 + Stripped Down (Liz Ryder)", "purpose": "Area damage against ground groups" }
  ],
  "utility_mounts": [
    "0I Chaff Launcher — Lightweight G5",
    "0I Heatsink Launcher — Lightweight G5 (silent running, lock breaking, scooping)",
    "0D Shield Booster — Resistance Augmented G5 + Super Capacitors",
    "0D Shield Booster — Resistance Augmented G5 + Super Capacitors"
  ],
  "core_internals": {
    "power_plant": "4D — Overcharged G5 + Stripped Down",
    "thrusters": "3D — Dirty Drive G5 + Drag Drives (optimal mass 78.75 t)",
    "frame_shift_drive": "3A SCO — Increased Range G5 + Deep Charge",
    "life_support": "1D — Lightweight G5",
    "power_distributor": "3D — Engine Focused G5 + Super Conduits",
    "sensors": "2D — Lightweight G5",
    "fuel_tank": "2C (4 t)",
    "armour": "Lightweight Alloy"
  },
  "optional_internals": [
    { "slot": "size3", "module": "3D Shield Generator — Reinforced G5 + Hi-Cap (131.7 MJ)" },
    { "slot": "size3", "module": "3E Cargo Rack — Extended G5 (11 t)" },
    { "slot": "size2", "module": "2E Cargo Rack — Extended G5 (5 t)" },
    { "slot": "size2", "module": "Planetary Vehicle Hangar 2G + Scarab SRV (wave scanner; Scorpion only for ground combat)" },
    { "slot": "size2", "module": "2D Fuel Scoop — Scoop-Rate Enhanced G5" },
    { "slot": "size1", "module": "1D Collector Limpet Controller — Lightweight G5" },
    { "slot": "size1", "module": "Detailed Surface Scanner — Expanded G5" },
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
    "One chaff launcher replaced with a Heatsink Launcher for the SCB (3 Oct 2026: Kill Warrant Scanner dropped — useless in CZs, as for the Charybdis)"
  ],
  "hardpoints": [
    { "slot": "largehardpoint1", "module": "3E Beam Laser (Gimballed)", "status": "Kept", "engineering_target": "Efficient or Short Range + Thermal Vent" },
    { "slot": "largehardpoint2", "module": "3E Beam Laser (Gimballed)", "status": "Kept", "engineering_target": "Efficient + Thermal Vent" },
    { "slot": "mediumhardpoint1", "module": "2E Multi-Cannon (Turret)", "status": "Kept", "engineering_target": "Overcharged + Corrosive Shell" },
    { "slot": "mediumhardpoint2", "module": "2E Multi-Cannon (Turret)", "status": "Kept", "engineering_target": "Overcharged + Incendiary Rounds" }
  ],
  "utility_mounts": ["0A Shield Booster (kept)", "0A Shield Booster (kept)", "0I Chaff Launcher (kept)", "0I Heatsink Launcher (new)"],
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
  "status": "V2 refit in progress (Phase 1, 'The Brick V2 — 90 % plan', §5.4). Cargo 758 t unchanged",
  "hardpoints": "Empty (all weapons sold)",
  "utility_mounts": [
    "0A Shield Booster — Thermal Resistant G3",
    "0A Shield Booster — Thermal Resistant G3",
    "0A Shield Booster — Thermal Resistant G3",
    "0A Shield Booster — Resistance Augmented G3",
    "(+ Super Capacitors on all 4 if Lei Cheung offers it)"
  ],
  "core_internals": {
    "power_plant": "6A stock (25.2 MW, everything on priority 1)",
    "thrusters": "7A — Dirty Drive G3 (+ Drag Drives if offered); G5 via Professor Palin later",
    "frame_shift_drive": "6B — Increased Range G5 + Deep Charge (unchanged)",
    "power_distributor": "6A — High Capacity G5 + Super Conduits (The Dweller)",
    "sensors": "4D", "fuel_tank": "5C (32 t)"
  },
  "optional_internals": [
    { "module": "5A Shield Generator — Reinforced G5 + Hi-Cap (Lei Cheung)" }
  ],
  "recommendations": [
    "Boosters to G5 with Didi Vatermann later (beyond the 90 % plan)",
    "Option: FSD 6A SCO if the targeted CGs have stations far from the star (notable time save)"
  ],
  "end_of_life": "Stored at the Medupe City museum after a full trade CG run with the Cornucopia (Phase 5)."
}
```

**A6 — Marco Polo, taxi configuration (Corsair; ex-"Hermes")**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Marco Polo",
  "configuration": "Taxi (light) — exploration configuration in annex B1",
  "role": "Long-range taxi: fly to a distant target, then transfer the needed ship there",
  "added": "4 Oct 2026 (EDSY) as \"Hermes\"; merged into Marco Polo on 5 Oct 2026",
  "shared_core": "Core internals and their engineering are shared with the exploration configuration (annex B1)",
  "edsy_target": { "unladen_mass_t": 316.4, "max_jump_ly": 67.9, "cargo_t": 0, "fuel_t": 16 },
  "hardpoints": "Empty",
  "utility_mounts": "Empty",
  "core_internals": {
    "power_plant": "4D — Overcharged G5 + Stripped Down (16.38 MW)",
    "thrusters": "4D — Dirty Drive G5 + Stripped Down (optimal mass 275.6 t)",
    "frame_shift_drive": "5A SCO — Increased Range G5 + Mass Manager (optimal mass 1894 t)",
    "life_support": "4D — Lightweight G5",
    "power_distributor": "5D — Engine Focused G5 + Stripped Down",
    "sensors": "6D — Lightweight G5",
    "fuel_tank": "4C (16 t)",
    "armour": "Lightweight Alloy"
  },
  "optional_internals": [
    { "slot": "size6", "module": "6A Fuel Scoop" },
    { "slot": "size6", "module": "6D AFMU (massless; off unless repairing — neutron boosting)" },
    { "slot": "size5", "module": "5D Shield Generator — Reinforced G5 + Stripped Down" },
    { "slot": "size1", "module": "Advanced Docking Computer" }
  ],
  "options": [
    "Supercruise Assist in a free small slot",
    "Guardian FSD Booster (size 5, ≈ +10 ly) once unlocked"
  ],
  "trade_offs": "Shield + AFMU cost 1.6 ly (69.5 → 67.9 ly); thermal resistance ≈ 0 % on the Reinforced shield — the taxi runs, it doesn't fight"
}
```

**B1 — Marco Polo, exploration configuration (Corsair)**

```json
{
  "ship": "Gutamaya Corsair",
  "name": "Marco Polo",
  "role": "Long-range exploration, exobiology, cartography",
  "replaces": "Hyperion (Asp Explorer) — retired once Marco Polo v2 beats her range",
  "revision": "5 Oct 2026 — same hull as the taxi configuration (annex A6, ex-Hermes): the core and its engineering are shared, so the core below follows A6; proposed mass savings from the taxi build listed under proposed_changes (to confirm in EDSY)",
  "kpi": "Jump range (reference value to measure in EDSY; the 81.5 ly of the initial build is to be confirmed)",
  "slot_layout": "Optional slots 6/6/6/5/5/5/4/3/2/1 | 3L + 3M | 4 utility | Core: PP7 T7 FSD5 LS4 PD7 S6 Fuel5",
  "versions": {
    "v1": "Straight away with FSD G5 and 5H Guardian booster (unlocked in Phase 2 by Hyperion)",
    "v2": "Full engineering"
  },
  "hardpoints": "Empty",
  "utility_mounts": ["0I Heatsink Launcher (Lightweight / Ammo Capacity)", "empty", "empty", "empty"],
  "core_internals": {
    "power_plant": "4D — Overcharged + Stripped Down (shared with A6; replaces the planned 3A Low Emissions — check the power budget with the exploration kit)",
    "thrusters": "4D — Dirty Drive Tuning + Stripped Down (shared with A6; was 7D — see proposed_changes)",
    "frame_shift_drive": "5A SCO — Increased Range + Mass Manager",
    "life_support": "4D Lightweight", "power_distributor": "5D Engine Focused + Stripped Down",
    "sensors": "6D Lightweight", "fuel_tank": "4C (16 t) — was 5C (32 t), see proposed_changes", "armour": "Lightweight Alloy (Heavy Duty + Deep Plating dropped, see proposed_changes)"
  },
  "proposed_changes": [
    "Thrusters 7D → 4D (shared with the taxi): several tens of tonnes saved; check the thrust margin in EDSY at the gravity of planets used for exobiology — keep a 7D in storage if high-g landings need it",
    "Fuel tank 5C (32 t) → 4C (16 t): enough with a 6A scoop, and a full tank counts in the jump calculation",
    "Armour: plain Lightweight Alloy, no Heavy Duty + Deep Plating (adds mass; hull reinforcement covers rough landings)",
    "Shield: 5D Reinforced + Stripped Down already fitted for the taxi, instead of Enhanced Low Power"
  ],
  "optional_internals": [
    { "slot": "size6", "module": "6A Fuel Scoop" },
    { "slot": "size6", "module": "6A AFMU" },
    { "slot": "size6", "module": "5A AFMU (the two AFMUs repair each other)" },
    { "slot": "size5", "module": "5H Guardian FSD Booster (from v1.5)" },
    { "slot": "size5", "module": "5D Shield Generator — Reinforced + Stripped Down (shared with A6)" },
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

## 4. ANNEX — COMPLETED REFIT PLANS (archive)

Plans kept for reference once done; open items and later tiers stay on the ship cards (§1).

### The Brick V2 — completed

**The Brick V2 — "90 %" plan (Type-9, solo, trade / Aisling Powerplay)** — added 25 Sept 2026
from Tonton Marcel's plan (written in French, translated here). Estimated time **6–10 h**.

*Why:* feeds Checkpoint 1 directly (measure the merit loops) — better credits/h and merits/h
through lower mass (hardpoints removed), engineered boosters, better pitch/roll for
arrivals/departures, and shield boosters to survive interdictions. The time spent also opens
engineers, farms materials and advances Imperial Navy and PP rank on the way.
*Why "90 %":* the ideal is G5 on every module, but some G5 engineers take long to unlock. So G5
is reserved for modules whose engineer is quick to reach (The Dweller for the distributor, Lei
Cheung for the shield); thrusters (Farseer) and boosters (Lei Cheung) stop at G3. The remaining
10 % is listed under "Beyond the 90 % plan" at the end.

| Slot | Original loadout | Brick V2 (90 % plan) |
|---|---|---|
| Hardpoints | 2× Beam Laser (M, Gimballed), 1× Multi-Cannon (M, Gimballed), 2× Multi-Cannon (S, Gimballed) | **Empty** |
| Utility | 2× Chaff, 2× stock 0A Shield Booster | **4× 0A Shield Booster**: 3× Thermal Resistant G3, 1× Resistance Augmented G3 (+ Super Capacitors if offered) |
| Power Plant | 6A stock | 6A stock (unchanged) |
| Thrusters | 6A stock | **7A Dirty Drive G3** (+ Drag Drives if offered) |
| FSD | 6B Increased Range G5 + Deep Charge | Unchanged |
| Distributor | 6A stock | **6A High Capacity G5 + Super Conduits** |
| Sensors | 4E | **4D** |
| Fuel Tank | 6C (64 t) | **5C (32 t)** |
| Shield | 5A stock | **5A Reinforced G5 + Hi-Cap** |
| Cargo | 758 t | 758 t (unchanged) |

*1. Preparation (≈ 30 min)*
- [x] Engineers checked in game, Inara crafting lists created for the 5 blueprints, material
      stock inventoried (shortfalls in step 3). Note: Lei Cheung isn't on the roster yet
      (journal `EngineerProgress`, 23 Sept) — step 4 is what brings her invitation.

*2. Outfitting (≈ 30 min)*
- [x] Station selling 7A thrusters: Kenig City (ICZ EG-O b6-2).
- [x] Sell the 2 Beam Lasers (M, Gimballed).
- [x] Sell the Multi-Cannon (M) and the 2 Multi-Cannons (S).
- [x] Sell the 2 Chaff Launchers.
- [x] Buy 2 × 0A Shield Boosters (utility slots 1 and 2).
- [x] Buy and fit the 7A thrusters.
- [x] Swap Fuel Tank 6C → 5C and Sensors 4E → 4D.
- [x] Check power: stock power plant at 25.2 MW, everything on priority 1, no overdraw.

*3. Materials (≈ 3–5 h, mostly via missions)* — rule: pick Imperial Navy and Powerplay missions
by their material rewards; trade surpluses at a Material Trader (manufactured, raw, encoded).
- Raw:
  - [x] Phosphorus ×35 · Iron ×10 · Cadmium ×4
  - [x] Chromium ×13 · Arsenic ×5 (see Paola Prospect, Kuki An)
  - [x] Manganese ×5 · Selenium ×5 · Germanium ×5 · Sulphur ×5
- Manufactured:
  - [x] Mechanical Components ×8 · Mechanical Equipment ×2 · Hybrid Capacitors ×3 · Heat
        Resistant Ceramics ×3
  - [x] Conductive Components ×20 · Conductive Ceramics ×5 · Conductive Polymers ×6
  - [x] Configurable Components ×5 · Proprietary Composites ×10 (see Olahus Hub, Kou Hua)
  - [x] High Density Composites ×5 · Compact Composites ×10
  - [x] Military Supercapacitors ×5 · Improvised Components ×5
  - [x] Heat Conduction Wiring ×10 · Heat Dispersion Plate ×5 · Focus Crystals ×10
  - [x] Worn Shield Emitters ×5 · Flawed Focus Crystals ×3
- Encoded:
  - [x] Specialised Legacy Firmware ×16 · Modified Consumer Firmware ×5
  - [x] Cracked Industrial Firmware ×5 · Security Firmware Patch ×2 · Untypical Shield Scans ×6
- Spares:
  - [x] Security Firmware Patch · Cracked Industrial Firmware (see Smoot Station, Chona)
  - [x] Heat Resistant Ceramics (see Olahus Hub, Kou Hua)
- [x] Re-check the Inara lists: all green?

*4. The Dweller — Wyrd, Black Hide (≈ 1 h 30)* — distributor
- [x] High Capacity G1 → G4 (Sulphur; SLF + Chromium; + High Density Composites; Modified
      Consumer Firmware + Selenium + Proprietary Composites).
- [x] High Capacity G5 (Cracked Industrial Firmware + Proprietary Composites + Military
      Supercapacitors).
- [x] Experimental **Super Conduits** (5 Phosphorus, 3 Heat Resistant Ceramics, 1 Security
      Firmware Patch).
- [x] Keep rolling if needed until Lei Cheung's invitation arrives, then pin the blueprint.

*5. Lei Cheung — Laksak, Trader's Rest (≈ 2 h)*
- Unlock:
  - [x] Trade at enough extra markets to pass 50, if not already there.
  - [x] Buy 200 t of Gold in Laksak (Pinto City or Hedin Hub, whichever is cheaper), one trip
        with The Brick.
  - [x] Donate the Gold to Lei Cheung (Trader's Rest).
- Shield:
  - [x] Reinforced G1 → G3 (Phosphorus; + Conductive Components; + Mechanical Components).
  - [x] Reinforced G4 (Manganese + Conductive Ceramics + Configurable Components).
  - [x] Reinforced G5 (Arsenic + Conductive Polymers + Improvised Components).
  - [x] Experimental **Hi-Cap** (5 Worn Shield Emitters, 3 Flawed Focus Crystals, 1 Conductive
        Polymers).
- Boosters:
  - [x] 3 boosters Thermal Resistant G1 → G3 (Iron; Heat Conduction Wiring + Germanium; Heat
        Conduction Wiring + Heat Dispersion Plate + Focus Crystals).
  - [x] 1 booster Resistance Augmented G1 → G3 (Phosphorus; + Conductive Components; + Focus
        Crystals).
  - [x] Check whether Lei Cheung offers **Super Capacitors**; if so, apply to all 4 boosters
        (3 Untypical Shield Scans, 5 Compact Composites, 2 Cadmium each).
  - [x] Pin the booster blueprint.

*6. Felicity Farseer — Deciat (≈ 45 min)* — thrusters
- [x] Dirty Drive G1 → G3 on the 7A thrusters (SLF; + Mechanical Equipment; SLF + Chromium +
      Mechanical Components).
- [x] Check whether Farseer offers **Drag Drives** (5 Iron, 3 Hybrid Capacitors, 1 Security
      Firmware Patch); if so, apply.
- [x] Pin the thruster blueprint.

*7. Validation (≈ 20 min)*
- [x] Export the loadout to EDSY and compare against the plan (power, boost, shield MJ).
- [x] Check power margin and priorities (cargo hatch on low priority).
- [x] Loaded test round-trip; drill the submit → boost → FSD sequence.

### Dart V2 — Tier 1 completed (5 Oct 2026)

**Dart V2 — "90 %" plan (Courier, solo, recovery / snatch and flee / taxi)** — added 3 Oct 2026,
revised the same day to the EDSY compromise build (annex A2). Same model as The Brick V2, but
split in three tiers by engineer access.

*Why:* three roles that all come down to getting in, grabbing something and getting out: a black
box from a signal source or a surface wreck, materials from an HGE, Jameson's crash site or a
raw-material site, or a ground team dropped after the defences are cleared. On a Courier, jump
range and speed both come from **low mass**: D-rated core modules and Lightweight engineering
take the ship from ~20 ly to ~43 ly while keeping the SRV hangar, three weapons, chaff, heatsink
and two boosters (stripped HGE/travel build without them: ~51 ly, EDSY, 3 Oct).
*Target (EDSY):* 60.9 t unladen, 43.6 ly, 18 t cargo, 131 MJ base shield.
*Known limits:* thrusters optimised for 78.75 t — fully laden (~83 t) the ship is noticeably
slower; 4 t tank for 2.09 t per jump = scoop every two jumps.
*Changes vs the first V2 plan (3 Oct):* pulse lasers kept instead of the beams of the first EDSY
draft (2 medium beams drain the WEP capacitor in ~6–7 s on an Engine Focused distributor);
D-rated core and Lightweight engineering everywhere; 2× 0D Resistance Augmented boosters
instead of 0A Heavy Duty; Extended cargo racks; the Supercruise Assist dropped for a
Lightweight collector limpet controller.

| Slot | Current (Inara, 3 Oct) | Target (annex A2) | Tier |
|---|---|---|---|
| Hardpoints | 2× Pulse Laser (M, Gimballed), Dumbfire (M) | Same, all **Lightweight G5 + Stripped Down** | 1 (pulse G4) / 2 (missiles) / 3 (pulse G5) |
| Utility | Point Defence, Chaff, 2× 0A Booster Heavy Duty G1 | Chaff, **Heatsink** (both Lightweight G5), **2× 0D Booster Resistance Augmented G5 + Super Capacitors** | 1 (buy, boosters G3) / 3 (G5, Lightweight) |
| Power Plant | 4A Overcharged G1 | **4D** Overcharged G5 + Stripped Down | 1 (buy) / 2 (G4) / 3 (G5) |
| Thrusters | 3A Dirty Drive G3 + Drag Drives | **3D** Dirty Drive G5 + Drag Drives | 1 (buy, G3) / 3 (G5) |
| FSD | 3A SCO Increased Range G4 + Deep Charge | 3A SCO Increased Range **G5** + Deep Charge | 1 |
| Life Support | 1D | 1D Lightweight G5 | 3 (engineer to identify) |
| Distributor | 3A High Capacity G2 | **3D Engine Focused G5 + Super Conduits** | 1 |
| Sensors | 2D | 2D Lightweight G5 | 1 |
| Fuel tank | 3C (8 t) | **2C (4 t)** | 1 (buy) |
| Armour | Lightweight Alloy | Unchanged | — |
| Size 3 | 3A Shield Reinforced G4 | **3D** Shield Reinforced G5 + Hi-Cap | 1 |
| Size 3 | 3E Cargo Rack | 3E Cargo Rack Extended G5 (11 t) | 3 (engineer to identify) |
| Size 2 | 2E Cargo Rack | 2E Cargo Rack Extended G5 (5 t) | 3 (engineer to identify) |
| Size 2 | 2A Fuel Scoop | **2D** Fuel Scoop Scoop-Rate Enhanced G5 | 1 (buy) / 3 (engineer to identify) |
| Size 2 | Planetary Vehicle Hangar 2H | Planetary Vehicle Hangar **2G** + Scarab | 1 (buy) |
| Size 1 | Detailed Surface Scanner Expanded G3 | DSS Expanded G5 | 1 |
| Size 1 | 2× Collector Limpet Controller 1A | **1× 1D** Collector, Lightweight G5 | 1 (buy) / 3 (Lightweight) |
| Size 1 | — | 1E Cargo Rack (2 t) | 1 (buy) |

**Tier 1 — reachable now (Farseer, The Dweller, Lei Cheung; ≈ 4–6 h)**

*1. Preparation (≈ 20 min)*
- [x] EDSY: Tier 1 fit (D-rated core, G3/G4 where G5 is out of reach) — check range, speed and
      that the power plant still covers everything with the stock 4D.
- [x] Inara crafting lists for the Tier 1 blueprints, material stock inventoried.

*2. Outfitting (≈ 30 min)* — store the engineered A-rated modules rather than sell them.
- [x] Buy and fit: 4D power plant, 3D thrusters, 3D distributor, 3D shield generator,
      2C fuel tank, 2D fuel scoop, Planetary Vehicle Hangar 2G, 1D collector, 1E cargo rack.
      → Fitted instead: **3A fuel scoop in the size-3 slot** (deliberate, 5 Oct — scoops are
      massless, so it costs 4 t of cargo, not range; much faster refuelling on a 4 t tank).
- [x] Sell the Point Defence and the second collector; buy a Heatsink Launcher.
- [x] Two 0D shield boosters to replace the 0A Heavy Duty pair (or keep the 0A pair until the
      0D ones are engineered — compare in EDSY).
- [x] Swap the SRV for a Scarab.
- [x] Power priorities and fire groups (heatsink reachable from the flight group).

*3. Materials — shopping list (Inara crafting lists "Dart V2 Tier 1", 3 Oct 2026)*
Shortfalls are the totals across all eight lists — Inara counts each list against the whole
stock, so it under-reports shared materials (Arsenic, Cadmium, Proto Radiolic Alloys).
Tier 1 reference fit (EDSY, 3 Oct): **68.7 t unladen, 38.8 ly**, pulse lasers Lightweight G4.

| Material | Needed | In stock | Missing | Blocks |
|---|---|---|---|---|
| Arsenic (raw) | 10 | 1 | **9** | FSD G5 (Farseer), shield G5 (Lei Cheung) |
| Cadmium (raw) | 9 | 0 | **9** | Boosters G3 (Lei Cheung), distributor G5 (The Dweller) |
| Proto Radiolic Alloys (manufactured) | 10 | 5 | **5** | DSS G5, sensors G5 (Lei Cheung) |
| Improvised Components (manufactured) | 5 | 0 | **5** | Shield G5 (Lei Cheung) |
| Datamined Wake Exceptions (encoded) | 5 | 0 | **5** | FSD G5 (Farseer) |

*Raw — Raw Material Trader (refinery / extraction economies) or SRV prospecting (Scarab)*
- [x] Arsenic ×9 (Orrere planned, or trade surplus raw: Iron 198, Carbon 276, Sulphur 202).
- [x] Cadmium ×9.

*Manufactured — HGE runs with the Dart, or Manufactured Material Trader (industrial economies)*
- [x] Proto Radiolic Alloys ×5.
- [x] Improvised Components ×5.
- Trade-in surplus if needed: Salvaged Alloys 81, Phase Alloys 86, Worn Shield Emitters 84,
  Galvanising Alloys 66.

*Encoded — Encoded Material Trader (high-tech / military economies)*
- [x] Datamined Wake Exceptions ×5 — the Dart has no wake scanner, so trade for them (surplus:
      Atypical Disrupted Wake Echoes 42).

*Watch*
- [x] Proto Light Alloys: exactly 18 needed for 18 in stock (DSS, power plant, pulse lasers,
      sensors) — don't spend any elsewhere before Tier 1 is done.
- [x] Re-check the Inara lists: all green?

*4. Felicity Farseer — Deciat* — FSD
- [x] Increased Range G4 → G5, keep Deep Charge.
- [x] Thrusters (new 3D): Dirty Drive G1 → G3 + **Drag Drives**.

*5. The Dweller — Wyrd, Black Hide* — distributor and lasers
- [x] Distributor (new 3D): Engine Focused G1 → G5 + **Super Conduits** (more recharge on all
      three capacitors, less capacity — chosen 3 Oct for chained engagements).
- [x] 2 pulse lasers: Lightweight G1 → G4 (The Dweller's maximum for pulse lasers).

*6. Lei Cheung — Laksak, Trader's Rest* — shield, boosters, sensors
- [x] Shield (new 3D): Reinforced G1 → G5 + **Hi-Cap**.
- [x] 2 boosters: Resistance Augmented G1 → G3 + **Super Capacitors**.
- [x] Sensors: Lightweight G1 → G5.
- [ ] DSS: Expanded G3 → G5 — not done, moved to the Dart card's later plan.

*7. Validation (≈ 30 min)*
- [x] EDSY export vs plan: range, boost, power margin, laden vs unladen speed.
- [x] Test: one HGE (manual scoop or limpet), one surface site with the Scarab, one silent-
      running escape with the heatsink, one Odyssey taxi run (doctrine, annex A2).

*Result (EDSY, 5 Oct 2026):* **68.76 t unladen, 38.8 ly**, 10 t cargo — on the Tier 1 reference.
