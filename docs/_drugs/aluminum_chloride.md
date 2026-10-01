---
layout: default
title: Aluminum Chloride
parent: Model Prediction Only (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Aluminum Chloride
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

# Aluminum Chloride: From Antiperspirant Use to Seborrheic Keratosis

## One-Sentence Summary

Aluminum chloride is a topical astringent and antiperspirant. The US-marketed products in this pack are antiperspirants, and the license records do not state an approved indication.
The TxGNN model predicts it may be effective for **seborrheic keratosis**, but there are **0 clinical trials** and **0 publications** for this specific indication, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records. Product names indicate antiperspirant use (excessive sweating). This is inferred, not documented. |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 license records (most have no license number listed) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, aluminum chloride is a topical aluminum salt with astringent, protein-precipitating action. It is used to reduce sweating by obstructing eccrine sweat ducts.

The only link to seborrheic keratosis is speculative. Aluminum salts act on the skin surface, and seborrheic keratosis is a benign keratotic skin lesion. Neither the pack nor the retrieved literature shows that aluminum chloride treats it. The high score likely reflects similarity between skin conditions in the knowledge graph rather than a demonstrated mechanism.

One adjacent signal exists elsewhere in the pack. A not-yet-recruiting Phase 1 study (NCT07401277) tests 5-fluorouracil plus aluminum in **actinic keratoses**, a different lesion type. Its relevance has not been graded. It does not support seborrheic keratosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | ANTIPERSPIRANT ANTISUDORIFIQUE (Archifox GmbH & Co. KG) | Spray | Not stated |
| M019 | Duradry Sweat Minimizing Gel (Novadore USA Inc) | Gel | Not stated |
| Not listed | Antiperspirant ODABAN (Ryma-Pharm GmbH) | Spray | Not stated |
| M017 | Certain Dri Clinical Strength Prescription Protection Rollon (Clarion Brands LLC) | Liquid | Not stated |
| Not listed | ANTIPERSPIRANT ANTISUDORIFIQUE (Ryma-Pharm GmbH) | Spray | Not stated |

Other listed dosage forms include lotion, solution, stick, for-solution, metered spray and cream.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interactions were found in the pack.

Some signals appear in the retrieved material and are relevant to any new skin indication:
- **Keratinization changes:** In a mouse model, daily 20% aluminum chloride caused apoptosis, keratinization arrest and granular parakeratosis (PMID 31567135).
- **Contact sensitization:** Aluminum is a recognized contact allergen (PMID 35029347).
- **Irritation and occlusion:** Mucosal and vulvar skin irritation is a concern. Follicular occlusion could worsen comedonal disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it and no supported mechanism. Evidence level is L5, and the pack's own assessment calls the link speculative.

**Other predictions in the pack:**
- "Skin disease" (rank 6) has the strongest evidence, including a completed Phase 3 RCT (NCT03433859, n=54) comparing topical aluminium chloride with onabotulinumtoxinA in residual limb hyperhidrosis. It also has several hyperhidrosis RCTs and reviews, and a single-arm study in regorafenib-associated hand-foot skin reaction (PMID 37142953). This is mostly an established use rather than repurposing, the indication is too broad, and the Phase 3 comparator is truncated in the input and needs verification.
- Dry eye syndrome and eye disease have no supportive evidence. The pack notes aluminum chloride is a known ocular and mucosal irritant.
- Congenital prothrombin deficiency, von Hippel anomaly and chronic relapsing inflammatory optic neuropathy have no plausible mechanism and are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- Verified original indication text for the marketed products
- Any preclinical or clinical evidence specific to seborrheic keratosis
- Route compatibility assessment
- Splitting the broad "skin disease" prediction into specific conditions (hyperhidrosis, hand-foot skin reaction) before any recommendation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

