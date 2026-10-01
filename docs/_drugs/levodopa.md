---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 854
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa: From Dopamine Replacement to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor that is marketed in the United States in several dosage forms.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but this rests only on a knowledge-graph score.
There are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Levodopa is a dopamine precursor. Its approved indication text is also missing from the US licensing records supplied, so the original clinical use cannot be confirmed from this data.

Rasmussen encephalitis is a chronic, usually unilateral, T-cell-mediated inflammatory brain disease. It causes intractable focal seizures, progressive hemiparesis and cognitive decline. No direct link between dopaminergic replacement and this immune-mediated pathology has been established, and levodopa has no known effect on the underlying inflammation.

The high score most likely reflects shared neurological features or neighboring genes in the knowledge graph. This is a hypothesis-generating signal only, and it does not amount to a mechanistic rationale. Similarity to the original indication and route compatibility have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The record lists 20 authorizations in total. The distinct main entries are shown below, and the indication text is empty in the source data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | L-Dopa (Deseret Biologicals, Inc.) | Liquid | Not stated in record |
| Not listed | L-Dopa (Professional Complementary Health Formulas) | Liquid | Not stated in record |
| Not listed | L DOPA (BioActive Nutritional, Inc.) | Liquid | Not stated in record |
| NDA209184 | Inbrija (Merz Pharmaceuticals, LLC) | Capsule | Not stated in record |

Other levodopa dosage forms in the record are oral capsule, tablet, extended-release tablet, orally disintegrating tablet and extended-release capsule.

## Safety Considerations

- **Seizure-prone patients**: Rasmussen encephalitis presents with refractory seizures, so levodopa's safety in this population would need review before any further work.

For all other safety information, please refer to the package insert. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high TxGNN score. There are no clinical trials or publications, no mechanism links dopaminergic therapy to an immune-mediated encephalitis, and safety in a seizure-prone population is unreviewed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking the safety screening)
- Mechanism of action data, for example from DrugBank
- A systematic literature search for any levodopa use in Rasmussen encephalitis or related epilepsy and neuroinflammation
- Evidence of a plausible mechanistic link to T-cell-mediated brain inflammation
- A seizure-risk safety review for this patient population
- Assessment of similarity to the original indication and of route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

