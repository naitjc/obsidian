---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, benchmark, contrastive-learning, graph, prompting, explainability]
sources: [raw/sources/Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection.pdf]
---

# Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection

## Metadata
- Source file: `raw/sources/Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets multimodal hate detection where hate may depend on implicit cues, cross-modal interactions, and diverse target groups.
- Highlights cross-modal-induced hate, where neither text nor image alone is hateful but their combination is.
- Argues that prompt-based inference and hypergraph fusion can better capture complex multimodal hate cues.

## Method
- Proposes HyperHatePrompt, a hypergraph-based prompting fusion model.
- Uses tailored prompts to infer implicit hateful cues.
- Builds hyperedges to model cross-modal-induced hate and diverse target-group relations before hypergraph convolution.

## Data and Evaluation Setup
- Evaluates on multimodal hate detection datasets involving image-text content.
- Compares hypergraph prompting fusion against multimodal baselines.
- Includes analysis of implicit cues, cross-modal hate, and target-group diversity.

## Results and Claims
- Claims improved multimodal hate detection by modeling implicit cues and cross-modal interactions.
- Positions hypergraph fusion as useful for representing relations among modalities and hate cues.
- Exact dataset scores and ablations require original-table verification before citation.

## Limitations and Follow-ups
- Prompt quality and hypergraph construction choices can affect robustness.
- The method may depend on dataset coverage of target groups and cross-modal hate patterns.
- Verify exact metrics, dataset settings, and ablation results before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: multimodal hate detection, hypergraph, prompting, implicit hateful cues
- Mentioned datasets: multimodal hate datasets
- Mentioned metrics: accuracy, F1, benchmark performance

## Abstract (Extracted)
> HyperHatePrompt is a hypergraph-based prompting fusion model for multimodal hate detection. It infers implicit hateful cues and models cross-modal-induced hate and diverse target groups through hypergraph fusion.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
