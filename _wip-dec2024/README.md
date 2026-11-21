# WIP: CSIR NET Life Sciences December 2024 paper (exam 01-Mar-2025, shift 1)

Temporary hand-off folder. Delete this whole folder in the final commit.

- `source/p1.txt`, `source/p2.txt`: `pdftotext -layout` OCR of the question paper (pages 1-66 and 67-106).
  OCR has errors; the question text in `data/*.py` for A1-C47 is already corrected.
- `source/key.json`: NTA final answer key, keyed by Question ID (703245 = "2 or 4").
- `source/order.txt`: Question IDs in paper order (145 lines: A1-20, B1-50, C1-75).
- `figs/figs.json`: cropped, watermark-free figures as webp data URIs with display w/h.
  Keys: A1 A5 A18 C14 C17 C19 C21 C27 C28 C31 C33a C33b C36 C41 C46 C50 C58 C63 C71 C74 C75.
- `data/h.py`: helpers P / IMG / TBL / MATCH / E / Q (block format matches pyq-jun2025.js, plus `explanation`).
- `data/qa.py` (Q_A, 20), `qb.py` (Q_B, 50), `qc1.py` (Q_C1, C1-C37), `qc2.py` (Q_C2, C38-C44),
  `qc3.py` (Q_C3, C45-C47). **C48-C75 still to write.**

NTA keys for C48-C75 (paper order):
C48:2 C49:4 C50:4 C51:2 C52:2 C53:2 C54:2 C55:4 C56:1 C57:1 C58:3 C59:2 C60:2 C61:1 C62:4
C63:1 C64:3 C65:2 C66:3 C67:2 C68:2 C69:4 C70:4 C71:4 C72:4 C73:2 C74:1 C75:1
Figures needed: C50, C58, C63, C71, C74, C75. C73 needs the complementation table.
