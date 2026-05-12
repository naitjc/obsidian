---
created: 2026-04-23
updated: 2026-05-12
tags: [synthesis, hate-speech, final]
sources: []
---

# Hate Speech Direction - Final Synthesis (v2)

## Scope and Confidence
- Scope: 44 hate-speech papers in this wiki direction.
- Confidence: high for direction-level qualitative structure; medium for method-family comparisons; table-level numeric claims require matrix verification before external citation.

## Strongest Method Patterns by Scenario
- **Implicit hate detection:** contrastive learning, counterfactual augmentation, prompting, and explanation signals are the recurring strategies for handling coded or indirect language.
- **Multimodal hateful memes:** retrieval, cross-modal alignment, uncertainty modeling, and prompt/rationale methods are the main strategies for context-dependent image-text hate.
- **Cross-domain / cross-platform transfer:** causal/disentangled representations and cross-lingual nearest-neighbor or prompt-based adaptation are the most consistent strategy family.
- **Dataset and benchmark work:** benchmark papers remain central because dataset definition determines what counts as implicit, explicit, toxic, hateful, multimodal, or target-aware detection.
- **Pure-text target/intent/span modeling:** recent 2025 work moves beyond binary labels toward rationales, target spans, intent/group tags, modular definitions, and compositional target-expression tests.

## Resolved Contradictions (Direction Level)
- **Prompting vs fine-tuning for multimodal hate:** both can win, but prompting dominates low-shot settings while fine-tuned contrastive/causal models are more stable for fixed benchmarks.
- **Causal methods vs standard discriminative training in transfer:** causal/disentangled methods show stronger transfer tendency, but gains depend on split design and platform mismatch severity.
- **Synthetic data augmentation utility:** helps when curated and target-aligned (e.g., adversarial or counterfactual generation), but noisy synthetic labels can reduce robustness.
- **Prompting vs fine-tuning for multilingual text hate:** prompted LLMs can be useful in low-data or functional-test settings, but fine-tuned encoders remain stronger on many real-world datasets when labeled data is available.
- **Group tags vs intent tags:** explicit group/target tags help, but [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] suggests intent tags are often the stronger signal for both classifier generalization and human moderation.

## Evidence Links
- Prompting-heavy examples: [[003-2025-acl-long-115|HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter]], [[008-2510-07707v2|Causality Guided Representation Learning for Cross-Style Hate Speech Detection]], [[012-ahn-2024-sharedcon-implicit-hate-speech-detection-using-shared-semantics|Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics]]
- Fine-tuning / contrastive / causal examples: [[006-2306-08804v2|PEACE: Cross-Platform Hate Speech Detection - A Causality-guided Framework]], [[008-2510-07707v2|Causality Guided Representation Learning for Cross-Style Hate Speech Detection]], [[012-ahn-2024-sharedcon-implicit-hate-speech-detection-using-shared-semantics|Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics]]
- Multimodal benchmark examples: [[001-2024-nlp4pi-1-23|Explainable Identification of Hate Speech towards Islam using Graph Neural Networks]], [[003-2025-acl-long-115|HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter]], [[006-2306-08804v2|PEACE: Cross-Platform Hate Speech Detection - A Causality-guided Framework]]
- Transfer-setting examples: [[003-2025-acl-long-115|HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter]], [[006-2306-08804v2|PEACE: Cross-Platform Hate Speech Detection - A Causality-guided Framework]], [[008-2510-07707v2|Causality Guided Representation Learning for Cross-Style Hate Speech Detection]]
- Synthetic data examples: [[008-2510-07707v2|Causality Guided Representation Learning for Cross-Style Hate Speech Detection]], [[043-hartvigsen-2022-toxigen-a-large-scale-machine-generated-dataset-for-adversarial-and-implicit-hate-speech-detection|Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection]], [[059-kim-2023-conprompt-pre-training-a-language-model-with-machine-generated-data-for-implicit-hate-speech-detect|Kim 等 - 2023 - ConPrompt Pre-training a Language Model with Machine-Generated Data for Implicit Hate Speech Detect]]
- Pure-text explainability/span examples: [[151-salles-2025-hatebrxplain-a-benchmark-dataset-with-human-annotated-rationales-for-explainable-hate-speech-detection-in-brazilian-portuguese|Salles 等 - 2025 - HateBRXplain]], [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection|Calabrese 等 - 2025 - Compositional Generalisation]], [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models|Boudraa 等 - 2025 - Implicit Hate Target Span Identification]], [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech|Carvallo 等 - 2025 - Hate Explained]]
- Prompt/definition multilingual examples: [[153-mnassri-2025-rag-and-recall-multilingual-hate-speech-detection-with-semantic-memory|Mnassri 等 - 2025 - RAG and Recall]], [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance|Melis 等 - 2025 - Modular Taxonomy]], [[157-ghorbanpour-2025-can-prompting-llms-unlock-hate-speech-detection-across-languages|Ghorbanpour 等 - 2025 - Can Prompting LLMs Unlock Hate Speech Detection]]

## Direction Deliverables
- Navigation and map: [[hate-speech-research-map]], [[hate-speech-source-hub]]
- Quality control: [[hate-speech-lint-report-2026-04-23]]
- Quant tracking: [[hate-speech-metrics-matrix]], [[hate-speech-priority-papers]]
- Completion status: [[hate-speech-direction-status]]
- Completion report: [[hate-speech-completion-report-2026-04-29]]

## Boundary
- This direction is complete as an internal LLM wiki artifact: sources, concepts, entities, synthesis, status, and lint are connected.
- It is not a publication-ready numeric leaderboard until every metric row is manually checked against original result tables.
