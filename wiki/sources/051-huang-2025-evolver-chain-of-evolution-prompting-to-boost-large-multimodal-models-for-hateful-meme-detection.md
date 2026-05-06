---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection.pdf]
---

# Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection

## Metadata
- Source file: `raw/sources/Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection.pdf`
- Year: 2025
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses hateful memes as evolving cultural artifacts, where new memes blend older visual and textual ideas.
- Argues that static training-heavy methods struggle with rapidly changing meme contexts.
- Frames interpretability and evolutionary context as important for hateful meme detection.

## Method
- Proposes Evolver, a Chain-of-Evolution prompting approach for large multimodal models.
- Uses an evolutionary pair mining module to retrieve or construct related meme evolution context.
- Prompts LMMs to reason step by step over meme evolution and expression.

## Data and Evaluation Setup
- Builds or uses a hateful meme detection benchmark tailored to LMM evaluation.
- Compares Evolver with conventional two-stream and LMM-based baselines.
- Assesses both detection performance and interpretability of evolutionary reasoning.

## Results and Claims
- Claims Evolver improves hateful meme detection by modeling meme evolution and context.
- Positions Chain-of-Evolution prompting as more adaptable to emerging meme variants than static training-only methods.
- Exact benchmark scores and ablations require original-table verification before citation.

## Limitations and Follow-ups
- Evolutionary context mining may fail for novel or poorly represented meme families.
- Prompt-based reasoning depends on the selected LMM and retrieved examples.
- Verify exact metrics, benchmark construction, and ablation settings before citing quantitative claims.

## Structured Signals
- Detected method keywords: hateful memes, large multimodal models, chain-of-evolution prompting, interpretability
- Mentioned datasets: hateful meme benchmarks
- Mentioned metrics: accuracy, F1, AUC, benchmark performance

## Abstract (Extracted)
> Evolver uses Chain-of-Evolution prompting to help large multimodal models detect hateful memes. It models how memes evolve and express hate, using evolutionary context to improve detection and interpretability.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
