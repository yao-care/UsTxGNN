---
layout: default
title: Fulvestrant
parent: Moderate Evidence (L3-L4)
nav_order: 742
evidence_level: L4
indication_count: 10
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-10-28
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L4). Approved use: Not listed in the data compiled for this report (fulvestrant is widel…"
---

# Fulvestrant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Fulvestrant: From Breast Cancer to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Fulvestrant is an estrogen receptor antagonist and degrader, used as an endocrine therapy in hormone receptor-positive breast cancer.
The TxGNN model predicts it may be effective for **HIV infectious disease**,
but the supporting evidence is thin: **0 clinical trials** and **2 publications** (one preclinical study and one study of a related retrovirus).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (fulvestrant is widely known as an endocrine therapy for HR+ breast cancer) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L4 |
| US Market Status | Marketed (valid licenses: 12 of 12) |
| Number of NDAs | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, fulvestrant is an estrogen receptor (ER) antagonist and degrader. Its efficacy in hormone receptor-positive breast cancer is well established, and it may be mechanistically relevant to HIV if ER signaling affects viral latency.

A 2026 preclinical study (PMID 42430506) examined how estrogen, fulvestrant and HIV latency-reversing agents affect ERα in CD4+ T cells. This suggests a plausible link between ER signaling and HIV transcription and latency. However, the evidence is in vitro and indirect, and no clinical data exist for fulvestrant in HIV. The other publication concerns HTLV-1, a related but different retrovirus, and does not directly support fulvestrant use in HIV.

Several other predicted indications scored highly but are not well supported. These include multiple endocrine neoplasia, rheumatoid arthritis, and veterinary or animal-model immunodeficiency conditions. The multiple endocrine neoplasia hits are breast cancer trials and likely reflect a label or ontology artifact rather than real evidence. In the rheumatoid arthritis rat model, estrogen blockade worsened inflammation, which argues against benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical / in vitro | JCI Insight | Evaluated the effect of estrogen on ERα nuclear translocation in CD4+ T cells, and the effect of fulvestrant and HIV latency-reversing agents on the ER pathway |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics cohort analysis (HTLV-1) | Research Square | Systems biology study of HTLV-1-associated myelopathy, a related retrovirus; no direct support for fulvestrant |

## US Market Information

The data compiled for this report list 12 US authorizations, all cancelled. Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021344 | FASLODEX | Injection | AstraZeneca Pharmaceuticals LP |
| NDA210326 | Fulvestrant | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA215077 | Fulvestrant | Injection | Alembic Pharmaceuticals Inc. |
| ANDA211422 | Fulvestrant | Injection, solution | Avenacy, Inc. |
| ANDA205935 | Fulvestrant | Injection | Sandoz Inc |

## Cytotoxicity

Fulvestrant is an antineoplastic drug, but it is an endocrine therapy rather than a conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/endocrine therapy (estrogen receptor antagonist and degrader) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease.
- **Drug Interactions**: 92 potential interactions were identified, but the severity level is unclassified for all of those listed. Examples include warfarin, acetylsalicylic acid, dexamethasone, prednisone, simvastatin, metformin, omeprazole, pantoprazole, ondansetron and morphine. The warfarin interaction deserves particular attention given the knowledge-graph coagulation signal.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but rests only on one preclinical study and one study of a related retrovirus. There are no clinical trials, and the drug is marketed in the US with 12 of 12 licenses valid.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Further preclinical validation of ER antagonism or degradation on HIV latency and transcription in CD4+ T cells
- Clarification of whether a new HIV-related formulation or development path is feasible, given that the drug is marketed in the US with 12 of 12 licenses valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

