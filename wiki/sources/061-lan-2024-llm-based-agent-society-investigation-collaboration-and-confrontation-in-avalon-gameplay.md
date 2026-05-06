---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, role-playing, llm-reasoning, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Lan 等 - 2024 - LLM-Based Agent Society Investigation Collaboration and Confrontation in Avalon Gameplay.pdf]
---

# Lan 等 - 2024 - LLM-Based Agent Society Investigation Collaboration and Confrontation in Avalon Gameplay

## Metadata
- Source file: `raw/sources/Lan 等 - 2024 - LLM-Based Agent Society Investigation Collaboration and Confrontation in Avalon Gameplay.pdf`
- Year: 2024
- Pages: 18
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Multi-agent games require LLM agents to reason under hidden roles, incomplete information, collaboration, deception, and adversarial incentives.
- Avalon is used as a testbed for studying collaboration and confrontation in LLM-based agent societies.
- The key question is whether structured analysis, planning, action, and experience modules improve gameplay behavior.

## Method
- Builds Avalon agents with modules for analysis, planning, action, and improvement from experience.
- Uses prompts and game-state tracking to guide role-specific strategy.
- Runs module ablations to measure the importance of learning from experience, analysis, planning, and action.

## Data and Evaluation Setup
- Evaluates gameplay outcomes with winning rate (WR), quest engagement rate (QER), failure voting rate (FVR), and valid response rate (VRR).
- Includes experience-learning and no-experience-learning ablation settings.
- Publication-checked values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- The full framework reports stronger gameplay outcomes than several ablated variants.
- Publication-checked values include WR 80 for the full experience-learning framework, WR 90 for all modules without experience learning, WR 60 when planning is removed, and VRR averages 59.9 for LLaMA2 versus 85.0 for GPT-3.5.
- Use this as evidence about agentic social reasoning in a game environment, not as a general LLM benchmark.

## Limitations and Follow-ups
- Avalon gameplay is a narrow simulated environment; real-world social reasoning has different incentives and safety constraints.
- Prompted modules may depend strongly on base model instruction following and valid response behavior.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, dialogue, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: TOP, Avalon
- Mentioned metrics: none detected


## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
