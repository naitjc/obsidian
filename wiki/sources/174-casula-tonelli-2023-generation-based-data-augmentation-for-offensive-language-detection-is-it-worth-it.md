---
created: 2026-05-27
updated: 2026-05-27
tags: [paper, deep-ingest-v2, hate-speech, synthetic-data, benchmark, bias]
sources: [raw/sources/2023.eacl-main.244.pdf]
---

# Casula 和 Tonelli - 2023 - Generation-Based Data Augmentation for Offensive Language Detection Is It Worth It

## Metadata
- Source file: `raw/sources/2023.eacl-main.244.pdf`
- Year: 2023
- Venue: EACL 2023
- Pages: 19
- Ingest level: deep-ingest-v2 (synthetic-data utility pass; first page visually checked)

## Problem Framing
- Generated augmentation is often proposed for offensive language detection, especially in low-resource settings.
- Existing positive reports leave uncertainty about cross-dataset robustness and whether generation injects lexical biases.
- The paper tests whether potential gains survive changes in source dataset, data scale, generation setup, and filtering threshold.

## Method
- Studies multiple generative data augmentation configurations for offensive-language classification.
- Tests within-dataset and cross-dataset training/evaluation, two low-resource starting sizes, four generation setups, and filtering thresholds.
- Performs a qualitative lexical-bias analysis and functional testing with HateCheck.

## Data and Evaluation Setup
- Evaluates on four English offensive-language resources, including OLID, SOLID, and SBIC as identified in the paper.
- Uses HateCheck functional tests to examine behavior beyond aggregate classification metrics.
- Compares generated augmentation with baseline training and oversampling conditions.

## Results and Claims
- Finds that gains from generative data augmentation are unreliable across datasets and setups.
- Reports that generated augmentation can have unpredictable effects on lexical bias and can improve some functional tests while worsening others.
- This is a direct caution for completed IHC/SBIC fields or generated statements: generated training content requires untouched test evaluation and shortcut diagnostics.

## Limitations and Follow-ups
- The study concerns generated offensive-language examples, not generated target annotations or relation labels.
- Exact table values and per-dataset comparisons should be checked before quantitative citation.
- Follow-up use: supports utility and bias controls in [[missing-annotation-completion-and-utility-literature-map]] and [[synthetic-data-generation]].

## Structured Signals
- Detected method keywords: generative augmentation, offensive language detection, lexical bias, functional testing, cross-dataset evaluation
- Mentioned datasets: OLID, SOLID, SBIC, HateCheck
- Mentioned metrics: classification performance, functional test outcomes, token association analysis

## Related Concepts
- [[synthetic-data-generation]]
- [[missing-annotation-completion-and-utility-literature-map]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-source-hub]]
