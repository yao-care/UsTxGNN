---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 1055
evidence_level: L5
indication_count: 10
---

# Plecanatide
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

# Plecanatide: From Chronic Constipation to Hypertrichosis

## One-Sentence Summary

Plecanatide is an oral guanylate cyclase-C (GC-C) agonist marketed in the US as Trulance. The Evidence Pack does not list an approved indication, but the drug class is used for chronic constipation.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, and no plausible mechanistic link was identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (approved indication text is empty) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on the known pharmacology of the drug class, plecanatide is a GC-C agonist. It raises cGMP in intestinal epithelial cells and is minimally absorbed into the bloodstream, so its effect is essentially confined to the gut.

No plausible link to hypertrichosis was identified. Hair growth regulation is not a known effect of the GC-C pathway. The TxGNN score is very high (99.998%), but it is a model output only. Similar predictions appear for related hair and genetic conditions (for example, Ambras-type congenital hypertrichosis and isolated hair shaft abnormalities). This pattern suggests the score reflects proximity in the knowledge graph rather than biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208745 | Trulance (Salix Pharmaceuticals Inc.) | Tablet (oral) | Not listed in the data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). There is also no plausible mechanistic link between a gut-restricted GC-C agonist and hair growth. The other nine predictions in the top 10 are also L5 with no plausible mechanism. The only one with any literature is a periodontal malformation syndrome, and those papers are general periodontitis background that never mention plecanatide.

**To proceed, the following is needed:**
- The US package insert (approved indications, warnings, contraindications), because safety screening cannot start without it
- Mechanism of action data from DrugBank
- A mechanistic hypothesis linking GC-C/cGMP signaling to hair follicle biology, ideally with preclinical support
- Drug-specific literature or registered trials; none currently exist

*This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

