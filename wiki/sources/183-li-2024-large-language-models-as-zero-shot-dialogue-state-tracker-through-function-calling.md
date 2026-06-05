---
created: 2026-06-04
updated: 2026-06-04
tags: [paper, deep-ingest-v2, dialogue, llm-reasoning, zero-shot, prompting, benchmark]
sources: [raw/sources/2402.10466v4.pdf]
---

# Li 等 - 2024 - Large Language Models as Zero-shot Dialogue State Tracker through Function Calling

## Metadata
- Source file: `raw/sources/2402.10466v4.pdf`
- Year: 2024
- Venue: arXiv v4
- Pages: 17
- Ingest level: deep-ingest-v2 (dialogue-state-tracking pass; first two pages plus conclusion checked)

## Problem Framing
- Task-oriented dialogue systems need dialogue state tracking (`DST`) rather than only fluent response generation.
- Existing LLM dialogue ability does not automatically yield strong zero-shot DST across unseen task domains.
- The paper frames function calling as a way to make DST outputs explicit and schema-constrained without collecting domain-specific training data for each new domain.

## Method
- Introduces `FnCTOD`, a function-calling approach for zero-shot DST with LLMs.
- Represents slot-value extraction as callable functions, giving the model structured output targets instead of free-form state descriptions.
- Studies both in-context prompting for existing LLMs and light fine-tuning to equip an open-source LLaMA2-Chat model with function-calling DST behavior.

## Data and Evaluation Setup
- Evaluates on MultiWOZ 2.1 using the 1,000-dialogue test split.
- Uses joint goal accuracy (`JGA`) as the main DST metric, with slot-level measures also reported in the paper tables.
- Reports fine-tuning of LLaMA2-13B-Chat on 7,200 training samples from 36 diverse domains for function-calling capability.

## Results and Claims
- Reports that function-calling prompting improves zero-shot DST for both proprietary and 7B/13B open-source LLMs.
- Claims a new zero-shot DST benchmark level on MultiWOZ for GPT-4 and competitive performance from a fine-tuned LLaMA2-13B-Chat variant.
- Exact JGA and slot-F1 values require table verification before external citation.

## Limitations and Follow-ups
- The authors note that zero-shot DST accuracy may still be below practical deployment needs.
- Response-generation evaluation remains limited by delexicalized metrics; natural-language response evaluation is a separate open issue.
- Local transfer: useful as a structured-output analogy for slot-like target/relation fields, but it is a dialogue DST paper rather than hate-speech evidence.

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[intent-slot-style-hate-speech-modeling]]
- [[dialogue-systems-source-hub]]
