---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, zero-shot, few-shot, prompting, benchmark]
sources: [raw/sources/2505.06149v3.pdf]
---

# Ghorbanpour 等 - 2025 - Can Prompting LLMs Unlock Hate Speech Detection across Languages

## Metadata
- Source file: `raw/sources/2505.06149v3.pdf`
- Year: 2025
- Venue: arXiv
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Evaluates whether multilingual instruction-tuned LLMs can detect hate speech across non-English languages without fine-tuning.
- Targets the gap between English-centric hate speech modeling and multilingual social media moderation.
- Compares prompting to fine-tuned encoder models under both real-world datasets and functional hate speech tests.

## Method
- Tests multiple prompting strategies: vanilla, classification, chain-of-thought, NLI-style, language-aware, role-play, translate-then-classify, definition-based, distinction-based, few-shot, and combinations.
- Evaluates instruction-tuned LLMs including LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Aya-101, and BloomZ-7B1.
- Fine-tunes encoder baselines including XLM-T and mDeBERTa.

## Data and Evaluation Setup
- Languages: Arabic, French, Spanish, Hindi, Italian, Portuguese, German, and Turkish.
- Real-world datasets include OUS19_AR, OUS19_FR, BAS19_ES, HAS21_HI, SAN20_IT, FOR19_PT, Gahd24_DE, and Xdomain_TR.
- Functional evaluation uses multilingual HateCheck-style test suites.
- Reports macro-F1 over repeated inference runs and compares against fine-tuned encoders.

## Results and Claims
- Prompt design strongly affects performance, and the best prompt type varies by language and model.
- Few-shot prompting usually improves over zero-shot prompting, especially on functional tests.
- Fine-tuned encoder models generally outperform prompted LLMs on real-world datasets when enough labeled data is available.
- Prompted LLMs can generalize better on controlled functional tests and can be competitive when training data is very limited.

## Limitations and Follow-ups
- The study focuses on text-only explicit hate labels and does not use extra context beyond the post text.
- Prompt search is broad but not exhaustive; prompt wording and decoding settings remain potential confounders.
- Follow-up use: pair with [[153-mnassri-2025-rag-and-recall-multilingual-hate-speech-detection-with-semantic-memory]] to compare prompting-only, retrieval-augmented, and fine-tuned multilingual strategies.

## Structured Signals
- Detected method keywords: multilingual prompting, zero-shot, few-shot, chain-of-thought, role-play, translate-then-classify, encoder fine-tuning
- Mentioned datasets: OUS19_AR, OUS19_FR, BAS19_ES, HAS21_HI, SAN20_IT, FOR19_PT, Gahd24_DE, Xdomain_TR, HateCheck
- Mentioned metrics: macro-F1, real-world test performance, functional test performance

## Related Concepts
- [[hate-speech-generalization-and-transfer]]
- [[zero-shot-learning]]
- [[hate-speech-datasets-and-benchmarks]]
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
