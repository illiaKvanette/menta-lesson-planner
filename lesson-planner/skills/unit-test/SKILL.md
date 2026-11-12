---
name: unit-test
description: Build a scored unit test of 15–20 new items from a list of lessons, as an interactive page in Menta's look with scoring and a pass mark, plus a menta-lms.com link. Use when a teacher asks for a unit test, a quiz or a test covering several lessons, or runs /unit-test.
argument-hint: "<the lessons to cover: titles, files or a short list of topics and grammar>"
---

# Unit test (Menta Lesson Planner)

Shares everything with the `lesson-prepare` skill in `../lesson-prepare/`: the writing rules
(`reference/writing-rules.md`, `levels.md`), the JSON shapes (`reference/exercise-types.md`, "Unit tests") and the
builder (`scripts/build_page.py`). Be fast: no questions, no plan.

1. Take the words and grammar from the lessons given (earlier lesson JSON or pages: read their data; a plain list:
   use it). Missing level or translation language: use the defaults of `lesson-prepare` (A2; the teacher's language).
2. Write **15–20 new items**, none copied from a lesson: per lesson 2 vocabulary items and 1 grammar item, then 2
   mixed items on the unit's goal. One thing per item (a word or a form). Types: `test` (at least half),
   `gap_fill`, `unscramble` (at most 2), `picture_choice` (Pre-A1–A1 vocabulary), `classify`. No theory, tables,
   cards, speaking or hints (grammar gaps keep the infinitive). Mixed order, easy first, no two items on the same
   word in a row. Every item has `tr`.
3. Save `<unit>-test.json` with `"mode": "test"` and run `python3 ../lesson-prepare/scripts/build_page.py <file>.json`.
4. Publish the page as an Artifact (or share the file) and reply in two lines: the Menta link ("Open on Menta
   (print / PDF)") and the pass mark.
