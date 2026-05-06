---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, graph, sentiment-analysis, benchmark]
sources: [raw/sources/Grover 等 - 2022 - Public Wisdom Matters! Discourse-Aware Hyperbolic Fourier Co-Attention for Social-Text Classificatio.pdf]
---

# Grover 等 - 2022 - Public Wisdom Matters! Discourse-Aware Hyperbolic Fourier Co-Attention for Social-Text Classificatio

## Metadata
- Source file: `raw/sources/Grover 等 - 2022 - Public Wisdom Matters! Discourse-Aware Hyperbolic Fourier Co-Attention for Social-Text Classificatio.pdf`
- Year: 2022
- Pages: 19
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- adequate for such tasks; therefore, recent methods attempted to incorporate other
- to generalise the social-text classification tasks by incorporating public discourse.
- Extensive experiments on four different social-text classification tasks, namely
- ing texts shared on social media (aka social-texts) are indispensable for multiple tasks – online

## Method
- adequate for such tasks; therefore, recent methods attempted to incorporate other
- intrinsic signals such as user behavior and the underlying graph structure.
- State-of-the-art methods on social-text classification tend to ig-
- We parse public discourse as an Abstract Meaning Representation (AMR) graph

## Data and Evaluation Setup
- Extensive experiments on four different social-text classification tasks, namely
- alises well, and achieves state-of-the-art results on ten benchmark datasets.
- also employ a sentence-level fact-checked and annotated dataset to evaluate how
- Figure 1: A motivating example (taken from our dataset) showing how user comments act as anal-

## Results and Claims
- State-of-the-art methods on social-text classification tend to ig-
- alises well, and achieves state-of-the-art results on ten benchmark datasets.
- the-art results across all datasets when compared with a suite of generic and data-specific baselines.
- also deliver benchmark results on generic social-

## Limitations and Follow-ups
- The performance of most of these models deteriorate when extended to multiple tasks and fail to
- Hyphen overcomes these limitations of the existing methods.
- However, for social-text classification, none of the above approaches simultane-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, synthetic-data, graph, benchmark, sentiment-analysis, sarcasm
- Mentioned datasets: SemEval, ATIS, TOP, Twitter, Reddit, MR
- Mentioned metrics: acc, f1, precision, recall, em

## Abstract (Extracted)
> Meaning Representation (AMR) graph and use the powerful hyperbolic geometric representation to model graphs with hierarchical structure. Finally, we equip it with a novel Fourier co-attention mech- anism to capture the correlation between the source post and public discourse. Extensive experiments on four different social-text classification tasks, namely detecting fake news, hate speech, rumour, and sarcasm, show that Hyphen gener- alises well, and achieves state-of-the-art results on ten benchmark datasets. We also employ a sentence-level fact-checked and annotated dataset to evaluate how Hyphen is capable of producing explanations as analogous evidence to the final prediction. Code is available at: https://github.com/LCS2-IIITD/Hyphen.

## Related Concepts
- [[llm-reasoning]]
- [[sentiment-analysis]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
