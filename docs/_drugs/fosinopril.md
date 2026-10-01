---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: From Its Marketed ACE-Inhibitor Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Fosinopril is an oral ACE inhibitor marketed in the US as generic tablets, but the supplied data do not list its approved indication text.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
This is a **model prediction only**: there are **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.87% (rank 3983) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are all ANDAs, i.e. generics) |
| Recommended Decision | Hold |

The original indication is not shown because the input has no original indications and every license's approved-indication text is blank.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fosinopril is an ACE inhibitor, so it blocks the renin-angiotensin-aldosterone system (RAAS). Malignant hypertension with renal injury is plausibly RAAS-driven, so the prediction is not implausible on its face. This link comes from the drug class, not from the supplied data.

There are several reasons for caution:
- Malignant hypertension is an acute emergency that usually needs parenteral therapy. An oral ACE inhibitor is unlikely to be a first-line option.
- ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis or stenosis in a solitary kidney. This matters for renovascular forms of malignant hypertension and would need explicit review.
- The TxGNN score is a knowledge-graph output with no clinical support behind it.

The other four predictions also have no trial evidence, and they are weaker still:
- **Malignant renovascular hypertension** (99.87%): plausible through RAAS, but with the same renal-safety concern.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.87%): no clear mechanistic link. ACE inhibitors are not established therapy for pulmonary hypertension.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.87%): 20 publications were retrieved, but they are general hypoxia biology papers (brain aging, HIF signaling, cancer, multiple sclerosis) and none studies fosinopril. They look like a keyword match and are not counted as evidence. Systemic vasodilation could also worsen ventilation-perfusion mismatch in hypoxic lung disease.
- **Braddock syndrome** (99.81%): no identifiable mechanistic link. The score is likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The first five of 20 licenses are listed below. Approved-indication text is blank for all of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077222 | Fosinopril Sodium | Tablet | Cipla USA Inc. |
| ANDA091163 | Fosinopril Sodium | Tablet | Aurobindo Pharma Limited |
| ANDA077222 | Fosinopril Sodium | Tablet | A-S Medication Solutions |
| ANDA205670 | Fosinopril sodium | Tablet | Bryant Ranch Prepack |
| ANDA077222 | Fosinopril Sodium | Tablet | Bryant Ranch Prepack |

All listed products are oral tablets. ANDA077222 appears three times because of repackagers.

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predictions are L5, with no trials, no drug-specific literature and no mechanism data. The class-based mechanistic link is plausible only for the two hypertension-related renal predictions. Even there, the acute setting, the likely need for parenteral therapy and the renal-artery-stenosis risk argue against advancing now.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A fosinopril-specific literature search (ACE inhibitors in malignant hypertension and hypertensive nephropathy)
- A safety review for renal artery stenosis and acute renal failure
- Confirmation of the original approved indications
- A route-compatibility assessment (oral tablet versus the parenteral therapy typically needed for malignant hypertension)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

