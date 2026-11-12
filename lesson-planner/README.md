# Menta Lesson Planner

Prepare language lessons the way Menta does: a 60-minute lesson built in an evidence-based order, written to strict
rules, delivered as an **interactive page** your students can click through, with translations on tap, drawn
pictures and a print / **Save as PDF** view (with or without the answers).

Website: https://menta-lms.com/plugin

## Skills (use them as /lesson and /unit-test)
- `/lesson <request>`: one lesson. Example:
  `/lesson prepare a lesson: A2 French, life stages, passé composé with avoir, students speak Ukrainian`
  Optional: a **focus** (speaking, grammar, vocabulary, reading, writing, or no grammar at all) and a **duration** (20–120 min, default 60),
  e.g. `/lesson B1 English, work, reported speech, students speak Polish, focus on speaking, 45 minutes`.
  Missing details (what the class knows, the students' language, the lesson kind) are asked first.
- `/unit-test <lessons>`: a scored test of 15–20 new items from a list of lessons, on its own page.

## Lesson kinds
Core, grammar focus, revision, production, bilan, unit test.

## Your style
The planner learns from the lessons you made before (the language you translate into, colours, fonts, picture
style) and keeps a small profile at `~/.lesson-planner/style-profile.json`. With no history it uses the Menta style.
Ask for any change ("serif font", "darker", "watercolour pictures", "redraw the kitchen with a cat") and it redraws
and remembers.

## Install
**Claude on the web or desktop**: download https://menta-lms.com/lesson-planner.zip, open **Customize**, choose
**Add plugin** and upload the zip. Then click **Try** on the lesson skill, or type `/lesson` and describe the lesson.

**Claude Code**
```
/plugin marketplace add illiaKvanette/menta-lesson-planner
/plugin install menta-lesson-planner@menta
```

## What's inside
```
.claude-plugin/plugin.json
skills/lesson/SKILL.md, skills/unit-test/SKILL.md
skills/lesson/reference/   lesson-kinds, exercise-types, writing-rules, levels, why-this-order, picture-style
skills/lesson/templates/   lesson-page.md, test-page.md (the HTML page templates)
```

## Licence
MIT: free to use, change and pass on to colleagues. Keep the copyright notice. See `LICENSE.md`.

Want each student's progress saved, video lessons, homework and payments in one place? → https://menta-lms.com
