---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 896
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Alkylating Chemotherapy to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is a nitrogen mustard alkylating chemotherapy that is currently marketed in the US as injectable products (EVOMELA and IVRA).
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**, but the supporting evidence is thin: **7 linked clinical trials** (all early-phase, mixed-tumor or combination-regimen studies) and **4 publications** (all from 1956-1977, with no abstracts available).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

*Evidence level note: the pipeline labelled this L2. However, the completed Phase 2 studies are single-arm or mixed-population, and no randomized trial is present. Under the L1-L5 rules the supported level is therefore L3, based on historical reviews and case series.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, melphalan is a bifunctional alkylating agent that forms DNA interstrand crosslinks and blocks cell division. Germ cell tumors are generally chemosensitive to DNA-damaging drugs, so an alkylator is mechanistically plausible here. This link comes from general knowledge, not from the supplied record.

The literature supports a historical, not a modern, signal. A 1956 report describes sarcolysin (a melphalan-related alkylator) in testicular seminoma, and 1970s reviews cover chemotherapy of testicular germ cell tumors. The most relevant modern study is a Phase 2 trial of high-dose chemotherapy in poor-prognosis relapsed germ cell tumors (NCT00936936). Its first cycle includes gemcitabine, docetaxel, melphalan and carboplatin.

Two caveats apply. First, melphalan's individual contribution cannot be separated in combination regimens. Second, most other linked trials are high-dose melphalan with stem cell rescue in mixed solid-tumor cohorts, not germ cell-specific studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy in poor-prognosis relapsed germ cell tumors. Cycle 1 is gemcitabine, docetaxel, melphalan and carboplatin; cycle 2 is ifosfamide, carboplatin and etoposide. Direct disease match, but results are not in the pack |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine in mixed solid tumors |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan + melphalan + topotecan with autologous transplant in advanced or recurrent tumors; combination limits attribution |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Autologous transplant with several high-dose regimens for hematologic malignancies and selected solid tumors; heterogeneous population |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis; only indirectly relevant (different route and indication) |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as chemoprotectant with transplant in pediatric solid tumors; tests supportive care, not melphalan efficacy |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | Completed | 174 | Autologous transplant protocols with or without total-body irradiation in mixed malignancies; no germ cell-specific melphalan signal |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | NA | Completed | 36 | Nonmyeloablative allogeneic transplant with melphalan/cladribine or TLI; melphalan is likely conditioning only |

## Literature Evidence

Abstracts were not available for these publications, so the findings below are summarized from titles only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Overview of chemotherapy for testicular germinal tumors |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | The Urologic Clinics of North America | Review of seminoma |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Case series | Voprosy Onkologii | Experience treating testicular seminoma and its metastases with sarcolysin |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Preclinical | Acta - Unio Internationalis Contra Cancrum | Effect of hormonal and alkylating drugs on pituitary follicle-stimulating function; not a direct efficacy study |

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA207155 | EVOMELA (Acrotech Biopharma Inc) | Injection, powder, lyophilized, for solution |
| NDA217110 | IVRA (Apotex Corp) | Injection, solution |

Approved indication text was not provided in the Evidence Pack. Both products are injectable, so any future route-compatibility review would start from intravenous use.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High. The high-dose regimens in the linked trials all require autologous stem cell rescue, which reflects profound marrow suppression |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.77%), but the supporting evidence is weak. There is no randomized trial, the melphalan-containing studies are mostly early-phase mixed-tumor or combination work, and the germ cell literature dates from 1956-1977. Package-insert safety data is also missing, which the Evidence Pack flags as blocking for safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for EVOMELA and IVRA (blocking gap)
- Mechanism of action data from DrugBank
- Results and regimen details for NCT00936936, the only trial that is both germ cell-specific and confirmed to include melphalan
- Full-text review of the historical germ cell literature
- Route and dosing compatibility assessment for a germ cell tumor setting

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

