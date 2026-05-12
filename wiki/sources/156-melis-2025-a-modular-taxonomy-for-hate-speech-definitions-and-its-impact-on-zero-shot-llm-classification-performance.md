---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, benchmark, zero-shot, prompting, explainability]
sources: [raw/sources/2025.woah-1.45.pdf]
---

# Melis 等 - 2025 - A Modular Taxonomy for Hate Speech Definitions and Its Impact on Zero-Shot LLM Classification Performance

## Metadata
- Source file: `raw/sources/2025.woah-1.45.pdf`
- Year: 2025
- Venue: WOAH 2025
- Pages: 32
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses the ambiguity of the hate speech construct: different datasets, policies, and papers operationalize hate speech differently.
- Asks how prompt definitions affect zero-shot LLM classification performance.
- Frames definition choice as both a conceptual issue for resource interoperability and a practical issue for prompt-based moderation.

## Method
- Collects 20 hate speech definitions from literature, platform policies, official documents, and LLM-generated definitions.
- Inductively derives 14 Conceptual Elements, including target, problematic content, possible implications, implicit hate, and other definitional building blocks.
- Constructs modular prompt definitions from combinations of these Conceptual Elements.
- Evaluates zero-shot classification with LLaMA-3, Mistral, and Flan-T5.

## Data and Evaluation Setup
- Datasets: HateCheck, Learning from the Worst, and Measuring Hate Speech.
- The datasets represent synthetic functional tests, human-in-the-loop adversarial data, and real-world examples.
- Reports macro-F1 and analyzes false positives/false negatives under different definition prompts.

## Results and Claims
- Definition choice affects model performance, but the direction of the effect depends on model architecture and dataset.
- Detailed definitions can reduce false negatives for some models while reducing false positives for others.
- Fine-grained HateCheck analysis suggests that targeted Conceptual Elements can improve specific hate categories, including implicit hate.

## Limitations and Follow-ups
- The taxonomy is necessarily incomplete and wording-sensitive; alternative verbalizations of the same Conceptual Elements may change results.
- The study is zero-shot only; carefully selected few-shot examples aligned to definitions remain future work.
- High-value use: treat this as a schema-control paper for comparing hate datasets and prompts, not as a single best-definition recipe.

## Structured Signals
- Detected method keywords: hate speech definitions, conceptual taxonomy, zero-shot prompting, prompt sensitivity, construct validity
- Mentioned datasets: HateCheck, Learning from the Worst, Measuring Hate Speech
- Mentioned metrics: macro-F1, false positives, false negatives, category-level errors

## Related Concepts
- [[hate-speech-datasets-and-benchmarks]]
- [[zero-shot-learning]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-research-map]]
