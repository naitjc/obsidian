---
created: 2026-04-23
updated: 2026-05-12
tags: [concept, hate-speech, datasets]
sources:
  - raw/sources/2025.coling-main.446.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.45.pdf
---

# Hate Speech Datasets and Benchmarks

## Common Benchmarks
- Latent Hatred
- ToxiGen
- ETHOS
- Hateful Memes
- ToxiCN
- HateBRXplain
- U-PLEAD / TARGET
- IHC / SBIC target-span settings
- HateCheck / Learning from the Worst / Measuring Hate Speech for definition-prompt evaluation

## Notes
- Dataset shift remains a central challenge: models tuned on one source often degrade on new domains.
- Implicit hate benchmarks are harder due to annotation ambiguity and context requirements.
- Recent text-only benchmarks increasingly annotate rationales, spans, slots, definitions, or functional tests rather than only sentence-level labels.
