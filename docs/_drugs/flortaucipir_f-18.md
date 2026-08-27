---
layout: default
title: Flortaucipir F-18
parent: 僅模型預測 (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
---

# Flortaucipir F-18
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Flortaucipir F-18: From Tau PET Imaging (Diagnostic Use) to Anaphylaxis

## One-Sentence Summary

Flortaucipir F-18 (Tauvid) is a radioactive diagnostic imaging agent used to visualize tau protein pathology in the brain via PET scan — it is not a therapeutic drug. The TxGNN model predicts a possible link to **Anaphylaxis**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the underlying evidence pack itself flags the association as likely model noise rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug is a non-therapeutic PET imaging tracer; see note below) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack). Based on the information that is available, Flortaucipir F-18 (brand name Tauvid) is a fluorine-18-labeled radiotracer that binds to tau neurofibrillary tangles in the brain, allowing PET-based quantification of tau pathology — most notably in the context of Alzheimer's disease diagnostic workups. It has no known pharmacodynamic activity as a treatment; its sole approved use is diagnostic imaging.

Given this, there is no established pharmacological pathway connecting Flortaucipir F-18 to anaphylaxis. Anaphylaxis is mediated by IgE-dependent mast cell/basophil degranulation and related immunologic cascades, none of which overlap with tau-binding radioligand chemistry. The evidence pack's own mechanistic assessment concurs: it explicitly characterizes this prediction as "likely noise arising from node proximity in the knowledge graph," lacking biological plausibility.

This pattern repeats across all 10 top-ranked TxGNN predictions for this drug (anaphylaxis, food-dependent exercise-induced anaphylaxis, hairy cell leukemia and its variant, hereditary neurocutaneous angioma, placental hemangioma, pseudoallergy, skin disease, primary bone lymphoma, and early T-cell progenitor ALL) — none have any supporting clinical trials or literature, and each rationale independently concludes there is no credible mechanistic link to a radiodiagnostic tau-imaging agent. Taken together, this suggests the model outputs for this drug should be treated with strong methodological caution rather than as a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorizations on file — Flortaucipir F-18 currently holds "Not Marketed" status in this dataset (0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are all flagged as data gaps in this evidence pack — including a Blocking-severity gap for TFDA label warnings/contraindications, which prevents this candidate from advancing past initial safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 (model-prediction-only) candidate with no clinical trial or literature support, and the drug itself is a diagnostic radiotracer with no established therapeutic pharmacology — the evidence pack's own mechanistic analysis assesses the anaphylaxis link (and all 9 other top-ranked predictions) as biologically implausible, most likely a knowledge-graph proximity artifact rather than a true signal. Additionally, a Blocking-severity data gap on TFDA label warnings/contraindications independently prevents this candidate from entering safety evaluation regardless of the efficacy question.

**To proceed, the following is needed:**
- Original mechanism of action (MOA) data from DrugBank or the manufacturer's prescribing information, to properly evaluate any biological rationale
- TFDA/FDA package insert warnings and contraindications (currently a Blocking data gap)
- Independent pharmacological or preclinical evidence connecting tau-PET radioligand chemistry to immunologic/oncologic/vascular pathways before any of the 10 predicted indications can be considered for further evaluation
- Given the consistent lack of plausibility across all top 10 predictions, consider deprioritizing this drug candidate in favor of TxGNN predictions with stronger mechanistic or evidentiary backing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

