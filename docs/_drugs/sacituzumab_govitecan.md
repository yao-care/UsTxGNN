---
layout: default
title: Sacituzumab Govitecan
parent: Model Prediction Only (L5)
nav_order: 1141
evidence_level: L5
indication_count: 4
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sacituzumab Govitecan: From Oncology Use to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab govitecan (marketed as TRODELVY) is a Trop-2-directed antibody-drug conjugate that delivers the cytotoxic topoisomerase I inhibitor SN-38, so it is an oncology drug.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis** with a very high score, but **0 clinical trials** and **0 publications** support this prediction. It rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (the drug is a cytotoxic oncology agent) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761115) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

**It is not well supported.** The database has no detailed mechanism-of-action entry for this drug. Based on known information, sacituzumab govitecan is a Trop-2-directed antibody-drug conjugate. The antibody guides the drug to Trop-2-expressing tumor cells, and the payload SN-38 kills cells by inhibiting topoisomerase I.

Nothing in this mechanism suggests it would prevent or treat bone loss. Cytotoxic chemotherapy and its supportive-care effects (for example gonadal suppression and poor nutrition) are more likely to worsen bone health. The 99.78% score is a graph-based prediction only and likely reflects network proximity rather than biology. No trials or literature were provided that could confirm or refute it.

The model also ranked three diabetes-related eye conditions highly:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Severe nonproliferative diabetic retinopathy | 99.69% | L5 | Hold |
| Diabetic retinopathy | 99.60% | L5 | Hold |
| Diabetic cataract | 99.12% | L5 | Hold |

None has a plausible mechanistic link. These conditions involve microvascular damage, VEGF signaling, inflammation, and lens oxidative stress, and they are not known targets of a Trop-2/SN-38 conjugate. Systemic exposure to a cytotoxic payload also carries myelosuppression and other toxicity risks. These risks are hard to justify in chronic, non-life-threatening eye conditions that already have effective therapies such as anti-VEGF drugs and laser treatment.

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
| BLA761115 | TRODELVY (Gilead Sciences, Inc.) | Powder, for solution | Not provided in the data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (SN-38) |
| Myelosuppression Risk | High (systemic exposure to the cytotoxic payload carries myelosuppression risk) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical, or literature support (L5), and no plausible mechanistic link. A cytotoxic ADC with myelosuppression risk is a poor fit for osteoporosis or chronic diabetic eye disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking Trop-2/SN-38 biology to bone metabolism or diabetic ocular disease
- The approved indication text for BLA761115, to confirm the original indication
- A benefit-risk justification against existing therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

