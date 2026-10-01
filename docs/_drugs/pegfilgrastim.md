---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 1020
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
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

# Pegfilgrastim: From Chemotherapy-Induced Neutropenia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a long-acting G-CSF (granulocyte colony-stimulating factor) marketed in the US as several biosimilar and reference products. It is generally used to reduce infection risk from low neutrophil counts after chemotherapy.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy (NPDR)**, but **no clinical trials and no publications** currently support this direction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced neutropenia (general drug knowledge; the approved-indication text is empty in the supplied record) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy (a second, broader prediction is diabetic retinopathy, score 99.73%) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (all listed authorizations are BLAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general knowledge, pegfilgrastim is a long-acting G-CSF that stimulates neutrophil production. Its established use is in neutropenia, not in any eye disease.

A plausible but unverified route to diabetic retinopathy runs through two effects. G-CSF mobilizes bone marrow-derived endothelial progenitor cells, and it modulates neutrophil function. Neutrophil-mediated leukostasis and endothelial injury are thought to contribute to retinal capillary damage in diabetes, so a G-CSF might influence retinal microvascular repair or injury.

The direction of effect is unclear, and it could be harmful. Progenitor mobilization and neutrophil activation could equally promote pathological neovascularization or inflammation. In severe NPDR, progression to proliferative disease is the main concern, so a pro-angiogenic or pro-inflammatory effect would be a real risk.

The broader "diabetic retinopathy" prediction is the parent term of the severe NPDR prediction, so the two are not independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied records contain no approved-indication text for these products, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761084 | FYLNETRA | Injection | Amneal Pharmaceuticals LLC |
| BLA761039 | UDENYCA | Injection, solution | Coherus Oncology, Inc. |
| BLA761075 | Fulphila | Injection | Biocon Biologics Inc. |
| BLA761045 | ZIEXTENZO | Injection | Sandoz Inc |

All products are injectables. The pack lists 12 authorizations in total, but only these 4 unique products are shown; UDENYCA appears twice under the same number.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.89%), but there are no trials or publications behind it (Evidence Level L5). The biological direction of effect is uncertain and may be harmful, because G-CSF could promote neovascularization or inflammation in the retina.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to test the proposed link to retinal disease
- Preclinical or observational evidence on G-CSF and diabetic retinal outcomes, including possible harm
- Confirmation that an injectable route is suitable for the intended eye-disease use

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

