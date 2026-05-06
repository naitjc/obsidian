---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, sentiment-analysis, benchmark]
sources: [raw/sources/Lin 等 - 2019 - Deep Mask Memory Network with Semantic Dependency and Context Moment for Aspect Level Sentiment Clas.pdf]
---

# Lin 等 - 2019 - Deep Mask Memory Network with Semantic Dependency and Context Moment for Aspect Level Sentiment Clas

## Metadata
- Source file: `raw/sources/Lin 等 - 2019 - Deep Mask Memory Network with Semantic Dependency and Context Moment for Aspect Level Sentiment Clas.pdf`
- Year: 2019
- Pages: 7
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Aspect level sentiment classification aims at iden-
- paper, we propose a novel framework for aspect
- context moment learning task, which aims to learn
- begun to be used in natural language processing tasks [Bah-

## Method
- Early methods for aspect-based sentiment analysis mostly
- adopted supervised learning approaches with hand-crafted
- paper, we propose a novel framework for aspect
- a simpler and easily-parallelized model based on CNNs and

## Data and Evaluation Setup
- Datasets, and the experimental results show that our
- The experiments on Sem Eval 2014 Datasets clearly show that and “food” if we know the sentiment of the sentence is posi-
- al., 2017] proposed a recurrent attention network which used ble, which can be pre-trained by unsupervised methods like
- The model is finally trained by minimizing the sum of

## Results and Claims
- are achieved, the relation information among as-
- ically, achieving promising results on the aspect level sen-
- Datasets, and the experimental results show that our
- model achieves a state-of-the-art performance.

## Limitations and Follow-ups
- Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence (IJCAI-19)
- Deep Mask Memory Network with Semantic Dependency and Context Moment
- Peiqin Lin1 , Meng Yang1;2 and Jianhuang Lai1
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: synthetic-data, retrieval, benchmark, sentiment-analysis
- Mentioned datasets: SemEval, TOP, Twitter
- Mentioned metrics: accuracy, acc, f1, macro-f1, em

## Abstract (Extracted)
> is “service”. It’s obvious that the same sentence may have different sentiment polarity for different opinion aspects. Aspect level sentiment classification aims at iden- Early methods for aspect-based sentiment analysis mostly tifying the sentiment of each aspect term in a sen- adopted supervised learning approaches with hand-crafted tence. Deep memory networks often use location features [Rao and Ravichandran, 2009; Jiang et al., 2011; information between context word and aspect to Perez-Rosas et al., 2012; Kiritchenko et al., 2014; Vo and generate the memory. Although improved results Zhang, 2015]. However, the performance of these models is are achieved, the relation information among as- highly dependent on the quality of features and feature engi- pects in the same sentence is ignored and the word neering is labor intensive. location can’t bring enough and accurate informa- In rece

## Related Concepts
- [[sentiment-analysis]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
