---
created: 2026-06-04
updated: 2026-06-04
tags: [paper, deep-ingest-v2, llm-reasoning, bias, synthetic-data, benchmark, safety-alignment]
sources: [raw/sources/2606.04807v1.pdf]
---

# Reddy 等 - 2026 - BiasGRPO Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization

## Metadata
- Source file: `raw/sources/2606.04807v1.pdf`
- Year: 2026
- Venue: arXiv v1
- Pages: 18
- Ingest level: deep-ingest-v2 (bias-mitigation pass; first two pages plus results and conclusion checked)

## Problem Framing
- Social-bias mitigation is a high-variance alignment problem because rewards are subjective and lack a single ground truth.
- DPO is limited by offline fixed preference data, while PPO can become unstable because it depends on critic estimates.
- The paper asks whether GRPO is a better fit for bias mitigation by using group-relative reward normalization.

## Method
- Introduces BiasGRPO, a modular framework combining a synthetically extended dataset, a custom bias reward model, and GRPO.
- Uses group-relative baselines instead of a learned value function to stabilize updates.
- Releases a small bias reward model intended as a plug-in component for multi-objective RLHF pipelines.

## Data and Evaluation Setup
- Trains Phi-2 with PPO, DPO, and GRPO variants.
- Evaluates bias across BOLD, RealToxicityPrompts, and BBQ, with TruthfulQA used to monitor capability or factual-knowledge degradation.
- Uses synthetically extended data spanning multiple domains and contexts.

## Results and Claims
- Reports that BiasGRPO outperforms DPO and PPO across multiple bias benchmarks while maintaining TruthfulQA performance.
- Argues that group-relative optimization is well matched to noisy subjective reward landscapes.
- Exact benchmark values and statistical tests require table verification before external citation.

## Limitations and Follow-ups
- Experiments are on 3B-parameter models; generalization to larger models remains unverified.
- Group-size choices may need adaptive or task-specific tuning.
- Local transfer: relevant to bias-aware moderation and reward-model design, but should not be treated as a hate-speech classifier result.

## Related Concepts
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[llm-reasoning-source-hub]]
