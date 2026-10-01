---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Established Antimetabolite Use to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is an antifolate (DHFR inhibitor) drug that is currently marketed in the United States in injectable and oral forms.
The TxGNN model predicts it may be effective for **pulmonary blastoma**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only prediction with no supporting evidence yet.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied data (no approved indication text in the US licence records) |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (the sample shown is ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Based on known information, methotrexate is an antifolate that inhibits dihydrofolate reductase (DHFR), which is needed for nucleotide synthesis. Its activity is greatest in rapidly proliferating cells. Mechanistically, it could be applicable to a rapidly dividing tumor such as pulmonary blastoma.

The score is very high (0.994; model rank 12,873), but a high score alone is not evidence. Pulmonary blastoma is a rare lung tumor, and nothing in the retrieved trials or literature ties methotrexate to it. The rationale is therefore purely a class-level plausibility argument.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The licence records contain no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040716 | Methotrexate | Injection | Accord Healthcare, Inc. |
| ANDA040385 | Trexall | Tablet, film coated | Teva Women's Health, Inc. |
| ANDA201749 | Methotrexate | Tablet | Bryant Ranch Prepack |
| ANDA201529 | Methotrexate | Injection, solution | Eugia US LLC |

Available routes across all 20 authorizations include injectable and oral forms. An "other" solution form and a lyophilized powder for injection are also listed.

## Cytotoxicity

Classification below is based on drug class, because the Evidence Pack has no toxicity data. Please also refer to the package insert warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate class) |
| Myelosuppression Risk | High (dose-dependent) |
| Emetogenicity Classification | Low to moderate, depending on dose and route |
| Monitoring Items | CBC with differential, liver and renal function; methotrexate levels with high-dose regimens |
| Handling Protection | Must follow cytotoxic (hazardous) drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no trials, no publications and no mechanistic data specific to pulmonary blastoma, and safety data (warnings, contraindications) are also missing. It is not currently supportable for further development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any case reports, preclinical data or registry data specific to pulmonary blastoma
- Consideration of other candidates in the same Evidence Pack that have more supporting evidence. For example, Hodgkin lymphoma (L3) and rhabdomyosarcoma (L2, including a phase II high-dose methotrexate study in children) are better supported.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

