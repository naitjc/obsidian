---
created: 2026-06-06
updated: 2026-06-06
tags: [paper, deep-ingest-v2, llm-reasoning, safety-alignment, retrieval, benchmark, prompting]
sources: [raw/sources/2508.16406v2.pdf]
---

# Yang 等 - 2025 - Retrieval-Augmented Defense Adaptive and Controllable Jailbreak Prevention for Large Language Models

## Metadata
- Source file: `raw/sources/2508.16406v2.pdf`
- Year: 2025
- Venue: arXiv v2
- Pages: 17
- Ingest level: deep-ingest-v2 (abstract, method, experiment setup, results, conclusion, limitations, and ethics text checked from local PDF text)

## Problem Framing
- LLM jailbreak defenses must adapt to newly emerging attack strategies without costly retraining.
- Safety systems also need controllable trade-offs between blocking harmful prompts and avoiding false refusals for benign queries.
- The paper treats jailbreak detection as a retrieval-augmented defense problem rather than as direct target-model generation intervention.

## Method
- Proposes Retrieval-Augmented Defense (RAD), which retrieves known attack examples and uses them to infer malicious intent and jailbreak strategy.
- Supports training-free updates by adding new attack examples to the retrieval database.
- Uses ensemble classification and a tunable threshold to control the safety-utility operating point.
- Separates detection from response generation, so the defense can sit upstream of target-model generation.

## Data and Evaluation Setup
- Evaluates harmful-query defense on StrongREJECT and multiple jailbreak attack types.
- Evaluates benign-query false refusal on a synthesized benign set plus general QA benchmarks including AlpacaEval 2.0 and MMLU.
- Uses StrongREJECT attack score, false refusal rate, and safety-utility operating curves.
- Studies adaptation by incrementally adding newly observed jailbreak strategies to the retrieval database.

## Results and Claims
- Reports that RAD substantially lowers attack success / StrongREJECT scores for strong attacks while keeping false refusal rates comparatively low.
- Shows incremental database expansion improves defense against new attacks without degrading earlier attack coverage.
- Claims the tunable threshold gives controllable safety-utility trade-offs across deployment settings.
- Exact operating-curve and table values should be manually checked before external quantitative citation.

## Limitations and Follow-ups
- Retrieval-database coverage and example quality are central assumptions; unseen attack families may still require new examples.
- The harmfulness labels follow benchmark definitions, so policy mismatch remains a deployment risk.
- Local relevance: useful for [[retrieval-augmented-generation]] as a safety-oriented retrieval application and for [[llm-evaluation]] because evaluation depends on safety-utility frontier design.

## Related Concepts
- [[llm-reasoning-source-hub]]
- [[retrieval-augmented-generation]]
- [[llm-evaluation]]
- [[llm-reasoning]]
