---
layout: default
title: Betaxolol
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: From Approved Beta-Blocker Uses to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a beta-1 selective adrenergic blocker marketed in the US as oral tablets and ophthalmic drops. The TxGNN model predicts it may be effective for **primary hereditary glaucoma**. Currently **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Betaxolol is known from general pharmacology to be a beta-1 selective adrenergic antagonist. In glaucoma, beta-blockade at the ciliary epithelium is expected to reduce aqueous humor production and lower intraocular pressure. This link comes from general pharmacology, not from the supplied data.

The very high TxGNN score may reflect rediscovery of a known ophthalmic use rather than a true repurposing signal. The record includes a Sandoz ophthalmic solution (NDA019270), and betaxolol ophthalmic solutions are marketed for glaucoma and ocular hypertension. The record lists no approved indication text, so this cannot be confirmed from the data.

It is also unclear whether "primary hereditary glaucoma" (for example, congenital or juvenile forms) matches the open-angle glaucoma indication of the marketed products. Beta-blockers are often less effective or poorly suited in pediatric or congenital glaucoma, so extrapolation is uncertain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The record lists 5 entries, two of which are identical (ANDA078962). Four distinct authorizations are shown below. The record contains no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078962 (KVK-Tech) | Betaxolol Hydrochloride | Tablet, coated (oral) | Not listed in record |
| ANDA075541 (PuraCap Laboratories) | Betaxolol | Tablet, film coated (oral) | Not listed in record |
| ANDA075541 (Epic Pharma) | Betaxolol | Tablet, film coated (oral) | Not listed in record |
| NDA019270 (Sandoz) | Betaxolol Hydrochloride | Solution/drops | Not listed in record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried interaction data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but it is a model output only (L5) with no registered trials or literature. The record lacks the original indications, mechanism data and safety information needed to advance. The high score may simply reflect the already-known ophthalmic glaucoma use.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for each US authorization, to check whether glaucoma is already labeled
- Clarification of whether "primary hereditary glaucoma" is distinct from the approved open-angle glaucoma indication
- A search for trials and literature on betaxolol in congenital, juvenile or hereditary glaucoma
- Route compatibility assessment (oral tablets vs. ophthalmic drops for the predicted indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

