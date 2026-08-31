"""
Regenerates the auto-managed blocks in PROGRESS-DASHBOARD.md from study-log.csv.

What it updates (only the text between the AUTO markers, nothing else):
  <!-- AUTO:STREAK -->      GitHub-style contribution grid (days x weeks)
  <!-- AUTO:STATS -->       current streak / longest streak / totals
  <!-- AUTO:LOG -->         the reverse-chronological session log table

Usage:
  python scripts/update_progress.py
  python scripts/update_progress.py --log "Day 28" "Attention mechanism" 75 notes/Day-28_Attention-Mechanism.md
      -> appends a row to study-log.csv (date = today) then regenerates the dashboard

study-log.csv columns:
  date (YYYY-MM-DD), item, topic, minutes, notes_file
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_CSV = ROOT / "study-log.csv"
DASHBOARD = ROOT / "PROGRESS-DASHBOARD.md"

# First column of the very first week shown on the grid. Keep it a Monday.
START_DATE = dt.date(2026, 8, 31)

LEVELS = [
    (0, "·"),      # ·   nothing
    (1, "░"),      # ░   1-44 min   (light)
    (45, "▒"),     # ▒   45-89 min  (one solid session)
    (90, "▓"),     # ▓   90-134 min (deep session)
    (135, "█"),    # █   135+ min   (marathon)
]
MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_rows() -> list[dict]:
    if not LOG_CSV.exists():
        return []
    with LOG_CSV.open(newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if r.get("date")]
    for r in rows:
        r["minutes"] = int(float(r.get("minutes") or 0))
    rows.sort(key=lambda r: r["date"])
    return rows


def append_row(item: str, topic: str, minutes: str, notes_file: str) -> None:
    today = dt.date.today().isoformat()
    new = not LOG_CSV.exists()
    with LOG_CSV.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["date", "item", "topic", "minutes", "notes_file"])
        w.writerow([today, item, topic, minutes, notes_file])


def level_char(minutes: int) -> str:
    ch = LEVELS[0][1]
    for threshold, c in LEVELS:
        if minutes >= threshold and threshold > 0:
            ch = c
    if minutes <= 0:
        ch = LEVELS[0][1]
    return ch


def minutes_by_day(rows: list[dict]) -> dict[dt.date, int]:
    agg: dict[dt.date, int] = defaultdict(int)
    for r in rows:
        d = dt.date.fromisoformat(r["date"])
        agg[d] += r["minutes"]
    return agg


def build_streak_grid(rows: list[dict]) -> str:
    agg = minutes_by_day(rows)
    today = dt.date.today()
    start = START_DATE - dt.timedelta(days=START_DATE.weekday())  # back to Monday
    end = today + dt.timedelta(days=(6 - today.weekday()))        # forward to Sunday
    if end < start:
        end = start + dt.timedelta(days=6)

    weeks: list[list[dt.date]] = []
    cur = start
    while cur <= end:
        weeks.append([cur + dt.timedelta(days=i) for i in range(7)])
        cur += dt.timedelta(days=7)

    # Month label row: 3-letter label overlaid at the week column where a month
    # first appears (labels may spill into following blank columns, GitHub-style).
    LPAD = 6            # width of the left "Mon   " gutter
    buf = [" "] * (LPAD + 2 * len(weeks) + 4)
    prev_month = None
    for wi, wk in enumerate(weeks):
        m = wk[0].month
        if m != prev_month:
            col = LPAD + 2 * wi
            for k, chn in enumerate(MONTHS[m]):
                buf[col + k] = chn
            prev_month = m
    month_row = "".join(buf).rstrip()

    day_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    lines = [month_row]
    for di, dname in enumerate(day_labels):
        row = f"{dname}   "
        for wk in weeks:
            day = wk[di]
            if day > today:
                row += "  "
            else:
                row += level_char(agg.get(day, 0)) + " "
        lines.append(row.rstrip())

    legend = "Less  · ░ ▒ ▓ █  More   " \
             "(· none | ░ <45m | ▒ 45-89m | ▓ 90-134m | █ 135m+)"
    lines.append("")
    lines.append(legend)
    return "```\n" + "\n".join(lines) + "\n```"


def compute_stats(rows: list[dict]) -> str:
    agg = minutes_by_day(rows)
    days = sorted(agg.keys())
    today = dt.date.today()

    total_days = len(days)
    total_minutes = sum(agg.values())
    total_sessions = len(rows)

    # longest streak of consecutive calendar days
    longest = cur = 0
    prev = None
    for d in days:
        if prev is not None and (d - prev).days == 1:
            cur += 1
        else:
            cur = 1
        longest = max(longest, cur)
        prev = d

    # current streak: walk back from today (or yesterday) while days are present
    current = 0
    probe = today
    if today not in agg:
        probe = today - dt.timedelta(days=1)
    while probe in agg:
        current += 1
        probe -= dt.timedelta(days=1)

    first_day = days[0].isoformat() if days else "-"
    last_day = days[-1].isoformat() if days else "-"
    hrs = total_minutes / 60

    return (
        f"| Metric | Value |\n"
        f"|---|---|\n"
        f"| \U0001f525 Current streak | **{current} day(s)** |\n"
        f"| \U0001f3c6 Longest streak | {longest} day(s) |\n"
        f"| \U0001f4c5 Days studied | {total_days} |\n"
        f"| \U0001f4da Sessions logged | {total_sessions} |\n"
        f"| ⏱️ Total time | {hrs:.1f} h ({total_minutes} min) |\n"
        f"| \U0001f195 First / last session | {first_day} / {last_day} |\n"
    )


def build_log_table(rows: list[dict]) -> str:
    if not rows:
        return "_No sessions logged yet. Run a study session, then `/save-session`._"
    out = ["| Date | Item | Topic | Time | Notes |", "|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["date"], reverse=True):
        nf = r.get("notes_file") or ""
        link = f"[notes]({nf})" if nf else ""
        out.append(
            f"| {r['date']} | {r.get('item','')} | {r.get('topic','')} "
            f"| {r['minutes']} min | {link} |"
        )
    return "\n".join(out)


def replace_block(text: str, name: str, new_body: str) -> str:
    start = f"<!-- AUTO:{name} -->"
    end = f"<!-- /AUTO:{name} -->"
    if start not in text or end not in text:
        raise SystemExit(f"Marker pair for {name} not found in PROGRESS-DASHBOARD.md")
    pre, rest = text.split(start, 1)
    _, post = rest.split(end, 1)
    return f"{pre}{start}\n{new_body}\n{end}{post}"


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == "--log":
        if len(args) < 5:
            raise SystemExit('Usage: --log "<item>" "<topic>" <minutes> <notes_file>')
        append_row(args[1], args[2], args[3], args[4])
        print(f"Logged: {args[1]} - {args[2]} ({args[3]} min)")

    rows = load_rows()
    text = DASHBOARD.read_text(encoding="utf-8")
    text = replace_block(text, "STREAK", build_streak_grid(rows))
    text = replace_block(text, "STATS", compute_stats(rows))
    text = replace_block(text, "LOG", build_log_table(rows))
    DASHBOARD.write_text(text, encoding="utf-8")
    print("PROGRESS-DASHBOARD.md updated.")


if __name__ == "__main__":
    main()
