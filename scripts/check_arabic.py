#!/usr/bin/env python3
"""Check Arabic text in a lesson file for Unicode and vocalization problems.

Usage:
    python3 scripts/check_arabic.py FILE [--level beginner|intermediate|advanced]

ERROR  = must fix (wrong Unicode letters, tatweel, presentation forms,
         alif maqsura inside a word, repeated diacritics).
WARN   = review (unvocalized words at beginner/intermediate level,
         lines that mix Arabic and Latin outside tables).
Exit code: 1 if any ERROR, else 0. Standard library only.
"""
import argparse
import re
import sys

ARABIC_LETTER = r"\u0621-\u063A\u0641-\u064A\u0671-\u06D3"
DIACRITICS = "\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0670"
WORD_RE = re.compile(f"[{ARABIC_LETTER}{DIACRITICS}\u0640]+")
LATIN_RE = re.compile(r"[A-Za-z]{2,}")

FORBIDDEN = {
    "\u06CC": "FARSI YEH (ی): use ARABIC YEH ي U+064A",
    "\u06A9": "KEHEH (ک): use ARABIC KAF ك U+0643",
    "\u06C1": "HEH GOAL (ہ): use HEH ه U+0647",
    "\u06D5": "AE (ە): use HEH ه or TEH MARBUTA ة",
    "\u0640": "TATWEEL (ـ): remove",
}

# Short function words that are often written without harakat are still
# flagged at beginner level, except single letters such as the plural marker ج.
MIN_LETTERS_FOR_HARAKAT = 2
# Explanations may quote a short Arabic term (1-2 words) in a Latin sentence.
MAX_EMBEDDED_WORDS = 2

# Frequent mistakes that are valid letter sequences but wrong spellings.
COMMON_MISSPELLINGS = {
    "فى": "write في (final yeh with dots), not ى",
    "الى": "write إلى (hamza under alif)",
    "انا": "write أنا (hamza on alif)",
}


def is_presentation_form(ch):
    cp = ord(ch)
    return 0xFB50 <= cp <= 0xFDFF or 0xFE70 <= cp <= 0xFEFF


def letters_only(word):
    return [c for c in word if c not in DIACRITICS]


def check(path, level):
    errors, warns = [], []
    in_code = False
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    for n, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        for ch in line:
            if ch in FORBIDDEN:
                errors.append((n, FORBIDDEN[ch]))
            elif is_presentation_form(ch):
                errors.append((n, f"presentation form U+{ord(ch):04X}: retype with base letters"))
        if re.search(f"[{DIACRITICS}]{{2,}}", line):
            for m in re.finditer(f"[{DIACRITICS}]{{2,}}", line):
                marks = m.group()
                if len(set(marks)) < len(marks):
                    errors.append((n, f"repeated diacritic near col {m.start()+1}"))
        for m in WORD_RE.finditer(line):
            word = m.group()
            base = letters_only(word)
            if "\u0649" in base[:-1]:
                errors.append((n, f"alif maqsura ى inside word: {word}"))
            if (level in ("beginner", "intermediate")
                    and len(base) >= MIN_LETTERS_FOR_HARAKAT
                    and not any(c in DIACRITICS for c in word)):
                warns.append((n, f"no harakat: {word}"))
        for m in WORD_RE.finditer(line):
            bare = "".join(letters_only(m.group()))
            if bare in COMMON_MISSPELLINGS:
                errors.append((n, f"{m.group()}: {COMMON_MISSPELLINGS[bare]}"))
        stripped = line.strip()
        if (not stripped.startswith("|") and not in_code
                and WORD_RE.search(line) and LATIN_RE.search(line)):
            # Short quoted terms (1-2 words) inside explanations are allowed;
            # flag Arabic runs of 3+ words embedded in a Latin-script line.
            longest = max(len(WORD_RE.findall(seg))
                          for seg in re.split(r"[A-Za-z]+", line))
            if longest > MAX_EMBEDDED_WORDS:
                warns.append((n, f"mixed line: Arabic run of {longest} words inside Latin text"))
    return errors, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file")
    ap.add_argument("--level", default="beginner",
                    choices=["beginner", "intermediate", "advanced"])
    args = ap.parse_args()
    try:
        errors, warns = check(args.file, args.level)
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        return 2
    for n, msg in errors:
        print(f"ERROR line {n}: {msg}")
    for n, msg in warns:
        print(f"WARN  line {n}: {msg}")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
