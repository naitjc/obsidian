---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, emotion-recognition, zero-shot, prompting, retrieval, benchmark, graph, causal]
sources: [raw/sources/Fu 等 - 2025 - LaERC-S Improving LLM-based Emotion Recognition in Conversation with Speaker Characteristics.pdf]
---

# Fu 等 - 2025 - LaERC-S Improving LLM-based Emotion Recognition in Conversation with Speaker Characteristics

## Metadata
- Source file: `raw/sources/Fu 等 - 2025 - LaERC-S Improving LLM-based Emotion Recognition in Conversation with Speaker Characteristics.pdf`
- Year: 2025
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Emotion recognition in conversation needs speaker-aware context, not just sentence-level emotion classification.
- Existing ERC methods can underuse speaker identity and speaker characteristics that shape emotional interpretation.
- The paper studies whether LLM-derived speaker characteristics improve ERC.

## Method
- Proposes LaERC-S, a speaker-characteristic enhanced ERC approach.
- Uses an initial stage to identify/inject speaker characteristics before final emotion analysis.
- Tests different speaker-characteristic elements and selects `oReact` as the final key element.

## Data and Evaluation Setup
- Evaluates on IEMOCAP, MELD, and EmoryNLP.
- Reports dataset-level scores and an average score across the three benchmarks.
- Publication-checked values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- LaERC-S improves performance by incorporating speaker characteristics in a two-stage setup.
- Publication-checked final `wS` / `oReact` values are IEMOCAP 72.40, MELD 69.27, EmoryNLP 42.08, and Avg 61.25.
- The page should be read as ERC evidence inside the broader LLM reasoning/evaluation cluster, not as a general reasoning benchmark.

## Limitations and Follow-ups
- Speaker-characteristic generation can introduce bias or noisy inferred attributes.
- Follow-up checks should separate gains from better context modeling versus gains from dataset-specific speaker cues.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: zero-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph, causal
- Mentioned datasets: MELD, IEMOCAP, TOP, Facebook, Persona
- Mentioned metrics: accuracy, f1


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
