---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 6
monitor_inn: "BLEOMYCIN"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-10-28
description: "Bleomycin: predicted new indication cauda equina neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Bleomycin: DNA strand-breaking cytotoxic antibiotic → cauda equina neoplasm
{: .text-alpha }

## One-Sentence Summary

Bleomycin is a cytotoxic antibiotic that damages tumour-cell DNA and is already marketed in the United States.
The TxGNN model predicts it may be useful for **cauda equina neoplasm**.
The data compiled for this report contain **no registered clinical trials** and **1 publication**, and that publication does not study bleomycin for this disease, so support rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of NDAs | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Bleomycin is generally understood to cause DNA strand breaks, which gives a broad antineoplastic rationale. Cauda equina neoplasms are tumours of the nerve roots at the lower end of the spinal canal.

No specific mechanistic or clinical link between bleomycin and cauda equina tumours was found. The only retrieved paper is a retrospective cohort on radiation therapy for relapsed CNS germinoma after a carboplatin, etoposide and bleomycin chemotherapy regimen. It studies radiotherapy, not bleomycin, and not this disease. The high TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort | Journal of Clinical Oncology | Retrospective evaluation of radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy including carboplatin, etoposide and bleomycin. It does not evaluate bleomycin for cauda equina neoplasm. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065031 | Bleomycin | Injection, powder, lyophilized, for solution | Hospira, Inc. |
| ANDA205030 | Bleomycin | Powder, for solution | NorthStar Rx LLC |
| ANDA065042 | Bleomycin | Injection, powder, lyophilized, for solution | Hikma Pharmaceuticals USA Inc. |
| ANDA065185 | Bleomycin | Injection, powder, lyophilized, for solution | Fresenius Kabi USA, LLC |

Approved indication text is not recorded in the local data for these authorizations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (glycopeptide antibiotic, DNA strand-breaking) |
| Myelosuppression Risk | Low (bleomycin is generally regarded as marrow-sparing; please refer to the package insert) |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function and chest imaging (pulmonary toxicity is the key concern), renal function, CBC |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. The sample reviewed lists levofloxacin as a minor interaction. Most others have no severity assigned, including pantoprazole, palonosetron, aprepitant, morphine, omeprazole, vancomycin, prednisone, hydrocortisone, ondansetron and clarithromycin.
- **Pulmonary toxicity**: The retrieved literature repeatedly identifies lung toxicity as a major bleomycin concern. This matters for any new use and calls for careful monitoring.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies bleomycin in cauda equina neoplasm, so the evidence level is L5 and the case rests only on a model prediction.

**To proceed, the following is needed:**
- Preclinical or clinical studies that directly evaluate bleomycin in cauda equina or comparable spinal tumours
- Detailed mechanism of action data
- Label warnings and contraindications from the package insert, including a pulmonary toxicity risk assessment
- A delivery-route assessment for access to this tumour site
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

