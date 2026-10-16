---
layout: default
title: Olaparib
parent: High Evidence (L1-L2)
nav_order: 986
evidence_level: L1
indication_count: 1
monitor_inn: "OLAPARIB"
predicted_indications: ["female breast carcinoma"]
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP inhibitor, originally used to treat ovarian cancer, particularly BRCA-associated disease.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **30 clinical trials** and **20 publications** currently supporting this direction, including multiple randomized Phase 3 studies in BRCA-mutated breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and hereditary breast and ovarian cancer syndrome; the license record carries no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on established PARP inhibitor pharmacology, olaparib blocks PARP enzymes involved in repairing DNA single-strand breaks. In cells that cannot repair double-strand breaks through homologous recombination, such as those with germline BRCA1/2 mutations, this leads to replication fork collapse and cell death (synthetic lethality).

Ovarian cancer and breast cancer share this vulnerability. BRCA1/2 mutations drive both hereditary breast and ovarian cancer syndrome and a subset of breast tumours, so a drug that works in BRCA-associated ovarian cancer is mechanistically expected to work in BRCA-mutated breast cancer.

Benefit appears to depend on a biomarker. The evidence centres on gBRCA1/2 carriers, and possibly on alterations in other homologous recombination repair genes such as PALB2 (TBCRC 048). Selecting patients by BRCA/HRD testing is therefore a key guardrail. The very high TxGNN score is consistent with this mechanistic and clinical convergence.

## Clinical Trial Evidence

The data include 30 trials. The table lists the most relevant ones, based on the relevance grading and design.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | Open-label olaparib (AZD2281) in known BRCA-mutated or triple-negative breast cancer and tubo-ovarian carcinoma; response rate and correlative markers (direct evidence) |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Post-marketing study in Indian patients with platinum-sensitive relapsed ovarian cancer and gBRCA-mutated metastatic breast cancer |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab plus ablative radiotherapy with or without olaparib in metastatic triple-negative or HR+/HER2- breast cancer |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Completed | 118 | PI3K inhibitor (BKM120 or BYL719) plus olaparib in recurrent triple-negative breast cancer or high-grade serous ovarian cancer; dose and safety |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1/2 | Unknown | 100 | Lurbinectedin (PM01183) plus olaparib in advanced solid tumours |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib followed by olaparib vs capecitabine in BRCA-mutated HER2-negative advanced breast cancer |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | Active, not recruiting | 155 | Cediranib plus olaparib vs olaparib alone in recurrent ovarian cancer or triple-negative breast cancer |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib plus navitoclax in triple-negative breast cancer and high-grade serous ovarian cancer |
| [NCT07695259](https://clinicaltrials.gov/study/NCT07695259) | Phase 4 | Recruiting | 45 | Olaparib with trastuzumab and pertuzumab as neoadjuvant therapy in elderly HER2-positive breast cancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiotherapy in triple-negative breast cancer |

Most breast-specific trials are early-phase combination studies. The strongest efficacy evidence for breast cancer comes from the large randomized trials in the literature below (OlympiAD, OlympiA, PARTNER), which are not all listed here as registered trials.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib in gBRCA1/2-mutated early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival analysis in high-risk, HER2-negative early breast cancer with gBRCA1/2 variants |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib in metastatic breast cancer with a germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final overall survival and tolerability vs physician's choice chemotherapy |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | Extended follow-up | Eur J Cancer | OlympiAD extended follow-up for overall survival and safety |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | Phase 2/3 RCT | Nature | PARTNER: neoadjuvant olaparib with carboplatin-paclitaxel in gBRCA wild-type triple-negative breast cancer (n=559) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 | J Clin Oncol | TBCRC 048: olaparib in metastatic breast cancer with somatic BRCA1/2 or other homologous recombination gene mutations |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Phase 2 | J Clin Oncol | Olaparib monotherapy in advanced cancers with a germline BRCA1/2 mutation |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 | Cancer Cell | I-SPY2: durvalumab plus olaparib and paclitaxel raised pathologic complete response rates in HER2-negative breast cancer |
| [32249603](https://pubmed.ncbi.nlm.nih.gov/32249603/) | 2020 | Review | Future Oncol | Review of olaparib in advanced breast cancer |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208558 | Lynparza (AstraZeneca Pharmaceuticals LP) | Film-coated tablet | No indication text recorded; status: cancelled |

The only US authorization on record is cancelled, so the current US marketing status of olaparib should be verified against FDA sources.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor, DNA-damage-repair inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine monitoring typically includes CBC and liver and renal function |
| Handling Protection | Please refer to the package insert and institutional policy for handling of hazardous oral anticancer drugs |

## Safety Considerations

**Drug Interactions** (100 interactions were found in the DDI query; the main ones are listed below):
- **Major**: Aprepitant, Dexamethasone, Clarithromycin
- **Moderate**: Metformin, Bupropion, Cimetidine, Miconazole, Clotrimazole, Glyburide, Ondansetron, Repaglinide, Rosuvastatin, Simvastatin, among others
- **Minor**: Prucalopride

The major interactions include commonly co-prescribed drugs (antiemetics, corticosteroids, a macrolide antibiotic), so co-medication review is important. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large randomized Phase 3 trials (OlympiAD, OlympiA) and a Phase 2/3 trial (PARTNER) support olaparib in breast cancer, and the mechanism (synthetic lethality in BRCA/HRD tumours) is coherent with its ovarian cancer use. The benefit is limited to biomarker-selected patients, and key regulatory and safety data are missing.

**To proceed, the following is needed:**
- Patient selection guardrail: confirmed gBRCA1/2 mutation (and HRD/HRR testing where relevant)
- Package insert warnings and contraindications, which are missing from the data compiled for this report
- Mechanism of action data from DrugBank to replace the pharmacology-based rationale
- Clarification of current US regulatory status, since the only NDA on record is cancelled
- A co-medication review plan for the major interactions (aprepitant, dexamethasone, clarithromycin)
- Safety monitoring plan, including myelosuppression and special populations such as older adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

