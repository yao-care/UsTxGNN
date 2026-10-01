---
layout: default
title: Topotecan
parent: Model Prediction Only (L5)
nav_order: 1243
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Solid-Tumor Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a topoisomerase I-inhibiting chemotherapy drug that is already marketed in the US as injection and oral capsule products. The supplied license records do not state its approved indications.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **5 registered clinical trials** and **20 publications** retrieved. Most of these are indirect, preclinical or early-phase, and no completed breast-specific randomised trial is confirmed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records. A trial summary in the evidence pack describes topotecan as used for lung cancer. |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (the pack lists L2, but no completed Phase 2/3 RCT in breast cancer is confirmed, so L2 is not met) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 (NDAs and ANDAs combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in DrugBank for this record. Based on general pharmacology, topotecan is a topoisomerase I inhibitor. It causes DNA damage in rapidly dividing cells, which is the basis of its use in solid tumors.

Preclinical work supports activity in breast cancer models. A CRISPR screen found that topoisomerase 1 inhibition is synthetically lethal in MYC-driven breast cancer cells (PMID 37987734). A 2025 study identified TFDP1 as a therapeutic target for topotecan in triple-negative breast cancer (PMID 40300683). Metronomic topotecan plus pazopanib was also effective in triple-negative breast cancer models (PMID 26623560).

A known limitation is that topotecan is a BCRP (ABCG2) substrate, so efflux-mediated resistance is a recognised problem in breast cancer cells (PMID 31408695, 10930538). Human data are limited to older Phase 2 and pilot studies. One of these reported no evidence of increased efficacy with continuous infusion (PMID 9413954).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | Not reported | Intensive-dose topotecan, ifosfamide/mesna and etoposide (TIME) followed by autologous stem cell rescue in metastatic breast cancer. Most directly relevant trial, but terminated. |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs physician's-choice single-agent chemotherapy in gBRCA-mutated platinum-sensitive relapsed ovarian cancer. Topotecan's role is not confirmed, and it is not a breast cancer trial. |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab/olaparib/cediranib combinations vs standard chemotherapy in platinum-resistant ovarian cancer. Indirect. |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with standard chemotherapies in advanced malignancies. Safety data only. |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid drug-screen-guided chemotherapy selection in refractory solid tumours. Does not test topotecan efficacy specifically. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase 2 | Am J Clin Oncol | CALGB trial of topotecan in previously treated advanced breast cancer (47 eligible patients). The response result is not shown in the available excerpt. |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase 2 | Br J Cancer | Continuous-infusion topotecan in advanced breast cancer and NSCLC. No evidence of increased efficacy. |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot study | Onkologie | Topotecan as primary chemotherapy for brain metastases in metastatic breast cancer. |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynakol Geburtshilfliche Rundsch | Overview of new drugs for breast carcinoma. |
| [7910993](https://pubmed.ncbi.nlm.nih.gov/7910993/) | 1994 | Review | World J Surg | Management of metastatic breast cancer. General background. |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | Int J Biol Macromol | TFDP1 drives triple-negative breast cancer and is a therapeutic target for topotecan. |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical | Cancer Res | Topoisomerase 1 inhibition causes R-loop accumulation and synthetic lethality in MYC-driven breast cancer cells. |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan plus pazopanib was potent in models of primary and metastatic triple-negative breast cancer. |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacol Res | Daidzein enhanced topotecan's anticancer effect and reversed BCRP-mediated resistance in breast cancer. |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical | Anticancer Res | Xenograft comparison of doxorubicin, cisplatin, irinotecan and topotecan in colon, lung and breast carcinoma. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091089 | Topotecan Hydrochloride (Fresenius Kabi USA) | Injection, powder, lyophilized, for solution | Not listed in supplied data |
| NDA020981 | HYCAMTIN (Sandoz) | Capsule | Not listed in supplied data |
| ANDA204406 | Topotecan (Accord Healthcare) | Injection | Not listed in supplied data |
| NDA200582 | Topotecan (Hospira) | Injection, solution, concentrate | Not listed in supplied data |
| ANDA202351 | Topotecan hydrochloride (Accord Healthcare) | Injection, powder, lyophilized, for solution | Not listed in supplied data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High. Myelosuppression was the major toxicity in a topotecan Phase 2 trial in germ cell tumors (PMID 8617580), with a median nadir neutrophil count of 1.55 cells/mm3 and platelet count of 20,500 cells/mm3. |
| Emetogenicity Classification | Low to moderate (general drug-class knowledge, not from the evidence pack) |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.92%), but the human evidence in breast cancer is thin. It consists of one terminated Phase 2 trial, older single-arm Phase 2 and pilot studies, and one study reporting no efficacy gain with continuous infusion. The rest is preclinical. The package-insert safety review is also still missing, and that gap blocks safety screening. The prediction is best treated as a research question, not a development candidate.

The other predicted indications add little. Adult germ cell tumor has only indirect evidence, and a small Phase 2 trial found no responses in 14 evaluable patients with cisplatin-refractory disease (PMID 8617580). The eight testicular yolk sac tumor subtypes have no trials or literature and are likely artifacts of a shared parent term.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to clear the blocking safety data gap
- Detailed mechanism-of-action data from DrugBank
- The approved-indication text for each US license, to establish the original indication
- The full records of NCT00006032 and NCT02282020, to confirm whether topotecan was tested in breast cancer
- The response results of the CALGB Phase 2 trial (PMID 10362325)
- A comparison of topotecan against current standard breast cancer therapy, including a plan to address BCRP-mediated resistance

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

