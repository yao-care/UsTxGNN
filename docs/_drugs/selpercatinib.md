---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 1153
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Selpercatinib: From RET Fusion-Positive NSCLC to Pulmonary Hypertension

## One-Sentence Summary

> Selpercatinib is a highly selective RET tyrosine kinase inhibitor, internationally approved for RET fusion/mutation-positive non-small-cell lung cancer (NSCLC) and thyroid cancer; it is not currently marketed in Taiwan.
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but this signal is currently supported by **zero clinical trials** and **zero directly relevant publications** — the two literature citations retrieved concern NSCLC safety/efficacy, not pulmonary hypertension.
> Two additional low-confidence predictions (migraine disorder, migraine with brainstem aura) carry no supporting evidence at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan licensing data (drug not marketed locally); per international approval, RET fusion/mutation-positive NSCLC and thyroid cancer |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently a data gap (DG002). Based on the available repurposing rationale, selpercatinib is a highly selective RET tyrosine kinase inhibitor, internationally approved for RET fusion/mutation-positive NSCLC and RET-driven thyroid cancers. Its efficacy in these oncology indications is well established through pivotal trials outside this evidence pack.

The link to pulmonary hypertension rests on a theoretical hypothesis: the RET/GDNF signaling axis has been associated with pulmonary vascular remodeling in some preclinical research. However, neither of the two retrieved publications addresses this pathway or pulmonary hypertension directly — both are NSCLC-focused (one comparing adverse-event profiles of RET inhibitors, the other a real-world efficacy analysis). This suggests the high TxGNN score likely arises from indirect "lung"-related node associations within the knowledge graph rather than substantive mechanistic or clinical evidence.

The two migraine-related predictions (ranks 2–3) rely on an even weaker hypothesis — RET's role in trigeminal sensory neuron signaling — with no literature or trial evidence whatsoever. These are noted for completeness but are not prioritized further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Cohort (AE profile) | Frontiers in Pharmacology | Compares adverse event profiles of pralsetinib vs. selpercatinib using FDA AERS data; safety-focused, no pulmonary hypertension relevance |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective analysis (NSCLC efficacy) | Therapeutic Advances in Medical Oncology | Real-world efficacy of selpercatinib in RET fusion-positive NSCLC (SIREN access program); no pulmonary hypertension relevance |

*Note: Both publications relate to the drug's original NSCLC indication, not the predicted pulmonary hypertension indication. No disease-specific evidence currently exists.*

---

## US Market Information

Selpercatinib is currently not marketed in Taiwan (0 licenses on record); no NDA/product data is available for review.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Selpercatinib is an antineoplastic agent (approved for RET fusion/mutation-positive NSCLC and thyroid cancer).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions — no TFDA toxicity data available (DG001) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | General class-level considerations for RET/TKI agents (liver function, blood pressure, QTc, CBC) — not confirmed against local labeling |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA labeling data (warnings/contraindications) is a blocking data gap (DG001) and safety cannot be evaluated until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is Evidence Level L5 (model prediction only) with no clinical trials and no disease-specific literature support; the retrieved publications relate to the drug's original NSCLC indication rather than pulmonary hypertension. Combined with a blocking gap in TFDA safety data (DG001), this candidate cannot proceed to safety evaluation (S1) at this time.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (resolve DG001)
- Confirmed mechanism of action data via DrugBank API (resolve DG002)
- Preclinical or mechanistic evidence directly linking RET inhibition to pulmonary vascular remodeling
- Monitoring for future trial registrations targeting pulmonary hypertension
- Re-evaluation of the migraine-related predictions only if any supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

