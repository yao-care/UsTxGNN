---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 1180
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Spironolactone: From Established Aldosterone-Antagonist Uses to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a marketed oral drug that blocks mineralocorticoid and androgen receptors. It is already used off-label for androgen-driven hair loss.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare hereditary hair loss disorder.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local regulatory records provided |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Spironolactone is known to act as an antagonist of both the androgen receptor and the mineralocorticoid receptor. That antiandrogen action is why it is used off-label for female pattern hair loss and other androgen-related hair loss.

Hypotrichosis simplex of the scalp is a rare inherited hair loss disorder. It is linked to variants in genes such as APCDD1, CDSN and SNRPE. Its mechanism is largely not androgen-dependent, so the connection to spironolactone's antiandrogen effect is speculative. The high TxGNN score reflects graph-based inference and should not be read as mechanistic proof.

The second-ranked prediction, **congenital hypotrichosis milia** (score 99.04%), is also unsupported. It is a very rare congenital condition with sparse mechanistic characterization, and it has no clinical trials or literature. It is not developed further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202187 | SPIRONOLACTONE (NorthStar Rx LLC) | Tablet | Not provided |
| ANDA040750 | Spironolactone (Proficient Rx LP) | Tablet, coated | Not provided |
| ANDA205936 | spironolactone (REMEDYREPACK INC.) | Tablet, film coated | Not provided |
| ANDA091426 | Spironolactone (Amneal Pharmaceuticals LLC) | Tablet | Not provided |
| NDA209478 | SPIRONOLACTONE (Padagis US LLC) | Suspension | Not provided |

Only 5 of the 20 authorizations are shown. All listed products are oral or oral-suspension forms. No topical formulation is listed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it (L5), and the disorder's biology is not clearly androgen-driven. The link to spironolactone's mechanism is therefore speculative. Safety data are also missing, which blocks the safety screening step.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap; download and parse the label)
- Mechanism of action data for spironolactone (for example, from the DrugBank API)
- Approved indication text for the US licenses
- Evidence that the disorder's genetic pathways (APCDD1, CDSN, SNRPE) respond to androgen or mineralocorticoid receptor blockade, such as preclinical or case-level data
- Route compatibility assessment: the available forms are oral, while hair disorders may call for a topical route

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

