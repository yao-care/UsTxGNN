---
layout: default
title: Telavancin
parent: Model Prediction Only (L5)
nav_order: 1205
evidence_level: L5
indication_count: 9
---

# Telavancin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Telavancin: From Antibacterial Therapy to Hyperamylasemia

## One-Sentence Summary

Telavancin is a lipoglycopeptide antibiotic marketed in the US as VIBATIV, an injectable product. The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** support this prediction. It rests on a graph-based score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the record (telavancin is an antibacterial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Telavancin is a lipoglycopeptide antibiotic that inhibits bacterial cell wall synthesis and depolarizes the bacterial membrane. Nothing in the data connects this to amylase regulation.

Hyperamylasemia is elevated blood amylase, a laboratory finding usually tied to pancreatic or salivary gland conditions. It has no evident relationship to an antibacterial's original use. The high score most likely reflects a pattern in the knowledge graph, not established biology. For this reason, no plausible mechanistic link can be drawn.

The same holds for the other eight predictions in this record, such as polyclonal hyperviscosity syndrome, congenital analbuminemia and monoclonal gammopathy. All are L5 with no trials or literature. The only one with a nominal anti-infective rationale is septicemic plague, but the fit is weak. *Yersinia pestis* is Gram-negative and its outer membrane is not readily penetrated by glycopeptides. Established plague therapies also already exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022110 | VIBATIV (Cumberland Pharmaceuticals Inc.) | Injection, powder, lyophilized, for solution | Not listed in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature and no plausible mechanistic link between a cell wall-targeting antibiotic and elevated amylase. Safety information is also missing, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), which currently blocks safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal linking telavancin to amylase changes
- A route-compatibility check, which has not yet been done
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

