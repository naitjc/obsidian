---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, retrieval, prompting, explainability]
sources: [raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf]
---

# Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin

## Metadata
- Source file: `raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Vision-language hate datasets are scarcer than text hate datasets, which makes multimodal hate detection harder to adapt and evaluate.
- The paper asks whether text-based hate speech examples can transfer useful knowledge to vision-language hate detection.
- The key framing is cross-modality transfer, not cross-lingual transfer.

## Method
- Uses few-shot in-context learning with large language models to test whether text hate demonstrations improve multimodal hate classification.
- Compares text-only demonstrations, vision-language demonstrations, and zero-shot settings.
- Treats shared hate-speech semantics as a bridge between textual and multimodal formats.

## Data and Evaluation Setup
- Evaluates cross-modality transfer using text hate support examples and vision-language hate test sets.
- The checked metrics focus on FHM and MAMI results under Latent Hatred and FHM support examples.
- Publication-checked values are tracked in [[hate-speech-metrics-matrix]].

## Results and Claims
- Text-based hate examples can improve few-shot multimodal hate detection, sometimes outperforming vision-language demonstrations.
- Publication-checked values include Mistral-7B and Qwen2-7B bests on FHM and MAMI under Latent Hatred and FHM support settings.
- The paper is evidence for cross-modality prompting and transfer, not for a general multimodal hate SOTA ranking.

## Limitations and Follow-ups
- The main limitation is whether text-based support examples cover the visual and cultural cues needed for unseen memes.
- Results should be interpreted by support set, model, and target dataset rather than collapsed into a single ranking.
- Exact priority values are publication-checked in [[hate-speech-metrics-matrix]].

## Structured Signals
- Detected method keywords: retrieval, prompting, multimodal, explainability
- Mentioned datasets: latent hatred, hateful memes, twitter
- Mentioned metrics: f1, accuracy

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
