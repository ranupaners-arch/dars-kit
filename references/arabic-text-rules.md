# Arabic text rules

## Contents
- Variety and register
- Harakat by level
- Morphology notation
- Orthography checks
- Unicode checks
- Direction (RTL/LTR)
- Learner errors (Indonesian learners)
- When to flag ⚠️

## Variety and register

- Use Modern Standard Arabic (الْفُصْحَى). Use dialect only on request, and label it.
- Use classroom-neutral vocabulary. When MSA has several common words, pick the
  one used in mainstream teaching materials and mention the alternative in teacher notes.

## Harakat by level

| Level | Where | What |
|---|---|---|
| Beginner, intermediate | every Arabic word in vocab, dialogue, examples, exercises, key | full harakat including case endings (i'rab) and tanwin |
| Advanced | new words, ambiguous words, grammar examples | selective; keep i'rab on the word the grammar point is about |

Conventions for full vocalization:
- Lam qamariyya takes sukun: الْبَيْتُ، الْحَدِيقَةُ، الْمَطْبَخُ.
- Lam shamsiyya takes no mark, and the next letter takes shadda: السَّكَنُ، النَّوْمُ، الدُّخُولُ.
- Hamzat al-wasl is written as a bare alif (ا) without a vowel sign in running
  text: اِسْمٌ may show kasra in isolation for beginners. Be consistent.
- Fathatan: two placements exist (on the letter before the alif, or on the alif).
  Default: on the letter before the alif (كِتَابًا، شُكْرًا), and use it consistently.
  No alif is added after ة or after final ء preceded by alif: مَدْرَسَةً، مَاءً.
- Diptotes take no tanwin and take fatha for the genitive: مَطَابِخُ، حَدَائِقُ،
  أَحْمَدُ، فِي مَسَاجِدَ.
- Use the dagger alif where standard: هٰذَا، هٰذِهِ، ذٰلِكَ، لٰكِنْ.
- Vocabulary lists use the citation form with tanwin: بَيْتٌ، غُرْفَةٌ.
- At a pause, the spoken ending may be sukun. Write the full ending and explain
  pause pronunciation (waqf) in teacher notes when relevant.

## Morphology notation

Nouns: `مُفْرَدٌ ج جَمْعٌ (جِنْسٌ)`
- `بَيْتٌ ج بُيُوتٌ (مُذَكَّرٌ)`
- `غُرْفَةٌ ج غُرَفٌ (مُؤَنَّثٌ)`
- When a noun has two common plurals, give the more frequent one first and the
  other after `/`: `سَرِيرٌ ج أَسِرَّةٌ / سُرُرٌ`.
- When plurals are the grammar topic, label the plural type: جَمْعُ تَكْسِيرٍ،
  جَمْعُ مُذَكَّرٍ سَالِمٌ، جَمْعُ مُؤَنَّثٍ سَالِمٌ.
- Flag feminine nouns without ة (دَارٌ، شَمْسٌ) and nouns of either gender
  (سُوقٌ، طَرِيقٌ) in teacher notes.

Verbs: `مَاضٍ – مُضَارِعٌ – مَصْدَرٌ`
- `كَتَبَ – يَكْتُبُ – كِتَابَةٌ`
- Always give the present-tense middle vowel, because it is not predictable
  (يَكْتُبُ، يَجْلِسُ، يَفْتَحُ).
- If a verb has more than one common masdar, give the one that fits the theme
  and flag ⚠️ if unsure.
- For intermediate and above, the form (وَزْنٌ) may be added: `(فَعَّلَ)`.

Adjectives: give masculine and feminine, and the plural if useful:
`كَبِيرٌ – كَبِيرَةٌ ج كِبَارٌ`.

## Orthography checks

- Hamza: أ / إ for hamzat al-qat' (أَنَا، إِلَى، أُمِّي), ا for hamzat al-wasl
  (اِبْنٌ، اسْمٌ، الـ). Medial and final seats follow the vowels (سُؤَالٌ، مَسْؤُولٌ / مَسْئُولٌ ⚠️ regional variant, شَيْءٌ).
- Alif maqsura ى only at word end (عَلَى، إِلَى، مُسْتَشْفًى). Final ي is a yeh with dots (فِي، بَيْتِي). Never write فِي as فى.
- Ta marbuta ة vs ha ه: غُرْفَةٌ (noun ending), but بَيْتُهُ (pronoun).
- Arabic punctuation inside Arabic text: ، (comma) ؛ (semicolon) ؟ (question mark).
- Digits: use Arabic-Indic (١ ٢ ٣) for numbering inside Arabic exercises and
  Western digits (1 2 3) in Indonesian or English text. Do not mix within one exercise.

## Unicode checks

| Use | Not | Why |
|---|---|---|
| ي U+064A ARABIC LETTER YEH | ی U+06CC FARSI YEH | looks similar, but breaks search, sorting and some fonts |
| ك U+0643 ARABIC LETTER KAF | ک U+06A9 KEHEH | Persian/Urdu letter |
| ه U+0647 HEH | ہ U+06C1 HEH GOAL, ە U+06D5 AE | Urdu/Kurdish letters |
| plain letters | U+0640 TATWEEL (ـ) | a stretching character, not a letter; it breaks copy, search and harakat placement |
| base letters U+0600–U+06FF | presentation forms U+FB50–U+FDFF, U+FE70–U+FEFF | deprecated for interchange; they break shaping and search |
| ى U+0649 at word end only | ى in mid-word or for final ي | changes the word |

Diacritics are U+064B–U+0652 plus U+0670 (dagger alif). Each letter gets at most one
vowel sign, plus an optional shadda. Never type the same mark twice.

`scripts/check_arabic.py` checks these mechanically.

## Direction (RTL/LTR)

- Arabic and Indonesian or English go on separate lines or in separate table cells.
- Never put Latin words inside an Arabic sentence. Exercise instructions and
  dialogue lines are single-script.
- Explanations (qawa'id, key reasons, teacher notes, rubric) may quote a short
  Arabic term of one or two words inside an Indonesian or English sentence.
  Longer Arabic examples go on their own line or table cell.
- Punctuation at the edge of a mixed line can jump to the wrong side, which is
  why rule 4 in SKILL.md exists.

## Learner errors (Indonesian learners)

Mention the relevant ones in teacher notes:
- Gender agreement: Indonesian has no grammatical gender, so learners mix
  هٰذَا/هٰذِهِ, هُوَ/هِيَ, and verb prefixes (يَكْتُبُ / تَكْتُبُ).
- Sound pairs: ح/ه، ع/ء، خ/ك، ذ/ز/د، ث/س، ص/س، ض/د، ط/ت، ظ/ز، ق/ك, plus long and short vowels (كَتَبَ vs كَاتِبٌ).
- Ta marbuta: pronounced -t in connected speech and idafa (غُرْفَةُ النَّوْمِ → ghurfatun-naum), and -h at a pause.
- Dropping or misreading tanwin and i'rab endings.
- Adding a copula: there is no "is" in the present-tense nominal sentence (الْبَيْتُ كَبِيرٌ).
- Intermediate learners: non-human plurals take feminine singular agreement (الْغُرَفُ كَبِيرَةٌ).

## When to flag ⚠️

Flag rather than guess when:
- a broken plural has several forms and you are unsure which is standard;
- a masdar is uncertain or differs by meaning (for example, the masdar of سَكَنَ in the sense of "to live/reside");
- a noun's gender is disputed or regional;
- the word is regional or colloquial (for example, words for modern appliances);
- vocalization of a rare word is uncertain.

Format: `⚠️ <word>: <what is uncertain> – mohon dicek di kamus (mis. al-Mu'jam al-Wasīṭ / kamus standar guru).`
