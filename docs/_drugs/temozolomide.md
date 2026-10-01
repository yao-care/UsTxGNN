---
layout: default
title: Temozolomide
parent: High Evidence (L1-L2)
nav_order: 1209
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **2** 
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

# Temozolomide: From Established Glioma Therapy to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy that is already an established standard of care for glioblastoma and anaplastic astrocytoma.
The TxGNN model predicts it may be effective for **adult astrocytic tumour**, and this is closer to confirming a known use than to true repurposing.
Currently, **2 clinical trials** (1 completed Phase 3 RCT) and **20 publications** (including several Phase 3 RCTs) support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (all listed generic products) |
| Recommended Decision | Proceed with Guardrails |

The US license records contain no approved-indication text, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input record. Based on the model's rationale, temozolomide is an oral alkylating agent that methylates DNA at the O6-guanine, N7-guanine and N3-adenine positions. Its cytotoxicity is greatest in tumours with MGMT promoter methylation, which is common in astrocytic gliomas. This fits the very high TxGNN score.

Adult astrocytic tumours, including anaplastic astrocytoma and glioblastoma, are glial-lineage CNS tumours. Temozolomide is already used as standard care for glioblastoma and anaplastic astrocytoma. The prediction therefore mostly confirms a known use rather than opening a new one.

Response is likely to depend on MGMT status, IDH status and WHO grade. Any development plan should stratify by these markers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised comparison of temozolomide vs procarbazine, lomustine and vincristine (PCV) in recurrent WHO grade III/IV astrocytic tumours. It tests temozolomide directly in the target disease. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding and PK safety study of cabozantinib (XL184) with temozolomide and radiotherapy in first-line glioblastoma. Temozolomide is background therapy, so this is weak support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Radiotherapy alone vs radiotherapy plus concomitant and adjuvant temozolomide in glioblastoma (efficacy and safety). |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | Final 5-year analysis of the EORTC-NCIC phase III trial of radiotherapy with temozolomide vs radiotherapy alone in glioblastoma. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 phase 3 trial: dose-dense temozolomide alone vs radiotherapy alone in elderly patients with anaplastic astrocytoma or glioblastoma. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 phase 3 trial: lomustine plus temozolomide vs standard temozolomide in MGMT-methylated glioblastoma. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Maintenance tumour-treating fields plus temozolomide vs temozolomide alone in glioblastoma. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Bevacizumab added to standard temozolomide and radiotherapy in newly diagnosed glioblastoma. |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT | J Neurooncol | Exploratory cohort of newly diagnosed anaplastic astrocytoma or oligo-astrocytoma treated with radiotherapy and temozolomide. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG BN007 phase II/III trial of dual checkpoint blockade in MGMT-unmethylated glioblastoma. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Review of glioblastoma and other primary malignant brain tumours in adults. |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Review of temozolomide as a second-generation alkylating agent for malignant glioma (glioblastoma and anaplastic astrocytoma). |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA207658 | Temozolomide | Capsule | Devatis, Inc. |
| ANDA201742 | Temozolomide | Capsule | Sun Pharmaceutical Industries, Inc. |
| ANDA207658 | Temozolomide | Capsule | Ascend Laboratories, LLC |

Five records were provided. The list above is deduplicated: three of them are Devatis entries under ANDA207658. The only route is oral.

---

## Cytotoxicity

The pack contains no toxicity data. The entries below reflect the drug class, so please confirm them against the package insert warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Medium to high (neutropenia, thrombocytopenia and lymphopenia are expected class effects) |
| Emetogenicity Classification | Low to moderate (oral administration) |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temozolomide is already established in glioblastoma and anaplastic astrocytoma. It is supported by a completed Phase 3 RCT in recurrent grade III/IV astrocytic tumours and by multiple published Phase 3 RCTs. The prediction is therefore well supported, but the safety data gap must be closed before further progression.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap; safety screening cannot proceed without them)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication and label status in the US
- Stratification of any study plan by MGMT status, IDH status and WHO grade

**Related prediction:** Cauda equina neoplasm (score 99.30%) is at evidence level L4, with only case reports and no registered trials. It remains a research question, and I did not evaluate it in this report.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

