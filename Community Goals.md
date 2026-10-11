# COMMUNITY GOALS — CMDR ONCLEMARCEL
## CG playbook, results, one card per CG

> Technical document. No narrative here — the story lives in `Logbook.md`.
> Satellite of `In-Game Operations.md`, created 11 October 2026 at Tonton Marcel's request: the
> CG detail (standings, brackets, sources, cycles, forecasts) moved here from §4 (session logs)
> and §5.4 (roadmap) of that file, which now keeps a one-line summary per CG and a link here.
> **How it grows:** one card per CG, newest first. While a CG runs, its card takes the detailed
> log (each standing, each source change); `In-Game Operations.md` §4 only gets what *happened*
> in the session, in a few lines. Lessons that hold beyond one CG go to the playbook (§2),
> refined in place.
> **References:** a bare `§N` points to `In-Game Operations.md`; ship names point to
> `Shipyard.md`.

---

## 1. Results

| CG | Type | Dates | Ship | Contribution | Bracket | Contributors | Reward |
|---|---|---|---|---|---|---|---|
| **861** Brewer Corporation Jump Satellite Initiative (Zero Squared, HIP 74116) | Trade (delivery) | 8–11 Oct 2026 | The Brick | **26,530 t** | **Top 25 %** | 11,810 | **200,000,000 CR** (11 Oct) + SCO FSDs size 4–7 (not located yet) |
| **860** Eliminate criminal pilots in Redonesses (Sword of Iustitia) | Combat (kill bonds) | 6–8 Oct 2026 | Pacifier | **19,122,798 CR** of bonds | **Top 25 %** | 8,849 | **220,000,000 CR** (8 Oct) |
| **859** Wreaken Calls for Sourced Materials… (Metz Enterprise, Ega) | Trade (delivery) | → 18 Sept 2026 | The Brick | **15,918 units** | **Top 25 %** | — | **170,000,000 CR** (18 Sept) |

Three CGs since the return, three Top 25 % finishes.

---

## 2. Playbook

- [ ] **Every week:** check the active CGs (Inara) and pick the ship via the target-fleet table
      (§5.5). Sign up at the CG station first — the first hand-in signs you up anyway.
- **What counts:** read the CG text closely. CG 860 (combat) counted **only combat bonds** —
  bounties cashed in the same system left the contribution at 0. A delivery CG counts tonnes, so
  any listed commodity works: pick by tonnes per hour first, profit per tonne second.
- **Taxi doctrine:** fly a fast ship (Marco Polo) to the CG, sign up, request the working ship's
  transfer from Medupe City (~1 h 15 for ~400 ly) and scout sources while it travels.
- **Sources:** Spansh/Inara stock figures older than a few hours are unreliable when thousands of
  commanders share a market — check the market's age, or the market in game, before committing.
  Busy sources empty within a day (CG 861: Thorn 673k t → 9k t in 24 h), but outposts restock
  between visits: mixed loads (whatever the best commodity has restocked + a second commodity to
  fill the hold) keep full tonnage every run.
- **Early close:** a CG that ends "when the target is met" can close days ahead of its expiry date
  — the pace accelerates through the week (CG 861: 2.9M/h → 7.5M/h). Re-forecast the close each
  session from the journal's `CommunityGoal` readings (`CurrentTotal` over time).
- **Bracket forecast (measured on CG 861, held at the close):** the Top 25 % threshold ≈
  **1.45 × the average contribution** (total ÷ contributors; measured 1.34 → 1.37–1.47 → 1.43–1.49
  → 1.41–1.46). Top 50 % ≈ 0.7 × the average, Top 75 % ≈ 0.1–0.35 ×. Forecast the threshold at
  the close as 1.45 × target ÷ expected contributors. An earlier close means fewer contributors
  sharing the target, so a *higher* threshold. Overnight, participation slows: a close during the
  night needs a smaller margin than a daytime one (CG 861: 8 runs would have done instead of 10).
  The in-game bracket is coarse and moves back and forth near the line (CG 861 slipped to Top
  50 % twice overnight).
- **Reward collection:** Frontier finalises a CG some hours after it closes (`IsComplete: true`);
  the credits then appear at the CG station (`CommunityGoalReward`). Collected so far in the
  working ship, on the spot.
- [ ] **Module rewards (open):** where do pre-engineered module rewards land when the CG station
      has no outfitting (CG 861, a megaship)? Not in storage on 11 Oct 13:59
      (`StoredModules`). To check: the CG text on Inara, the Frontier forum thread, and storage
      again in a few days.

---

## 3. CG cards

### CG 861 — "Brewer Corporation Jump Satellite Initiative" (8–11 October 2026)

**Brief (Inara, 8 Oct 20:01 UTC):** deliver **Semiconductors, Superconductors, Power Generators
or Computer Components** to the megaship **Zero Squared, HIP 74116** (6 ls; sign up there
first). ~461 ly from Cubeo. Runs one week (≈ until 15 Oct; ends early if the 200M target is
met — 4.7 % on 8 Oct).

**Result:** **26,530 t, Top 25 %**, 11,810 contributors at the close (200,000,158 t, tier 5,
completed overnight 10–11 Oct). Reward **200,000,000 CR** collected 11 Oct 13:48 at Zero
Squared. Hauling profit on top: **≈1.36 billion CR** over 35 runs (journal `MarketSell` − `MarketBuy`).

- **Rewards:** Top 75 % → pre-engineered SCO FSDs **size 4 and 5** (Increased Range + Fast
  Boot, experimentals unlocked); **Top 50 % → also size 6 and 7**, plus credits by tier. Size 5
  = Corsairs (Nemesis, Soteria, Aegis) and Clippers; **size 6 = the three Cutters**
  (Cornucopia, Hephaestus, Charybdis). Target was Top 50 % — thresholds on 8 Oct: Top 50 % from
  ~3,645 t, Top 25 % from ~6,912 t; aim 10,000 t+.
  - [ ] **Locate the four SCO FSDs** — not in storage on 11 Oct (playbook, §2).
- **Commodity:** contribution counts tonnes, so any of the four works. Zero Squared buys:
  Superconductors 65,510 · Power Generators 23,880 · Semiconductors 10,840 · Computer
  Components 7,080 CR. Profit per 758 t run: Superconductors ≈44.6M, Power Generators ≈16.5M,
  Semiconductors ≈7.4M, Computer Components ≈4.9M CR — Superconductors first while a source
  lasts, Power Generators to fill the hold.
- **Plan (taxi doctrine):** the Marco Polo flew to Zero Squared, signed up, requested The
  Brick's transfer from Medupe City and scouted meanwhile. Planned source Peralta Station
  (52.4 ly, 25 ls) — its Superconductors were already gone, so the runs started from Thorn
  Constructions (HR 5518).

**Sources**

| Source (L pad) | ly from HIP 74116 | ls | Superconductors | Also | Used |
|---|---|---|---|---|---|
| Thorn Constructions, HR 5518 (Grushin Prospect system) | 55.1 | 608 | 6,808 CR, 673k t on 8 Oct → 9k t on 9 Oct | Semis, Power Gen | 9 Oct morning, 14 runs |
| **Vercher Survey**, Col 285 Sector US-B b29-3 | 70.8 | 35 | 6,608 CR, 504k t on 9 Oct, then restocking between visits | Semis 1.32M t, Power Gen 207k t, Computers 554k t | 9 Oct afternoon → end, 21 runs |
| Schroder Vision, Col 285 Sector GQ-F b27-1 | 66.1 | 16 | 6,584 CR, 96k t | Semis 102k t; Stupka Berth (28 ls): Power Gen 273k t | — |
| Porzio Station, Praea Euq IT-X b2-1 | 68.5 | 109 | 6,808 CR, 347k t | Semis 528k t, Power Gen 76k t | — |
| Arnold Collection, Praea Euq ZP-X c1-9 | 70.4 | 536 | 5,909 CR, 1.32M t | Semis 809k t | — |
| Peralta Station, Praea Euq PY-Y b1-0 | 52.4 | 25 | gone by 8 Oct | Power Gen 2,330 CR, 123k t; Semis 565k t | — |
| Schubert Berth, HIP 75663 (Inara's pick) | 50.5 | 1,019 | 6,071 CR, 1.25M t | — | — |
| Lim Hub, 3 Serpentis (last Superconductors, 10 Oct) | 73.1 | 1,648 | 6,710 CR, 123k t | — | — |

**Runs and route**

- **Thorn Constructions (9 Oct, 06:31–11:45):** 14 runs of 758 t Superconductors, bought at
  6,808 CR, sold at 65,510 CR — **44.5M CR profit per run, ≈623M CR in total**. Cycle ~13–14 min
  sale to sale (median ~14:30, best 12:50). Out 2 jumps empty (28.7 + 27.1 ly), back **4 jumps
  laden** (18.4 / 15.2 / 19.1 / 9.7 ly) — laden range ≈ 20 ly. ≈4.4 runs/h → ≈3,300 t/h and
  ≈195M CR/h. Two near-empty fuel arrivals → 6C tank (`Shipyard.md`, The Brick).
- **Vercher Survey (9 Oct 12:55 → 10 Oct 23:36):** out 3 jumps empty, back 4 jumps laden (19.7 /
  19.9 / 19.1 / 17.1 ly, 30.6 t of fuel). Cycle 13:05 on 9 Oct; **12:40 on average** on the last
  evening (nine cycles). Superconductors only at first (≈44.6M CR per run), then from 10 Oct
  14:03 **mixed loads**: whatever Superconductors had restocked (188–755 t) + Power Generators
  (2,666 CR) to 758 t — ≈21–49M CR per run. Last evening: ten runs, 4,413 t + 3,167 t,
  **327.1M CR**, ≈4.7 runs/h → ≈3,600 t/h and ≈170M CR/h.
- **Interdictions:** four NPC, two escaped (9 Oct), two submitted to (10 Oct, 22:10 and 22:48),
  no damage.

**Standings (journal `CommunityGoal`)**

| When (UTC) | Contribution | Bracket | Contributors | CG total | Tier / pool |
|---|---|---|---|---|---|
| 9 Oct 11:58 | 10,612 t | Top 25 % | 4,620 | — | 2 / 155M |
| 9 Oct 13:25 | 12,128 t | Top 25 % | 4,872 | — | — |
| 10 Oct 07:35 | — | slipped to Top 50 % | — | — | — |
| 10 Oct 11:06 | 13,644 t | Top 50 % | — | 100.3M | — |
| 10 Oct 15:56 | 18,950 t | Top 25 % | 9,629 | 122.5M | 3 / 170M |
| 10 Oct 21:26 | 18,950 t | Top 50 % | 10,770 | 158.6M | 4 / 130M |
| 10 Oct 22:20 | 21,982 t | Top 25 % (21,224 t still Top 50 % at 22:18) | 10,975 | 165.7M | 4 / 185M |
| 10 Oct 23:36 | **26,530 t** | Top 25 % | 11,233 | 174.9M | 4 / 185M |
| 11 Oct 13:47 | 26,530 t | **Top 25 %, final** | 11,810 | 200.0M, complete | 5 / 200M |

**Forecasts (10 Oct)**

- *Close:* rate per interval 2.9M/h overnight 9–10 Oct → 3.2 → 4.3 → 5.1M/h (13:57–15:29) →
  7.5M/h in the evening. Forecast at 23:36: close ≈ 11 Oct 03:00–07:00 UTC.
- *Rule for the last day:* **tonnes per hour first** (the CG may close within hours) — same
  route, other commodity: Power Generators at Vercher Survey, then Stupka Berth, Semiconductors
  if those ran out; Lim Hub only if Superconductor profit mattered more than the bracket.
- *Top 25 % threshold:* ≈ 1.45 × the average contribution (playbook, §2). Target set at 15:56:
  **25,000 t or more** (≈ 8 more runs). At 23:36: 200M ÷ ~11,800–12,300 contributors ×
  1.41–1.49 → **≈ 23,000–25,300 t**; 26,530 t would only be overtaken if the ratio climbed to
  ≈ 1.55–1.6, or if the CG ran on to 15 Oct.
- *Outcome (11 Oct):* forecast confirmed — Top 25 % held with 11,810 contributors at the close.
  Participation slowed overnight more than assumed: **8 runs would have been enough** instead
  of 10 (25,014 t at 23:10).

---

### CG 860 — "Eliminate criminal pilots in Redonesses" (6–8 October 2026)

**Brief:** Sword of Iustitia, Redonesses Defence Party; combat bonds against Clan of
Redonesses. Ended 8 Oct, 10:00 UTC.

**Result:** **19,122,798 CR** of bonds (the last hand-in of 7 Oct, 18:33, counted after the
18:32 reading), **Top 25 %**, 8,849 contributors, tier 2, bonus pool 220M CR. Reward
**220,000,000 CR** collected 8 Oct 21:26 at Redonesses — not yet available at 10:39 that
morning (`IsComplete: false` after the expiry; finalised some hours later).

- **6 Oct (Pacifier V2's first fight):** bonus pool 110M CR, 7,579 contributors, tier 1 of 5.
  - **12:38–13:20, bounty hunting** at the EVE-597 Riker-class Reformatory (a prison megaship):
    **13 wanted ships** — 3 Pythons, an Anaconda, 2 Krait Mk II, 2 Krait Phantoms, 2 Vultures,
    2 Viper Mk IV, an Eagle → **5,070,483 CR** of bounties.
  - **13:20–15:02, conflict zones** against Clan of Redonesses: four low-intensity and one
    medium-intensity → **20 kill bonds, 2,589,023 CR**.
  - **Only the combat bonds count for this CG:** the contribution stayed at 0 after the 5.07M CR
    of bounties were cashed, then moved to 988,656 and 2,589,023 with the bonds. Bracket
    **Top 75 %**.
  - Shields lost six times, lowest hull **58 %**, three heat warnings, no death. Repairs and ammo
    ≈96k CR. Tonton Marcel's account: the beams run the weapon capacitor dry quickly; the
    turreted multi-cannons do little damage even on unshielded targets → weapons reworked 7 Oct
    (`Shipyard.md`, Pacifier).
- **7 Oct, ~9.5 h on and off:** 18 low-intensity and 2 medium-intensity conflict zones —
  **107 kill bonds**, cashed in 12 trips to Sword of Iustitia for **13,580,454 CR** (redeemed
  value ≈3× the 4.36M CR shown at each kill). Plus 4 bounties (574,245 CR).
  - Standing at 15:44: contribution 2,589,023 → **16,169,477 CR**, bracket **Top 75 % → Top
    25 %**. Tier 2 of 5, bonus pool 220M CR, 8,235 contributors.
  - Evening, 17:15–18:33: four more low-intensity zones, 24 kill bonds, 2,953,321 CR redeemed.
    Standing at 18:32: **17,783,572 CR, Top 25 %**, 8,336 contributors.
- **Metrics:** every zone rebuilt with `tools/combat_stats.py` — benchmark table in Checkpoint 1
  (§5.4).

---

### CG 859 — "Wreaken Calls for Sourced Materials for Output Comparison Tests" (closed 18 September 2026)

**Brief:** Metz Enterprise, Ega — delivery CG flown with The Brick. The Ega CG is already told
in `Logbook.md` (through the 17 Sept entries).

**Result (journal-verified):** **15,918 units contributed, Top 25 %, 170,000,000 CR paid.**
Docked at Metz Enterprise 07:18:29 UTC on 18 Sept; the `CommunityGoal` read moments later
confirmed **CGID 859 `IsComplete: true`**, final `PlayerContribution` **15,918**,
`PlayerPercentileBand` **25** (supersedes the 17 Sept 50 %-band expectation).
`CommunityGoalReward` fired at 07:18:48 UTC for **170,000,000 CR** — exactly the live `Bonus`
figure spotted 17 Sept.
