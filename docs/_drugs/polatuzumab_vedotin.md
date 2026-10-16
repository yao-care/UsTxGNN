---
layout: default
title: Polatuzumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 1058
evidence_level: L5
indication_count: 1
monitor_inn: "POLATUZUMAB VEDOTIN"
predicted_indications: ["HER2 positive breast carcinoma"]
last_modified_at: 2026-10-14
description: "Polatuzumab Vedotin: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Not available in the compiled data"
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From an Unspecified Original Indication to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an antibody-drug conjugate (ADC) marketed in the US as POLIVY, but the data compiled for this report do not specify an original approved indication.
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761121) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the compiled data. Based on known pharmacology, polatuzumab vedotin is an ADC that targets CD79b, a component of the B-cell receptor, and delivers the microtubule-disrupting payload MMAE (monomethyl auristatin E). Its biology is therefore tied to B-cell malignancies, not breast cancer.

The only plausible indirect link is the payload. Microtubule-targeting payloads are already used in HER2-directed ADCs such as trastuzumab emtansine (DM1) and trastuzumab deruxtecan, so cytotoxic payload activity is not foreign to HER2-positive breast cancer. However, polatuzumab vedotin has no HER2-directed targeting, and breast tumor cells are not known to express CD79b at meaningful levels. Any activity would depend on non-specific payload effects, which is an unsupported hypothesis. The high TxGNN score (0.993) is a computational prediction only and should not be read as evidence of efficacy. The model's rank for this drug-disease pair was 14,969.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761121 | POLIVY | Injection, powder, lyophilized, for solution | Not stated in the compiled data (status: cancelled; manufacturer: Genentech, Inc.) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic microtubule-disrupting payload (MMAE) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (complete blood count and liver and renal function are generally advisable for cytotoxic agents) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records; the first 20 reviewed are listed below.
  - **Major**: Clarithromycin, Cobicistat, Deferiprone, Samarium (153Sm) lexidronam
  - **Moderate**: Aprepitant, Cimetidine, Naltrexone, Metronidazole, Miconazole, Rosuvastatin, Simvastatin, Tinidazole, Clotrimazole, Strontium chloride Sr-89, Ticagrelor, Chloroquine, Disulfiram, Secnidazole, Hydroxychloroquine, Benznidazole

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no registered trials and no literature, and the mechanism is not credible: CD79b is not a recognized target in HER2-positive breast cancer, and HER2-directed ADCs already cover this space with targeted delivery. The US license is also listed as cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (FDA label)
- Confirmed mechanism of action data and the original approved indication
- Preclinical evidence, such as CD79b expression in HER2-positive breast tumors and in vitro MMAE sensitivity
- Clarification of the current US regulatory and availability status
- A rationale for choosing this drug over existing HER2-directed ADCs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

