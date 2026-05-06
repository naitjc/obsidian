---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, sarcasm, dialogue, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Tomar 等 - 2024 - Action and Reaction Go Hand in Hand! a Multi-modal Dialogue Act Aided Sarcasm Identification.pdf]
---

# Tomar 等 - 2024 - Action and Reaction Go Hand in Hand! a Multi-modal Dialogue Act Aided Sarcasm Identification

## Metadata
- Source file: `raw/sources/Tomar 等 - 2024 - Action and Reaction Go Hand in Hand! a Multi-modal Dialogue Act Aided Sarcasm Identification.pdf`
- Year: 2024
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- better. Toward this aim, we extend the multi-modal MUStARD dataset to enclose dialogue acts for each dialogue.
- sarcasm identification (MM-SARDAC), leveraging interrelation between these tasks. In addition, we introduce an
- sarcasm identification alone. The dataset and code are available at https://github.com/mohit2b/MM-SARDAC.
- Keywords: Sarcasm Identification, Dialogue Act Classification (DAC), Multi-modality, Multi-tasking

## Method
- order-infused, multi-modal infusion mechanism into our proposed model, which allows for a more intuitive combined
- cause I got an ugly, itchy sweater, and my brother following paragraphs, we have summarized the
- developed a benchmark multi-modal sarcasm iden-
- (2020) developed a multi-task framework for detect-
- cross-modal graph-based model for identifying sar-

## Data and Evaluation Setup
- better. Toward this aim, we extend the multi-modal MUStARD dataset to enclose dialogue acts for each dialogue.
- sarcasm identification alone. The dataset and code are available at https://github.com/mohit2b/MM-SARDAC.
- developed a benchmark multi-modal sarcasm iden-
- tification dataset called MUStARD. Chauhan et al.
- (2022) developed HOPE dataset that is used for

## Results and Claims
- results indicate that dialogue act-aided sarcasm identification achieved better performance compared to performing
- ceptable agreement. It is achieved in the first round
- sentation Cˆ t−m1−m2 is sent to the above layers for We use accuracy, weighted F1-score, precision,
- further processing. and recall measures to evaluate the performance of
- cess (explained above) of modality encoding and several baselines and state-of-the-art (SOTA) mod-

## Limitations and Follow-ups
- dataset has been manually annotated with DAs to
- dataset, annotators can be biased towards certain deep bidirectional transformers for language un-
- dialogue acts; thus, any biases in our dataset are derstanding. arXiv preprint arXiv:1810.04805.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: MUStARD, ATIS, Persona
- Mentioned metrics: accuracy, acc, f1, precision, recall, f1-score

## Abstract (Extracted)
> Sarcasm primarily involves saying something but "meaning the opposite" or "meaning something completely different" in order to convey a particular tone or mood. In both the above cases, the "meaning" is reflected by the communicative intention of the speaker, known as dialogue ac

## Benchmark Evidence Lines
- better. Toward this aim, we extend the multi-modal MUStARD dataset to enclose dialogue acts for each dialogue.
- sarcasm identification alone. The dataset and code are available at https://github.com/mohit2b/MM-SARDAC.
- developed a benchmark multi-modal sarcasm iden-
- tification dataset called MUStARD. Chauhan et al.
- (2022) developed HOPE dataset that is used for
- MUStARD dataset (Castro et al., 2019) for sarcasm
- dataset to curate Multi-modal Sarcasm-Dialogue combine text, audio, and visual modality and learn-
- Act Dataset, (M U StARD ), having human anno- ing useful representation to help in downstream

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
