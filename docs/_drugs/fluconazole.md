---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 1
---

# Fluconazole
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

# Fluconazole: From Antifungal Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an azole antifungal that is widely marketed in the United States.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (fluconazole is an antifungal) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Fluconazole is known to inhibit fungal lanosterol 14-alpha-demethylase (CYP51), which blocks the synthesis of fungal cell membrane ergosterol.

The link between this mechanism and the predicted indication is weak. Punctate epithelial keratoconjunctivitis is most often adenoviral or otherwise non-fungal, so an antifungal mechanism has no clear target. The high TxGNN score (0.992) likely reflects knowledge-graph proximity to ocular or antifungal-related nodes rather than real pharmacological rationale.

Because the original indications are also missing from the input, the prediction cannot be checked against known drug biology. It should be treated as an unvalidated, low-plausibility hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The source data lists 20 authorizations in total; the five main ones are shown below. Approved indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Approved Indication |
|---------|------|------|------|-----------|
| ANDA078764 | Fluconazole | Injection | Hikma Pharmaceuticals USA Inc. | Not listed |
| ANDA076658 | Fluconazole | Tablet | Cardinal Health 107, LLC | Not listed |
| ANDA077731 | Fluconazole | Tablet | Sportpharm LLC | Not listed |
| ANDA078698 | Fluconazole | Injection | Hikma Pharmaceuticals USA Inc. | Not listed |
| ANDA078423 | Fluconazole | Tablet | Golden State Medical Supply, Inc. | Not listed |

Available dosage forms include oral tablets, injections (including injection solutions), and powder for suspension. No ophthalmic (topical eye) formulation appears in the data.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). No clinical trials or literature support it, and the antifungal mechanism does not plausibly match a mostly non-fungal condition.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank and the original approved indications
- A literature and trial search for fluconazole in punctate epithelial keratoconjunctivitis and fungal keratitis
- An assessment of route compatibility, since the marketed forms are oral and injectable and no ophthalmic formulation is listed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

