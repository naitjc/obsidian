---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, dialogue, benchmark, graph]
sources: [raw/sources/0523.pdf]
---

# Ding 等 - 2021 - Focus on Interaction A Novel Dynamic Graph Model for Joint Multiple Intent Detection and Slot Filling

## Metadata
- Source file: `raw/sources/0523.pdf`
- Year: 2021
- Venue: IJCAI 2021
- Pages: 7
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets spoken language understanding where an utterance can contain multiple intents and slot spans.
- Prior joint multi-intent models either inject the same multi-intent vector into every token or build token-level intent-slot graphs, which can introduce intent noise and high computational cost.
- The paper frames the central problem as selecting the intent information relevant to tokens that actually matter for intent-slot interaction.

## Method
- Proposes a Dynamic Graph Model (DGM) for joint multiple intent detection and slot filling.
- Builds a sentence-level intent-slot interactive graph that connects important token nodes with relevant intent nodes instead of broadcasting all intent information to all tokens.
- Uses a generation graph layer to dynamically update the graph and a graph attention network to encode the interaction.
- Optimizes intent detection and slot filling jointly with task-specific decoders.

## Data and Evaluation Setup
- Multi-intent datasets: MixATIS and MixSNIPS.
- Single-intent datasets for generalization: ATIS and SNIPS.
- Metrics include slot F1, intent F1 or accuracy, and overall semantic-frame accuracy.
- The paper also compares runtime against AGIF-style token-level graph interaction.

## Results and Claims
- Reports state-of-the-art or improved performance on MixATIS and MixSNIPS, especially in overall semantic-frame accuracy.
- Claims a three-to-six times speed improvement over the prior graph-interactive model because the graph is sentence-level rather than token-level.
- Results on ATIS and SNIPS are used to argue the method is not limited to multi-intent utterances.
- Exact benchmark numbers are table-dependent and should be checked in Tables 1-3 before external citation.

## Limitations and Follow-ups
- The approach still depends on supervised SLU datasets with intent and slot labels.
- The dynamic graph construction is evaluated on standard SLU benchmarks; robustness under policy-like or open-domain slot definitions remains unverified.
- Follow-up link: compare its graph construction with AGIF and Co-guiding Net in the dialogue direction, and with policy-aware hate detection where slots are explanation-bearing rather than task-action arguments.

## Structured Signals
- Detected method keywords: dynamic graph, graph attention network, intent-slot interaction, multi-intent SLU
- Mentioned datasets: MixATIS, MixSNIPS, ATIS, SNIPS
- Mentioned metrics: slot F1, intent F1, intent accuracy, overall accuracy, runtime

## Related Concepts
- [[dialogue-systems]]
- [[multi-agent-systems]]
- [[intent-slot-style-hate-speech-modeling]]
- [[dialogue-systems-source-hub]]
