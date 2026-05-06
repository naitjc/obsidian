---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, prompting, explainability]
sources: [raw/sources/Hee 等 - 2024 - Recent Advances in Online Hate Speech Moderation Multimodality and the Role of Large Models.pdf]
---

# Hee 等 - 2024 - Recent Advances in Online Hate Speech Moderation Multimodality and the Role of Large Models

## Metadata
- Source file: `raw/sources/Hee 等 - 2024 - Recent Advances in Online Hate Speech Moderation Multimodality and the Role of Large Models.pdf`
- Year: 2024
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Surveys online hate-speech moderation in an environment where hate appears across text, images, audio, video, and memes.
- Argues that text-only surveys underrepresent the complexity of multimodal hate.
- Emphasizes the growing role of large language models and large multimodal models in moderation workflows.

## Method
- Organizes recent hate-speech moderation work by modality and model family.
- Reviews detection, explanation, debiasing, and counter-speech generation.
- Discusses how LLMs and LMMs affect both capabilities and risks in moderation.

## Data and Evaluation Setup
- Covers text-based, vision-language, and video/audio hate-speech settings.
- Uses representative datasets and recent model families as survey anchors.
- Compares technical moderation goals across detection, interpretability, bias mitigation, and response generation.

## Results and Claims
- Concludes that multimodal hate requires richer modeling than text-only detection.
- Identifies large models as useful but not sufficient for robust, fair, and context-sensitive moderation.
- Highlights gaps around bias, interpretability, evolving content, and cross-platform deployment.

## Limitations and Follow-ups
- As a survey, it synthesizes trends rather than providing a single benchmark result.
- Coverage depends on the included literature and may age quickly as large models change.
- Use primary source pages for exact benchmark values.

## Structured Signals
- Detected method keywords: survey, multimodal hate moderation, LLMs, LMMs, debiasing, counter-speech
- Mentioned datasets: Hateful Memes, SBIC, online hate-speech datasets
- Mentioned metrics: survey-level synthesis; no single benchmark metric

## Abstract (Extracted)
> This survey reviews recent online hate-speech moderation research with a focus on multimodal content and large models. It covers detection, explanation, debiasing, and counter-speech across text, images, audio, video, and memes.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
