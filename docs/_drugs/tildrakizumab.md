---
layout: default
title: Tildrakizumab
parent: Model Prediction Only (L5)
nav_order: 1228
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab (brand name ILUMYA) is an anti-IL-23 p19 monoclonal antibody marketed in the US. Its approved-indication text is blank in the Evidence Pack, so the plaque psoriasis indication in the title comes from public labeling, not from the pack.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are **0 clinical trials** and **0 publications** for this drug-disease pair.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the Evidence Pack (the license's approved indication text is empty). Plaque psoriasis per public labeling, not verified against the pack. |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761067) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Tildrakizumab is known to be an anti-IL-23 p19 monoclonal antibody, so it blocks the IL-23/IL-17 inflammatory axis. The pack lists no original indications, so the graph-based rationale cannot be cross-checked against them.

The hypothesis is that low-grade inflammation and cytokine signaling, including IL-17-related pathways, contribute to microvascular damage in the diabetic retina. Blocking IL-23 could therefore be relevant. A direct role for IL-23 blockade in diabetic retinopathy has not been established.

There are also practical concerns. Tildrakizumab is a large antibody given systemically, and no data on ocular delivery or retinal penetration were provided. The high TxGNN score is a model output, not evidence of efficacy or safety.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA 761067 | ILUMYA (Sun Pharmaceutical Industries, Inc.) | Injection, solution | Not provided in the source data |

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no warnings or contraindications, and the drug-interaction query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5), with no registered trials or retrieved literature. The mechanistic link is speculative, and ocular delivery of a systemic antibody is unaddressed.
Other predicted indications (diabetic retinopathy, diabetic cataract, drug-induced osteoporosis) are also L5 and on Hold. The diabetic cataract prediction has no plausible mechanistic path.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism-of-action data from DrugBank
- Preclinical or clinical evidence that IL-23/IL-17 inhibition affects diabetic retinopathy
- Data on retinal exposure or an ocular delivery strategy
- A literature and trial search for the drug-disease pair

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

