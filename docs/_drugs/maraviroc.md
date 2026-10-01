---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 887
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist. The Evidence Pack lists no approved-indication text, but the drug is known as an HIV antiviral.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (general knowledge: CCR5-tropic HIV-1 infection) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Maraviroc is a CCR5 antagonist. Currently, detailed mechanism of action data is not available in the Evidence Pack, so this description comes from the candidate's rationale notes and general knowledge.

The provided data supports **no mechanistic link** between CCR5 and MEN syndromes (MEN1 or RET-driven disease). MEN syndromes are genetic tumour-predisposition disorders and are not obviously driven by chemokine signalling. The high TxGNN score (0.998) reflects a pattern found by the knowledge-graph model, not an established biological rationale. The score should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022128 | SELZENTRY (A-S Medication Solutions) | Film-coated tablet | Not listed |
| ANDA217880 | Maraviroc (Zydus Pharmaceuticals USA) | Film-coated tablet | Not listed |
| ANDA217114 | Maraviroc (i3 Pharmaceuticals) | Film-coated tablet | Not listed |
| ANDA217114 | Maraviroc (A2A Integrated Pharmaceuticals) | Film-coated tablet | Not listed |
| ANDA203347 | Maraviroc (Hetero Labs) | Film-coated tablet | Not listed |

The only listed route is oral.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction records were available in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials, no literature, and no supported CCR5–MEN mechanism. Maraviroc is already marketed, so supply is not a barrier, but there is nothing yet to justify further investment for this indication.

**To proceed, the following is needed:**
- A literature search for a biological link between CCR5/chemokine signalling and MEN pathology (MEN1 or RET), including preclinical data
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications, which are currently a blocking gap for safety screening
- A route and formulation compatibility assessment (currently oral tablets only)

Among the other top-10 predictions, **HER2-positive breast carcinoma** is the most biologically coherent. A preclinical study links autocrine CCL5 to trastuzumab resistance, and CCL5 signals through CCR5. It is still preclinical (L4) and does not test maraviroc directly. It may be a better candidate to pursue first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

