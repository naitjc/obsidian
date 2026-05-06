---
created: 2026-04-23
updated: 2026-04-23
tags: [concept, hate-speech, nlp]
sources:
  - raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf
  - raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf
  - raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf
  - raw/sources/Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics.pdf
  - raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf
  - raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf
---

# Implicit Hate Speech Detection

Implicit hate speech refers to hateful content that does not contain explicit slurs or overtly offensive language but relies on stereotypes,dog-whistles, or indirect implications.

## Key Challenges

1. **Implicit meaning** - No explicit markers, requires world knowledge and reasoning
2. **Context dependence** - Same statement can be hateful or neutral depending on context
3. **Annotation difficulty** - Annotators often disagree on implicit hate
4. **Generalization** - Models struggle to generalize across domains and targets

## Approaches

### Contrastive Learning
Learning generalizable representations via hard negative sampling and contrastive loss. Key papers: Kim et al. 2022, Jiang 2025.

### Shared Semantics
SharedCon (Ahn et al. 2024) leverages shared semantics between explicit and implicit hate speech for improved detection.

### Causality-guided Learning
Jiang 2025 uses causality to identify failure cases and guide contrastive learning.

### Knowledge Infusion
KIDDIN (Garg et al. 2026) infuses knowledge into LLM for indecent meme detection.

## Datasets

- **Latent Hatred** (ElSherief et al. 2021) - Benchmark for implicit hate speech
- **ToxiGen** (Hartvigsen et al. 2022) - Large-scale machine-generated dataset

## Related Concepts

- [[explicit-hate-speech-detection]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]


## Direction Link

- [[hate-speech-research-map]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
