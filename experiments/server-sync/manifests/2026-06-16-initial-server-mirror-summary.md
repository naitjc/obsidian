# Initial Server Mirror Summary

Generated: 2026-06-16

## Local Mirror Roots

| Server | Local path | Files | Size | Remote paths |
|---|---:|---:|---:|---|
| `nlp06` | `experiments/server-sync/remotes/nlp06/` | 997 | 340M | `/data/cjt/hate/Try/RA-HMD_text`, `/data/cjt/hate/AnyCode-xu-l20/DATA`, `/data/cjt/hate/AnyCode-xu-l20/FineTune`, `/data/cjt/nlpcourse` |
| `xu-l20` | `experiments/server-sync/remotes/xu-l20/` | 965 | 1.2G | `/data/chenjt/hate/DATA`, `/data/chenjt/hate/FineTune` |
| `huashan` | `experiments/server-sync/remotes/huashan/` | 522 | 108M | `/data/chenjt/Hate/FineTune_only`, `/data/chenjt/Hate/Try`, `/data/chenjt/Study/base_multi_study`, `/data/chenjt/Study/practise` |

## Included

- Experiment source code, scripts, configs, README/status files, prompt/data preparation code, evaluation code, and shell launchers.
- Dataset files and deterministic processed inputs in `.json`, `.jsonl`, `.csv`, `.tsv`, `.txt`, `.gz`, `.pdf`, `.doc`, and `.docx` formats when they were part of the requested server paths.
- Compact run evidence such as metrics, prediction JSONL/CSV files, error summaries, logs, and status files.
- Backup source/config files when they document meaningful experiment branches.

## Excluded

- Model and adapter weights: `*.safetensors`, `adapter_model.*`, `*.pt`, `*.pth`, `*.ckpt`, and large `*.bin` artifacts.
- Repeated tokenizer payloads such as `tokenizer.json`.
- Python caches, notebook checkpoints, `.cache`, `.git`, `wandb`, checkpoint folders, `.DS_Store`, and process state files such as `*.pid` and `pid.txt`.
- RA-HMD_text derived Stage2 embedding tensors under `Stage2/data/Embedding`.
- RA-HMD_text `LLAMA-FACTORY/checkpoints`, because this is model-output state rather than portable code or dataset input.

## Permission Handling

`nlp06` initially had unreadable RA-HMD_text backup files, run logs/status files, and one `AnyCode-xu-l20/DATA/hate_data.tar.gz`. After explicit permission approval, `chmod -R u+rwX` was run on the requested `nlp06` paths. The final `unreadable-after` check was empty, and the second `nlp06` sync completed with an empty stderr log.

Some `chmod` calls under `AnyCode-xu-l20` reported `Operation not permitted` because those files are not owned by `cjt`; they remained readable and were copied when relevant.

## Detailed Manifests

- `2026-06-16-nlp06-inventory.txt`
- `2026-06-16-nlp06-permissions.log`
- `2026-06-16-nlp06-resync.stderr.log`
- `2026-06-16-nlp06-local-summary.txt`
- `2026-06-16-nlp06-local-files.txt`
- `2026-06-16-xu-l20-inventory.txt`
- `2026-06-16-xu-l20-local-summary.txt`
- `2026-06-16-xu-l20-local-files.txt`
- `2026-06-16-huashan-inventory.txt`
- `2026-06-16-huashan-local-summary.txt`
- `2026-06-16-huashan-local-files.txt`
