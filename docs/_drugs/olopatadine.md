---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 989
evidence_level: L5
indication_count: 1
---

# Olopatadine
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an antihistamine marketed in the US mainly as an ophthalmic solution. Its indication text is not recorded in this Evidence Pack, but the prediction rationale describes it as an eye drop for allergic conjunctivitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**.
Currently **no clinical trials and no publications** support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the record (the rationale describes allergic conjunctivitis) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on the prediction rationale, olopatadine is a selective H1 receptor antagonist and mast cell stabilizer. Its efficacy in allergic conjunctivitis is established.

Ocular rosacea is a chronic inflammatory disease of the ocular surface. It is driven mainly by meibomian gland dysfunction and innate immune activation, and possibly by mast cell activity. Olopatadine's anti-histamine and mast-cell-stabilizing effects could plausibly reduce ocular surface inflammation and itching.

This link is an inference, not evidence. The high score may partly reflect the disease's proximity to allergic and inflammatory conjunctivitis nodes in the knowledge graph rather than a rosacea-specific signal. The mechanism could not be checked against the source record.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA219557 | Olopatadine Hydrochloride (Glenmark Therapeutics) | Solution | Not listed in record |
| ANDA209995 | Olopatadine Hydrochloride (Allwell Health) | Solution | Not listed in record |
| ANDA213514 | Olopatadine HCl (Rugby Laboratories) | Solution/Drops | Not listed in record |
| ANDA209420 | Olopatadine Hydrochloride (Alembic Pharmaceuticals) | Solution/Drops | Not listed in record |
| ANDA204812 | Olopatadine Hydrochloride (Harris Teeter) | Solution | Not listed in record |

Other dosage forms on record include a metered spray. Route compatibility with the predicted indication has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Level L5). There are no registered trials or publications, and the record lacks original indications, mechanism data and safety information.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed original indications and mechanism of action from DrugBank
- A literature and trial search specific to ocular rosacea and mast cell or histamine involvement
- Route and formulation compatibility assessment (ophthalmic use for the new indication)
- Similarity analysis between the original and predicted indications

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

