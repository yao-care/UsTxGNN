---
layout: default
title: Latanoprostene Bunod
parent: 僅模型預測 (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Latanoprostene bunod (marketed elsewhere as Vyzulta) is a nitric-oxide-donating prostaglandin analog originally used for open-angle glaucoma and ocular hypertension. TxGNN's top-ranked prediction for this drug is **Visceral Calciphylaxis**, with a **99.76%** statistical score, but currently **zero clinical trials and zero publications** support this direction — and the evidence pack itself notes no known mechanistic overlap between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in official license data for this drug in this dataset; drug is pharmacologically known as an IOP-lowering agent (open-angle glaucoma / ocular hypertension) per contextual notes elsewhere in this evidence pack |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.76% (global rank 6635) |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 licenses recorded in this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug record. Based on context elsewhere in this evidence pack, latanoprostene bunod is metabolized into latanoprost acid (an FP-receptor agonist that increases uveoscleral outflow) and butanediol mononitrate (an NO donor that relaxes the trabecular meshwork to increase trabecular outflow) — this is the approved mechanism behind its use in open-angle glaucoma/ocular hypertension.

Calciphylaxis, however, is a small-vessel calcification and thrombotic-ischemic disease driven primarily by calcium-phosphate metabolism and vascular smooth muscle mineralization. There is no established pharmacological link between prostaglandin FP-receptor agonism or localized NO release and the pathways that drive vascular calcification. The evidence pack's own rationale for this prediction states explicitly that no mechanistic or clinical link is currently known — this candidate is a pure TxGNN statistical output (L5, decision stage S0), not a mechanistically or clinically supported hypothesis.

It is worth noting that other, lower-ranked predictions in this pack (e.g., primary hereditary glaucoma at rank 2, and vascular disease at rank 6, which has supporting clinical trial and literature evidence) have a substantially stronger evidentiary and mechanistic basis than the top-ranked candidate presented here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No license records are currently available for this drug in this dataset.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by the TxGNN model's statistical score — there are no clinical trials, no literature, and no established mechanistic pathway linking this drug's known pharmacology to visceral calciphylaxis. The evidence pack's own analysis concludes there is no known mechanistic intersection.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action documentation for the drug (currently unavailable, flagged as a high-severity data gap)
- FDA/TFDA label warnings and contraindications (currently unavailable, flagged as a blocking data gap for any safety screening)
- Preclinical or mechanistic studies specifically linking NO-donor/prostaglandin pathways to vascular calcification biology, if this direction is to be pursued further
- Consider prioritizing better-supported candidates from this same prediction set instead — notably "primary hereditary glaucoma" (L2, Proceed with Guardrails) and "vascular disease" (L3, supported by 2 clinical trials and 1 publication), which have materially stronger evidence bases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

