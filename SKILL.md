---
name: dars-kit
description: Builds ready-to-teach Modern Standard Arabic lessons for non-native learners from a theme and level - fully vocalized vocabulary (mufradat) with plural, gender and verb forms, a dialogue (hiwar), one grammar point (qawa'id), exercises across the four skills (maharat), a separate answer key with rubrics, teacher notes with timing, and an optional slide outline or modul ajar. Use when a teacher asks for Arabic teaching material, e.g. "materi bahasa Arab", "mufradat berharakat", "hiwar tema ...", "latihan/soal bahasa Arab", "kunci jawaban", "modul ajar/RPP bahasa Arab", "bahan ajar madrasah/pesantren", "slide pelajaran bahasa Arab", "Arabic lesson plan", "Arabic worksheet" or "Arabic vocabulary list".
license: MIT (see LICENSE)
metadata:
  author: Ranupane Rimba Argana
  version: "1.0.0"
---

# Dars Kit

Turns a theme (السَّكَنُ, الْأُسْرَةُ, الْمَدْرَسَةُ, ...) into a classroom-ready Arabic
lesson for Indonesian learners in madrasah, pesantren or general classes.

## 1. Inputs and defaults

Ask only for what is missing. If the teacher gives only a theme, proceed with
the defaults and list the assumptions at the top of the answer.

| Input | Default | Notes |
|---|---|---|
| Theme (مَوْضُوعٌ) | required | Arabic or Indonesian |
| Level | beginner (مُبْتَدِئٌ) | intermediate (مُتَوَسِّطٌ), advanced (مُتَقَدِّمٌ); see references/pedagogy.md for rough CEFR/ACTFL orientation |
| Explanation language | Indonesian | English or others on request |
| Output mode | full lesson | vocab only, exercises only, slide outline, modul ajar |
| Class length | 90 minutes (2 × 45) | timing in teacher notes must add up to this |
| Learners | not specified | age, fase/kelas, madrasah/pesantren/umum, mixed or single-gender |
| Curriculum alignment | none | if the teacher asks for madrasah alignment, follow references/pedagogy.md §Curriculum |

## 2. Non-negotiable rules

1. **MSA (الْفُصْحَى)** by default; dialect only if the teacher asks.
2. **Harakat by level**: beginner and intermediate get full harakat on every
   Arabic word in vocab, dialogue, examples and exercises, including i'rab and
   tanwin; advanced gets harakat only on ambiguous or newly introduced words.
3. **Nouns**: singular, plural and gender, e.g. `بَيْتٌ ج بُيُوتٌ (مُذَكَّرٌ)`.
   **Verbs**: past, present and masdar, e.g. `كَتَبَ – يَكْتُبُ – كِتَابَةٌ`.
4. **Direction**: Arabic and its translation never share a line. Use separate
   table cells or separate lines. Instructions and dialogue are never mixed-script.
   Explanations (grammar, key reasons, notes) may quote a short Arabic term of one
   or two words inside an explanation-language sentence.
5. **Agreement**: pronouns and verb forms match each speaker (أَنْتَ / أَنْتِ,
   هُوَ / هِيَ). Dialogue speakers are the same gender unless the teacher says otherwise.
6. **Skills**: exercises cover at least two of the four maharat (اِسْتِمَاعٌ،
   كَلَامٌ، قِرَاءَةٌ، كِتَابَةٌ).
7. **Answer key** is a separate section after all student material and is never on student slides.
8. **Originality**: write new dialogues, texts and items. Do not reproduce
   published textbooks, even partially; use them only as structural models.
9. **Uncertainty**: if unsure about a vocalization, plural, gender, masdar or
   meaning, mark it ⚠️ with a short reason instead of guessing.
10. **Speaker notes and teacher notes** are written in the explanation language.

## 3. Workflow

Copy this checklist into your working notes and tick it off:

```
- [ ] 1. Inputs confirmed, defaults stated
- [ ] 2. Lesson plan: goals → target words → one grammar point → skills
- [ ] 3. Draft with assets/lesson-template.md
- [ ] 4. Arabic checked against references/arabic-text-rules.md
- [ ] 5. Exercises, key and rubric checked against references/assessment.md
- [ ] 6. Slides (if requested) per references/slide-design.md
- [ ] 7. Self-check loop passed (section 5)
- [ ] 8. Delivered with assumptions and ⚠️ list
```

**Step 1 – Inputs.** Apply section 1. Do not ask more than one round of questions.

**Step 2 – Plan backwards from the goals.** Write 2–3 measurable goals
(observable verb + amount + skill, e.g. "Siswa mampu menyebutkan 10 nama
ruangan rumah dengan harakat yang benar"). Choose target words that serve the
goals, then one grammar point that occurs naturally in the dialogue, then the
skills each exercise will assess. Every goal must be checked by at least one exercise.

**Step 3 – Draft.** Fill assets/lesson-template.md in order. Sizes by level:

| | Beginner | Intermediate | Advanced |
|---|---|---|---|
| New words | 10–15 | 15–20 | 20–25 |
| Dialogue / text | 6–10 short lines | 8–12 lines or a short text | text or longer dialogue |
| Transliteration | yes, one consistent scheme | no | no |
| Exercise types | 3–5 | 4–6 | 4–6, include one HOTS task |

Supporting words that are not target vocabulary may appear in the dialogue
only if they are very common or clear from context. List them under
"ungkapan pendukung".

**Step 4 – Arabic accuracy.** Read references/arabic-text-rules.md before
writing Arabic for the first time in a session. Pay particular attention to
hamza forms, lam shamsiyya/qamariyya marking, diptotes (مَمْنُوعٌ مِنَ الصَّرْفِ),
and Unicode letters (Arabic ي and ك, never Persian ی or ک).

**Step 5 – Exercises and key.** Read references/assessment.md. Use 3-option
multiple choice with plausible distractors, give each exercise its maharah and
cognitive level, and attach an analytic rubric to every speaking or writing task.

**Step 6 – Slides (only if requested).** Read references/slide-design.md and
use the slide block format there.

**Step 7 – Self-check loop.** Run the section 5 checklist. If shell access
exists, also run:

```bash
python3 scripts/check_arabic.py <output.md> --level beginner
```

The script reports Unicode errors (Persian letters, tatweel, presentation forms,
misplaced ى) and unvocalized words. Fix every error and re-run until it is clean.
Treat warnings as items to review, not automatic failures.

**Step 8 – Deliver.** Start with a 2–4 line summary: theme, level, length,
assumptions. End with the ⚠️ list (or "Tidak ada item ⚠️").

## 4. Output modes

- **Full lesson**: every section of assets/lesson-template.md.
- **Vocab only**: goals, vocabulary table, 2–3 example sentences per verb, one
  quick exercise, and its key.
- **Exercises only**: the exercises, key and rubric. State which vocabulary and
  grammar they assume.
- **Slide outline**: the slide block format in references/slide-design.md, plus a
  separate answer-key block for the teacher.
- **Modul ajar**: wrap the full lesson in the modul ajar components listed in
  references/pedagogy.md §Modul ajar. Do not invent policy names or regulation
  numbers. Use only those in that file, and only if the teacher asks for alignment.

## 5. Quality checklist (run before answering)

Arabic
- [ ] Harakat present at the level's density, and i'rab matches each word's role.
- [ ] Every plural, gender and masdar is correct or flagged ⚠️.
- [ ] Hamzat qat' written (أ / إ), hamzat wasl bare (ا); lam qamariyya has sukun (الْ), lam shamsiyya none and the next letter has shadda (السَّ).
- [ ] Diptotes carry no tanwin (مَطَابِخُ، أَحْمَدُ).
- [ ] Only Arabic-block letters; no tatweel, no Persian ی/ک, ى only word-final.

Pedagogy
- [ ] Each goal is measurable and assessed by at least one exercise.
- [ ] Every target word appears in the dialogue or exercises at least once.
- [ ] At least two maharat covered; listening and speaking come before writing for beginners.
- [ ] Timing adds up exactly to the class length.

Assessment
- [ ] Every item has exactly one correct answer. For open or rearrange items, the key lists all accepted variants.
- [ ] The key numbering matches the items one-to-one.
- [ ] Distractors are plausible and homogeneous, and the position of the correct option varies.
- [ ] Speaking and writing tasks have a rubric.

Format
- [ ] Instructions and dialogue are single-script; Arabic and translation are in separate lines or cells.
- [ ] The answer key is separate, and student slides contain no answers.
- [ ] Teacher and speaker notes are in the explanation language.

## 6. Reference files (read when needed)

- references/pedagogy.md: maharat and unsur lughah, lesson flow, level
  orientation, Indonesian curriculum alignment, modul ajar components.
- references/arabic-text-rules.md: harakat, morphology notation, orthography
  and Unicode checks, common learner errors.
- references/assessment.md: exercise types by maharah, item-writing rules,
  distractor design, HOTS, rubrics, answer-key format.
- references/slide-design.md: fonts and licenses, sizes, RTL layout, slide block format.
- assets/lesson-template.md: exact output skeleton.
- examples/sakan-pemula.md: worked example (السَّكَنُ, beginner, 2 × 45 min).
- scripts/check_arabic.py: Unicode and vocalization checker (Python 3, no dependencies).
