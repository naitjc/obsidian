---
created: 2026-06-01
updated: 2026-06-01
tags: [paper, deep-ingest-v2, hate-speech, implicit, llm-reasoning, prompting, benchmark, explainability]
sources: [raw/sources/2025.emnlp-main.296.pdf]
---

# Chen 和 Wang - 2025 - Pragmatic Inference Chain Improving LLMs' Reasoning of Authentic Implicit Toxic Language

## Metadata
- Source file: `raw/sources/2025.emnlp-main.296.pdf`
- Year: 2025
- Venue: EMNLP 2025 Main
- Pages: 16
- Ingest level: deep-ingest-v2 (pragmatic-inference pass; first three pages checked)

## Problem Framing
- Authentic implicit toxic language can evade censorship and require context-dependent inference rather than surface keyword matching.
- The required inference may depend on intentions, signs, social experience, and context rather than logical deduction alone.

## Method
- Introduces Pragmatic Inference Chain (`PIC`), an in-context prompting method adapted from relevance theory.
- Compares PIC prompt variants with zero-shot, few-shot, chain-of-thought, rule-based, and combined baselines.

## Data and Evaluation Setup
- Constructs a Chinese dataset of inference-intensive toxic online interactions from Weibo and RedNote.
- The inspected text reports 3,097 gender-targeted post-comment pairs and expert annotation of inferential processes for a subset.
- Evaluates several LLMs, including GPT-4o, Llama-3.1-70B-Instruct, DeepSeek-v2.5, DeepSeek-v3, and QwQ32b.

## Results and Claims
- Reports improved detection success rates and more explicit, coherent reasoning processes under PIC prompting.
- The relevant local transfer is that implicit rows may need pragmatic cues beyond literal target spans.
- Exact table values require verification before external citation.

## Limitations and Follow-ups
- The dataset focuses on Chinese gender-targeted interactions and context-comment pairs; direct transfer to English IHC/SBIC must be tested.
- Long reasoning traces should remain optional until they improve relation-grounded evaluation beyond compact outputs.

## Related Concepts
- [[p0-target-grounding-reading-synthesis-2026-06-01]]
- [[leakage-resistant-target-relation-modeling]]
- [[llm-reasoning]]
- [[hate-speech-source-hub]]

