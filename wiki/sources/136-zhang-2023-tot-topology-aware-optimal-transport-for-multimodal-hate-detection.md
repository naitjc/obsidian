---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, benchmark, contrastive-learning, causal, explainability]
sources: [raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf]
---

# Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection

## Metadata
- Source file: `raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf`
- Year: 2023
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Enabling explorations were made for flourishing genceofalignmentrepresentedbythepair-wisedotproduct hateful meme detection studies by publishing benchmarks.
- Approaches of multimodal hateful memes classifica- soningscoresbasedoncross-modalmulti-headattentionto tion (Kiela et al.
- TheHatefulMemes This research was funded by the National Natural Science Challenge: Detecting Hate Speech in Multimodal Memes.

## Method
- Previous workhasmadeenlighteningexplorationindetectingex- plicithateremarks.However,mostoftheirapproaches neglect the analysis of implicit harm, which is partic- ularly challenging as explicit text markers and demo- graphic visual cues are often twisted or missing.
- To address these semantic gap is- sues,weproposeTOT:atopology-awareoptimaltrans- Figure1:Differencesbetweenexplicit-alignedandimplicit- portframeworktodeciphertheimplicitharminmemes aligned memes.
- However, under the influence visual-linguisticmodels(Das,Wahi,andLi2020;Velioglu, of major events such as the Russian-Ukrainian conflict and Rose, and Analytics 2020).
- However, these approaches ne- COVID-19, these platforms are flooded with hateful con- glectthenuanceofthemultimodalaligningprocess,which tent,disseminatingdiscriminatorystatementstowardsocial is necessary for subsequent reasoning procedures.

## Data and Evaluation Setup
- The newly achieved state-of-the-art performance ontwopubliclyavailablebenchmarkdatasets,together hatefulcontentisconcealed.Thecriticalfactorindetecting withfurthervisualanalysis,demonstratethesuperiority harmful memes is combining well-aligned visual-linguistic ofTOTincapturingimplicitcross-modalalignment.
- a large number of benchmark datasets (Bretschneider and OThastheabilitytoreducedistributionalbiasinamorein- Peters 2017; Ross et al.
- Specif- Although the existing methods of hateful content detection ically, we leverage an optimal transport kernel method to have yielded considerable experimental progress and com- reformulate the alignment problem across different modal- mercial application, theyjust focused on text-based hateful ities.
- Enabling explorations were made for flourishing genceofalignmentrepresentedbythepair-wisedotproduct hateful meme detection studies by publishing benchmarks.

## Results and Claims
- The newly achieved state-of-the-art performance ontwopubliclyavailablebenchmarkdatasets,together hatefulcontentisconcealed.Thecriticalfactorindetecting withfurthervisualanalysis,demonstratethesuperiority harmful memes is combining well-aligned visual-linguistic ofTOTincapturingimplicitcross-modalalignment.
- state-of-the-art performance by a large margin on two OptimalTransport publicly available benchmarks.
- With the constructed TOT graphs, we perform dynam- TOTagainstotherstate-of-the-artunimodalandmultimodal ically topology reasoning to capture the inner-modal cor- approaches.

## Limitations and Follow-ups
- a large number of benchmark datasets (Bretschneider and OThastheabilitytoreducedistributionalbiasinamorein- Peters 2017; Ross et al.
- TheHatefulMemes This research was funded by the National Natural Science Challenge: Detecting Hate Speech in Multimodal Memes.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, multimodal, explainability
- Mentioned datasets: hateful memes, twitter
- Mentioned metrics: f1, macro-f1, accuracy

## Abstract (Extracted)
> Abstract Multimodal hate detection, which aims to identify the harmful content online such as memes, is crucial for building a wholesome internet environment. Previous workhasmadeenlighteningexplorationindetectingex- plicithateremarks.However,mostoftheirapproaches neglect the analysis of implicit harm, which is partic- ularly challenging as explicit text markers and demo- graphic visual cues are often twisted or missing. The leveraged cross-modal attention mechanisms also suf- fer from the distributional modality gap and lack log- ical interpretability. To address these semantic gap is- sues,weproposeTOT:atopology-awareoptimaltrans- Figure1:Differencesbetweenexplicit-alignedandimplicit- portframeworktodeciphertheimplicitharminmemes aligned memes. The aligning procedure is naturally com- scenario, which formulates the cross-modal aligning pleted in explicit harmful content, but is indispensable for problem as solutions for optimal transportation plans. Specifically, we leverage an optimal transport kernel implicitcases. method to capture complementary information from multiple modalit

## Benchmark Evidence Lines
- ing. The newly achieved state-of-the-art performance
- state-of-the-art performance by a large margin on two
- TOTagainstotherstate-of-the-artunimodalandmultimodal
- outperforms the existing methods by a larger margin, with by ablating topology reasoning score and residual global
- 3.13% absolute points of M-F1 improvement on Harm-C score. We also report different training strategies for these
- score (1.57% points in Acc and 1.45% points in M-F1 for
- Our proposed TOT outperforms other methods by a larger
- margin, with 5.66% absolute Accuracy points on Harm-

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
