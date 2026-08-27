---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 657
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor (AR) antagonist originally developed for prostate cancer, most notably castration-resistant prostate cancer (mCRPC). The TxGNN model's top-ranked prediction points to **Prostate Cancer/Brain Cancer Susceptibility** — a hereditary predisposition phenotype rather than an active malignancy — and this prediction currently has **0 clinical trials** and **0 publications** supporting it, despite a high raw similarity score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate Cancer (mCRPC) — no formal indication text is provided in this data pack; inferred from associated trial evidence elsewhere in the pack |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002, High severity). Based on known information, enzalutamide is an androgen receptor (AR) signaling inhibitor in the class of second-generation antiandrogens; its efficacy in prostate cancer is well established — this pack itself contains extensive castration-resistant prostate cancer (mCRPC) trial evidence under the related "male reproductive organ cancer" indication entry (rank 6, L2 evidence, Proceed with Guardrails).

The top-ranked prediction evaluated here, however, is different in kind: "Prostate Cancer/Brain Cancer Susceptibility" describes a hereditary predisposition phenotype, not an active tumour. Per the evidence pack's own rationale, this phenotype has no direct pharmacological relationship to AR antagonism — the prediction reflects TxGNN graph-similarity scoring only (score 99.71%, model rank 7808), with zero clinical trial or literature evidence of any kind attached to it.

In short, the high raw prediction score should not be read as clinical relevance. This candidate sits at evidence level L5 (model prediction only, no actual studies) and decision stage S0 — it is a hypothesis generated purely from knowledge-graph similarity, with no mechanistic or empirical corroboration currently available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Androgen Receptor Signaling Inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This top-ranked candidate (Prostate Cancer/Brain Cancer Susceptibility) has no clinical trial or literature support and rests entirely on TxGNN graph-similarity scoring (L5, decision stage S0). A blocking data gap — missing TFDA label warnings/contraindications (DG001) — also prevents any safety pre-screening. Note that a lower-ranked candidate in this same pack, "male reproductive organ cancer" (rank 6), is far better evidenced (L2, Proceed with Guardrails) and may warrant separate evaluation.

**To proceed, the following is needed:**
- TFDA/label prescribing information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action detail — currently a High-priority data gap
- Any preclinical or mechanistic evidence specifically linking AR antagonism to hereditary prostate/brain cancer susceptibility, since none currently exists
- If pursuing this drug's repurposing potential further, consider prioritizing the better-evidenced "male reproductive organ cancer" candidate instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

