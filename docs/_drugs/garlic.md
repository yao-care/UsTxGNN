---
layout: default
title: Garlic
parent: 僅模型預測 (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
---

# Garlic
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

# Garlic (DB10532): From No Approved Indication to Gastrin Secretion Abnormality

## One-Sentence Summary

Garlic (INN: GARLIC, DrugBank DB10532) has no approved drug indication and is not marketed as a licensed pharmaceutical in Taiwan — it is tracked here as a botanical/dietary substance. The TxGNN model's top-ranked prediction is **Gastrin Secretion Abnormality** (score 99.96%), but this candidate is currently supported by **zero clinical trials** and **zero publications** — it is a pure knowledge-graph prediction with no mechanistic or empirical backing yet.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — garlic has no approved drug indication in this evidence pack |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for garlic is not currently available in DrugBank, and there is no approved original indication on file — garlic is not marketed as a regulated drug product in Taiwan (0 licenses) and appears to be tracked here as a dietary/botanical substance rather than a conventional pharmaceutical. As general background, garlic (*Allium sativum*) contains organosulfur compounds (allicin, diallyl sulfide, S-allyl cysteine) with known antioxidant, anti-inflammatory, and cardiovascular effects, which is why it surfaces across many TxGNN predictions in this pack.

For the top-ranked candidate specifically — Gastrin Secretion Abnormality — the model's own rationale field states plainly that there is no clinical trial or literature support and no mechanistic hypothesis linking garlic to gastrin regulation; the prediction rests solely on knowledge-graph pattern similarity (rank 1549 among candidates). No plausible pharmacological pathway connecting garlic's known organosulfur activity to gastrin secretion is documented anywhere in this evidence pack. This should be treated as hypothesis-generating only, not as a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Garlic is not marketed as an approved drug product in Taiwan — `taiwan_regulatory.total_licenses = 0` and no license records exist. There is no NDA, approved dosage form, or approved-indication text to report.

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interaction data) is available for garlic in this evidence pack — the DDI query returned `not_found`. Please refer to the package insert for safety information, if and when one becomes available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gastrin Secretion Abnormality) has no clinical, literature, or mechanistic support — it is a raw model score only (L5), and two Blocking/High-severity data gaps remain open: TFDA label/warning data (DG001, Blocking) and MOA data (DG002, High). There is no basis to advance this candidate past S0.

**To proceed, the following is needed:**
- Mechanism-of-action data for garlic (DrugBank query)
- TFDA label/warning and contraindication data (Blocking gap, DG001)
- Any preclinical or mechanistic hypothesis linking garlic to gastrin secretion, before further evidence collection is prioritized

**Note on other candidates in this pack:** This evidence pack (`TW-DB10532-multi`) contains 9 additional TxGNN-ranked candidates beyond the top prediction, with meaningfully different evidence profiles — notably *cerebral infarction* (rank 3, L4, 13 animal-model publications, staged at S1 "Research Question") and *HIV infectious disease* (rank 8, 3 trials + 20 publications, staged at S1 but recommended **Hold** because the literature documents garlic as a CYP3A4 inducer that reduces protease-inhibitor levels, e.g. saquinavir and darunavir — a known interaction risk, not a treatment benefit). If garlic repurposing work continues, those two candidates warrant separate evaluation rather than default reliance on the top TxGNN score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

