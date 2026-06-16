---
created: 2026-06-13
updated: 2026-06-13
tags: [query-answer, hate-speech, ihc, rahmd, retrieval, experiment-lineage]
sources:
  - raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf
promotion_reason: "Durable experiment lineage for the nlp06 RA-HMD_text migration from native RA-HMD to text-only IHC retrieval variants."
---

# Query Answer: RA-HMD Text Migration Lineage

## Question

How did `nlp06:/data/cjt/hate/Try/RA-HMD_text` evolve after directly migrating the native `nlp06:/data/cjt/hate/RGCL-main/RA-HMD` RAHMD model, and what were the associated scores?

## Source Boundary

Checked on `nlp06`:

| Path | Role |
|---|---|
| `/data/cjt/hate/RGCL-main/RA-HMD` | Native RA-HMD reference. |
| `/data/cjt/hate/Try/RA-HMD_text` | Current text-only IHC experiment workspace. |
| `/data/cjt/hate/Try/RA-HMD` | Earlier migration/runtime patch reference. |
| `/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535` | Supplement runs kept outside project `runs/` because of unstable ACL behavior. |

The formal inference constraint in the current workspace is:

```text
validation/test input = post text only
```

If target information is used at validation/test time, it must be predicted from the post text. Oracle/direct target runs were removed from the formal `runs/` summaries.

## Lineage Summary

### 1. Native RA-HMD two-stage RAC

Native source:

```text
/data/cjt/hate/RGCL-main/RA-HMD
  LLAMA-FACTORY/
  Stage2/src/run_rac_lmm.py
```

The source architecture is:

```text
Stage1 LLaMA-Factory classifier / feature model
-> extracted LMM feature .pt files
-> Stage2 RAC contrastive training with hard negatives, pseudo positives, retrieval evaluation
```

This is a multimodal hateful-meme method. It was not a native IHC text method.

### 2. Mechanical text-only migration

Workspace:

```text
/data/cjt/hate/Try/RA-HMD_text
```

The first migration preserved the two-stage RA-HMD boundary:

```text
IHC post text
-> Qwen3 classifier fine-tuning
-> Qwen hidden-state feature extraction
-> native Stage2 RAC over .pt features
```

The migrated `Stage2/src/run_rac_lmm.py` mostly keeps the native RA-HMD code. The practical patches were engineering/runtime patches:

- add safer directory creation and group-writable permissions;
- add `--retrieval_backend {faiss,torch}` so dense retrieval can run without faiss-gpu;
- recognize Qwen3/Qwen2.5/Mistral feature path names;
- guard `.detach()` calls for non-tensor-like labels/features.

The 1-epoch smoke pipeline:

```text
runs/text_pipeline_1epoch_20260608_135057
```

Key logged test scores:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Evidence |
|---|---:|---:|---:|---:|---|
| Stage1 test evaluator | 0.4955 | 0.4960 | 0.4955 | 0.6663 | `runs/stage1_test_eval_20260611_131817/metrics.json` |
| Stage2 RAC 1 epoch, final classifier line | about 0.669 | 0.5549 | 0.7528 | 0.7524 | `runs/text_pipeline_1epoch_20260608_135057/logs/stage2.log`; Macro-F1 estimated from rounded log precision/recall/F1. |
| Stage2 RAC 1 epoch, retrieval line | about 0.633 | 0.4772 | 0.7662 | 0.7472 | Same log; retrieval line underperformed the classifier line. |

Interpretation: the migrated pipeline ran, but native RAC did not transfer strongly to IHC text in the first direct form.

### 3. Paper-aligned native Stage2 supplement

To check whether the weak result was only a smoke-test artifact, a paper-aligned 30-epoch supplement was run:

```text
/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535/rahmd_stage2_paper_aligned_seed1_30epoch/logs/stage2_paper_aligned.log
```

Settings included:

```text
epochs=30
metric=ip
loss=contrastive
hybrid_loss=true
hard_negatives_loss=true
in_batch_loss=true
topk=20
retrieval_backend=torch
```

Scores:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Note |
|---|---:|---:|---:|---:|---|
| Native Stage2 RAC 30 epoch, final epoch | about 0.679 | 0.5173 | 0.7614 | 0.7183 | Macro-F1 estimated from rounded log values. |
| Native Stage2 RAC 30 epoch, best observed epoch | about 0.698-0.700 | 0.5577 | 0.7683 | 0.7505 | Best observed around epoch 8; project summary conservatively records about 0.698. |

Interpretation: even with paper-aligned tuning, native Stage2 RAC stayed below 0.70 Macro-F1. The failure was not only due to the 1-epoch smoke setting.

### 4. Frozen-feature Stage2 classifier

Next change:

```text
Stage2/src/run_text_classifier.py
Stage2/scripts/IHCText/qwen3-4b-text-classifier.sh
runs/text_stage2_classifier_20260611_121938/metrics.json
```

This simplified Stage2 into a classifier over frozen Qwen features, dropping the native RAC objective.

Scores:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Threshold |
|---|---:|---:|---:|---:|---:|
| Frozen-feature Stage2 classifier | 0.6759 | 0.5613 | 0.7164 | 0.7528 | 0.46 |

Interpretation: simplifying Stage2 did not solve the transfer problem. It was comparable to the paper-aligned native RAC result, but still weak.

### 5. Single-stage text retrieval

The project then moved away from native RAC training and retained only the transferable idea: retrieval-augmented decision support.

Main files:

```text
Stage2/src/run_single_stage_llm_retrieval.py
scripts/run_single_stage_retrieval.sh
scripts/run_text_single_stage_3epoch_lora_no4bit.sh
LLAMA-FACTORY/my_configs/text/ihc/qwen3-4b_text_3epoch_lora_no4bit.yaml
```

New flow:

```text
post text
-> retrieve top-k training examples by Qwen input-embedding similarity
-> prompt LMH to answer Yes/No
-> tune threshold on validation
```

Score:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Threshold |
|---|---:|---:|---:|---:|---:|
| Single-stage text retrieval, nonfull DB | 0.7604 | 0.6781 | 0.7887 | 0.8582 | 0.835 |
| Single-stage text retrieval, full/completed-target DB | 0.7582 | 0.6700 | 0.7903 | 0.8535 | 0.85 |

Interpretation: removing native Stage2 RAC and using LMH-style retrieval prompting produced the first large jump.

### 6. Predicted-target retrieval

The next redesign treated target as a latent query signal:

```text
post text -> predicted target -> target embedding retrieval -> retrieved examples -> LMH Yes/No
```

Important constraint: validation/test never use gold target. Targets are predicted from post text.

The database side has two views:

- nonfull/default: only toxic train rows keep native IHC targets; not-toxic rows have no target;
- full/completed: completed target view via `--no-native-toxic-targets-only`.

Before parser tightening:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Threshold |
|---|---:|---:|---:|---:|---:|
| Full target-only | 0.7650 | 0.6816 | 0.7945 | 0.8534 | 0.79 |
| Nonfull target-only | 0.7523 | 0.6759 | 0.7758 | 0.8532 | 0.64 |
| Full text+target | 0.7476 | 0.6708 | 0.7710 | 0.8494 | 0.735 |
| Nonfull text+target | 0.7412 | 0.6583 | 0.7678 | 0.8425 | 0.885 |

After target parser tightening:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Threshold |
|---|---:|---:|---:|---:|---:|
| Nonfull target-only | 0.7895 | 0.7119 | 0.8181 | 0.8749 | 0.72 |
| Full target-only | 0.7889 | 0.7082 | 0.8197 | 0.8791 | 0.72 |
| Nonfull text+target | 0.7589 | 0.6749 | 0.7881 | 0.8592 | 0.90 |
| Full text+target | 0.7487 | 0.6688 | 0.7742 | 0.8568 | 0.75 |

Interpretation: predicted target-only retrieval became the strongest single-adapter route; text+target mixing did not consistently help.

### 7. Target parser cleanup, cluster retrieval, and Macro-F1 thresholding

Backups show the incremental 2026-06-12 edits:

| Change | Backup |
|---|---|
| Target parser cleanup and shorter generation | `Stage2/src/run_single_stage_llm_retrieval.py.bak_20260612_112336_target_parse` |
| Target cluster retrieval via `--target-cluster-threshold` | `Stage2/src/run_single_stage_llm_retrieval.py.bak_20260612_cluster_threshold` |
| Validation Macro-F1 threshold tuning and `macro_f1` recording | `Stage2/src/run_single_stage_llm_retrieval.py.bak_20260612_macro_threshold` |

Cluster results:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Threshold |
|---|---:|---:|---:|---:|---:|
| Nonfull target cluster 0.70 | 0.7914 | 0.7104 | 0.8229 | 0.8801 | 0.805 |
| Nonfull target cluster 0.80 | 0.7938 | 0.7143 | 0.8245 | 0.8784 | 0.80 |
| Full target cluster 0.70 | 0.7905 | 0.7101 | 0.8213 | 0.8812 | 0.72 |
| Full target cluster 0.80 | 0.7935 | 0.7142 | 0.8240 | 0.8823 | 0.72 |

Interpretation: clustering added a small improvement in the single-adapter predicted-target setting. Nonfull and full DB were nearly tied; full DB gave slightly higher AUROC but not higher Macro-F1.

### 8. Dual adapter and uncertainty gate

The project then trained separate adapters:

```text
target extractor adapter:
LLAMA-FACTORY/checkpoints/qwen3-4b/lora/ihc_text_target_v1/target_extraction/extractor_seed42_3epoch_lora8_alpha16_no4bit

target-then-classifier adapter:
LLAMA-FACTORY/checkpoints/qwen3-4b/lora/ihc_text_target_v1/target_then_classifier/classifier_seed42_3epoch_lora8_alpha16_no4bit
```

Relevant files:

```text
LLAMA-FACTORY/scripts/ihc/prepare_ihc_target_extraction_data.py
LLAMA-FACTORY/my_configs/text/ihc/qwen3-4b_target_extractor_3epoch_lora_no4bit.yaml
LLAMA-FACTORY/my_configs/text/ihc/qwen3-4b_target_then_classifier_3epoch_lora_no4bit.yaml
scripts/run_target_then_classifier_training.sh
```

Scores:

| Variant | Test Macro-F1 | Toxic F1 | Acc | AUROC | Retrieval used |
|---|---:|---:|---:|---:|---:|
| Dual adapter + target cluster 0.80 | 0.7863 | 0.7038 | 0.8181 | 0.8869 | 100% target-mode run |
| Dual adapter + target retrieval, no cluster | 0.7881 | 0.6952 | 0.8288 | 0.8866 | 100% |
| Dual adapter + uncertainty gate + target cluster | 0.7981 | 0.7098 | 0.8368 | 0.8870 | 94 / 1869 test rows, about 5.0% |
| Dual adapter base-only, no retrieval | 0.7965 tuned; 0.7994 at threshold 0.5 | 0.7054 tuned; 0.7152 at 0.5 | 0.8373 tuned; 0.8347 at 0.5 | 0.8883 | 0% |

Interpretation: the best logged tuned run is the uncertainty-gated variant, but ablations show that most of the gain comes from the stronger target-then-classifier base adapter and calibration, not from always-on retrieval. At threshold 0.5, base-only slightly exceeds the gated tuned score.

## Current Interpretation

The clean lineage is:

```text
native RA-HMD RAC
-> mechanical text-only IHC migration
-> paper-aligned native Stage2 check
-> frozen-feature classifier simplification
-> single-stage LMH text retrieval
-> predicted-target retrieval
-> target parser + cluster + Macro-F1 thresholding
-> dual-adapter and uncertainty-gated retrieval ablations
```

The useful transferred idea is retrieval-augmented decision support, not the native multimodal RAC objective. Direct RAC transfer stayed below about 0.70 Macro-F1. Single-stage retrieval lifted performance to 0.7604. Predicted-target retrieval lifted it to 0.7895, and target clustering to 0.7938. The best tuned run reached 0.7981 with uncertainty-gated retrieval, but the base-only dual-adapter ablation reached 0.7965 tuned and 0.7994 at threshold 0.5, so retrieval should be presented as auxiliary rather than the main source of the final gain.

## Bottleneck

The current target retrieval bottleneck is target coverage:

```text
predicted full_080 test empty targets: 1469 / 1869
raw output starts with None: 1467 / 1469 empty cases
```

This means parser filtering is not the main reason target-RAG fails on many rows. The target generator usually emits `None` as the first line.

Likely causes recorded in the project docs:

- the original single-adapter generator was a classification adapter, not a target-extraction adapter;
- the target-generation prompt explicitly permits `None`;
- many toxic examples have implicit or contextual targets rather than short explicit group names.

## Post-ablation Direction Audit: 2026-06-13

After checking the full project tree and supplement directory, several plausible next directions have already been tried and should not be repeated as if they were new:

| Direction | Already done? | Evidence | Result |
|---|---|---|---|
| Dedicated target extractor adapter | yes | `LLAMA-FACTORY/scripts/ihc/prepare_ihc_target_extraction_data.py`, `qwen3-4b_target_extractor_3epoch_lora_no4bit.yaml`, `runs/target_then_classifier_training_20260612_182600` | Dual-adapter target coverage improved substantially, but retrieval did not become the main source of gain. |
| Target-then-classifier adapter | yes | `qwen3-4b_target_then_classifier_3epoch_lora_no4bit.yaml` and `target_then_classifier_training_20260612_182600` | Base-only dual-adapter ablation reached 0.7965 tuned / 0.7994 at threshold 0.5. |
| Always-on dual-adapter target retrieval | yes | `/home/cjt/.../dual_adapter_target_no_cluster/metrics.json` | 0.7881 tuned; worse than base-only. |
| Dual-adapter target cluster retrieval | yes | `runs/target_then_classifier_training_20260612_182600/dual_adapter_cluster080_eval/metrics.json` | 0.7863 tuned; cluster did not help in this setting. |
| Uncertainty-gated retrieval | yes | `runs/uncertainty_gated_target_cluster080_20260612_211500/metrics.json` | 0.7981 tuned, but retrieval used only 94 / 1869 test rows. |
| Macro-F1 threshold tuning | yes | current `Stage2/src/run_single_stage_llm_retrieval.py` and `macro_threshold_rescore_20260612.json` | Current metrics use validation-tuned Macro-F1 thresholds where available. |
| Parser cleanup | yes | `run_single_stage_llm_retrieval.py.bak_20260612_112336_target_parse` | Improved single-adapter predicted-target retrieval. |
| Target cluster threshold sweep | yes, narrow sweep | `cluster_070`, `cluster_080`, `full_cluster_070`, `full_cluster_080` | Gains are small; further sweeping is low priority. |

Additional direct prediction-file diagnostics:

| Run | Predicted target coverage on test toxic rows | Predicted target coverage on test not-toxic rows | Test Macro-F1 |
|---|---:|---:|---:|
| Single-adapter target cluster 0.80 | 237 / 547 = 43.3% | 163 / 1322 = 12.3% | 0.7938 |
| Dual-adapter base-only / no retrieval | 418 / 547 = 76.4% | 610 / 1322 = 46.1% | 0.7965 tuned; 0.7994 at 0.5 |
| Dual-adapter uncertainty-gated cluster | 418 / 547 = 76.4% | 610 / 1322 = 46.1% | 0.7981 |
| Dual-adapter no-cluster always retrieval | 418 / 547 = 76.4% | 610 / 1322 = 46.1% | 0.7881 |

The dual-adapter target extractor already fixed much of the original target coverage problem. The remaining problem is not simply "extract more targets"; it is that using those targets for retrieval can damage otherwise correct base decisions.

Two ablation comparisons make this clear:

| Comparison | Changed predictions | Helped | Hurt | Interpretation |
|---|---:|---:|---:|---|
| Base-only vs uncertainty-gated cluster | 19 threshold-label changes | 9 base-wrong rows fixed | 10 base-right rows broken | Gate is nearly neutral at the label level; most of the 0.7981 comes from the base adapter/calibration. |
| Base-only vs always-on no-cluster retrieval | 164 threshold-label changes | 74 base-wrong rows fixed | 90 base-right rows broken | Always-on retrieval is net harmful. |

Revised next directions:

1. Do not redo target extractor training as the main next step. It has already been done and improved coverage.
2. Do not do more broad target-cluster/top-k sweeps before explaining retrieval harm.
3. Build an explicit retrieval-trust diagnostic/calibrator from existing prediction fields:
   - `base_prob_yes`;
   - `retrieval_prob_yes`;
   - `abs(base_prob_yes - 0.5)`;
   - `target_empty`;
   - `target_count`;
   - retrieved positive ratio;
   - maximum and average similarity;
   - cluster size.
4. Use the calibrator or a small rule search to decide when retrieval is allowed to override the base classifier. The first target is not a larger retrieval gain; it is reducing the 90 base-right to retrieval-wrong flips while preserving as many of the 74 fixes as possible.
5. Add durable error-slice reports from prediction JSONL files. Current project files have predictions, but no standalone slice report artifact for base-only versus gated versus always-on retrieval.
6. Only after the retrieval-trust mechanism is understood, consider target alias/vocabulary fallback. It should be evaluated as a precision-controlled support feature, not as a blanket target-coverage fix.

## Link Check

Input:

- IHC text rows from `/data/cjt/hate/AnyCode-xu-l20/DATA/llm_restructed/IHC_target_v1`;
- train 14930, valid 1865, test 1869;
- test positives 547, negatives 1322.

Processing:

- native RAC uses frozen/extracted Qwen features plus contrastive and classification losses;
- single-stage retrieval uses Qwen input embeddings and LMH Yes/No probabilities;
- target retrieval predicts target strings from post text, then retrieves target-level train entries;
- threshold is tuned on validation Macro-F1 in current runs.

State changes:

- Stage2 native RAC is retained only for reproduction;
- `Stage2/src/run_single_stage_llm_retrieval.py` became the active main script;
- target generation, cluster retrieval, Macro-F1 recording, dual-adapter support, and uncertainty gating were added as dated changes.

Output:

- primary metric is test Macro-F1;
- toxic F1, accuracy, and AUROC are secondary diagnostics.

Upstream/downstream impact:

- RA-HMD should not be described as successfully transferred wholesale;
- future writeups should say that native RAC was mechanically migrated and tested, but the successful adaptation is text-only predicted-target retrieval plus stronger base classification/calibration;
- oracle/direct target results are upper bounds only and should not be reported as deployable formal results.

## Evidence Paths

Core project docs:

```text
/data/cjt/hate/Try/RA-HMD_text/README.md
/data/cjt/hate/Try/RA-HMD_text/PROJECT_INDEX.md
/data/cjt/hate/Try/RA-HMD_text/PROJECT_OVERVIEW.md
/data/cjt/hate/Try/RA-HMD_text/runs/README.md
/data/cjt/hate/Try/RA-HMD_text/docs/EXPERIMENT_STATUS_20260612.md
/data/cjt/hate/Try/RA-HMD_text/docs/TEXT_ONLY_PROJECT_SUMMARY_20260613.md
```

Key metric artifacts:

```text
/data/cjt/hate/Try/RA-HMD_text/runs/stage1_test_eval_20260611_131817/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/text_stage2_classifier_20260611_121938/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/single_stage_text_3epoch_lora8_alpha16_no4bit_20260611_155514/single_stage_text_eval/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/target_parse_fix_4way_20260612_112814/nonfull_target_target_only/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/cluster_rag_threshold_2way_20260612_153938/cluster_080/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/full_target_cluster_rag_threshold_2way_20260612_162907/full_cluster_080/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/target_then_classifier_training_20260612_182600/dual_adapter_cluster080_eval/metrics.json
/data/cjt/hate/Try/RA-HMD_text/runs/uncertainty_gated_target_cluster080_20260612_211500/metrics.json
/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535/dual_adapter_base_only_no_retrieval_retry/metrics.json
/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535/dual_adapter_target_no_cluster/metrics.json
/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535/rahmd_stage2_paper_aligned_seed1_30epoch/logs/stage2_paper_aligned.log
```
