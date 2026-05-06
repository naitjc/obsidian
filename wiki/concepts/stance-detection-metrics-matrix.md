---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, stance-detection, metrics, verification]
sources: []
---

# Stance Detection Metrics Matrix

This page is a verification workspace, not a leaderboard. Stance papers mix in-domain, zero-shot, cross-lingual, conversational, multimodal, and LLM-prompted settings, so exact scores should not be compared globally without matching dataset, split, and evaluation protocol.

## Verification Policy

- `visually-verified`: the original PDF page was rendered to PNG and the table values were checked visually.
- `table-located`: a likely result table or benchmark line was located in PDF extraction; use internally but visually check the PDF before external citation.
- `pending-manual-verification`: the page has relevant claims but automatic extraction did not reliably preserve table structure.
- Do not cite exact numbers externally unless the original table has been manually checked.

## Priority Evidence Rows

| Paper | Scenario | Evidence Status | Evidence Located | Next Action |
|---|---|---|---|---|
| [[143-zhao-2024-zerostance-leveraging-chatgpt-for-open-domain-stance-detection-via-dataset-generation|ZeroStance]] | Open-domain data generation | visually-verified | Rendered Table 4 on PDF page 7. ZeroStance reports pstance 77.63, ibm30k 94.42, sem16 59.28, vast 72.24, covid 67.54, wtwt 31.60, Avg 67.12; ChatGPT no-training baseline Avg is 68.11. | PNG: `tmp/pdfs/stance-zerostance-page-07.png`. |
| [[144-zhao-caragea-2024-ez-stance-a-large-dataset-for-english-zero-shot-stance-detection|EZ-STANCE]] | Large zero-shot benchmark | visually-verified | Rendered Table 2 on PDF page 3 and Table 7 on page 7. EZ-STANCE reports 40,678 targets and 47,316 examples. Subtask A Table 7 reports BART-MNLI-ep mixed-target scores M/N/C = .812/.669/.885 and noun-phrase target scores M/N/C = .446/.687/.322. | PNGs: `tmp/pdfs/stance-ezstance-page-03.png`, `tmp/pdfs/stance-ezstance-page-07.png`. |
| [[026-ding-2024-edda-an-encoder-decoder-data-augmentation-framework-for-zero-shot-stance-detection|EDDA]] | Encoder-decoder augmentation | visually-verified | Rendered Table 1 on PDF page 6. EDDA-GPT reports SEM16 HC 77.4, FM 69.7, LA 62.7, DT 69.8; VAST 100% Pro 66.9, Con 68.2, All 75.1; VAST 10% Pro 62.6, Con 66.9, All 72.7. EDDA-LLaMA reports VAST 100% All 76.3 and VAST 10% All 73.2. | PNG: `tmp/pdfs/stance-edda-page-06.png`. |
| [[100-taranukhin-2024-stance-reasoner-zero-shot-stance-detection-on-social-media-with-explicit-reasoning|Stance Reasoner]] | Explicit reasoning | visually-verified | Rendered Table 2 on PDF page 6. Stance Reasoner with LLaMA 65B reports macro-F1 SemEval 72.6, Covid-19 76.2, WT-WT 78.3; Vicuna 13B reports 65.9, 74.6, 73.6. | PNG: `tmp/pdfs/stance-reasoner-page-06.png`. |
| [[111-weinzierl-harabagiu-2024-tree-of-counterfactual-prompting-for-zero-shot-stance-detection|Tree-of-Counterfactual Prompting]] | Counterfactual prompting | visually-verified | Rendered Tables 2 and 3 on PDF page 6. GPT-4-ToC reports SemEval macro F1 77.1, macro P 96.8, macro R 64.6; CoVAXFRAMES macro F1 79.1, macro P 90.2, macro R 70.8. GPT-3.5-ToC reports SemEval macro F1 69.4 and CoVAXFRAMES macro F1 64.4. | PNG: `tmp/pdfs/stance-toc-page-06.png`. |
| [[137-zhang-2024-an-llm-enabled-knowledge-elicitation-and-retrieval-framework-for-zero-shot-cross-lingual-stance-iden|LLM-enabled knowledge elicitation]] | Cross-lingual zero-shot | visually-verified | Rendered Table 2 on PDF page 7. KEAR zero-shot reports Politics de->fr Acc/F1 79.3/79.2, CIC es->ca 54.0/52.5, and VaxxStance es->eu 55.5/53.1; the same values are shown against cross-lingual baselines. | PNG: `tmp/pdfs/stance-kear-page-07.png`. |
| [[075-li-zhang-2024-pro-woman-anti-man-identifying-gender-bias-in-stance-detection|Gender bias in stance]] | Bias analysis | visually-verified | Rendered Table 5 on PDF page 4. GenderStance bias table reports VAST-trained TTS F1 78.6 with deltas -0.5, -0.4, 2.6, -2.6; SemEval-trained TTS F1 58.7 with deltas -4.0, 5.0, 12.2, -12.2; zero-shot GPT-4 bias deltas are 0.2, 0.1, 0.7, -1.5. | PNG: `tmp/pdfs/stance-genderbias-page-4.png`. |
| [[085-niu-2024-a-challenge-dataset-and-effective-models-for-conversational-stance-detection|Conversational stance]] | Dialogue/context stance | visually-verified | Rendered Tables 6 and 7 on PDF page 7. In-target MT-CSD with conversation history reports GLAN target scores Bitcoin 56.95, Tesla 52.38, SpaceX 55.98, Biden 38.15, Trump 48.91, Avg 50.47. Cross-target Table 7 reports GLAN best within-domain DT->JB 30.10, JB->DT 31.56, SX->TS 40.08, TS->SX 40.85. | PNG: `tmp/pdfs/stance-mtcsd-page-07.png`. |
| [[141-zhang-2025-mpvstance-mitigating-hallucinations-in-stance-detection-with-multi-perspective-verification|MPVStance]] | Hallucination mitigation | visually-verified | Rendered Tables 1 and 2 on PDF page 7. On SEM16, MPVStance Qwen2.5-7B reports DT/HC/FM/LA/A/CC = 81.4/82.0/84.2/81.5/81.9/81.7; LLaMA3.1-8B reports 80.4/82.3/79.0/81.8/81.2/82.6. On VAST, Mistral-7B-Instruct reports Zero-Shot 83.2, Few-Shot 82.0, Overall 83.1. | PNG: `tmp/pdfs/stance-mpvstance-page-07.png`. |
| [[142-zhang-2025-t-mad-target-driven-multimodal-alignment-for-stance-detection|T-MAD]] | Multimodal alignment | visually-verified | Rendered Table 1 on PDF page 6. In-target multimodal results show T-MAD+CWVF scores MTSE DT/JB 75.00/77.50, MCCQ CQ 76.20, MWTWT CA/CE/AC/AH/DF 81.30/73.50/74.80/77.10/87.30, MRUC RUS/UKR 50.20/66.90, and MTWQ MOC/TOC 73.50/64.30. | PNG: `tmp/pdfs/stance-tmad-page-06.png`. |

## Direction-Level Use

- Safe internal claim: the stance direction is dominated by zero-shot target generalization, LLM/data augmentation, target-aware modeling, and reliability checks.
- Unsafe without manual verification: exact SOTA rank, cross-paper numeric superiority, or claims that one method family dominates all stance settings.
