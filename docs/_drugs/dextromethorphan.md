---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a widely marketed over-the-counter cough suppressant, and the US product names (for example "Cough Relief" and "Long Acting Cough Softgel") reflect that use.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials or publications** currently support this direction.
The only trial retrieved studies major depressive disorder, not a nasal condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough (inferred from product names; the licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dextromethorphan is a centrally acting cough suppressant that also has NMDA-receptor and sigma-1 activity. Its efficacy in cough is established in marketed products. Neither of these actions has an obvious link to nasal cavity pathology.

The prediction comes from the knowledge graph alone, and the very high score (rank 843 overall) does not replace mechanistic or clinical support. The link could at best be symptomatic, for example cough associated with upper-airway irritation. It is not a disease-modifying effect on the nasal cavity.

Among the other predictions, acute laryngopharyngitis is the most plausible (cough relief in upper respiratory tract inflammation). It also has no trials or literature. The remaining candidates are speculative or likely graph artifacts:
- faucial diphtheria
- trigeminal autonomic cephalalgia
- cervical disc degenerative disorder
- allergic urticaria

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Randomized, double-blind, placebo-controlled trial of dextromethorphan and bupropion sustained-release tablets in Chinese adults with **major depressive disorder**. Expected completion is 2026-12-30. No results are reported, and the trial is not relevant to nasal cavity disease. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Showing 5 of 20 authorizations. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| M012 | Childrens Giltuss Honey DM Cough | Liquid | Dextrum Laboratories Inc |
| M012 | RoboTablets | Tablet | DXM Pharmaceutical, Inc |
| M012 | QUALITY CHOICE Long Acting Cough Softgel | Capsule, liquid filled | Chain Drug Marketing Association, Inc. |
| M012 | Father Johns Medicine | Liquid | Humco Holding Group, Inc |
| M012 | Cough Relief | Liquid | TOP CARE (Topco Associates LLC) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for nasal cavity disease is the graph-based TxGNN score. The one trial found targets a different condition (major depressive disorder). There is no literature and no documented mechanism, so the evidence stays at L5.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible mechanistic link to nasal cavity disease
- Package insert warnings and contraindications, to allow safety screening
- Trials or publications that actually study dextromethorphan in nasal or upper-airway conditions
- Clarification of the specific nasal cavity condition, and whether the target is symptomatic cough relief or a disease effect
- A route and formulation compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

