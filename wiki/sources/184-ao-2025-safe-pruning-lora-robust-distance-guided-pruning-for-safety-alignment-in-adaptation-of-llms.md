---
created: 2026-06-04
updated: 2026-06-04
tags: [paper, deep-ingest-v2, llm-reasoning, safety-alignment, benchmark]
sources: [raw/sources/2025.tacl-1.67.pdf]
---

# Ao 等 - 2025 - Safe Pruning LoRA Robust Distance-Guided Pruning for Safety Alignment in Adaptation of LLMs

## Metadata
- Source file: `raw/sources/2025.tacl-1.67.pdf`
- Year: 2025
- Venue: TACL 2025
- Pages: 14
- Ingest level: deep-ingest-v2 (safety-alignment pass; first page plus experiments and conclusion checked)

## Problem Framing
- LoRA adaptation can weaken safety alignment even when fine-tuning data is benign.
- Existing safety methods may not isolate which LoRA layers are responsible for unsafe parameter shifts.
- The paper asks for a pruning method that improves safety while preserving utility and reliability.

## Method
- Introduces Safe Pruning LoRA (`SPLoRA`), which selectively removes LoRA layers that weaken safety alignment.
- Uses Empirical-DIEM (`E-DIEM`), a dimension-insensitive distance/similarity measure, to identify unreliable LoRA layers.
- Compares against safety-alignment baselines including SafeInstr, Backdoor Enhanced Alignment, SafeLoRA, and Vaccine.

## Data and Evaluation Setup
- Fine-tunes with Dialog Summary, Alpaca, and PureBad settings, including mixed benign/malicious and purely benign adaptation.
- Measures utility with ROUGE-1 F1 and METEOR.
- Measures safety with Attack Success Rate (`ASR`) and harmfulness score (`HS`), including GPT-4-based harmfulness evaluation.

## Results and Claims
- Reports that SPLoRA reduces safety risks while maintaining or improving utility and reliability.
- Claims that E-DIEM enables precise layer selection for pruning safety-damaging LoRA components.
- Exact safety and utility table values require verification before external citation.

## Limitations and Follow-ups
- The note supports LoRA safety-maintenance decisions, not hate-speech target grounding directly.
- Local transfer: relevant if IHC/SBIC adapters need safety or reliability checks after domain fine-tuning.

## Related Concepts
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[llm-reasoning-source-hub]]
