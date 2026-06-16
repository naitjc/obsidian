# Baselines

Use this folder for external paper code, upstream repositories, and baseline-specific reproduction work.

Keep active local experiment pipelines under `experiments/`. Promote only durable findings, adaptations, or comparison conclusions from baseline work into `wiki/`.

Do not commit large checkpoints, downloaded model caches, virtual environments, package caches, datasets, or bulk generated outputs unless their inclusion has been explicitly reviewed.

## Current Baseline Code Mirrors

| Local path | Source | Upstream | Notes |
|---|---|---|---|
| `amplehate/` | `huashan:/data/chenjt/Hate/AmpleHate` | `https://github.com/leeyejin1231/AmpleHate.git` | Code/config/docs only. Excludes `Amplehate_DATA/`, `save/`, checkpoints, and caches. Remote had local edits in config, train/test, and dataloader files when copied. |
| `cadet/` | `huashan:/data/chenjt/Hate/CADET` | `https://github.com/Shu-Wan/cadet.git` | Code/config/docs only. Excludes `CADET_DATA/`, checkpoints, and caches. |
| `harm/` | `xu-l20:/data/chenjt/hate/clone/HARM` | `https://github.com/Lorenzo815/HARM.git` via mirror URL | Code/docs only. Excludes explanation datasets, `HARM-MOE-Off/`, checkpoints, and caches. |
| `hatexplain/` | `xu-l20:/data/chenjt/hate/clone/HateXplain` | `https://github.com/hate-alert/HateXplain` | Code/docs/notebooks only. Excludes `Data/`, `Models/`, `TensorDataset/`, `best_model_json/`, checkpoints, and caches. |
| `hare-hate-speech/` | `xu-l20:/data/chenjt/hate/clone/hare-hate-speech` | `https://github.com/joonkeekim/hare-hate-speech.git` | Code/config/docs only. Excludes `data/`, checkpoints, and caches. |
| `privacy-filter/` | `xu-l20:/data/chenjt/hate/clone/privacy-filter` | `https://github.com/openai/privacy-filter.git` via mirror URL | Code/docs/examples scripts only. Excludes Git metadata and caches. |
| `rgcl-main/` | `nlp06:/data/cjt/hate/RGCL-main` | Project README points to `https://github.com/JingbiaoMei/RGCL.git` and the RGCL/RA-HMD project page | Code/config/docs only. Includes root RGCL code, RA-HMD Stage2, and LLAMA-FACTORY source/config scripts. Excludes `RA-HMD-dataset/`, `RA-HMD/LLAMA-FACTORY/data/`, `.env.local`, logs, zip archives, checkpoints, generated embeddings, caches, and model artifacts. |

## Boundary With `experiments/server-sync/`

Use `baselines/` when the main artifact is an external method repository to inspect, reproduce, or adapt.

Use `experiments/server-sync/` when the task is to stage a runnable bundle, mirror server state, upload to a server, or pull back run diagnostics. Server snapshots can inform what belongs here, but durable external code mirrors should be promoted into `baselines/` once their source and exclusion boundary are clear.
