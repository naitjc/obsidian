# newRAHMD Local Bundle Audit — 2026-06-29

## Scope

This manifest records the current local staging bundle at `experiments/server-sync/staging/newRAHMD/`. It does not assert that the remote run status recorded on 2026-06-17 is still current; no server was checked during this organization pass.

The stale `experiments/server-sync/staging/newRAHMD.tar.gz` transfer archive was removed because it predated files now listed by the bundle manifest. Rebuild a transfer archive from the staging directory only when the bundle is next synced.

## Portable Files

| Relative path | SHA-256 |
|---|---|
| `MANIFEST.md` | `f12958e5247f540b24a9ad021d20ae15b3032116d4177cb45cb8d1b30dcdb696` |
| `README.md` | `f3ad484980fb30b55e5f9127f38f51608b9d31ef5225b4e924096153c7ace5ed` |
| `assets/sft-gtar-framework.png` | `2e8d8bd742eabf8557aed323b9b9fca813a74710b4f426efc44e20278b7bd7be` |
| `configs/qwen3_4b_router_lora.yaml` | `4278fa235a863dc6e19f7c7d8ad4d01bf05137c7cb32f540358d4a9fe3ec5987` |
| `run_full_ihc_qwen3_4b.sh` | `34cc076e67b2b87a6d0bf8ca34811db5ee60146740ad9c1b64b93a3fb8890612` |
| `scripts/prepare_router_sft_data.py` | `2d6e1f5e1fecce8fa7959a2280cfc28af1b34d270fb46601478c8b380b10e018` |
| `scripts/run_gtar_pipeline.py` | `265903b3e8dc4d9c22e247f493c280bd83c178b9a7f13830c3c7dc61eefe899e` |
| `scripts/train_router_lora_hf.py` | `5b37b286d201d0edba1dead5247f92004a1579a68bdef2ed832bb0230d41d739` |
| `scripts/update_router_config.py` | `b61598a50cb98e143ea1bb8bdc857f464eb1efd793d54c646deaebdbe122634b` |

## Boundary

- `runs/` remains local run state and is excluded from the portable file list.
- The exact dataset, base-model, environment, and remote target assumptions remain documented in the staging `README.md` and `MANIFEST.md`.
- Refresh this central manifest whenever portable code, configs, docs, or assets change.
