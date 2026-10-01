---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 951
evidence_level: L5
indication_count: 10
---

# Nafarelin
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

# Nafarelin: From Endometriosis to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Nafarelin is a GnRH agonist nasal spray marketed in the US as Synarel. The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it. There is no plausible biological link, so this candidate is not recommended for further development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license record; the Evidence Pack notes indicate endometriosis as a known nafarelin use |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Nafarelin is known to be a GnRH agonist. With continuous dosing it desensitizes pituitary GnRH receptors and suppresses the pituitary-gonadal axis, lowering sex hormone levels. That effect underlies its use in hormone-dependent conditions such as endometriosis.

Ambras syndrome is different. It is a congenital hair-growth disorder linked to genomic rearrangements at 8q22 (the TRPS1 region), not to hormone excess. Suppressing sex hormones would not be expected to correct a genetic defect of this kind. The very high TxGNN score (99.87%) most likely reflects graph proximity to other hair and hormone-related conditions rather than biology, so it should not be read as evidence of efficacy.

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
| NDA 019886 | Synarel (Pfizer Laboratories Div Pfizer Inc) | Metered spray | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature and no plausible mechanism, so it stays at evidence level L5. The other nine predictions were also graded Hold. Only one of them, central precocious puberty (rank 9), has a strong mechanistic fit. It is probably an existing labeled use rather than true repurposing. The rank 7 candidate (physiological sexual disorder) has one indirect paper on endometriosis pain, which does not address sexual dysfunction directly.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the current labeled indications, including whether central precocious puberty is already on the label, since the license record has no indication text
- Any direct biological or clinical evidence linking GnRH agonism to Ambras syndrome. Without it, this candidate should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

