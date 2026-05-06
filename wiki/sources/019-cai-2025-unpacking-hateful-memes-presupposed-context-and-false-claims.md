---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, graph, prompting, explainability]
sources: [raw/sources/Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims.pdf]
---

# Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims

## Metadata
- Source file: `raw/sources/Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Investigates what makes hateful memes hateful rather than only improving black-box classification.
- Argues that hateful memes often combine presupposed evaluative context with false or misleading claims.
- Frames hateful meme detection as requiring multimodal context, cultural knowledge, and reference understanding.

## Method
- Develops PCM to model presupposed context across image and text.
- Introduces FACT to detect false claims using external knowledge and cross-modal reference graphs.
- Combines PCM and FACT into SHIELD, a hateful meme detection framework informed by philosophical and psychological accounts of hate.

## Data and Evaluation Setup
- Evaluates SHIELD on hateful meme detection datasets and reports additional transfer to related tasks such as fake news detection.
- Uses image-text examples to distinguish presupposed context alone, false claims alone, and their combination.
- Compares against state-of-the-art hateful meme detection methods across datasets and metrics.

## Results and Claims
- Claims SHIELD outperforms existing methods across evaluated hateful meme datasets and metrics.
- Shows that presupposed context and false claims are complementary rather than individually sufficient signals.
- Reports broader versatility beyond hateful memes, including fake news detection, in the extracted claims.

## Limitations and Follow-ups
- The framework depends on external knowledge and reference-graph quality.
- Cultural and historical knowledge requirements may limit robustness across communities or rapidly evolving memes.
- Verify exact dataset scores and ablation results before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: multimodal hate detection, external knowledge, graph, explainability
- Mentioned datasets: hateful meme datasets, fake news task
- Mentioned metrics: accuracy, F1, benchmark metrics

## Abstract (Extracted)
> The paper argues that hateful memes are characterized by presupposed context and false claims. It proposes SHIELD, combining a presupposed-context module with a false-claim module using external knowledge and cross-modal reference graphs.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
