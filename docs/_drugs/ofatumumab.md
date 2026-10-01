---
layout: default
title: Ofatumumab
parent: Model Prediction Only (L5)
nav_order: 983
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Ofatumumab: Predicted New Indication in CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody that is marketed in the US as KESIMPTA.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) with immunoglobulin heavy chain variable-region gene somatic hypermutation**.
However, this specific subtype has **0 clinical trials** and **0 publications** mapped to it, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | CLL/SLL with immunoglobulin heavy chain variable-region gene somatic hypermutation (IGHV-mutated) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125326) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, ofatumumab is an anti-CD20 antibody, and CD20 is expressed on CLL/SLL B cells. Mechanistically, it may therefore be applicable to this disease.

The predicted disease is a molecular subtype of CLL/SLL (IGHV-mutated). No trials or publications specific to this subtype were found. Evidence for the broader CLL/SLL disease is not automatically transferable to this subtype in this dataset.

The pack also notes that rank 2 (pregerminal center CLL/SLL) has the identical score, 99.77%. This suggests both terms map to the same graph neighborhood, so the score may reflect the parent disease rather than subtype-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific subtype.

## Literature Evidence

Currently no related literature available for this specific subtype.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125326 | KESIMPTA (Novartis Pharmaceuticals Corporation) | Injection, solution | Not listed in the data provided |

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack has no warnings, contraindications, or drug interaction records for this drug. An assessment attached to the broader CLL/SLL entry mentions a boxed warning for hepatitis B reactivation and progressive multifocal leukoencephalopathy (PML). Please verify this against the current label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature for this IGHV-mutated subtype. The high score likely reflects the parent CLL/SLL disease.

The broader entries in the same pack have real evidence:
- **CLL/SLL:** L1, with completed Phase 3 trials in which ofatumumab was the comparator arm. The pack notes this is likely an established use rather than a novel one.
- **Follicular lymphoma:** L2, with several completed Phase 2 trials.

**To proceed, the following is needed:**
- Subtype-specific data on ofatumumab in IGHV-mutated CLL/SLL, for example subgroup analyses from existing CLL Phase 3 trials
- Mechanism of action data from DrugBank
- FDA package insert warnings and contraindications (blocking for safety screening)
- The approved indication text, to confirm whether CLL is an established or a new use
- Route and formulation compatibility. KESIMPTA is a subcutaneous injection, so the route needed for oncology use must be confirmed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

