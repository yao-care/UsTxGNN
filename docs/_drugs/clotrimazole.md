---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: predicted new indication Acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Clotrimazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is a topical azole antifungal marketed in the United States as creams. The TxGNN model predicts it may be useful for **acne (disease)**, but the evidence is thin: the only related study is **1 suspended clinical trial** of a three-drug combination cream, and **no publications** were found. The evidence level is **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 24 of 43; OTC monograph / unapproved listings: 158) |
| Number of FDA Applications | 43 (active: 24) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Clotrimazole belongs to the azole antifungal class, which inhibits fungal CYP51 and so disrupts the fungal cell membrane. It also has some anti-inflammatory activity.

The suggested link to acne is indirect. Colonisation by *Malassezia* or *Candida* has been proposed as a contributor to acne-like folliculitis, so an antifungal could in theory help in that subset of cases. This is a hypothesis only. The one registered trial tested a fixed combination of beclomethasone, gentamicin and clotrimazole, so any effect cannot be attributed to clotrimazole alone.

The very high TxGNN score is not backed by clinical or published evidence and should be treated as a computational signal, not as proof of benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a combination cream (beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1%) in contaminated dermatosis with bilateral symmetrical lesions. No results available; the combination design cannot isolate a clotrimazole effect. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA072641 | Clotrimazole | Cream | Sun Pharmaceutical Industries, Inc. | Valid |
| M005 | Clotrimazole | Cream | Proficient Rx LP | Valid |
| ANDA072640 | Clotrimazole | Cream | Sun Pharmaceutical Industries, Inc. | Valid |
| ANDA078338 | Clotrimazole | Cream | E. Fougera & Co. (Fougera Pharmaceuticals Inc.) | Valid |

The list may be partial.

---

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

- **Drug Interactions**: 100 interactions were found in total. Examples by severity:
  - Major: fentanyl, alfentanil, amiodarone, hydrocodone
  - Moderate: abemaciclib, paclitaxel, acalabrutinib, nifedipine, levonorgestrel, estradiol, alprazolam, apixaban, aprepitant
  - Minor: dolutegravir, amphotericin B

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No completed study tests clotrimazole in acne. The only trial is a suspended study of a combination cream, and there is no published literature. The evidence level is L5, and the high TxGNN score alone does not justify moving forward.

**To proceed, the following is needed:**
- Controlled studies of clotrimazole alone in acne, or in acne-like folliculitis with confirmed *Malassezia* involvement
- Mechanism-of-action data to clarify how an antifungal could act in acne
- Package insert safety information (warnings and contraindications)
- Review of the drug interaction profile for the intended patient population

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

