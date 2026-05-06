---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, emotion-recognition, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Shen 等 - 2025 - CoE A Clue of Emotion Framework for Emotion Recognition in Conversations.pdf]
---

# Shen 等 - 2025 - CoE A Clue of Emotion Framework for Emotion Recognition in Conversations

## Metadata
- Source file: `raw/sources/Shen 等 - 2025 - CoE A Clue of Emotion Framework for Emotion Recognition in Conversations.pdf`
- Year: 2025
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- is often limited by challenges in interpreting Please select the emotional label of Chandler's statement:
- tional clues to enhance the ERC task. Build- Chandler: known for his wit and
- reasoning tasks, each targeting different as-
- strate that CoE consistently outperforms state- in the ERC task, where contextual information (e.g.,

## Method
- CoE: A Clue of Emotion Framework for Emotion Recognition in
- reasoning tasks, each targeting different as-
- ing and enhancing the model’s ability to in- The emotional label for Chandler’s statement is Joyful.
- on EmoryNLP, MELD, and IEMOCAP demon- Figure 1: This figure illustrates the CoE framework
- ment on EmoryNLP. These results underscore role-playing, speaker identification, and reasoning) on

## Data and Evaluation Setup
- through textual and parametric optimizations.
- out in-depth experiments on multiple auxiliary
- Our experimental findings highlight important retrieval-based instruction-following task, achiev-
- emotion analysis. The consistent performance im- datasets that rival previous baselines (Lei et al.,
- provements across multiple benchmarks suggest 2023). General purpose LLMs such as ChatGPT

## Results and Claims
- strate that CoE consistently outperforms state- in the ERC task, where contextual information (e.g.,
- of-the-art methods, achieving a 2.92% improve- Persona and Scene) on the left and auxiliary tasks (e.g.,
- as a significant research direction, driven by its po-
- tential applications to improve human-computer in-
- et al., 2017). Despite the remarkable performance

## Limitations and Follow-ups
- is often limited by challenges in interpreting Please select the emotional label of Chandler's statement:
- Recognizing the challenge of determining the 5.1.3 Training Setup
- Our experimental findings (Section 5.4) demon- constraints and time limitations, we employed the
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: MELD, IEMOCAP, ATIS, TOP, Persona
- Mentioned metrics: accuracy, f1, precision

## Benchmark Evidence Lines
- strate that CoE consistently outperforms state- in the ERC task, where contextual information (e.g.,
- fectively capture and analyze the nuances of dia- complex reasoning tasks, highlighting a notable re-
- the entire method using three ERC benchmark
- datasets, and the outstanding results demon-
- implications for the broader field of computational ing state-of-the-art zero-shot results on multiple
- emotion analysis. The consistent performance im- datasets that rival previous baselines (Lei et al.,
- provements across multiple benchmarks suggest 2023). General purpose LLMs such as ChatGPT
- recognition, while datasets such as KD-EmoR nally, we discuss the design of the training strategy

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
