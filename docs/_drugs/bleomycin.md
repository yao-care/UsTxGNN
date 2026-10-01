---
layout: default
title: Bleomycin
parent: Moderate Evidence (L3-L4)
nav_order: 464
evidence_level: L4
indication_count: 6
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Bleomycin: From Cytotoxic Chemotherapy to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a cytotoxic anticancer agent that causes iron-dependent DNA strand breaks, and it is marketed in the US as several generic injectables.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, but **no clinical trials** and only **3 indirect publications** (case report, retrospective studies) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (bleomycin is a cytotoxic antineoplastic) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (the listed authorizations are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on general pharmacology, bleomycin causes iron-dependent DNA strand breaks and is cytotoxic to some lymphoid and germ cell tumours. Mechanistically, it could be applicable to other neoplasms.

The supporting papers are only indirect. They cover neurological manifestations of Hodgkin lymphoma, relapsed CNS germinoma and CNS lymphoma. None of them studies a tumour of the cauda equina. Bleomycin also has poor CNS penetration, which weakens the case for a tumour in this location. The high TxGNN score (0.993) is a computational prediction and has no clinical corroboration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case report | Rinsho Shinkeigaku | 17-year-old man with Hodgkin lymphoma and paraneoplastic sensory neuropathy. MRI showed enhancement of the trigeminal nerves and cauda equina. Not a cauda equina tumour, and bleomycin is not the focus. |
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Clinical study | J Clin Oncol | Retrospective study of radiotherapy salvage in CNS germinoma that relapsed after primary chemotherapy (carboplatin, etoposide, bleomycin). Indirect. |
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Cohort | Am J Clin Oncol | 277 patients with aggressive NHL. CNS involvement occurred in 14, one of them in the cauda equina (found at autopsy). Descriptive only, no bleomycin efficacy data. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065031 | Bleomycin | Injection, powder, lyophilized, for solution | Hospira, Inc. |
| ANDA205030 | Bleomycin | Powder, for solution | NorthStar Rx LLC |
| ANDA205030 | Bleomycin | Powder, for solution | Meitheal Pharmaceuticals Inc. |
| ANDA065042 | Bleomycin | Injection, powder, lyophilized, for solution | Hikma Pharmaceuticals USA Inc. |
| ANDA065185 | Bleomycin | Injection, powder, lyophilized, for solution | Fresenius Kabi USA, LLC |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-damaging glycopeptide antibiotic) |
| Myelosuppression Risk | Generally low compared with other cytotoxics; please refer to the package insert |
| Emetogenicity Classification | Low (general drug-class knowledge; please refer to the package insert) |
| Monitoring Items | Pulmonary function and chest imaging, CBC, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Key Warnings**: The retrieved literature reports interstitial pneumonitis with bleomycin ([PMID 4118423](https://pubmed.ncbi.nlm.nih.gov/4118423/)). Pulmonary toxicity is the dose-limiting concern.
- **Drug Interactions**: No interaction records were found in the dataset.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, the three papers are indirect, and none addresses a cauda equina tumour. Poor CNS penetration and pulmonary toxicity add further doubt.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Detailed mechanism of action (MOA) data
- Direct clinical or preclinical evidence in cauda equina or spinal tumours, including whether therapeutic drug levels can be reached at the site
- A separate look at other predictions in the same run. The rank 3 prediction, reticulum cell sarcoma (non-Hodgkin lymphoma), has L1 evidence with several Phase 3 trials, though these may reflect existing on-label lymphoma use.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

