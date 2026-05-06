---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, few-shot, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Chen 等 - 2021 - Image Manipulation Detection by Multi-View Multi-Scale Supervision.pdf]
---

# Chen 等 - 2021 - Image Manipulation Detection by Multi-View Multi-Scale Supervision

## Metadata
- Source file: `raw/sources/Chen 等 - 2021 - Image Manipulation Detection by Multi-View Multi-Scale Supervision.pdf`
- Year: 2021
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Image Manipulation Detection by Multi-View Multi-Scale Supervision
- The key challenge of image manipulation detection is
- level and image-level manipulation detection.
- Figure 1. Image manipulation detection by the state-of-the-

## Method
- model strikes a good balance between sensitivity and specificity.
- Figure 2. Conceptual diagram of the proposed MVSS-Net model. We use the edge-supervised branch and the noise-sensitive branch to
- learn semantic-agnostic features for manipulation detection, and multi-scale supervision to strike a balance between model sensitivity and
- either by pre-defined high-pass filters [9] or by their train- for retinal lesion segmentation, we propose multi-view fea-
- [21, 29]. Note that the prior art [29] uniformly concatenates • We propose MVSS-Net as a new network for image manip-

## Data and Evaluation Setup
- we term MVSS-Net. Extensive experiments on five bench-
- capture semantic information, making the network dataset-
- ports that DeepLabv2 [4] trained on the CASIAv2 dataset
- [8] performs well on the CAISAv1 dataset [7] homologous
- COVER dataset [25]. A similar behavior of FCN [18] is

## Results and Claims
- Unsurprisingly, the state-of-the-arts are deep learning
- that novel elements introduced by slicing and/or inpainting improve their specificity by learning from the authentic.
- by the prior art, and consequently improve the model speci-
- state-of-the-art. Code and models are available at https:
- Table 1. A taxonomy of the state-of-the-art for image manipulation detection. Note that edge and image labels used in this work are

## Limitations and Follow-ups
- The key challenge of image manipulation detection is
- automatically extracted from pixel-level annotations. So our multi-scale supervision does not use extra manual annotation.
- distinct tasks, the challenge lies in how to strike a proper ance between detection sensitivity and specificity, the multi-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, synthetic-data, retrieval, multimodal, emotion-recognition, benchmark, graph
- Mentioned datasets: TOP
- Mentioned metrics: f1, precision, recall, auc

## Abstract (Extracted)
> The key challenge of image manipulation detection is how to learn generalizable features that are sensitive to ma- nipulations in novel data, whilst specific to prevent false alarms on authentic images. Current research emphasizes the sensitivity, with the specificity overlooked.

## Benchmark Evidence Lines
- capture semantic information, making the network dataset-
- ports that DeepLabv2 [4] trained on the CASIAv2 dataset
- [8] performs well on the CAISAv1 dataset [7] homologous
- COVER dataset [25]. A similar behavior of FCN [18] is
- Unsurprisingly, the state-of-the-arts are deep learning
- alone [16, 27] or together with the input image [14, 26, 30]. ulation detection. To the best of our knowledge (Table 1),
- a public dataset, say CASIAv2 [8], and then test it on other
- public datasets such as NIST16 [12], Columbia [13], and

## Related Concepts
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
