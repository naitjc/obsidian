---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, sarcasm, llm-reasoning, emotion-recognition, prompting, synthetic-data, retrieval, benchmark, graph, causal]
sources: [raw/sources/Qiu 等 - 2025 - Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning.pdf]
---

# Qiu 等 - 2025 - Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning

## Metadata
- Source file: `raw/sources/Qiu 等 - 2025 - Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning.pdf`
- Year: 2025
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- This paper focuses on sarcasm detection, which job by rejoining the Paris Agreement(PA).
- sive understanding of the semantics in the state- 2. Trump aborted the PA in 2017, Trump amod hostile emotio a na m l in o co d ngrutiy Biden
- Figure 1: A sarcasm detection example that needs a
- we first employ retrieval-augmented large lan- sarcasm detection is to discern subtle incongruity

## Method
- Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning
- vey criticism, mockery, or other negative senti- Commonsense Augmentation Incongruity Reasoning
- ment opposite to the literal meaning. To detect Inference Subgraphs
- good commonsense reasoning ability to identify the
- we first employ retrieval-augmented large lan- sarcasm detection is to discern subtle incongruity

## Data and Evaluation Setup
- of the detector. Experiments conducted on five
- datasets demonstrate the effectiveness of EICR.
- 2024) as augmented tools. However, KGs are usu- experimental results from five datasets demonstrate
- due to their reliance on implicitly parametric knowl-
- • We conduct extensive experiments on the five

## Results and Claims
- narios, leading to unsatisfactory performance.
- the given statement. This task holds significant refers to the well-established fact and emotional
- improves the quality of knowledge provided to the sense augmentation, graph-based incongruity rea-
- to improve the quality of generated commonsense
- bust performance by integrating both perspectives. We conducted experiments with qualitative and

## Limitations and Follow-ups
- or pre-trained language models PLMs (Yao et al., feature space to mitigate the word biases. Extensive
- PLMs suffer from hallucinations (Wei et al., 2024)
- • We point out the challenges of providing reli-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph, causal
- Mentioned datasets: SemEval, ATIS, TOP, Persona
- Mentioned metrics: accuracy, acc, macro-f1, f1

## Benchmark Evidence Lines
- datasets demonstrate the effectiveness of EICR.
- 2024) as augmented tools. However, KGs are usu- experimental results from five datasets demonstrate
- public datasets to evaluate the rationality and
- depend solely on uninterpretable high-dimensional We first give the problem definition of sarcasm de-
- dictable results and deteriorating their robustness. we utilize a retrieval-augmented GPT-4o to provide
- into an undirected graph using Spacy, denoted as Datasets #Train #Test #Avg.Len %Sarcasm
- Table 1: Statistics of datasets. #Avg.Len denotes the
- sd is used for classification as Eq.(10), We conducted our experiments on five benchmark

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
