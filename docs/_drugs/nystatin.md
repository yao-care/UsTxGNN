---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 978
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-06
monitor_inn: "NYSTATIN"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: predicted new indication Disease of orbital region (evidence level L5). Approved use: Not recorded in the local data"
---

# Nystatin
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

## Nystatin: Disease of orbital region
{: .text-alpha }

## One-Sentence Summary

Nystatin is an antifungal medicine that is already marketed in the United States in several dosage forms.
The TxGNN model predicts it may be useful for **disease of orbital region**, but this is a computational prediction only.
The data compiled for this report contain **1 registered clinical trial** (which studies a different drug in a different eye condition) and **no publications** on this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Disease of orbital region |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 51 of 124) |
| Number of FDA Applications | 124 (active: 51) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nystatin are not available in the data compiled for this report. Nystatin is generally known as a polyene antifungal, which acts on fungal cell membranes.

No plausible mechanistic link to disease of orbital region was identified. The only trial returned for this prediction (NCT03178149) tests a different drug, ASP7317, in geographic atrophy secondary to age-related macular degeneration. That is a retinal disease, not an orbital one, so it is not evidence for nystatin. The high TxGNN score therefore remains an unsupported model output. No clinical or literature data currently connect nystatin to this condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | Recruiting | 42 | Dose-escalation safety study of ASP7317 in geographic atrophy secondary to age-related macular degeneration. It does not involve nystatin and is not about an orbital disease, so it appears to be a spurious retrieval and gives no support. |

## Literature Evidence

Currently no related literature available.

## US Market Information

The list below shows 5 of the 12 licences on record. The list may be partial. The licence records carry no indication text.

<!-- review:begin us-lic-20261112-nystatin-1 -->

> **Review correction (2026-11-12)**: Originally stated: "Eleven are valid and one is cancelled; the list may be partial." Removed: the number or status of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 124 FDA applications for this drug, 51 active and 73 discontinued; the Quick Overview shows the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261112-nystatin-1 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203621 | Nystatin | Suspension | Not available |
| ANDA062506 | Nystatin | Tablet, film coated | Not available |
| ANDA062225 | Nystatin | Cream | Not available |
| ANDA207767 | Nystatin | Ointment | Not available |
| ANDA208581 | Nystatin | Powder | Not available |

Across all records, the dosage forms include suspension, ointment, powder, film-coated tablet (oral) and cream (topical).

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 listed interacting drugs, none with a graded severity level. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, bortezomib, tramadol, lorazepam and pantoprazole.

No warnings or contraindications from the product label are available in the data compiled for this report. Please refer to the package insert for full safety information. Any use in or around the eye or orbit would need a separate safety assessment, because the existing formulations were not developed for that site.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There is no plausible mechanism, no relevant clinical trial and no publication linking nystatin to disease of orbital region. The one trial retrieved studies a different drug in a retinal disease.

**To proceed, the following is needed:**
- A plausible biological rationale, such as a specific fungal or infectious process in the orbit that nystatin could address
- Published preclinical or clinical data on nystatin in orbital disease
- Mechanism-of-action data and label warnings and contraindications for nystatin
- A formulation and route assessment for any use near the eye or orbit

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-12 | Corrected: "Eleven are valid and one is cancelled; the list may be partial" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

