---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 954
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From Pain and Inflammation to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a widely marketed non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a congenital limb malformation.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and inflammation (general drug knowledge; the US label text is not included in the supplied data) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Naproxen is a non-selective COX-1/COX-2 inhibitor. Its efficacy in pain and inflammation is well established, and it works by reducing prostaglandin production.

Brachydactyly-syndactyly syndromes are congenital limb malformations with a developmental or genetic basis. Prostaglandin inhibition is not known to modify them, and NSAIDs would not be expected to correct a structural developmental defect. **No established mechanistic link was identified.**

The high score most likely reflects proximity in the knowledge graph, not a biological rationale. The other top-ranked predictions show the same pattern:
- Colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.22%)
- Acromesomelic dysplasia, Hunter-Thompson type (99.17%)
- Brachyolmia-amelogenesis imperfecta syndrome (99.06%)

All are rare congenital skeletal or developmental disorders with no trials or literature, and none has a plausible link to COX inhibition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied data lists no approved indication text for these authorizations. The table shows 5 of the 20 authorizations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020204 | Aleve | Tablet | Lil' Drug Store Products, Inc |
| ANDA208363 | Naproxen Sodium | Capsule, liquid filled | Care One (American Sales Company) |
| ANDA091416 | Naproxen | Tablet | NuCare Pharmaceuticals, Inc. |
| ANDA212517 | Naproxen | Tablet | Preferred Pharmaceuticals, Inc. |
| ANDA200629 | Naproxen Sodium | Tablet, film coated | Aurobindo Pharma Limited |

All listed products are oral: tablets, film-coated or coated tablets, and liquid-filled capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score, with no trials, no publications, and no plausible mechanism linking COX inhibition to a congenital limb malformation. The evidence level is L5, and the candidate remains at the initial screening stage (S0).

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- A biological rationale connecting prostaglandin or COX pathways to the pathogenesis of the predicted disease
- Any supporting preclinical, case-level, or clinical evidence
- Route compatibility assessment, which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

