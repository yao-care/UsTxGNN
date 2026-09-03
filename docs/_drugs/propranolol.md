---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 1092
evidence_level: L5
indication_count: 6
---

# Propranolol
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

# Propranolol: From Unrecorded Original Indication to Distal Myopathy, Tateyama Type

## One-Sentence Summary

> Propranolol's original approved indication and detailed mechanism of action are not recorded in this evidence pack (data gap).
> The TxGNN model's highest-ranked repurposing prediction is **Distal Myopathy, Tateyama Type**,
> but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale explicitly notes a lack of known biological plausibility for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no approved indication text on record) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for propranolol in this evidence pack (data gap, DG002). No original indication is on record either, so the historical drug–disease relationship that would normally anchor a repurposing rationale cannot be established from this dataset.

For the top-ranked prediction itself, the model's own generated rationale is explicit about the weakness of the link: **distal myopathy, Tateyama type** is a rare, RNA-metabolism–related hereditary skeletal myopathy. There is no known mechanistic intersection between this disease process and propranolol's β-adrenergic receptor blockade. The rationale text states the high TxGNN score "appears to lack biological plausibility support" — meaning this is a purely data-driven association from the knowledge graph, not one grounded in known pharmacology.

It is worth noting that several **lower-ranked** candidates in this evidence pack — particularly *cardiomyopathy* (rank 6) and *cirrhotic cardiomyopathy* (rank 5) — have substantially stronger mechanistic rationale (propranolol is an established treatment for hypertrophic obstructive cardiomyopathy and is used in cirrhotic portal hypertension) and real supporting literature/trial evidence. These may warrant separate evaluation rather than the top TxGNN-ranked candidate discussed here (see Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization records are available for this drug in this dataset. Market status is recorded as **Not Marketed**, with **0** total licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/FDA warnings and contraindications data is flagged as a Blocking data gap — DG001 — meaning this candidate cannot currently pass an initial safety screen, S1, without this information.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (distal myopathy, Tateyama type) has no supporting clinical trials or literature, and the model's own rationale flags weak biological plausibility. In addition, a blocking data gap (missing TFDA warnings/contraindications) prevents this candidate from proceeding to even an initial safety review.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required to clear the S1 safety gate (DG001, Blocking)
- Confirmed mechanism of action from DrugBank (DG002, High priority)
- Original approved indication(s) for propranolol, to establish a baseline for mechanistic comparison
- If pursuing this program, consider re-evaluating priority toward the better-evidenced candidates in this same pack — *cardiomyopathy* (L3, 3 trials + 20 publications, S2) and *cirrhotic cardiomyopathy* (L3, 5 publications, S1) — rather than the top TxGNN-score candidate, since evidence strength diverges significantly from score rank here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

