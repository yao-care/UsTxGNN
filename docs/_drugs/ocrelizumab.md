---
layout: default
title: Ocrelizumab
parent: Model Prediction Only (L5)
nav_order: 981
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Ocrelizumab: From Multiple Sclerosis to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody that depletes B cells and is marketed in the US for multiple sclerosis.
The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**,
but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (the license records provide no indication text) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both are BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ocrelizumab is a CD20-directed antibody that depletes B cells, and its efficacy in multiple sclerosis is established. Mechanistically, however, there is no clear reason for it to apply to breast cancer.

Breast carcinoma cells generally do not express CD20, so there is no direct target rationale. Any link would be indirect, for example through tumour-infiltrating B cells, and nothing in the provided evidence supports it.

The high score (0.9989) is a graph-based signal only. The same pattern appears in the other four predicted breast cancer subtypes:

- **Progesterone-receptor positive and normal breast-like subtypes:** both have an identical score (0.99813), which suggests one shared graph-neighbourhood signal rather than independent evidence.
- **Luminal A/B and progesterone-receptor negative subtypes:** none has any supporting clinical trial, and the only literature retrieved (for luminal A/B) is irrelevant.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

For the fourth-ranked prediction (breast tumor luminal A or B), 19 articles were retrieved. They appear to be keyword-matching noise on the letter "B" (B-cell biology, hepatitis B vaccines, HLA-B alleles, bacteriochlorophyll b). None concern ocrelizumab, anti-CD20 therapy or breast cancer, so they were not counted as evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA761053 | OCREVUS | Injection |
| BLA761371 | Ocrevus Zunovo | Injection, solution |

Both products are marketed by Genentech, Inc. The approved indication text was not provided in the records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature or clear mechanistic support (Evidence Level L5, stage S0). Breast carcinoma generally lacks the CD20 target, so the high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- The US package insert (warnings and contraindications), which is required before any safety screening
- Evidence that CD20-positive B cells or tumour-infiltrating B cells play a role in HER2-positive breast cancer, such as preclinical or translational studies
- A re-run of the literature search with drug-specific terms (ocrelizumab, anti-CD20 and breast cancer) to replace the noisy results
- Route compatibility assessment, currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

