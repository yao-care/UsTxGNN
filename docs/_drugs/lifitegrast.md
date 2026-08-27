---
layout: default
title: Lifitegrast
parent: 僅模型預測 (L5)
nav_order: 860
evidence_level: L5
indication_count: 6
---

# Lifitegrast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lifitegrast: From Dry Eye Disease to Penile Fibromatosis

## One-Sentence Summary

Lifitegrast (Xiidra) is an LFA-1 antagonist originally approved for dry eye disease; it is not marketed in Taiwan.
The TxGNN model's top-ranked prediction for this drug is **Penile Fibromatosis (Peyronie's disease)**,
but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no mechanistic or clinical corroboration.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry Eye Disease (Xiidra) — not TFDA-approved; drug not marketed in Taiwan |
| Predicted New Indication | Penile Fibromatosis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal `original_moa` field for lifitegrast is a data gap. However, the evidence pack's own rationale text (attached to a different candidate indication) identifies lifitegrast as an LFA-1 (integrin αLβ2) antagonist that blocks the LFA-1/ICAM-1 interaction to suppress T-cell adhesion and activation — its only approved use being dry eye disease.

Penile fibromatosis (Peyronie's disease) is pathologically driven by TGF-β–mediated myofibroblast proliferation and fibrosis, a mechanism distinct from T-cell adhesion inhibition. The evidence pack explicitly states there is no known mechanistic link between LFA-1 antagonism and this fibrotic pathway.

Notably, the top four TxGNN predictions for this drug (penile fibromatosis, palmar fibromatosis, Ledderhose disease, infantile digital fibromatosis) all cluster in a narrow 0.9953–0.9959 score band. This pattern suggests the model is scoring based on a shared embedding for "fibromatosis"-type diseases as a class, rather than detecting a drug-specific signal — a strong indicator that this is model-artifact clustering rather than a genuine biological hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by any clinical trial, publication, or plausible mechanistic link — the drug's known LFA-1 pathway has no established connection to the TGF-β–driven fibrosis underlying Peyronie's disease, and the score pattern across related fibromatoses suggests a disease-class artifact rather than a drug-specific signal. This is L5/S0 evidence, the lowest tier in the framework.

**To proceed, the following is needed:**
- TFDA/FDA label data on warnings and contraindications (currently blocking — flagged as DG001, "Blocking" severity, preventing any S1 safety evaluation)
- Confirmed mechanism of action via DrugBank API (DG002)
- Preclinical or in-vitro evidence testing LFA-1/ICAM-1 pathway involvement in fibromatosis pathogenesis before any clinical evidence-generation is warranted
- Note: within this same evidence pack, rank 6 (diabetic retinopathy, score 99.03%) has an actual Phase 1/2 trial and 2 supporting publications, reaching L4/S1 ("Research Question") — that candidate has a materially stronger evidence base than this top-ranked one and may merit separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

