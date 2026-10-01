---
layout: default
title: Loteprednol Etabonate
parent: Model Prediction Only (L5)
nav_order: 873
evidence_level: L5
indication_count: 10
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

# Loteprednol Etabonate: From Topical Ophthalmic Corticosteroid to Conjunctival Folliculosis

## One-Sentence Summary

Loteprednol etabonate is a topical corticosteroid marketed in the US as eye drops, suspension and gel. The regulatory data provided does not list its approved indication text.
The TxGNN model predicts it may be effective for **conjunctival folliculosis** with a very high score, but **0 clinical trials** and **0 publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available licence records (generally a corticosteroid for inflammatory eye conditions) |
| Predicted New Indication | Conjunctival folliculosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licences (includes ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Loteprednol is described elsewhere in the evidence as a glucocorticoid receptor agonist with anti-inflammatory activity. Its efficacy in inflammatory eye conditions is generally established, so it is mechanistically plausible for other conjunctival inflammatory conditions.

For conjunctival folliculosis, that reasoning is weak. Folliculosis is usually a benign, non-inflammatory finding, so a corticosteroid has little rationale and its risks are not justified. The high TxGNN score reflects a knowledge-graph association, not clinical support.

Steroids can also worsen unrecognized infection, so the etiology of any conjunctival condition must be established before use. A related point is that several of the top-10 predictions in this pack (parasitic, acute hemorrhagic and acute contagious conjunctivitis) are infectious, and steroid use there raises safety concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217484 | Loteprednol Etabonate | Suspension/drops | Amneal Pharmaceuticals NY LLC |
| ANDA207609 | Loteprednol Etabonate | Suspension/drops | Armas Pharmaceuticals Inc. |
| ANDA215933 | Loteprednol Etabonate | Suspension/drops | Armas Pharmaceuticals Inc. |
| NDA202872 | Loteprednol Etabonate | Gel | Bausch & Lomb Americas Inc. |
| ANDA212450 | Loteprednol Etabonate | Suspension/drops | NorthStar Rx LLC |

Five of 20 licences are shown. The records also list ointment and suspension forms.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or literature. Folliculosis is usually benign and non-inflammatory, so a corticosteroid is poorly justified.

Other predicted indications have slightly more support but are still weak:
- **Chronic follicular conjunctivitis**: two case reports, neither shown to involve loteprednol (L4, Research Question).
- **Pseudomembranous conjunctivitis**: one indirect adenoviral conjunctivitis study (L4, Hold).
- **Rosacea conjunctivitis**: no literature, but flagged as a Research Question.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation that conjunctival folliculosis is a condition that needs pharmacological treatment
- A targeted literature search for loteprednol in non-infectious follicular and rosacea-related conjunctivitis
- Etiology-based exclusion criteria (infectious causes) for any future study

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

