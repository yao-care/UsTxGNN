---
layout: default
title: Loteprednol Etabonate
parent: Model Prediction Only (L5)
nav_order: 873
evidence_level: L5
indication_count: 10
monitor_inn: "LOTEPREDNOL ETABONATE"
predicted_indications: ["conjunctival folliculosis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "pseudomembranous conjunctivitis", "Angelucci syndrome", "acute hemorrhagic conjunctivitis", "rosacea conjunctivitis", "acute contagious conjunctivitis", "otitis externa"]
last_modified_at: 2026-10-14
description: "Loteprednol Etabonate: predicted new indication Conjunctival folliculosis (evidence level L5). Approved use: Uveitis and other ocular inflammatory conditions (including atopic…"
---

# Loteprednol Etabonate
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

# Loteprednol Etabonate: From Allergic and Inflammatory Eye Disease to Conjunctival Folliculosis

## One-Sentence Summary

Loteprednol etabonate is a topical corticosteroid originally used for inflammatory and allergic eye conditions such as uveitis, atopic and vernal conjunctivitis, and rosacea.
The TxGNN model predicts it may be effective for **conjunctival folliculosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uveitis and other ocular inflammatory conditions (including atopic, vernal and papillary conjunctivitis) |
| Predicted New Indication | Conjunctival folliculosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 14 (NDA and ANDA entries combined; all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, loteprednol etabonate is a topical corticosteroid with anti-inflammatory activity. Its efficacy in allergic and inflammatory conjunctival disease (atopic, vernal and papillary conjunctivitis) is established, so it may be mechanistically applicable to other conjunctival conditions.

However, the mechanistic rationale for conjunctival folliculosis is weak. Folliculosis is generally a benign, often non-inflammatory follicular change, so an anti-inflammatory steroid has little to treat. The high TxGNN score is most likely driven by the condition's proximity to approved conjunctival indications in the knowledge graph rather than by any biological evidence.

Other top-ranked predictions are also conjunctival conditions (serous conjunctivitis, chronic follicular conjunctivitis, parasitic conjunctivitis, pseudomembranous conjunctivitis, acute hemorrhagic conjunctivitis, rosacea conjunctivitis, acute contagious conjunctivitis). Many of these are infectious, where a steroid alone may worsen disease. Of the group, rosacea conjunctivitis is the most coherent extension, since rosacea and ocular inflammation are already among the original indications. It is rated "Research Question" at evidence level L4 (indirect, by indication adjacency).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction, conjunctival folliculosis. One indirectly related paper was retrieved for a lower-ranked prediction (pseudomembranous conjunctivitis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40638366](https://pubmed.ncbi.nlm.nih.gov/40638366/) | 2025 | Comparative study | Ocular Immunology and Inflammation | PCR-based comparison of topical ganciclovir, povidone-iodine, and combinations with loteprednol etabonate for viral load reduction in adenoviral conjunctivitis. Indirect context only; the role of loteprednol was not confirmed from the available data. |

## US Market Information

All 14 US authorizations are cancelled. Main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020583 | LOTEMAX | Suspension/drops | Not available |
| NDA020803 | Loteprednol etabonate | Suspension/drops | Not available |
| NDA200738 | Lotemax | Ointment | Not available |
| NDA202872 | Loteprednol etabonate | Gel | Not available |
| NDA208219 | Lotemax SM | Gel | Not available |

The remaining entries are generic (ANDA) applications from Amneal, Armas, NorthStar, Padagis and Lupin, in suspension/drops, suspension, and gel forms.

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not taken from label text): ocular hypertension, glaucoma, herpes simplex virus keratitis, fungal eye infection, viral eye infection, ocular tuberculosis, and ophthalmic herpes zoster.
- **Drug Interactions**: 30 potential interactions were recorded, none with a severity grade. Examples include pantoprazole, doxycycline, omeprazole, triamcinolone, prednisone, simvastatin, warfarin, clopidogrel, hydroxychloroquine and ibuprofen. Clinical significance cannot be judged from this data.
- **Relevance to the predictions**: Several predicted indications are infectious (parasitic, viral, acute contagious conjunctivitis). These overlap with the contraindicated infection types above, and steroids may worsen or prolong infection.

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for conjunctival folliculosis rests on model score alone (L5). There are no trials or literature, the condition is largely benign and non-inflammatory, and all US licenses are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical rationale for treating folliculosis, or a pivot to a better-supported candidate such as rosacea conjunctivitis
- Confirmation of whether any valid US marketing authorization exists or would need to be re-established
- Route and formulation compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

