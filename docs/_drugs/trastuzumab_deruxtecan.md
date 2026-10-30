---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 1251
evidence_level: L5
indication_count: 1
monitor_inn: "TRASTUZUMAB DERUXTECAN"
predicted_indications: ["drug-induced osteoporosis"]
last_modified_at: 2026-10-30
description: "Trastuzumab Deruxtecan: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not specified in the data compiled for this report"
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Trastuzumab Deruxtecan: From Oncology (HER2-Directed Therapy) to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-directed antibody-drug conjugate (ADC) carrying a topoisomerase I inhibitor payload (deruxtecan), marketed in the US as Enhertu.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on a model score alone and should be treated as a low-confidence signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trastuzumab deruxtecan is a HER2-directed antibody-drug conjugate whose payload, deruxtecan, is a topoisomerase I inhibitor. It is a cytotoxic oncology agent.

Its high TxGNN score (0.9931) is the only support for this prediction, and no plausible mechanistic path to bone metabolism or to treating drug-induced osteoporosis is evident. The prediction may reflect TxGNN model (deep learning) artifacts, such as shared links with other oncology drugs or with cancer treatments that cause osteoporosis, rather than a true therapeutic signal.

A cytotoxic ADC is also an unlikely candidate for a chronic bone-protective indication. Its known toxicity profile (interstitial lung disease, myelosuppression, cardiac dysfunction) raises serious safety concerns for this use. The relationship between the original oncology use and the predicted indication therefore remains unvalidated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761139 | Enhertu (Daiichi Sankyo Inc.) | Lyophilized powder for injection solution | Not listed (status: valid) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (targeted therapy delivering a cytotoxic agent) |
| Myelosuppression Risk | Medium to High (neutropenia and other cytopenias are a recognised concern; confirm with the package insert) |
| Emetogenicity Classification | Moderate (based on drug class; confirm with the package insert) |
| Monitoring Items | CBC with differential, liver and renal function, pulmonary status (interstitial lung disease), cardiac function (LVEF) |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for authoritative details.

## Safety Considerations

**Drug Interactions**: The interaction screening completed with 42 interactions found. Examples of the main ones include:

- **Major**: Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, Baricitinib, Certolizumab pegol, Cladribine, Leflunomide, Natalizumab
- **Moderate**: Palifermin, Strontium chloride Sr-89, Roflumilast, Chloramphenicol, Alemtuzumab, Anakinra, Azathioprine, Canakinumab, Dimethyl fumarate, Niraparib

Many of these are immunosuppressive or myelosuppressive agents, so additive effects on blood counts and infection risk should be considered.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (evidence level L5), with no clinical trials or literature and no plausible mechanistic link to bone metabolism. The drug's cytotoxic profile and serious known toxicities make it an unfavourable candidate for a chronic bone-protective indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (MOA) to evaluate any link to bone metabolism
- Preclinical or mechanistic evidence supporting an effect on bone turnover
- Confirmation of the original approved indications and the reason the US license is recorded as cancelled
- A comparison with established treatments for drug-induced osteoporosis, and a risk-benefit assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

