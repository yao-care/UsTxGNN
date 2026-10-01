---
layout: default
title: Piperine
parent: Model Prediction Only (L5)
nav_order: 1048
evidence_level: L5
indication_count: 2
---

# Piperine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Piperine: From Unspecified Original Indication to Acne

## One-Sentence Summary

Piperine is marketed in the US as a liquid product, but no approved indication is recorded in the available data.
The TxGNN model predicts it may be relevant for **acne**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available data |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The one US listing for piperine is a liquid product from Professional Complementary Health Formulas. It has no recorded approved indication, so there is no established original use to compare with acne.

The high score reflects proximity in the TxGNN knowledge graph, not clinical or mechanistic evidence. Piperine is generally reported to have anti-inflammatory and antioxidant activity, which could plausibly relate to inflammatory acne. This is a hypothesis only and is not confirmed by the supplied evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not specified | Piperine | Liquid | Not specified |

Manufacturer: Professional Complementary Health Formulas.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction is supported only by a model score (Evidence Level L5). No trials, literature, mechanism data, or approved indication exist in the record. The package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (download and parse the label)
- Mechanism of action data (for example, from DrugBank)
- The approved indication and authorization details for the US product
- A literature and trial search for piperine in acne to establish any supporting evidence
- Assessment of whether the current liquid product can be used for a skin indication

The second-ranked prediction, amenorrhea (score 99.39%), is in the same position: model prediction only, with no supporting evidence and no plausible mechanism established.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

