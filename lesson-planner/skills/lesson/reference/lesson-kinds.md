# Lesson kinds and block order (60 minutes by default)

Pick the kind from the request; default **Core**.

| Kind | When |
|---|---|
| Core | a topic, a text, a grammar point and new words (most lessons) |
| Grammar focus | the lesson is about one structure; the input is a short text full of it |
| Revision | the end of a unit: review the unit's grammar and words |
| Production | the goal is a piece of writing or speaking on a model text |
| Bilan | three lessons closing a block of units: lexical, grammatical, production |
| Unit test | a scored test, see the skill's "Unit test" section |

## Core
| # | Block | What goes in | Min |
|---|---|---|---|
| 1 | Warm-up | 3 `speaking`. Pre-A1–A1: yes/no questions with "why?". A2+: open questions | 5 |
| 2 | Reading, round 1 (gist) | the `text` (with its picture) or `dialogue`. Pre-A1–A1: 2–3 simple `speaking` (Who? Where? How many people?). A2+: `sort_paragraphs`, `paragraph_headings` or 2–3 `speaking`. When the text describes a person, family, place or childhood, add a picture-fit question (`picture_choice`, mode `fit`) | 8 |
| 3 | Reading, round 2 (detail) | reread, 4–6 `test` / `gap_fill` on content and words, never grammar | 7 |
| 4 | Pictures | `picture_choice`: 5 `picture_to_word` + 5 `word_to_picture` with the lesson's words | 3 |
| 5 | Grammar | notice: one `classify` or 5–10 `test`; then `grammar_theory` (easy words) and `grammar_table`s | 8 |
| 6 | Grammar practice | **at most 10 items**: mixed `test`, `gap_fill`, `unscramble` | 9 |
| 7 | Vocabulary | intro: `memory_pairs` or `label_picture`; then about 10 items (`test`, `unscramble`, `gap_fill`) so that every new word is practised once | 10 |
| 8 | Cards | `cards` with the lesson's words, as review (after the vocabulary block) | 2 |
| 9 | Speaking | 1–2 items: `incomplete_dialogue` (a small podcast), `production_cards` or `image_task` | 8+ |

## Grammar focus
As Core, but one reading round only (2 or 3), a longer grammar block (theory plus 2–3 tables), and blocks 4, 7, 8
only if the lesson has new words.

## Revision
1. Warm-up (3 `speaking`). 2. A text with gaps (`gap_fill` in text order) or a text plus one round.
3. Review table only (`grammar_table`, no theory). 4. 10 mixed items (`test`, `gap_fill`, `unscramble`, `classify`).
5. Vocabulary and cards only if the unit had words to review. 6. Speaking (1–2 items).

## Production
1. Warm-up. 2. The model text. 3. Analysis: `sort_paragraphs` or `paragraph_headings`.
4. A grammar table only if the task needs a structure; never a table of words or phrases (useful phrases go in
   `image_task.phrases`, `production_cards.required_words` or the hints of an `incomplete_dialogue`).
5. Production: `speaking`, `production_cards`, `incomplete_dialogue`. Written work is homework. No grammar practice block.

## Bilan
- Lexical: `classify`, `memory_pairs`, `picture_choice` (all modes), `label_picture`, with the block's words. No new words.
- Grammatical: comparison `grammar_table`s side by side, then 10 contrast items (`test` with two plausible options, `gap_fill`, `classify`).
- Production: one guided speaking task (`production_cards` or `incomplete_dialogue`) crossing the block's topics, plus a written task set as homework.

## The podcast (every `incomplete_dialogue`)
A short podcast interview: a named host asks, the student is the guest. Title it like a show
("Podcast 'My life in stages': you are the guest"). 6–8 guest turns, open questions about the student's own life
that use the lesson's grammar and words. The host reacts briefly before each next question. Each guest line has a
`hint`: a 2–3 sentence model answer at the level.

## Focus and duration (both optional)
The tables above are a **balanced 60-minute** lesson. The teacher may ask for another length, another focus, or both.
The block **order** never changes; only minutes and item counts do. Set `"minutes"` and `"focus"` in the page JSON.

**Duration.** Scale every block's minutes in proportion, then round to whole minutes so they add up to the duration.
- Under 45 minutes: keep warm-up, the text with one reading round, notice + theory, practice, the speaking task;
  merge picture matching into the vocabulary block; drop cards (they are review) unless the focus is vocabulary.
- 45–75 minutes: all blocks.
- Over 75 minutes: all blocks, plus a second speaking task (a role play with `production_cards`) and a short
  writing task (`constrained_text`) at the end. Grammar practice stays at most 10 items; add a second practice set
  of up to 6 items after the vocabulary block if needed.
- Item counts follow the time: about one minute per practice item, 2–3 minutes per speaking item.

**Focus.** Move about a third of the time toward the focus, taken evenly from the other blocks, never below
2 minutes for a kept block.
| Focus | More of | Less of |
|---|---|---|
| speaking | warm-up (4–5 questions), speaking `items` after the gist round, two speaking tasks at the end (podcast + role play) | grammar practice (5–6 items), vocabulary practice |
| grammar | notice, theory with 2–3 tables, practice up to 10 items, a second short set | second reading round, picture matching |
| vocabulary | picture matching, `memory_pairs` or `label_picture`, about 12 vocabulary items, cards, `crossword` | theory slides (one slide + one table) |
| reading | a longer text (top of the level range), both rounds, `paragraph_headings` or `sort_paragraphs` | grammar practice |
| **no grammar** | the second reading round, speaking after the text, vocabulary (about 12 items), word games (`memory_pairs`, `crossword`), cards, a short `constrained_text` | **blocks 5 and 6 are removed entirely**: no notice step, no theory, no tables, no grammar practice |
| writing / production | the model-text analysis, `constrained_text` in class with required words, then a short speaking task | picture matching, cards |
| balanced | the tables above | — |
A **grammar-focus** or **production** lesson kind already leans that way; the focus setting adds to it.

**No grammar** (the teacher says "no grammar", "without grammar", "just words and talking"). Remove blocks 5 and 6,
give their minutes to reading, vocabulary and speaking, and add a short writing task. Then nothing in the lesson
may *teach or test* a structure: no `grammar_theory`, no `grammar_table`, no gap fill with a verb in brackets, no
`classify` of forms, and no comprehension question about a form. The text and the dialogue still use correct
language, but they are read for meaning only. If the lesson kind is *grammar focus*, ask once what they want, because
the two cannot both be true.

## Flows at a glance (each adds up to the lesson length; here 60 minutes)
| Style | Blocks (minutes) |
|---|---|
| Balanced | warm-up 5, gist 8, details 7, pictures 3, notice + theory 8, grammar practice 9, vocabulary 10, cards 2, podcast 8 |
| Speaking | warm-up 8, gist 6, talk about the text 8, notice + theory 6, grammar practice 4, vocabulary 6, podcast 10, role play 12 |
| Vocabulary | warm-up 5, gist 7, details 5, pictures 6, vocabulary 14, word games 10, cards 5, podcast 8 |
| Grammar | warm-up 5, gist 7, notice + theory 16, practice 14, contrast practice 8, podcast 10 |
| No grammar | warm-up 6, gist 8, details 8, pictures 5, vocabulary 12, cards 3, podcast 8, writing task 10 |
| Unit test | easy start, words (2 per lesson), grammar (1 per lesson), mixed review, score; no minutes |
