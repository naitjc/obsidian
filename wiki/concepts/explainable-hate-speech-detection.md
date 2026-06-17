---
created: 2026-04-23
updated: 2026-06-17
tags: [concept, hate-speech, explainability]
sources:
  - raw/sources/17745-13-21239-1-2-20210518.pdf
  - raw/sources/2021.naacl-demos.17.pdf
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.coling-main.446.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2025.woah-1.45.pdf
  - raw/sources/2023.acl-short.66.pdf
  - raw/sources/2022.naacl-main.433.pdf
  - raw/sources/2026.findings-eacl.230.pdf
  - raw/sources/2601.09342v2.pdf
  - raw/sources/3774904.3792159.pdf
  - raw/sources/07936-AAAI24.ZhangJ-SRRAI.pdf
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

- [[159-mathew-2021-hatexplain-a-benchmark-dataset-for-explainable-hate-speech-detection]] provides a foundational English benchmark combining class labels, target communities, and human rationales.
- [[162-ranasinghe-2021-mudes-multilingual-detection-of-offensive-spans]] adds a deployable offensive-span detection system with multilingual models.
- [[163-calabrese-ross-lapata-2022-explainable-abuse-detection-as-intent-classification-and-slot-filling]] reframes abuse detection as policy-aware intent classification and slot filling with PLEAD.
- [[168-yu-2022-hate-speech-and-counter-speech-detection-conversational-context-does-matter]] shows that explanation and classification can depend on conversational context, especially for counter-speech.
- [[169-zampieri-2023-target-based-offensive-language-identification]] links offensive argument expressions with target spans, making explanations relation-bearing rather than only toxic-span highlights.
- [[151-salles-2025-hatebrxplain-a-benchmark-dataset-with-human-annotated-rationales-for-explainable-hate-speech-detection-in-brazilian-portuguese]] adds Portuguese human rationale spans and shows that plausible post-hoc explanations may still be unfaithful.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] uses slots and parse structures to test whether models learn atomic hate-speech components rather than target-expression shortcuts.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] localizes implicit hate target spans with lightweight models.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] evaluates intent/group tags for both machine classifiers and human moderators.
- [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance]] shows that definition wording changes zero-shot LLM behavior and error tradeoffs.
- [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] shows that generic reward models can underrate richer offensive-content explanations and provides a hate-aware evaluation resource for generated explanations.
- [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]] adds an agentic explanation path where Moderator and Community Agent rationales are fused for uncertain implicit-hate cases.
- [[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]] makes explanation more structured by forcing the system to mine latent hate components and deliberate over each component before final classification.
- [[194-zhang-2024-efficient-toxic-content-detection-by-bootstrapping-and-distilling-large-language-models]] shows a distillation path: use DToT-generated rationales as supervision for smaller toxic-content detectors, while keeping rationale faithfulness as a separate evaluation risk.
