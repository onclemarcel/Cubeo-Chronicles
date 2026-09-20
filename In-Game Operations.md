# OPERATIONAL GUIDE — CMDR ONCLEMARCEL
## Campaign memory — status as of 18 September 2026 (3312), end of evening session

> Technical document. No narrative here — the story lives in `Logbook.md`.

---

## 1. COMMANDER SHEET

| | |
|---|---|
| CMDR | Onclemarcel |
| Inara role | Freelancer / Scientist |
| Squadron | EliteCommanders |
| Trade rank | **Elite** (earned 16 Sept 2026) |
| Imperial Navy rank | **Viscount** |
| Power | Aisling Duval — pledged, **Rank 5 / 16,424 merits** |
| Home port | Cubeo — Medupe City |
| Treasury | **1,818,649,914 CR** |
| Game mode | Solo |
| Expansions | Horizons + Odyssey |
| Absence | ~4 years (last memory: Thargoid war, Colonia CG) |

---

## 2. THE FLEET — STATUS AND WORK ORDERS

### 2.1 Asp Explorer — *exploration / rescue*

**Current fit** (`MA-07A`, ShipID 4 — matches the Inara SLEF export of 19 Sept): FSD 5A *Increased
Range* g4 + *Deep Charge* (43.08 ly unladen / 41.17 laden) · DSS 1I g5 *Expanded Probe Scanning
Radius* (CG reward, irreplaceable) · Fuel Scoop 6A · Power Plant 5A *Armoured* g1 / Thrusters 5A *Tuned*
g1 (thrusters on power priority 3 — the likely origin of the old "`enabled: false`" scare) ·
planetary hangar 2G, shield 5D, 20 t cargo racks · collector limpet controller 3A · life support 4D ·
distributor 4D · sensors 5D. *Lakon hull — stored from 19 Sept (§3, rule 6); modules moved to
storage keep their engineering (rule 2), so the DSS and FSD can follow her into a Gutamaya hull.*

**To fix**
- [x] Thrusters flagged `enabled: false` in the export — **closed 19 Sept**: no problem observed in
      play; the Asp flew the Ega CG and the Lambda Hydri rescue runs (§4b) without issue. Export
      artefact, not a real fault.
- [x] Strip 2× missile racks 2B + 4× lasers 1E → ~13 t of dead weight — **done 18 Sept**, all 6
      hardpoints sold at Medupe City (journal-verified, +1,341,400 CR combined with the shield
      boosters below)
- [x] Strip the 2 shield boosters 0A → ~7 t — **done 18 Sept**
- [ ] FSD grade 4 → **grade 5** (Farseer)
- [ ] Thrusters and power plant grade 1 → **grade 5**
- [ ] Add an **AFMU**
- [x] Fill the empty utility slots with **heat sink launchers** — **done 18 Sept**, all 4 tiny
      hardpoints fitted (not just the 2 originally empty — the 2 freed by the shield-booster strip
      got one too)
- [ ] Unlock and fit the **Guardian FSD Booster** (Tech Broker) → target 55+ ly
- [~] Buy an **FSD 5A (SCO)** and keep the engineered FSD in storage — **tried and reverted, 18
      Sept**: bought the SCO (5,971,625 CR), test-fitted it, judged the range loss too steep against
      the grade-4 *Increased Range*/*Deep Charge* engineering (43.08 ly unladen); swapped back to
      the engineered FSD and put the SCO in storage instead (free, same station). Revisit once the
      FSD reaches grade 5 — a higher engineered range floor may make the SCO trade-off easier to
      accept.

**Two loadouts to save:** *Long range* and *Rescue* (limpets + cargo racks). The 18 Sept strip
already puts the ship close to the *Long range* config (no weapons left at all) — worth locking in
as a saved loadout before anything gets re-added by habit.

**Re-armed for the rescue runs — 18 Sept, 18:32–18:35 UTC (journal-verified):** 2× medium gimballed
pulse lasers, 4× small fixed dumbfire missile racks and a **collector limpet controller 3A** (slot
4) were fitted. This reverses the earlier strip — the habit warned about above — and is deliberate
only for the collector limpets: the Asp is the medium-pad hull that can land at Hansteen Depot
(Lambda Hydri), where the Clipper cannot (§4b). Strip the weapons again before the *Long range*
loadout is saved.

### 2.2 Imperial Clipper — *combat / bounty hunting*

`MA-10E` (ShipID 2). **Fit as of 19 Sept — Inara SLEF export, cross-checked against the journal
`Loadout` of 18 Sept 19:57 UTC:**

- **Hardpoints:** 2× large gimballed beam laser 3C · 2× medium multi-cannon **turret** (replaced the
  2 medium gimballed beams, 18 Sept 12:06) · 2× shield booster · 2× chaff launcher (replaced the
  third booster and the crime scanner, 12:07)
- **Core:** shield 6A · thrusters 6A · power plant 6A · distributor 6A · sensors 5D · life support 5D ·
  fuel tank 4C · armour **grade 3** (20.07M CR)
- **FSD:** 5A, engineered **Faster Boot Sequence g5** — *not* the stock 5E the earlier version of this
  sheet claimed; the upgrade was already done before 18 Sept
- **Internals:** cargo rack 7E · 2× hull reinforcement 4D · module reinforcement 1D · fuel scoop 3A ·
  FSD interdictor 2D · multi limpet controller (operations) 3C · planetary hangar 2G
- **Engineering:** the FSD is the *only* engineered module on the hull — weapons, shields, power
  plant, distributor and thrusters are all stock. That is the real work order for this ship (see §13)
- **Flagged `Hot: true` in the export** — cause not identified (no `CommitCrime` on this hull in the 16–18
  Sept journals except two 400 CR docking fines on the 16th). Check in-game; it can restrict docking

*Correction, 19 Sept:* the "FSD 5A on the combat Clipper" item in earlier versions of this file was
based on a stale export. The 5A engineered FSD on **this** hull was already fitted; the 18 Sept
purchase (12:38 UTC) was the *mining* Clipper's (§2.3), as Tonton Marcel reported. No burst lasers are
fitted: per Tonton Marcel the weapon change was a power-budget experiment, and the beam lasers turned
out to fit within the power limit after all.

**Future role:** Powerplay merit generator. **Do not sell.**

**18 Sept, journal-verified:** flown for the Tritium supply mission round trip (Medupe City →
Cellarius Beacon → Medupe City, §4) specifically for its 440 m/s top boost — no interdiction taken.
Repaired on departure (2,692 CR).

### 2.3 Imperial Clipper — *mining*

`MA-04E` (ShipID 10). **Fit as of 19 Sept — Inara SLEF export:** cargo rack 7E (128 t) · 3× collector
limpet controller 3A · prospector limpet controller 1A · refinery 2A · 2× fixed mining laser 2D ·
DSS 1I (unengineered) · shield 6A · thrusters 6A · power plant **6C** · distributor 6A · fuel scoop 4A ·
sensors 5D · life support 5D · armour grade 1. It also carries 1× large gimballed beam laser, 1× large
gimballed multi-cannon, chaff, ECM and 2× shield booster — more armed than the earlier sheet said.
**No engineering on any module.**

**FSD 5E → 5A: done 18 Sept, 12:38 UTC (journal-verified, ShipID 10, unengineered)** — the "FSD 5A on
the Clipper" item from the old Immediate list. The combat Clipper already had its own (§2.2).

*Was to be replaced by the Type-11 Prospector — shelved 19 Sept by the Gutamaya-only rule (§3, rule
6); this hull is now the mining hull for the foreseeable future.*

### 2.4 Type-9 Heavy — `ON-16T`

**758 t cargo · 26.49 ly · total value 130.7M CR · hull 76.5M**

Fully outfitted. **This was the CG ship** — CG 859 closed 18 Sept (§4), so the Type-9 is off active CG duty. **SLEF fit, 19 Sept** (`MA-16T`, ShipID 11): FSD 6B engineered *Increased Range* g5 + *Deep Charge* · power plant 6A · thrusters 6A · distributor 6A · shield 5A · sensors 4E · 3 medium + 2 small gimballed weapons · armour grade 1. Lakon hull — **stored, not flown, from 19 Sept** (§3, rule 6). An SCO FSD is no longer a priority.

**Current location (18 Sept, journal-verified): home at Medupe City.** `ShipyardTransfer` from Ega
(Metz Enterprise) to Medupe City — 200.5 ly, 1,599,783 CR, ~38 min transfer, completed the same
session as the Asp refit. First time all four hulls (Asp, combat Clipper, mining Clipper, Type-9)
have sat docked at the same station together this campaign.

### 2.5 In storage

**Modified Mining Laser 1A — pre-engineered grade 5** — LHS 3872 [Curbeam Hub].
**Class 1** hardpoint: incompatible with the Clipper (large/medium hardpoints only), destined for the Asp. To retrieve.

---

## 3. ESTABLISHED GROUND RULES

1. **Never sell.** Ship and module storage are free and unlimited.
2. **Engineered modules keep their engineering on transfer** — they only lose it on sale.
3. **One ship, two FSDs:** one long-range engineered, one SCO. Swap in minutes at the hangar.
4. **No new hull purchases before ~500M CR.**
5. ~~Target fleet: Mandalay (exploration/exobiology) · Type-9 (cargo, colonisation) · Type-11 + Rhino
   (mining) · combat Clipper (merits).~~ **Superseded 19 Sept by rule 6.**
6. **Gutamaya only (decided 19 Sept 2026).** She flies Gutamaya hulls exclusively — Imperial Eagle /
   Courier / Clipper / Cutter, Gutamaya Corsair. Non-Gutamaya hulls (Asp, Type-9) are **stored, not
   sold** (rule 1). She works mainly for Aisling Duval; the exception is trips to farm G5
   materials/data/components to engineer the Gutamaya fleet. Consequences: Type-11 + Rhino and
   Mandalay are shelved as *her* hulls (no Gutamaya hull carries a Rhino) — **one story exception,
   decided 19 Sept:** for missions that need surface mining, a Type-11 + Rhino may enter the fleet as
   *someone else's ship, on loan* (`Guidelines.md`, Ch. III); some missions will be hard until each
   hull is properly engineered — that is intended. Story reason: `Guidelines.md`, Through-Line,
   Ch. III. Fleet plan and engineering work order: §13.

---

## 4. CURRENT OPERATION — THE EGA COMMUNITY GOAL

**CLOSED — 18 September 2026, journal-verified.** Final result below; this section is now historical
except where noted. See §11 for what replaces it as the active roadmap.

**"Wreaken Calls for Sourced Materials for Output Comparison Tests"** — ended **17 September 2026**.

- **Location:** Metz Enterprise, **Ega** system — Coriolis, **5,394 Ls** from the arrival star, large platform
- **Commodities:** palladium, gold, silver, bertrandite, indite, gallite, coltan, uraninite, lepidolite, cobalt, rutile, water — **bought at a nearby market**, not mined
- **Multiplier:** ×3 on sale price
- **Participation rewards:** Type-11 Umbra Red livery, Rhino Excavation Precision-Red livery, Vodel decal, credits by tier

**Credit tiers**

| Bracket | Contributions | Reward |
|---|---|---|
| Top 10 | ~90,878 – 163,060 | 200M CR |
| Top 25% | ~10,566 – 90,877 | 155M CR |
| Top 50% | ~3,712 – 10,565 | 110M CR |
| Top 75% | ~1,124 – 3,711 | **90M CR** ← target |
| Top 100% | ~1 – 1,123 | 35M CR |

**Plan adopted**
1. Sign up for the CG at Metz Enterprise **before** any sale.
2. Cubeo → Ega run **empty**: ~200 ly, i.e. 8–9 jumps at 26.49 ly.
3. Buy at a market near Ega, sell at Metz Enterprise. Local shuttle run.
4. **2 to 3 runs of 758 t** → 90M tier. Don't aim higher (the next tier needs 14 runs).
5. Expected trade profit on top: roughly 75–80M per full load on palladium (~104,000 CR margin/ton). **Check live prices on Inara before departure.**

**Actual execution (log)**
- **14 Sept, Day 3:** deviated from the plan above — flew the **Asp** to Ega solo (4–5 jumps at
  ~43 ly unladen, not the Type-9's 8–9), then paid for a **ship transfer** to bring `ON-16T` out
  from Medupe City rather than flying it there manually. Signed on to the CG first, as planned.
- **Open on arrival:** Asp shows a **Hostile** tag in Ega with no traceable cause (no bounty, no
  bond, no known faction conflict, no prior visit on record) — investigate before the first
  supply run, not after. Possible connection: Powerplay standing with Aisling Duval never
  lapsed (see `characters.md`, Viscountess sheet) — worth checking whether Ega's controlling
  faction is hostile to that Power specifically.
  - **15–16 Sept — plausible mundane explanation surfaced:** the Ega-area trading loop put the
    Type-9 in reputation contact with **Beyond Infinity Corporation**, a minor faction reported
    as aligned with **Edmund Mahon** (Alliance Prime Minister of Colonia, an independent Power
    outside Aisling's ZYADA bloc — see `Galaxy Chronicles.md`). Standard Powerplay behaviour: a
    system leaning toward a rival Power can flag a commander pledged elsewhere as hostile on
    sight, independent of any bounty/bond. **Not yet confirmed** — check Ega's controlling
    faction and current Power-conflict state on Inara before treating this as closed. (Keeping
    the mystery open in the narrative doc regardless — this is a technical note, not a verdict.)
- **15 Sept:** ran the CG loop plus independent Gold trading — Ega → **Scorpii Sector PI-T B3-4**
  (Zolloz City), 4 round trips, ≈300M CR. Two interdictions, both evaded without incident. Type-9
  confirmed hard to thread into narrow starport approaches — worth a note for any future large-hull
  purchase (Panther Clipper Mk II, Type-11) re: station compatibility. Hostile flag had no gameplay
  effect on trading access.
- **16 Sept:** continued Gold trading, Ega → **Crucis Sector OY-R B4-1** (Sukarno Horizons), ≈300M
  CR more — crossed the threshold for the **Trader Elite** rank. Reputation with **Beyond Infinity
  Corporation** reached Allied as a side effect of the trade volume.
- **16 Sept — Powerplay (journal-verified):** `Powerplay` event confirms Power=Aisling Duval,
  Rank=**0**, Merits=**0**, TimePledged≈6.8 days. Allegiance is genuinely live (not lapsed), but at
  rank 0 with no merits banked this cycle — consistent with §7's note that the 5 gating missions
  haven't been run yet. Doesn't resolve the Hostile-tag question either way.
- **16 Sept — CG result (journal-verified, CGID 859, matches this section):** `PlayerContribution`
  **6,822** units, `PlayerPercentileBand` **50** → **Top 50% bracket, 110M CR**, beating the 90M
  target. CG closes **17 Sept 11:00 UTC** — still technically open, so this could still climb if
  more is contributed before expiry. The original buy-near-Ega/sell-at-Metz-Enterprise plan and
  the Gold-trading log above are **the same activity**: gold is on the CG's commodity list (§4),
  so the "regular" trading was contributing to the CG the whole time.
- **Also found — a second, already-closed CG** (CGID 856, "Wreaken tests its new mining rig,"
  expired 10 Sept, not previously logged here): `TierReached` Tier 5, 50M CR bonus tier. Predates
  this session's narrative window; noting it for the treasury trail, not for the Logbook.
- **16 Sept — faction confirmation:** `Beyond Infinity Corporation` (see above) is in an active
  **Boom** economic state per the last `Docked` event — plausible knock-on effect of the trade
  volume passing through, worth keeping as a narrative detail if useful.
- **Lifetime trading stats (journal `Statistics` event, not session-scoped):** 835,108,663 CR
  total market profit, 26 markets traded with, highest single transaction 72,958,258 CR.
- **16 Sept, continued:** additional independent Gold runs beyond the CG contribution logged
  above — **Hannah Station** (49 Librae), **Eternal Flame Citadel** (Scorpii Sector WZ-P a5-1),
  **Violet Ann Memorial** (Scorpii Sector QT-R b4-0). Combined with the runs already logged this
  session, total trading profit for 16 Sept alone now exceeds **1 billion CR** — the treasury
  figure in §1 predates this activity and should be re-synced from the journal next session.
- **16 Sept — notable interdiction:** a persistent NPC pirate, callsign broadcast as **"Paladin"**
  (Cobra Mk III), pursued the Type-9 from Violet Ann Memorial back to Ega across multiple
  interdiction attempts, no hull damage taken. Logged here as a recurring-antagonist candidate for
  the narrative (see `characters.md`, "The rival").
- **17 Sept — one more gold run (journal-verified):** Violet Ann Memorial → Metz Enterprise, 758 t
  bought at 44,839 CR/t (33,987,962 CR out), sold at 141,339 CR/t (107,134,962 CR in) — net
  +73,147,000 CR. `CommunityGoal` (CGID 859, last read 06:54 UTC) confirms this run pushed
  `PlayerContribution` to **15,918** units and `PlayerPercentileBand` to **25** —
  **corrects the pre-session expectation of a 50% finish: this is a Top 25% result.** The
  in-journal live `Bonus` field for that band reads **170,000,000 CR** (higher than §4's static
  155M table estimate — CG reward scaling is dynamic and moves with total participation, not
  fixed). CG closes **17 Sept 11:00 UTC**; it was still open at session end (`Shutdown` 06:57 UTC,
  docked at Violet Ann Memorial), so payout hasn't posted yet and the band could still shift a
  little before expiry — but this is comfortably clear of the 90M target either way.
- **17 Sept — treasury resync (journal-verified, supersedes the 16 Sept snapshot in §1):**
  `LoadGame` 1,587,955,063 CR at session start + this run's net profit − refuel cost =
  **1,661,101,632 CR**. The 782M figure previously in §1 predated the bulk of 16 Sept's gold
  trading, as already flagged there.
- **17 Sept — stated plan for the next session:** fly the Type-9 from Violet Ann Memorial back to
  Metz Enterprise (Ega) to close out the CG properly, swap the active ship to the **Asp Explorer**
  at Ega, fly the Asp back to Cubeo, then regroup the whole fleet at Medupe City and start working
  the upgrade checklists (§2, §11) — treasury now clears Ground Rule 4 many times over, so nothing
  in the recommendation below is money-gated anymore.
- **18 Sept — CG closed, final result (journal-verified):** docked at Metz Enterprise 07:18:29 UTC;
  the `CommunityGoal` read moments later confirms **CGID 859 `IsComplete: true`**, final
  `PlayerContribution` **15,918**, `PlayerPercentileBand` **25** — the **Top 25% bracket** stands as
  the definitive result (supersedes the 17 Sept 50%-band expectation). `CommunityGoalReward` fired
  at 07:18:48 UTC for **170,000,000 CR** — exactly the live `Bonus` figure already spotted 17 Sept,
  confirming the payout held steady into close. The older CG (CGID 856, "new mining rig," Tier
  5/50M) is unchanged from the 16 Sept note — already resolved before this session.
- **18 Sept — fleet regrouped at Medupe City (journal-verified):** swapped to the Asp at Metz
  Enterprise (`ShipyardSwap`, 07:19:32), flew Ega → Cubeo (5 jumps, ~43 ly/jump unladen), docked
  Medupe City 07:29:52. `ShipyardTransfer` brought the Type-9 home the same session (§2.4). Combat
  and mining Clippers were already in storage there — **all four hulls now sit at the same station
  for the first time this campaign.**
- **18 Sept — Tritium supply mission, Prismatic Imperium (journal-verified):** picked up
  `Mission_Collect_Industrial` at Medupe City (72 t Tritium, offered reward 8,190,042 CR, expiry 19
  Sept), swapped into the **combat Imperial Clipper** for the run (§2.2 — 440 m/s boost), bought 128
  t Tritium at **Cellarius Beacon** (Tucanae Sector CG-W b2-0, 50,118 CR/t), delivered 72 t at
  Medupe City. Actual `MissionCompleted` reward: **3,380,042 CR + 12× Antimony**, plus
  **Reputation ++** and **Influence ++** with Prismatic Imperium. No interdiction logged on the
  round trip — clean run both ways, ~15 minutes undock to dock. Sold the 56 t leftover Tritium
  locally afterward for **+3,016,048 CR**. The Antimony batch is tied in-session to an
  outfit-upgrade checklist noted on Roskam's workbench — raw material for a future `Logbook.md` day,
  not yet drafted (see `characters.md`, Roskam sheet, and `Guidelines.md` §"Recurring Characters:
  the old mechanic of Hangar 12").
- **18 Sept — Asp refit, first pass (journal-verified, see §2.1):** stripped both missile racks, all
  four beam lasers and both shield boosters (**+1,341,400 CR** module sale); fitted heat sink
  launchers to all four tiny hardpoints (**−13,652 CR**). Bought an FSD (SCO) to test
  (**−5,971,625 CR**), judged the range loss too steep against the grade-4 engineered FSD's ~43 ly
  unladen range, and swapped back — the SCO is now in storage at Medupe City (free), the engineered
  FSD stays fitted.
- **18 Sept — treasury resync (journal-verified, supersedes the 17 Sept snapshot in §1):**
  `Status.json` reads **1,824,833,287 CR** at 08:31 UTC — cross-checked against `LoadGame`
  (1,661,100,215 CR) plus this session's transactions (CG reward, ship transfer, mission, trading,
  refit) to within 1,462 CR of the live balance; the small residual is an untracked minor fee, not a
  data error.

**Status update, 18 Sept:** points 1–2 of the recommendation below are now substantially executed —
see the refit log just above and §2.1/§2.2. Point 3 (first new-hull purchase) is still open; §11 now
carries the concrete next-session sequencing for it and everything else.

**Recommendation (requested 16 Sept — ship outfit upgrades)**
Treasury was 130M CR at session start (§1); the two Gold runs above add roughly **+600M CR** before
CG payout and expenses, which almost certainly clears **Ground Rule 4** ("no new hull purchases
before ~500M CR", §3). Can't give an exact figure without a current treasury read (see note on
Inara sync at the end of this file), but directionally:
1. **Cheap, high-value fixes first, regardless of exact balance:** Imperial Clipper (combat) FSD
   5E → 5A (~5M CR, §2.2) — this was already flagged as the best value upgrade in the fleet and
   costs a rounding error next to the CG profit.
2. **Asp "To fix" checklist (§2.1)** is now comfortably affordable in full: strip the missile racks
   and shield boosters, FSD grade 4→5, thrusters/power plant grade 1→5, AFMU, heat sink launchers.
   This was gated on money more than anything else.
3. **First new-hull purchase under Ground Rule 4** becomes a live option for the first time this
   campaign. Roadmap (§11, medium term) already names the targets: **Type-11 Prospector (67.86M
   CR)** is the cheapest and most immediately useful (mining role, SCO-optimised, frees the aging
   mining Clipper) — reasonable first pick. **Mandalay** (exploration/exobiology) is the other
   medium-term candidate but has no listed price here yet to compare against.
4. Hold off on the **Guardian FSD Booster** and **Fleet Carrier** — still long-term items per §11,
   no new information this session changes that.

---

## 4b. SESSION LOG — AISLING'S FIVE GATING MISSIONS (18 Sept, journal-verified)

Source: journal files of 18 Sept, 10:26–19:57 UTC (all times below UTC). **Result: Powerplay Rank
0 → 5, merits 0 → 16,424** — the `PowerplayRank` event (Rank 5) fired at 19:47:50, seconds after the
fifth mission paid out. Merits had been accruing the whole day while the rank stayed 0 (5,708 by
12:02, 9,401 by 14:07, 13,117 by 19:30), then posted at once: the §7 gating works exactly as
documented. Per-mission merit awards below are the round-number jumps in `PowerplayMerits`.

| # | Mission | Where | Ship | Merits | Notes |
|---|---|---|---|---|---|
| 1 | Rare material → unexploited system | **Karsuki Ti** (West Market: 18× Karsuki Locusts @ 915 CR, 10:37) → **HIP 7311** (Fan Base, unoccupied, 10:49) | Asp | +3,600 | Clean. |
| 2 | Ship scans, reinforcement | **HIP 3254** (Aisling Stronghold, heavy undermining) — nav beacon scan 11:18 | combat Clipper (ID 2) | +2,000 | First visit 11:12–11:24 (scan done). Second visit 14:20 after the refit below: shields dropped 14:23, hull 79.9% at 14:25 (`HullDamage`), shields back 14:26, jumped home 14:26. Pirates thick around the beacon. |
| 3 | Aisling Programme → undermine an exploited system | **Vargerson** (Browncoat Refuge; exploited by *A. Lavigny-Duval* + Aisling) — 15× `aislingpromotionalmaterials` collected at Cubeo 12:03, delivered 12:21 | combat Clipper (ID 2) | +3,600 | Route out via Ehlanda / Gliese 54.3 / Tehuenef, back via HIP 6616 / Kaukamal / Hernovacle. Easy. Note the irony: ALD is a ZYADA ally on paper (`Galaxy Chronicles.md`), yet this mission undermines her hold. |
| 4 | Rescue — wreckage / black boxes | **Lambda Hydri** (Hansteen Depot, pop. 2,490, exploited) | Clipper (first pass, 18:01) → **Asp** (from 18:38) | +2,800 | See mechanics below. Three more runs after the first hand-in. |
| 5 | Bounty hunting, reinforced system | **Chinovane** (pop. 2,133, exploited) — nav beacon, 19:42–19:48 | combat Clipper (ID 2) | +3,200 | Easier than expected; wanted pilots found by scanning at the beacon. Rank 5 posts here. |

**Rescue mission — how it actually works (no in-game briefing says this plainly):**
- There is **no mission board entry** — not from minor factions, not from the Imperial contact. It is
  wreckage collected in space and handed in.
- Go to a system **exploited by Aisling** where other Powers are more likely to contest it; use the
  **FSS** to find signal sources of Power-ship wreckage there.
- Recover the items with **collector limpets**; take care with **black boxes** — the authorities
  jump in quickly to check on arrivals.
- **Hand-in must be to the Imperial contact in the same system** where the items were found. Hansteen
  Depot has **no large pad**: the Clipper (large) cannot dock, so the Asp is the right hull for this
  job. Fitted for it 18:32–18:35 (collector limpet controller 3A, §2.1).
- Solved by watching other players' videos; worth keeping this paragraph so it isn't rediscovered.

**Combat Clipper refit between the two HIP 3254 visits (§2.2):** multi-cannon turrets, chaff and a
module reinforcement went in at 12:06–12:11, after the first visit. The journal logs no damage on
that first visit; the only `HullDamage` is on the second (see the discrepancies just below).

**Discrepancies between the session notes and the journal — all settled 19 Sept:**
- *"Lambda Hybris"* was a typo for **Lambda Hydri** (confirmed).
- The journal's order stands (confirmed): **scans first** (11:18, +2,000 merits), refit second
  (12:06–12:11), the only logged combat damage on the **second** HIP 3254 visit (79.9% hull at the
  logged hit, not the remembered 66% — `HullDamage` logs the first hit, not necessarily the worst).
  The session notes were written quickly; the Inara/journal record is authoritative.
- Burst lasers were never fitted, and the combat Clipper's FSD 5A predates 18 Sept: see §2.2.

**Raw material for future `Logbook.md` days** (real play, not yet drafted): falling out of power in
the combat Clipper during a pirate engagement — the "what it cost me" of a bad power-distribution
policy; the Clipper's speed as the escape; wreckage and black boxes recovered from other pilots'
dead ships, handed to a stranger on a pad the Clipper wouldn't fit; a second, easier bounty run
that ends with the rank arriving unannounced.

---

## 5. THE SETTING — CUBEO

Imperial system, **10.02 billion inhabitants**, agriculture/industry economy, Patronage government, controlling faction **Prismatic Imperium**, high security, **scoopable class F** star. Powerplay HQ of Aisling Duval.

**Orbital ports**

| Station | Type | Distance |
|---|---|---|
| Medupe City | Orbis | 332 Ls |
| Adelman Station | Orbis | 425 Ls |
| Chelomey Orbital | Coriolis | ~734 Ls |
| Weaver Vision | Orbis | ~1,103 Ls |
| Whittle Orbital | Outpost | ~1,904 Ls |

**Surface ports** — all ~735 Ls, faction *Cubeo Patron's Principles* (≠ Prismatic Imperium)

- Finch Beacon
- **Lubbock Penal colony**
- Roskam Enterprise

Plus **4 Odyssey settlements** in the system (on-foot training ground) and over 100 Fleet Carriers in orbit.

**Services at Medupe City:** shipyard, outfitting, commodities market, Apex Interstellar, bar, contacts, crew lounge, **Frontline Solutions**, missions, Pioneer Supplies, refuel/repair, **Search & Rescue**, **system colonisation contact**, Tuning, Universal Cartographics, **Vista Genomics**.

Everything fits in a single station. No need to leave Cubeo before Chapter II.

---

## 6. WHAT CHANGED DURING THE ABSENCE

- **Thargoid war over.** Cocijo, the last Titan, destroyed at Sol in December 3310. Reconstruction since.
- **Powerplay 2.0** (Oct 3310): merits earned through normal play, 100 cumulative ranks, exclusive modules.
- **Colonisation** (Trailblazers, March 3311): claim an uninhabited system within 15 ly of an inhabited one, ~25M CR, beacon deployed via the Colonisation Suite, permanent **Architect** status, tax collected.
- **FSD SCO:** supercruise overcharge, intra-system travel times cut by 3–4×.
- **Operations** (30 June 3312): 1–4 CMDR co-op scenarios, on foot and in ship, launched from any dock. *Mercenary* and *Powerplay* modes. Rewards: credits, both ship **and** on-foot materials, merits, **Merc Coin** (cap 9,999, 1,000/week).
- **Surface mining** (2 Sept 3312): **Rhino** SRV, 6 autonomous drills, DSS detecting planetary mining sites. New resources: magnesite, rubidium, bastnäsite, deuterium.
- **New hulls:** Python Mk II, Type-8, Mandalay, Cobra Mk V, **Gutamaya Corsair**, Panther Clipper Mk II, Type-11 Prospector (**67.86M CR**, medium platform, SCO-optimised), Caspian, Kestrel Mk II, Lynx Highliner, Nomad.
- **Rhino:** requires a **large planetary hangar Mk II** → Caspian Explorer, Panther Clipper Mk II or Type-11 Prospector only. Not the Clipper, not the Keelback.

---

## 7. POWERPLAY — AISLING DUVAL

- Reinstate allegiance from any station.
- **The 5 initial missions are gating**: rank 0 until they're done, even with merits already accumulated.
  **Confirmed in play, 18 Sept:** all five done (§4b) — rank jumped 0 → 5 on completion of the fifth,
  with 16,424 merits banked by then.
- Merits earned through almost any activity in ducal territory. Progress is **cumulative, never lost**. 100 ranks.
- All Powers grant access to the same 12 modules; only the unlock order differs. Aisling unlocks the **Prismatic Shield Generator** first.
- **Aisling's perks: +200% Search & Rescue payouts and +100% minor faction reputation gain, within ducal territory.**

**Key synergy:** the +100% reputation gain directly speeds up the Viscount → Duke climb (section 8), and the +200% S&R payout gives real value to the rescue limpet controller already fitted on the Asp.

---

## 8. IMPERIAL RANK — TARGET: CUTTER

Remaining: **Count → Earl → Marquis → Duke**. Duke rank unlocks the **Imperial Cutter**.

Method: rank up to **Allied** with an Imperial faction in a dense system → "Imperial Navy" missions start appearing on the board → stack them. Ranks are never lost. One rank per session, in parallel with merit grinding.

Recommended stepping stone: **Gutamaya Corsair**, medium Imperial multi-role.

---

## 9. ON-FOOT MISSION PROTOCOL (Odyssey)

Root cause of past failures identified: **the permission system**. Every door and terminal requires level 1, 2 or 3 access, obtained by **cloning an NPC's profile with the Profile Analyser**. Without it, every access attempt is a break-in → alarm → hostile settlement.

**Base loadout:** **Maverick** suit (not Dominator), Profile Analyser, E-Breach, Energylink.

**Progression**
1. **Abandoned settlement reactivation** missions — zero NPCs, zero alarms. Find the power distribution centre, insert the regulator. Learn the layout + gather micro-resources.
2. **Data recovery** missions at powered-down sites.
3. **Cut the reactor** at an active settlement = alarms, lights and turrets offline. Master key for any infiltration.
4. **Land more than 1 km away**, or arrive by Apex taxi. A ship landed inside the settlement triggers a scan, then hostility.
5. **Frontline conflict zones** before any on-foot bounty hunting: allies nearby, respawn at the dropship, failure costs nothing.

---

## 10. ENGINEERING

Three ship-side stocks: **raw** · **manufactured** · **encoded**. Plus, separately, Odyssey **micro-resources**.

- Farms: **HGE** in boom-state systems (high-grade manufactured) · brain trees / crystalline shards (raw, in bulk) · abandoned settlements (micro-resources, no opposition).
- **Material traders:** 6-for-1 upward conversion. Farm volume, convert afterward.
- **3312 shortcut:** Operations reward both ship **and** on-foot engineering materials, and Merc Coin buys modules and **engineering blueprints**.
- Priorities: Farseer (FSD) · Martuuk · McQuinn or Nemo (weapons) · Qwent (power plant) · Vatermann (shields). Odyssey: Oden Geiger (data), Hero Ferrari (suit), Terra Velasquez.

---

## 11. ROADMAP

**Immediate — done, 18 September**
- [x] Sign up for the CG at Metz Enterprise
- [x] 2–3 runs of 758 t — Top 25% bracket reached (journal-verified, §4)
- [x] Close out the CG at Metz Enterprise (170M CR paid, §4)
- [x] Swap to the Asp at Ega, fly it back to Cubeo, regroup the whole fleet at Medupe City (§2.4, §4)
- [x] Strip the Asp's weapons + shield boosters, fit heat sink launchers ×4 (§2.1)

**Immediate — updated 19 Sept**
- [x] FSD 5A on a Clipper — **done on the mining Clipper**, 18 Sept 12:38 UTC (§2.3). The combat
      Clipper already had an engineered 5A (Faster Boot g5) — the old "critical issue" was stale (§2.2)
- [x] Check power priorities on the Asp — no problem observed, closed (§2.1)
- [ ] **Power distribution policy on the combat Clipper** — lost power mid-fight at HIP 3254 (§4b).
      Review the priority groups (weapons/shields/thrusters/FSD) before the next combat sortie

**Short term — the "first steps back" arc**

Treasury clears Ground Rule 4 many times over (§3) — nothing below is money-gated. Sequenced,
roughly one block per session:

1. [x] **Reinstate Aisling Duval allegiance** and run the **5 gating missions** (§7) — **done 18
       Sept**: Rank 5, 16,424 merits (journal-verified, §4b). The allegiance never needed
       reinstating — it had never lapsed.
2. [ ] **First on-foot excursion** — one **abandoned-settlement reactivation** mission, on one of
       Cubeo's 4 Odyssey settlements (§9 step 1: zero NPCs, zero alarms, lowest possible risk).
       First boots on the ground since the coma; a natural low-stakes way to "find the reflexes
       back" before anything harder.
3. [ ] Follow up with a **data recovery** mission at a powered-down site (§9 step 2), same or a
       second settlement — banks Profile Analyser clones and on-foot materials without combat risk,
       and starts the engineering material stockpile (§10).
4. [ ] ~~Finish the rest of the Asp refit (§2.1)~~ — **superseded 19 Sept**: the Asp is stored under
       rule 6 (§3). Engineering effort goes to the Gutamaya hulls instead (§13).
5. [ ] Push reputation with one Imperial faction in a dense system to **Allied** (Aisling's +100%
       rep-gain perk applies in ducal territory, §7) — this is what makes Imperial Navy missions
       start appearing on the board (§8).

**Medium term**
- [ ] Only once steps 2–3 above have gone cleanly: attempt a **cut-the-reactor** infiltration at an
      *active* settlement (§9 step 3) — the first real on-foot risk taken, deliberately not before
      confidence is re-established.
- [ ] Unlock the **Prismatic Shield Generator** — Aisling's first Power module (§7)
- [ ] Farseer (Deciat): FSD grade 4 → grade 5 — was the Asp's; now retargeted at a Gutamaya hull (§13)
- [ ] Vatermann / Qwent visits (shields, power plant) once material stock allows (§10, §13)
- [ ] ~~**Type-11 Prospector** (67.86M CR) + Rhino~~ — **shelved 19 Sept** (rule 6, §3) *except as a loaned hull, when a mission needs a Rhino*. First new hull
      purchase is now a Gutamaya one: Courier or Corsair (§13)
- [ ] Stack Imperial Navy missions toward **Count → Earl → Marquis → Duke** (§8)
- [ ] ~~**Mandalay** (migrate the grade-5 DSS and the FSD once acquired)~~ — **shelved 19 Sept**
      (rule 6); the DSS and FSD migrate to a Gutamaya hull instead (§13)
- [ ] **Guardian FSD Booster** once the FSD is grade 5 — target 55+ ly (§2.1)
- [ ] **Duke rank → Imperial Cutter** (§8)

**Long term**
- [ ] Claim a system and Architect status, on the Imperial frontier
- [ ] Fleet Carrier
- [ ] Deep-space expedition / exobiology

**Deliberately not on this list:** no trip to **LHS 3447**. It's her departure system, currently
Fortified under Yuri Grom with no rival Power contest live (checked 18 Sept, `Galaxy Chronicles.md`)
— routing a supply, explo, or CG run through it by accident would spend a beat that isn't due for a
while. Two candidate reasons for an eventual deliberate visit are on record (`Guidelines.md`,
Through-Line Ch. VIII) — neither is a live trigger yet. Plot a wide berth around it until one is.

---

## 12. TOOLS

| Tool | Use |
|---|---|
| Inara | Database, live CGs, trade routes, engineers |
| EDSM | Cartography, stations, history |
| Spansh | Exobiology, material, cargo and neutron routes |
| Coriolis / EDSY | Builds before purchase |
| ED Colonisation Planner | Build order for a system |
| EDMC / EDDiscovery | Automatic journal upload, Inara sync |

**Inara note:** only the active ship reports in if the Frontier account link has expired. Relink the account in settings, or pull each hull out of the hangar once with EDMC running.

---

---

## 13. THE GUTAMAYA PROGRAMME (rule 6, decided 19 Sept 2026)

Technical plan only — the story reason lives in `Guidelines.md`, Through-Line, Ch. III. **Hull specs
and rank gates below are from memory and unverified — check Coriolis/EDSY and the in-game shipyard
before buying anything.**

| Role | Hull | Status | Note |
|---|---|---|---|
| Combat / merits | Imperial Clipper `MA-10E` | owned | FSD engineered, everything else stock (§2.2) |
| Mining | Imperial Clipper `MA-04E` | owned | nothing engineered (§2.3); no Rhino on any Gutamaya hull |
| On-foot settlement work (taxi and escape) / piracy | Imperial Courier | to buy | revised 19 Sept: its edge is **speed, boost and the best base shields of any small ship** — settlement-hopping and a fast getaway when a site turns hostile — *not* stealth. Land >1 km away (§9 step 4); the ship is the exit, not the infiltration tool. Web sources; unverified in-game |
| Multi-role / trading / medium-pad jobs | Gutamaya Corsair | to buy | the §8 stepping stone; would also cover the Lambda Hydri-type jobs the Asp did |
| Heavy bounty hunting ("tank") | Imperial Cutter | **needs Duke** (§8) | Tonton Marcel's build: flight assist off, flipping, beam turrets + corrosive-shell multi-cannons |
| Long-range exploration + exobiology | Gutamaya Corsair (revised 19 Sept — was "Courier, for steep terrain") | to buy | Stratum Tectonicas-type species live on **flat ground** (thin CO₂/NH₃/SO₂ atmosphere, ≥165 K, up to ~0.6 g), so the Courier's steep-terrain agility isn't needed. Web sources: many internal slots (one each size 1–4, three each of 5 and 6), SCO-optimised, community exploration builds reported around 50 ly with a Guardian booster — **unverified in-game**, and the rank gate still unchecked |

**Stored, not sold:** Asp (grade-5 DSS and grade-4 FSD to migrate) · Type-9.

**Courier as a long-range hull — research, 19 Sept (web sources, not checked in-game):** a heavily
engineered Courier is reported at about **45.5 ly**; 50 ly would need everything at once. Levers:
FSD engineering (*Increased Range* g5, Deep Charge-type experimental), stripping weight, and a
**Guardian FSD Booster** — a *flat* bonus by size (about +10 ly at class 5), so it helps small hulls
most, but is limited by the Courier's largest optional slot. Unlocking it means a long Guardian-site
materials grind at a Guardian Tech Broker. The real limit is **optional slots**: fuel scoop (needed for
neutron supercharging) + booster + AFMU leaves little else. **Neutron stars:** supercharging
multiplies the *next* jump range by 4 (capped by the FSD's max fuel per jump) at about 1% module
damage per jet; an AFMU is standard kit — repair before integrity falls under ~90%. Before committing,
build it in Coriolis/EDSY and read the real slot sizes.

**Decision, 19 Sept (Tonton Marcel): long jumps and exobiology go to a larger Gutamaya hull, most
likely the Corsair** (its slot count answers the scoop + booster + AFMU squeeze above); the Courier
stays a specialist for infiltration and piracy, with neutron-boosted range as a bonus.

**Engineering work order (from the 19 Sept SLEF exports):** the only engineered modules across the
four hulls are the two Lakon FSDs, the Asp's DSS/power plant/thrusters (g1), and the combat Clipper's
FSD. Both Clippers have stock weapons, shields, distributors and thrusters. Order of work, per §10's
engineer list: FSD range (Farseer) → shields and power plant (Vatermann, Qwent) → weapons
(McQuinn/Nemo) → thrusters/distributor. Blueprints per hull to be fixed once each role is settled;
this is the "side roadmap" of material farming and engineer visits that gives Ch. IV its shape.

**Open:** whether a farming trip may use a non-Gutamaya hull (e.g. mining) or only a non-Aisling
employer. Default until decided: the exception covers *who she works for*, not what she flies.

---

*Last updated: 19 September 2026 (journal of 18 Sept read through 19:57 UTC; Inara SLEF exports of all four hulls, 19 Sept). To be completed session by session.*

**Data source note:** the game writes local Journal files (`%USERPROFILE%\Saved Games\Frontier
Developments\Elite Dangerous\`) on this machine as you play — plain JSON-lines, one event per
line (`LoadGame`, `Rank`, `Progress`, `Reputation`, `Powerplay`, `CommunityGoal`, `MarketSell`,
`Statistics`, etc.). Everything marked "journal-verified" above was read directly from today's
files, no API or login involved. This is the preferred source going forward — more accurate than
memory, no setup, no credentials. Two fallbacks exist if the journal ever isn't available (e.g.
working from a different machine): **(a)** a public Inara CMDR profile page can be read directly
if you share the URL — one-off, no API key needed; **(b)** Frontier's own Companion API would give
the same data but requires OAuth login with the actual game account, which isn't something worth
setting up for this — Frontier has also long restricted new API client registrations. The journal
folder makes both unnecessary while this session's machine is the one being played on.
