---
created: 2026-06-17
updated: 2026-06-17
tags: [paper, deep-ingest-v2, hate-speech, implicit, llm-reasoning, prompting, retrieval, benchmark, bias, explainability]
sources: [raw/sources/2601.09342v2.pdf]
---

# Gajewska 等 - 2026 - Improving Implicit Hate Speech Detection via a Community-Driven Multi-Agent Framework

## Metadata
- Source file: `raw/sources/2601.09342v2.pdf`
- Year: 2026
- Venue: ICAART 2026 / arXiv v2
- Pages: 8
- Ingest level: deep-ingest-v2 (agentic implicit-hate pass; method and results sections checked)

## Problem Framing
- Implicit hate speech is difficult because meaning depends on social identity, historical context, coded references, and target-group perspectives.
- The paper argues that standard prompting and fine-tuned classifiers often show high true negative rates but miss hateful content, leaving targeted communities under-protected.
- The central fairness concern is the balance between detecting hate and avoiding over-moderation of benign speech.

## Method
- Proposes a community-driven multi-agent moderation framework.
- A central Moderator Agent first classifies the post and decides whether additional consultation is needed.
- If the case is uncertain, the system extracts a target group, retrieves Wikipedia-backed background for that group, constructs a Community Agent persona, and fuses the Moderator and Community Agent decisions.
- The implementation uses Gemini 2.5 Flash and an AutoGen-style multi-agent workflow.

## Data and Evaluation Setup
- Evaluates on manually annotated ToxiGen examples for six target groups: Black people, Asians, Jewish people, Muslims, women, and LGBTQ people.
- Compares the agentic approach with zero-shot, few-shot, and chain-of-thought prompting under the same underlying LLM architecture.
- Uses true positive rate, true negative rate, balanced accuracy, and F1 to track both detection effectiveness and moderation fairness.

## Results and Claims
- Reports that community consultation improves positive-class detection and balanced accuracy across target groups compared with prompt-only baselines.
- The ablation without Community Agents performs much worse on several groups, especially LGBTQ and women, supporting the claim that consultation adds value beyond the central Moderator Agent.
- Exact table values should be treated as pending manual table verification before publication-grade citation.

## Local Transfer to IHC/SBIC Work
- Useful as a contrast to the local candidate-target relation path: it injects target-group context through external community personas, while the local project can keep target relations as compact, auditable structured fields.
- The most transferable mechanism is gated consultation: trigger expensive reasoning only when the base classifier is uncertain or the example is target-sensitive.
- For the current ReAct-style idea, this paper supports a bounded verifier design rather than always-on agentic inference for every row.

## Limitations and Follow-ups
- Wikipedia-derived community context is public and reproducible but may be incomplete, dominant-culture-biased, or too broad for specific in-group interpretation.
- The paper evaluates ToxiGen target groups, so direct transfer to IHC/SBIC should be tested rather than assumed.
- The framework uses broad demographic agents; it does not directly solve candidate target extraction or attacked-versus-mentioned relation classification.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[explainable-hate-speech-detection]]
- [[target-relation-grounding-literature-map]]
- [[llm-reasoning]]
- [[hate-speech-source-hub]]
