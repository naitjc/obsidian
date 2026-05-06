---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, graph, prompting, explainability]
sources: [raw/sources/Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers.pdf]
---

# Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers

## Metadata
- Source file: `raw/sources/Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers.pdf`
- Year: 2025
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Shifts hate detection from isolated posts to user- and community-level detection of hatemongers.
- Argues that user-level aggregation can reveal coded language and hate-group dynamics that post-level classifiers miss.
- Frames online hate as a social phenomenon promoted by communities rather than only individual utterances.

## Method
- Uses a multimodal aggregative approach for detecting hate-promoting users.
- Aggregates textual and potentially social or profile-level signals rather than classifying a single utterance alone.
- Compares classifier and large-model judgments on examples of hate-promoting content.

## Data and Evaluation Setup
- Evaluates hate-promoting text and user-level signals with several classifiers and LLM-style baselines.
- Includes examples where coded or ambiguous statements require context beyond a single sentence.
- Positions the task as efficient detection of hatemongers for analysis and moderation support.

## Results and Claims
- Claims user-level multimodal aggregation is useful for identifying hatemongers.
- Shows that sentence-level systems can disagree on nuanced or coded hate-promoting examples.
- Exact model comparisons should be checked against source tables before citation.

## Limitations and Follow-ups
- User-level detection can raise fairness and privacy concerns and depends on available activity history.
- Aggregated signals may conflate hateful identity with community membership or topical discussion.
- Verify exact metrics, dataset definitions, and labeling criteria before citing quantitative results.

## Structured Signals
- Detected method keywords: user-level hate detection, multimodal aggregation, hatemonger detection
- Mentioned datasets: online hate datasets, classifier examples
- Mentioned metrics: classification scores, model agreement

## Abstract (Extracted)
> The paper argues for detecting hate at the user or community level, not only the post level. It proposes an efficient multimodal aggregation approach for identifying hatemongers and studying hate as a social phenomenon.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
