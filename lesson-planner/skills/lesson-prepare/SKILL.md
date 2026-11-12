---
name: lesson-prepare
description: Prepare a language lesson (60 minutes by default) to the Menta method, with an optional focus and length, as an interactive page in Menta's look (exercises with automatic checking, translations, pictures) plus a menta-lms.com link where the lesson opens with Menta's own exercises and prints to PDF. Use when a teacher asks to prepare, plan or write a lesson, a worksheet or a class for a language course, or runs /lesson-prepare.
argument-hint: "<e.g. A2 English, travel, present perfect, students speak Ukrainian, focus on speaking, 45 min>"
---

# Lesson prepare (Menta Lesson Planner)

You write **only the lesson data (JSON) and its pictures**. A script turns them into the page; you never write or
copy page code. Be fast: no questions, no plan, no previews. Build the lesson straight away.

## 1. Read the request, fill the gaps yourself
Take from the request: the language being taught, level, topic, grammar point, the students' language, and two
optional settings, **focus** and **length**.

| Missing | Use |
|---|---|
| level | A2 |
| students' language (translations) | the language the teacher wrote in, or the teacher's style profile; if that is the language being taught, English |
| grammar point | one that fits the topic and level (e.g. travel at A2: present perfect for experiences) |
| what the class already knows | assume only what is normal for the level; never ask |
| lesson kind | core |
| focus / length | balanced / 60 minutes |

Focus words: "talking", "conversation", "more speaking" = speaking; "a grammar lesson" = grammar; "no grammar",
"without grammar" = no grammar teaching or testing at all; also vocabulary, reading, writing.
**Do not ask the teacher anything** unless the language being taught truly cannot be guessed. After the lesson,
state your assumptions in one short line ("A2, translations into Ukrainian, 60 min"), so the teacher can ask for a change.
Talk to the teacher in the language they wrote in.

## 2. The rules (read once per session, quickly)
- `reference/lesson-kinds.md`: blocks, minutes and counts per kind, focus and length.
- `reference/writing-rules.md`: how every sentence, gap and distractor is written. Binding.
- `reference/levels.md`: tense limits and text lengths per level.
- `reference/exercise-types.md`: the JSON shape of every exercise. Follow it exactly.
- `reference/picture-style.md`: how pictures are drawn.

## 3. Write the JSON
1. Blocks in the order of the kind, minutes adding up to the length, focus applied (`lesson-kinds.md`).
2. Write each answer first, then the sentence around it. Every sentence a student reads in an exercise has `tr`
   (translation into the students' language). Texts, dialogues and grammar tables are not translated.
3. Page labels in the teacher's language go in `"ui"` (keys: see `exercise-types.md`, "Page labels"); leave
   `"ui": {}` for English.
4. **Pictures, kept small so the lesson builds fast**: one picture for the text, and up to 6 word pictures
   (picture matching / cards). Add a picture-fit question or `label_picture` only when the topic needs it. Each SVG
   simple, under about 4 KB: the house frame and pencil filter from `picture-style.md`, flat shapes, few details.
   Picture-fit decoys reuse the same SVG with one detail changed.

## 4. Build and hand over
1. Save the JSON as `<language>-<level>-<topic>.json` (lowercase, dashes) and run:
   `python3 <this skill's folder>/scripts/build_page.py <file>.json`
   It writes `<file>.html` (the page in Menta's look) and prints the **menta-lms.com/play link**. A JSON error
   stops it: fix the JSON and run again.
2. Show the page: publish `<file>.html` as an Artifact when the host can publish a file, otherwise share the file.
   Copy it to `~/.lesson-planner/lessons/` when that folder can be written.
3. Your reply, short: one line with the assumptions, the Menta link as **"Open on Menta (print / PDF)"**, and one
   line saying the teacher can ask to change any block, the level or the pictures. Nothing else.

## 5. The teacher's style
- Lessons look like Menta by default. A saved profile (`~/.lesson-planner/style-profile.json`, or what you remember
  about this teacher) may set `translate_to`, the label language, `picture_style`, and a `style`
  (`{"primary": "#…", "font": "…"}`, put into the JSON) — use it without asking.
- When the teacher asks for a change ("darker pictures", "serif font", "redraw the text picture with a cat", "more
  speaking"), rebuild only what changed, run the script again, and update the profile so the next lesson has it.

## Checklist (silently, before building)
- [ ] Block order and counts fit the kind, focus and length; minutes add up; grammar practice at most 10 items.
- [ ] Focus "no grammar": no theory, tables, bracketed-verb gaps or form questions anywhere.
- [ ] No past tense at Pre-A1–A1; nothing beyond the level.
- [ ] Dialogues: at most 2 speakers, real-life order. Comprehension tests content, not grammar.
- [ ] Vocabulary gaps: no hint. Grammar gaps: the infinitive in `hint`. Distractors are real words. Memory: ≤ 5 pairs.
- [ ] Every exercise sentence has `tr`; every speaking item and podcast guest line has a model answer.
- [ ] Pictures: no text, no fingers, everything inside the frame.

## Never
- Never write or paste the page code; only the JSON, then the script.
- Never reuse Menta's own course pictures or texts.
- Never ask what the class has learned before.
