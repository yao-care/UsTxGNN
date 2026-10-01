---
layout: default
title: Carteolol
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 1
---

# Carteolol
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

# Carteolol: From Beta-Blocker Use (Original Indication Not Recorded) to Primary Hereditary Glaucoma

## One-Sentence Summary

Carteolol is a non-selective beta-blocker marketed in the US as a solution. The record does not list its original indication.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but the only support is the model score, with **0 clinical trials** and **0 publications** supplied.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the record (the approved indication text is empty) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (ANDA075476) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Carteolol is a non-selective beta-adrenergic blocker. Beta-blockers lower intraocular pressure by reducing aqueous humor production, so a link to glaucoma is biologically plausible.

Carteolol is already marketed as an ophthalmic agent for glaucoma and ocular hypertension in many jurisdictions. This record's empty original-indication field is therefore probably a gap in the data, not proof that this is a true repurposing case. The model score alone cannot separate a genuine repurposing signal from a use the label already covers.

It is also unresolved whether "primary hereditary glaucoma" (for example congenital or juvenile forms) differs from the adult open-angle indication on the label. Beta-blocker use in infants carries systemic safety concerns, which makes this distinction important.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075476 | Carteolol Hydrochloride (Sandoz Inc) | Solution | Not stated in record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a very high TxGNN score, with no trials or literature. The record also lacks the original indication, mechanism data, and label safety information. A known label use cannot yet be ruled out.

**To proceed, the following is needed:**
- Label indications and package insert warnings and contraindications, confirmed from FDA sources
- Mechanism of action data confirmed in DrugBank
- A literature and trial search for pediatric or hereditary glaucoma studies
- A review of systemic safety for beta-blocker use in infants and children
- A check of whether the route of administration matches the intended use (the record lists the route only as "Other")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

