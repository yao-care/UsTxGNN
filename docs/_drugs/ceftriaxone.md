---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 508
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ceftriaxone: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic given by injection for bacterial infections. The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but this prediction has **0 clinical trials** and **0 publications** behind it and no plausible mechanism. It is most likely a graph-model artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (the approved indication text is empty in all listed licenses); ceftriaxone is a broad-spectrum injectable antibacterial |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not, based on the available information. Detailed mechanism of action data is not available in the DrugBank record. Ceftriaxone is a bactericidal beta-lactam that inhibits penicillin-binding proteins and bacterial cell wall synthesis. It has no known effect on serum viscosity or immunoglobulin burden, which are the core problems in polyclonal hyperviscosity syndrome.

The score of 0.994 is identical to that of hyperamylasemia (rank 2), which suggests a saturated, non-discriminative graph prediction. Ceftriaxone's high albumin binding is a pharmacokinetic property, not a treatment rationale.

Among the other TxGNN predictions for this drug, only **infectious otitis media** (rank 4) has a credible mechanistic link. Ceftriaxone covers the main pathogens (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*), and single-dose or 3-day IM regimens are an established use. This is closer to on-label or guideline use than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065169 | Ceftriaxone Sodium (Hospira, Inc) | Injection, powder, for solution | Not stated in source data |
| ANDA065169 | Ceftriaxone Sodium (Hospira, Inc) | Injection, powder, for solution | Not stated in source data |
| ANDA065169 | Ceftriaxone Sodium (Sandoz Inc) | Injection, powder, for solution | Not stated in source data |
| ANDA065169 | Ceftriaxone Sodium (Sandoz Inc) | Injection, powder, for solution | Not stated in source data |
| ANDA065342 | Ceftriaxone (Civica, Inc.) | Injection, powder, for solution | Not stated in source data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

Two pharmacokinetic and safety points from the mechanistic review are relevant to the predicted indications:
- Ceftriaxone is highly albumin-bound, so low albumin (as in congenital analbuminemia) raises the free fraction and would change dosing and safety considerations.
- Ceftriaxone is a known cause of biliary sludge and pseudolithiasis, which can raise pancreatic enzymes. This makes the hyperamylasemia prediction potentially backwards.

## Other Predicted Indications (for Context)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|------|
| 2 | Hyperamylasemia | 99.39% | L4 | Hold | Lab finding, not an infection; no therapeutic mechanism |
| 3 | Congenital analbuminemia | 99.37% | L5 | Hold | Likely knowledge-graph artifact |
| 4 | Infectious otitis media | 99.26% | L2 | Proceed with Guardrails | Supported by RCTs: [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) (1997, IM ceftriaxone vs oral TMP-SMZ) and [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) (2000, 1-day vs 3-day IM ceftriaxone) |
| 5 | Blood group incompatibility | 99.12% | L5 | Hold | Retrieved papers are keyword matches only |
| 6 | Suppurative otitis media | 99.02% | L4 | Research Question | Mostly microbiology surveys; limited *Pseudomonas* activity |
| 7 | Chronic otitis media | 99.01% | L4 | Research Question | No interventional trials; topical quinolones remain standard |

None of the three registered trials linked to otitis media (NCT01511107, NCT01272999, NCT02567825) evaluates ceftriaxone. They concern short-course antibiotic therapy, a vaccine and tympanostomy tubes, respectively.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (polyclonal hyperviscosity syndrome) has no trials, no literature and no plausible mechanism, so it should not be pursued. The only credible direction is infectious otitis media, which is essentially an existing use. It should be reserved for treatment failure or when oral therapy is not feasible, and it should follow antimicrobial stewardship and account for pneumococcal resistance.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the US licenses, to confirm whether otitis media is already on-label
- Confirmation of the phase and design of the comparative otitis media trials, since the evidence level is capped at L2
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

