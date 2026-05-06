---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, sarcasm, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod.pdf]
---

# Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod

## Metadata
- Source file: `raw/sources/Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod.pdf`
- Year: 2024
- Pages: 25
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- timodal sarcasm detection. We then propose making it a significant area of study in both NLP
- The MSTI task is to extract the entities being
- Sarcasm, a prevalent form of figurative language, an end-to-end task, primarily focusing on the super-
- eral meaning (Joshi et al., 2017). As an important and understanding of the underlying meanings are

## Method
- a versatile MSTI framework with a coarse-to- words in red denote the visual and textual targets.
- ability with reasoning and pre-training knowl-
- modal reasoning, we first engage LMMs to gen-
- pre-training of a small language model on mul- to the forefront of research (Wang et al., 2022),
- fine-tuning the model for finer-grained sarcasm applications and multimedia computing.

## Data and Evaluation Setup
- ently in LMMs. Experimental results demon- ous work (Devlin et al., 2019; Bochkovskiy et al.,
- the implicit meanings intrinsic in sarcasm, we re- iments conducted on two public sarcasm datasets
- et al., 2023a; Bai et al., 2023). This design philos- petitive results compared with MSD baselines. The
- ophy enables complex reasoning, thereby enhanc- experimental analysis further underscores the en-
- ing both the MSTI accuracy and explainability; 2) hanced ability to provide superior explainability in

## Results and Claims
- timodal sarcasm detection. We then propose making it a significant area of study in both NLP
- strate that our model far outperforms state-of- 2020) attempted to straightforwardly integrate a
- and image, respectively. The state-of-the-art ap-
- sort to the extensive prior knowledge embedded reveal that our approach far outperforms previous
- within Large Multimodal Models (LMMs) (Liu state-of-the-art MSTI methods, and achieves com-

## Limitations and Follow-ups
- et al., 2013), and online harassment detection (Yin casm poses a considerable challenge, because its
- as a marketing tactic. We contend the challenge reasoning knowledge, acquired in the pre-training
- they still suffer from preconception bias and other one for the ground truth. The contextual sub-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy, acc, f1, precision, recall

## Benchmark Evidence Lines
- strate that our model far outperforms state-of- 2020) attempted to straightforwardly integrate a
- and image, respectively. The state-of-the-art ap-
- Moreover, as the example shows in Figure 1(b), the tive impact of inevitable noise from LMMs through
- the implicit meanings intrinsic in sarcasm, we re- iments conducted on two public sarcasm datasets
- sort to the extensive prior knowledge embedded reveal that our approach far outperforms previous
- within Large Multimodal Models (LMMs) (Liu state-of-the-art MSTI methods, and achieves com-
- ing both the MSTI accuracy and explainability; 2) hanced ability to provide superior explainability in
- prehensive MSD dataset, incorporating text, image, LLMs, with publicly shared model weights (Black

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
