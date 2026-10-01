---
layout: default
title: Pegloticase
parent: Model Prediction Only (L5)
nav_order: 1022
evidence_level: L5
indication_count: 1
---

# Pegloticase
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

# Pegloticase: From a Urate-Lowering Biologic to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegloticase is a PEGylated recombinant uricase that converts uric acid to allantoin and lowers serum urate. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**. This prediction currently rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries are the same BLA125293) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indications are recorded in the input. Pegloticase is known as a recombinant uricase that breaks down uric acid into allantoin.

One speculative link is that high uric acid and oxidative stress have been associated with diabetic microvascular complications in some observational reports. On that basis, lowering urate could in principle affect retinal microvascular disease.

There are important counterpoints:
- Uricase catalysis also produces hydrogen peroxide, which could be counterproductive in a retinal oxidative-stress setting.
- Pegloticase is a large systemic biologic with immunogenicity and infusion-reaction risks.
- Nothing in the input shows that it reaches the retina or acts on a retinal target.

The link therefore depends only on the TxGNN knowledge-graph score and has not been validated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125293 | Krystexxa | Injection, solution | Horizon Therapeutics USA, Inc. |

The Evidence Pack lists this authorization twice with identical details and no approved-indication text, so it appears once here.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5). There are no registered trials or publications, and the mechanistic link is speculative. Uricase-generated hydrogen peroxide, the systemic immunogenicity profile, and the lack of any evidence of retinal exposure are all unresolved concerns. Package insert safety data is also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism of action data, for example from DrugBank
- Preclinical evidence of a retinal target or benefit, plus an assessment of hydrogen peroxide risk in retinal tissue
- Route compatibility assessment, since the only available form is a systemic injection
- Literature and trial searches showing any link between urate lowering and diabetic retinopathy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

