---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 1178
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sotalol: From Cardiac Arrhythmia to Sick Sinus Syndrome 2, Autosomal Dominant

## One-Sentence Summary

Sotalol is an oral antiarrhythmic that combines beta-blockade with potassium-channel blockade, and the retrieved literature describes its use in atrial fibrillation and ventricular arrhythmias.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** support this prediction.
The pack's mechanistic review suggests the link is likely a graph artifact and may carry a safety concern.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (indication text is empty) |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank in this pack. Based on the pack's own mechanistic review, sotalol combines beta-adrenergic blockade with class III potassium-channel blockade, which slows sinus rate and atrioventricular conduction.

Sick sinus syndrome is a disorder of sinus node function, typically causing slow or unstable heart rhythm. Sotalol's effects on sinus rate and conduction would more plausibly worsen this condition than treat it. Sotalol is generally cautioned or contraindicated in sick sinus syndrome without pacing, so the high score probably reflects knowledge-graph topology rather than biology.

Note that this sick sinus syndrome subtype is a hereditary channelopathy-related condition. A pharmacological link to sotalol could be considered only for symptomatic arrhythmia management, and that is not supported by any retrieved evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA207428 | Sotalol (Unichem Pharmaceuticals) | Tablet | Not stated in source data |
| ANDA075563 | Sotalol Hydrochloride (Proficient Rx) | Tablet | Not stated in source data |
| ANDA075563 | Sotalol Hydrochloride (A-S Medication Solutions) | Tablet | Not stated in source data |
| ANDA075500 | Sotalol Hydrochloride (Bryant Ranch Prepack) | Tablet | Not stated in source data |
| ANDA075563 | Sotalol Hydrochloride (Bryant Ranch Prepack) | Tablet | Not stated in source data |

The 20 licenses are all oral tablets, and the five above are a sample.

## Safety Considerations

- **Predicted-indication concern (from the pack's mechanistic review, not the label)**: Sotalol is generally cautioned or contraindicated in sick sinus syndrome without pacing, because it slows sinus rate and AV conduction.
- **Proarrhythmic risk**: QT prolongation and torsades de pointes.
- **Drug interactions**: No interactions were found in the DDI query.

Please refer to the package insert for the full warnings and contraindications, which were not available in this pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The pharmacology points toward possible harm rather than benefit in sinus node dysfunction.

**Other predicted indications in the pack:**
- **Stroke disorder (rank 4)** is the only prediction with a meaningful evidence base (L4, research question). It has indirect support through atrial fibrillation rhythm-control work, including the Phase 3 RCT NCT00007605 (n=706), but no trial uses stroke as an endpoint.
- **Manic bipolar affective disorder (rank 5)** has only safety and interaction literature, with no therapeutic support.
- **Wildervanck syndrome, sarcoglycanopathy, macrocephaly/dysmorphic facies syndrome and obsolete susceptibility to ischemic stroke** have no evidence and no plausible mechanism. The obsolete ischemic stroke entry should be merged into the stroke indication.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- A safety review of sotalol use in sinus node dysfunction and in patients without pacing
- If any indication is pursued, redirecting effort to the stroke question, which needs an endpoint-based evidence review

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

