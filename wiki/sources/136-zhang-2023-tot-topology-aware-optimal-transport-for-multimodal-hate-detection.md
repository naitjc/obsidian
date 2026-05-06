---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, benchmark, contrastive-learning, causal, explainability]
sources: [raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf]
---

# Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection

## Metadata
- Source file: `raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf`
- Year: 2023
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Multimodal hate detection must identify implicit harmful meaning when explicit hateful text or obvious demographic visual cues are absent.
- The paper argues that cross-modal attention alone does not fully handle modality gaps or provide interpretable alignment.
- The key problem is implicit image-text alignment for harmful meme reasoning.

## Method
- Proposes TOT, a topology-aware optimal transport framework for multimodal hate detection.
- Uses optimal transport to model cross-modal alignment and topology reasoning to capture inner-modal correlations.
- Designed to make implicit harm detection more interpretable than opaque cross-modal attention alone.

## Data and Evaluation Setup
- Evaluates on Harm-C and Harm-P benchmark settings with 2-class and 3-class variants.
- Metrics include accuracy, F1, and MMAE.
- Publication-checked priority values are tracked in [[hate-speech-metrics-matrix]].

## Results and Claims
- TOT reports strong gains on the evaluated Harm-C and Harm-P settings.
- Publication-checked values include 2-class Harm-C Acc/F1/MMAE 87.01/85.93/0.1634; 2-class Harm-P 91.55/91.29/0.1245; 3-class Harm-C 82.76/55.38/0.5027; 3-class Harm-P 88.61/71.54/0.6697.
- The evidence supports topology-aware cross-modal alignment for implicit multimodal hate; it should not be merged into a global hateful meme ranking without matching datasets and label schemas.

## Limitations and Follow-ups
- The method is evaluated in specific Harm-C/Harm-P settings; transfer to newer meme distributions remains a separate question.
- Interpretability claims should be checked through the paper's visual analysis rather than inferred from metrics alone.
- Exact priority values are publication-checked in [[hate-speech-metrics-matrix]].

## Structured Signals
- Detected method keywords: contrastive-learning, causal, multimodal, explainability
- Mentioned datasets: hateful memes, twitter
- Mentioned metrics: f1, macro-f1, accuracy


## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
