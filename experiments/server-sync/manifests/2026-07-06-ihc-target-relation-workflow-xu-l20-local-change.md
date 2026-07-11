# IHC Target-Conditioned Label-Contrast Workflow Manifest

- Snapshot status: superseded and diverged after 2026-07-07.
- This file records the 2026-07-06 label-only / `key_difference` contract. It is
  not a manifest of the current huashan remote workspace.
- Follow-up remote changes are recorded in
  `2026-07-07-huashan-ihc-target-relation-v9like-change.md` and
  `2026-07-07-huashan-v9-current-validation-runner.md`.
- The current v9-like portable code and runner have not been pulled back into
  local staging, so local reproducibility of that remote state is unverified.

- Local staging: `experiments/server-sync/staging/ihc-target-relation-workflow-xu-l20`
- Remote target: `xu-l20:/data/chenjt/hate/Try/ihc-target-relation-workflow`
- API model: `deepseek-v4-flash`, thinking disabled, temperature 0, JSON required
- Small model default: `/data/public_model/Qwen3-4B`
- Evaluation input boundary: current query exposes text only
- Evidence grouping: gold training label only (`toxic` / `not_toxic`); no attacked/mentioned status

## Aligned retrieval corpora

All three corpora contain the same 14,930 IDs and exact text order, with text-order SHA-256
`4d19e6f9581329156a4530df47efd9cf2cb92e45794bd8fa5f9af69472b37636`.

| Condition | not-toxic target | not-toxic statement | File SHA-256 |
|---|---|---|---|
| `original` | absent | absent | `d287998656347402b549b52717b2b4acf9ceca26adbf62f2d7a38457c8b2e7cd` |
| `target_only` | completed | absent | `beda459611cffa7b69afedf3956f4b0171bc2823c233e9e8c94ae2c4486c9651` |
| `target_statement` | completed | completed | `b9fdbaafc9c145ed0540970d723c9d7a00037f95895f829b0ca146807c7a9d57` |

All conditions reuse the same BGE-small-en-v1.5 training text embeddings.

## Validation subset

- Source: native FineTune IHC validation split, 1,865 rows
- Source distribution: 545 toxic / 1,320 not-toxic
- Selection: deterministic proportional stratified sample, seed `20260706`
- Sample distribution: 58 toxic / 142 not-toxic
- Validation text SHA-256: `b759c6ceb6c0a76f16e5b901afdb5b335c55585d1145f75219785b3140a7ced6`
- Validation label SHA-256: `06d34cd86a6402f6550eee0293d66053ac52f4f72b941c84716767f7dab9eef7`
- BGE text query array SHA-256: `470f5bd0c91e646d0c339f7586e20d079eb5c879b163ae78883376ad867bab31`
- Source indices and selection provenance: `private/validation_manifest.json`

## Implemented architectures

- `big-big`: API summarizer + API classifier
- `big-small`: API summarizer + Qwen3-4B classifier LoRA
- `small-small`: Qwen3-4B summarizer LoRA + separate Qwen3-4B classifier LoRA

Shared retrieval and prompts live in `src/core.py`. API calls are sample-isolated,
JSON-required, retry-bounded, checkpointed, and traced without credentials. Training-query
summary construction excludes the query's own row.

## Launchers and cleanup

- `scripts/run_big_big.sh {original|target_only|target_statement}` runs one validation condition.
- `scripts/run_big_big_all.sh` runs the three big+big validation conditions in order and is suitable for `nohup`.
- Runtime evaluation accepts only the `validation` split; test labels are not included in this workspace.
- Empty runtime directories are kept intentionally: `runs/`, `checkpoints/`, `logs/`, `models/`, and `training/`.
- Cleanup should remove only caches and confirmed-disposable interrupted artifacts. Fixed corpora, validation subset, BGE embeddings, checkpoints for resumable runs, metrics, predictions, and traces are retained.

## Local/remote boundary at capture time

On 2026-07-06, local staging and the xu-l20 remote workspace contained matching code,
configs, aligned corpora, validation subset, and fixed embeddings. The later huashan
workspace diverged through the v9-like target-relation changes and a remote-only current-
validation runner. Do not use this snapshot to claim the present local and huashan trees
match. Model weights, LoRA adapters, API credentials, bulk predictions, traces,
checkpoints, and test-1869 labels remain excluded. Test-1869 remains frozen.
