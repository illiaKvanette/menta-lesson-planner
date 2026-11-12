# Menta Lesson Planner

Prepare language lessons the way Menta does: a 60-minute lesson built in an evidence-based order, written to strict
rules, delivered as an **interactive page** your students can click through, with translations on tap, drawn
pictures and a print / **Save as PDF** view (with or without the answers).

Website: https://menta-lms.com/plugin

## Skills (use them as /lesson-prepare and /unit-test)
- `/lesson-prepare <request>`: one lesson. Example:
  `/lesson-prepare A2 French, life stages, passé composé with avoir, students speak Ukrainian`
  Optional: a **focus** (speaking, grammar, vocabulary, reading, writing, or no grammar at all) and a **duration** (20–120 min, default 60),
  e.g. `/lesson-prepare B1 English, work, reported speech, students speak Polish, focus on speaking, 45 minutes`.
  No questions and no plan step: missing details get sensible defaults (A2, translations into your language, 60 min), named in one line so you can change them.
- `/unit-test <lessons>`: a scored test of 15–20 new items from a list of lessons, on its own page.

## Lesson kinds
Core, grammar focus, revision, production, bilan, unit test.

## What you get
- An interactive page in Menta's look: exercises with automatic checking, translations, a speaking wheel, chat-style
  dialogues, slides, pictures drawn for the lesson. Claude writes only the lesson data; a small script builds the page.
- A **menta-lms.com/play** link: the same lesson with Menta's own exercises, where print and PDF work. Share it with
  students; nothing is stored, the lesson lives in the link.
- Ask for any change ("more speaking", "redraw the text picture", "B1 instead") and only that part is rebuilt.

## Install
**Claude on the web or desktop**: download https://menta-lms.com/lesson-planner.zip, open **Customize**, choose
**Add plugin** and upload the zip. Then click **Try** on the lesson-prepare skill, or type `/lesson-prepare` and describe the lesson.

**Claude Code**
```
/plugin marketplace add illiaKvanette/menta-lesson-planner
/plugin install menta-lesson-planner@menta
```

## What's inside
```
.claude-plugin/plugin.json
skills/lesson-prepare/SKILL.md, skills/unit-test/SKILL.md
skills/lesson-prepare/reference/   lesson-kinds, exercise-types, writing-rules, levels, why-this-order, picture-style
skills/lesson-prepare/templates/   lesson-page.md, test-page.md (the page, built by scripts/build_page.py)
skills/lesson-prepare/scripts/     build_page.py
```

## Licence
MIT: free to use, change and pass on to colleagues. Keep the copyright notice. See `LICENSE.md`.

Want each student's progress saved, video lessons, homework and payments in one place? → https://menta-lms.com
