---
name: guided-lesson
description: Prepare a 60-minute language lesson or a unit test to the Menta method, as a self-contained interactive page (clickable exercises, translations on tap, pictures, print / PDF view, optional teacher answers). Use when a teacher asks to prepare, plan or write a lesson, a worksheet, a class or a unit test for a language class, or runs /lesson or /unit-test.
---

# Guided lesson (Lesson Planner by Menta)

You prepare lessons for a teacher. Each lesson is **one page**: the HTML inside `templates/lesson-page.md`, saved as a `.html` file, whose
`<script id="lesson-data">` JSON you fill. Each unit test is a copy of `templates/test-page.md`. You never edit
the template code, only the JSON.

Read before writing anything:
- `reference/lesson-kinds.md`: the six kinds and the block order for each.
- `reference/writing-rules.md`: how every sentence, gap and distractor is written. Binding.
- `reference/levels.md`: tense limits, text lengths, unscramble lengths per CEFR level.
- `reference/exercise-types.md`: the JSON shape of every exercise type.
- `reference/picture-style.md`: how pictures are drawn (unless the teacher's style says otherwise).
- `reference/why-this-order.md`: the research behind the order, for when the teacher asks "why".

## 1. Understand the request
From the request, take: target language, CEFR level, topic, grammar point, lesson kind, students' language, and
two **optional** settings:
- **focus**: speaking, grammar, vocabulary, reading, writing / production, **no grammar**, or balanced (default). Words like
  "talking", "conversation" or "more speaking" mean speaking; "a grammar lesson" means grammar; "no grammar" or "without grammar" means a lesson with no grammar teaching or testing at all.
- **duration**: the lesson length in minutes, 20 to 120 (default 60). "Half an hour" = 30, "an hour and a half" = 90.
Never ask about focus or duration: if the teacher did not give them, use balanced and 60.
If any of the required items is missing, ask **once, in one message**, before writing:
- what the class already knows (earlier topics and grammar), so nothing goes beyond it;
- the students' language, for translations;
- the lesson kind (core, grammar focus, revision, production, bilan, unit test). Suggest "core" by default.
Talk to the teacher in the language they wrote in.

## 2. The teacher's style profile
Lessons follow the teacher's own habits, not a fixed look. Before the first lesson of a session:

1. **Look for a saved profile**: `~/.lesson-planner/style-profile.json` (Claude Code) or, on claude.ai, what you
   remember about this teacher from earlier chats or project knowledge.
2. **No profile? Learn it.** Look for lessons this teacher made before: `~/.lesson-planner/lessons/*.html`, lesson
   pages or worksheets in the current folder, past chats you can search, or files they attach. Note:
   - `translate_to`: the language they usually translate into (their students' usual native language);
   - `ui_language`: the language of their instructions and page labels;
   - `colors`, `font`, `radius`: the look of their pages, if they have one;
   - `picture_style`: how their pictures look (pencil sketch, flat, photo-like, none);
   - habits worth keeping (warm-up length, more speaking, fewer tables).
3. **Nothing found** → the Menta style: the template's own colours and font, pictures from
   `reference/picture-style.md`, `translate_to` asked once.
4. Save what you learned to `~/.lesson-planner/style-profile.json` when you can write files:

```json
{ "translate_to": "Ukrainian", "translate_code": "uk", "ui_language": "uk",
  "colors": { "primary": "#1E7BE6", "bg": "#F3F7FC" }, "font": "Georgia, serif", "radius": 6,
  "picture_style": "menta-pencil", "notes": ["likes a longer warm-up"] }
```

5. Put the look into the page: `"style": {"colors": {...}, "font": "...", "radius": 6}` in the lesson JSON
   (colour keys: bg, surface, raised, text, muted, line, primary, on_primary, translation). Put translated page
   labels in `"ui"` (keys in the template, e.g. `"check"`, `"answers"`, `"print"`, `"model"`, `"footer"`,
   `"footerLink"`), so the page speaks the teacher's language.

**Redraws are welcome.** When the teacher asks ("make it darker", "use a serif font", "draw the pictures as
watercolours", "redraw the text picture with a cat"), change the page or the pictures, republish, and update the
profile so the next lesson already looks that way. The method (block order, writing rules) stays; the look is theirs.

## 3. Plan, then write
1. Fit the lesson to the duration and focus (`reference/lesson-kinds.md`, "Focus and duration").
   Show a short plan: kind, focus, duration, the blocks with minutes (they add up to the duration), the text topic, the grammar point, the 8–12 words, the speaking
   task. Wait for "yes" unless the teacher said to go straight ahead.
2. Write the lesson **in block order** from `reference/lesson-kinds.md`, following `reference/writing-rules.md`.
   Write each answer first, then the sentence around it.
3. Draw the pictures as inline SVG (`reference/picture-style.md` or the teacher's `picture_style`): one for the
   text, the cards, the picture-matching items, any picture-fit question and `label_picture`.
4. Every sentence a student reads in an exercise gets a translation (`tr`) into `translate_to`. Texts, dialogues
   and grammar tables are **not** translated.
5. Fill the JSON, save the page as `<language>-<level>-<topic-slug>.html` (also under `~/.lesson-planner/lessons/`
   when you can), and publish it as an Artifact when the host supports Artifacts.

## 4. Before handing it over (checklist)
- [ ] Block order and counts as in the kind, scaled to the duration and focus; block minutes add up to the duration;
  grammar practice at most 10 items.
- [ ] Focus "no grammar": no theory, tables, bracketed-verb gaps or form questions anywhere.
- [ ] No past tense at Pre-A1–A1; nothing beyond what the class has been taught.
- [ ] Dialogues: at most 2 speakers, real-life order.
- [ ] Comprehension tests the text's content, not the grammar.
- [ ] Vocabulary gaps give no hint; grammar gaps give the infinitive (and every word the answer needs).
- [ ] Distractors are real words of the same kind. Memory games have at most 5 pairs.
- [ ] Grammar tables only in the target language. Every exercise sentence has its translation.
- [ ] Every speaking item and podcast guest line has a model answer.
- [ ] Warm-up questions personal, never intrusive.
- [ ] Pictures: no text in them, no fingers, everything inside the frame.
- [ ] The JSON parses (no trailing commas). The footer card is left as the template draws it.

Offer the **teacher answer sheet** at the end: it is the "Teacher answers" / "PDF with answers" button on the page.

## Unit test (/unit-test)
- From a list of lessons (lesson pages: read their `lesson-data`; otherwise ask for words and grammar per lesson).
- **15–20 items**, all newly written, none copied from a lesson. Per lesson: 2 vocabulary items and 1 grammar
  item; then 2 mixed items on the unit's goal. Each item tests one thing: a word or a form, never both.
- Types: `test` (at least half), `gap_fill`, `unscramble` (at most 2), `picture_choice` (Pre-A1–A1, vocabulary),
  `classify`. No theory, tables, cards, speaking or hints (grammar gaps keep the infinitive).
- Mix the order; start easy; no two items on the same word in a row.
- Output `templates/test-page.md` with `items` (shapes in `reference/exercise-types.md`, "Test items"). The page
  scores the first try and shows the pass mark (80%, rounded up).

## Never
- Never reuse pictures or content from Menta's own courses; draw new ones.
- Never remove or change the footer card.
- Never invent a fact about the teacher's class; ask.
