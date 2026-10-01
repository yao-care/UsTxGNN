---
layout: default
title: Olaparib
parent: High Evidence (L1-L2)
nav_order: 986
evidence_level: L1
indication_count: 1
---

# Olaparib
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP inhibitor, originally developed for maintenance treatment of BRCA-mutated ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, and the evidence is strongest in germline BRCA1/2-mutated, HER2-negative disease.
Currently **50 clinical trials** and **20 publications** are linked to this prediction, including several Phase 3 randomized trials in breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRCA-mutated ovarian cancer (from trial descriptions; the US label text was not supplied) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (all under NDA208558) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Olaparib inhibits PARP1/2. In tumors with defective homologous recombination repair (HRR), such as those with germline BRCA1/2 mutations, blocking PARP-mediated repair of single-strand breaks causes synthetic lethality. Detailed DrugBank mechanism-of-action text was not available. The mechanism above is taken from the evidence pack's repurposing rationale and the trial and literature descriptions.

Breast and ovarian cancers share BRCA-driven DNA repair deficiency. The literature shows Phase 3 benefit in HER2-negative breast cancer with germline BRCA1/2 mutations, in both the metastatic setting (OlympiAD) and the adjuvant setting (OlympiA). Phase 2 data in non-BRCA HRR-mutated disease (TBCRC 048, including PALB2) extend the mechanism beyond BRCA. The high TxGNN score is consistent with this body of evidence.

Two caveats apply:
- **Benefit is biomarker-restricted.** It should not be generalized to unselected breast cancer.
- **This is largely confirmation of an existing use, not a novel repurposing.** Breast cancer with a germline BRCA mutation is a labeled use in many jurisdictions. Check the current US labeling before treating this as repurposing.

## Clinical Trial Evidence

Of the 50 registered trials, the most relevant to breast cancer are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin plus olaparib, then olaparib alone vs capecitabine, in BRCA1/2-mutated HER2-negative advanced breast cancer. Phase 1 established the combination dose. |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC: biomarker-guided pre-surgical treatment in high-risk breast cancer, with olaparib as one targeted arm. |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab plus ablative radiotherapy, with or without olaparib, in metastatic triple-negative or HR+/HER2− breast cancer. |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Olaparib with or without elacestrant in HR+/HER2− locally advanced or metastatic breast cancer with gBRCA1/2 mutations. |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib alone or with durvalumab in early-stage HER2-negative breast cancer with BRCA mutations. |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Prospective study of olaparib in Indian patients with ovarian cancer or gBRCA1/2-mutated metastatic breast cancer. |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | Early olaparib (AZD2281) study in BRCA-mutated or triple-negative breast cancer and ovarian cancer, measuring response rate. |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiation therapy in inflammatory, locally advanced or metastatic triple-negative breast cancer (TNBC). |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib plus navitoclax in BRCA1/2- or PALB2-mutated TNBC and recurrent high-grade serous ovarian cancer. |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recruiting | 2900 | ComboMATCH: large biomarker-driven platform; the olaparib-breast subset is unclear. |

Most registered breast-cancer trials are early-phase or combination studies. The pivotal Phase 3 evidence comes from the publications below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib in BRCA1/2-mutated early breast cancer. |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival analysis of adjuvant olaparib vs placebo in high-risk, HER2-negative early breast cancer. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib in metastatic breast cancer with a germline BRCA mutation. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final overall survival and tolerability vs physician's-choice chemotherapy. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up. In the final analysis, median OS was 19.3 vs 17.1 months (P = 0.513), with a significant PFS benefit. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 trial | J Clin Oncol | TBCRC 048: olaparib in metastatic breast cancer with somatic BRCA1/2 or other HRR-gene mutations. |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 RCT | Cancer Cell | I-SPY2: durvalumab plus olaparib and paclitaxel raised pathologic complete response rates in HER2-negative disease (20%–37% overall). |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Phase 2 trial | Breast | NOBROLA: olaparib in advanced TNBC with HRD but no germline BRCA1/2 mutation. |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Real-world study | Breast Cancer Res Treat | LUCY final analysis. The interim median PFS was 8.11 months, similar to the olaparib arm of OlympiAD (7.03 months). |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Target Oncol | Overview of PARP inhibitors in breast cancer. Olaparib and talazoparib are approved as monotherapy for gBRCA-mutated, HER2-negative disease. |

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA208558 | Lynparza (AstraZeneca Pharmaceuticals LP) | Tablet, film coated (oral) |

The source data holds four identical license records, all under NDA208558. Approved indication text was not provided in these records.

## Cytotoxicity

The pack contains no toxicity data. The entries below reflect general knowledge of the PARP inhibitor class and should be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | Medium (anemia is commonly reported; hematologic toxicity and rare myeloid malignancies are class concerns) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC (with differential), liver and renal function |
| Handling Protection | Follow institutional hazardous-drug handling policies |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 RCTs (OlympiAD and OlympiA) support olaparib in germline BRCA1/2-mutated, HER2-negative breast cancer, and Phase 2 data suggest a signal in other HRR-mutated disease. Benefit is restricted to biomarker-selected patients. Safety information is missing from the pack, so this cannot yet advance to full safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the blocking gap)
- The US approved-indication text, to confirm whether breast cancer is already labeled
- A biomarker-selection requirement (germline BRCA1/2 testing, and HRR testing if extending beyond BRCA)
- DrugBank mechanism-of-action data
- A hematologic monitoring plan
- Results from the ongoing HR+ and neoadjuvant combination trials (for example NCT06201234 and NCT05498155)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

