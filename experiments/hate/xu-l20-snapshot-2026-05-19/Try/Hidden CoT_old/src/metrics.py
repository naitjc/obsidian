from typing import Dict, List, Sequence, Set

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support
from sklearn.metrics.pairwise import cosine_similarity


def _to_set_list(items: Sequence[Sequence[str]]) -> List[Set[str]]:
    out: List[Set[str]] = []
    for x in items:
        out.append(set(x))
    return out


def jaccard_for_sets(y_true: Sequence[Sequence[str]], y_pred: Sequence[Sequence[str]]) -> float:
    true_sets = _to_set_list(y_true)
    pred_sets = _to_set_list(y_pred)
    scores = []
    for g, p in zip(true_sets, pred_sets):
        union = g | p
        if not union:
            scores.append(1.0)
        else:
            scores.append(len(g & p) / len(union))
    return float(np.mean(scores)) if scores else 0.0


def f1_for_sets(y_true: Sequence[Sequence[str]], y_pred: Sequence[Sequence[str]]) -> float:
    true_sets = _to_set_list(y_true)
    pred_sets = _to_set_list(y_pred)
    scores = []
    for g, p in zip(true_sets, pred_sets):
        if not g and not p:
            scores.append(1.0)
            continue
        tp = len(g & p)
        prec = tp / len(p) if p else 0.0
        rec = tp / len(g) if g else 0.0
        if prec + rec == 0:
            scores.append(0.0)
        else:
            scores.append(2 * prec * rec / (prec + rec))
    return float(np.mean(scores)) if scores else 0.0


def embedding_cosine_for_sets(y_true: Sequence[Sequence[str]], y_pred: Sequence[Sequence[str]]) -> float:
    if not y_true:
        return 0.0
    true_texts = [" ".join(sorted(set(x))) if x else "none" for x in y_true]
    pred_texts = [" ".join(sorted(set(x))) if x else "none" for x in y_pred]

    docs = true_texts + pred_texts
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
    mat = vectorizer.fit_transform(docs)
    half = len(true_texts)
    true_vec = mat[:half]
    pred_vec = mat[half:]
    sims = cosine_similarity(true_vec, pred_vec)
    diag = np.diag(sims)
    return float(np.mean(diag))


def _binarize_labels(y_true: Sequence[Sequence[str]], y_pred: Sequence[Sequence[str]]):
    labels = sorted({v for row in y_true for v in row} | {v for row in y_pred for v in row})
    idx = {v: i for i, v in enumerate(labels)}
    t = np.zeros((len(y_true), len(labels)), dtype=np.int32)
    p = np.zeros((len(y_pred), len(labels)), dtype=np.int32)
    for i, row in enumerate(y_true):
        for v in set(row):
            t[i, idx[v]] = 1
    for i, row in enumerate(y_pred):
        for v in set(row):
            p[i, idx[v]] = 1
    return t, p


def compute_class_metrics(y_true: Sequence[str], y_pred: Sequence[str]) -> Dict[str, float]:
    true_bin = [1 if x == "toxic" else 0 for x in y_true]
    pred_bin = [1 if x == "toxic" else 0 for x in y_pred]
    return {
        "accuracy": float(accuracy_score(true_bin, pred_bin)),
        "macro_f1": float(f1_score(true_bin, pred_bin, average="macro")),
    }


def compute_multilabel_metrics(y_true: Sequence[Sequence[str]], y_pred: Sequence[Sequence[str]]) -> Dict[str, float]:
    t, p = _binarize_labels(y_true, y_pred)
    if t.shape[1] == 0:
        return {
            "micro_f1": 1.0,
            "macro_f1": 1.0,
            "jaccard": 1.0,
        }
    micro_p, micro_r, micro_f1, _ = precision_recall_fscore_support(
        t, p, average="micro", zero_division=0
    )
    _ = (micro_p, micro_r)
    macro_f1 = f1_score(t, p, average="macro", zero_division=0)
    jaccard = jaccard_for_sets(y_true, y_pred)
    return {
        "micro_f1": float(micro_f1),
        "macro_f1": float(macro_f1),
        "jaccard": float(jaccard),
    }
