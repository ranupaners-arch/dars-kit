# Slide and document design

## Contents
- Fonts and licenses
- Sizes and spacing
- RTL layout
- Slide block format
- Slide sequence for a full lesson

## Fonts and licenses

Pick a Naskh face with reliable harakat positioning:

| Font | Use | License |
|---|---|---|
| Amiri | body text, vocabulary, dialogue (classic book Naskh) | SIL Open Font License 1.1 |
| Noto Naskh Arabic | body text; pairs well with Noto Sans for Latin | SIL Open Font License 1.1 |
| Scheherazade New (SIL) | body text, very clear harakat, simplified style; real Medium/SemiBold/Bold weights | SIL Open Font License 1.1 |
| KFGQPC Uthmanic Script Hafs | **Qur'anic quotations only** | proprietary terms from King Fahd Glorious Qur'an Printing Complex: free to use, but no modification or reproduction without approval. Do not bundle it in the repo or template. |

Rules:
- Use one Arabic font per deck, with a regular and a bold weight. Avoid
  synthetic bold or italic. Most Arabic fonts have no true italic, and faux
  styles can damage letterforms and harakat.
- Quote Qur'anic text in a Uthmani or Naskh font, copied from a verified source,
  never retyped from memory. Mark it ⚠️ for the teacher to verify.
- Do not use decorative or display fonts (Diwani, Thuluth-style) for anything
  learners must read with harakat.

## Sizes and spacing

No official minimum size for harakat on slides was found. The values below are
working defaults that teachers should adjust after a test projection.

- On a 16:9 slide, Arabic body text should be **at least 32 pt** and vocabulary
  cards 40–60 pt. Arabic body text should be about 1.2–1.3× the size of Latin
  text on the same slide, because harakat and letter dots are small.
- Line spacing should be **at least 1.3–1.5**. Arabic ascenders and descenders
  extend further than Latin ones, and stacked marks such as shadda + kasra need room.
- Use at most 6 lines of Arabic per slide, with one idea per slide.
- Use high contrast (dark text on a light background). Do not put text on busy
  photos. Do not colour individual harakat unless you are teaching them.
- To highlight a word, use colour or a box, not underline. Underline collides
  with dots and kasra.

## RTL layout

- Set every Arabic text box to **right-to-left paragraph direction** and
  **right alignment**. Setting the alignment alone is not enough: punctuation
  and numbers will be ordered wrongly.
- Keep Arabic and translation in **separate text boxes or table cells**. In
  a table, put Arabic in the right-hand column and the meaning in the left-hand
  column. A bilingual table may stay LTR as a whole, but its Arabic cells must be RTL.
- Do not mix scripts on one line. If a mixed line cannot be avoided, put the
  Arabic in its own run and check where punctuation, brackets and numbers end up.
  The Unicode bidi algorithm treats them as neutral or weak characters, so they
  may move to the wrong side.
- Brackets mirror automatically in RTL. Type them logically and do not swap them by hand.
- In PowerPoint, Google Slides or Canva, enable the right-to-left text controls
  (usually by adding Arabic as an editing language) before building the deck.

## Slide block format

For a slide outline, produce one block per slide:

```
Slide N — <title in explanation language>
Arabic content (RTL box):
  <max 6 lines, fully vocalized for beginner/intermediate>
Translation / instruction (LTR box):
  <explanation-language text, separate box>
Speaker note (<explanation language>): <what the teacher says or does, ≤3 sentences, timing>
Suggested visual: <picture or icon idea; no text baked into images>
```

## Slide sequence for a full lesson

1. Title: theme in Arabic plus the explanation language, level, and meeting number.
2. Goals (explanation language).
3. Trigger question or picture (pertanyaan pemantik).
4–6. Vocabulary: 4–6 words per slide, picture + Arabic + meaning.
7–8. Dialogue: 4–5 lines per slide, speaker names on the right.
9. Grammar point: rule plus 3 examples, with the target form highlighted.
10–12. Exercises: student version only.
13. Speaking or writing task, with sentence frames and the rubric summary.
14. Closing: reflection question and preview.

The answer key goes in a separate teacher-only section or deck, never on student slides.
