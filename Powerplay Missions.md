# POWERPLAY MISSIONS — CMDR ONCLEMARCEL
## Aisling Duval playbook: weekly assignments, merit loops, mission type cards

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Satellite of `In-Game Operations.md` §5 (Roadmap): the main line there holds phases and
> checkpoints; this file holds the Powerplay work. Created 25 September 2026 when §5 was split
> into satellite files (content moved, not rewritten).
> **How it grows:** cards are refined in place, never appended to as a log. A new lesson edits a
> checkbox or a pitfall line; a repeat run updates the card's **Stats** line. What *happened* in
> a session (raw material for the story) still goes to `In-Game Operations.md` §4.
> **References:** a bare `§N` points to `In-Game Operations.md`; "annex A1…B9" and ship names
> point to `Shipyard.md`; "Engineers" = `Engineers & Materials.md`.

---

## 0. STATUS

| | |
|---|---|
| Power | Aisling Duval — pledged |
| Rank | **7** (`Powerplay`, 29 Sept 2026 18:36 UTC) |
| Merits | **34,892** (`PowerplayMerits`, 29 Sept 2026 19:20 UTC) |
| Target | Rank 34 (≈247,000 merits) — unlocks Prismatic Shields (Phase 4, §5.4) |

---

## 1. THIS WEEK — tick of Thursday 24 September 2026

*Reset at every Thursday tick: delete last week's rows, after moving each result into its card's
Stats line (§4).*

| # | Assignment | Card | System(s) | Status | Merits |
|---|---|---|---|---|---|
| 1 | *to fill from Tonton Marcel's notes* | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## 2. WEEKLY LOOP (generic)

- [ ] After the Thursday tick, read the 5 assignments in the Powerplay screen and map each one
      to a card (§4). An assignment with no matching card gets a new card.
- [ ] Weekly assignments are **optional bonus merits**: only the very first set after pledging
      (18 Sept, §4) gated rank progression. If one can't be done this week, skip it and put the
      time into a merit loop (§3) instead; everything counts toward rank.
- [ ] Group assignments by region and by hull; do the ship swaps at Medupe City in one go (all
      hulls are stored there, §2).
- [ ] Before picking a hull, check the pad size at every hand-in station (Clipper = large pad —
      see the Rescue card).
- [ ] If a bounty assignment is on the list and McQuinn is still locked, **don't redeem the
      vouchers** (see the Bounty card and Engineers).
- [ ] After each assignment, note the merits earned (round-number jumps in `PowerplayMerits`) and
      the time spent, then update the card's Stats line.
- [ ] Anything learned the hard way goes into the card's Pitfalls, not into a new paragraph.

---

## 3. MERIT LOOPS (between assignments)

*Moved from Phase 1 (§5.4). "Measure merits/h for each loop" is Checkpoint 1.*

**Powerplay: ≈212,000 merits remaining to rank 34** (≈247,000 − 34,892)
- [ ] PP trade with The Brick: high-margin sales in the targeted Aisling systems.
  - **Rules** (community guides, matched by our 29 Sept journal): sale must make **≥ 40% profit**.
    - *Reinforcement system* (any Aisling-controlled system, incl. Exploited): goods can come
      from anywhere. ✔ paid at Col 285 Sector YA-K b23-10.
    - *Acquisition system* (Unoccupied): goods must be **bought in an Aisling Fortified system
      within 20 ly or a Stronghold within 30 ly**. Goods from an *Exploited* system don't count.
      ✘ Our medicines (bought at YA-K b23-10, Exploited) paid **0 merits** at ZA-K b23-1, five
      sales in a row.
  - **Sell the whole hold in one sale.** Merits are worked out per sale and small sales round
    to zero: cobalt lots of 1, 2 and 1 t gave nothing; the 16 t lot gave 9.
  - **Formula — not settled.** A community formula (merits ≈ 0.375 × √profit) predicts ~90
    merits for our cobalt lot; we got 9, so it doesn't fit (older data, or nerfed since). Our
    own four data points fit **merits ≈ 2.3 × 10⁻⁹ × (profit of the sale)²** — cobalt 16 t,
    62,896 CR → 9; uraninite 20 t, 46,400 CR → 5; 2 t, 7,862 CR → 0. Two non-zero points only,
    so a simpler "tons × margin" rule fits almost as well; a single full-hold Type-9 sale will
    tell the two apart (squared: thousands of merits; linear: ~20× the Asp result).
  - **Route finder:** `python tools/pp_trade_routes.py` (Spansh data; defaults to the current
    system and ship cargo from the journal; `--radius`, `--max-age`, `--mode acquire`,
    `--cargo`, `--pad M`). Lists merit legs ≥40% plus the best return leg.
  - **The 40% gate is strict**: palladium, Type-9, 29 Sept (ZA-K 47,138 → YA-K 59,250, +25.7%),
    668 t sold for 8.1M CR profit → **0 merits**. Check `(sell − buy) / buy ≥ 0.40` before
    loading.
  - Asp (20 t) measurement, 29 Sept: 14 merits for ~30 min → **~30 merits/h**. Not worth it in
    the Asp; retry with the Type-9 (moved to YA-K b23-10 the same evening).
- [ ] PP mining with Astroforge: mine and sell in the same reinforcement system.
- [ ] Light PP combat with Pacifier: Low RES in the reinforcement system. **Do not redeem the
      bounty vouchers this time** — carry them to Wolf 397 (Trophy Camp) once past 100k CR
      instead, for McQuinn's unlock donation (Engineers). **Expect this to be slow toward
      the 100k figure**: Low RES was chosen here for safety (Novice rank, survival-first per §2),
      not bounty density — "easier targets, lower payouts," and local security often kills wanted
      NPCs before you reach them. Treat the first session as a real data point (matches
      Checkpoint 1's "measure it" approach) rather than assuming a quick errand. If it's too slow
      and the Pacifier's shield/boosters are holding up, step up to a **regular RES** (not
      Hazardous — no security cover there, and the Pacifier isn't G3-engineered yet) for faster
      bounty income.

---

## 4. MISSION TYPE CARDS

*Seeded from the five gating missions of 18 September 2026 (`In-Game Operations.md` §4 keeps the
day's log and story material). One card per mission type; always generic, never ticked for a
specific week — the week's progress lives in §1.*

### 4.1 Rare material → unexploited system

- **Recognise it:** deliver a rare commodity to a system no Power holds (unoccupied).
- **Ship:** any hull with enough cargo (18 Sept: Asp).
- **Run:**
  - [ ] Find the rare commodity's source market.
  - [ ] Buy the required quantity.
  - [ ] Fly to the target system and deliver.
- **Pitfalls:** none met so far.
- **Stats:** 1 run · +3,600 merits · last: 18 Sept, **Karsuki Ti** (West Market: 18× Karsuki
  Locusts @ 915 CR, 10:37) → **HIP 7311** (Fan Base, unoccupied, 10:49) — ~12 min.

### 4.2 Ship scans, reinforcement

- **Recognise it:** scan in an Aisling system that needs reinforcing (nav beacon scan).
- **Ship:** combat hull (18 Sept: Pacifier).
- **Run:**
  - [ ] Check the power distribution priorities before going in (open task, §5.1).
  - [ ] Drop at the nav beacon, do the scan, leave.
- **Pitfalls:** pirates thick around the beacon at **HIP 3254** (Aisling Stronghold, heavy
  undermining). Second visit that day: shields dropped, hull down to 79.9%, lost power mid-fight
  — escaped on the Clipper's speed.
- **Stats:** 1 run · +2,000 merits · last: 18 Sept, HIP 3254 — scan done 11:18 (visit 11:12–11:24).

### 4.3 Aisling Programme → undermine an exploited system

- **Recognise it:** carry Aisling promotional materials to a system another Power exploits.
- **Ship:** any hull with a small cargo hold (18 Sept: Pacifier).
- **Run:**
  - [ ] Collect `aislingpromotionalmaterials` at Cubeo (15× on 18 Sept).
  - [ ] Fly to the target system and deliver.
- **Pitfalls:** none met so far — "easy."
- **Stats:** 1 run · +3,600 merits · last: 18 Sept, **Vargerson** (Browncoat Refuge; exploited by
  A. Lavigny-Duval + Aisling) — collected 12:03, delivered 12:21, ~18 min. Route out via Ehlanda /
  Gliese 54.3 / Tehuenef, back via HIP 6616 / Kaukamal / Hernovacle.

### 4.4 Rescue — wreckage / black boxes

*How it works (moved verbatim from the 18 Sept log, §4):*

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

- **Ship:** a medium-pad hull with collector limpets (18 Sept: Asp — the Clipper couldn't dock
  at Hansteen Depot).
- **Run:**
  - [ ] Collector limpet controller fitted, limpets bought.
  - [ ] Check the hand-in station's pad size before choosing the hull.
  - [ ] FSS for Power-ship wreckage signal sources.
  - [ ] Collect; watch for authorities arriving when black boxes are aboard.
  - [ ] Hand in to the Imperial contact **in the same system**.
- **Stats:** 1 assignment (first hand-in + three more runs) · +2,800 merits · last: 18 Sept,
  **Lambda Hydri** (Hansteen Depot, pop. 2,490, exploited) — Clipper first pass 18:01, Asp from
  18:38.

### 4.5 Bounty hunting, reinforced system

- **Recognise it:** kill wanted ships in an Aisling system being reinforced.
- **Ship:** combat hull (18 Sept: Pacifier).
- **Run:**
  - [ ] Go to the nav beacon; scan ships to find the wanted pilots.
  - [ ] Kill and collect the vouchers.
  - [ ] **While McQuinn is still locked:** keep the vouchers unclaimed for her unlock donation
        (Engineers) — don't redeem them at a station.
- **Pitfalls:** none met so far — "easier than expected."
- **Stats:** 1 run · +3,200 merits · last: 18 Sept, **Chinovane** (pop. 2,133, exploited) — nav
  beacon, 19:42–19:48, ~6 min.

### 4.6 Holoscreens, rival system

- **Recognise it:** hack holoscreens at a station in a system **another Power controls** (the
  screens show that Power's adverts).
- **Ship:** any hull with a **recon limpet controller** and recon limpets.
- **Run:**
  - [ ] Pick a system controlled by another Power, next to Aisling's border.
  - [ ] Drop at the station, target a holoscreen, launch a recon limpet (+merits per hack).
  - [ ] Back to supercruise, drop again: the screens reset, hack them again. Repeat until the
        assignment pays out.
- **Pitfalls:** none met — "easy." Every screen can be selected in these systems.
- **Stats:** 1 assignment · +4,800 merits (+ 14 × 86 per hack) · last: 25 Sept, **Shui Wei
  Sector VT-R b4-5** (Lavigny-Duval, Exploited), Lounge Reach — 06:32–06:52, ~20 min.

### 4.7 Holoscreens, reinforcement

- **Recognise it:** hack holoscreens in an **Aisling system** that needs reinforcing.
- **Ship:** any hull with a **recon limpet controller** and recon limpets.
- **What to look for (the tricky part):** in your own system you can only hack a screen that
  **another Power has already hijacked** — a screen showing Aisling cannot even be selected.
  Hijacked screens are only found where rivals are active:
  - [ ] An Aisling system **on the border**, whose `Powers` list (journal `FSDJump`, or the
        system panel) names **several other Powers**. Amaneque had four.
  - [ ] Marked as a **priority system for reinforcement** in the Powerplay screen (active
        undermining).
  - [ ] High undermining alone is **not** enough: HIP 5700 (Stronghold, 20,526 undermining) and
        Wababa list only Aisling — no screen could be selected there.
- **Run:**
  - [ ] Drop at the station, check every screen; the selectable ones are the hijacked ones.
  - [ ] Recon limpet on it (+merits per hack).
  - [ ] Back to supercruise, drop again: the screen shows the rival's adverts again — one screen
        is enough for the whole assignment.
- **Pitfalls:**
  - A day lost searching Aisling-only systems (25 Sept) before finding the rule above.
  - Merits per hack dropped from 100 (25 Sept) to 65 (26 Sept) — reason unconfirmed (maybe the
    system's reinforcement going up).
- **Stats:** 1 assignment · +2,400 merits (+ 5 × 100 and 7 × 65 per hack) · last: 25–26 Sept,
  **Amaneque** (Aisling, Exploited; Lavigny-Duval, Mahon, Torval also present), Gilliland Colony
  (outpost) — completed 26 Sept 09:18.

### 4.8 Power classified data (settlement data ports)

*Not completed yet — this card holds what is known so far.*

- **Recognise it:** download **Power classified data** at settlement data ports and hand it in.
- **Ship / suit:** any ship that can land near the settlement; on-foot suit and a tool to open
  the data ports.
- **What to look for (the tricky part):** the assignment says **download in a reinforcement
  system and deliver in the same system** (an Aisling system being reinforced).
  - [ ] Settlement type does **not** seem to decide it: players report classified data drops
        **at random from any type of settlement data port**, with a low chance (Steam thread,
        not confirmed by Frontier). Our own results agree: tourism, industrial, agricultural and
        military settlements all gave only the common data types (see Pitfalls).
  - [ ] So it is a **volume game**: open as many data ports as possible in one reinforcement
        system, and hand in the common data as you go (it pays merits too, see Stats).
  - [ ] Faster ways to open many ports: "restore power" / "power up" missions at abandoned
        settlements (one player got classified data this way) — **untested here**; and
        settlements in anarchy systems — ✔ **worked once** (29 Sept, see Stats).
  - [ ] Pair it with an on-foot massacre mission against the same settlement's faction: you
        clear the guards anyway, then open the ports in peace (29 Sept, Sarana).
- **Run:**
  - [ ] Land, find the data ports, download.
  - [ ] Check the backpack for `powerclassifieddata` before leaving.
  - [ ] Hand in at the Power contact **in the same system**.
- **Pitfalls:**
  - 25 Sept — settlements in Aisling-controlled systems gave only the other Power data types
    (association, industrial, political); never classified:
    - Sasaki Tourism Lodge (Wababa, Stronghold, tourism)
    - Sar Metallurgic Complex (Aisoci, Fortified)
    - Almeida-Vega Agricultural (ICZ ZZ-P b5-4, Exploited)
  - 26 Sept 09:23 — `dockingMinorTresspass` fine (400 CR) on touchdown at Aoki Astrophysics
    Expedition: land on the pad or outside the settlement's no-landing zone.
  - 26 Sept — Aoki Astrophysics Expedition and Dashkevych's Astrophysics (Amaneque, high-tech):
    the journal shows no data downloaded at either.
  - 27 Sept — **Gabraceni** (Stronghold, heavily undermined): about 20 downloads, none
    classified (and no research data either). Settlements: Sklyarenko's Edge (tourism,
    3 passes), Hammond Military Site (military), Pidgaiko's Joy (tourism).
- **Stats:** 1 classified data handed in · **+187 merits** · last: 29 Sept, **Sarana**
  (Aisling Stronghold, anarchy) — Sharma Analytics Installation (Sarana 6 a, high-tech), handed
  in at Blaha Dock. Side income from the common data: 234 merits per item handed in (27 Sept,
  Gabraceni). **7 common data items still in the ship locker** (29 Sept) — hand them in.
