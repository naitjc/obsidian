---
created: 2026-04-23
updated: 2026-05-12
tags: [concept, hate-speech, explainability]
sources:
  - raw/sources/2025.coling-main.446.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2025.woah-1.45.pdf
---

# Explainable Hate Speech Detection

## Why Explainability Matters
Moderation decisions require auditability, appeal support, and reduced annotator disagreement.

## Typical Approaches
- Rationales and span-level evidence
- Step-by-step reasoning prompts
- Interpretable reasoning graphs
- Intent/group tagging and NER-style text enrichment
- Slot-filling and compositional parse structures

## Open Challenges
- Faithfulness of explanations
- Tradeoff between accuracy and interpretability
- Evaluation standards for explanation quality

## Recent Pure-Text Additions

- [[151-salles-2025-hatebrxplain-a-benchmark-dataset-with-human-annotated-rationales-for-explainable-hate-speech-detection-in-brazilian-portuguese]] adds Portuguese human rationale spans and shows that plausible post-hoc explanations may still be unfaithful.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] uses slots and parse structures to test whether models learn atomic hate-speech components rather than target-expression shortcuts.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] localizes implicit hate target spans with lightweight models.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] evaluates intent/group tags for both machine classifiers and human moderators.
- [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance]] shows that definition wording changes zero-shot LLM behavior and error tradeoffs.
