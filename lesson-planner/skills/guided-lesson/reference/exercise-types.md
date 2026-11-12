# Exercise JSON shapes

These are the same exercise types and data shapes Menta's lesson player uses, so a lesson made here can later be
rebuilt in Menta one to one. The lesson page JSON:
```json
{ "title": "Life stages", "language": "French", "lang_code": "fr", "level": "A2", "kind": "Core", "focus": "speaking", "minutes": 45,
  "translate_to": "Ukrainian", "goal": "Talk about the stages of your life with the passé composé.",
  "style": {}, "ui": {},
  "blocks": [ { "name": "Warm-up", "minutes": 5, "exercises": [ { "type": "speaking", "task": "…", "task_tr": "…", "items": [] } ] } ] }
```
Every exercise may carry `task` + `task_tr` (the instruction and its translation) and `teacher_note` (shown only
with "Teacher answers"). `tr` is always the translation into `translate_to`. `svg` / `picture` hold an inline SVG string
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

## Test items (`templates/test-page.md`)
```json
{ "title": "Unit 2 test", "language": "French", "level": "A2", "translate_to": "Ukrainian", "style": {}, "ui": {},
  "items": [
    { "type": "test", "sentence": "…", "answer": "…", "options": ["…","…","…"], "tr": "…", "source": "Lesson 2.3" },
    { "type": "gap_fill", "sentence": "…", "answer": "…", "hint": "infinitive, grammar only", "tr": "…" },
    { "type": "unscramble", "sentence": "…", "tr": "…" },
    { "type": "picture_choice", "svg": "<svg…>", "answer": "…", "options": ["…","…","…"] },
    { "type": "classify", "sentence": "task", "columns": [{"title": "…"}], "items": [{"text": "…", "column": 0}] }
  ] }
```
