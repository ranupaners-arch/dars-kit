# dars-kit

Agent Skill untuk menyusun materi pelajaran **bahasa Arab (fusha)** yang siap
dipakai di kelas dari sebuah tema. Hasilnya mencakup mufradat berharakat, hiwar,
qawa'id, latihan empat maharah, kunci jawaban, rubrik, catatan guru, dan
(opsional) kerangka slide atau modul ajar.

Skill ini dibuat untuk guru bahasa Arab di Indonesia (madrasah, pesantren, dan
kelas umum). Ia mengikuti format terbuka [Agent Skills](https://agentskills.io),
sehingga bisa dipakai di Claude Code dan tool lain yang mendukung standar tersebut.

> ⚠️ Materi yang dihasilkan AI tetap harus diperiksa guru sebelum dipakai,
> terutama harakat, jamak, dan mashdar. Skill ini menandai kata yang meragukan
> dengan ⚠️, tetapi tidak menggantikan pemeriksaan manusia.

## Fitur

- Mufradat berharakat lengkap sesuai level, dengan jamak dan gender untuk isim
  serta *madhi – mudhari' – mashdar* untuk fi'il (contoh `كَتَبَ – يَكْتُبُ – كِتَابَةٌ`)
- Hiwar orisinal; penutur default sesama gender dan dhamir selalu cocok
- Satu poin qawa'id yang diambil dari hiwar, disajikan secara fungsional
- Latihan minimal dua dari empat maharah (istima', kalam, qira'ah, kitabah),
  ditandai level kognitif C1–C6 dan disertai rubrik untuk kalam/kitabah
- Kunci jawaban terpisah, cocok per butir, dengan alasan singkat
- Catatan guru: alokasi waktu yang pas dengan durasi kelas, kesalahan umum
  siswa Indonesia, serta remedial dan pengayaan
- Mode keluaran: pelajaran lengkap, mufradat saja, latihan saja, kerangka
  slide, atau modul ajar
- Panduan slide Arab: font berlisensi terbuka, ukuran, dan tata letak RTL
- `scripts/check_arabic.py` untuk mengecek huruf Persia (ی ک), tatweel,
  presentation forms, ى di tengah kata, dan kata tanpa harakat

## Instalasi

### Claude Code (personal, berlaku di semua proyek)

```bash
git clone https://github.com/ranupaners-arch/dars-kit.git \
  ~/.claude/skills/dars-kit
```

Atau salin foldernya secara manual ke `~/.claude/skills/dars-kit/`
(Windows: `%USERPROFILE%\.claude\skills\dars-kit\`).

### Claude Code (khusus satu proyek)

Salin folder ke `.claude/skills/dars-kit/` di root proyek, lalu commit.

### Aplikasi Claude (claude.ai) dan tool lain

- **claude.ai**: unggah folder ini sebagai skill lewat pengaturan Skills (ikuti petunjuk unggah di sana).
  Frontmatter hanya memakai field standar (`name`, `description`, `license`,
  `metadata`), jadi aman untuk diunggah.
- **Tool lain yang mendukung Agent Skills**: salin folder ke direktori skills
  milik tool tersebut. Lihat dokumentasi masing-masing tool.

### Validasi (opsional)

```bash
pip install skills-ref
agentskills validate ./dars-kit
```

## Contoh pemakaian

```
Buatkan materi bahasa Arab tema السَّكَنُ untuk pemula, 2 × 45 menit.
Buat 10 soal pilihan ganda mufradat tema المهنة untuk kelas 8 MTs, lengkap dengan kunci.
Susun kerangka slide qawa'id isim isyarah untuk santri putri tingkat menengah.
Buat modul ajar bahasa Arab Fase D tema الأسرة, 2 pertemuan.
Make an Arabic lesson on الطعام for intermediate adult learners, explanations in English.
```

Di Claude Code, skill bisa juga dipanggil langsung dengan `/dars-kit`.

Contoh hasil lengkap ada di [examples/sakan-pemula.md](examples/sakan-pemula.md).

## Struktur folder

```
dars-kit/
├── SKILL.md                     # alur kerja inti, aturan, checklist (dibaca saat skill aktif)
├── references/
│   ├── pedagogy.md              # maharah & unsur lughah, alur pembelajaran, level, CP madrasah, modul ajar
│   ├── arabic-text-rules.md     # harakat, notasi sharaf, ortografi & Unicode, kesalahan umum
│   ├── assessment.md            # jenis latihan, penulisan soal, pengecoh, HOTS, rubrik, format kunci
│   └── slide-design.md          # font & lisensi, ukuran, RTL, format blok slide
├── assets/
│   └── lesson-template.md       # kerangka keluaran
├── examples/
│   └── sakan-pemula.md          # contoh lengkap: السَّكَنُ, pemula
├── scripts/
│   └── check_arabic.py          # pemeriksa Unicode & harakat (Python 3, tanpa dependensi)
├── evals/
│   └── evals.json               # 3 skenario uji
├── README.md
└── LICENSE
```

## Pengujian

`evals/evals.json` berisi tiga skenario uji: pelajaran lengkap, soal saja, dan
slide berbahasa Inggris, masing-masing dengan perilaku yang diharapkan. Jalankan
setiap skenario di sesi baru, sekali dengan skill dan sekali tanpa skill, lalu
bandingkan hasilnya. Cek juga hasilnya dengan:

```bash
python3 scripts/check_arabic.py hasil.md --level beginner
```

## Kontribusi

Koreksi bahasa Arab (harakat, jamak, mashdar) sangat diharapkan. Saat mengirim
koreksi, sertakan rujukan kamus. Jangan menambahkan teks atau latihan yang
disalin dari buku ajar yang dilindungi hak cipta.

## Lisensi

[MIT](LICENSE) © 2026 Ranupane Rimba Argana

---

## English summary

**dars-kit** is an Agent Skill that turns a theme and learner level
into a ready-to-teach Modern Standard Arabic lesson for Indonesian classrooms:
fully vocalized vocabulary with plural, gender and verb forms; an original
dialogue; one functional grammar point; exercises across the four skills with
cognitive levels and rubrics; a separate answer key; and teacher notes with
timing. It can also output a slide outline or a *modul ajar*.

Install it by copying this folder to `~/.claude/skills/dars-kit/`
(Claude Code), or to the skills directory of any tool that supports the
[Agent Skills](https://agentskills.io) format. Then ask, for example,
*"Make an Arabic lesson on السَّكَنُ for beginners, 90 minutes."* Generated
material must be reviewed by a teacher. MIT licensed.
