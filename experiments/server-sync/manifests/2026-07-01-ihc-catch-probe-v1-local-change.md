# IHC CATCH-Style C/T Probe 1.0 Local Change Manifest

Generated: 2026-07-01

## Task

Implement the first executable feasibility version of an LLM-instantiated C/T
factor probe for implicit-only IHC, while preserving completed not-toxic targets
as independent target/referent supervision.

## Local Bundle

`experiments/server-sync/staging/ihc-catch-probe-v1/`

Included:

- `README.md`
- `MANIFEST.md`
- `configs/probe.json`
- `prompts/system.txt`
- `prompts/user.txt`
- `code/build_sample.py`
- `code/run_probe.py`
- `code/evaluate_probe.py`
- `code/build_audit_sample.py`

## Intended Remote Target

`xu-l20:/data/chenjt/hate/Try/ihc-catch-probe-v1`

## Data Dependency

`/data/chenjt/hate/DATA/llm_restructed/IHC_target_v1/train.json`

The builder reads the source dataset and writes private derived inputs and hidden
gold into the task bundle. It never edits the source file.

Pair construction uses exact normalized target overlap and caps each normalized
target at five pairs so that one frequent identity cannot dominate the diagnostic.

## Experiment Boundary

- The LLM runner sees only `id` and `text`.
- `C_probe` and `T_probe` are predicted separately.
- A not-toxic row may have a non-empty completed target/referent.
- `T_probe=[]` is expected only for genuine no-target rows.
- Completed not-toxic targets are reported as weak-label agreement, separated by
  `lexicon_match` and `llm_unmatched_extraction` provenance.

## Excluded

- credentials and endpoint secrets;
- dataset copies and sample-level derived files;
- API calls and remote execution;
- model outputs, raw responses, audit sheets, logs, checkpoints, and caches.

The API runner uses `httpx` directly, matching the existing fixed DeepSeek
runtime. It does not require the `openai` Python SDK. The default model identifier
is `deepseek-v4-flash`, with environment overrides retained.

## Completed Baseline 0 Result

The local run `runs/ct_v1_20260701_210258/` completed all 200 rows with
`FormatValidity=1.0`. Aggregate results were `C_probe` Macro-F1 `0.6726`,
`Pair_C_correct=14/50`, `Pair_CT_joint=1/50`, `IdentityGap=0.24`, and
target-present non-hate FPR `0.36`. The completed-target metric is weak-label
agreement, not unquestioned target accuracy. The run is retained as historical
Baseline 0 because `C_probe` is operationally the final binary verdict; it is
not the active M/T/S factor-pool design. Sample-level artifacts remain private.
