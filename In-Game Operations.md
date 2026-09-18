# OPERATIONAL GUIDE — CMDR ONCLEMARCEL
## Campaign memory — status as of 18 September 2026 (3312)

> Technical document. No narrative here — the story lives in `Logbook.md`.

---

## 1. COMMANDER SHEET

| | |
|---|---|
| CMDR | Onclemarcel |
| Inara role | Freelancer / Scientist |
| Squadron | EliteCommanders |
| Trade rank | **Elite** (Trader Elite badge earned 16 Sept 2026) |
| Imperial Navy rank | **Viscount** |
| Power | Aisling Duval — pledged, **Rank 0 / 0 merits** (~8.7 days pledged, journal-verified 18 Sept — still gated on the 5 initial missions, see §7, §11) |
| Home port | Cubeo — Medupe City |
| Treasury | **1,824,833,287 CR** (journal-verified, `Status.json` 18 Sept 08:31 UTC — `LoadGame` 1,661,100,215 + CG 859 payout 170,000,000 + this session's transfer/mission/trading/refit activity, reconciled to within 1,462 CR of the live balance; see §4) |
| Game mode | Solo |
| Expansions | Horizons + Odyssey |
| Absence | ~4 years (last memory: Thargoid war, Colonia CG) |

---

## 2. THE FLEET — STATUS AND WORK ORDERS

### 2.1 Asp Explorer — *exploration / rescue*

**Notable modules**
- FSD 5A — *Increased Range* **grade 4** + **Deep Charge** experimental effect → 43.08 ly unladen, 41.17 ly laden
- DSS 1I — *Expanded Probe Scanning Radius* **grade 5** (CG reward, irreplaceable)
- Fuel Scoop 6A
- Power Plant 5A *Armoured* **grade 1** / Thrusters 5A *Clean* **grade 1**
- Planetary hangar 2G, shield 5D, 20 t cargo
- **Rescue Multi Limpet Controller 3C** → latent Search & Rescue configuration

**To fix**
- [ ] Thrusters flagged `enabled: false` in the export — check power priorities in-game
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

### 2.2 Imperial Clipper — *combat / bounty hunting*

Shield 6A, thrusters 6A, distributor 6A, power plant 6C, gimballed beam laser 3C, multi-cannon 3C, chaff, ECM, 2 boosters, scoop 4A.

**Critical issue: stock FSD 5E.** Never replaced. A 5A costs ~5M — best value-for-money upgrade in the whole fleet.

**Future role:** Powerplay merit generator. **Do not sell.**

**18 Sept, journal-verified:** flown for the Tritium supply mission round trip (Medupe City →
Cellarius Beacon → Medupe City, §4) specifically for its 440 m/s top boost — no interdiction taken.
Repaired on departure (2,692 CR). Still on the stock FSD 5E; the 5A upgrade above remains open.

### 2.3 Imperial Clipper — *mining*

Cargo hold 7E (128 t), 3× collector limpet controllers 3A, prospector limpet controller 1A, refinery 2A, 2× mining lasers 2D, DSS 1I.

Eventually replaced by the Type-11 Prospector. Keep for now.

### 2.4 Type-9 Heavy — `ON-16T`

**758 t cargo · 26.49 ly · total value 130.7M CR · hull 76.5M**

Fully outfitted. **This was the CG ship** — CG 859 closed 18 Sept (§4), so the Type-9 is off active CG duty. Consider an FSD (SCO), class 6, next time it's in for outfitting.

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
5. Target fleet: Mandalay (exploration/exobiology) · Type-9 (cargo, colonisation) · Type-11 + Rhino (mining) · combat Clipper (merits).

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

**Immediate — still open**
- [ ] FSD 5A on the combat Clipper — still the best value-for-money upgrade in the fleet (§2.2)
- [ ] Check power priorities on the Asp — thrusters flagged `enabled: false` in the export (§2.1)

**Short term — the "first steps back" arc**

Treasury clears Ground Rule 4 many times over (§3) — nothing below is money-gated. Sequenced,
roughly one block per session:

1. [ ] **Reinstate Aisling Duval allegiance** (any station — already home at Medupe City) and run the
       **5 gating missions** (§7). Powerplay has sat at Rank 0 / 0 merits for ~8.7 days pledged
       (journal-verified, 18 Sept, §1) purely because these haven't been run yet — pure upside, no
       new risk.
2. [ ] **First on-foot excursion** — one **abandoned-settlement reactivation** mission, on one of
       Cubeo's 4 Odyssey settlements (§9 step 1: zero NPCs, zero alarms, lowest possible risk).
       First boots on the ground since the coma; a natural low-stakes way to "find the reflexes
       back" before anything harder.
3. [ ] Follow up with a **data recovery** mission at a powered-down site (§9 step 2), same or a
       second settlement — banks Profile Analyser clones and on-foot materials without combat risk,
       and starts the engineering material stockpile (§10).
4. [ ] Finish the rest of the Asp refit (§2.1): FSD/thrusters/power plant to grade 5, fit an AFMU.
5. [ ] Push reputation with one Imperial faction in a dense system to **Allied** (Aisling's +100%
       rep-gain perk applies in ducal territory, §7) — this is what makes Imperial Navy missions
       start appearing on the board (§8).

**Medium term**
- [ ] Only once steps 2–3 above have gone cleanly: attempt a **cut-the-reactor** infiltration at an
      *active* settlement (§9 step 3) — the first real on-foot risk taken, deliberately not before
      confidence is re-established.
- [ ] Unlock the **Prismatic Shield Generator** — Aisling's first Power module (§7)
- [ ] Farseer (Deciat): FSD grade 4 → grade 5 on the Asp (§2.1, §10)
- [ ] Vatermann / Qwent visits (shields, power plant) once material stock allows (§10)
- [ ] **Type-11 Prospector** (67.86M CR) + Rhino — retires the aging mining Clipper (§2.3); first new
      hull purchase of the campaign, easily affordable now
- [ ] Stack Imperial Navy missions toward **Count → Earl → Marquis → Duke** (§8)
- [ ] **Mandalay** (migrate the grade-5 DSS and the FSD once acquired)
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

*Last updated: 18 September 2026. To be completed session by session.*

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
