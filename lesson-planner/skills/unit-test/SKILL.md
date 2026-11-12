---
name: unit-test
description: Build a scored unit test of 15–20 new items from a list of lessons, as a separate interactive page with scoring and a pass mark. Use when a teacher asks for a unit test, a quiz or a test covering several lessons, or runs /unit-test.
argument-hint: "<the lessons to cover: titles, files or a short list of topics and grammar>"
---

# Unit test (Menta Lesson Planner)

This skill shares everything with the `lesson` skill, in `../lesson/`:
- the method and test rules: `../lesson/SKILL.md`, section "Unit test (/unit-test)";
- the writing rules: `../lesson/reference/writing-rules.md` and `levels.md`;
- the item shapes: `../lesson/reference/exercise-types.md`, "Test items";
- the page: the HTML inside `../lesson/templates/test-page.md`, saved as a `.html` file, with only its
  `<script id="test-data">` JSON filled.

Steps:
1. If the lessons are lesson pages made earlier, read their `lesson-data` JSON for the words and grammar they
   taught. Otherwise ask, once, for each lesson's words and grammar point, the level, and the students' language.
2. Follow the teacher's style profile (`../lesson/SKILL.md`, section 2) for colours, font and translation language.
3. Write 15–20 newly written items, none copied from a lesson; mixed order; no theory, tables, cards or hints.
4. Save the page and publish it as an Artifact when the host supports Artifacts.
