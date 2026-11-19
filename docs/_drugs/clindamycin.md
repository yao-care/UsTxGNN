---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 535
evidence_level: L5
indication_count: 6
monitor_inn: "CLINDAMYCIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-06
description: "Clindamycin: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). In the US: 141 FDA applications (85 active)"
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Clindamycin: Lincosamide antibacterial (protein synthesis inhibitor) → punctate epithelial keratoconjunctivitis (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## One-Sentence Summary

Clindamycin is a lincosamide antibacterial that is marketed in the United States in oral, injectable, and topical forms.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis** (score 0.9997), but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 85 of 141) |
| Number of FDA Applications | 141 (active: 85) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for clindamycin: "Clindamycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the ribosome. Clindamycin is bacteriostatic." ([DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a), label version 2026-09-16; accessed 2026-11-19.) Clindamycin belongs to the lincosamide class of antibacterials, which inhibit bacterial protein synthesis. Its activity is directed at bacteria, particularly Gram-positive organisms such as *Staphylococcus aureus* and anaerobes.

Punctate epithelial keratoconjunctivitis is usually inflammatory, viral (for example adenoviral), or related to toxicity or dry eye. A protein-synthesis-inhibiting antibacterial therefore has no clear mechanistic rationale, unless a bacterial component such as staphylococcal blepharokeratoconjunctivitis is present. Clindamycin is also not a standard ophthalmic agent, and none of the marketed forms listed in the data are ophthalmic preparations. The high score most likely reflects network similarity in the model rather than a demonstrated biological link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The US records compiled for this report list 14 licences, and the list may be partial. They cover oral capsules, granules for oral solution, injectable solutions, topical solutions, and topical creams. The records carry no approved-indication text. Main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050441 | CLEOCIN PHOSPHATE | Injection, solution | Not recorded |
| NDA050793 | Clindesse | Cream | Not recorded |
| ANDA065061 | Clindamycin hydrochloride | Capsule | Not recorded |
| ANDA207047 | Clindamycin palmitate hydrochloride | Granule, for solution | Not recorded |
| ANDA208084 | Clindamycin phosphate | Injection, solution | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The ones graded Moderate are:
  - balsalazide
  - clarithromycin
  - picosulfuric acid
  - attapulgite
  - kaolin

  Other listed partners, graded Unknown, include amphotericin B, aspirin, amoxicillin, vancomycin, and omeprazole.

No label warnings or contraindication text were available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest score among the listed candidates but no supporting trials or publications. Clindamycin has no clear mechanistic rationale for a largely viral or inflammatory eye condition, and it has no ophthalmic product on the US market.

**To proceed, the following is needed:**
- Evidence that a bacterial component contributes to this condition and that clindamycin is active against it
- Preclinical or clinical data on ocular delivery, tolerability, and efficacy
- Mechanism of action data and the package insert warnings and contraindications
- A feasible ophthalmic formulation and route of administration

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

