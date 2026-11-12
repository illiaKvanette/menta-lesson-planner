---
description: Build a scored unit test (15–20 new items) from a list of lessons
argument-hint: "<the lessons to cover: titles, files or a short list of topics and grammar>"
---

Use the `guided-lesson` skill, section "Unit test", to build one test from these lessons:

$ARGUMENTS

If the lessons are lesson pages made earlier, read them (their `lesson-data` JSON) for the words and grammar they
taught. Otherwise ask for each lesson's words and grammar point. Write 15–20 new items, never copied from a
lesson, and output a separate page from `templates/test-page.html`.
