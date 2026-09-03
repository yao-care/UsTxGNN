---
layout: default
title: Plecanatide
parent: 僅模型預測 (L5)
nav_order: 1055
evidence_level: L5
indication_count: 10
---

# Plecanatide
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

# Plecanatide: Original Indication Not Documented → Predicted Link to Hypertrichosis (Low-Confidence)

## One-Sentence Summary

> Plecanatide (DrugBank DB13170) is described in the evidence pack as a locally-acting intestinal guanylate cyclase-C (GC-C) agonist with negligible systemic absorption, though its original approved indication is not documented in this evidence pack.
> The TxGNN model's top prediction links plecanatide to **hypertrichosis (excessive hair growth)**, with a prediction score of **99.998%**,
> but **zero clinical trials and zero literature records** support this specific pairing — the model's own accompanying rationale flags the result as likely noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no approved indication text available) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for plecanatide is not available in the structured `drug.original_moa` field. However, the mechanistic-link notes attached to every predicted indication in this pack consistently describe plecanatide as a **guanylate cyclase-C (GC-C) agonist acting locally on the intestinal epithelium**, with minimal systemic absorption — this is consistent with its known pharmacological class of GI-restricted secretagogues.

For the top-ranked prediction, hypertrichosis, the evidence pack's own rationale states there is **no known physiological pathway connecting intestinal GC-C/cGMP signaling to hair follicle growth regulation**, and explicitly characterizes the high TxGNN score as likely model noise rather than a biologically grounded signal. This pattern repeats across all ten top-ranked predictions in this pack (hypertrichosis subtypes, congenital malformation syndromes, hair shaft disorders, Dandy-Walker malformation, coronary artery dissection, vascular disease, thoracic outlet syndrome, pheochromocytoma) — none have a plausible mechanistic link to a drug whose action is confined to the gut lumen, and none are supported by clinical trials.

The one prediction with attached literature (rank 3, "malformation syndrome with odontal/periodontal component") returned 20 general periodontology papers that never mention plecanatide or GC-C signaling — a case of keyword co-occurrence rather than genuine drug-disease evidence. Overall, this evidence pack does not support a credible repurposing rationale for any of the top-10 candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No NDA or marketing authorization records were found for plecanatide in this evidence pack (`total_licenses: 0`, `market_status: 未上市/Not Marketed`). The drug does not currently appear to hold an active license in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/FDA-equivalent warning and contraindication data for plecanatide is flagged as a **Blocking** data gap (DG001) in this pack, meaning a formal safety assessment (S1 stage) cannot currently proceed without sourcing the official prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (hypertrichosis) has no clinical trial or literature support, and its own mechanistic rationale identifies it as probable model noise given plecanatide's GI-restricted mode of action. This pattern holds across all ten top-ranked predictions in the pack — none reach beyond L5 (model-only) evidence, and the drug has no market presence or NDA in this jurisdiction to build on.

**To proceed, the following is needed:**
- Source TFDA/FDA prescribing information (warnings, contraindications) — currently a Blocking gap preventing any safety evaluation
- Obtain formal mechanism-of-action documentation (e.g., via DrugBank API) to replace the current data gap
- Independently verify whether any biologically plausible indication exists among lower-ranked TxGNN candidates, since the current top-10 all lack mechanistic or evidentiary support
- Re-run evidence collection (clinical trials, PubMed) once a more mechanistically plausible candidate indication is identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

