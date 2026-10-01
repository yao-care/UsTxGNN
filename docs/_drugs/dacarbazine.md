---
layout: default
title: Dacarbazine
parent: Moderate Evidence (L3-L4)
nav_order: 563
evidence_level: L4
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Dacarbazine: From Cancer Chemotherapy to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is an injectable DNA-alkylating chemotherapy agent that is marketed in the US as generic products.
The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm**, with a very high score of 99.26%.
Evidence for this specific drug and indication is thin: **1 clinical trial** and **19 publications** were retrieved, but the trial tested a related drug (temozolomide) and none of the literature directly shows dacarbazine working in this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records listed (3 unique ANDA numbers; all generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dacarbazine is not available in the input. From general pharmacology, dacarbazine is a DNA-alkylating (methylating) agent. It is metabolically activated to MTIC, which damages tumor-cell DNA.

Temozolomide acts through the same MTIC species. The only linked clinical trial studied temozolomide in advanced aerodigestive tract cancers (head and neck, esophageal, non-small-cell lung, and colorectal) selected for MGMT promoter methylation. That gives class-level, indirect support for the idea that this type of alkylating agent may act in these tumors. It says nothing about dacarbazine itself.

The 99.26% TxGNN score is a computational prediction only, and it does not replace clinical evidence. The approved-indication text was not available in the input, so the link between dacarbazine's labeled uses and this new indication could not be assessed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Temozolomide (not dacarbazine) in advanced aerodigestive tract, colorectal, and lung cancers selected for MGMT promoter methylation. The termination reason and efficacy results are not provided. |

This is indirect evidence only, because the study drug differs from dacarbazine and the record does not show a randomized design.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | RCT (Phase 3) | JAMA Oncology | Toripalimab vs dacarbazine as first-line therapy in acral melanoma. Dacarbazine was the comparator, in a different indication. |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 trial | Molecular Cancer Therapeutics | Publication of NCT00423150: temozolomide in advanced aerodigestive tract and colorectal cancers with MGMT promoter methylation. This is a related drug, not dacarbazine. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Clinical study | Annals of Oncology | Dacarbazine plus 5-fluorouracil chemotherapy in advanced medullary thyroid cancer. This is a neuroendocrine head-and-neck-region tumor, not an aerodigestive tract cancer. |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clinical Oncology | Overview of medullary thyroid carcinoma. |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Review | J Clin Neurosci | Temozolomide in aggressive pituitary tumors (related drug, different disease). |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | Current concepts in melanoma management. |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Review (Japanese) | Gan to Kagaku Ryoho | Chemotherapy for head and neck angiosarcoma, including the CYVADIC regimen, which contains dacarbazine. Prognosis remains extremely poor. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohort (6 patients) | Ear, Nose & Throat Journal | Clinicopathological and genetic features of head and neck malignant paragangliomas. |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective cohort | Int J Radiat Oncol Biol Phys | Radiotherapy of esthesioneuroblastoma, a rare intranasal tumor. Radiotherapy only, not dacarbazine. |

Most of the retrieved literature is indirect: it involves a different drug, a different disease, or both. None of it shows dacarbazine efficacy in upper aerodigestive tract neoplasm.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075259 | Dacarbazine | Injection, powder, for solution | Meitheal Pharmaceuticals Inc. |
| ANDA075371 | Dacarbazine | Injection, powder, for solution | Fresenius Kabi USA, LLC |
| ANDA075812 | Dacarbazine | Injection, powder, lyophilized, for solution | Hikma Pharmaceuticals USA Inc. |

All products are injectable. One record (ANDA075371) appeared twice in the input and is listed once here.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Expected to be significant for this class. Please refer to the package insert for specifics. |
| Emetogenicity Classification | Moderate to high (typical for dacarbazine-type alkylators). Confirm against the package insert. |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are based on general drug-class knowledge, not on data in the Evidence Pack. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the only linked trial tested temozolomide, was terminated, and has no efficacy conclusion. No dacarbazine-specific evidence exists for this indication, so the evidence level is L4.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are required for any safety screening.
- Mechanism-of-action data for dacarbazine (for example, from DrugBank).
- Dacarbazine-specific clinical or preclinical evidence in upper aerodigestive tract tumors.
- The trial's termination reason and results for NCT00423150, to judge how far the temozolomide class-level signal carries over.
- A clear definition of which tumor subtypes fall under "upper aerodigestive tract neoplasm".
- Route compatibility assessment (dacarbazine is injectable only).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

