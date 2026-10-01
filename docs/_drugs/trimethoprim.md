---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 1264
evidence_level: L5
indication_count: 2
---

# Trimethoprim
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

# Trimethoprim: From Antibacterial Use (Label Indication Not Provided) to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a bacterial dihydrofolate reductase inhibitor, and the US label data in this pack do not state its approved indication.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** were retrieved for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the label data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. The assessment notes that trimethoprim inhibits bacterial dihydrofolate reductase and has no known antiviral activity.

Punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or toxic/inflammatory. A direct mechanistic rationale is therefore weak. The very high score likely reflects proximity in the knowledge graph to conjunctivitis, not a real therapeutic link.

A different predicted indication for this drug, **conjunctivitis**, does have supporting evidence. It includes a completed Phase 4 trial of trimethoprim-polymyxin B ophthalmic solution against moxifloxacin, and an RCT comparing the two. That signal reflects an established topical antibacterial use for bacterial conjunctivitis. It does not transfer to punctate epithelial keratoconjunctivitis, which is often not bacterial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216393 | Trimethoprim | Tablet | Novitium Pharma LLC |
| ANDA091437 | Trimethoprim | Tablet | Lupin Pharmaceuticals, Inc. |
| ANDA216393 | Trimethoprim | Tablet | Golden State Medical Supply, Inc. |
| ANDA091437 | Trimethoprim | Tablet | Novel Laboratories, Inc. |
| NDA018679 | Trimethoprim | Tablet | Dr. Reddy's Laboratories Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there is no clinical or literature support. The mechanism (antibacterial, no antiviral activity) does not fit a condition that is often viral or toxic/inflammatory. The score most likely reflects association with conjunctivitis.

**To proceed, the following is needed:**
- Evidence that bacterial or other treatable pathogens play a role in punctate epithelial keratoconjunctivitis, plus any clinical or preclinical studies for this specific indication
- Package insert data (indications, warnings, contraindications), which is currently missing and blocks safety screening
- Confirmed mechanism of action data from DrugBank
- Separate evaluation of the **conjunctivitis** prediction, limited to bacterial etiology and topical combination formulations, which has stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

