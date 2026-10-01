---
layout: default
title: Enalaprilat
parent: Model Prediction Only (L5)
nav_order: 652
evidence_level: L5
indication_count: 1
---

# Enalaprilat
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

# Enalaprilat: From an Injectable ACE Inhibitor to Primary Hereditary Glaucoma

## One-Sentence Summary

Enalaprilat is an injectable ACE inhibitor marketed in the United States as generic injection products.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available US license records (the approved indication text is blank) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license records (ANDAs, two unique numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Enalaprilat is an ACE inhibitor, so it acts on the renin-angiotensin system (RAS). A local RAS exists in ocular tissues (ciliary body, aqueous humor). Experimental work suggests that modulating it may affect aqueous humor dynamics and intraocular pressure. This is a plausible but unverified link.

Three factors weaken it:

- **Disease biology:** Primary hereditary (congenital) glaucoma is mainly a developmental anomaly of the trabecular meshwork and anterior chamber angle, often linked to genes such as CYP1B1 and LTBP2. It is usually treated surgically, not by drug-based pressure lowering.
- **Formulation:** Enalaprilat is available only as an intravenous injection. Its ocular penetration and suitability for chronic use are unknown.
- **Data gaps:** The mechanism-of-action record is incomplete, and no drug-interaction data was found.

The high score is most likely a knowledge-graph association. It should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075578 | Enalaprilat | Injection | Dr. Reddys Laboratories Inc |
| ANDA078687 | Enalaprilat | Injection | HF Acquisition Co LLC, DBA HealthFirst |

ANDA075578 appears twice in the source records and is shown once here. The approved indication text is blank in all records. All products are injectables.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature, and a weak biological fit. Congenital glaucoma is developmental and mainly surgical, and enalaprilat exists only as an IV product. There is not enough evidence to justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Preclinical evidence that ACE inhibition changes aqueous outflow or intraocular pressure in relevant glaucoma models
- An assessment of ocular penetration and of whether a non-IV route (topical or oral ACE inhibitor) is realistic
- A literature review of RAS and ACE-inhibitor effects in glaucoma, particularly developmental forms

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

