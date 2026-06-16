# HARM

## HARM-MOE-Off

A notebook with guidance into how to run the model can be found [HERE](./HARM-MOE-Off/run.ipynb)

## SBIC-Explain 

The dataset proposed by this work is based on the [original SBIC dataset](./README.md#original-sbic-reference).

The dataset is in the parquet format and can be loaded using pandas:

```python
import pandas as pd

sbic_explain = pd.read_parquet("./SBIC-Explain.parque.gzip")
```

### Dataset structure:

|   Column     |       Non-Null | Count |  Dtype  |
| -------- | ------- | -------- | ------- |
| base_model   |     123596 | non-null |  object 
 | set   |             123596 | non-null |  object | 
 | post   |            123596 | non-null |  object | 
 | is_offensive   |    123596 | non-null |  float64 |
 | targetMinority   |  123596 | non-null |  object | 
 | targetCategory   |  123596 | non-null |  object | 
 | targetStereotype   |123596 | non-null |  object | 
 | dataSource   |      123596 | non-null |  object | 
 | tier 1 |            123596 | non-null |  object | 
 | tier 2 |            123596 | non-null |  object | 
 | tier 3 |            123596 | non-null |  object | 


### Number of instances per model and per NLE tier type

| base_model                |   tier 1 |   tier 2 |   tier 3 |
|:--------------------------|---------:|---------:|---------:|
| Falcon3-10B-Instruct-Q8_0 |    30899 |    30899 |    30899 |
| Gemma-3-27b-it-Q4_0       |    30899 |    30899 |    30899 |
| Phi4-14B-Q8_0             |    30899 |    30899 |    30899 |
| Qwen3-14B-Q8_0            |    30899 |    30899 |    30899 |

### Statistics of `is_offensive` annotation.

|       |   is_offensive |
|:------|---------------:|
| mean  |       0.532562 |
| std   |       0.457962 |
| min   |       0        |
| 25%   |       0        |
| 50%   |       0.5      |
| 75%   |       1        |
| max   |       1        |

### Instance sample example

```json
{
 "base_model": "Qwen3-14B-Q8_0",
 "set": "train",
 "post": "just like girls can't be a hoe.... guys can't hit a girl back... it's a double standard that will forever exist....",
 "is_offensive": 0.75,
 "targetMinority": "['women']",
 "targetCategory": "['gender']",
 "targetStereotype": ["are all hoes", "deserve to be hurt", "should be called hoes", "should be hit if they hit first"],
 "dataSource": "t/davidson",
 "tier 1": "The statement implies that there is an unfair double standard between how men and women are treated in relationships, specifically regarding behavior like being 'a hoe' or defending oneself by hitting back. This can be offensive because it generalizes people based on gender, reinforces harmful stereotypes, and suggests that women are judged more harshly for similar actions than men, which perpetuates inequality.",
 "tier 2": "The statement reinforces harmful stereotypes by implying that girls are judged harshly for certain behaviors while boys are not held to the same standards, which perpetuates inequality and disrespect. It also suggests that men should not defend themselves, which can enable harmful behavior. These ideas contribute to a culture of sexism and are therefore offensive.",
 "tier 3": "The statement reinforces harmful stereotypes about women, implying they are 'all hoes' and suggesting they 'deserve to be hurt' or 'should be hit if they hit first.' This perpetuates a double standard that unfairly targets women, reinforcing gender-based prejudice and violence. It is offensive because it dehumanizes and justifies mistreatment based on gender."
 }
```

# References

## Harm-reference

```
@inproceedings{vecchi-etal-2026-harm,
    title = "{HARM}: Learning Hate-Aware Reward Model for Evaluating Natural Language Explanations of Offensive Content",
    author = "Vecchi, Lorenzo Puppi  and
      Jr., Alceu De Souza Britto  and
      Paraiso, Emerson Cabrera  and
      M. O. Cruz, Rafael",
    editor = "Demberg, Vera  and
      Inui, Kentaro  and
      Marquez, Llu{\'i}s",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EACL} 2026",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-eacl.230/",
    pages = "4393--4431",
    ISBN = "979-8-89176-386-9",
    abstract = "Explaining why content is hateful using natural language is crucial for fostering transparency in automated content moderation systems. However, evaluating the quality of such explanations remains an open challenge. General-purpose reward models (RMs), commonly used for scoring natural language outputs, are typically optimized for broad notions of safety. We argue that this optimization penalizes situations where references to stereotypes or offensive content are essential for explanations with higher explanatory fidelity. To address this gap, we introduce SBIC-Explain, a human-validated dataset of 370,788 LLM generated NLEs for offensive content, spanning three levels of human-annotated contextual richness: Tier 1: text-only, Tier 2: + classification-aware, and Tier 3: + semantics-informed. We hypothesize that as human-annotated context increases, explanations should lead to higher perceived explanations with higher explanatory fidelity. Yet, we find that existing RMs systematically assign lower scores to more contextually rich (and often more offensive) explanations, revealing a misalignment between model preferences and explanatory fidelity for this context. We propose HARM (Hate-Aware Reward Model), a RM that integrates interpretable signals to better align reward scores with the needs of hate speech explanation. HARM outperforms general-purpose baselines, improving NLE pair-wise preference. Available at: https://github.com/Lorenzo815/HARM."
}
```

## Original SBIC-reference

```
@inproceedings{sap-etal-2020-social,
    title = "Social Bias Frames: Reasoning about Social and Power Implications of Language",
    author = "Sap, Maarten  and
      Gabriel, Saadia  and
      Qin, Lianhui  and
      Jurafsky, Dan  and
      Smith, Noah A.  and
      Choi, Yejin",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.486",
    doi = "10.18653/v1/2020.acl-main.486",
    pages = "5477--5490",
    abstract = "Warning: this paper contains content that may be offensive or upsetting. Language has the power to reinforce stereotypes and project social biases onto others. At the core of the challenge is that it is rarely what is stated explicitly, but rather the implied meanings, that frame people{"}s judgments about others. For example, given a statement that {``}we shouldn{"}t lower our standards to hire more women,{""} most listeners will infer the implicature intended by the speaker - that {``}women (candidates) are less qualified.{""} Most semantic formalisms, to date, do not capture such pragmatic implications in which people express social biases and power differentials in language. We introduce Social Bias Frames, a new conceptual formalism that aims to model the pragmatic frames in which people project social biases and stereotypes onto others. In addition, we introduce the Social Bias Inference Corpus to support large-scale modelling and evaluation with 150k structured annotations of social media posts, covering over 34k implications about a thousand demographic groups. We then establish baseline approaches that learn to recover Social Bias Frames from unstructured text. We find that while state-of-the-art neural models are effective at high-level categorization of whether a given statement projects unwanted social bias (80{\%} F1), they are not effective at spelling out more detailed explanations in terms of Social Bias Frames. Our study motivates future work that combines structured pragmatic inference with commonsense reasoning on social implications.",
}
```