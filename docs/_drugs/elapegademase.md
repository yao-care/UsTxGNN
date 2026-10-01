---
layout: default
title: Elapegademase
parent: Model Prediction Only (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
---

# Elapegademase
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

# Elapegademase: From ADA-SCID to Diabetic Retinopathy

## One-Sentence Summary

Elapegademase (Revcovi) is a PEGylated adenosine deaminase enzyme replacement therapy. The Evidence Pack lists no approved-indication text, but public labeling identifies it for adenosine deaminase severe combined immunodeficiency (ADA-SCID).
The TxGNN model predicts it may be effective for **diabetic retinopathy**, but this is a model output only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADA-SCID (from public labeling; the Evidence Pack's indication text is empty) |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761092) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Based on known information, elapegademase is a systemic PEGylated enzyme that converts adenosine to inosine.

A link to diabetic retinopathy is conceivable but speculative. Adenosine signaling through A2A/A2B receptors is implicated in retinal angiogenesis and VEGF regulation. However, the direction of effect is unclear, because lowering adenosine could be either pro- or anti-angiogenic. A large PEGylated protein is also unlikely to reach the retina in meaningful amounts.

The other nine predictions are also eye conditions: severe nonproliferative diabetic retinopathy, diabetic cataract, and several cataract subtypes. They have near-identical scores (0.9937–0.9945), and several share exactly the same score. This points to knowledge-graph clustering around diabetic eye disease rather than independent signals. Severe nonproliferative diabetic retinopathy is a substage of the top prediction. The cataract predictions have no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761092 | Revcovi (Chiesi USA, Inc.) | Injection | Not listed in the Evidence Pack |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or publications. The mechanism is speculative, and ocular delivery of a large systemic enzyme is unaddressed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data, for example from DrugBank
- Preclinical evidence that adenosine deaminase replacement affects retinal angiogenesis or VEGF signaling
- An assessment of whether a systemic PEGylated enzyme can reach the retina, or whether an ocular route would be needed
- A literature and trial search for evidence linking adenosine metabolism to diabetic retinopathy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

