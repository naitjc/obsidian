---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf]
---

# Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes

## Metadata
- Source file: `raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf`
- Year: 2026
- Pages: 20
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Just KIDDIN’ : Knowledge Infusion and Distillation for Detection of
- task due to the complex contextual connections
- tively in HatefulMemes Benchmark across vari- Figure 1: Given a meme, we aim to derive the answer by
- contextual complexity of the toxicity detection

## Method
- tively in HatefulMemes Benchmark across vari- Figure 1: Given a meme, we aim to derive the answer by
- ants. Further, KID-VLM demonstrates better joint reasoning over the knowledge from LVLM, the KG
- plicit evaluations can misinterpret tone or intent Net, constructing a joint graph that combines the
- such as PromptHate (Cao et al., 2022a) and Hate-
- pend only on training data and pre-trained mod- the KID-VLM framework by consistently outper-

## Data and Evaluation Setup
- state-of-the-art baselines across AUC, and F1,
- tively in HatefulMemes Benchmark across vari- Figure 1: Given a meme, we aim to derive the answer by
- plicit evaluations can misinterpret tone or intent Net, constructing a joint graph that combines the
- els, which limits their ability to capture complex forming the baselines. Error analysis and ablation
- 2023), achieve comparable performance but re- 0.5% in F1 and AUC, respectively. Further, our

## Results and Claims
- state-of-the-art baselines across AUC, and F1,
- with improvements of 0.5%, and 10.6%, respec-
- generalizability and achieves best performance (green box), and reason over toxicity (red box).
- (Alayrac et al., 2022) and LENS (Berrios et al., infusion, providing improvements of 10.6% and
- 2023), achieve comparable performance but re- 0.5% in F1 and AUC, respectively. Further, our

## Limitations and Follow-ups
- els, which limits their ability to capture complex forming the baselines. Error analysis and ablation
- these limitations by leveraging ConceptNet (Speer
- single vector representing the entire working graph resource limitations, while fewer than 250 nodes
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, benchmark, graph
- Mentioned datasets: ATIS, TOP, HatefulMemes, ECHO
- Mentioned metrics: accuracy, acc, f1, precision, recall, auc

## Benchmark Evidence Lines
- mark datasets show the superior performance
- state-of-the-art baselines across AUC, and F1,
- tively in HatefulMemes Benchmark across vari- Figure 1: Given a meme, we aim to derive the answer by
- across all baselines in HarMeme Dataset with
- an 6.3% and 3.2% in F1 and AUC. Given the
- plicit evaluations can misinterpret tone or intent Net, constructing a joint graph that combines the
- 2023), achieve comparable performance but re- 0.5% in F1 and AUC, respectively. Further, our
- struggle to effectively address nuanced or context- the HarMeme Dataset, where we beat all baselines

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
