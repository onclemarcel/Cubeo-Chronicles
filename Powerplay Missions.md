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
| Rank | **23** (`PowerplayRank`, 26 Oct 2026 10:55 UTC — 21 and 22 on 25 Oct) |
| Merits | **164,825** (`Powerplay` at login, 27 Oct 2026 17:59 UTC) |
| Target | Rank 34 (≈247,000 merits) — unlocks Prismatic Shields (Phase 4, §5.4) |

---

## 1. THIS WEEK — tick of Thursday 22 October 2026

*Reset at every Thursday tick: delete last week's rows, after moving each result into its card's
Stats line (§4).* Last week's rows (15 Oct tick, 4 of 5) are already in the cards' Stats.

*Deduced from the journal (27 Oct): each payout matched to the events just before it.* **5 of 5
done** in two sessions (25 Oct 20:56–23:16, 26 Oct 07:18–11:31 UTC) — **+24,000 merits**, Rank
20 → 23.

| # | Assignment | Card | System(s) | Status | Merits |
|---|---|---|---|---|---|
| 1 | Holoscreens, **unoccupied** system | 4.6 | ICZ OX-U c2-15 (Bowen Beacon) | ✔ 25 Oct 21:41 — 12 hacks | 4,800 (+ 12 × 126) |
| 2 | Rescue — Power wreckage | 4.4 | Col 285 Sector WO-O b20-1 → Spitzer Gateway | ✔ 25 Oct 21:58 | 2,800 |
| 3 | Power goods stolen on foot | 4.12 | Heath's Quarry (Shui Wei Sector VT-R b4-4) → Smoot Station, Chona | ✔ 25 Oct 22:59 | 4,800 |
| 4 | **Power malware uploads** (new) | 4.14 | Bessel Dock, Munshin → Heath's Quarry | ✔ 26 Oct 10:55 | 5,200 |
| 5 | Holoscreens, reinforcement | 4.7 | Amaneque (Gilliland Colony) | ✔ 26 Oct 11:31 — 8 hacks | 2,400 |

The journal again wrote the 2,800 twice (21:58:49 and :50); the next total shows one was real.

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

**Powerplay: ≈112,500 merits remaining to rank 34** (≈247,000 − 134,534, 21 Oct)

**Comparison, rough (assignment bonuses excluded; journal 1–21 Oct):**

| Loop | Ship | Merits/h | Basis |
|---|---|---|---|
| PP trade (pyrophyllite) | The Brick | **~7,600** | 30 Sept, measured (below) |
| Megaship datalink scans | Dart | **~3,100**, **~4,300** at a steady pace | 8 paid scans × 468 in ~72 min; steady stretch 6 scans in 39 min (~6.5 min per megaship). The 2 unpaid scans in Cubeo cost ~10 min. Card 4.9 |
| Power data on foot | Dart + suit | **~2,100**, **~3,300** without lost time | 10 items, 5,040 merits, 14:58 undock → 17:21 hand-in (143 min). ~50 min of it gave nothing (first landings, two re-logs). Card 4.11 |
| Holoscreens (side income) | any + recon limpets | ~126 per hack, ~1 min each | 3 hacks, 1 Oct. Cards 4.6/4.7 |
| PP mining, Platinum / LTD hotspot | Astroforge (110 t) | **~7,700–11,500 per hold** (estimate) — hours per hold not yet measured | `tools/pp_mining_routes.py`, 21 Oct: HIP 5700 Platinum 3× (sell Kaiser's Journey, price 240 days old — check in game); Reddis LTD (Olahus Port, fresh price, demand 2,268 t). Formula exact, 1 Oct |
| Rival Power kills | Nemesis | **~5,000–6,000** while fighting | 11 kills × ≈230 in two 15-min visits, Shui Wei Sector VT-R b4-5, 17 Oct. Murders pile up in that system. Card 4.13 |
| Holoscreens, Aisling system with rivals | any + recon limpets | **~3,800** | Khepri, 7 × 126 in 13 min, no fines, 13 Oct. Card 4.7 |
| Power data on foot, re-landing loop | Dart + suit | **~2,800** | 9 items × 540, 21 Oct. Card 4.11 |
| Massacre stacks | Nemesis | ~1,700 (+7 per scan) — but ≈50M CR/h and Navy progress | Osane, 16–17 Oct |

**Route check, 21 Oct** (`pp_trade_routes.py --ref Cubeo --radius 25 --cargo 758 --mode reinforce`,
markets ≤ 3 days old): **cobalt** is the loop — huge stocks, so buying barely moves the price.
- Bainbridge Orbital (Lambda-1 Tucanae, 2,702) → Borrelly Hub (Purungurawn, 15,570), **1.4 ly**,
  ~1,393 merits per hold; stock 407,651 t.
- Kristina Queen (ICZ EG-O b6-2, 2,787) → Dayuan Vista (Tucanae Sector YZ-X b1-1, 16,008),
  5.5 ly, ~1,431 merits; stock 4.3M t.
- ✔ **Pyrophyllite, Temple Works (HIP 5623) → Spitzer Gateway (Col 285 Sector WO-O b20-1),
  7.8 ly — the best loop measured so far.** Flown 21 Oct, 3 holds of 758 t (14:57–15:24): bought
  10,394 → 10,384 → 10,375 CR, sold ~28,435 → **1,642 / 1,643 / 1,644 merits** and 13.7M CR
  profit per hold. **One round trip ≈ 11.5 min → ~8,600 merits/h and ~71M CR/h.** Spansh
  showed only 2,321 t of stock, yet the price didn't rise after 2,274 t bought — the stock seems
  to regenerate between trips (Tonton Marcel's observation). Formula exact on all three sales.
  Keep watching the buy price: if it climbs above ~13,000, the margin over the 40 % line shrinks.
- Alternate the two cobalt buyers so neither sale price sinks.

The Brick's trade loop is still the best merits/h by about 2×. The Dart loops are worth running
when an assignment pays for the same work, since the assignment bonus is added on top.

- [x] PP trade with The Brick: high-margin sales in the targeted Aisling systems — **measured
      30 Sept: ~7,600 merits/h, ~64M CR/h** (pyrophyllite loop, benchmark in
      `In-Game Operations.md` Checkpoint 1).
  - **Rules** (community guides, matched by our 29 Sept journal): sale must make **≥ 40% profit**.
    - *Reinforcement system* (any Aisling-controlled system, incl. Exploited): goods can come
      from anywhere. ✔ paid at Col 285 Sector YA-K b23-10.
    - *Acquisition system* (Unoccupied): goods must be **bought in an Aisling Fortified system
      within 20 ly or a Stronghold within 30 ly**. Goods from an *Exploited* system don't count.
      ✘ Our medicines (bought at YA-K b23-10, Exploited) paid **0 merits** at ZA-K b23-1, five
      sales in a row.
  - **Sell the whole hold in one sale** (answered by split test C): merits are linear in
    tonnage and rounded down per sale, so small lots only lose merits. **Demand must cover
    the load** — check it in-game before buying (the route finder filters on Spansh demand).
  - **Formula — not settled; merits follow the credit profit of each sale.** The community
    formula (0.375 × √profit, Inara guide) is ~10× too high today (trade nerf). Journal data:

    | Date | Sale (one transaction) | Where it was sold | Profit | Merits |
    |---|---|---|---|---|
    | 29 Sept | cobalt 16 t | YA-K b23-10 (**Exploited**) | 62,896 | 9 |
    | 29 Sept | uraninite 20 t | YA-K b23-10 (**Exploited**) | 46,400 | 5 |
    | 30 Sept | water 758 t, +2,278% | Fefra's Legacy (**acquisition**) | 466,170 | 22 |
    | 30 Sept | catalysers 10 t, +57% | Fefra's Legacy (acquisition) | 12,920 | 0 |
    | 30 Sept | silver 10 t, +42% | The Knight's Watch, HIP 3254 (**Stronghold**) | 146,250 | 0 |
    | 30 Sept | agronomic treatment 758 t, +45% | Chelomey Orbital, Cubeo (**Stronghold**) | 877,764 | **0** |
    | 30 Sept | **A**: silver 758 t, +41.7% | Flettner Ring, Primi (**Fortified**) | 10,626,402 | **67** |
    | 30 Sept | **B**: lepidolite 758 t, +232% | Ackerman's Folly, Luphis (**Exploited**) | 626,866 | **80** |
    | 30 Sept | **C** (split test): silver 1 / 5 / 10 / 25 / 50 / 667 t, +41.7% | Flettner Ring, Primi (Fortified) — **demand only 64 t** | 14,019 CR/t | 0 / 0 / 0 / **2** / **4** / **59** (seen in the login total) |
    | 30 Sept | **D**: cryolite 758 t, +189% | Kurosawa Gateway, Tucanae Sector UT-Z b5 (Fortified) | 14,148,070 | **1,740** |
    | 30 Sept | cryolite 758 t, +178% (bought 10,217) | Kurosawa Gateway (Fortified) | 13,799,390 | **1,669** |
    | 30 Sept | silver 758 t, +45%, demand 4,023 t | Kurosawa Gateway (Fortified) | 11,537,518 | **209** |
    | 30 Sept | cryolite 758 t, +149% (bought 11,345) | Kurosawa Gateway (Fortified) | 12,817,780 | **1,462** |

    **✔ Formula — exact on 13 of 14 sales (the 14th, acquisition, is 1 off):**

    > **merits = floor( tons × (sell − 1.4 × buy) × 156 / 1,000,000 )**
    > into Exploited or Fortified systems; ~**48** instead of 156 into an acquisition system.

    **Only the profit above the 40% line counts.** Silver at +45% leaves ~1,770 CR/t above
    the line (209 merits for 11.5M CR profit); cryolite at +190% leaves ~14,700 CR/t
    (1,740 merits for 14.1M CR). It's neither the material nor demand: the old
    "low-demand penalty" was just silver's thin margin (demand 4,023 t at Kurosawa paid
    the same low rate). Rounded down per sale → **sell the whole hold at once**.
    **Buying pushes the price up**: cryolite went 9,859 → 10,217 → 11,345 at Gottlob Frege
    over three runs, and the merits fell 1,740 → 1,669 → 1,462. Rotate goods.
    **Best trade:** high margin (well above 40%) × high price per tonne × full hold.
    Route finder uses the formula (`tools/pp_trade_routes.py`).

    ✘ **Credit profit does not drive merits**: B made 17× less profit than A and earned more.
    ✘ Both models tried so far (√profit, profit-linear) and "tons × margin" are dead.
    A full Type-9 hold sold in one go earns only **~70–80 merits** whatever the profit —
    consistent with player reports of **diminishing returns per sale** (merits per tonne drop
    as the lot grows; some split sales down to 1 t). Next test: split a hold into rising lots.
  - **Demand ≥ 4× the load**, or the price crashes: Luphis showed 6,046 CR on Spansh, paid
    1,184 CR for 758 t. The route finder flags such legs `LOW DEMAND`.
  - **Strongholds paid nothing** for 40%+ trade, twice (incl. 878k CR profit). **Fortified
    pays** (A), Exploited pays (B, 29 Sept), acquisition pays (water).
  - **No fleet carriers** (buy or sell): owner-set prices, and carrier goods reportedly
    earn no merits. The route finder now skips them.
  - **Route finder:** `python tools/pp_trade_routes.py` (Spansh data; defaults to the current
    system and ship cargo from the journal; `--radius`, `--max-age`, `--mode reinforce|acquire`,
    `--cargo`, `--pad M`, `--hubs LY` for acquisition around nearby Fortified/Stronghold hubs,
    `--skip-states` default `Stronghold`, fleet carriers skipped). Ranks merit legs ≥40% by
    profit, flags `LOW DEMAND`, no merit estimate (formula unknown); plus the best return leg.
  - **The 40% gate is strict**: palladium, Type-9, 29 Sept (ZA-K 47,138 → YA-K 59,250, +25.7%),
    668 t sold for 8.1M CR profit → **0 merits**. Check `(sell − buy) / buy ≥ 0.40` before
    loading.
  - Asp (20 t) measurement, 29 Sept: 14 merits for ~30 min → **~30 merits/h**. Not worth it in
    the Asp; retry with the Type-9 (moved to YA-K b23-10 the same evening).
- [ ] PP mining with Astroforge: mine and sell in the same reinforcement system.
  - **✔ Formula — exact on all 10 mined-goods sales (1 Oct, journal):**

    > **merits = floor( sale value / 2,560 )** — about **391 merits per 1M CR** of sale

    | Sale | Where | Value (CR) | Merits |
    |---|---|---|---|
    | silver 17 t | Kaiser's Journey, HIP 5700 (**Stronghold**) | 832,235 | 325 |
    | gold 2 t | Kaiser's Journey (Stronghold) | 111,532 | 43 |
    | coltan 5 t / praseodymium 3 t | Kaiser's Journey (Stronghold) | 19,610 / 15,999 | 7 / 6 |
    | tritium 5 t | Noel Station, ICZ DG-O b6-3 (**Exploited**) | 269,460 | 105 |
    | H₂O₂ 5 t / methane clathrate 9 t / LiOH 2 t | Noel Station (Exploited) | 16,060 / 15,102 / 11,522 | 6 / 5 / 4 |
    | water 3 t, liquid oxygen 1 t, lepidolite 2 t | both | < 2,560 each | 0 |

    **Strongholds pay for mining**, unlike trade, at the same rate as Exploited. Mined goods have
    no purchase price, so the whole sale counts: 2.5× the trade rate (156 per 1M CR of profit
    above the 40% line). Rounded down per sale, so sell each commodity in one go.
    **A full hold of Platinum (~110 t × ~267k) ≈ 29M CR ≈ 11,000 merits; LTD (~198k) ≈ 8,500.**
  - **Spot finder:** `python tools/pp_mining_routes.py --cargo 110` (Spansh: ring hotspots,
    reserves, Power state, best in-system buyer, laser-minable minerals only, merits per hold
    from the formula above). Set `--cargo` to the hold minus the limpets.
  - **Best spot: HIP 5700** (Stronghold, 13 ly from Cubeo). Platinum **3× hotspot** in the
    A 2 A Ring (2,073 ls), sold at Kaiser's Journey (2,038 ls, next to the ring). Spansh's
    Platinum price there (267k, demand 551 t) is 220 days old: check it in game. Backups: ICZ
    DG-O b6-3 (Pristine icy ring, LTD hotspot, Noel Station next to it); Daibo (Platinum 4×,
    43.6 ly, but only 124 t demand).
  - **Fit:** mining lasers only exist in sizes 1 and 2 (no large ones). Upgrade the 2× 2D to
    **2× 2B**, the best available. The large hardpoints keep their weapons. Limpets take part of
    the 128 t.

**PP mining run — how to hit the hotspot** (lesson of 1 Oct):
- [ ] Before the session: buy limpets, then check the station's real price and demand for the
      target mineral.
- [ ] **Map the ring with the Detailed Surface Scanner** (probes on the ring). Hotspots only
      appear on the ring once it's mapped.
- [ ] Target the hotspot marker and drop **into** it. Not into a Resource Extraction Site: on
      1 Oct the drop in HIP 5700 was into a Hazardous RES, and the ring at Noel Station was never
      mapped. Result: 61 asteroids prospected, **no Platinum, no LTD** (silver, gold, osmium,
      tritium…).
- [ ] Prospect; only mine asteroids with a good share of the target mineral (e.g. Platinum
      ≥ 20–25 %). Skip the rest.
- [ ] Sell each commodity in one go at the in-system station.
- **Stats:** 1 session · 1 Oct, without hotspots: HIP 5700 19:08–19:34 (29 t, **381 merits**,
  ~880/h) and ICZ DG-O b6-3 19:52–20:14 (25 t, **120 merits**). Real hotspot rate still to
  measure.
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
- **Shortcut:** it has been **Karsuki Locusts every time** (18× at West Market, Karsuki Ti, 915 CR)
  — go straight there. HIP 7311 (Fan Base) is one jump away and sells them at a small profit.
- **Stats:** 3 runs · +3,600 merits each · last: 12 Oct, **Karsuki Ti** (West Market) →
  **HIP 7311** (Fan Base, unoccupied), bought 23:48, sold 23:56 — ~18 min from Grushin
  Prospect. 1 Oct: → Tucanae Sector WO-Z b0 (Fefra's Legacy), ~20 min. 18 Sept: → HIP 7311, ~12 min.

### 4.2 Ship scans, reinforcement

- **Recognise it:** scan in an Aisling system that needs reinforcing (nav beacon scan).
- **Ship:** combat hull (18 Sept: Pacifier).
- **Run:**
  - [ ] Check the power distribution priorities before going in (open task, §5.1).
  - [ ] Drop at the nav beacon, do the scan, leave.
- **Pitfalls:** pirates thick around the beacon at **HIP 3254** (Aisling Stronghold, heavy
  undermining). Second visit that day: shields dropped, hull down to 79.9%, lost power mid-fight
  — escaped on the Clipper's speed.
- **Easy in passing:** every ship targeted in an Aisling system pays **+7 merits** per scan, so
  any combat session there fills this assignment without trying (16 Oct, Osane massacre stack).
- **Stats:** 2 runs · +2,000 merits each · last: 16 Oct, **Osane** (Stronghold), during the
  massacre stack — paid 01:36. 18 Sept: HIP 3254 — scan done 11:18 (visit 11:12–11:24).

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
- **Pitfalls:**
  - **Check the distance before accepting the trip.** 13 Oct, Alpha Centauri (Aisling
    Stronghold, six Powers present): two salvageable-wreckage signals, but ≈800,000 Ls from the
    arrival star — limpets bought at al-Din Prospect (00:18), then given up. A 2,800-merit
    assignment isn't worth a long supercruise; skip it that week (§2).
- **Quick version (25 Oct):** in an **Aisling Exploited** system with a station, drop on the
  **"Power wreckage signature"** signals (*Signature d'épave de puissance*), collect with limpets,
  hand in at the same system's station (`SearchAndRescue`). Col 285 Sector WO-O b20-1: three
  signals, 4 occupied escape pods + 8 wreckage components + 3 black boxes, handed in at **Spitzer
  Gateway** — **15 min**. It's the pyrophyllite loop's sell station (§3): do both together.
- **Stats:** 2 assignments · +2,800 merits each · last: 25 Oct, Col 285 Sector WO-O b20-1 →
  Spitzer Gateway, 21:43–21:58. 18 Sept:
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
- **Pitfalls:**
  - Every screen can be selected in these systems — "easy."
  - **Each hack is a crime:** `stationTamperingMinor`, **2,000 CR fine** to the station's
    faction (9 fines at Chinga, 13 Oct; 11 on 25 Sept). Cheap, but pay them before docking there.
  - Hacks in an **Aisling** system don't count for this one: 7 hacks at Newton Port (Khepri,
    13 Oct 00:55–01:08) paid 126 merits each but no assignment payout — that's card 4.7.
- **Unoccupied variant (25 Oct):** the assignment can name an **unoccupied** system instead —
  same method. ICZ OX-U c2-15, Bowen Beacon: 12 hacks in 4 drops of 3, 126 merits each, paid on
  the 12th. ⚠ The fines (2,000 CR each) went to **Nexus Heavy Industries** — a Cubeo faction
  you donate to for Navy rank. Check who owns the station before hacking.
- **Stats:** 3 assignments · +4,800 merits each · last: 25 Oct, **ICZ OX-U c2-15** (unoccupied),
  21:27–21:41, ~14 min. 13 Oct: **Chinga** (Lavigny-Duval,
  Fortified), Wilson Stop — 9 limpets, 8 paid hacks × 67, 01:38–01:48, ~10 min (3 drops of 3). 25 Sept: Shui Wei
  Sector VT-R b4-5 (Lavigny-Duval, Exploited), Lounge Reach — 14 × 86, ~20 min.

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
  - Another system that fits the rule: **Khepri** (Exploited; Lavigny-Duval, Mahon, Grom
    present), Newton Port — 7 hacks × **126 merits** on 13 Oct (00:55–01:08), no fines. Good
    loose merits even when this isn't the week's assignment.
- **Stats:** 2 assignments · +2,400 merits each · last: 26 Oct, **Amaneque** again (Gilliland
  Colony) — 8 hacks, one per drop, 11:17–11:31, ~14 min, **no fines**. First: +2,400 (+ 5 × 100 and 7 × 65 per hack), 25–26 Sept,
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
  Gabraceni). **7 common data items still in the ship locker** (29 Sept) — hand them in. One
  was handed in at Wababa on 1 Oct for only 187 merits. Fresh data from an unoccupied system
  paid 540 per item the same day (card 4.11).

### 4.9 Megaship datalink scans

- **Recognise it:** scan the datalink (uplink) of megaships in Aisling systems.
- **Ship:** the Dart (fast, small, recon limpets on board). Journal event: `DataScanned`
  `$Datascan_ShipUplink;`.
- **Run:**
  - [ ] Megaships sit near planets: supercruise to the planet, drop at the megaship signal.
  - [ ] Target the datalink and scan it, then leave.
  - [ ] Chain systems one jump apart (1 Oct: Primi → Lambda-1 Tucanae → Osane → Ehlanda →
        Fire Fade → HIP 7142, via Cubeo as a hub).
- **Pitfalls:**
  - **Cubeo paid 0 merits** for two scans (1 Oct 13:40 and 13:46). Every other system paid
    468: Karsuki Ti, Lambda-1 Tucanae, Osane, Ehlanda, Fire Fade (Strongholds), Primi and
    HIP 7142 (Fortified). Cause unconfirmed (Cubeo is Aisling's capital). Skip Cubeo.
- **Combine it with faction missions:** Prismatic Imperium's "access the megaship uplink" missions
  (`Mission_HackMegaship`, 0.1–1.9M CR each) are the same scan — credits, Navy progress and
  merits at once (17 Oct).
- **Stats:** 2 assignments · +2,400 merits each + **468 per scan** · last: 17 Oct, 9 scans
  18:58–20:25 alongside six Prismatic Imperium hack missions (Huang Gun, HIP 7869, Boloine, Clido
  Pi, Koyans…; Segnir abandoned). 1 Oct: 8 paid, 11:57–14:27.
  **~6.5 min per megaship** at a steady pace (6 scans 13:48 → 14:27) → **~4,300 merits/h**;
  ~3,100 merits/h over the whole run.

### 4.10 Aisling sealed contracts

- **Recognise it:** collect `aislingmediaresources` ("Aisling's sealed contracts", Tonton
  Marcel's "Aisling bonds") and deliver them to another Aisling system — sometimes one under
  undermining.
- **Ship:** any hull with a small cargo hold (1 Oct: the Dart, 14 t; 13 Oct: Marco Polo, 30 t).
- **Run:**
  - [ ] Collect at the Power contact (1 Oct: 12 at Medupe City, Cubeo; 13 Oct: 30 at Wheelock
        Settlement, Zeaex).
  - [ ] Deliver to the target system's station.
- **Pitfalls:** none met — 6–7 min from collection to delivery. A bigger load pays a bit more on
  top (+180 for 30, +37 for 12).
- **Stats:** 2 runs · +2,000 merits each · last: 13 Oct, Wheelock Settlement, **Zeaex**
  (Stronghold, 00:42) → **Banks Port, Khepri** (Exploited, four Powers present — undermined,
  00:48). 1 Oct: Medupe City → Roelofs Station, Wababa.

### 4.11 Power data on foot (association / political / research)

- **Recognise it:** download the common Power data types (`poweremployeedata` = association,
  `powerpropagandadata` = political, `powerresearchdata` = research) at settlement data ports,
  and hand them in.
- **Ship / suit:** the Dart (lands close to the settlement); on-foot suit.
- **Run:**
  - [ ] Pick settlements in an **unoccupied** system next to Aisling space (1 Oct: Irush;
        21 Oct: Tucanae Sector BV-X b1-1, one jump from Cubeo).
  - [ ] Prefer a settlement **not** owned by an Imperial faction you're building rep with: every
        download seen is a fine with the owner (21 Oct: HIP 1914 Imperial Society, a Navy-rank
        faction).
  - [ ] **One item per landing, then leave:** download, run back to the Dart, lift off,
        supercruise, drop straight back in. The settlement resets — fresh data ports, guards
        calm again (21 Oct: 9 items in 9 drops, ~4–6 min each).
  - [ ] Stealth or brute force: see `On-Foot.md` §1 ("Play-tested 21 Oct").
  - [ ] Hand in at an Aisling Stronghold station (1 Oct: Jones Hub, Kapoongzi; 21 Oct: Roelofs
        Station, Wababa — two jumps).
- **Pitfalls:**
  - 1 Oct took 12 landings for 10 items.
  - Two re-logs on the ground (15:47, 16:07) and ~50 min lost before the first item.
  - Value per item depends on where it came from: **540** (association, political) and **360**
    (research) for Irush data. An older association item from the locker paid **187** at
    Wababa.
  - **21 Oct: 7 `onFoot_dataTransfer` fines (500 CR each) + 1 trespass (250 CR)** with HIP 1914
    Imperial Society — every download that an NPC saw, even with the alarm disabled.
- **Stats:** 2 assignments · +5,600 merits each · last: 21 Oct, **Techno Defence Facility**
  (Tucanae Sector BV-X b1-1 5, unoccupied) → Roelofs Station, Wababa — 7 association + 2
  political, **540 merits each** (4,860) — 07:05–08:08 and 11:13–11:54, **~6,000 merits/h with
  the assignment, ~2,800/h without**. 1 Oct: +5,600 merits + **5,040 for the items** (5 association, 3 political,
  2 research) · last: 1 Oct, **Irush A 3 a** (Ganguly's Garden, Ma Hydroponics Hub),
  15:09–17:15. ~2,100 merits/h over the whole session (143 min); ~3,300 merits/h if the lost
  50 min are left out.

### 4.12 Power goods stolen on foot (Power containers) → Aisling system

- **Recognise it:** take Power goods from the **Power containers** at a settlement in a
  **rival Power's** system, and hand them in at an Aisling station. Items seen (13 Oct):
  `powerequipment` (personal protective equipment), `powerinventory` (stock register),
  `poweragriculture`, `powermedical`, `powerresearch`, `powerexperiment`.
- **Ship / suit:** the Dart (lands close to the settlement); on-foot suit.
- **Run:**
  - [ ] Pick a settlement in a rival system next to Aisling space (13 Oct: Kremovi,
        Lavigny-Duval Fortified, one jump from Cubeo via Morinmutino).
  - [ ] Land **outside the no-landing zone** (800 CR `dockingMinorTresspass` fine at Verne
        Landing, 02:06), walk in, empty the Power containers.
  - [ ] Hand in at the nearest Aisling station (13 Oct: Reid Gateway, **Oshanla**, Fortified —
        one jump from Kremovi).
- **Pitfalls:**
  - Goods are worth little on their own: ~52 merits per item (7 items → 367, 5 items → 262).
    The assignment payout is what counts.
  - Took **two trips**: the first hand-in (7 items) paid no assignment; the payout came with the
    second (5 more, 12 in all). Check the required quantity before the first landing.
- **Stats:** 2 assignments · +4,800 merits each · last: 25 Oct, **Heath's Quarry** (Shui Wei
  Sector VT-R b4-4 A 2, Lavigny-Duval Exploited) → **Smoot Station, Chona** (Stronghold) — three
  landings, 18 items (equipment, inventory, extraction samples, a military plan…), paid on the
  10th handed in, 22:07–22:59.
  13 Oct: **Savko Nutrition
  Habitat** (Kremovi A 2) → Reid Gateway, Oshanla — 01:58–03:08, ~70 min with the two trips.

### 4.13 Kill rival Power ships in a named system

- **Recognise it:** destroy ships of **another Power** in the system the assignment names. Only
  ships whose target panel shows a rival Power count (journal `ShipTargeted` → `Power`).
  Minor-faction pirates, even Wanted ones, don't count (17 Oct, HIP 3254).
- **Ship:** combat hull (17 Oct: Nemesis).
- **Where the rival ships are:**
  - [ ] **In a system the rival Power holds:** look for **"Power convoy distress signal"**
        (*Signal de détresse de convoi de puissance*). 17 Oct, Shui Wei Sector VT-R b4-5
        (Lavigny-Duval, Exploited): two signals in 15 min, full of Lavigny-Duval Type-9s,
        Cobras, Vipers and Anacondas, all marked "Enemy". A **"Power weapons fire signature"**
        (*Signature de tirs de puissance*) works too (17 Oct evening, 2 kills).
  - [ ] **In an Aisling system:** rival ships only show up if a rival Power is **present**
        there — check the `Powers` list (system panel, or journal `FSDJump`), the same rule as
        the reinforcement holoscreens (card 4.7). **HIP 3254 lists only Aisling** (17 Oct,
        five visits), despite 42,125 undermining. That undermining most likely comes from rival
        commanders playing in Open, who can't be met in Solo. Convoy dispersals, weapons fire,
        trade beacons and Power wreckage signals there held only minor-faction ships.
  - [ ] So in an Aisling system with only Aisling listed, the assignment **can't be done in
        Solo**. Probably not a bug in the mission itself: the game picks a system where rivals
        are active, but in Solo only their effect (the undermining) is visible, not their
        ships. Skip it (§2) — or, if a rival Power is listed, look for its ships at the
        signals above.
- **Pitfalls:**
  - **Every kill is a murder** for the system's authorities: 5,000 CR bounty per ship plus
    200 CR per assault (The 10th Legion, 17 Oct). You're **Wanted** in that system afterwards:
    expect the police to join in, and don't dock there.
  - Convoys mix armed escorts and Type-9 haulers; the haulers are slow and tanky, kill the
    escorts first.
  - The journal again wrote the +4,800 payout twice (21:02:04 inside a +4,978, 21:02:05 alone);
    the next line's total shows only one was real (same glitch as card 4.12).
- **Stats:** 1 assignment · **+4,800 merits on the 10th kill** + ≈230 per kill (178–312) ·
  17 Oct, **Shui Wei Sector VT-R b4-5** (Lavigny-Duval) — 11 kills in two visits: 5 at 16:11–16:17,
  6 at 20:50–21:03 (one weapons-fire signature, two convoy signals). ≈20 min of fighting in all.
  Cost: 11 murders, ≈57,000 CR of bounties with The 10th Legion.

### 4.14 Power malware uploads at a rival settlement

- **Recognise it:** collect **Power injection malware** (`powerpreparationspyware`, *Malware
  d'injection de puissance*) at an Aisling Power contact and upload it at a **rival Power's
  settlement** — each upload uses one from the backpack.
- **Ship / suit:** the Dart; on-foot suit.
- **Run (25–26 Oct):**
  - [ ] Collect at the Power contact (Bessel Dock, **Munshin**, Stronghold — 10 at a time).
  - [ ] Land at the rival settlement (**Heath's Quarry**, Shui Wei Sector VT-R b4-4 A 2,
        Lavigny-Duval, one jump), find the terminals, upload.
  - [ ] Same re-landing loop as card 4.11 when things heat up; collect more malware at
        Munshin if needed. Steal the Power goods in passing (card 4.12) — they pay too.
- **Pitfalls:**
  - Two `onFoot_dataTransfer` fines and one *failure to submit to police* (The 10th Legion) on
    26 Oct — the uploads are witnessed like downloads (`On-Foot.md` §1).
  - The payout came on the **11th upload** (10:55), over three landings and ≈3.5 h with a
    break.
- **Stats:** 1 assignment · **+5,200 merits** · 26 Oct, Munshin → Heath's Quarry, 07:24–10:55.
