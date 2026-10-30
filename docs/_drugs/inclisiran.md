---
layout: default
title: Inclisiran
parent: Model Prediction Only (L5)
nav_order: 794
evidence_level: L5
indication_count: 9
monitor_inn: "INCLISIRAN"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
last_modified_at: 2026-10-30
description: "Inclisiran: predicted new indication Potassium deficiency disease (evidence level L5). Approved use: Not recorded in the data compiled for this report"
---

# Inclisiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Inclisiran: From Hypercholesterolemia (Original Indication Not Recorded) to Potassium Deficiency Disease
{: .text-alpha }

## One-Sentence Summary

Inclisiran is a small interfering RNA (siRNA) that targets PCSK9 and is marketed in the US under the brand name LEQVIO. The TxGNN model (deep learning) predicts it may be effective for **potassium deficiency disease**, but **no clinical trials or publications** currently support this prediction. The score is a computational result from the TxGNN model only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, inclisiran is a PCSK9-targeting siRNA that lowers LDL-C by upregulating hepatic LDL receptors.

The prediction is difficult to justify mechanistically. There is no plausible link between hepatic PCSK9 silencing and potassium homeostasis. The very high TxGNN score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature were found.

The other top-ranked predictions show the same pattern. These include esophageal disease, atypical coarctation of aorta, several migraine subtypes, esophageal malformation, esophageal ulcer, and Raynaud disease. All are Evidence Level L5 with a "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials are registered for potassium deficiency disease.

For reference, two Phase 3 trials were mapped to a lower-ranked prediction (aortic malformation, rank 8). They appear to be pediatric familial hypercholesterolemia studies and are not direct evidence for that indication either. The mapping is likely an artifact of indication matching.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 60 | Inclisiran vs placebo, then open-label, in children 6 to <12 years with heterozygous familial hypercholesterolemia |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Inclisiran vs placebo, then open-label, in children 2 to <12 years with homozygous familial hypercholesterolemia |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA214012 (cancelled) | LEQVIO (Novartis Pharmaceuticals Corporation) | Injection, solution | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There is no mechanistic rationale, no relevant clinical trial, and no literature for potassium deficiency disease. The drug is marketed, with 1 valid licence of 1.

**To proceed, the following is needed:**
- Documented original indication and approved indication text from the FDA label
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, to assess any biological link to potassium homeostasis
- Any preclinical or clinical evidence supporting the predicted indication
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

