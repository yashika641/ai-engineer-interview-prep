# ai-engineer-interview-prep

My AI Engineer interview prep — a study system, not just notes.

**Study a topic with Claude → run `/save-session` → the repo permanently remembers
it** (structured notes, a crib sheet, a Word doc, and a GitHub-style streak graph).

## Start here

| I want to… | Open |
|---|---|
| See my progress + streak | **[PROGRESS-DASHBOARD.md](PROGRESS-DASHBOARD.md)** |
| Cram the day before an interview | **[Interview-Cram-Sheet.docx](Interview-Cram-Sheet.docx)** (source: [`.md`](Interview-Cram-Sheet.md)) |
| Learn the daily workflow | **[HOW-TO-STUDY-WITH-CLAUDE.md](HOW-TO-STUDY-WITH-CLAUDE.md)** |
| Read past topic notes | [`notes/`](notes/) · [`system-design/`](system-design/) |

## The loop

```
cd ai-engineer-interview-prep      # open Claude Code here
/study Day 28                      # interactive lesson + mock questions
/save-session                      # writes notes, updates cram sheet + streak, commits
git push                           # when you want it on GitHub
```

## Scope

- **60-day curriculum:** Python/SQL → ML → DL → LLMs → RAG → Agents → Backend/Prod
  → MLOps/System Design → Project grilling.
- **20 system-design problems** + 4 AI-specific variants (RAG serving, LLM serving,
  recommenders, agent orchestration).

## Setup

```bash
pip install python-docx
```
