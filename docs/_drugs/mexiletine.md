---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
---

# Mexiletine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mexiletine: From Ventricular Arrhythmia to Hypertrichosis

## One-Sentence Summary

Mexiletine is a Class Ib sodium-channel-blocking antiarrhythmic, historically used for ventricular arrhythmias and (off-label) myotonia/neuropathic pain. The TxGNN model predicts a possible signal for **Hypertrichosis (disease)**, but this is currently supported by **0 clinical trials** and **0 publications** — a pure model-derived score with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack's regulatory data (drug not marketed, no TFDA license record). Literature captured elsewhere in this pack confirms mexiletine's established use as a Class Ib antiarrhythmic for ventricular arrhythmias, and off-label for myotonia/neuropathic pain |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | Not marketed (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mexiletine is not available in this evidence pack (flagged as a High-severity data gap). Based on information present in the supporting literature for other candidates in this pack, mexiletine is a Class Ib sodium-channel blocker in the same pharmacological family as lidocaine, historically used for ventricular arrhythmias and, off-label, for myotonia and neuropathic pain.

For the top-ranked candidate specifically — Hypertrichosis — the model's own rationale states there is **no known mechanistic relationship**: "無已知機轉關聯，無臨床試驗與文獻支持，純為 TxGNN 模型預測分數" (no known mechanistic link, no clinical trial or literature support, purely a TxGNN model prediction score). Sodium-channel blockade has no established biological connection to hair follicle growth regulation, and no publication in this pack links mexiletine to hypertrichosis. This candidate should be treated as an unvalidated graph-embedding signal rather than a mechanistically grounded hypothesis.

Notably, other candidates in the same prediction set (not the subject of this report but visible in the underlying data) — headache disorder (L3) and migraine disorder (L4) — do have drug-specific literature (case series and cohort studies on mexiletine for headache/trigeminal autonomic cephalalgias), consistent with its known sodium-channel mechanism. Hypertrichosis has no such support.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No marketing authorization (NDA) records are available — mexiletine is currently **not marketed** (Not marketed) in this jurisdiction, with 0 total licenses on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction (Hypertrichosis) is Evidence Level L5 — a model score with zero supporting clinical trials or literature, and the model's own rationale identifies no plausible mechanistic link between sodium-channel blockade and hair growth. There is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA warning/contraindication data for mexiletine (currently a Blocking data gap — required before any S1 safety screening)
- Verified mechanism of action (MOA) data from DrugBank or equivalent source (currently a High-severity data gap)
- Preclinical or mechanistic studies specifically linking sodium-channel blockade to hair follicle/hypertrichosis pathways, if this candidate is to be pursued further
- Consider evaluating alternative candidates from the same TxGNN run with stronger drug-specific literature support — headache disorder (L3, Research Question) and migraine disorder (L4, Research Question) both have published case series/cohort data on mexiletine — as separate, higher-priority repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

