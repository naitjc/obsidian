---
created: 2026-07-01
updated: 2026-07-11
tags: [paper, deep-ingest-v2, llm-reasoning, retrieval, prompting, synthetic-data, benchmark]
sources: [raw/sources/20812_Process_vs_Outcome_Rewar.pdf]
---

# Zhang 等 - 2025 - Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning?

## Metadata
- Source file: `raw/sources/20812_Process_vs_Outcome_Rewar.pdf`
- Year: 2025
- Venue: NeurIPS 2025
- Pages: 29
- Code: `https://github.com/Applied-Machine-Learning-Lab/ReasonRAG`
- Ingest level: deep-ingest-v2 (method, process-data construction, inference loop, main tables, ablations, limitations, and societal-impact section checked)

## Problem Framing
- The paper studies whether an agentic RAG policy should receive only a final-answer outcome reward or finer supervision for intermediate retrieval and reasoning decisions.
- It argues that outcome-only supervision is sparse, delays feedback until a full trajectory is complete, and can penalize correct early actions when a later action fails.
- Local synthesis: process supervision is best read here as a data-quality and credit-assignment intervention, not merely as a longer reasoning prompt.

## Method
- ReasonRAG defines three agent actions: query generation, evidence extraction, and answer generation. Inference alternates between Reasoning, Grounding, and Terminal states under a maximum-step bound.
- Shortest Path Reward Estimation (SPRE) scores a partial trajectory through repeated continuations, final-answer correctness, and a decay penalty for unnecessary steps.
- A tailored Monte Carlo Tree Search explores alternative actions, propagates SPRE estimates, and yields preferred versus dispreferred next-action pairs from the same partial state.
- RAG-ProGuide contains 4,603 questions and 13,289 process-level preference pairs after pruning duplicate or weak-gap comparisons. These values were visually checked in Table 1 and the adjoining construction text.
- The policy is optimized with DPO over next-step preference pairs rather than with an online policy-gradient objective.

## Data and Evaluation Setup
- Training questions come from PopQA, HotpotQA, and 2WikiMultiHopQA; evaluation additionally uses Bamboogle and MuSiQue as out-of-domain multi-hop sets.
- Section 3.1 states that ReasonRAG and all baselines use Qwen2.5-7B-Instruct, but Appendix E.2 and Table 5 list separate public checkpoints for Self-RAG and AutoRAG. Treat backbone uniformity as an internal reporting inconsistency rather than a fully verified control. ReasonRAG itself uses a 2018 Wikipedia dump augmented with dataset evidence and a BGE retriever.
- Evaluation reports Exact Match and F1. The paper compares zero-shot, active, adaptive, RAG-CoT, summary, and reasoning-oriented baselines.

## Results and Claims
- Table 2 reports that ReasonRAG trained on roughly 5k questions exceeds Search-R1 trained on 90k questions on the five-dataset average; the reported average is 34.4 EM / 42.3 F1 versus 32.8 EM / 40.7 F1. These values were visually checked on the original page.
- The controlled optimization comparison in Table 3 favors process-level preference learning over the base model, SFT, and outcome-reward variants, including an outcome-reward variant trained on twice as many questions. The table was visually checked.
- The retrieval-step analysis reports task-dependent saturation: single-hop questions peak with fewer rounds than multi-hop questions.
- These results establish evidence for the paper's own open-domain QA setup; they do not prove that process supervision is universally better across agent tasks or reward constructions.

## Local Transfer
- The strongest reusable distinction is between final task acceptance and intermediate decision quality. A workflow can keep the final metric as the acceptance criterion while separately learning or auditing planning, evidence selection, and stopping behavior.
- For the local autonomous IHC workflow-search line, the paper suggests logging and judging intermediate actions separately, but it does not justify importing QA-specific SPRE rewards or MCTS directly into classification experiments.
- The same-state preference-pair design is a cleaner transfer target than unrestricted trajectory imitation because it isolates which next action was useful under a fixed prior context.
- Local inference: the task-dependent retrieval saturation supports testing a bounded adaptive-depth policy rather than imposing one fixed retrieval count.
- Local caution: shortest-path rewards inherit answer-key and retrieval-corpus assumptions; a shortest correct path is not automatically the most faithful path when the answer metric is incomplete.

## Limitations and Follow-ups
- Process-level annotation requires additional trajectory exploration and therefore costs more during data rollout, even if later policy training is more data efficient.
- The experiments use open-domain QA, one backbone family, and a specific retrieval setup. Transfer to hate-speech classification, subjective labels, or non-retrieval agents remains unverified.
- The paper notes that retrieved racist or harmful material may steer generation and recommends controlled corpora and safety evaluation.

## Related Concepts
- [[llm-reasoning]]
- [[retrieval-augmented-generation]]
- [[llm-reasoning-source-hub]]
