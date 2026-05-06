---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, graph, benchmark]
sources: [raw/sources/Agarwal 等 - 2023 - GASCOM Graph-based Attentive Semantic Context Modeling for Online Conversation Understanding.pdf]
---

# Agarwal 等 - 2023 - GASCOM Graph-based Attentive Semantic Context Modeling for Online Conversation Understanding

## Metadata
- Source file: `raw/sources/Agarwal 等 - 2023 - GASCOM Graph-based Attentive Semantic Context Modeling for Online Conversation Understanding.pdf`
- Year: 2023
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- NLP problem which has many useful applications (e.g., hate speech
- understanding is an important yet challenging NLP problem which
- In this paper, we propose a Graph-based Attentive Semantic
- well-studied problems: polarity prediction and hate speech detec-

## Method
- GASCOM: Graph-based Attentive Semantic Context Modeling for
- based Attentive Semantic Context Modeling for Online Conversation Un-
- In this paper, we propose a Graph-based Attentive Semantic
- COntext Modeling (GASCOM) framework for online conversation polarity prediction [2, 3, 20].

## Data and Evaluation Setup
- Experimental results also show that Manning [41]) to predict the polarity of replies on the now-defunct
- parameters depend upon the dataset and therefore, needs to be me to take them out for valentine's day.
- Further- Figure 1: An example conversation from Guest dataset.
- the probability scores in the stationary distribution of the random similarity score is computed using a pre-trained Sentence-BERT

## Results and Claims
- Our proposed framework significantly outperforms state-of-
- the-art methods on both tasks, improving macro-F1 scores by 4.5%
- performs state-of-the-art methods on two very important context of persuasive essays or political debates.
- Experimental results also show that Manning [41]) to predict the polarity of replies on the now-defunct

## Limitations and Follow-ups
- However, online conversations typically unfold over a derstanding.
- However, this has not been [9] Johan Bos and Katja Markert.
- GASCOM makes use of conversation context from surrounding RTE Challenge.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, synthetic-data, retrieval, graph, benchmark, sentiment-analysis
- Mentioned datasets: ATIS, TOP, Twitter
- Mentioned metrics: accuracy, acc, f1, macro-f1, precision, recall, auc, em

## Abstract (Extracted)
> ACM Reference Format: Online conversation understanding is an important yet challenging Vibhor Agarwal, Yu Chen, and Nishanth Sastry. 2023. GASCOM: Graph- based Attentive Semantic Context Modeling for Online Conversation Un- NLP problem which has many useful applications (e.g., hate speech detection). However, online conversations typically unfold over a derstanding. In Proceedings of Preprint. Under Review. (Preprint). ACM, New York, NY, USA, 10 pages. https://doi.org/XXXXXXX.XXXXXXX series of posts and replies to those posts, forming a tree structure within which individual posts may refer to semantic context from higher up the tree. Such semantic cross-referencing makes it diffi- cult to understand a single post by itself; yet considering the entire

## Related Concepts
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
