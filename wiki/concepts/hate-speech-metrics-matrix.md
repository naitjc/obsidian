---
created: 2026-04-23
updated: 2026-04-29
tags: [synthesis, hate-speech, metrics, verification]
sources: []
---

# Hate Speech Metrics Matrix

This page is a verification workspace, not a leaderboard. Use it to track which quantitative claims are safe to cite and which still need manual PDF table checks.

## Verification Policy

- `visually-verified`: the original PDF page was rendered to PNG and the table values were checked visually.
- `table-located`: a relevant result table or table line was located in the PDF extraction; the claim can guide internal synthesis but should still be checked visually before publication.
- `pending-manual-verification`: automatic extraction found likely evidence, but the table layout or context is not reliable enough for exact citation.
- Do not cite exact numbers externally unless the row has been manually checked against the original PDF table.

## Priority Papers

| Paper | Scenario | Table Evidence Status | Table-Located Evidence | Next Action |
|---|---|---|---|---|
| [[031-elsherief-2021-latent-hatred-a-benchmark-for-understanding-implicit-hate-speech|ElSherief 2021 Latent Hatred]] | Implicit hate benchmark | visually-verified | Rendered Table 3 on PDF page 6. Binary task: BERT reports P 72.1, R 66.0, F 68.9, Acc 78.3; BERT+Aug reports P 67.8, R 73.2, F 70.4, Acc 77.5. Fine-grained implicit hate categories: BERT reports P 59.1, R 57.9, F 58.0, Acc 62.9; BERT+Aug reports P 58.6, R 59.1, F 58.6, Acc 63.8. | PNG: `tmp/pdfs/elsherief-2021-page-06.png`; Table 6 category-level appendix remains optional. |
| [[043-hartvigsen-2022-toxigen-a-large-scale-machine-generated-dataset-for-adversarial-and-implicit-hate-speech-detection|Hartvigsen 2022 ToxiGen]] | Adversarial implicit hate dataset | visually-verified | Rendered Table 1 on PDF page 3. ToxiGen reports source GPT-3, size 274,186, 98.2% implicit, and 50.1% hate class; ImplicitHateCorpus comparison row reports size 22,584, 96.8% implicit, and 39.6% hate class. | PNG: `tmp/pdfs/hartvigsen-2022-page-03.png`; exact downstream classifier-gain tables are not yet visually checked. |
| [[058-kim-2022-generalizable-implicit-hate-speech-detection-using-contrastive-learning|Kim 2022 ImpCon]] | Cross-dataset implicit hate generalization | visually-verified | Rendered Tables 3 and 4 on PDF page 6. Training on IHC: HateBERT + ImpCon reports IHC->SBIC 0.635 and IHC->DYNAHATE 0.594; BERT + AugCon + ImpCon reports IHC->SBIC 0.611. Training on SBIC: BERT + ImpCon reports SBIC->IHC 0.614 and SBIC->DYNAHATE 0.612; HateBERT + ImpCon reports SBIC->IHC 0.599 and SBIC->DYNAHATE 0.606. | PNG: `tmp/pdfs/kim-2022-impcon-page-06.png`. |
| [[095-sheth-2024-causality-guided-disentanglement-for-cross-platform-hate-speech-detection|Sheth 2024 CATCH]] | Cross-platform transfer | visually-verified | Rendered Table 1 on PDF page 7. Macro-F1 table shows CATCH best on 11 of 12 cross-platform cells; CATCH rows include GAB->Reddit 0.72, GAB->Twitter 0.69, GAB->YouTube 0.66, Reddit->YouTube 0.76, Twitter->Reddit 0.69, and YouTube->Reddit 0.72. | PNG: `tmp/pdfs/sheth-2024-catch-page-07.png`. |
| [[046-hee-2024-bridging-modalities-enhancing-cross-modality-hate-speech-detection-with-few-shot-in-context-learnin|Hee 2024 cross-modality ICL]] | Few-shot cross-modality hate detection | visually-verified | Rendered Tables 2 and 3 on PDF pages 3-4. With Latent Hatred support, Mistral-7B bests include FHM Acc/F1 0.660/0.658 and MAMI 0.705/0.701; Qwen2-7B bests include FHM 0.654/0.653 and MAMI 0.679/0.674. With FHM support, Mistral-7B bests include FHM 0.638/0.635 and MAMI 0.687/0.680; Qwen2-7B bests include FHM 0.636/0.636 and MAMI 0.676/0.674. | PNGs: `tmp/pdfs/hee-2024-crossmod-page-03.png`, `tmp/pdfs/hee-2024-crossmod-page-04.png`. |
| [[080-mei-2024-improving-hateful-meme-detection-through-retrieval-guided-contrastive-learning|Mei 2024 RGCL]] | Retrieval-guided hateful meme detection | visually-verified | Rendered Table 1 on PDF page 5. HateCLIPper w/ RGCL reports HatefulMemes AUC 87.0, Acc. 78.8; HarMeme AUC 91.8, Acc. 87.0. | PNG: `tmp/pdfs/mei-2024-rgcl-page-05.png`; appendix hyperparameters remain optional. |
| [[056-jiang-2025-learn-from-failure-causality-guided-contrastive-learning-for-generalizable-implicit-hate-speech-det|Jiang 2025 CCL]] | Failure-guided implicit hate generalization | visually-verified | Rendered Tables 2 and 3 on PDF pages 5-6. Training on IHC: CCL w/ DA reports BERT IHC 65.3, DynaHate 62.7, SBIC 78.4; HateBERT IHC 66.4, DynaHate 63.1, SBIC 77.6. Training on SBIC: CCL w/ DA reports BERT IHC 61.3, DynaHate 62.1, SBIC 84.3; HateBERT IHC 61.5, DynaHate 61.9, SBIC 84.8. | PNGs: `tmp/pdfs/jiang-2025-ccl-page-05.png`, `tmp/pdfs/jiang-2025-ccl-page-06.png`. |
| [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection|Mei 2025 RA-HMD]] | Retrieval-augmented LMM adaptation | visually-verified | Rendered Tables 1 and 2 on PDF pages 6-7. Supervised Qwen2-VL-7B w/ RA-HMD reports HatefulMemes AUC/Acc 91.1/82.1, HarMeme 93.2/88.1, MAMI 90.4/79.9, Harm-P Acc/F1 91.6/91.1, MultiOFF 71.1/64.8, PrideMM 78.1/78.4. Low-resource Qwen2-VL-7B RA-HMD+RKC reports HatefulMemes 77.1/69.3, HarMeme 88.8/81.7, MAMI 81.4/75.6, Harm-P 64.5/66.4, MultiOFF 63.8/55.6, PrideMM 69.3/69.3. | PNGs: `tmp/pdfs/mei-2025-rahmd-page-06.png`, `tmp/pdfs/mei-2025-rahmd-page-07.png`. |
| [[121-yang-2024-uncertainty-aware-cross-modal-alignment-for-hate-speech-detection|Yang 2024 UCA]] | Uncertainty-aware multimodal alignment | visually-verified | Rendered PDF page 7. UCA reports Hate Acc. 76.10, AUROC 84.32; Harm-C Acc. 88.98, F1 88.31, MMAE 0.1015; Harm-P Acc. 92.68, F1 92.66, MMAE 0.0739; Offense F1 65.89, Pre. 66.09, Rec. 66.90; Sarcasm F1 87.36, Pre. 87.13, Rec. 87.64, Acc. 87.80. | PNG: `tmp/pdfs/yang-2024-uca-page-07.png`. |
| [[136-zhang-2023-tot-topology-aware-optimal-transport-for-multimodal-hate-detection|Zhang 2023 TOT]] | Multimodal topology-aware optimal transport | visually-verified | Rendered Table 2 on PDF page 5. TOT reports 2-class Harm-C Acc 87.01, F1 85.93, MMAE 0.1634; 2-class Harm-P Acc 91.55, F1 91.29, MMAE 0.1245; 3-class Harm-C Acc 82.76, F1 55.38, MMAE 0.5027; 3-class Harm-P Acc 88.61, F1 71.54, MMAE 0.6697. | PNG: `tmp/pdfs/zhang-2023-tot-page-5.png`. |

## Direction-Level Use

- For internal synthesis, it is safe to say that the priority papers cover benchmark construction, implicit hate generalization, multimodal hateful meme detection, and cross-platform transfer.
- For external writing, cite exact values only after opening the PDF and checking the relevant table row visually.
- Avoid global SOTA rankings across these rows because datasets, splits, metrics, and model scales differ.
