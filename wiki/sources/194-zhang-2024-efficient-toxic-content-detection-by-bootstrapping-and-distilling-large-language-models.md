---
created: 2026-06-17
updated: 2026-06-17
tags: [paper, deep-ingest-v2, hate-speech, implicit, llm-reasoning, prompting, benchmark, explainability]
sources: [raw/sources/07936-AAAI24.ZhangJ-SRRAI.pdf]
---

# Zhang 等 - 2024 - Efficient Toxic Content Detection by Bootstrapping and Distilling Large Language Models

## Metadata
- Source file: `raw/sources/07936-AAAI24.ZhangJ-SRRAI.pdf`
- Year: 2024
- Venue: AAAI 2024
- Pages: 9
- Ingest level: deep-ingest-v2 (DToT and distillation pass; method, evaluation, and limitations checked)

## Problem Framing
- The paper targets toxic content detection broadly, including hate speech, biased content, sexual content, violent content, and bullying.
- It frames two practical problems: prompt-based LLM detection is costly and prompt-sensitive, while fine-tuned smaller models often lack transferability and rationales.

## Method
- Proposes BD-LLM, a bootstrapping-and-distillation pipeline.
- The core prompting method is Decision-Tree-of-Thought (`DToT`): when the model response is low-confidence, a confidence checker and context selector choose a more fine-grained context from a predefined context tree and re-prompt the LLM.
- DToT can be combined with few-shot demonstrations and rationale augmentations.
- The generated labels and rationales are then used to fine-tune smaller student language models.

## Data and Evaluation Setup
- Evaluates on ToxiGen, SBIC, DHate, and a private Amazon toxic-content dataset.
- Compares DToT against CoT, UniLC, and fine-tuned RoBERTa-style baselines.
- Evaluates both inference-time prompting and student-model distillation with or without LLM-generated rationales.

## Results and Claims
- Reports that DToT improves LLM detection over CoT and that student models trained with DToT rationales outperform label-only and CoT-rationale distillation baselines.
- Also reports stronger cross-dataset transfer after rationale-based distillation.
- Exact table values should be visually verified before using them as publication-grade numbers.

## Local Transfer to IHC/SBIC Work
- The key transferable mechanism is confidence-gated context refinement: use extra reasoning or retrieval only when the initial classifier is uncertain.
- The distillation step is especially relevant if ReAct-style verification is too slow for full inference; traces can become training signals or compact features for a smaller verifier.
- For the local IHC work, DToT supports a bounded design: no always-on long reasoning, no uncontrolled prompt expansion, and no claim that rationales are faithful unless separately evaluated.

## Limitations and Follow-ups
- The context tree is predefined and greedily searched, so it may miss globally better context choices.
- The paper is about broad toxic content detection rather than only hate speech or target-relation grounding.
- DToT rationales improve performance in their setup, but they are not automatically faithful explanations of why a local classifier should change its label.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[explainable-hate-speech-detection]]
- [[llm-reasoning]]
- [[hate-speech-source-hub]]
