# 📖 How to study with Claude (and keep everything in the repo)

A repeatable loop: **study a topic with Claude → save the session → the repo
remembers it forever.**

---

## Setup (once)

```bash
cd "C:\Users\palya\Desktop\interview prep\ai-engineer-interview-prep"
pip install python-docx      # only dependency, for the Word cram sheet
```

Always open Claude Code **from inside this folder** so the `/study` and
`/save-session` commands and the file paths line up.

---

## The daily loop

### 1. Start a session
Type one of:
```
/study Day 28
/study attention mechanism
/study SD-1            (a system-design problem)
```
or just talk: *"teach me chunking strategies for RAG"*, *"mock interview me on the news feed design"*.

Claude will: explain from first principles → check your understanding with
questions → push back like an interviewer → give you the crisp version at the end.

### 2. End the session
Type:
```
/save-session
```
Claude then, from the conversation that just happened:

1. **Writes a notes file** → `notes/Day-28_Attention-Mechanism.md`
   (or `system-design/SD-01_URL-Shortener.md`) using `notes/_TEMPLATE.md`.
2. **Appends the crispest 5–10 lines** to `Interview-Cram-Sheet.md` under the right
   heading, replacing that topic's `⏳` placeholder.
3. **Rebuilds** `Interview-Cram-Sheet.docx`.
4. **Logs the session** → adds a row to `study-log.csv`.
5. **Refreshes the dashboard** → `python scripts/update_progress.py` regenerates the
   streak graph + stats + session log, and ticks the checkbox in `PROGRESS-DASHBOARD.md`.
6. **Commits** everything with a message like `study: Day 28 — attention mechanism`.
   (Push with `git push` when you want it on GitHub.)

### 3. Check progress any time
Open [PROGRESS-DASHBOARD.md](PROGRESS-DASHBOARD.md).

---

## Doing it manually (if you're not using the slash commands)

```bash
# after writing/adding a notes file and editing the cram sheet:
python scripts/update_progress.py --log "Day 28" "Attention mechanism" 75 notes/Day-28_Attention-Mechanism.md
python scripts/build_cram_docx.py
git add -A && git commit -m "study: Day 28 — attention mechanism"
```

`--log` appends today's date automatically. Omit it and just run
`python scripts/update_progress.py` to regenerate the dashboard from the existing CSV.

---

## File map

| File / folder | What it's for | Who edits it |
|---|---|---|
| `PROGRESS-DASHBOARD.md` | streak graph, stats, checklist of all 84 items | you tick boxes; script writes the AUTO blocks |
| `Interview-Cram-Sheet.md` | **the day-before-interview file**, densest form | grows one topic per session |
| `Interview-Cram-Sheet.docx` | Word version of the above, for reading on any device | generated — never hand-edit |
| `notes/Day-XX_*.md` | full notes for one topic: mechanism, Q&A, gotchas | one per study session |
| `system-design/SD-NN_*.md` | **reference solution + Mermaid architecture diagram** for each of the 20 problems (pre-written); your mock-round notes get appended at the bottom | you append via `/save-session` |
| `system-design/README.md` | index of all 20 solutions + the AI variants | — |
| `study-log.csv` | one row per session (date, topic, minutes) | append-only, script + `--log` |
| `scripts/update_progress.py` | regenerates dashboard streak/stats/log | run it, don't edit output |
| `scripts/build_cram_docx.py` | `Interview-Cram-Sheet.md` → `.docx` | run after cram-sheet edits |
| `.claude/commands/` | the `/study` and `/save-session` command definitions | rarely |

---

## Streak graph legend

```
· none   ░ <45 min   ▒ 45–89 min   ▓ 90–134 min   █ 135+ min
```
Grid is days-of-week (rows) × weeks (columns), like GitHub's contribution graph.
It starts on 2026-08-31 and extends to the current week automatically.

---

## Tips

- **One topic per session** keeps notes files clean and the streak honest.
- If you revisit a topic, `/save-session` **updates** the existing notes file and
  bumps its date rather than making a duplicate.
- Before an interview: read `Interview-Cram-Sheet.docx` top to bottom, then reread
  only the `🔴`/`🟡` confidence notes files.
- `/study` a system-design problem = full mock round; Claude plays interviewer.
