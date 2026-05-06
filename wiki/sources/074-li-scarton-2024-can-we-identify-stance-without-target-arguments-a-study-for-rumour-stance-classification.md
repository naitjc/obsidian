---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, synthetic-data, retrieval, conversational, target-adaptive, bias, verification]
sources: [raw/sources/Li和Scarton - 2024 - Can We Identify Stance without Target Arguments A Study for Rumour Stance Classification.pdf]
---

# Li和Scarton - 2024 - Can We Identify Stance without Target Arguments A Study for Rumour Stance Classification

## Metadata
- Source file: `raw/sources/Li和Scarton - 2024 - Can We Identify Stance without Target Arguments A Study for Rumour Stance Classification.pdf`
- Year: 2024
- Pages: 8
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Considering a conversation thread, rumour stance classification aims to identify the opinion (e.g. agree or disagree)
- of replies towards a target (rumour story). Although the target is expected to be an essential component in
- traditional stance classification, we show that rumour stance classification datasets contain a considerable amount
- Keywords: rumour stance classification, rumour analysis on social media, stance classification

## Method
- performance of the supervised models without awareness of the target. We find that current target-aware models
- underperform in cases where the context of the target is crucial. Finally, we propose a simple yet effective framework
- to enhance reasoning with the targets, achieving state-of-the-art performance on two benchmark datasets.
- models without awareness of the target (dubbed
- guage Inference and Argument Reasoning Com- urally inferred without knowing the target.2 More

## Data and Evaluation Setup
- traditional stance classification, we show that rumour stance classification datasets contain a considerable amount
- to enhance reasoning with the targets, achieving state-of-the-art performance on two benchmark datasets.
- datasets. For instance, in Figure 1, one can rea-
- datasets, due to spurious sentiment- and lexicon-
- due to spurious or superficial cues in the datasets

## Results and Claims
- performance of the supervised models without awareness of the target. We find that current target-aware models
- to enhance reasoning with the targets, achieving state-of-the-art performance on two benchmark datasets.
- without awareness of the target, achieves com-
- parable or even better performance than target-
- to classify the stance of the tweets. We then com- 2019) achieved similar performance).

## Limitations and Follow-ups
- in rumour stance classification. Our study sug- dataset biases. In Proceedings of the 2019
- memory limitations, we reduce the batch size from same as experiments in fine-tuning the BERTweet.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, synthetic-data, retrieval, llm-reasoning, conversational, target-adaptive, bias, verification
- Mentioned datasets: SemEval, RumourEval, ARC, Twitter
- Mentioned metrics: none detected

## Abstract (Extracted)
> Considering a conversation thread, rumour stance classification aims to identify the opinion (e.g. agree or disagree) of replies towards a target (rumour story). Although the target is expected to be an essential component in traditional stance classification,

## Benchmark Evidence Lines
- to enhance reasoning with the targets, achieving state-of-the-art performance on two benchmark datasets.
- Table 1: Number of target-independent tweets in
- the specific rumour story (Table 1), especially in
- Table 2: Model performance over the full test set, target-dependent and -independent direct replies (av-
- Table 3: The proportion (%) of target-aware BERTweet predictions of direct replies in each class that are
- BERT (Yu et al., 2020), achieving state-of-the-art tion information, would perform significantly bet-
- when the source tweet is provided (LLaMA (source conversation-based system that outperforms the
- As shown in Table 2, not surprisingly, all the dependent denies may contribute to the good gen-

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[sentiment-analysis]]
