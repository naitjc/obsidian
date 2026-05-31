# Fine-Tuning Experiment Eval Scores

**SOTA Reference (Macro F1):** IHC = 81.94 | SBIC = 84.30

## IHC Dataset

| Model                    | Schema       | Accuracy | Precision | Recall | F1     | Macro F1 | Δ vs SOTA |
|--------------------------|--------------|----------|-----------|--------|--------|----------|-----------|
| Mistral-7B-Instruct-v0.3 | class_only   | 0.8550   | 0.7500    | 0.7569 | 0.7534 | 0.8254   | +0.60 ✅  |
| Mistral-7B-Instruct-v0.3 | class_target | 0.8646   | 0.7702    | 0.7660 | 0.7681 | 0.8363   | +1.69 ✅  |
| Mistral-7B-Instruct-v0.3 | full         | 0.8604   | 0.7527    | 0.7788 | 0.7655 | 0.8330   | +1.36 ✅  |
| Qwen2.5-7B               | class_only   | 0.8438   | 0.7249    | 0.7514 | 0.7379 | 0.8133   | -0.61     |
| Qwen2.5-7B               | class_target | 0.8571   | 0.7500    | 0.7678 | 0.7588 | 0.8287   | +0.93 ✅  |
| Qwen2.5-7B               | full         | 0.8582   | 0.7573    | 0.7587 | 0.7580 | 0.8289   | +0.95 ✅  |
| Qwen3-4B                 | class_only   | 0.8368   | 0.7232    | 0.7166 | 0.7199 | 0.8024   | -1.70     |
| Qwen3-4B                 | class_target | 0.8545   | 0.7561    | 0.7422 | 0.7491 | 0.8233   | +0.39 ✅  |
| Qwen3-4B                 | full         | 0.8357   | 0.7281    | 0.7002 | 0.7139 | 0.7993   | -2.01     |
| Qwen3-8B                 | class_only   | 0.8373   | 0.7189    | 0.7294 | 0.7241 | 0.8044   | -1.50     |
| Qwen3-8B                 | class_target | 0.8480   | 0.7458    | 0.7294 | 0.7375 | 0.8153   | -0.41     |
| Qwen3-8B                 | full         | 0.8448   | 0.7358    | 0.7331 | 0.7344 | 0.8124   | -0.70     |

> ✅ = exceeds SOTA or is within 0.05 Macro F1 of SOTA.

### IHC - Target Jaccard (toxic only)

| Model                    | class_target | full   |
|--------------------------|--------------|--------|
| Mistral-7B-Instruct-v0.3 | 0.3633       | 0.3769 |
| Qwen2.5-7B               | 0.3661       | 0.3376 |
| Qwen3-4B                 | 0.3523       | 0.3287 |
| Qwen3-8B                 | 0.3425       | 0.3410 |

---

## SBIC Dataset

| Model                    | Schema       | Accuracy | Precision | Recall | F1     | Macro F1 | Δ vs SOTA |
|--------------------------|--------------|----------|-----------|--------|--------|----------|-----------|
| Mistral-7B-Instruct-v0.3 | class_only   | 0.8783   | 0.8371    | 0.8732 | 0.8547 | 0.8750   | +3.20 ✅  |
| Mistral-7B-Instruct-v0.3 | class_target | 0.8802   | 0.8280    | 0.8935 | 0.8595 | 0.8775   | +3.45 ✅  |
| Mistral-7B-Instruct-v0.3 | full         | 0.8819   | 0.8470    | 0.8690 | 0.8579 | 0.8784   | +3.54 ✅  |
| Qwen2.5-7B               | class_only   | 0.8717   | 0.8359    | 0.8550 | 0.8453 | 0.8678   | +2.48 ✅  |
| Qwen2.5-7B               | class_target | 0.8725   | 0.8332    | 0.8617 | 0.8472 | 0.8689   | +2.59 ✅  |
| Qwen2.5-7B               | full         | 0.8753   | 0.8407    | 0.8586 | 0.8496 | 0.8715   | +2.85 ✅  |
| Qwen3-4B                 | class_only   | 0.8672   | 0.8314    | 0.8482 | 0.8397 | 0.8632   | +2.02 ✅  |
| Qwen3-4B                 | class_target | 0.8732   | 0.8334    | 0.8633 | 0.8481 | 0.8696   | +2.66 ✅  |
| Qwen3-4B                 | full         | 0.8802   | 0.8478    | 0.8628 | 0.8552 | 0.8765   | +3.35 ✅  |
| Qwen3-8B                 | class_only   | 0.8715   | 0.8358    | 0.8545 | 0.8450 | 0.8676   | +2.46 ✅  |
| Qwen3-8B                 | class_target | 0.8832   | 0.8489    | 0.8701 | 0.8593 | 0.8797   | +3.67 ✅  |
| Qwen3-8B                 | full         | 0.8774   | 0.8433    | 0.8612 | 0.8521 | 0.8737   | +3.07 ✅  |

> ✅ = exceeds SOTA or is within 0.05 Macro F1 of SOTA.

### SBIC - Target Jaccard (toxic only)

| Model                    | class_target | full   |
|--------------------------|--------------|--------|
| Mistral-7B-Instruct-v0.3 | 0.6866       | 0.6634 |
| Qwen2.5-7B               | 0.6621       | 0.6510 |
| Qwen3-4B                 | 0.6633       | 0.6593 |
| Qwen3-8B                 | 0.6682       | 0.6629 |

---

## Notes

- SOTA Macro F1: **IHC = 81.94**, **SBIC = 84.30**
- `Δ vs SOTA` = (model Macro F1 − SOTA) × 100 (expressed as percentage points)
- `✅` = exceeds SOTA or is within 0.05 Macro F1 of SOTA
- `class_only`: model predicts only the `class` label (`toxic` / `non_toxic`)
- `class_target`: model predicts `class` and `target`
- `full`: model predicts `class`, `hate_class`, and `target`
- Target Jaccard is applicable to schemas that predict `target`; `class_only` experiments have `target_jaccard_toxic_only = 0.0`
- SBIC Mistral `class_target` uses the retrained `5e-5` learning-rate checkpoint from 2026-05-08.
