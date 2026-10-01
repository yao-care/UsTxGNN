---
layout: default
title: Cantharidin
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 1
---

# Cantharidin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Cantharidin: From an Unspecified Original Indication to Amenorrhea

## One-Sentence Summary

Cantharidin is marketed in the US as a topical solution (YCANTH), but the supplied data does not list its approved indication.
The TxGNN model predicts it may be effective for **Amenorrhea**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the supplied data |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records carry the same number, NDA212905) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. No original indication is recorded in the supplied data either, so the TxGNN score of 0.994 cannot be traced to a specific pathway.

For context only (this is general background, not from the supplied data): cantharidin is generally known as a protein phosphatase 2A/1 (PP2A/PP1) inhibitor and a topical vesicant. Its marketed use is dermatologic, for example molluscum contagiosum. No link has been established from PP2A/PP1 inhibition to menstrual regulation or the hypothalamic-pituitary-ovarian axis.

Systemic cantharidin is also highly toxic, causing renal and gastrointestinal injury. This makes any systemic gynecologic use implausible without new evidence. At this stage the prediction should be treated as a model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212905 | YCANTH (Verrica Pharmaceuticals Inc.) | Solution (topical/other route) | Not listed in the supplied data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no literature, no mechanism data, and no plausible mechanistic link. Systemic toxicity also argues against systemic gynecologic use, so there is no basis to advance the candidate.

**To proceed, the following is needed:**
- The FDA package insert (approved indication, warnings, contraindications), which is currently a blocking gap
- Mechanism of action data (e.g., from DrugBank), followed by a mechanistic analysis linking it to amenorrhea
- Preclinical or mechanistic evidence for a pathway to menstrual or hypothalamic-pituitary-ovarian regulation
- A route and toxicity assessment showing that any relevant exposure would be safe, given that the marketed product is topical
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

