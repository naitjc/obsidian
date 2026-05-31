import re
from typing import Any, Dict, List, Tuple


VALID_NORM_MODES = {"minimal", "hybrid"}


def ensure_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        out = []
        for item in value:
            if item is None:
                continue
            s = str(item).strip()
            if not s or s.lower() == "none":
                continue
            out.append(s)
        return out
    if isinstance(value, str):
        s = value.strip()
        if not s or s.lower() == "none":
            return []
        if "," in s:
            parts = [p.strip() for p in s.split(",")]
            return [p for p in parts if p and p.lower() != "none"]
        return [s]
    return [str(value).strip()]


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def _normalize_mode(norm_mode: str) -> str:
    mode = (norm_mode or "minimal").strip().lower()
    if mode not in VALID_NORM_MODES:
        raise ValueError(f"norm_mode must be one of {sorted(VALID_NORM_MODES)}, got: {norm_mode}")
    return mode


def _singularize_token(token: str) -> str:
    if len(token) <= 3:
        return token
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith(("ses", "xes", "zes", "ches", "shes")) and len(token) > 4:
        return token[:-2]
    if token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def _normalize_target_label(value: str, norm_mode: str) -> str:
    x = _clean_text(value)
    if not x or x == "none":
        return ""
    mode = _normalize_mode(norm_mode)
    if mode == "minimal":
        return x

    x = x.replace("_", " ").replace("-", " ")
    x = re.sub(r"[^a-z0-9\s]", " ", x)
    x = _clean_text(x)
    toks = [_singularize_token(t) for t in x.split()]
    return " ".join(toks)


def _normalize_hate_label(value: str, norm_mode: str) -> str:
    x = _clean_text(value)
    if not x or x == "none":
        return ""
    mode = _normalize_mode(norm_mode)
    if mode == "hybrid":
        x = x.replace("_", " ").replace("-", " ")
        x = re.sub(r"[^a-z0-9\s]", " ", x)
        x = _clean_text(x)
        toks = [_singularize_token(t) for t in x.split()]
        x = " ".join(toks)
    return x.replace(" ", "_")


def normalize_targets(raw_targets: Any, norm_mode: str = "minimal") -> List[str]:
    targets = ensure_list(raw_targets)
    seen = set()
    result: List[str] = []
    for t in targets:
        canon = _normalize_target_label(t, norm_mode)
        if canon and canon not in seen:
            seen.add(canon)
            result.append(canon)
    return result


def normalize_hate_classes(raw_hate: Any, norm_mode: str = "minimal") -> List[str]:
    hates = ensure_list(raw_hate)
    out: List[str] = []
    seen = set()
    for h in hates:
        x = _normalize_hate_label(h, norm_mode)
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def normalize_class_label(raw_class: str) -> str:
    x = (raw_class or "").strip().lower().replace("-", "_")
    if x in {"not_toxic", "non_toxic"}:
        return "not_toxic"
    return "toxic"


def build_prompt(post: str) -> str:
    return (
        "You are given a post. Produce only one structured block [OUTPUT] with fields "
        "class, hate_class, and target.\n"
        "- class must be toxic or not_toxic\n"
        "- hate_class is a pipe-separated list or none\n"
        "- target is a pipe-separated list of canonical concepts or none\n"
        f"Post: {post}\n"
    )


def _join_or_none(items: List[str]) -> str:
    return "none" if not items else "|".join(items)


def build_think_text(hate_classes: List[str], targets: List[str]) -> str:
    unique_hate_labels = sorted(set(hate_classes))
    unique_target_labels = sorted(set(targets))

    return (
        "[THINK]\n"
        f"hate_labels: {_join_or_none(unique_hate_labels)}\n"
        f"target_labels: {_join_or_none(unique_target_labels)}\n"
        f"card: h={len(hate_classes)};t={len(targets)}\n"
        "link: h=>t\n"
        "[/THINK]\n"
    )


def build_output_text(class_label: str, hate_classes: List[str], targets: List[str]) -> str:
    return (
        "[OUTPUT]\n"
        f"class: {class_label}\n"
        f"hate_class: {_join_or_none(hate_classes)}\n"
        f"target: {_join_or_none(targets)}\n"
        "[/OUTPUT]"
    )


def parse_output_text(text: str, norm_mode: str = "minimal") -> Dict[str, Any]:
    raw = text or ""
    block_match = re.search(r"\[OUTPUT\](.*?)\[/OUTPUT\]", raw, flags=re.DOTALL | re.IGNORECASE)
    block = block_match.group(1) if block_match else raw

    class_label = "not_toxic"
    hate_classes: List[str] = []
    targets: List[str] = []

    for line in block.splitlines():
        ln = line.strip()
        if not ln or ":" not in ln:
            continue
        key, val = ln.split(":", 1)
        k = key.strip().lower()
        v = val.strip()
        if k == "class":
            class_label = normalize_class_label(v)
        elif k == "hate_class":
            if v.lower() != "none":
                hate_classes = normalize_hate_classes([x.strip() for x in v.split("|") if x.strip()], norm_mode=norm_mode)
        elif k == "target":
            if v.lower() != "none":
                targets = normalize_targets([x.strip() for x in v.split("|") if x.strip()], norm_mode=norm_mode)

    return {
        "class": class_label,
        "hate_class": hate_classes,
        "target": targets,
    }
