---
description: Persist the current study session — notes file, cram sheet, Word doc, streak log, commit
argument-hint: [optional: minutes spent, e.g. "75"]
---

Persist the study session that just happened in this conversation. Work from the
actual conversation above — do not invent content the user didn't engage with.

If no real study happened in this conversation, say so and stop.

## Steps

1. **Identify** the topic(s) covered and the matching item id(s) from
   `PROGRESS-DASHBOARD.md` (e.g. `Day 28`, `SD-1`). Estimate minutes spent
   (use `$ARGUMENTS` if given, else infer from the conversation depth, round to 15).
   Gauge the user's confidence: 🔴 low / 🟡 ok / 🟢 solid.

2. **Notes file** — `notes/Day-NN_Kebab-Topic.md` (curriculum) or
   `system-design/SD-NN_Kebab-Name.md` (system design):
   - If it already exists, UPDATE it (merge new understanding, refresh the date,
     keep history of what improved). Otherwise create it from `notes/_TEMPLATE.md`.
   - Fill every section from the conversation: TL;DR, core concepts, mechanism,
     the interview Q&A you actually did, gotchas the user hit, connections to other
     days, and the cram-sheet lines.

3. **Cram sheet** — edit `Interview-Cram-Sheet.md`:
   - Find the heading for this topic. Replace its `⏳ Fills in after…` line with
     5–10 dense bullets (the "Cram-sheet lines" from the notes file).
   - Keep it *terse* — this file is for panic-reading the day before an interview.
   - For SD problems, fill the matching row/summary in the System Design section.

4. **Rebuild the Word doc:**
   `python scripts/build_cram_docx.py`

5. **Log + dashboard:**
   `python scripts/update_progress.py --log "<item>" "<topic>" <minutes> <notes_path>`
   Then in `PROGRESS-DASHBOARD.md`:
   - Tick the checkbox for this item: `- [ ]` → `- [x]`, and append
     ` · ✅ YYYY-MM-DD · [notes](<path>)` to that line.
   - Bump the matching row in the "Completion" table.

6. **Verify:** re-read the changed region of `PROGRESS-DASHBOARD.md` and the cram
   sheet heading you edited. Confirm the streak grid rendered.

7. **Commit** (do not push):
   ```
   git add -A
   git commit -m "study: <item> — <short topic>"
   ```
   Tell the user it's committed and they can `git push` when ready.

## Output to the user
A 4–6 line recap: what was saved, files touched, current streak, and the single
most important thing to revisit next time.
