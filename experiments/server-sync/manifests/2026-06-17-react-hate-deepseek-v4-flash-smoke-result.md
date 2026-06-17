# ReAct Hate DeepSeek V4 Flash Smoke Result

Generated: 2026-06-17

## Remote Project

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

## Effective API Configuration

- base URL: `https://api.deepseek.com`
- model: `deepseek-v4-flash`
- thinking: `disabled`
- temperature: `0.0`
- split: `validation`
- sample size: `50`
- retrieval top-k: `4`
- data variant: `uncompleted`
- max searches: `2`
- search pools: `train,validation`

## Latest Valid Smoke Run

Remote path:

`runs/api/validation/api_validation_uncompleted_adaptive_50_strict`

Metrics:

- total: `50`
- valid predictions: `50`
- missing predictions: `0`
- parse errors: `0`
- accuracy: `0.66`
- Macro-F1: `0.6486151302190988`
- toxic precision: `0.6176470588235294`
- toxic recall: `0.84`
- toxic F1: `0.711864406779661`
- non-toxic precision: `0.75`
- non-toxic recall: `0.48`
- non-toxic F1: `0.5853658536585366`
- confusion: `tp=21`, `tn=12`, `fp=13`, `fn=4`

Distribution:

- gold: `25` non-toxic, `25` toxic
- predicted: `16` non-toxic, `34` toxic
- search calls: `43/50` examples used one local Search call; `7/50` stopped
  without Search
- validation self-leak check: no retrieved observation had the same id as the
  current validation example

## Interpretation

The latest strict adaptive API smoke test is operationally valid: DeepSeek V4
Flash with thinking disabled returns parseable ReAct outputs for all 50
validation examples after the strict `Finish[...]` parser fix.

The main quality signal is still a toxic-leaning decision boundary. False
positives dominate the observed errors (`13` fp versus `4` fn), and the latest
strict adaptive loop is below the earlier fixed-retrieval smoke run
`api_validation_smoke_50_v3` on Macro-F1 (`0.648615` versus `0.702886`).

## Runs Folder Organization

Current remote layout:

- `runs/api/validation/`: valid API validation runs
- `runs/archive/dryrun/`: no-key dry-run and parser checks
- `runs/archive/failed/`: preflight and path failures
- `runs/archive/invalid/`: invalid runs excluded from comparison
- `runs/archive/obsolete_format/`: old API run before thinking was disabled
- `runs/archive/aborted/`: interrupted old API smoke run
- `runs/archive/generated_cache/`: generated Python cache files moved out of
  source directories

## Next Step

The full IHC test run can proceed, but the result should be interpreted with
attention to false positives and class-bias diagnostics.
