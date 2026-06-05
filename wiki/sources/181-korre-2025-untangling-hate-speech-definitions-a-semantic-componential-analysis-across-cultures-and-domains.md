---
created: 2026-06-01
updated: 2026-06-01
tags: [paper, deep-ingest-v2, hate-speech, benchmark, zero-shot, prompting, bias, explainability]
sources: [raw/sources/2025.findings-naacl.175.pdf]
---

# Korre 等 - 2025 - Untangling Hate Speech Definitions A Semantic Componential Analysis Across Cultures and Domains

## Metadata
- Source file: `raw/sources/2025.findings-naacl.175.pdf`
- Year: 2025
- Venue: Findings of NAACL 2025
- Pages: 15
- Ingest level: deep-ingest-v2 (definition-frame pass; first three pages checked)

## Problem Framing
- Hate-speech definitions vary across cultures and domains, making universal labels underspecified.
- Dataset construction and model evaluation can inherit unexamined assumptions from legal, academic, dictionary, Wikipedia, or platform-policy definitions.

## Method
- Introduces Semantic Componential Analysis (`SCA`) for decomposing hate-speech definitions into interpretable components.
- Creates HateDefCon, a resource of 493 definitions from more than 100 cultures and five domains.
- Studies how definition complexity changes zero-shot LLM hate-speech decisions.

## Data and Evaluation Setup
- Definition sources include legislation, Wikipedia, online dictionaries, research papers, and online platform or technology-company policies.
- The component framework covers target, intention or purpose, and act or means.

## Results and Claims
- Reports substantial variation in definition components and cross-domain borrowing that may ignore cultural context.
- Reports that LLM responses change with the complexity of prompted definitions.
- Exact experimental values require table verification before external citation.

## Limitations and Follow-ups
- Definition-aware prompting can introduce instability if frames are large or uncontrolled.
- Follow-up use: construct two compact modular `definition_frame` conditions before broader policy experiments.

## Related Concepts
- [[p0-target-grounding-reading-synthesis-2026-06-01]]
- [[leakage-resistant-target-relation-modeling]]
- [[llm-evaluation]]
- [[hate-speech-source-hub]]

