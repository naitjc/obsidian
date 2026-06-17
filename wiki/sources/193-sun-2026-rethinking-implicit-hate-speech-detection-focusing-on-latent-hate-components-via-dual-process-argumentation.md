---
created: 2026-06-17
updated: 2026-06-17
tags: [paper, deep-ingest-v2, hate-speech, implicit, llm-reasoning, prompting, benchmark, explainability]
sources: [raw/sources/3774904.3792159.pdf]
---

# Sun 等 - 2026 - Rethinking Implicit Hate Speech Detection Focusing on Latent Hate Components via Dual-Process Argumentation

## Metadata
- Source file: `raw/sources/3774904.3792159.pdf`
- Year: 2026
- Venue: WWW 2026
- Pages: 12
- DOI: `10.1145/3774904.3792159`
- Ingest level: deep-ingest-v2 (latent-component and argumentation pass; method, main table, ablation, and limitation sections checked)

## Problem Framing
- The paper argues that LLM detectors often produce pseudo-reasoning: they overreact to spurious sensitive cues or miss latent semantic units that carry implicit hate.
- It names these semantic units Latent Hate Components (`LHCs`) and treats them as the anchors for implicit-hate inference.
- The two failure modes are over-sensitivity to spurious LHCs and omission of actual LHCs.

## Method
- Introduces DuPL, a dual-process argumentation framework.
- Stage 1, Mining of Latent Hate Components, uses a Candidate Miner, Critical Challenger, and Confusion Judge to extract candidate LHCs, filter noisy candidates, and early-exit on clear cases.
- Stage 2, Deliberation of Latent Hate Components, performs component-wise argumentation with Proponent and Opponent agents, then uses an Integrative Decision agent to synthesize a final verdict.
- The design separates fast high-recall mining from slower structured deliberation, resembling a controlled agentic verifier rather than unconstrained chain-of-thought.

## Data and Evaluation Setup
- Evaluates on IHC, SBIC, and ToxiGen.
- Tests multiple LLM backbones including GPT-4o-mini, Qwen2.5-7B-Instruct, and DeepSeek-V3.
- Reports accuracy, macro-F1, false positive rate, and false negative rate to measure both over-sensitivity and missed implicit hate.

## Results and Claims
- Reports consistent improvements over direct judging, CoT, self-reflection, multi-agent debate, and PREDICT across the three datasets.
- Ablations show that removing LHC mining, the Critical Challenger, component-wise argumentation, or integrative decision reduces performance, supporting the claim that the system depends on the structured component pipeline rather than debate alone.
- Exact table values and effect sizes should be visually verified from the PDF before external citation.

## Local Transfer to IHC/SBIC Work
- This is the closest paper to a defensible ReAct-style design for the current IHC/SBIC target-relation project.
- The transferable unit is not free-form reasoning; it is the explicit intermediate object: `latent_hate_component`.
- For the local project, map LHCs into structured fields such as `candidate_target`, `evidence_span`, `relation_state`, and `context_modifier`, then trigger deliberation only for uncertain or shortcut-prone examples.
- The paper is also a warning: generic multi-agent debate can be weaker than component-grounded argumentation.

## Limitations and Follow-ups
- LHCs are heuristic intermediate constructs, not causal proof of speaker intent.
- Cultural definitions and thresholds may not transfer across communities or datasets.
- The framework still depends on underlying LLM quality and uses substantial API/token cost relative to direct judging.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[explainable-hate-speech-detection]]
- [[target-relation-grounding-literature-map]]
- [[llm-reasoning]]
- [[hate-speech-source-hub]]
