# Exercise JSON shapes

The lesson JSON. `scripts/build_page.py` turns it into the page (Menta's look) and the menta-lms.com/play link, where
the same JSON opens with Menta's own exercise components. Write valid JSON only (no comments, no trailing commas).
```json
{ "title": "Life stages", "language": "French", "lang_code": "fr", "level": "A2", "kind": "Core", "focus": "speaking", "minutes": 45,
  "translate_to": "Ukrainian", "goal": "Talk about the stages of your life with the passé composé.",
  "ui": {},
  "blocks": [ { "name": "Warm-up", "minutes": 5, "exercises": [ { "type": "speaking", "task": "…", "task_tr": "…", "items": [] } ] } ] }
```
Every exercise may carry `task` + `task_tr` (the instruction and its translation). `tr` is always the translation into `translate_to`. `svg` / `picture` hold an inline SVG string
(escape `"` as `\"` inside JSON).

| type | fields |
|---|---|
| `text` | `title`, `picture` (svg), `body` (paragraphs separated by `\n\n`). No translation |
| `dialogue` | `title`, `lines: [{speaker, text}]` (2 speakers). No translation |
| `speaking` | `items: [{q, tr, model}]`, `model` = the model answer |
| `test` | `items: [{sentence, answer, options: [3 distractors], tr}]`; `sentence` contains `answer` once (the page cuts the gap) |
| `gap_fill` | `items: [{sentence, answer, hint?, accept?: [], tr}]`; `hint` only for grammar (the infinitive) or Pre-A1 scrambles |
| `unscramble` | `items: [{sentence, tr}]`; the page shuffles the words |
| `classify` | `columns: [{title, tr}]`, `items: [{text, tr, column}]` (`column` = index) |
| `sort_paragraphs` | `paragraphs: [in the right order]`, `translations: [one per paragraph]` |
| `paragraph_headings` | `paragraphs: [{text, heading}]`, `extra_headings: []` |
| `picture_choice` | `mode: "picture_to_word" \| "word_to_picture"`, `items: [{word, tr, svg}]`; picture-fit: `mode: "fit"`, `question`, `question_tr`, `items: [{svg, correct: true}, {svg}, {svg}, {svg}]` |
| `memory_pairs` | `pairs: [{a, b}]`, at most 5 |
| `label_picture` | `svg`, `mode: "pick" \| "type"`, `labels: [{text, x, y}]` (x, y from 0 to 1) |
| `grammar_theory` | `slides: [{header, header_tr, text, text_tr, examples: [{text, tr}]}]` |
| `grammar_table` | `title`, `headers: []`, `rows: [[]]`. Target language only |
| `cards` | `cards: [{word, tr, svg?, example?}]` |
| `incomplete_dialogue` | `lines: [{speaker, text, tr?}]` for the host; guest lines `{speaker: "You", text: "…", hint: "model answer"}` |
| `match_pairs` | `pairs: [{a, b}]` (word → collocation or definition; the page shuffles the right side) |
| `crossword` | `words: [{answer, clue, tr?}]` (5–8 words from the lesson) |
| `constrained_text` | `required_words: []`, `min_words`, `max_words`, `model?` (a model text for the teacher). Homework-style writing with a live word counter |
| `story_telling` | `phrases: []` (4–6 phrase cards), `seconds?` (default 60). The student tells a story using every card |
| `production_cards` | `cards: [{role, role_tr, required_words: []}]` |
| `image_task` | `svg`, `phrases: []` (useful phrases shown on tap) |

## Unit tests
Same JSON with `"mode": "test"` and only scorable types in the blocks (`test`, `gap_fill`, `unscramble`,
`picture_choice`, `classify`); one block per part, or a single block. The page counts the first answer of every item
and shows the pass mark (80%, rounded up).
```json
{ "mode": "test", "title": "Unit 2 test", "language": "English", "level": "A2", "translate_to": "Ukrainian", "ui": {},
  "blocks": [ { "name": "Words and grammar", "exercises": [
    { "type": "test", "items": [ { "sentence": "…", "answer": "…", "options": ["…","…","…"], "tr": "…" } ] },
    { "type": "gap_fill", "items": [ { "sentence": "…", "answer": "…", "hint": "infinitive, grammar only", "tr": "…" } ] } ] } ] }
```

## Optional look
`"style": {"primary": "#1E7BE6", "font": "Georgia, serif"}`: only from the teacher's style profile or request.

## Page labels (`"ui"`)
English by default. For another teacher language, translate the ones you need:
`check, retry, correct, wrong, reset, model, translate, answers, allTr, min, build, wheel, done, phrases, words, start,
choose, yourAnswer, allPairs, moves, tapCard, score, pass, finish, passed, failed, firstTry, made, ctaTitle, ctaSub,
ctaBtn, ctaPrint, footer`.
