---
layout: default
title: Pilocarpine
parent: Model Prediction Only (L5)
nav_order: 1044
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine: From an Unrecorded Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is a marketed muscarinic agonist, but the source record lists no original indication.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
yet there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so the evidence rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, pilocarpine is a muscarinic (M3-preferring) agonist. It contracts the ciliary muscle and the iris sphincter, which increases trabecular outflow and lowers intraocular pressure. This is a plausible mechanism for glaucoma in general.

This link comes from general pharmacology, not from the supplied data, and two caveats apply:

- **Possible missing known indication:** Pilocarpine is a long-established ophthalmic miotic used for glaucoma. The very high score (99.83%) may simply reflect an existing indication that is missing from the source record, so it may not be a true repurposing signal.
- **Subtype specificity:** "Primary hereditary glaucoma" (for example, primary congenital glaucoma) is narrower than general glaucoma use. No data here supports efficacy in that subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Five of the 20 authorizations are shown below. The source record contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077220 | Pilocarpine Hydrochloride | Film-coated tablet (oral) | Bryant Ranch Prepack |
| ANDA076963 | Pilocarpine Hydrochloride | Film-coated tablet (oral) | Amici Pharmaceuticals LLC |
| NDA214028 | VUITY | Solution/drops | AbbVie Inc. |
| NDA217836 | Qlosi | Solution | Orasis Pharmaceuticals, Inc. |
| ANDA077248 | Pilocarpine Hydrochloride | Film-coated tablet (oral) | Amneal Pharmaceuticals NY LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5, model prediction only). The high score may reflect an already-known glaucoma use missing from the source record, and nothing supports the specific "primary hereditary glaucoma" subtype. Safety data is also missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications), which blocks safety screening
- Mechanism of action data, for example from DrugBank
- The original approved indications for the ophthalmic products (VUITY, Qlosi), to confirm whether glaucoma is already labeled
- Subtype-specific evidence for primary hereditary or congenital glaucoma
- A route compatibility assessment between the available formulations and the required route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

