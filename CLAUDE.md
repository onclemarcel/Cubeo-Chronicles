# CLAUDE.md
## Operating manual — Cubeo Chronicles

> This file is loaded automatically at the start of every session. It documents how this project
> works between sessions — not the story, not the rules of craft, not the stats. Those live in the
> files listed below. Read this first; read the others as the work in front of you requires them.

---

## 1. What this is

A collaborative fanfiction project set in Elite Dangerous: CMDR Onclemarcel (Marcella Delavalette,
Viscountess of the Empire) is writing an in-character logbook after waking from a four-year coma,
built on real 2026-session gameplay and real Elite Dangerous canon. Tonton Marcel plays the game
and reports back; Claude turns the reports into prose, keeps the supporting documents consistent,
and proposes plot material drawn from real Galnet/game events.

## 2. File map & boundaries

Each file states its own scope at its own top; restated here for a quick reference:

| File | Contains | Never contains |
|---|---|---|
| `Logbook.md` | The story itself — prologue, chapters, dated entries, in her voice | Stats, builds, roadmaps |
| `In-Game Operations.md` | Fleet status, CMDR stats, in-game goals, roadmap/tasks, session logs not captured in the story — technical, no narrative | Prose, character interiority |
| `Guidelines.md` | Narrative craft: style manual, entry format, recurring motifs, through-line, character-writing rules | In-game notes, stats, Numeric/technical data, prose |
| `Galaxy Chronicles.md` | Canon bedrock — real Elite Dangerous dates, events, real people available for use | Invented characters, invented events |
| `characters.md` | Character sheets (invented + real-person usage notes) | updated stats, prose |
| `Reviews.md` | **Ephemeral.** Tonton Marcel's session notes, tagged. Cleared once distributed — see §3 | Anything meant to last |

*(exception)* a `PLANNING NOTE — TEMPORARY` block at the top of a chapter in `Logbook.md` may be created to show "Where we stand on a chapter still being planned": decisions, workplan, questions waiting. **Delete it once the chapter is drafted** — it is the one place `Logbook.md` holds a roadmap.

## 3. How updates happen — the Reviews.md cycle

Tonton Marcel's input arrives two ways: 
  - in conversation for short updates or questions, or,
  - in `Reviews.md` with one or more tags per note, marking which file(s) it's mainly about. Known tags so far:

| Tag | Primary destination | Notes |
|---|---|---|
| `[IN-GAME]` | `In-Game Operations.md` (session log, roadmap, remaining tasks, goals) | Session logs are raw material for future `Logbook.md` days — real play, not yet fictionalised. Session logs are removed after use in the 'logbook.md' prose - ask Marcel for removing old session logs already implemented |
| `[NARRATIVE]` | `Logbook.md` | Two modes: **feedback** on existing prose (paragraph-by-paragraph notes to apply as edits), or a **request for new text** to be drafted. Read the note to tell which. |
| `[CONTEXT]` | Wherever the idea actually belongs — often 'Guidelines.md' but may touch several files at once when context deals with a new/updated plot/event or introduction of new characters and links with in-game logs | Background/worldbuilding ideas, open questions, story mechanics not yet prose |
| `[CHARACTER]` | `characters.md` | Two modes: **additive** (new material to fold in, may also feed `Logbook.md`), or **corrective** (may require checking whether already-written `Logbook.md` content needs to change for consistency) |
| `[GALNET]` / `[GALAXY]` | `Galaxy Chronicles.md` | Real Elite Dangerous info (news, events, game facts). May double as plot-brainstorming fodder — propose ideas in conversation; don't write invented plot into this file until Tonton Marcel picks one (this file is canon-only, see §2) |
| `[GUIDELINES]` | `Guidelines.md` | Clarifies *how* a `[NARRATIVE]` note should be interpreted or written — craft direction, not content |

**This list may grow.** If a new tag, or an ambiguous use of an existing one, shows up: make a
reasonable call about where it goes, apply it, and say so plainly in your reply rather than
silently guessing. Tonton Marcel will confirm or correct — fold the confirmed mapping back into
this table so the next session doesn't have to re-derive it.

**`Reviews.md` itself is not kept.** Once its notes have been read and distributed into the target
files, it gets cleared out — there is no changelog of Reviews.md itself, and none is needed.
Everything worth keeping must already be sitting in the destination file, dated (§4), before a
Reviews.md pass is considered "handled."

## 4. Durable record-keeping convention

Reviews.md and the conversation itself are not preserved, every file that changes as a
result of a session will be reviewed by Marcel and a new Github commit done when accepted.
After a cold-start (e.g. new conversation), take existing file as granted and accepted - check in previous
Github commits for change history of a file, where needed, or ask Marcel for any doubt or detected
inconsistencies:

- `characters.md` : No changelok. Additions are visible in Github Changelog over commited versions. Each character has a card, regularly updated and commited when accepted by Marcel
- `In-Game Operations.md` : No changelok. Additions are visible in Github Changelog over commited versions
  - This file is updated with the in-game logs history on each `Reviews.md` update.
  - Tasks done are removed from file while Marcel progresses in-game - session logs not yet incorporated in the prose (`logbook.md`) are kept in this file until taken into account or until explicit request from Marcel to remove it.
  - Roadmap is updated when needed, depending on [CONTEXT] inputs in `Reviews.md`
- `Logbook.md` — no changelog (it's prose), but structural changes of consequence (renumbering,
  cut paragraphs, moved scenes) are worth a one-line mention back to Tonton Marcel in the same
  reply, so nothing silently vanishes without him seeing it.
- `Guidelines.md` / `Galaxy Chronicles.md` — No changelok. Additions are visible in Github Changelog over commited versions

## 5. Starting a new session

1. Read this file (automatic).
2. If `Reviews.md` exists and has content: read it, route each tagged note per §3, apply the
   changes to the target files with record-keeping as per §4, confirm with Tonton Marcel, then clear
   `Reviews.md`.
3. **Check the game's own Journal files** before relying on numbers already in
   `In-Game Operations.md` — they're the ground truth and update as he plays, no API/login needed:
   `%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous\Journal.*.log` (plain
   JSON-lines; useful events: `LoadGame` for credits, `Rank`/`Progress`, `Reputation`, `Powerplay`,
   `CommunityGoal`, `Market{Buy,Sell}`, `Statistics`). Read the most recent file(s) by mtime, not
   by filename order. Only do this if the journal folder exists on the current machine — if
   working from elsewhere, fall back to what Tonton Marcel reports or a shared public Inara
   profile URL (see the data-source note in `In-Game Operations.md`).
4. Before writing or editing `Logbook.md` prose specifically, read `Guidelines.md` — it is not
   auto-loaded, and its rules (voice, pacing, the arc-of-the-hand, what never gets explained
   outright) are not optional.
5. For anything touching a specific character or the `logbook.md`, check `characters.md` first — sheets are living and
   may have moved since the last session touched them. Take current file as granted and accepted. Check in Github commits history in case of unresolved discrepancy (e.g. request for modifying a character while it does not exist at all in the `characters.md` file)
6. For anything touching real Elite Dangerous facts (dates, Powers, factions, canon events), check
   `Galaxy Chronicles.md` before inventing — the project's credibility rests on fiction never
   contradicting the real timeline (see its own "Golden Rule").

---

*This file describes process, not content. If unsure whether something belongs here or in
`Guidelines.md`: "is this about how we work, or about how the story should read?" — the first goes
here, the second goes there.*
