---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, role-playing, llm-reasoning, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark]
sources: [raw/sources/Wang 等 - 2025 - OpenCharacter Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas.pdf]
---

# Wang 等 - 2025 - OpenCharacter Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas

## Metadata
- Source file: `raw/sources/Wang 等 - 2025 - OpenCharacter Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas.pdf`
- Year: 2025
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- and response generation, to create character-aligned instructional responses. To
- language virtual assistant and dialogue [8, 9], multi-modal understanding [10, 11], agent systems [12,
- tasks such as online customer support, content creation and entertainment, and non-player character
- 1https://huggingface.co/datasets/xywang1/OpenCharacter

## Method
- OpenCharacter: Training Customizable Role-Playing
- Customizable role-playing in large language models (LLMs), also known as char-
- efficiency in developing and deploying role-playing dialogue agents. This study
- model. Our best-performing model strengthens the original LLaMA-3 8B Instruct
- model and achieves performance comparable to GPT-4o models on role-playing

## Data and Evaluation Setup
- 1https://huggingface.co/datasets/xywang1/OpenCharacter
- 4k characters from Wikipedia and generate a self-simulated role-playing dataset. Different from these
- approach embraces the LLM-synthetic characters and dialogue sessions. We experiment with over
- role-playing dialogue, Li et al. [26] study LLM-based style generalization with evaluation styles
- The evaluation of persona or character-driven role-playing dialogue also draws attention in multiple

## Results and Claims
- model and achieves performance comparable to GPT-4o models on role-playing
- role-playing agents relies on human-annotated or crowd-sourced data. It would struggle to achieve
- characters, which is impractical to achieve if the model is trained with purely human annotated data.
- distinct characters. Based upon Persona Hub, we explore to achieve character generalization through
- generalization can be achieved when the LLMs are trained with well-curated post-training data

## Limitations and Follow-ups
- vised fine-tuning (SFT)) with character-based role-playing dialogue data consisting of manually-
- would bring distributional bias to the character library. We explore enabling LLM’s out-of-domain
- manually labeled or LLM-generated assistant response y.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, benchmark
- Mentioned datasets: ATIS, MASSIVE, TOP, SocialBench, Persona
- Mentioned metrics: none detected

## Abstract (Extracted)
> Customizable role-playing in large language models (LLMs), also known as char- acter generalization, is gaining increasing attention for its versatility and cost- efficiency in developing and deploying role-playing dialogue agents. This study explores a large-scale data synthesis

## Benchmark Evidence Lines
- 1https://huggingface.co/datasets/xywang1/OpenCharacter
- outperforming) the popular GPT-4o [21] models.
- 4k characters from Wikipedia and generate a self-simulated role-playing dataset. Different from these
- role-playing dialogue, Li et al. [26] study LLM-based style generalization with evaluation styles
- The evaluation of persona or character-driven role-playing dialogue also draws attention in multiple
- our evaluation benchmark considering it evaluates the out-of-domain persona-driven role-playing
- dialogue capability with multiple evaluation metrics including “expected action,” “toxicity control,”
- character’s dialogue responses in a well-curated SFT dataset would reflect the character’s language

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
