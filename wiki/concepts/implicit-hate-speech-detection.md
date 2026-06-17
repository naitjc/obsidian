---
created: 2026-04-23
updated: 2026-06-17
tags: [concept, hate-speech, nlp]
sources:
  - raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf
  - raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf
  - raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf
  - raw/sources/Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics.pdf
  - raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf
  - raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2601.09342v2.pdf
  - raw/sources/3774904.3792159.pdf
  - raw/sources/07936-AAAI24.ZhangJ-SRRAI.pdf
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

### Span and Structure-Aware Detection
Recent pure-text work shifts from sentence labels toward internal structure. [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] treats implicit target span identification as a BIO tagging problem, while [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] tests whether models can generalize target-expression and slot combinations beyond training correlations.

### Intent and Target Enrichment
[[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] shows that intent tags are stronger than group tags alone for both classifier generalization and human moderation support. This supports treating target labels as relational evidence rather than as simple identity priors.

### Knowledge Infusion
KIDDIN (Garg et al. 2026) infuses knowledge into LLM for indecent meme detection.

### Agentic and Structured Reasoning
Recent LLM-based work shifts from one-shot labels toward gated reasoning systems.
[[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]] triggers Community Agent consultation only for uncertain target-sensitive cases, using target-group context to improve balanced moderation outcomes.
[[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]] argues that implicit hate should be grounded in Latent Hate Components and shows that structured component mining plus pro/con deliberation is stronger than generic CoT or debate.
[[194-zhang-2024-efficient-toxic-content-detection-by-bootstrapping-and-distilling-large-language-models]] contributes a broader toxic-content mechanism: confidence-gated DToT refinement and rationale distillation into smaller models.

For the local IHC/SBIC line, these papers support bounded verifier designs: trigger expensive reasoning on uncertain or shortcut-prone rows, expose compact intermediate objects, and evaluate false positives and false negatives separately instead of relying only on aggregate F1.

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
