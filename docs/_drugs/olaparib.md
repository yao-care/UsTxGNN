---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 986
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP1/2 inhibitor whose established use, per the clinical trial evidence in this pack, is maintenance therapy for platinum-sensitive, BRCA1/2-mutated ovarian, fallopian tube, and peritoneal cancer. The TxGNN model additionally flags **Female Breast Carcinoma** as a high-confidence indication, and this direction is already strongly corroborated by real-world evidence — **50 clinical trials** and **20 publications**, including two pivotal completed Phase 3 RCTs (OlympiAD, OlympiA).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory license data (0 licenses on file); per trial-derived evidence (NCT05078671), historically used for maintenance treatment of platinum-sensitive, BRCA-mutated advanced ovarian/fallopian tube/peritoneal cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

A formal mechanism-of-action record is not yet populated in the regulatory database (data gap, see below). However, the evidence pack's repurposing rationale and multiple trial descriptions consistently characterize olaparib as a PARP1/2 inhibitor that exploits **synthetic lethality**: in tumor cells carrying BRCA1/2 pathogenic mutations (homologous recombination deficiency, HRD), PARP inhibition blocks base-excision repair of single-strand DNA breaks, causing replication fork collapse and selective death of BRCA-deficient cells while sparing normal cells.

The original evidence base for this mechanism was built in BRCA-mutated ovarian cancer, but BRCA1/2 mutations and HRD are shared molecular features across ovarian and breast tumors — both are gynecologic/hormone-pathway malignancies with substantial overlap in hereditary cancer syndromes (hereditary breast and ovarian cancer, HBOC). This shared biology is why the same synthetic-lethality mechanism translates directly to breast cancer.

This is not a purely theoretical extrapolation: it is already backed by two completed Phase 3 RCTs specific to breast cancer — **OlympiAD** (metastatic, germline BRCA-mutated, HER2-negative breast cancer) and **OlympiA** (adjuvant, high-risk early breast cancer) — both demonstrating significant efficacy benefit. The clinical population, however, remains restricted to patients with confirmed germline (or in some studies somatic) BRCA1/2 mutations or broader HRD status, not unselected breast cancer patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05078671](https://clinicaltrials.gov/study/NCT05078671) | Phase 4 | Recruiting | 160 | Post-marketing PK-boosting study to improve olaparib exposure, tolerability, and cost-effectiveness across approved indications including BRCA-mutated breast cancer |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | Rollover study providing continued olaparib access/long-term safety data for patients benefiting from prior oncology trials |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1/2 | Completed | 25 | Carboplatin-olaparib followed by olaparib monotherapy vs. capecitabine as first-line therapy in BRCA1/2-mutated, HER2-negative advanced breast cancer |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab + ablative radiotherapy ± olaparib in metastatic triple-negative/HR+/HER2- breast cancer |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC personalized-medicine platform trial in high-risk breast cancer, with olaparib as one treatment arm |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Olaparib + elacestrant vs. olaparib alone in HR+/HER2- advanced breast cancer with gBRCA1/2 mutations |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib monotherapy vs. olaparib + durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Real-world Indian cohort of olaparib in gBRCA1/2-mutated metastatic breast cancer and platinum-sensitive relapsed ovarian cancer |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | AZD2281 (olaparib) + carboplatin in BRCA1/2-mutated familial and sporadic triple-negative breast/ovarian cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | AZD2281 (olaparib) response rate and correlative biomarkers in known-BRCA and triple-negative breast cancer, plus ovarian carcinoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | NEJM | OlympiA primary results: adjuvant olaparib significantly reduces recurrence in BRCA1/2-mutated early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | NEJM | OlympiAD primary results: olaparib shows antitumor activity in metastatic breast cancer with germline BRCA mutation |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | OlympiA overall survival analysis confirming sustained benefit of adjuvant olaparib in high-risk early breast cancer |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD final overall survival and tolerability vs. chemotherapy of physician's choice |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | European Journal of Cancer | OlympiAD extended follow-up confirming long-term safety and OS trend favoring olaparib |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 Cohort | J Clin Oncol | TBCRC 048: olaparib response extends beyond germline BRCA1/2 to somatic and other HRR gene mutation carriers |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 Cohort | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increases pathologic complete response in HER2-negative breast cancer |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Phase 2 | Breast (Edinburgh) | NOBROLA: olaparib monotherapy effective in HRD-positive triple-negative breast cancer without germline BRCA1/2 mutation |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Real-world | Breast Cancer Res Treat | LUCY final analysis: real-world effectiveness and safety of olaparib consistent with OlympiAD trial data |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for gBRCA-mutated, HER2-negative breast cancer |

## US Market Information

No market authorizations are currently on file — the regulatory record shows 0 licenses and a "Not Marketed" status for this drug entity in this dataset.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor; synthetic-lethality mechanism, not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is met with two completed Phase 3 RCTs (OlympiAD, OlympiA) plus consistent real-world confirmation (LUCY), strongly supporting olaparib's efficacy in breast cancer — but strictly within the biomarker-defined population (germline/somatic BRCA1/2-mutated or HRD-positive), not all breast cancer patients. Formal safety labeling and MOA documentation are still missing, which blocks a full go decision.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings, contraindications, and DDI data (currently a blocking data gap — DG001)
- Formal MOA documentation from DrugBank (DG002)
- Confirmation of BRCA1/2 germline mutation or HRD testing as a mandatory patient-selection gate before any indication expansion
- Regulatory pathway assessment given the current "Not Marketed" status and zero licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

