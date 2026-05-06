---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, causal, retrieval, prompting]
sources: [raw/sources/Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label.pdf]
---

# Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label

## Metadata
- Source file: `raw/sources/Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label.pdf`
- Year: 2025
- Pages: 19
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets hate-speech detection when labeled data is limited, especially for low-resource or under-annotated languages.
- Notes that collecting hate-speech labels is expensive, slow, and culturally sensitive.
- Frames cross-lingual retrieval as a scalable alternative to manually selecting source languages or tasks.

## Method
- Embeds multilingual hate-speech instances and retrieves nearest neighbors for a small target-language training set.
- Combines retrieved cross-lingual samples with limited target-language data to fine-tune a multilingual model.
- Uses maximum marginal relevance to reduce redundant retrieved examples.

## Data and Evaluation Setup
- Evaluates on eight languages with limited labeled target-language data.
- Retrieves from a multilingual pool built from fourteen hate-speech detection tasks.
- Compares against training only on the target-language examples and other transfer settings.

## Results and Claims
- Reports consistent improvements over target-only training in the limited-label setting.
- Finds that redundancy filtering with MMR improves performance in some languages.
- Exact language-level scores should be checked in the original tables before citation.

## Limitations and Follow-ups
- Retrieval effectiveness depends on embedding quality and multilingual pool coverage.
- Cross-lingual transfer can miss language-specific hate expressions and cultural context.
- Verify exact metrics, language splits, and retrieval-pool composition before citing quantitative claims.

## Structured Signals
- Detected method keywords: cross-lingual retrieval, limited labels, multilingual transfer, hate-speech detection
- Mentioned datasets: multilingual hate-speech datasets across eight languages
- Mentioned metrics: F1, macro-F1, language-level performance

## Abstract (Extracted)
> The paper proposes a data-efficient cross-lingual retrieval method for hate-speech detection with limited labeled data. It retrieves related multilingual examples, combines them with target-language data, and fine-tunes a multilingual model.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
