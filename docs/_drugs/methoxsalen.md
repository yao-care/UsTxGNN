---
layout: default
title: Methoxsalen
parent: Model Prediction Only (L5)
nav_order: 912
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From Photochemotherapy to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen is a light-activated (photosensitizing) drug used with UVA light, either on the skin or on blood treated outside the body. The TxGNN model predicts it may be effective for **localized pagetoid reticulosis**, with a very high score. However, **0 clinical trials** and **0 publications** were supplied for this specific disease, so the prediction currently rests on the model and mechanism alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved-indication text for both US licenses was empty in the supplied data) |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (1 NDA and 1 ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied. From general pharmacology, methoxsalen is activated by UVA light. It inserts itself into DNA and forms crosslinks, which can trigger apoptosis in skin-homing malignant T cells. It may also modulate immune responses. It is used topically with UVA (PUVA) and in extracorporeal photopheresis.

Pagetoid reticulosis is a localized, indolent variant within the mycosis fungoides spectrum of cutaneous T-cell lymphoma (CTCL). Because the disease is confined to the skin and involves skin-homing T cells, a mechanistic fit with UVA-activated methoxsalen is plausible. This rationale comes from the mechanism and from evidence in neighboring CTCL conditions, not from data on this specific entity.

Two supplied papers concern photopheresis in CTCL. They are attached to the second-ranked prediction, indolent primary cutaneous T-cell lymphoma, not to this one. They do not directly support this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020969 | UVADEX (Therakos LLC) | Injection, solution | Not listed in supplied data |
| ANDA202687 | Methoxsalen (Strides Pharma Science Limited) | Capsule, liquid filled | Not listed in supplied data |

The two products cover two routes: injectable (used with extracorporeal treatment) and oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trials or literature were supplied for localized pagetoid reticulosis, so evidence is L5. The mechanistic rationale is reasonable but indirect. The strongest nearby signal is photopheresis evidence in other cutaneous T-cell lymphomas, which belongs to a different predicted indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text from the US labels, to confirm whether CTCL or pagetoid reticulosis is already a labeled use
- Mechanism-of-action data from DrugBank
- A targeted search for PUVA or photopheresis studies, case series or reports in pagetoid reticulosis or mycosis fungoides
- A route-compatibility assessment (topical PUVA vs. extracorporeal use) for a localized skin disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

