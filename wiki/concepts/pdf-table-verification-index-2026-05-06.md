---
created: 2026-05-06
updated: 2026-05-06
tags: [maintenance, pdf, metrics, verification]
sources: []
---

# PDF Table Verification Index 2026-05-06

This page was generated from source links in direction metrics matrices. It narrows manual metric verification to likely PDF pages and evidence lines. It is not a substitute for visual table inspection.

## Scope

- Input pages: direction `*metrics-matrix.md` files
- Extraction method: `pdfplumber`, first 20 pages per PDF
- Verification boundary: exact benchmark values still require visual checking against the rendered PDF table

## [[004-2025-coling-main-170|2025.coling-main.170]]

- Source PDF: `raw/sources/2025.coling-main.170.pdf`
- Likely table/result pages:
  - Page 1:
    - state-of-the-art approaches in terms of over-
  - Page 2:
    - accuracy in the main task ERC. For example, as discourse structural information by analyzing the
    - can be considered noise for judging Joey’s emotion. outperforming comparable state-of-the-art methods
    - vision-language model as the fundamental archi- compared to most other state-of-the-art methods,
    - tecture that connects a vision encoder and an LLM and achieving SOTA results on the multi-modal
  - Page 6:
    - Table 1: The statistical information of three ERC
    - outlined in Table 1. In addition, the details regard-
    - the TV series Friends, including multi-person con- 2021a, 2023), the accuracy and weighted-F1 score
    - terance has an annotated emotion label including Also, the F1 score per class and macro-F1 score are
  - Page 7:
    - Table 2: The overall performance (%) of all the compared baselines and our DialogueMMT on three ERC datasets.
    - Table 3: Fine-grained results (%) of DialogueMMT and
    - 4.4 Implementation Details tains the best accuracy score and weighted-F1
    - the training, we utilize FlashAttention (Dao et al., strongest baseline (i.e., SACL_LSTM) by 3.33%
  - Page 8:
    - over other state-of-the-art methods on MELD. Al-
    - and MultiEMO on IEMOCAP, the weighted-F1
    - Table 4: Experimental results (%) of sentiment (3-cls)
    - and emotion (7-cls) classification of DialogueMMT ble 4. From Table 3 we can see that the textual
  - Page 9:
    - Table 6: Examples of utterances from the IEMOCAP, MELD, and EmoryNLP datasets for the error analysis.
    - Table 7: Experimental results (%) of ablation study. 7 Limitations
    - Table 6 shows three utterances sampled from Firstly, this work focuses on the textual and visual
    - logueMMT. accuracy of the main task, which requires the per-

## [[009-2654-rebuttal-2|2654-rebuttal-2]]

- Source PDF: `raw/sources/2654-rebuttal-2.pdf`
- Likely table/result pages:
  - Page 1:
    - accuracy across all languages, and demonstrates robust performance when dierent languages are used as the source.
  - Page 3:
    - As shown in Section 4.7, a small subset of categories exhibited decreased rather than improved accuracy. Without
  - Page 4:
    - accuracy improvement of 4.95%, while more distant Chinese (zh-CN) achieves a greater improvement of 10.93%.
    - This discrepancy stems from XLM-R's baseline performance dierences between nl-NL and zh-CN - nl-NL's original
    - accuracy was already 5.68% higher than zh-CN, hence zh-CN demonstrates more signicant gains.
    - 3. The paper could benet from some format improvements, such as more descriptive gure and table captions and
  - Page 5:
    - gure/table captions throughout would improve readability.
  - Page 6:
    - R3: We will optimize the table titles and formatting to improve the manuscript’s readability.
  - Page 7:
    - methods in accuracy across multiple languages.
    - 4. Outperforms baseline models on established multilingual SLU datasets.
    - for slot information aggregation. Even without “span“, our proposed INT still outperforms the baseline model by

## [[015-balaraman-2021-recent-neural-methods-on-dialogue-state-tracking-for-task-oriented-dialogue-systems-a-survey|Balaraman 等 - 2021 - Recent Neural Methods on Dialogue State Tracking for Task-Oriented Dialogue Systems A Survey]]

- Source PDF: `raw/sources/Balaraman 等 - 2021 - Recent Neural Methods on Dialogue State Tracking for Task-Oriented Dialogue Systems A Survey.pdf`
- Likely table/result pages:
  - Page 4:
    - goal accuracy, joint goal accuracy, requested slots bution over all the slot-value pairs, or sigmoid, to
    - F1 and time complexity. In the following, a brief get the individual probability for each slot-value
    - Average Goal Accuracy is the average accuracy
    - Joint Goal Accuracy is the primary evaluation latency in prediction, and the use of pre-trained
  - Page 5:
    - Table 1: Statistics of available data sets for the dialogue state tracking task.
  - Page 7:
    - dataset. (Balaraman and Magnini, 2021) proposed used in most of the state-of-the-art models,
  - Page 8:
    - SGD-Baseline (Rastogi et al., 2020) - 0.810 0.434 (2.1) 0.254
    - Table 2: Performance (joint goal accuracy) of DST systems on available datasets as reported in respective papers.
  - Page 13:
    - SGD-Baseline (Rastogi et al., 2020) Open Open Dynamic Rules
    - Table 3: Tracking approach of implemented by vari-

## [[049-hosseini-asl-a-simple-language-model-for-task-oriented-dialogue|Hosseini-Asl 等 - A Simple Language Model for Task-Oriented Dialogue]]

- Source PDF: `raw/sources/Hosseini-Asl 等 - A Simple Language Model for Task-Oriented Dialogue.pdf`
- Likely table/result pages:
  - Page 1:
    - leads to state-of-the-art performance on the MultiWOZ dataset. SimpleTOD is a
    - of-the-art in joint goal accuracy for dialogue state tracking, and our analysis reveals
  - Page 2:
    - Evaluation results demonstrate the advantages of SimpleTOD. It achieves 55.76 joint goal accuracy
    - • SimpleTOD – a state-of-the-art generative model for dialogue state tracking (DST).
    - • SimpleTOD is also the first model to achieve state-of-the-art performance for dialogue state
  - Page 3:
    - (DAMD) using augmented dialogue data, which achieved state-of-the-art combined score for dialogue
  - Page 4:
    - end-to-end evaluation, whereas we outperform all previous models.
  - Page 6:
    - to recent state-of-the-art methods. To the best of our knowledge, all prior work on action and response
    - for the combined score. Joint goal accuracy is used to evaluate the performance of dialogue state
    - tracking (i.e. belief state tracking). It measures the accuracy of the generated belief states as they
    - generation is computed as (BLEU + 0.5 ∗ (Inf orm + Success)).
  - Page 7:
    - Model Decoder Context Encoder Extra Supervision Joint Accuracy
    - Table 1: Evaluation of Dialogue State Tracking (DST) on MultiWOZ 2.1 using joint accuracy metric.
    - knowledge, the first system that generates state-of-the-art results judged according to dialogue state
    - Table 1 compares the joint goal accuracy to previous methods. We compare to TRADE [53],

## [[070-lin-2024-generate-then-refine-data-augmentation-for-zero-shot-intent-detection|Lin 等 - 2024 - Generate then Refine Data Augmentation for Zero-shot Intent Detection]]

- Source PDF: `raw/sources/Lin 等 - 2024 - Generate then Refine Data Augmentation for Zero-shot Intent Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - over the zero-shot LLM baseline for unseen do-
    - mains and over common baseline approaches.
  - Page 2:
    - compared to state-of-the-art data augmenta-
  - Page 3:
    - intent has 100 training examples and 30 test exam- on the accuracy of intent classification evaluation
  - Page 4:
    - Table 1: SGD train and test split: the number in paren- Refiner (Zephyr) 72.2 (5.3) 76.0 (0.8)
    - Table 2: Intent prediction accuracy is compared across
    - reported accuracy results share the same classifier
    - report on diversity (distinct-1 & 2) (Li et al., 2016; Table 3: Lexical diversity results, averaged over 5 trials.
  - Page 5:
    - ample is “Can you put a hold on my account? I’m Table 4: Intent prediction accuracy for unseen domains:
    - a customer support team)”. The refiner can remove Table 5: Intent prediction accuracy for unseen domains
    - Effect of fine-tuning on performance. The re- Table 6: Intent prediction accuracy for unseen domains
    - sults in Table 2 and 3 have shown that using refined
  - Page 8:
    - buses, hotels, services, homes, banks, calen- D Details of the SuperGen baseline

## [[072-liu-2022-cross-domain-slot-filling-as-machine-reading-comprehension-a-new-perspective|Liu 等 - 2022 - Cross-Domain Slot Filling as Machine Reading Comprehension A New Perspective]]

- Source PDF: `raw/sources/Liu 等 - 2022 - Cross-Domain Slot Filling as Machine Reading Comprehension A New Perspective.pdf`
- Likely table/result pages:
  - Page 1:
    - in accomplishing certain tasks, such as reserving a table at
    - user request “I’d like to book a table at Hat Restaurant for
  - Page 2:
    - F1 over current state-of-the-art methods in a common zero- in order to complete the task. The most popular approach for
    - of-the-art methods by 10.4% in F1 on average in a more of capturing the joint probability distribution of the utterance
  - Page 3:
    - can better learn slot semantics. A recent state-of-the-art approach an answer span a. Finally, as a result of slot filling, SLMRC
  - Page 4:
    - are accessible (e.g., SNIPS [25] and ATIS [1]), we use them TABLE I
    - Table I compares the questions generated by the three method- sponds to zero or one answer but rarely multiple answers,
  - Page 6:
    - It displays state-of-the-art performance across a wide range of
    - datasets usually have distinct schema (i.e., they usually have in F1 and matching the state-of-the-art performance [24]. In
    - C. Baseline Models V. EXPERIMENTAL RESULTS
  - Page 7:
    - F1-SCORES (%) ON SNIPS FOR ZERO-SHOT CROSS-DOMAIN ADAPTATION. F1-SCORES (%) ON SGD FOR ZERO-SHOT CROSS-DOMAIN LEARNING,
    - F1-SCORES (%) ON ATIS FOR ZERO-SHOT CROSS-DOMAIN ADAPTATION,
    - model SLMRC, in particular, produces the best F1 score on
    - each dataset, outperforming previous state-of-the-art models by

## [[087-qin-2023-end-to-end-task-oriented-dialogue-a-survey-of-tasks-methods-and-future-directions|Qin 等 - 2023 - End-to-end Task-oriented Dialogue A Survey of Tasks, Methods, and Future Directions]]

- Source PDF: `raw/sources/Qin 等 - 2023 - End-to-end Task-oriented Dialogue A Survey of Tasks, Methods, and Future Directions.pdf`
- Likely table/result pages:
  - Page 1:
    - 1We collect the related papers, baseline projects, and
  - Page 5:
    - Model Inform (%) Success (%) BLEU Combined Inform (%) Success (%) BLEU Combined
    - Table 1: Modularly EToD performance on MultiWOZ2.0 and MultiWOZ2.1. The highest scores are marked with
    - Model Match Success BLEU designed to improve adaptation ability. BORT (Sun
    - Table 2: Modularly EToD performance on of converting EToD into other task forms like
  - Page 6:
    - Table 3: Three types of KB Representation in EToD, including (a) entity triple representation; (b) row-level
  - Page 7:
    - Model BLEU Ent.F1(%) Sch.F1(%) Wea.F1(%) Nav.F1(%) BLEU Ent.F1(%) Res.F1(%) Att.F1(%) Hot.F1(%)
    - Table 4: Fully EToD performance on SMD and MultiWOZ2.1. Ent.F1, Sch.F1, Wea.F1, Nav.F1, Res.F1, Att
    - F1.and Hot.F1 stand for the abbreviation of Entity F1, Schedule F1, Weather F1, Navigation F1, Restaurant F1 and
    - Hotel F1, respectively. We adopted reported results from published literature (Qin et al., 2020b; Wu et al., 2021a;
  - Page 13:
    - Jing Zhu. 2002. Bleu: A Method for Automatic Eval- Yangming Li, and Ting Liu. 2019b. Entity-
  - Page 17:
    - Fully EToD adopts BLEU and Entity F1 to eval-
    - BLEU has been described in Section A.1.1.
    - small-scale restaurant domain dataset, which con- Entity F1 Eric and Manning (2017) is used
    - BLEU (Papineni et al., 2002) is used to measure On DST, Balaraman et al. (2021b) and Jacqmin

## [[097-su-2022-multi-task-pre-training-for-plug-and-play-task-oriented-dialogue-system|Su 等 - 2022 - Multi-Task Pre-Training for Plug-and-Play Task-Oriented Dialogue System]]

- Source PDF: `raw/sources/Su 等 - 2022 - Multi-Task Pre-Training for Plug-and-Play Task-Oriented Dialogue System.pdf`
- Likely table/result pages:
  - Page 1:
    - against previous SOTA methods show that the Secondly, the training data must be annotated for
  - Page 2:
    - 2020; Peng et al., 2021), we propose a dialogue TOD tasks reporting state-of-the-art results in
    - tails in Table 1). When applying the pre-trained
  - Page 3:
    - Table 1: The summary of data annotations and number
    - discrete latent variable structure for the response over 2.3M utterances across 80 domains. In Table
  - Page 4:
    - 3.3 Fine-Tuning to a New Task Success, and BLEU (Papineni et al., 2002). An
  - Page 5:
    - Inform Success BLEU Combined Score Inform Success BLEU Combined Score
    - Table 2: End-to-end evaluation. †: the models require the history of oracle dialogue states when making predictions
    - Inform Succ. BLEU Comb. Inform Succ. BLEU Comb. Inform Succ. BLEU Comb. Inform Succ. BLEU Comb.
    - Table 3: Low-resource evaluation on MultiWOZ 2.0, where Succ. and Comb. denote the Success and Combined
  - Page 6:
    - Table 5: Low-resource DST Evaluation: The means
    - Table 4: DST results. †: the models require a full pre-
    - settings. Furthermore, with 20% of training data, Table 5 shows the experimental results. As seen,
    - trained with full dataset as reported in Table 2. only 1% of training data, PPTOD surpasses the

## [[101-tomar-2024-action-and-reaction-go-hand-in-hand-a-multi-modal-dialogue-act-aided-sarcasm-identification|Tomar 等 - 2024 - Action and Reaction Go Hand in Hand! a Multi-modal Dialogue Act Aided Sarcasm Identification]]

- Source PDF: `raw/sources/Tomar 等 - 2024 - Action and Reaction Go Hand in Hand! a Multi-modal Dialogue Act Aided Sarcasm Identification.pdf`
- Likely table/result pages:
  - Page 4:
    - Table 1: Distribution of dialogue acts and sarcasm of 16kHz. For sampling audio files, we use Librosa
  - Page 6:
    - sentation Cˆ t−m1−m2 is sent to the above layers for We use accuracy, weighted F1-score, precision,
    - further processing. and recall measures to evaluate the performance of
    - cess (explained above) of modality encoding and several baselines and state-of-the-art (SOTA) mod-
    - Role of Aided Classification. Table 2 presents
  - Page 7:
    - Accuracy Precision Recall F1-Score Accuracy Precision Recall F1-Score
    - Table 2: Results of all the baselines and MM-SARDAC for sarcasm detection in standalone and dialogue
    - Table 3: Results of all the baselines and MM-SARDAC for DAC in standalone and sarcasm aided settings
    - Audio Video Model Acc Precision Recall F1 Model Acc. Prec. Recall F1
  - Page 8:
    - MM-SARDAC surpasses all the SOTA approaches,
    - Table 2), the best results were obtained when the
    - modalities were fused in text –> audio –> visual We also analyze the case in Table 2 where we
    - and +6.67% in terms of accuracy and F1-score, when aided by dialogue act (see Bimodal row). In
  - Page 11:
    - Language Processing (Volume 1: Long Papers), ers: State-of-the-art natural language process-

## [[113-wu-incorporating-instructional-prompts-into-a-unified-generative-framework-for-joint-multiple-intent-de|Wu 等 - Incorporating Instructional Prompts into a Unified Generative Framework for Joint Multiple Intent De]]

- Source PDF: `raw/sources/Wu 等 - Incorporating Instructional Prompts into a Unified Generative Framework for Joint Multiple Intent De.pdf`
- Likely table/result pages:
  - Page 1:
    - achieves new SOTA performances on full-data
  - Page 2:
    - achieves new SOTA performances. Remarkably,
  - Page 4:
    - their names. Turning to intent accuracy, UGEN
    - exceeds SDJN (the previous SOTA) by 0.4% and
    - Graph-Interactive Framework for joint multiple in- Table 2 reports the results in the setting of 5/10-
    - points in slot F1, but it leads to 28.1, 23.0, and 5.1
  - Page 5:
    - S-F1 I-Acc O-Acc S-F1 I-Acc O-Acc S-F1 I-Acc O-Acc
    - Table 2: Results on the MixSNIPS set in the few shot settings. Because Joint Multiple ID-SF (JM) and SDJN are not
    - publicly available, we can only compare the other baselines. S-F1, I-Acc,O-Acc refer to the slot F1, intent-accuracy,
    - and overall accuracy (both intents and slots need to be right), respectively.

## [[114-xing-2024-dc-instruct-an-effective-framework-for-generative-multi-intent-spoken-language-understanding|Xing 等 - 2024 - DC-Instruct An Effective Framework for Generative Multi-intent Spoken Language Understanding]]

- Source PDF: `raw/sources/Xing 等 - 2024 - DC-Instruct An Effective Framework for Generative Multi-intent Spoken Language Understanding.pdf`
- Likely table/result pages:
  - Page 1:
    - els and state-of-the-art methods, demonstrat-
  - Page 2:
    - Determination Intent 7 over state-of-the-art models. The ablation study
  - Page 4:
    - examples of detailed instructions in Appendix (Table 5 and Table 6).
  - Page 6:
    - Overall(Acc) Slot (F1) Intent(Acc) Overall(Acc) Slot(F1) Intent(Acc)
    - Table 1: Results comparison. denotes we implement the model using the official code. denotes DC-Instruct
    - models significantly outperform UGEN counterparts (p < 0.01 under t-test). TP denotes the trainable parameter size.
    - our model and baselines are shown in Table 1, from (3) ChatGPT can hardly handle multi-intent SLU,
  - Page 7:
    - (Acc) (F1) (Acc) (Acc) (F1) (Acc) (Acc) (F1) (Acc) (Acc) (F1) (Acc)
    - Table 2: Experiment results on different low-resource settings. TSN denotes the number of training samples.
    - MixATIS MixSNIPS decreases not only in slot F1 but also in intent ac-
    - curacy and overall accuracy. This can be attributed
  - Page 8:
    - model over the state-of-the-art generative model
    - In case A, UGEN cannot identify ‘ground (LLama2-7B). The results are listed in Table 4.
    - correctly predict because the subtle semantics dif- ChatGPT in Appendix (Table 7).

## [[115-xing-tsang-2022-co-guiding-net-achieving-mutual-guidances-between-multiple-intent-detection-and-slot-filling-via-he|Xing和Tsang - 2022 - Co-guiding Net Achieving Mutual Guidances between Multiple Intent Detection and Slot Filling via He]]

- Source PDF: `raw/sources/Xing和Tsang - 2022 - Co-guiding Net Achieving Mutual Guidances between Multiple Intent Detection and Slot Filling via He.pdf`
- Likely table/result pages:
  - Page 1:
    - ing state-of-the-art results and significant speedup.
  - Page 4:
    - Hetegeneous Graph State-of-the-art models (Qin et al., 2020, 2021b)
  - Page 5:
    - works, we adopt accuracy (Acc) for multiple intent
    - detection, F1 score for slot filling, and overall accu-
    - Loss Function The loss function for multiple Overall accuracy denotes the ratio of sentences
  - Page 6:
    - Overall(Acc) Slot (F1) Intent(Acc) Overall(Acc) Slot(F1) Intent(Acc)
    - Table 1: Results comparison. denotes our model significantly outperforms baselines with p < 0.01 under t-test.
    - source code will be released. (3) The improvements in overall accuracy are
    - and baselines are shown in Table 1, from which we other using their initial predictions. For each task,
  - Page 7:
    - Overall(Acc) Slot (F1) Intent(Acc) Overall(Acc) Slot(F1) Intent(Acc)
    - Table 2: Results of ablation experiments.
    - and its result is shown in Table 2. We can find that lem (e.g., B-singer followed by I-song) (Wu et al.,
    - on Overall Acc, proving that both of the intent-to- improves the slot filling performance by modeling
  - Page 11:
    - ers: State-of-the-art natural language processing. In
    - aspect-level sentiment classification. arXiv preprint Table 3 shows the result comparison of Co-
    - Bowen Xing and Ivor Tsang. 2022c. Neural subgraph their state-of-the-art counterparts: AGIF, GL-GIN,
    - further boosted, achieving new state-of-the-art.

## [[002-2025-acl-long-102|2025.acl-long.102]]

- Source PDF: `raw/sources/2025.acl-long.102.pdf`
- Likely table/result pages:
  - Page 1:
    - weighted F1-score and accuracy, demonstrating emotional causes. As noted in (Poria et al., 2021),
  - Page 2:
    - considers the four types of causes. ECERC utilizes of weighted F1-score and Accuracy metrics. These
  - Page 6:
    - where W e R 4Kd × C , b e , i,j R C , c Table 1: Statistics of the datasets.
  - Page 7:
    - Table 2: Comparison of our approach against MMERC baselines on the IEMOCAP dataset. F1.=F1-score. Acc.=
    - Happy Sad Neutral Angry Excited Frustrated F1. Acc.
    - Table 3: Comparison of our approach against MMERC baselines on the MELD dataset. F1.=F1-score. Acc.=
    - Neutral Surprise Fear Sad Joy Disgust Angry F1. Acc.
  - Page 8:
    - ence capabilities. This could be attributed to its Table 4: Impact of core components on models’ perfor-
    - experimental results are shown in Table 4. Regard-
    - Table 5: Impact of modalities on models’ performance.
    - are ignored, lowering the accuracy of emotion in-
  - Page 9:
    - issues continue to pose challenges to the accuracy national Joint Conference on Natural Language Pro-

## [[005-2025-coling-main-18|2025.coling-main.18]]

- Source PDF: `raw/sources/2025.coling-main.18.pdf`
- Likely table/result pages:
  - Page 6:
    - Happy Sad Neutral Angry Excited Frustrated W-F1 Neutral Surprise Fear Sadness Joy Disgust Anger W-F1
    - Table 1: Comparison with other baselines on the IEMOCAP and MELD dataset.
    - We report the F1 and the weighted F1 (W-F1).
    - As shown in Table 1, the experimental results show
  - Page 7:
    - has better W-F1 scores than other methods on the three categories of emotions "happy", "neutral" and
    - model also achieves the best W-F1 scores on the
    - experiment, the emotion recognition accuracy of
    - 0.8 0.8 W-F1 0. 0 5 . 0 6 .7 Sad W-F1 0. 0 4 . 0 5 . 0 6 .7 Surprise

## [[007-2507-09076v2|2507.09076v2]]

- Source PDF: `raw/sources/2507.09076v2.pdf`
- Likely table/result pages:
  - Page 2:
    - Comparative experiments show that our DPM-enhanced method achieves state-of-the-art (SOTA)
  - Page 3:
    - that our DPM-enhanced SLLM achieves new state-of-the-art results on both benchmarks.
  - Page 8:
    - Table 1: Ablation study on IEMOCAP and MELD. We compare our full model (SLLM-DPM)
    - To establish a strong baseline and isolate the gains from our SLLM’s autoregressive structure, we
    - compared our model against a traditional classifier-based approach. This baseline model processes
    - baseline used 1e-4. For our DPM inference, the temporary LoRA module was updated with a learn-
  - Page 9:
    - Table 2: Comparison with recent models for ERC on IEMOCAP and MELD datasets. The best
    - We compared our model with recent models for ERC in Table 2. To ensure fairness, all compared
    - method achieved SOTA results on both the IEMOCAP and MELD datasets. This demonstrates the
  - Page 12:
    - Table 3: Impact of DPM stepping strategies on performance on the MELD dataset.
    - The results, presented in Table 3, reveal several key insights. Firstly, the sentence-by-sentence strat-
    - choose a strategy that balances the need for accuracy with computational constraints.
  - Page 13:
    - Table 4: Performance comparison between models with different context window lengths on the
    - As shown in Table 4, when using autoregressive methods for one-time emotion inference, the 4k

## [[033-fu-2025-laerc-s-improving-llm-based-emotion-recognition-in-conversation-with-speaker-characteristics|Fu 等 - 2025 - LaERC-S Improving LLM-based Emotion Recognition in Conversation with Speaker Characteristics]]

- Source PDF: `raw/sources/Fu 等 - 2025 - LaERC-S Improving LLM-based Emotion Recognition in Conversation with Speaker Characteristics.pdf`
- Likely table/result pages:
  - Page 2:
    - ration of speaker characteristics can bring superior LaERC-S over the state-of-the-art methods.
  - Page 5:
    - Table 1: Performance comparison between our pro-
    - sults are bolded. Our evaluation metric is weighted-F1.
    - BiosERC (Xue et al., 2024). of our proposed method and other baseline methods
    - in Table 1, where ‘Avg.’ denote the overall average
  - Page 6:
    - Table 2: Performance comparison by speaker charac-
    - Table 3: Analysis of different elements in the initial
    - The experimental results are presented in Table 2, To investigate the influence of different key ele-
    - relevant experiments in Table 2, where the first Table 3 shows the results, from which we can
  - Page 7:
    - Baseline 69.95 68.86 40.87 59.89 Characteristics Generation
    - Table 5. We randomly sampled 100 samples from
    - Table 4: Performance of LaERC-S with different large
    - Table 5: Performance of LaERC-S with different tem- 4 is removed in template 2, leading to a 0.97% drop
  - Page 8:
    - average of the differences between ‘Single’ W-F1 and ‘Ratio mix’ W-F1.
  - Page 12:
    - Number IEMOCAP MELD EmoryNLP Final Emotion tee clarity and accuracy in each stage.
    - 5 excited - - excited In the different template design shown as Table 10,
    - in Table 7. We can notice that LaERC-S achieves listeners" word can better extract accurate speaker
    - reference, in the first row of the table, LaERC- performance

## [[064-li-2024-multimodal-emotion-cause-pair-extraction-with-holistic-interaction-and-label-constraint|Li 等 - 2024 - Multimodal Emotion-Cause Pair Extraction with Holistic Interaction and Label Constraint]]

- Source PDF: `raw/sources/Li 等 - 2024 - Multimodal Emotion-Cause Pair Extraction with Holistic Interaction and Label Constraint.pdf`
- Likely table/result pages:
  - Page 1:
    - results demonstrate the superior performance of HiLo, evidenced by an increase of more than 2% in the F1 score compared to
  - Page 2:
    - improving the precision of emotion-cause pair extraction.
  - Page 3:
    - across all three tasks, achieving a notable improvement of more than 2% in the F1 score for the ECPE task. Further
  - Page 9:
    - Table 1. Dataset statistics for train, dev, test set, and all set, respectively.
    - utterances. The detailed statistics for the dataset can be found in Table 1.
    - extraction using precision (P) , recall (R), and F1 score (F1). These metrics are specifically defined for each evaluated
  - Page 10:
    - For emotion detection, we apply these metrics to assess the accuracy of identified non-neutral emotions:
    - labels. To provide a more nuanced assessment, we also implement category-level precision, recall, and F1 score
  - Page 12:
    - Table 2. Experiment results on the MECPE task. We present Precision/Recall/F1 scores for emotion detection, cause detection,
    - and ECPE. We do not distinguish the emotion category in this table, and scores with wavelines denote the second-best
    - Table 3. Ablation study conducted on holistic interaction, label constraint strategy, and RoPE encoding. We provide the
    - precision, recall, and F1 scores for emotion-cause pairs, as well as the weighted average score across different emotion

## [[088-qiu-2025-detecting-emotional-incongruity-of-sarcasm-by-commonsense-reasoning|Qiu 等 - 2025 - Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning]]

- Source PDF: `raw/sources/Qiu 等 - 2025 - Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning.pdf`
- Likely table/result pages:
  - Page 4:
    - Table 1: Statistics of datasets. #Avg.Len denotes the
  - Page 5:
    - The statistics of datasets are shown in Table 1.
  - Page 6:
    - Acc Ma-F1 Acc Ma-F1 Acc Ma-F1 Acc Ma-F1 Acc Ma-F1
    - Table 2: Performance comparison of different methods on datasets. Acc denotes Accuracy and Ma-F1 denotes
    - Macro-F1. The best results are represented in bold. The second-best results are underlined.
    - Table 3: Performance comparison of LLMs of different scales (without fine-tune) as the generative model on
  - Page 8:
    - Figure 5: Low-resource performance on four benchmark datasets. The left axis represents the accuracy, while the
    - right axis illustrates our improvement over the baseline.
    - ure 4a showed that performance initially improved Cue (Yao et al., 2024) as the baseline. The observed
    - and GPT-4o. As presented in Table 3, the results the sarcastic intent in Hillary’s statement, as shown

## [[094-shen-2025-coe-a-clue-of-emotion-framework-for-emotion-recognition-in-conversations|Shen 等 - 2025 - CoE A Clue of Emotion Framework for Emotion Recognition in Conversations]]

- Source PDF: `raw/sources/Shen 等 - 2025 - CoE A Clue of Emotion Framework for Emotion Recognition in Conversations.pdf`
- Likely table/result pages:
  - Page 2:
    - implications for the broader field of computational ing state-of-the-art zero-shot results on multiple
  - Page 5:
    - 4o’s relatively low accuracy results in a higher pro-
    - more correct rationales, its reasoning accuracy im-
  - Page 6:
    - ing FP16 precision for training. The final results
    - used weighted F1 (W-F1) as the evaluation metric, bedding them explicitly within the task itself. Ad-
    - splits with both InstructERC (Lei et al., 2023) and Our results (Table 1) show that CoE outper-
  - Page 7:
    - R1 show limited performance in zero-shot ERC. results are summarized in Table 2, from which we
    - CoE achieved the highest average W-F1 score (+ can conclude that the study highlights the signifi-
    - task through the multi-stage auxiliary learning strat- the accuracy of the ERC task.
    - Table 2: Ablation Study on Textual Clues
  - Page 8:
    - Table 3: Performance Improvement of the Main Task
    - W-F1 W-F1 1. Curriculum-based Sequential Training
    - effectiveness of mixed auxiliary training and cur- The results in Table 4 of this small-scale ex-
    - a subset of the dataset to assess the effectiveness Table 4: Ablation Study on Different Strategies
  - Page 9:
    - Table 5: Comparison of CoE Strategies A and B
    - enhancing the model’s grasp of speaker identities, gies, achieving state-of-the-art performance on the
    - egy B. As shown in Table 5, the results indicate identities needed for speaker identification tasks,

## [[134-yuan-2025-reflectdiffu-reflect-between-emotion-intent-contagion-and-mimicry-for-empathetic-response-generatio|Yuan 等 - 2025 - ReflectDiffu Reflect between Emotion-intent Contagion and Mimicry for Empathetic Response Generatio]]

- Source PDF: `raw/sources/Yuan 等 - 2025 - ReflectDiffu Reflect between Emotion-intent Contagion and Mimicry for Empathetic Response Generatio.pdf`
- Likely table/result pages:
  - Page 5:
    - emotion recognition. To enhance the accuracy of ∈ − −
    - value of n is 3 as shown in Table 1. We provide an (8)
    - surprised, proud, impressed, acknowledging, from a predetermined set of intent refer (Table 1),
    - Table 1: Mapping of Emotion-Group to Top-3 Universal Twice
  - Page 6:
    - twice klpos klneg intent both classic and recent state-of-the-art (SOTA)
    - mativeness, including BLEU-n, BART , Emo-
  - Page 7:
    - B-1 ↑ B-2 ↑ B-3 ↑ B-4 ↑ BART Score ↑ Acc emo ↑ Acc Intent ↑ PPL ↓ D-1 ↑ D-2 ↑
    - Table 2: Results of automatic evaluations and ablation study. Metrics include BLEU-1 to BLEU-4 (B-1 B-4),
    - BARTScore for Relevance; emotion and intent accuracy (Acc , Acc ) for Controllability; perplexity (PPL) and
    - tion Accuracy Acc , Intent Accuracy Acc , ilarity and coherence with the empathetic ground
  - Page 8:
    - fewshots (a SOTA LLM-based empathetic Sampling-Correcting mechanism; and (4) w/o
    - Acc , Acc , Distinct-1 and Distinct-2.Higher
    - icant decrease in BLEU-n, BART and Acc ,
    - Human Evaluation Results Table 3 presents the
  - Page 9:
    - Table 4: Case study comparison between ReflectDiffu following our instructions (refer to Appendix D).
  - Page 11:
    - limitations, and recommendations. arXiv preprint Jing Zhu. 2002. Bleu: a method for automatic evalu-

## [[031-elsherief-2021-latent-hatred-a-benchmark-for-understanding-implicit-hate-speech|ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech]]

- Source PDF: `raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf`
- Likely table/result pages:
  - Page 2:
    - we train competitive baseline classifiers to detect cations. However, we are the first to take this frame-
    - ments. While state-of-the-art neural models are and extend it to implicit hate speech more broadly.
    - marize them in Table 1. The majority are skewed
  - Page 3:
    - Table 1: Summary of English hate speech datasets in terms of Domain / Scope, Size, hate class Balance ratio, the
  - Page 5:
    - Table 2: Implicit hate category label distribution before
  - Page 6:
    - Table 3: Classification performance metrics averaged over five random seeds. (Left) Binary Classification. Perfor-
    - dimensional ConceptNet) embeddings, and fed this fine-tuned baselines significantly outperform both
    - left side of Table 3, baseline SVM models offer negative errors from our best model in the binary
    - significantly better macro precision than the lin- as #WPWW (white pride world wide), #National-
  - Page 7:
    - Models BLEU BLEU∗ Rouge-L Rouge-L∗ BLEU BLEU∗ Rouge-L Rouge-L∗
    - Table 4: Evaluation of the generation models for Target Group and Implied Statement. (*) denotes the maximum
    - lenge current state-of-the-art baselines, which can [Gi] [Si]
  - Page 8:
    - Table 5: Example posts from our dataset along with their implicit category labels, the GPT-2 generated target and
    - notations belongs only to one split. our domain. The BLEU and ROUGE-L scores
    - Following recent work on social bias inference are higher for the target group (e.g., 83.9 BLEU)
    - and commonsense reasoning (Sap et al., 2020; than for the implied statement (e.g., 75.3 BLEU),

## [[043-hartvigsen-2022-toxigen-a-large-scale-machine-generated-dataset-for-adversarial-and-implicit-hate-speech-detection|Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection]]

- Source PDF: `raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf`
- Likely table/result pages:
  - Page 2:
    - slurs, or swearwords (Table 1). fine-tuning existing classifiers on TOXIGEN con-
  - Page 3:
    - Table 1: Comparing toxic language datasets. % Hate Class is the percent labeled as hate (according to prompts for
    - start blocking most language referencing minority tences for 13 identity groups—see Table 2.
    - Table 1, existing datasets contain large amounts name and (2) contain mainly implicit language,
  - Page 5:
    - Table 2: Statistics for TOXIGEN across all groups. Avg. • False positives: We use benign prompts to en-
  - Page 6:
    - Statistics of TOXIGEN are presented in Table 2.
  - Page 7:
    - Table 3: Example responses from human evaluation where machine-generated text fools annotators into thinking
    - the y-axis gives the percentage of examples per anno- example—see Table 3—human annotators often
  - Page 8:
    - Table 4: AUC for HateBert and RoBERTa both zero-
    - Our results—see Table 4—show that fine-tuning

## [[058-kim-2022-generalizable-implicit-hate-speech-detection-using-contrastive-learning|Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning]]

- Source PDF: `raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf`
- Likely table/result pages:
  - Page 1:
    - pirically confirm that the performance drops at Table 1: Example input texts and labels (Hate / Not
    - least 12.5%p in F1 score when tested on the Hate) from IMPLICIT HATE CORPUS (IHC) (ElSherief
    - sexual orientation, nationality, religion, or other See Table 1 for examples of implicit hate speech.
  - Page 2:
    - outperform other baselines in terms of in-dataset Train IHC SBIC DYNAHATE
    - of a model (Wiegand et al., 2019). As a preliminary Table 2: Cross-dataset and in-dataset evaluation results
    - tion for the current state-of-the-art models trained dicates the dataset used for training, while the row on
  - Page 3:
    - issue. As shown in Table 2, the performance of yˆ indicates the model predicted probability of i-
    - both models drops consistently over 12.5%p in F1 th input x and y is the ground-truth label of x ,
  - Page 5:
    - tion or augmented version of IM P (x )). In detail, We experimented with three baseline training ap-
  - Page 6:
    - Table 3: Cross-dataset and in-dataset evaluation results for the models trained on IHC dataset. We use → to
    - Table 4: Cross-dataset and in-dataset evaluation results for the models trained on SBIC dataset. Boldfaced values
    - ants) has shown state-of-the-art performance in
    - pushed apart in the representation space 3. choose the best model with validation F1 score. We
  - Page 7:
    - Adding AugCon on BERT increases the perfor- Table 5: Quantitative analysis on the representation
    - ImpCon consistently outperform the models trained
    - IHC validation set. As shown in Table 5, two train-

## [[095-sheth-2024-causality-guided-disentanglement-for-cross-platform-hate-speech-detection|Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection]]

- Source PDF: `raw/sources/Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection.pdf`
- Likely table/result pages:
  - Page 2:
    - enhanced efficacy compared to existing state-of-the-art methods in and hate crimes [1, 41]. Thus, given the heinous effects and the
  - Page 3:
    - hinders the performance of the existing models is the over-reliance challenges posed by existing state-of-the-art models that strive
    - state-of-the-art models overly rely on identity words (e.g., "jews") limitations. A prevalent and proven technique for constructing a
  - Page 4:
    - CATCH outperforms the state-of-the-art baselines. using data from their social context and their profiles. However,
    - current state-of-the-art (SOTA) models trained on specific topics
  - Page 7:
    - Table 1: Cross-platform and in-dataset evaluation results for the different baseline models compared against CATCH. Boldfaced values denote
    - aid in learning invariant causal representations that can improve A summary of the datasets can be found in Table 2. We use macro
    - the generalizability of hate speech detection? F1-measure for validation.
    - Table 2: Dataset statistics with corresponding platforms and
  - Page 8:
    - compared using the macro-F1 measure as a benchmark in Table 1. 0 0
    - • The EasyMix baseline encounters challenges in generalizing in
    - top three baseline models, and the results are illustrated in Figure 4.
    - • The baseline based on linguistic features (POS + EMO) doesn’t
  - Page 9:
    - 0.6 0.58 0.6 0.6 0.7 0.74 and Falcon [32], as shown in Table 3. We give the following prompt
    - Figure 5: Macro-F1 score reflecting the importance of each tial, they may fall short in nuanced tasks like hate speech detection.
    - Table 3: Performance comparison of LLMs, GPT4 and Falcon,

## [[046-hee-2024-bridging-modalities-enhancing-cross-modality-hate-speech-detection-with-few-shot-in-context-learnin|Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin]]

- Source PDF: `raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf`
- Likely table/result pages:
  - Page 1:
    - tion accuracy of vision-language hate speech. improving performance in low-resource settings.
    - Motivation. Hate speech in the online space ap- the classification accuracy of vision-language hate
    - and vision-language memes. Recent hate speech strations in few-shot learning contexts outperform
  - Page 2:
    - Table 1: Statistical distributions of datasets, where "H"
  - Page 3:
    - Model # Shots Dem. Samp. Matching Acc. F1 # Invalids Acc. F1 # Invalids
    - Table 2: Comparison of zero-shot and few-shot in-context learning with Latent Hatred support set across different
    - elements, focusing on target groups, imagery, and generated rationale. Table 2 shows the compari-
  - Page 4:
    - Model # Shots Dem. Samp. Matching Acc. F1 # Invalids Acc. F1 # Invalids
    - Table 3: Comparison of zero-shot and few-shot in-context learning experiment results with FHM support set across
    - two datasets in terms of F1 score. Secondly, the achieves an F1 score improvement of 0.64 and 1.23
    - Table 3 shows the comparison of zero-shot and few-
  - Page 5:
    - accuracy of vision-language hate speech, and using
  - Page 7:
    - from prejudice and discrimination based on race, bles, such as the highest accuracy and F1 scores

## [[080-mei-2024-improving-hateful-meme-detection-through-retrieval-guided-contrastive-learning|Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning]]

- Source PDF: `raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf`
- Likely table/result pages:
  - Page 1:
    - with an AUROC of 87.0, outperforming much challenge in classifying "confounder memes", in
    - tribute to their hateful nature. Even state-of-the-art
  - Page 2:
    - mance than state-of-the-art large multimodal sys- latency (Kim et al., 2021).
    - AUC and accuracy using the KNN majority voting this paper, we show that such CLIP-based models
    - Flamingo 80B achieves a state-of-the-art AUROC
  - Page 5:
    - 4.1 Comparing RGCL with baseline systems HatefulMemes HarMeme
    - Table 1 presents the experimental results with lo-
    - of baseline models including OD-based models,
    - fulMemes dataset, RGCL obtains an AUC of
  - Page 6:
    - Model AUC Acc. AUC and 78.3% accuracy. These scores also
    - surpass all baseline systems including fine-tuned
    - fine-tuned on HarMeme 56.3 54.3 In Table 3, we report a comparative analysis by
    - Table 2: Retrieval-based KNN classifier results on Hate-
  - Page 7:
    - ALIGN3 (Jia et al., 2021). As shown in Table 4, is included. For simplicity, we maintain a 1:1 mix-
    - RGCL enhances the AUC score by a margin of ing ratio. Notably, in the absence of cross-entropy
    - 4.4% over the baseline ALIGN model. loss, we identified several examples where models
    - Model AUC Acc. ceed. Conversely, inclusion of cross-entropy loss
  - Page 8:
    - shows improvement over baseline across all four 6 Conclusion
    - of more than 3% on both accuracy and F1 scores.
    - contextual understanding. Achieving an AUC score
    - tem outperforms prior state-of-the-art models. Our

## [[056-jiang-2025-learn-from-failure-causality-guided-contrastive-learning-for-generalizable-implicit-hate-speech-det|Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det]]

- Source PDF: `raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf`
- Likely table/result pages:
  - Page 1:
    - state-of-the-art methods in cross-domain gener-
  - Page 2:
    - state-of-the-art performance on three widely-
  - Page 3:
    - still encounter challenges in both accuracy and effi- distinguishing between the anchor and hard nega-
  - Page 5:
    - Table 2: Cross-dataset and in-dataset evaluation results for different training objectives trained on IHC dataset.
    - ble 1. We use the macro F1-score measure for
  - Page 6:
    - Table 3: Cross-dataset and in-dataset evaluation results for different training objectives trained on SBIC dataset.
    - with macro F1-score in the validation set and report plored three augmentation methods: implication
    - the macro F1-score on the test set. and synonym substitution (Kim et al., 2022), as
    - Table 2 and Table 3 present the evaluation results data augmentation, incorporating external knowl-
  - Page 7:
    - this experiment to three baseline models: SCL, Im- hate speech compared to the other three models.

## [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection|Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection]]

- Source PDF: `raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf`
- Likely table/result pages:
  - Page 2:
    - classification, achieving new state-of-the-art
    - demonstrates state-of-the-art performance for
  - Page 5:
    - 4 Experiments As shown in Table 1, RGCL (#3) achieves the high-
    - 4.1 Comparing RA-HMD to Baseline Systems
    - Table 1 presents the performance of baseline sys-
    - where few-shot systems consistently outperform
  - Page 6:
    - Model AUC Acc. AUC Acc. AUC Acc. Acc. F1 Acc. F1 Acc. F1
    - Table 1: Comparison with baseline systems under supervised settings. For large multimodal models, we report the
    - is deployed to evaluate trending memes. Few-shot 7B zero-shot (#11 in Table 2) matches its SFT
    - and RKC examples are drawn from the training model performance (#13 in Table 1) on Hateful-
  - Page 7:
    - Model AUC Acc. AUC Acc. AUC Acc. Acc. F1 Acc. F1 Acc. F1
    - Table 2: Comparing out-of-domain meme classification performance under low-resource settings. For systems
    - with RKC inference mode outperforms baseline agent-based framework. Furthermore, our method
    - methods outperforms LOREHM by 8.2% in accuracy on
  - Page 8:
    - Table 4: Comparison of the pretrained, SFT, and RA-
    - In Appendix H, we also conduct ablation stud- Baseline (From Table 1)
    - Mode AUC Acc. AUC Acc. RA-HMD + LRC 84.4 (-6.7) 75.5 (-6.6)
    - w/ Combined 88.9 77.8 90.2 83.4 Table 5: Comparison of the SFT and RA-HMD Qwen2-
  - Page 9:
    - Generalization Across Model Variants scale of 0–10), the SFT baseline achieved an aver-
    - Table 2. Our results show that RA-HMD consis- nations, we find that improvements in classifica-
    - tently outperforms both baselines under both the tion accuracy are supported by a deeper semantic
    - els (Table 1 rows 15 and 16) on the validation set of work for LMMs tailored for hateful meme classi-

## [[121-yang-2024-uncertainty-aware-cross-modal-alignment-for-hate-speech-detection|Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection]]

- Source PDF: `raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf`
- Likely table/result pages:
  - Page 7:
    - PromptHate 72.98 81.45 Table 3: Performance comparison on the Harm-P.
    - UCA (Ours) 76.10 84.32 Models F1 ↑ Pre. ↑ Rec. ↑
    - Table 1: Performance comparison on the Hate. CNNText+VGG16 46.30 37.30 61.10
    - Acc. ↑ F1 ↑ MMAE ↓ UCA (Ours) 65.89 66.09 66.90
  - Page 8:
    - Acc. ↑ AUROC ↑ Acc. ↑ F1 ↑ MMAE ↓ Acc. ↑ F1 ↑ MMAE ↓ F1 ↑ Pre. ↑ Rec. ↑ F1 ↑ Pre. ↑ Rec. ↑ Acc. ↑
    - Table 6: Ablation study evaluated on the Hate, Harm-C, Harm-P, Offense and Sarcasm datasets.
    - features into the classifier as a baseline. Compared between the fun in the text and the crazy move-
  - Page 10:
    - Niklas Muennighoff. 2020. Vilio: state-of-the-art

## [[136-zhang-2023-tot-topology-aware-optimal-transport-for-multimodal-hate-detection|Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection]]

- Source PDF: `raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - ing. The newly achieved state-of-the-art performance
  - Page 2:
    - state-of-the-art performance by a large margin on two
  - Page 4:
    - TOT against other state-of-the-art unimodal and multimodal
    - reasoning, the current node xn is replaced with xn+1. When the two benchmarks are displayed in Table 1. To make a fair
    - ∈ Rdh. Accuracy (Acc), Macro-F1 (F1), and Macro-Averaged Mean
    - Table 1: Statistics of Harm-C and Harm-P dataset.
  - Page 5:
    - Acc F1 MMAE Acc F1 MMAE Acc F1 MMAE Acc F1 MMAE
    - Table 2: Overall performance of proposed TOT model against a set of baselines. For Acc (↑) and F1 (↑), the larger values are
    - 2-class Detection Results The left part of Table 2 reports
  - Page 6:
    - 3.13% absolute points of M-F1 improvement on Harm-C score. We also report different training strategies for these
    - and 3.02% points on Harm-P. The other two metrics of Acc two modules: joint learning and independent learning, which
    - demonstrating the effectiveness of our method. learning. The ablation results are shown in Table 4. We
    - score (1.57% points in Acc and 1.45% points in M-F1 for
  - Page 7:
    - herding. Note that Wilson is the name of the dog. However, ments have shown that TOT outperforms the state-of-the-art

## [[017-behnamghader-2024-llm2vec-large-language-models-are-secretly-powerful-text-encoders|BehnamGhader 等 - 2024 - LLM2Vec Large Language Models Are Secretly Powerful Text Encoders]]

- Source PDF: `raw/sources/BehnamGhader 等 - 2024 - LLM2Vec Large Language Models Are Secretly Powerful Text Encoders.pdf`
- Likely table/result pages:
  - Page 1:
    - Large decoder-only language models (LLMs) are the state-of-the-art models
    - tasks. We outperform encoder-only models by a large margin on word-level
    - tasks and reach a new unsupervised state-of-the-art performance on the
    - LLM2Vec with supervised contrastive learning, we achieve state-of-the-art
  - Page 2:
    - recognition, and part-of-speech tagging), LLM2Vec-transformed models outperform strong
    - LLM2Vec-transformed models set a new state-of-the-art for unsupervised models, with our
    - contrastive training and achieve a new state-of-the-art performance among models that
  - Page 4:
    - transformed models to DeBERTa-v3-large (He et al., 2023), the current state-of-the-art
    - is provided in Table 4). On each of the three tasks, constructing token representations with
    - causal attention (Uni) already outperforms the encoder-only baseline. This is not surprising,
  - Page 5:
    - instructions are only added to queries and can be found in Table 10 of Appendix C.2. For
    - As a baseline, we compare to the unsupervised BERT models obtained from Gao et al. (2021).
    - best causal baseline on the MTEB subset. We further conduct an ablation of each component
    - of LLM2Vec recipe in Appendix D.2.2 (Table 5).
  - Page 6:
    - Table 1: Unsupervised results on MTEB. We compare S-LLaMA-1.3B, LLaMA-2-7B,
    - further boosts all three models by a large margin, making our LLM2Vec Mistral-7B SOTA
    - performance, but does not outperform LLM2Vec applied to Mistral-7B.
    - into strong text embedding models which outperform previous unsupervised approaches
  - Page 8:
    - Table 2: Supervised results on full MTEB benchmark. The best performing LLM2Vec model
    - Meta-LLaMA-3-8B + LLM2Vec (w/o SimCSE) achieves a new SOTA performance among
    - Results Table 2 shows the results of our evaluation. For all models, transforming a
    - baseline. As expected, performing unsupervised SimCSE is less crucial for supervised

## [[024-cocchieri-2025-what-do-you-call-a-dog-that-is-incontrovertibly-true-dogma-testing-llm-generalization-through-hu|Cocchieri 等 - 2025 - “What do you call a dog that is incontrovertibly true Dogma” Testing LLM Generalization through Hu]]

- Source PDF: `raw/sources/Cocchieri 等 - 2025 - “What do you call a dog that is incontrovertibly true Dogma” Testing LLM Generalization through Hu.pdf`
- Likely table/result pages:
  - Page 1:
    - performing the human baseline. Additionally,
  - Page 5:
    - employed the vLLM library. For 70B-parameter herent Pun Accuracy (CPA) and Misleading Pun
    - models, AWQ quantization was applied to opti- Accuracy (MPA), measuring performance on co-
    - We evaluate 9 state-of-the-art LLMs, categorized approach proved robust, with fewer than 1% of
    - protocol combining automatic evaluation with hu- We use three key metrics: Accuracy (ACC),
  - Page 6:
    - Models CPA MPA− MPA+ MPA Models ACC VPA EWA
    - Table 1: Model performance on the Comprehension
    - task. Models are ordered based on decreasing CPA. Table 2: Model performance on the Resolution task.
    - Models are ordered based on decreasing Accuracy.
  - Page 7:
    - GPT-4o-mini (cid:63) 41.7 24.0 36.0 84.0 human baseline and subjected them to the same
    - Table 3: Model performance on both Generation
    - 6.3 Can LLMs Generate Puns? accuracy score of 85.7, ranking second only to the
    - Table 3 presents model results. In the Constrained
  - Page 8:
    - ACC VPA EWA ACC VPA EWA ACCC ACCF C¯ ACCC ACCF C¯
    - Table 6. (1) The model fails to use the subject appends a suffix to the subject, producing a se-
  - Page 9:
    - Table 4: Examples of errors in the Pun Comprehension task.

## [[030-dubreuil-2025-are-stereotypes-leading-llms-zero-shot-stance-detection|Dubreuil 等 - 2025 - Are Stereotypes Leading LLMs' Zero-Shot Stance Detection]]

- Source PDF: `raw/sources/Dubreuil 等 - 2025 - Are Stereotypes Leading LLMs' Zero-Shot Stance Detection .pdf`
- Likely table/result pages:
  - Page 1:
    - times outperform traditional NLP model tuning for
  - Page 2:
    - prompting methods, LLMs are able to outperform
  - Page 3:
    - "Okay then, I’m on it!!! And remember readability (or very high complexity, see Table 1
  - Page 4:
    - Table 1: Discretization of Flesch-Kincaid Score
  - Page 5:
    - F1 as a measure of performance for the (binary)
  - Page 6:
    - erty a, knowing that the true label of the text is 1. Table 2: Weighted F1 for each dataset and LLM
    - The weighted F1-score of each model on each
    - dataset can be found in Table 2. To put these results English, AAE for African American English. In green,
    - dataset in the Appendix (F1-score is computed only

## [[041-han-2025-reasoning-with-graphs-structuring-implicit-knowledge-to-enhance-llms-reasoning|Han 等 - 2025 - Reasoning with Graphs Structuring Implicit Knowledge to Enhance LLMs Reasoning]]

- Source PDF: `raw/sources/Han 等 - 2025 - Reasoning with Graphs Structuring Implicit Knowledge to Enhance LLMs Reasoning.pdf`
- Likely table/result pages:
  - Page 5:
    - AIW+ datasets are presented in Table 1, while
    - shown in Table 2. From these results, we can make
    - numbers or options, we use accuracy as the evalua-
    - by-step procedure of RWG is presented in Table 3.
  - Page 6:
    - Table 1: The results on the AIW and AIW+ datasets. Since the AIW+ dataset contains many possible relationships,
    - Table 2: The results on LogiQA and AR-LSAT datasets.
    - second rounds of verification, respectively. In the Table 3: The graph updating procedure of RWG applied
    - The results are shown in Table 4. From these
  - Page 7:
    - Table 4: The results of AIW+ Complete dataset. question by updating the previous graph, inferring
    - (a) GPT-4o (b) Cluade is shown in Table 5. Additionally, we evaluate
  - Page 8:
    - Table 5: Comparison of different models on the Multi-hop Question Answering datasets
    - GPT-4o is as follows in Table 6: - (Jason, parent, Jeff)
    - Table 6: The illustration of Case 1 Based on this graph, we can confirm the relationship between
  - Page 10:
    - in state-of-the-art large language models. arXiv Zhou, Zhongyu Wei, Zhumin Chen, and Nan Duan.
  - Page 12:
    - performance in Table 5 while the detailed results

## [[045-he-crab-a-novel-configurable-role-playing-llm-with-assessing-benchmark|He 等 - Crab A Novel Configurable Role-Playing LLM with Assessing Benchmark]]

- Source PDF: `raw/sources/He 等 - Crab A Novel Configurable Role-Playing LLM with Assessing Benchmark.pdf`
- Likely table/result pages:
  - Page 2:
    - pared to baseline models, RP-LLMs powered
  - Page 3:
    - stage, reference-based metrics, e.g., Rouge and
  - Page 4:
    - Table 1: Statistics for various RP datasets and their associated attributes. Our dataset is the largest since RoleLLM is
    - Table 1 compares our dataset with existing RP cessed into the Dialogue Corpus.
    - alogues and retained the rest. For literary Episodes, and inference. We used various LLMs as baseline
  - Page 5:
    - rics as shown in Table 12. All annotations were compare the proposed RoleRM with widely used
    - open-source software called MAE 2.0 (Rim, 2016) 2023), and GPTScore (Fu et al., 2024). The cal-
  - Page 6:
    - Table 2: The results of evaluation on the test data of our Benchmark. The listed scores are from our RoleRM. Bold
    - reasons (as shown in Table 12 of Appendix). The
    - GPT. We calculate MAE to illustrate the gaps of Human
    - Absolute Error (MAE) scores for RoleRM are
  - Page 7:
    - Table 3: The ablation study for Crab. Due to missing attributes in our dataset, we sampled 1,000 fully attributed
    - Table 4: The comparisons of RoleRM with other eval-
    - data source comes from novel and other public RP pressiveness does not compromise factual accuracy

## [[054-jang-2025-expanding-computation-spaces-of-llms-at-inference-time|Jang 等 - 2025 - Expanding Computation Spaces of LLMs at Inference Time]]

- Source PDF: `raw/sources/Jang 等 - 2025 - Expanding Computation Spaces of LLMs at Inference Time.pdf`
- Likely table/result pages:
  - Page 5:
    - ‘<pad>’ (pad), ‘-’ (dash). Across models, we observe accuracy improvements of up to 12.372
    - substantially higher than the baseline. Qwen2.5-14B-IT model shows far smaller gains compared
  - Page 6:
    - Figure 2: MMLU and ARC accuracy (%) results of four different models. Each model exhibits
    - served that once the number of added tokens surpassed 1024, the accuracy consistently declined to
    - the 20% range across almost all cases, as shown in Table 1 in Appendix A.1.
    - IT model exhibits the opposite trend, with accuracy continuing to improve as the number of tokens
  - Page 7:
    - an initial performance gain, but its accuracy gradually decreases as more tokens are introduced.
  - Page 8:
    - from mid to late Stage 2 does performance approach and slightly exceed the baseline, suggesting
  - Page 13:
    - ger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. Transformers: State-of-the-art
  - Page 14:
    - Table 1: MMLU and ARC accuracy (%) with ‘ ’ (space) tokens added. The numbers highlighted

## [[055-ji-2025-llm-driven-implicit-target-augmentation-and-fine-grained-contextual-modeling-for-zero-shot-and-few-s|Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S]]

- Source PDF: `raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf`
- Likely table/result pages:
  - Page 1:
    - proach achieves state-of-the-art results, con- (Hasan and Ng, 2014; Mohammad et al., 2016;
  - Page 2:
    - cial. However, existing state-of-the-art methods
    - To address the aforementioned issues, we pro- state-of-the-art performance on both ZSSD
  - Page 4:
    - Table 1: Sample Predictions using LLM for Implicit Target Extraction. This table compares the performance of the
    - omitted targets. As demonstrated in Table 1, in a
  - Page 5:
    - mension size. For implementation, sequences are Table 2: Statistics of VAST Dataset.
    - demonstrated in Table 2. Following the previous
    - ∈ average of F1-score is adopted as evaluation metric.
  - Page 6:
    - Table 3: Performance comparison of models on stance detection across zero-shot, few-shot and all settings. ♮
    - our reproduction, ♭ are taken from the original papers and improves the best baseline at p < 0.05 with paired
    - Table 4: Zero-Shot 10% Train. ♮ denotes numbers are
    - in Table 3, our model achieves state-of-the-art per-
  - Page 7:
    - over the state-of-the-art TTS baseline, particularly
    - Table 5: Ablation study of HCTA framework and accurate recognition of neutrality. Furthermore,
    - with HCTA achieves a new state-of-the-art macro-
    - F1 score of 0.801. This results confirm that the

## [[057-jiang-2025-know-me-respond-to-me-benchmarking-llms-for-dynamic-user-profiling-and-personalized-responses-at-s|Jiang 等 - 2025 - Know Me, Respond to Me Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at S]]

- Source PDF: `raw/sources/Jiang 等 - 2025 - Know Me, Respond to Me Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at S.pdf`
- Likely table/result pages:
  - Page 1:
    - o1, or Gemini-2.0 achieving only around 50% overall accuracy, suggest-
  - Page 2:
    - With PERSONAMEM, we evaluate whether state-of-the-art LLMs can infer evolving user
    - settings in user-LLM interactions, we design 7 types of in-situ user queries (Table 1), where
    - around 50% overall accuracy and Llama-4-Maverick slightly lower at 43% using direct
  - Page 3:
    - preference changes (60–70% accuracy), they struggle to incorporate users’ latest situations
    - into responses (30–50% accuracy). We provide detailed analysis on how factors such as
    - PERSONAMEM benchmark. We include examples for each type of user queries in Table 1.
    - 1. Recall user-shared facts. We evaluate whether a personalized chatbot can recall static
  - Page 4:
    - [1] Recall user- ”User: I shared my playlist with my friends and they loved it. ......
    - Table 1: Examples of the 7 types of in-situ user queries and expected chatbot response in the
  - Page 6:
    - leading foundation models, GPT-4.5 and Gemini-1.5 outperform others in overall accu-
  - Page 7:
    - performance when asked to recall how the user preferences evolve over time. We observe

## [[061-lan-2024-llm-based-agent-society-investigation-collaboration-and-confrontation-in-avalon-gameplay|Lan 等 - 2024 - LLM-Based Agent Society Investigation Collaboration and Confrontation in Avalon Gameplay]]

- Source PDF: `raw/sources/Lan 等 - 2024 - LLM-Based Agent Society Investigation Collaboration and Confrontation in Avalon Gameplay.pdf`
- Likely table/result pages:
  - Page 1:
    - box environment. However, prior studies mostly ence learning. We utilize a competitive baseline
  - Page 2:
    - Table 1: Comparison between our work and related works in both agent framework and social behaviour analysis.
    - compared with the baseline method. We also 2023; Qian et al., 2023; Fu et al., 2023).
    - mura et al. (2016) proposes a psychological model thorough behavior analysis. Table 1 illustrates the
  - Page 3:
    - Resistance”, instead of Werewolf as our environ- prompts used are shown in Appendix Table 4. To
  - Page 5:
    - end and the baseline’s. In all experiments, we set
    - generating a response to the host’s inquiry. Agents agents and the baseline agents.
    - for the above steps are shown in Appendix Table 5. culated by dividing total approval votes by total
  - Page 6:
    - picted in Table 2, our method demonstrated a 90%
    - Table 2: Results of the gameplay between ours and
    - baseline. We present the winning rates (WR) of our
    - vote rate when playing evil side. Baseline is worse.
  - Page 7:
    - gameplay towards victory. However, the baseline
    - baseline agents, indicating enhanced persuasion

## [[066-li-2025-how-far-are-llms-from-being-our-digital-twins-a-benchmark-for-persona-based-behavior-chain-simulati|Li 等 - 2025 - How Far are LLMs from Being Our Digital Twins A Benchmark for Persona-Based Behavior Chain Simulati]]

- Source PDF: `raw/sources/Li 等 - 2025 - How Far are LLMs from Being Our Digital Twins A Benchmark for Persona-Based Behavior Chain Simulati.pdf`
- Likely table/result pages:
  - Page 1:
    - state-of-the-art models struggle with accurately
  - Page 2:
    - paradigm shift: these models can synthesize per- state-of-the-art LLMs and performed detailed anal-
    - authorized proxy behaviors on behalf of human 4 achieving sub-60% accuracy. 2) LLMs are less
    - ten state-of-the-art LLMs based on BEHAV-
  - Page 3:
    - knowledge recall (Shen et al., 2024), decision-
    - ence distributions, enabling high-precision election lished character traits, we extracted the main char-
  - Page 6:
    - Table 1: Models performance on BEHAVIORCHAIN, showing average AvgScore and CumScore results for simulating
    - haviors by calculating the node-wise accuracy of half selection (representing a scenario where there
    - model’s response at node i. The criteria for cor- Table 2. These baselines can serve as references:
    - baseline signify exceptionally poor performance,
  - Page 7:
    - erage accuracy simulating nonfiction personas
    - Table 3: Scaling performance on BehaviorChain across closed-source GPT-4o and the open-source Llama-
    - As demonstrated in Table 3, the performance of all behaviors than on sub-key behaviors in both fiction
  - Page 8:
    - Table 5: Comparison of model performance on
    - shown in Table 4, the distribution of correct be-
    - Table 4: AvgScore and CumScore at different stages of
    - Table 5, by comparing the model’s AvgScore and

## [[001-2024-nlp4pi-1-23|2024.nlp4pi-1.23]]

- Source PDF: `raw/sources/2024.nlp4pi-1.23.pdf`
- Likely table/result pages:
  - Page 1:
    - embeddings, achieving state-of-the-art perfor- psychological impacts on individuals and commu-
    - mance and enhancing detection accuracy while nities, leading to real-world violence and discrimi-
  - Page 2:
    - the same community, which GNNs can leverage to bined approach improves the accuracy, context-
    - target identification, which achieves state-of-the-art
  - Page 4:
    - icantly outperform all others, with XG-HSI-BERT
    - achieving the highest accuracy (0.741) and Macro
    - F1 (0.747). These results demonstrate the superior
    - Baselines. The baseline models are: 5 Graph Explanation Case Study
  - Page 5:
    - By enhancing the detection accuracy and providing
    - exceptional performance, significantly outperform- sion while curbing harmful rhetoric, thus promot-
    - highest accuracy (0.741) and Macro F1 (0.747).
  - Page 7:
    - Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, ers: State-of-the-art natural language processing. In

## [[003-2025-acl-long-115|2025.acl-long.115]]

- Source PDF: `raw/sources/2025.acl-long.115.pdf`
- Likely table/result pages:
  - Page 3:
    - Table 1: Examples of tweets for each class and main try level, with the share of hateful posts being
  - Page 4:
    - mance using average precision, which corresponds
    - to the area under the precision-recall curve, and is
    - include the Perspective API (Lees et al., 2022), a We report the average precision of each model
    - based on supervised learning. Specifically, we use languages (Table 2) and across countries (Table 3).
  - Page 5:
    - Table 2: Model performance across languages and evaluation sets, as measured by average precision (%). We
    - average precision of 41.1% on average across all
    - Llama3.1 8B, scores 32.4% on average. Addition- Low precision and recall As the average preci-
    - ally, despite being originally developed to detect sion corresponds to the area under the precision-
  - Page 7:
    - Figure 4: Cost-recall tradeoff in human-in-the-loop (UNESCO, 2023) and points to the potential role of
  - Page 8:
    - score distribution, which reduces precision. While real-world English-speaking and US contexts, po-
  - Page 12:
    - and Paul Röttger. 2023. Improving the detection of table language identification. In Proceedings of the

## [[014-bai-2025-state-toxicn-a-benchmark-for-span-level-target-aware-toxicity-extraction-in-chinese-hate-speech-det|Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det]]

- Source PDF: `raw/sources/Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det.pdf`
- Likely table/result pages:
  - Page 1:
    - For example, in Exp. 3 from Table 1, the target
  - Page 2:
    - Table 1: Examples of annotated posts from STATE TOXICN dataset with corresponding annotations of Target-
  - Page 3:
    - Table 2: Comparison of hate speech datasets based on Platforms, Language, #Posts, span-level annotations (Span),
  - Page 4:
    - Table 3: Fleiss’ Kappa for different granularities.
    - For example, in Exp. 2 from Table 1, Target- Others 351 3.68
    - is “LGBTQ, others”. The quadruple is [ 男同| 艾 Table 4: Statistics of annotated posts from the STATE
    - hierarchy detailed in Table 3. The detailed analysis
  - Page 5:
    - containing hateful information, making up 63.60%. Table 5: Statistics of train and test datasets, including
    - ICN in Table 4. Gender, Region, and Race are the non-hateful quads (Non-hate).
    - ing for 8.96%. In addition, the annotated lexicon detailed in Table 5. The fine-tuning process was
    - 2024), and Closed-source LLMs: LLaMA3-70B Pair), fine-tuned models significantly outperform
  - Page 6:
    - Table 6: Performance comparison of various models across different levels of annotated tasks, including Target,

## [[016-barel-2025-acquired-taste-multimodal-stance-detection-with-textual-and-structural-embeddings|Barel 等 - 2025 - Acquired TASTE Multimodal Stance Detection with Textual and Structural Embeddings]]

- Source PDF: `raw/sources/Barel 等 - 2025 - Acquired TASTE Multimodal Stance Detection with Textual and Structural Embeddings.pdf`
- Likely table/result pages:
  - Page 1:
    - stance. TASTE achieves state-of-the-art results tural Embeddings. Multi-participant conversations
    - ance U (“Government is a disease pretending to be lines, including the state-of-the-art, across topics
    - speaker’s stance may emerge as the conversation further adds, on average, 12% to the accuracy. This
  - Page 2:
    - sociolinguistics concepts of face (Goffman, 1955), modalities, serve as our baseline models (see Sec-
  - Page 4:
    - of d is 1 (for antipodal vectors/stances), and the in Table 1.
  - Page 5:
    - Table 1: Descriptive statistics of the datasets.
    - S-BERT has been shown to outperform traditional
  - Page 6:
    - (a) Post stance classification accuracy for 4Forums dataset.
    - (b) Author stance classification accuracy for 4Forums dataset.
    - (c) Post stance classification accuracy for CreateDebate dataset.
    - (d) Author stance classification accuracy for CreateDebate dataset.
  - Page 7:
    - Table 2(a–d) compares TASTE and the baseline # Interaction 14,460 9,640 13,764 6,462
    - benchmarks and across topics. The table also pro- SDP (Acc.) 81.2 76.3 78.1 67.7
    - Table 3: Post stance classification on the 4Forums
    - Reported values are average accuracy of a 5-fold

## [[019-cai-2025-unpacking-hateful-memes-presupposed-context-and-false-claims|Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims]]

- Source PDF: `raw/sources/Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims.pdf`
- Likely table/result pages:
  - Page 1:
    - state-of-the-art methods across datasets and metrics, while demon- now often refers to humorous or satirical image-text combinations
  - Page 6:
    - cases. In the false claim detection scenario, the label of a graph may Table 1: Summary of hateful meme datasets.
  - Page 7:
    - Table 2: Hateful Meme Classification results. The best and runner-up results are in bold and underlined, respectively.
    - Model AUC Accuracy Macro-F1 AUC Accuracy Macro-F1 AUC Accuracy Macro-F1
    - Table 3: Ablation studies by using different modules.
    - sometimes been overlooked, leading to inaccurate model evalua- sion, achieving the best baseline performance across many metrics.
  - Page 8:
    - surpasses the best baseline models by 5.75%, 1.56%, and 1.52% in fake news. If SHIELD framework indeed captures these features, it
    - terms of AUC on FHM, Harm-C, and Harm-P, respectively. It also should generalize to broader social media tasks. To verify this, we
    - achieves the highest Accuracy and Macro-F1 across all datasets, applied SHIELD to multimodal fake news classification task. For
    - confirming its superiority. The smaller gains on Harm-C and Harm- baseline models, we selected several of the most recently released
  - Page 9:
    - Table 4: Model specificity and generalization across hate targets. Harm-C + Harm-P denotes the combined dataset. Models are trained on
    - Model AUC Accuracy Macro-F1 AUC Accuracy Macro-F1 AUC Accuracy Macro-F1
    - Table 5: Performance on the Fake News Classification. language models. arXiv preprint arXiv:2106.09685 (2021).
    - Dataset Model Accuracy Macro-F1 memes via prompt based approach. In Proceedings of the ACM Web Conference
  - Page 10:
    - The detailed description of the comparison baseline is as follows:
    - As shown in Table 6, the model exhibits noticeable sensitivity to

## [[020-chen-2021-image-manipulation-detection-by-multi-view-multi-scale-supervision|Chen 等 - 2021 - Image Manipulation Detection by Multi-View Multi-Scale Supervision]]

- Source PDF: `raw/sources/Chen 等 - 2021 - Image Manipulation Detection by Multi-View Multi-Scale Supervision.pdf`
- Likely table/result pages:
  - Page 2:
    - alone [16, 27] or together with the input image [14, 26, 30]. ulation detection. To the best of our knowledge (Table 1),
    - state-of-the-art. Code and models are available at https:
  - Page 3:
    - Table 1. A taxonomy of the state-of-the-art for image manipulation detection. Note that edge and image labels used in this work are
    - image manipulation detection, see Table 1. In what follows, balance between the two. Directly using deeper features for
  - Page 5:
    - Figure 5. Dual Attention , with its channel attention module with the state-of-the-art, we adopt CASIAv2 [8] for train-
  - Page 6:
    - use two training sets and five test sets, see Table 2. DeepLabv3+ [6], see the supplement. This competitive
    - baseline is referred to as Seg in Table 3.
    - Table 2. Two training sets and five test sets in our experiments.
    - in the ablation study (Section 4.2), while for the SOTA comparison
  - Page 7:
    - Component Pixel-level manipulation detection (F1) Image-level manipulation detection
    - loss ESB NSB cpmv. spli. inpa. MEAN AUC Sen. Spe. F1
    - Table 3. Ablation study of MVSS-Net. Training: DEFACTO-84k. Test: DEFACTO-12k. Copy-move, splicing and inpainting are
    - have to be selective, choosing the state-of-the-art that meets
  - Page 8:
    - Table 4. Performance of pixel-level manipulation detection. Best result per test set is shown in bold. All the models are trained on
    - AUC Sen. Spe. F1 AUC Sen. Spe. F1 AUC Sen. Spe. F1 AUC Sen. Spe. F1
    - Table 5. Performance of image-level manipulation detection on Columbia, CASIAv1, COVER and DEFACTO-12k. Sen.: sensitivity.
    - Table 6. Com-F1, the harmonic mean of pixel-level F1 and

## [[021-chen-2024-cofipara-a-coarse-to-fine-paradigm-for-multimodal-sarcasm-target-identification-with-large-multimod|Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod]]

- Source PDF: `raw/sources/Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod.pdf`
- Likely table/result pages:
  - Page 1:
    - and image, respectively. The state-of-the-art ap-
  - Page 2:
    - within Large Multimodal Models (LMMs) (Liu state-of-the-art MSTI methods, and achieves com-
    - ing both the MSTI accuracy and explainability; 2) hanced ability to provide superior explainability in
  - Page 3:
    - like Exact Match accuracy and F1 score. Patro As for the finer-grained MSTI task, the label y is
  - Page 6:
    - only provide the text T and the LMM-generated Acc. P R F1
    - Table 1: Multimodal sarcasm detection results.
    - et al., 2023). We adopt Accuracy, F1 score, Preci-
    - L sion, and Recall to evaluate the MSD performance.
  - Page 7:
    - and F1 score (Molla and Joshi, 2019) as evaluation in MSTI samples further contributes to their sub-
    - Average Precision (AP) (Lin et al., 2014), i.e., the excels in EM and AP50 compared to baselines, es-
    - MSTI2.0, baseline descriptions and model imple- compared to MSTI-VB, suggesting that our model
    - Sarcasm Detection Performance. Table 1 illus- visual target identification performance, especially
  - Page 8:
    - Table 2: Multimodal sarcasm target identification results.
    - EM F1 AP AP50 AP75 (a) LMM Rationale: The tweet is sarcastic
    - Table 3: Ablation results on MSTI2.0 test set. for a #selfie for d 1st time first time ever" implies that Modi has never

## [[028-dong-2023-mvss-net-multi-view-multi-scale-supervised-networks-for-image-manipulation-detection|Dong 等 - 2023 - MVSS-Net Multi-View Multi-Scale Supervised Networks for Image Manipulation Detection]]

- Source PDF: `raw/sources/Dong 等 - 2023 - MVSS-Net Multi-View Multi-Scale Supervised Networks for Image Manipulation Detection.pdf`
- Likely table/result pages:
  - Page 2:
    - Fig. 1. Image manipulation detection by the state-of-the-art. Test images image manipulation detection. Note that several previous
    - lated) and specificity (lower false alarm on the authentic). (Table 1), we are the first to jointly exploit the noise view
    - bone as input of the auxiliary branch. As such, there is a risk (cid:1) Superior to the SOTA on multiple benchmarks. As exten-
    - ulation detection, remain semantic-aware and thus not MVSS-Net compares favorably against the SOTA. The inclu-
  - Page 3:
    - A Taxonomy of the State-of-the-Art for Image Manipulation Detection
    - tion when images circulate on the Internet. manipulation detection, see Table 1. We describe in brief
  - Page 7:
    - Pixel-Scale Loss. As manipulated pixels are typically in TABLE 2
    - tion 4.2), while for the SOTA comparison (Section 4.3) we train on
    - ments use two training sets and six test sets, see Table 2.
    - Through ConvGeM, the image-scale supervision can now pixel-level precision and recall, and report their F1. For
  - Page 8:
    - that accuracy is not a reliable metric when the class distribu- TABLE 3
    - bined loss, we empirically set a ¼ 0:16 and b ¼ 0:04, see a F1 scores are in percentage.
    - Setup #6 and #7 in Table 4, we see that MVSS-Net is bet-
    - Influence of the semantic segmentation backbone. We depart from Table 4. Compared with GMP, GeM obtains a higher pixel-
  - Page 9:
    - Training: DEF-84k. Test: DEF-12k. F1, Sensitivity (Sen.) and Specificity (Spe.) scores are in percentage. Best number per column is highlighted in bold. The
  - Page 10:
    - each pixel being the center of an object, while the other 4.3 Comparison with State-of-the-art
    - mum bbox that encloses all pixels in a given tempering tive, choosing the state-of-the-art that meets one of the fol-
    - Table 4 (Setup #9.1). Its relatively lower scores than lowing a common evaluation protocol where CASIAv2 is
    - tion (from 0.405 to 0.382, cmpv in Table 4) indicates the (trained on the same data as ManTra-Net and finetuned on

## [[034-garg-2026-just-kiddin-knowledge-infusion-and-distillation-for-detection-of-indecent-memes|Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes]]

- Source PDF: `raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf`
- Likely table/result pages:
  - Page 1:
    - state-of-the-art baselines across AUC, and F1,
    - an 6.3% and 3.2% in F1 and AUC. Given the
  - Page 2:
    - 2023), achieve comparable performance but re- 0.5% in F1 and AUC, respectively. Further, our
    - dependent toxicity due to their reliance on pattern with an AUC of 92.98.
    - compare to baseline methods in detecting toxicity mar and Nandakumar, 2022a),(Cao et al., 2022a)
  - Page 3:
    - the memes (See Appendix Table 11) KD is em-
  - Page 5:
    - representations by applying relation-specific trans- AUC, F1 score, Precision, Recall, and Accuracy.
  - Page 6:
    - Framework Accuracy F1 Precision Recall AUC
    - Table 1: Performance Comparison of various models on the HatefulMemes Dataset (seen & unseen splits). Top
    - NeXT (Liu et al., 2024b) was used in a zero-shot forms the competitive baseline models from prior
    - baseline reference for all reported values is RGCL. et al., 2024a; Cao et al., 2022b) across both the
  - Page 7:
    - Framework Accuracy F1 Precision Recall AUC
    - Table 2: Performance Comparison of various models on HarMeme Dataset across multiple metrics. The top values
    - per outperform in precision and recall, respectively,
    - while both fall short in recall and precision, show-

## [[013-ahn-2024-timechara-evaluating-point-in-time-character-hallucination-of-role-playing-large-language-models|Ahn 等 - 2024 - TimeChara Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models]]

- Source PDF: `raw/sources/Ahn 等 - 2024 - TimeChara Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models.pdf`
- Likely table/result pages:
  - Page 2:
    - character can interact with users drawing from their ral consistency of their responses. Table 1 outlines
    - events and deepens their emotional bond with the state-of-the-art LLMs, including GPT-4o (OpenAI,
    - unawareness of future events, their ability to recall
  - Page 3:
    - to TIMECHARA in Table 6 in Appendix A. The unawareness of the future (i.e., future
    - ter should accurately recall past events. Since
  - Page 4:
    - RoleBench ✓ ✗ ✗ ✗ ✗ Rouge-L w/ gold response:
    - Table 1: Comparison of TIMECHARA with other datasets or benchmarks: TemporalWiki (Jang et al., 2022),
    - Table 4. In the last column, ‘accurate’ means TIMECHARA uses spatiotemporal labels provided to the LLM judge
    - Table 2: An example of our future type data instance with the fact-based structured question.
  - Page 5:
    - Figure 2: Evaluation accuracy of LLM judges for spa-
    - Slytherin?” to first-year Harry on September 1st: Turbo (see Table 5) and manually annotate them with
    - accuracy of LLM judges with humans (marked by 100).
    - in-time character hallucination: The model should but should not wrongly recall it:{moment descrip-
  - Page 6:
    - Figure 3: An illustration of our automated pipeline for constructing TIMECHARA. See Table 2 and Appendix C for
    - as detailed in Appendix D.1 (see Table 13). For
    - Table 3: Data statistics of four series in TIMECHARA.
  - Page 7:
    - # Past-presence 1 (0.7%) 0 (0.0%) 3,459 (31.7%) poral consistency as in Table 5, despite their exten-
    - Table 4: Comparison of test data statistics from three
    - 10,895 instances, and Table 3 provides detailed
    - Table 4. While TIMECHARA consists of data in- stance dataset is challenging. Instead, we randomly

## [[022-chen-2024-socialbench-sociality-evaluation-of-role-playing-conversational-agents|Chen 等 - 2024 - SocialBench Sociality Evaluation of Role-Playing Conversational Agents]]

- Source PDF: `raw/sources/Chen 等 - 2024 - SocialBench Sociality Evaluation of Role-Playing Conversational Agents.pdf`
- Likely table/result pages:
  - Page 1:
    - agents that mimic diverse characters and hu- and utilized Rouge-L and GPT 3.5 to assess the
  - Page 5:
    - for CM Long, we prompt the agent to recall key- provided. Invalid questions are either modified by
  - Page 6:
    - Metrics Acc single Acc single Acc multiple Acc single Cover Cover Acc single Acc single Acc single
    - Table 1: Metrics and statistics of SocialBench. There are a total of 500 roles, comprising 6,000 questions and 30,800
    - We show the statistic of SocialBench in Table 1 and 102
    - may suffer from questionable accuracy on the role-
  - Page 7:
    - Table 2: Main results from SocialBench. Best performances are shown in bold, while suboptimal ones underlined.
    - As presented in Table 2, the performance of closed-
    - role-playing, such as Xingchen-Plus, outperform
  - Page 11:
    - ble 3 and Table 4. For the dimension of long-term
    - employ four methods for dialogue construction. logue context are provided in Table 5. For generat-
    - world scenarios. Data gathered through this group conversations can be found in Table 6.
  - Page 14:
    - Table 3: Prompt for role-playing tasks with GPT-4-Turbo.
    - Table 4: Prompt for automatic self-dialogue generation.

## [[083-ng-2024-how-well-can-llms-echo-us-evaluating-ai-chatbots-role-play-ability-with-echo|Ng 等 - 2024 - How Well Can LLMs Echo Us Evaluating AI Chatbots' Role-Play Ability with ECHO]]

- Source PDF: `raw/sources/Ng 等 - 2024 - How Well Can LLMs Echo Us Evaluating AI Chatbots' Role-Play Ability with ECHO.pdf`
- Likely table/result pages:
  - Page 6:
    - to assess the tone, thought process, and identification accuracy of the responses to iden-
    - baseline for random guessing is 50%. A success rate substantially higher than this baseline,
    - Baseline Methods We evaluate four widely used role-playing methods:
    - Table 1 presents the success rates of various role-playing baselines in deceiving human
  - Page 7:
    - Table 1: Success rates of role-playing LLMs in deceiving human evaluators. The human
  - Page 8:
    - Table 2: Success rates of role-playing LLMs in deceiving evaluator LLMs. The evaluator
    - Table 3: Success rates of role-playing LLMs in deceiving evaluator LLMs. The evaluator
    - responses are shown in Table 2 and Table 3, respectively. As discussed before, success rates
  - Page 9:
    - in Table 2, both models show proficiency in this differentiation, with success rates for all
    - by discrepancies between the results from Table 2 and Table 3. Note that unbiased models
    - should exhibit comparable accuracy in these two settings. In both scenarios, Gemini-1.0-
    - Pro demonstrates accuracy akin to random guessing, suggesting it is free of bias toward
  - Page 11:
    - accuracy and reliability of ai-generated medical responses: an evaluation of the chat-gpt
  - Page 13:
    - elicit personal insights relevant to that area, as listed in Table 4. We collect the data using
    - Table 4: Example questions for gathering human background information.

## [[090-sadeq-2024-mitigating-hallucination-in-fictional-character-role-play|Sadeq 等 - 2024 - Mitigating Hallucination in Fictional Character Role-Play]]

- Source PDF: `raw/sources/Sadeq 等 - 2024 - Mitigating Hallucination in Fictional Character Role-Play.pdf`
- Likely table/result pages:
  - Page 2:
    - Figure 2: Factual precision degrades when we minimize
    - tiveness and it can even hurt factual precision. This
    - Figure 3: Factual precision degrades with decreasing
    - RoleFact improves factual precision by 18%
  - Page 4:
    - one or more unsupported claims as a result Table 1: SGR Dataset
  - Page 5:
    - Baseline 0.41 3.7 0.72 6.5 0.52 6.4 0.65 5.2
    - Baseline 0.50 5.0 0.70 7.7 0.52 3.4 0.62 6.0
    - Baseline 0.61 3.8 0.76 5.8 0.65 4.2 0.74 4.8
    - Table 2: Factual precision (Fact Score ↑) and informativeness (SFPR ↑) of RoleFact on all tasks in the SGR dataset.
  - Page 6:
    - Table 3: Temporal hallucination rate (THR ↓) on scene-
    - Table 4: Ablation study (adversarial task, GPT-3.5)
    - Table 5: Human ratings on a scale of one to seven
    - sponses. This is shown in Table 4. The most sig-
  - Page 7:
    - of dragon training. In the baseline response, the ries (Zhang et al., 2018; Park et al., 2023a), demo-
    - retrieval. Unlike the baseline, RoleFact is able characters, known as character role-play (Shao
    - strange look towards him. The baseline response or instruction-tuning (Shao et al., 2023; Lu et al.,
  - Page 8:
    - Baseline Baseline + KGR Baseline + SR RoleFact
    - Table 6: Case Study, hallucinations are in red and underlined.

## [[107-wang-2025-opencharacter-training-customizable-role-playing-llms-with-large-scale-synthetic-personas|Wang 等 - 2025 - OpenCharacter Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas]]

- Source PDF: `raw/sources/Wang 等 - 2025 - OpenCharacter Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas.pdf`
- Likely table/result pages:
  - Page 8:
    - Brief statistics on these instruction datasets and data synthesis details are provided in Table 1.
    - Table 1: Statistics on our character-driven response synthesis. n is the number of characters randomly assigned
    - ment with six different data recipes as indicated in Table 2. Note that we always combine LIMA and
    - Table 2: The SFT data recipes for OpenCharacter ablation study. For our final OpenCharacter model, we
  - Page 10:
    - PersonaGym-Light are shown in Table 3. From this comparison, we observe OpenCharacter model
    - Table 3: Model performances on PersonaGym-Light. “EA,” “TC,” “LH,” “PC,” and “AJ” stands for the
    - LLaMA-3-8B-Instruct with its training data recipe indicated in Table 2.
    - We further conduct comprehensive ablation study on different data recipes discussed in Table 2. The
  - Page 11:
    - in Table 4, we can find that instructions from the combination of LIMA and Alpaca are slightly
    - mark. The results are listed in Table 5.
    - Table 5: Model performances on PersonaGym. “EA,” “TC,” “LH,” “PC,” and “AJ” stands for the evaluation
    - OpenCharacter models with their training data recipe indicated in Table 2.

## [[117-xu-2025-guess-what-i-am-thinking-a-benchmark-for-inner-thought-reasoning-of-role-playing-language-agents|Xu 等 - 2025 - Guess What I am Thinking A Benchmark for Inner Thought Reasoning of Role-Playing Language Agents]]

- Source PDF: `raw/sources/Xu 等 - 2025 - Guess What I am Thinking A Benchmark for Inner Thought Reasoning of Role-Playing Language Agents.pdf`
- Likely table/result pages:
  - Page 2:
    - monologues from the original novels as references, reasoning processes, including memory recall and
  - Page 3:
    - model how characters recall relevant memories,
    - the same input format of profile P and scenario S, Table 1: Case study of ROLETHINK, including data
    - filtered to ensure quality. Table 1 shows two com- ter thoughts not present in the original book. To
  - Page 4:
    - tered to ensure quality. Table 1 shows a complete
    - 2, MIRROR guides RPLAs to first recall related
    - rics including BLEU (Papineni et al., 2002) and
    - ROUGE-L (Lin, 2004). However, we observe that
  - Page 5:
    - pervisor Lord Mormont, his fellow Night’s Watch addition to MIRROR, we employ three baseline
  - Page 6:
    - BLEU ROUGE-L NLI LLM Human BLEU ROUGE-L NLI LLM Human
    - Table 2: Results of different methods and models on ROLETHINK. We evaluate both Gold Task (reproducing
    - original thoughts) and Silver Task (generating plausible thoughts) using BLEU, ROUGE-L, NLI scores, and both
    - Table 2 shows the experimental results for character
  - Page 7:
    - perts to analyze 100 randomly sampled charac- Table 3: Performance comparison on downstream RPLA
    - likely influenced by the tendencies in most role- Table 3 demonstrates that character thought data
    - incorporating relevant past events that human read- recall and tone consistency, we observe moder-

## [[130-yu-2025-beyond-dialogue-a-profile-dialogue-alignment-framework-towards-general-role-playing-language-model|Yu 等 - 2025 - Beyond Dialogue A Profile-Dialogue Alignment Framework Towards General Role-Playing Language Model]]

- Source PDF: `raw/sources/Yu 等 - 2025 - Beyond Dialogue A Profile-Dialogue Alignment Framework Towards General Role-Playing Language Model.pdf`
- Likely table/result pages:
  - Page 3:
    - Table 1: Comparison of BEYOND DIALOGUE with other datasets or framework. “✓” indicates that the
    - role profiles and evaluations in Table 1: Style, Char- brid task training has emerged as a pivotal method
  - Page 5:
    - Figure 2 panels 3-4, with accuracy metrics and cost profile-dialogue relationships. Meanwhile, D pre-
    - analysis in Table 5 of § A.2), while implementing serves the model’s general conversational ability.
  - Page 6:
    - pared to the other datasets listed in § A.3 Table 7, remaining metrics are automatically evaluated us-
    - using the MBTI classification (binary recall),
  - Page 7:
    - Recall ↑ Recall ↑ NMAPE ↓ NMAPE ↓ Precision ↑
    - Table 2: Main results of BEYOND DIALOGUE. We report the average scores with their standard error of the mean
    - statistically significant improvements over the untrained baseline (achieving p < 0.05 in t-test). The Qualification
    - performance. More baseline results are provided in § B.2 Table 10. All dialogues are evaluated by GPT-4o as judges,
  - Page 8:
    - the untrained baseline (p < 0.05 in t-test). Adding Comparable Baselines
    - Table 3: Comparison of Baseline Models on Dialogue
    - pared to their baseline performance. According comes. Detailed case studies are in § G.2.
    - to annotator feedback, models trained with our The results from Table 2 and Table 3 indicate that
  - Page 9:
    - Table 4: Ablation Results on CSERP Training Tasks. believe this is an important and underexplored di-
    - the dialogues generated during training. Addition- data accuracy. We employ trained professionals

## [[132-yu-2025-rpgbench-evaluating-large-language-models-as-role-playing-game-engines|Yu 等 - 2025 - RPGBENCH Evaluating Large Language Models as Role-Playing Game Engines]]

- Source PDF: `raw/sources/Yu 等 - 2025 - RPGBENCH Evaluating Large Language Models as Role-Playing Game Engines.pdf`
- Likely table/result pages:
  - Page 1:
    - that state-of-the-art LLMs can produce engaging mechanics. Game mechanics define how the game state
  - Page 3:
    - condition (whether it succeeds). Upon execution, an GS task (Table 1 shows the distribution).
  - Page 5:
    - Main Results Table 2 reports the format-check pass rate
  - Page 6:
    - 6 Main Results Table 3 presents our GS evaluation results,
    - Figure 3. LengthRatio of three models Table 4 summarizes the results. Interestingly, FAC increases
    - ing metrics exhibit minimal variance. Table 5 shows that
  - Page 7:
    - Table 3. Game Simulation results. LEN: length; FAC: role-playing factual consistency; PER: role-playing personality consistency; ACT:
    - Table 4. Performance under different sampling temperatures lated games, focusing on four subjective metrics: FAC (Fac-
    - variations. We observe in Table 5 that FAC score increases
    - Table 5. Performance under different number of simulation rounds
  - Page 8:
    - Table 6. Comparison of human and automatic evaluation scores for four subjective metrics (FAC, ACT, INT, and PER) on a subset of 20
    - Table 7. Mean Absolute Difference (MAD), Pearson correlation coefficient, and Kendall rank correlation coefficient between automatic
    - Examining Table 6, we find a fair degree of overlap in the 6. Conclusion
    - not for PER. From Table 7, we see that the inter-annotator

## [[040-guo-2025-multi-view-incongruity-learning-for-multimodal-sarcasm-detection|Guo 等 - 2025 - Multi-View Incongruity Learning for Multimodal Sarcasm Detection]]

- Source PDF: `raw/sources/Guo 等 - 2025 - Multi-View Incongruity Learning for Multimodal Sarcasm Detection.pdf`
- Likely table/result pages:
  - Page 2:
    - SOTA model (Jia et al., 2024) and attribute the • Experimental results indicate that our ap-
  - Page 3:
    - accuracy and ambiguous meaning, as shown in the Hindi, it is difficult for a non-multilingual pre-trained
    - in both recognition accuracy and sequential integrity,
    - et al., 2023) with more precision extraction and
  - Page 6:
    - Pre.(%) Rec.(%) F1(%) Pre.(%) Rec.(%) F1(%)
    - Table 1: Main results on MMSD dataset for sarcasm detection. We use ∗ indicates the reproduced results by using
    - ous works (Jia et al., 2024), we report the accuracy, 2022), Multi-View CLIP (Qin et al., 2023), MIL-
    - precision, recall, F1-score, and macro-average re- Net (Qiao et al., 2023), DMSD-CL (Jia et al., 2024)
  - Page 7:
    - Method Acc. P. R. F1 P. R. F1 Base fw fe fs c Acc.(%) F1(%) Acc.(%) F1(%)
    - Table 3: Experiment results of ablation study.
    - Table 2: Comparison results on SPMSD dataset (%).
    - The main results are shown in Table 1. Our analy-
  - Page 8:
    - compromising the baseline performance. These Case 2 investigates the impact of modifying non-
  - Page 9:
    - rious correlations, it achieves only a 68% accuracy 4186.

## [[044-he-2025-chumor-2-0-towards-better-benchmarking-chinese-humor-understanding-from-ruo-zhi-ba|He 等 - 2025 - Chumor 2.0 Towards Better Benchmarking Chinese Humor Understanding from (Ruo Zhi Ba)]]

- Source PDF: `raw/sources/He 等 - 2025 - Chumor 2.0 Towards Better Benchmarking Chinese Humor Understanding from (Ruo Zhi Ba).pdf`
- Likely table/result pages:
  - Page 1:
    - their accuracy slightly above random and Chinese humor. Table 1 provides examples of the
  - Page 2:
    - Table 1: Different types of jokes. Descriptions (Desc.) explain humor mechanisms. Examples (Ex.) illustrate each
    - highlight that the best accuracy achieved by et al., 2019), “C3” (Wang et al., 2022), and “Talk-
    - in Table 2. We highlight that most existing datasets
  - Page 3:
    - Table 2: Existing datasets related to humor. For the easily used to test LLMs’ capabilities in humor
    - shorthands in the table, abbreviations represent the fol- understanding. Specifically, we use two LLMs,
    - rize the jokes in RZB into six types in Table 1, with
  - Page 4:
    - Table 3: Examples from Chumor. The second example’s explanation is bad because the joke does not “creating an
    - Gemini (Google, 2024) from Google, GLM- culate accuracy scores as part of our evaluation. In
    - from OpenAI, ERNIE (Baidu, 2024) from tion Coefficient (MCC) in Appendix H in Table 4.
    - 释”，不需要解释为什么对或者不对。 the accuracy of different LLMs on Chumor in DP
  - Page 5:
    - Figure 1: The accuracy of different models’ test re- Pun-based 57.0
    - Gemini achieve the highest accuracy of 60.3%. 44.0
    - achieving 60.0% to 70.0% accuracy in both DP 62.0
    - GLM-4 plus achieves 65.0% accuracy on Homo- 61.0
  - Page 6:
    - instance, as shown in Figure 1, the accuracy of findings on its limitations in humor interpretation.
    - ing to 85.0% for CoT prompting (Table 4 in Ap-
    - positive rate, rising from 59.8% to 96.9% (Table 4
    - ing (Table 4 in Appendix H). We highlight that a length, 151,730 Chinese characters, is comparable

## [[048-hong-2025-rhetorical-device-aware-sarcasm-detection-with-counterfactual-data-augmentation|Hong 等 - 2025 - Rhetorical Device-Aware Sarcasm Detection with Counterfactual Data Augmentation]]

- Source PDF: `raw/sources/Hong 等 - 2025 - Rhetorical Device-Aware Sarcasm Detection with Counterfactual Data Augmentation.pdf`
- Likely table/result pages:
  - Page 5:
    - Table 1: The overall statistics of nine rhetorical devices in RedSD. Due to space limitation, we use the following
    - Table 2: Number of dialogues generated at each phase.
    - Table 1, hyperbole and presupposition are the
    - of sarcastic and non-sarcastic dialogues. Table 2
  - Page 6:
    - Table 3: Examples of sarcastic dialogues and their corresponding counterfactuals in RedSD. Due to space limitation,
    - Table 4: Human and automatic evaluation results of
    - As shown in Table 4, the Human-Refined set-
  - Page 7:
    - Model Acc Macro Macro Macro Sarc Sarc Sarc Non-Sarc Non-Sarc Non-Sarc
    - Table 5: Experimental results (%) on the test set of RedSD. The best results are represented in bold. The second-best
    - other hand, since the context remains identical and detection results using seven metrics: Accuracy
    - only the sarcastic utterance is rewritten, annotators (Acc), Macro F1 score, Macro Precision (Macro P),
  - Page 8:
    - Table 6: Accuracy (%) across different rhetorical devices of different models trained on different datasets when
    - Table 7: Macro F1 scores (%) of intra- and cross-dataset
    - attributed to the presence of instances that require complex scenarios, we compute accuracy for each
    - as sarcastic, resulting in inflated accuracy across
  - Page 9:
    - Table 8: Macro F1 scores (%) of ablation study. cus on the performance within our dataset, which
    - As shown in Table 8, the DCA strategy yields casm detection into context: The effects of class im-
    - baseline systems, demonstrating the necessity and place: Santiago.
  - Page 12:
    - Artificial Intelligence, EAAI 2014, February 20-27, errors made by various models in Table 9. As

## [[052-hwang-2025-bottlehumor-self-informed-humor-explanation-using-the-information-bottleneck-principle|Hwang 等 - 2025 - BottleHumor Self-Informed Humor Explanation using the Information Bottleneck Principle]]

- Source PDF: `raw/sources/Hwang 等 - 2025 - BottleHumor Self-Informed Humor Explanation using the Information Bottleneck Principle.pdf`
- Likely table/result pages:
  - Page 2:
    - matic evaluation metrics that resemble precision dictions has been used for opinion understanding
    - and recall, and better correlate with human judg- (Hwang et al., 2024; Hoyle et al., 2023), factual-
  - Page 6:
    - propose LLM-based precision and recall scores.
    - For recall, we decompose the reference ref into
    - Precision follows the same process in reverse, Figure 3: An example analysis of the explanations of ZS
    - Precision = 1 LLM (x , ref ) = Yes alignment with human judgment. Prompts are in
  - Page 7:
    - Table 1: Precision, Recall, and F1 scores of models and baselines on three multimodal humor benchmarks.
    - Table 2: F1 score comparison of using a single refined
    - Ablation study. Table 2 presents an ablation
  - Page 8:
    - Table 3: Precision, Recall, and F scores on interme-
    - ing precision and recall values in Table 3. For
    - ations, primarily driven by recall, which increases
    - initial hop. Precision also improves significantly at method inspired by the information bottleneck prin-
  - Page 9:
    - the model verify the accuracy and relevance of each
  - Page 10:
    - accuracy, and updatability. In Findings of the Asso- kenSHAP: Interpreting large language models with

## [[053-jana-2024-continuous-attentive-multimodal-prompt-tuning-for-few-shot-multimodal-sarcasm-detection|Jana 等 - 2024 - Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal Sarcasm Detection]]

- Source PDF: `raw/sources/Jana 等 - 2024 - Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal Sarcasm Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - timodal baseline methods in the few-shot set-
  - Page 2:
    - state-of-the-art results in few-shot multimodal sar-
  - Page 3:
    - tions while achieving state-of-the-art performance can be directly fed to the PLM. However, PLMs
  - Page 5:
    - Accuracy (Acc), mean Macro-F1 (F1), and the stan-
    - compare our model with state-of-the-art multi-
  - Page 6:
    - Table 1: Statistics of MMSD and MMSD2.0 dataset in the few shot setting. For splits presented as X/Y, X represents
    - Table 2: Performance comparison of existing methods with our proposed model CAMP. The best results across
    - image, text, and image attributes. D&R Net We run all the baseline models in their original
    - data in Table 2. Our findings are as follows: (1)
  - Page 7:
    - Table 3: Performance comparison on OOD setting. Dis-
    - Table 4: Ablation on caption tokens for CAMP model for various token lengths.
    - lines across both the datasets. This observation is It can be observed from Table 3 that our model
    - methods should outperform unimodal ones, we find of language understanding, which results in better

## [[065-li-2025-ambiguity-aware-multi-level-incongruity-fusion-network-for-multi-modal-sarcasm-detection|Li 等 - 2025 - Ambiguity-aware Multi-level Incongruity Fusion Network for Multi-Modal Sarcasm Detection]]

- Source PDF: `raw/sources/Li 等 - 2025 - Ambiguity-aware Multi-level Incongruity Fusion Network for Multi-Modal Sarcasm Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - posed model over state-of-the-art methods. sought to explore diverse multimodal strategies
  - Page 6:
    - where A denotes the size of mini-batch, i refers Model Acc(%) Pre(%) Rec(%) F1(%)
    - Table 1: Comparison results for sarcasm detection.
    - sixteen baselines shown in Table 1. More details
    - baseline models, as presented in Table 1. Addi-
  - Page 7:
    - Table 2: Experimental results of ablation study.
    - and DGP on F1-score. This indicates that AMIF simultaneously and efficiently mining the hidden in-
    - metrics, outperforming Acc, Pre, Rec and F1-score fine-grained inter-modal fragments. 3) AMIF w/o
    - by 1.15%, 1.66%, 1.78% and 1.72%, respectively. AG exhibits a 0.81% decrease in F1-score and a
  - Page 8:
    - the metrics ACC and F1-score for different T, λ
    - highest F1-socre and ACC are achieved when λ
    - small values don’t enhance the accuracy of local Multi-level Incongruity Fusion Network (AMIF)
  - Page 9:
    - cantly outperforms state-of-the-art methods on the Empirical Methods in Natural Language Processing,
  - Page 11:
    - shown in Table 3. 4. HKE (Liu et al., 2022): a baseline that
    - A.2 Baseline Models atomic and composition-level congruities.
    - 2. ViT (Dosovitskiy et al., 2020): a baseline that 8. SAHFN (Liu et al., 2024): a hierarchical fu-

## [[089-ravi-2024-small-but-funny-a-feedback-driven-approach-to-humor-distillation|Ravi 等 - 2024 - Small But Funny A Feedback-Driven Approach to Humor Distillation]]

- Source PDF: `raw/sources/Ravi 等 - 2024 - Small But Funny A Feedback-Driven Approach to Humor Distillation.pdf`
- Likely table/result pages:
  - Page 2:
    - human judgments with up to 76% accuracy, but
    - Our work on distilling humor is a step towards rics such as BLEU (Papineni et al., 2002), ROUGE
  - Page 5:
    - where λ corresponds to the average output length, ROUGE (Lin, 2004), may not work well for the
  - Page 6:
    - This baseline is denoted as BART-FT-WS (WS paraphrase of I is P ” (for i = 1, 2). Conversely,
    - by some of the authors (“annotators”). In Table 1, sitional biases to a huge extent for this task. Hence,
  - Page 7:
    - Table 1: Evaluation of Human Agreement with different
    - Table 5: Effect of feedback frequency on win rate of
    - Table 2: LLM-based Evaluation of student models - Win
    - enhancement in the student, with the DPO baseline
  - Page 8:
    - Table 6: Qualitative Examples showcasing variants trained with different types of feedback
    - Table 7: Effect of length filter on average response
    - ing or active learning could be leveraged to choose without length filters is shown in Table 7. This is
    - ple. Table 4 shows that simply increasing the data Figure 6 highlights instances where each of the
  - Page 10:
    - Jack Hessel, Ana Marasovic, Jena D. Hwang, Lillian Chin-Yew Lin. 2004. ROUGE: A package for auto-

## [[096-srirag-2025-besstie-a-benchmark-for-sentiment-and-sarcasm-classification-for-varieties-of-english|Srirag 等 - 2025 - BESSTIE A Benchmark for Sentiment and Sarcasm Classification for Varieties of English]]

- Source PDF: `raw/sources/Srirag 等 - 2025 - BESSTIE A Benchmark for Sentiment and Sarcasm Classification for Varieties of English.pdf`
- Likely table/result pages:
  - Page 1:
    - We collect datasets for these language varieties Table 1: Comparison of BESSTIE with past benchmarks
  - Page 2:
    - namely, Australian (en-AU), Indian (en-IN), and evaluation provides a solid baseline to examine
  - Page 3:
    - Table 2: Performance of DISTIL on sentiment classifica-
    - erate ratings, i.e., 2 and 4 stars (OURS). Table 2
  - Page 4:
    - P (en¯g) in Table 3 is the probability that the text
    - Table 3: Data quality for each variety and subset.
    - With respect to the true label (based on the loca- Table 4: Inter-annotator agreement for the validation
    - subsets of the corpus3, focusing on the transcrip- tators, measured by κ, are reported in the Table 4.
  - Page 5:
    - Table 5: Dataset statistics for each variety, subset, split, and label type. % Pos. Sent. and % Pos. Sarc. indicates the
    - for the two domains and three varieties. Table 5 precision, we fine-tune quantised decoder models
  - Page 6:
    - We present our results and subsequent discussions in Table 5), sarcasm classification is conducted
    - to address the following questions: (a) How well only on REDDIT subset. Table 6 shows that mod-

## [[119-xue-2024-breakthrough-from-nuance-and-inconsistency-enhancing-multimodal-sarcasm-detection-with-context-awar|Xue 等 - 2024 - Breakthrough from Nuance and Inconsistency Enhancing Multimodal Sarcasm Detection with Context-Awar]]

- Source PDF: `raw/sources/Xue 等 - 2024 - Breakthrough from Nuance and Inconsistency Enhancing Multimodal Sarcasm Detection with Context-Awar.pdf`
- Likely table/result pages:
  - Page 1:
    - We evaluate our method on the MUStARD dataset, achieving an accuracy of 76.9 and an F1 score of 76.1, which
    - surpasses the current state-of-the-art IWAN model by 1.7 and 1.6 respectively.
    - alogue, the accuracy of the ERC model is greatly
  - Page 2:
    - ficacy of our methods, achieving an F1 score of However, these multimodal sarcasm detection
    - 76.1, surpassing the state-of-the-art methods by methods often underutilize the rich multimodal infor-
    - analysis with state-of-the-art methods, explor-
  - Page 5:
    - wi wi wi wi obtained: precision (P), recall (R), and F1-score
    - (F1). These metrics provide a comprehensive view
  - Page 6:
    - text models and multimodal models. Table 1
    - The com parison results are shown in Table 1.
    - it is wor th noting from Table 1 that our model can
    - mental setup. The F1 score sur passes that of the
  - Page 7:
    - Table 1: The experimental results of nine comparison models and our proposed model. S-D means
    - Firstly, Table 3 indicates that our model’s effec-
    - after removing the CAAF module, the F1 score
    - the WWC module downstream of the task, the F1
  - Page 8:
    - Table 2: Different modal inputs and their corresponding experimental results.
    - Table 3: According to the test data divided in MUStARD dataset, we performed ablation analysis on our
    - pared C&W with the other nine baseline models machine translation architectures. arXiv preprint

## [[143-zhao-2024-zerostance-leveraging-chatgpt-for-open-domain-stance-detection-via-dataset-generation|Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation]]

- Source PDF: `raw/sources/Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation.pdf`
- Likely table/result pages:
  - Page 2:
    - the generation by incorporating desired attributes Table 1: An example of CHATStance.
    - Table 1 shows a generated sample from our CHAT-
  - Page 4:
    - Table 2: Examples of generated claims. are [STANCE] the “[CLAIM]”. Please generate
    - texts are shown in Table 3. More examples are
  - Page 5:
    - Table 3: Examples of generated texts given claims and stance labels.
    - In this section, we first introduce the baseline
  - Page 6:
    - the macro-averaged F1 across all stance classes as variability scores to improve the data quality. More
    - tions. Random Guess is a baseline that randomly 5 Results and Discussions
    - GPT is a strong zero-shot baseline that directly pre-
    - Table 4. First, we observe that ZeroStance outper-
  - Page 7:
    - Table 4: Comparison of ZeroStance (RoBERTa + CHATStance) with unsupervised and data augmentation baselines.
    - Table 5: Ablation studies of our approach on human-annotated datasets.
    - of ibm30k, which are not well captured by other sults are shown in Table 5.
    - average F1-macro. This result demonstrates that mance on most datasets. Similar results can be
  - Page 8:
    - Table 6: Results of different sizes of training set of CHATStance.
    - Table 7: Augmenting existing human-annotated stance detection datasets with our CHATStance dataset.
    - Table 8: Comparison of each human-annotated dataset (ZeroStance-Aug) and evaluated using the left-out
    - and CHATStance (CHAT) as the open-domain dataset. dataset. The results are shown in Table 7. We ob-

## [[144-zhao-caragea-2024-ez-stance-a-large-dataset-for-english-zero-shot-stance-detection|Zhao和Caragea - 2024 - EZ-STANCE A Large Dataset for English Zero-Shot Stance Detection]]

- Source PDF: `raw/sources/Zhao和Caragea - 2024 - EZ-STANCE A Large Dataset for English Zero-Shot Stance Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - ing state-of-the-art deep learning models. Fur- still exhibits several limitations. First, the VAST
    - Garrido et al., 2020), and cross-target stance detec- class in Table 1). Deep learning models can easily
  - Page 2:
    - Text: What happened to "herd immunity"? Are people noun phrase and claim targets (see Table 1); 3)
    - We establish baseline results using both traditional
    - Table 1: Examples from EZ-STANCE and VAST.
    - neutral) in Table 1. As we can see from the table, adapted from different but related targets. However,
  - Page 3:
    - Table 2: Comparison of English stance detection datasets.
    - this task are limited. In Table 2, we compare our as keywords for crawling (e.g., sports, education,
    - table, VAried Stance Topics (VAST) (Allaway and as supplementary keywords. In total, we collect
    - a new and more challenging task in which clas- Protection" (EP), and “Politics" (P). Table 3 shows
  - Page 4:
    - Table 3: The domains used in our dataset and the selected query keywords for each domain.
    - Table 4: Overall label distribution for noun-phrase and
    - claim targets for each domain is shown in Table 4.
    - domain) are shown in Table 5. The full statistics of
  - Page 5:
    - Table 5: Comparison of key statistics of EZ-STANCE subtask A and subtask B (with Covid Epidemic (CE) as the
    - Dataset Size In Table 5, we observe that EZ- Suppose we are given a training set Dtrain=
    - Text/target Lengths Table 5 indicates that the i
    - space (Bojanowski et al., 2017). As shown in Table trained models, we propose to transform stance
  - Page 6:
    - Table 6: Examples of formulating ZSSD as NLI. The
    - amples in Table 6 demonstrate the re-formulation
    - 2020), we employ the macro-averaged F1 score
    - sider fine-tuning the base version of state-of-the-art targets; 2) the test subset with noun-phrase targets

## [[026-ding-2024-edda-an-encoder-decoder-data-augmentation-framework-for-zero-shot-stance-detection|Ding 等 - 2024 - EDDA An Encoder-Decoder Data Augmentation Framework for Zero-Shot Stance Detection]]

- Source PDF: `raw/sources/Ding 等 - 2024 - EDDA An Encoder-Decoder Data Augmentation Framework for Zero-Shot Stance Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - demonstrate our approach substantially improves over state-of-the-art ZSSD techniques. The proposed EDDA
  - Page 2:
    - accuracy improvements compared to conventional
    - forms current state-of-the-art methods. tation approaches for ZSSD. These methods ef-
  - Page 5:
    - where W , W and W are trainable parameters. the average F1 score on the F avor and Against
    - vectors, enabling the rationale knowledge to effec- Macro F1 score, defined as the average F1 score
    - yˆ = sof tmax(W o (λAtt + h x )). (2) similarity, ROUGE (Lin, 2004) to measure content
    - as our loss function for stance detection: 4.3. Compared Baseline Methods
  - Page 6:
    - Table 1: Experimental results on two zero-shot stance detection (ZSSD) datasets. The results with ‡, ♢
    - target and zero-shot stance detection using con- benchmark datasets are reported in Table 1. We
    - outperform other contrastive approaches, espe-
    - Table 2: Performance comparison of cross-target
  - Page 7:
    - Table 3: Examples of text generated by TDDA and EEDA.
    - results shown in Table 2, we can see that EDDA per- targets and enhancing ZSSD performance.
    - ods under the cross-target condition. This verifies SimCSEaug ↓ SimCSEtest ↑ ROUGE ↓ Levenshtein ↑
    - Table 4: Text similarity comparison. aug denotes
  - Page 8:
    - EDDA, we provide example texts generated by both accuracy improved steadily as more augmented
    - methods in Table 3. Despite prompts to increase data was added, peaking at around 6000 samples.
    - linguistic variance, making them less realistic. In baseline data generation methods, EDDA consis-
    - contrast, the texts from EDDA contain rich sen- tently improves accuracy. Moreover, under the 10%

## [[100-taranukhin-2024-stance-reasoner-zero-shot-stance-detection-on-social-media-with-explicit-reasoning|Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning]]

- Source PDF: `raw/sources/Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning.pdf`
- Likely table/result pages:
  - Page 1:
    - outperforms the current state-of-the-art models on 3 Twitter datasets, including fully supervised models. It can bet-
  - Page 2:
    - external knowledge bases (KBs) may struggle from the current state-of-the-art models on 3 Twitter
    - to further increase the model’s accuracy (Sec 2.3).
    - forms all the baseline methods including the fully erate intermediate reasoning steps. As our exper-
    - supervised state-of-the-art models. In addition, the iments show, choosing the right prompt is key to
  - Page 3:
    - To further increase the model’s prediction accuracy
    - than increasing the accuracy of the model, self-
  - Page 4:
    - 2020) to load the LLaMA models in half-precision
  - Page 5:
    - Table 1: Experimental results on the SemEval 2016 task 6a dataset. We report macro F scores for
    - The second-best results for each group of the baseline models are highlighted with underlining.
    - few-shot baseline, but augment the examples with cess to the set of supporting examples compared
    - Table 1 displays the performance of Stance Rea-
  - Page 6:
    - model performance. Table 3 shows that when we
    - LLaMA 65B 68.5 75.5 73.7 3 Twitter datasets from different domains. Table 2
    - achieves state-of-the-art performance on all the
    - Table 2: Generalization results across three

## [[111-weinzierl-harabagiu-2024-tree-of-counterfactual-prompting-for-zero-shot-stance-detection|Weinzierl和Harabagiu - 2024 - Tree-of-Counterfactual Prompting for Zero-Shot Stance Detection]]

- Source PDF: `raw/sources/Weinzierl和Harabagiu - 2024 - Tree-of-Counterfactual Prompting for Zero-Shot Stance Detection.pdf`
- Likely table/result pages:
  - Page 4:
    - and e , produced in phase B, as the baseline re-
  - Page 5:
    - Table 1: Dataset details and distribution of stance values for test collections from SemEval-2016 Task 6 A,
    - lection of COVAXFRAMES are provided in Table 1.
    - ferent stance-annotated datasets, detailed in Table 1. from Twitter. The objects of the stance annota-
    - “Abortion”, “Atheism”, “Climate Change”, “Femi- MMVAX-STANCE are provided in Table 1.
  - Page 6:
    - Table 2: Results from prior stance detection fine-tuning experiments and tabula rasa zero-shot stance detection
    - experiments on the test collection from SemEval-2016 Task 6 A. Missing values represent unreported precision,
    - Table 3: Results from prior stance detection fine-tuning experiments and tabula rasa zero-shot stance detection
    - nAI, 2023). Furthermore, two baseline prompting demonstrating the importance of taking into ac-
  - Page 7:
    - tiple baseline systems utilized by prior work on (Xu et al., 2023) were also fine-tuned for stance
    - on COVAXFRAMES due to the benefits of con- of multimodal stance detection. Table 4 illustrates
    - sidering attitude consistency. Table 3 illustrates that LLaVA-1.5 and GPT-4V underperform the fine-
    - Two baseline prompting methods were employed if not thousands, of training examples. Further-
  - Page 8:
    - Table 4: Results from prior multimodal stance detection fine-tuning experiments and tabula rasa multimodal
    - ToC prompting improves upon baseline prompting MMVAX-STANCE demonstrate significant ad-
  - Page 9:
    - lyzing the 599 mistakes made by GPT-4V on the strong baseline systems were considered for com-

## [[137-zhang-2024-an-llm-enabled-knowledge-elicitation-and-retrieval-framework-for-zero-shot-cross-lingual-stance-iden|Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden]]

- Source PDF: `raw/sources/Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden.pdf`
- Likely table/result pages:
  - Page 1:
    - rives different types of stance knowledge from ing data) in target language. The state-of-the-art
  - Page 4:
    - Table 1: Categories and examples of speech act lexicon 10 l k → INF knowledge
    - i Table 1 shows our design of the speech act cat-
  - Page 7:
    - Acc (%) F1 (%) Acc (%) F1 (%) Acc (%) F1 (%)
    - Table 2: Experimental results of comparative baselines and our proposed method KEAR on the three datasets.
    - We use accuracy and macro F1 as the evaluation
    - metrics. Table 2 reports the experimental results
  - Page 8:
    - Acc (%) F1 (%) Acc (%) F1 (%) Acc (%) F1 (%)
    - Table 3: Ablation results of the variants of our proposed method KEAR on the three datasets. For each variant of
    - (macro F1) better than the above baseline methods types of knowledge, the serious decrease in both
    - on the three datasets. This improvement demon- accuracy and F1 indicates the effectiveness of fine-
  - Page 9:
    - Table 4: Human evaluation on the efficacy of each type of stance knowledge. Ratio 1 and Ratio 2 denote the correct
    - From the results in Table 4, we can see that the guages are rather limited (Lai et al., 2018;
    - can see that the accuracy of inference knowledge is high-resource source language to low-resource tar-
  - Page 12:
    - tweets: The catalonia independence corpus. In Pro- Table 5: The impact of knowledge sources and their uti-
    - model. Experimental results in Table 5 show that
    - two lines of ablation study in Table 3. Only using
    - Table 6 provides cases of background knowledge

## [[075-li-zhang-2024-pro-woman-anti-man-identifying-gender-bias-in-stance-detection|Li和Zhang - 2024 - Pro-Woman, Anti-Man Identifying Gender Bias in Stance Detection]]

- Source PDF: `raw/sources/Li和Zhang - 2024 - Pro-Woman, Anti-Man Identifying Gender Bias in Stance Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - et al., 2018; Zhao et al., 2018; Cao and Daumé III, state-of-the-art models (Allaway and McKeown,
  - Page 2:
    - Table 1: The list of categories used in GenderStance.
    - Ds= (xs, ts, ys) Ns and two gender evaluation Table 2: Examples of noun phrases representing the
    - nology. The complete domain list is shown in Table
    - of which are shown in Table 2, [TOPIC] repre- × ×
  - Page 3:
    - Table 4: Statistics of VAST and SemEval-2016 datasets.
    - this tendency on F1 measure. An unbiased model
    - shown in Table 4. stance classification. WS-BERT (He et al., 2022)
    - We calculate the F1 for each class and adopt the pair for classification. KASD (Li et al., 2023a)
  - Page 4:
    - Table 6: Performance of the models on GenderStance
    - KASD 56.8 -1.3 0.5 10.6 -16.6 are same as those in Table 5.
    - Table 5: Analysis of gender bias in stance detection. Third, in terms of training data, although both
    - The F1 metric represents the macro-average F1 score VAST and SemEval-2016 show similar trends with
  - Page 8:
    - Table 3. For the label None, we still use claims
    - Table 7: The complete pairs of noun phrases represent-

## [[085-niu-2024-a-challenge-dataset-and-effective-models-for-conversational-stance-detection|Niu 等 - 2024 - A Challenge Dataset and Effective Models for Conversational Stance Detection]]

- Source PDF: `raw/sources/Niu 等 - 2024 - A Challenge Dataset and Effective Models for Conversational Stance Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - inherent in conversational data. Notably, even state-of-the-art stance detection methods, exemplified by GLAN,
    - exhibit an accuracy of only 50.47%, highlighting the persistent challenges in conversational stance detection.
  - Page 2:
    - Cantonese and suffers from a scarcity of labeled ation of state-of-the-art stance detection methods
    - (more than two-turn) comments, MT-CSD exhibits teristics of these datasets are presented in Table 1.
  - Page 3:
    - Table 1: Comparison of different stance detection
  - Page 4:
    - Table 3: Annotation consistency and agreement.
    - Table 2: The number of data items for each target.
    - stance or too noisy, while posts with more than presented in Table 3. The results indicate that the
    - Following this stringent data filtering process, the Table 5 presents the statistics of our MT-CSD
  - Page 5:
    - Table 4: Statistics of the MT-CSD dataset. Here,
  - Page 6:
    - Table 5: Statistics of the MT-CSD dataset with varying input depths.
    - into a two-layer GCN. The graph representation H utilized in the experiments and outline the baseline
    - MHA After obtaining the sentence vectors (H , F represents the average F1 score computed

## [[141-zhang-2025-mpvstance-mitigating-hallucinations-in-stance-detection-with-multi-perspective-verification|Zhang 等 - 2025 - MPVStance Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification]]

- Source PDF: `raw/sources/Zhang 等 - 2025 - MPVStance Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification.pdf`
- Likely table/result pages:
  - Page 1:
    - troduce MPVStance, a framework that incor- accuracy and consistency. For instance, consider
    - factual accuracy, logical consistency, contex-
    - new benchmarks for reliability and accuracy
    - * Corresponding author. tion. First, the baseline response generated by the
  - Page 2:
    - accuracy and logical consistency, ensuring no as-
    - cantly outperforms existing state-of-the-art meth-
    - that MPVStance outperforms state-of-the-art logical validity. Knowledge augmentation involves
    - ing scenarios. Our ablation studies further prove the factual accuracy of generated content
  - Page 3:
    - tify and fix hallucinations (Yan et al., 2024a; Ding 3.2 Baseline Response Generation
    - The first step of our model is to generate a baseline
    - the target. The baseline response is generated by a
    - To guide the model in generating baseline re-
  - Page 4:
    - seen as dismissing climate change’s urgency?" factual accuracy, logical coherence, and contextual
    - incorrectly adopt neutrality despite downplaying lucinations in the baseline response, RAG strength-
    - Expert Perspective aligns the response with ex- to verify or challenge the baseline response against
    - ing sentiment can lead to a misclassification. being evaluated, such as factual accuracy, logical
  - Page 5:
    - sistencies identified in the baseline response. The final stance label y is determined by the
    - suring the accuracy and reliability of the stance
    - phase, the baseline response R i was generated, and We conduct experiments on the VAST and SEM16
    - tion by systematically comparing the baseline re- instance comprising a sentence r, a target t, and a
  - Page 6:
    - et al., 2022a), which incorporates contrastive learn- tance compare to state-of-the-art stance detection
    - EDDA-LLaMA(Ding et al., 2024a), and a collab- Performance Comparison with State-of-the-Art
    - LLM-based Models We compare with KE- stance detection accuracy on the VAST and SEM16
    - knowledge-enhanced prompt tuning, KASD (Li consistently outperforms state-of-the-art stance de-

## [[142-zhang-2025-t-mad-target-driven-multimodal-alignment-for-stance-detection|Zhang 等 - 2025 - T-MAD Target-driven Multimodal Alignment for Stance Detection]]

- Source PDF: `raw/sources/Zhang 等 - 2025 - T-MAD Target-driven Multimodal Alignment for Stance Detection.pdf`
- Likely table/result pages:
  - Page 1:
    - outperforms state-of-the-art models, with op-
    - Despite progress, existing MSD methods face stance detection accuracy in cases of modality
  - Page 2:
    - that T-MAD outperforms state-of-the-art mod- 11,300 instances (Weinzierl and Harabagiu, 2023).
    - the best accuracy, and a depth of 5 optimally multimodal stance detection datasets, totaling
    - balancing accuracy and efficiency. 17,544 annotated instances (Liang et al., 2024).
    - et al., 2024).MultiClimate deploys state-of-the-art
  - Page 5:
    - step remains target-guided, reinforcing the focus and 10% testing, as summarized in Table 9.
    - proceeds iteratively, refining specific aspects of the For the MMSD dataset, we use the Macro F1-
    - either of the following conditions is met: A fixed F1-score provides an equal weight to each class,
    - racy and weighted F1-score as the evaluation met-
  - Page 6:
    - Table 1: Experimental results (%) of in-target multi-modal stance detection.Results with * denote the significance
    - tests of our T-MAD over the baseline models at p-value < 0.05.
    - compare to state-of-the-art models on the MMSD
    - model (Devlin et al., 2019), and for image embed- Performance Comparison with State-of-the-Art
  - Page 7:
    - Table 2: Experimental results (%) of zero-shot multi-modal stance detection. Best scores of each group are in bold.
    - Results with * denote the significance tests of our T-MAD over the baseline models at p-value < 0.05.
    - ting (Table 1), T-MAD+CWVF establishes a new Vision+CWVF. Similarly, on the MWTWT and
    - state-of-the-art, achieving the highest Macro F1 MRUC tasks, T-MAD+CWVF demonstrates su-
  - Page 8:
    - Modality Method ACC F1 F1 scores for MWTWT and MRUC decreasing
    - ResNet50 0.424 0.399 sistencies and improve prediction accuracy. The
    - Multi-modal Table 4: Macro F1-scores of ablation study on T-MAD
    - T-MAD+CWVF 0.780* 0.808* Macro F1 scores of 69.00 and 71.80 for MTSE
