---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 810
evidence_level: L5
indication_count: 1
---

# Irinotecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Irinotecan: From Colorectal Cancer (Established Use) to Female Breast Carcinoma

> Note: This evidence pack contains no Taiwan/US regulatory license records and no `original_indications` entries for irinotecan. "Colorectal cancer" above reflects irinotecan's widely documented pharmacological use (general knowledge), not data extracted from this evidence pack.

## One-Sentence Summary

Irinotecan is a topoisomerase I inhibitor best known as a component of colorectal cancer chemotherapy regimens (e.g., FOLFIRI). The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, supported by **22 clinical trials** and **20 publications**, though the drug currently has **no marketing authorization** on file in this evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`taiwan_regulatory.licenses` and `original_indications` are both empty) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 (1 completed Phase 2 randomized trial of irinotecan monotherapy in breast cancer) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for irinotecan in this evidence pack (`original_moa: [Data Gap]`). Based on generally established pharmacology, irinotecan is a semi-synthetic camptothecin analog that is metabolized to SN-38, its active metabolite, which inhibits topoisomerase I and causes lethal DNA double-strand breaks during replication — its efficacy in colorectal cancer and other solid tumors is well documented.

Female breast carcinoma is mechanistically plausible as a repurposing target because SN-38 (irinotecan's active metabolite) is the payload of sacituzumab govitecan, an antibody-drug conjugate now approved for triple-negative and HR+/HER2- metastatic breast cancer. This validates that SN-38-mediated topoisomerase I inhibition is an active mechanism in breast cancer biology, even though the ADC delivers the payload via a Trop-2-targeting antibody rather than as free irinotecan.

Directly, irinotecan itself has been tested as monotherapy and in combination (with capecitabine, gemcitabine, or targeted agents) in metastatic and triple-negative breast cancer in multiple Phase 1/2 trials, providing direct — not just mechanistic — supporting evidence for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Randomized trial of two irinotecan dosing schedules in metastatic breast cancer after anthracycline/taxane/capecitabine failure |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Single-arm trial of third-line-or-later irinotecan in locally recurrent/metastatic breast cancer (Chinese patients) |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma; dose-finding |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | Irinotecan + UCN-01 (7-hydroxystaurosporine) in triple-negative recurrent breast cancer |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Navicixizumab monotherapy or with paclitaxel/irinotecan, including a TNBC cohort |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | IMMU-132 (SN-38 antibody-drug conjugate) safety/efficacy in epithelial cancers |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101, a nano-particle formulation of SN-38, in advanced solid tumors |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | Nanoliposomal irinotecan (MM-398/nal-IRI); tumor drug level and imaging feasibility study |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | Completed | 38 | Irinotecan (CPT-11) + gemcitabine in solid tumors |
| [NCT02033551](https://clinicaltrials.gov/study/NCT02033551) | Phase 1 | Completed | 47 | Veliparib alone or with carboplatin/paclitaxel or FOLFIRI (irinotecan-containing) in solid tumors |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | RCT | N Engl J Med | ASCENT trial: sacituzumab govitecan-hziy (SN-38 conjugate) improves outcomes in refractory metastatic triple-negative breast cancer |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | RCT | J Clin Oncol | Sacituzumab govitecan in HR+/HER2- metastatic breast cancer |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Clinical trial | J Clin Oncol | Sacituzumab govitecan efficacy/safety in heavily pretreated metastatic TNBC |
| [32727805](https://pubmed.ncbi.nlm.nih.gov/32727805/) | 2020 | Pilot study | Anticancer Res | Irinotecan + S-1 (IRIS) pilot study for advanced/metastatic breast cancer |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | Irinotecan activity across tumor types, including breast cancer |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology (Williston Park) | Rationale for mitomycin + irinotecan combination in advanced breast cancer |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Review | Breast (Edinburgh) | Clinical development of TROP-2-targeting antibody-drug conjugates in metastatic breast cancer |
| [35882754](https://pubmed.ncbi.nlm.nih.gov/35882754/) | 2022 | Preclinical | Breast Cancer (Tokyo) | Trop-2 expression alteration in breast cancer cells by therapeutic agents and tamoxifen resistance |
| [39768216](https://pubmed.ncbi.nlm.nih.gov/39768216/) | 2024 | Review | Cells | Sacituzumab govitecan in refractory triple-negative breast cancer precision medicine |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Clinical trial | Clin Cancer Res | First-in-human trial of anti-Trop-2/SN-38 conjugate sacituzumab govitecan in diverse metastatic solid tumors |

## US Market Information

Currently no marketing authorization records are available — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with 0 total licenses on file in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin class) — based on general pharmacological classification, since DrugBank MOA/category data is not available in this evidence pack |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A completed randomized Phase 2 trial and a supportive literature base (including two completed Phase 3 RCTs for the mechanistically related SN-38 antibody-drug conjugate class) suggest a plausible signal for irinotecan in breast cancer. However, the drug has no Taiwan/US marketing authorization on file, and the missing TFDA label/warnings data is flagged as a **Blocking** gap that prevents any S1 safety assessment.

**To proceed, the following is needed:**
- TFDA (or equivalent) product label with warnings, precautions, and contraindications (Blocking gap DG001)
- Confirmed DrugBank mechanism of action data (High-priority gap DG002)
- Drug-drug interaction (DDI) data — current query returned no results
- Route compatibility assessment between original and predicted-indication use
- Formal relevance grading of the listed clinical trials and literature (currently marked "pending")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

