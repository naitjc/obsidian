---
created: 2026-06-05
updated: 2026-06-05
tags: [paper, deep-ingest-v2, hate-speech, multimodal, llm-reasoning, benchmark, prompting, explainability, safety-alignment]
sources: [raw/sources/2510.08630v3.pdf]
---

# Mei 等 - 2026 - ExPO-HM Learning to Explain-then-Detect for Hateful Meme Detection

## Metadata
- Source file: `raw/sources/2510.08630v3.pdf`
- Year: 2026
- Venue: ICLR 2026 / arXiv v3
- Pages: 34
- Ingest level: deep-ingest-v2 (first page visually rendered; abstract, methodology, experiment setup, conclusion, and ethical statement checked)

## Problem Framing
- Hateful meme moderation needs more than binary alarms because moderators need target, attack type, and rationale-like support for action.
- Prior Explain-then-Detect systems based on CoT prompting or LMM agents can underperform direct SFT baselines.
- The paper diagnoses two bottlenecks: generated explanations may miss policy-relevant cues such as targets and attack types, and binary rewards are too weak to guide reasoning quality.

## Method
- Proposes ExPO-HM, an Explain-then-Detect policy-optimization framework for hateful meme detection.
- Uses SFT warmup on policy-manual-augmented data to align model outputs with moderation guideline structure.
- Applies GRPO with curriculum learning, moving from fine-grained policy/category supervision toward binary hateful/benign decisions.
- Introduces Conditional Decision Entropy (CDE) as both a reasoning-quality metric and reward signal: good explanations should condition sharper and correct decisions.

## Data and Evaluation Setup
- Evaluates on HatefulMemes, MAMI, and PrideMM.
- Tests binary classification across all three datasets.
- Tests fine-grained classification for attack methods and target groups on HatefulMemes, attack methods on MAMI, and stance/target group categories on PrideMM.
- Evaluates reasoning quality on HatefulMemes because gold human rationales are available there.
- Uses macro F1 for binary classification, micro F1 for imbalanced fine-grained classification, LLM-as-a-judge for rationale alignment, CDE as a proxy reasoning metric, and additional human evaluation.

## Results and Claims
- Claims state-of-the-art performance on binary detection, fine-grained classification, and reasoning quality across the evaluated hateful meme benchmarks.
- Reports ExPO-HM outperforms GRPO and DPO baselines and makes Explain-then-Detect competitive with or stronger than direct detection.
- Exact table values, effect sizes, and statistical reliability should be treated as pending manual table verification before external citation.

## Limitations and Follow-ups
- The framework depends on explicit moderation policies and fine-grained labels; transfer to datasets without those structures is not automatic.
- Reasoning quality is partly evaluated through LLM-as-a-judge and CDE, so judge reliability and metric faithfulness remain important audit points.
- Deployment requires cultural and policy adaptation because hateful-content judgments depend on local norms and moderation guidelines.
- Local transfer: relevant to [[dual-view-target-statement-relation-alignment]] and [[ai-assisted-research-ideation-workflow]] because it turns explanation fields into trainable/evaluable structure rather than free-form CoT.

## Related Concepts
- [[hate-speech-source-hub]]
- [[multimodal-learning-source-hub]]
- [[llm-reasoning-source-hub]]
- [[multimodal-inspired-ihc-relation-methods-2026-06-05]]
- [[p0-target-grounding-reading-synthesis-2026-06-01]]
