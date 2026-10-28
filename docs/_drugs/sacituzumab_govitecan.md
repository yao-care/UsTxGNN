---
layout: default
title: Sacituzumab Govitecan
parent: Model Prediction Only (L5)
nav_order: 1141
evidence_level: L5
indication_count: 4
monitor_inn: "SACITUZUMAB GOVITECAN"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
last_modified_at: 2026-10-14
description: "Sacituzumab Govitecan: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the compiled data"
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Sacituzumab Govitecan: From an Unspecified Original Indication to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Sacituzumab govitecan is a Trop-2-directed antibody-drug conjugate that carries the topoisomerase I inhibitor SN-38 as its cytotoxic payload. The original indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the license record has no approved indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known drug characteristics, sacituzumab govitecan is an antibody-drug conjugate. The antibody targets Trop-2, and the payload SN-38 is a topoisomerase I inhibitor that kills rapidly dividing cells.

On the available data, a mechanistic link to drug-induced osteoporosis is not supported. The TxGNN score is a network-based computational prediction and is not evidence of efficacy. No plausible bone-protective mechanism is apparent. Cytotoxic chemotherapy is, if anything, more commonly associated with bone loss. The relationship between the original indication and this predicted indication has not been established, so the prediction should be treated as a hypothesis only.

Other predicted indications, all also at L5 with a Hold recommendation, were:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Severe nonproliferative diabetic retinopathy | 0.9969 |
| 3 | Diabetic retinopathy | 0.9960 |
| 4 | Diabetic cataract | 0.9912 |

None has clinical or literature support. A Trop-2-directed cytotoxic ADC has no established role in retinal microvascular disease or lens pathology. Systemic exposure to a cytotoxic agent in these non-malignant chronic conditions would be hard to justify without supporting data.

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
| BLA761115 (cancelled) | TRODELVY (Gilead Sciences, Inc.) | Powder, for solution | Not recorded in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (SN-38, topoisomerase I inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (myelosuppression and neutropenia are expected with topoisomerase I inhibitor payloads) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (at minimum, CBC with differential and liver and renal function would be expected) |
| Handling Protection | Please refer to the package insert warnings and precautions; follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 40 interacting drugs. Examples of **Major** interactions include:
  - Immunosuppressants and biologics: adalimumab, certolizumab pegol, natalizumab, ozanimod, leflunomide, cladribine, fostamatinib
  - Other agents: deferiprone, apalutamide, dacomitinib, irinotecan, nilotinib

  Examples of **Moderate** interactions include alefacept, alemtuzumab, anakinra, canakinumab, dimethyl fumarate, lorlatinib, ocrelizumab, and omacetaxine mepesuccinate.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature, and no plausible mechanism. The drug's cytotoxic profile makes a favorable benefit-risk balance unlikely in a non-malignant condition such as drug-induced osteoporosis. The only US license record is cancelled, and safety label data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block safety screening
- Mechanism of action data for mechanistic-link analysis
- The original approved indication, to assess its relationship to the predicted indication
- Preclinical or observational evidence of any bone-protective effect
- A benefit-risk assessment of systemic cytotoxic exposure in a non-malignant chronic condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

