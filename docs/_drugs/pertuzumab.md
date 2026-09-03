---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 1034
evidence_level: L5
indication_count: 10
---

# Pertuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab is a HER2-targeted monoclonal antibody used in combination regimens for HER2-positive breast cancer.
The TxGNN model predicts it may be effective for **progesterone-receptor (PR) positive breast cancer**,
with **10 clinical trials** and **20 publications** currently supporting this direction — though this largely reflects a hormone-receptor subgroup of the drug's existing HER2-positive population rather than an independent new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no license entries); clinical trial text confirms established use in HER2-positive breast cancer |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on known information, pertuzumab is a recombinant humanized monoclonal antibody that binds the HER2 extracellular dimerization domain (subdomain II), blocking HER2/HER3 heterodimerization and downstream signaling. It is used in combination with trastuzumab and taxane chemotherapy, and its efficacy in HER2-positive breast cancer has been established through multiple pivotal trials (e.g., NeoSphere, CLEOPATRA-family programs).

PR-positive breast cancer and HER2-positive breast cancer are not mutually exclusive — roughly half of HER2-overexpressing tumors co-express hormone receptors (ER and/or PR). The TxGNN prediction here largely captures this **HR+/HER2+ intersection** rather than an independent mechanistic extension: pertuzumab's anti-HER2 activity is only pharmacologically relevant when HER2 is co-expressed. Several trials in the evidence set (e.g., NEOADAPT, PERTAIN, WSG-TP-II) specifically test pertuzumab-based regimens combined with endocrine therapy in HR+/HER2+ patients, supporting the biological plausibility of this indication — but strictly within HER2-positive disease. If a patient is HER2-negative, the mechanistic link does not hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant study of Herceptin/docetaxel/pertuzumab combinations in HER2+ breast cancer; a key early registration-supporting trial |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | QL1209 (pertuzumab biosimilar) vs. reference pertuzumab + docetaxel in early/locally advanced HER2+, ER/PR-negative breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs. placebo added to neoadjuvant ddAC-PacHP (incl. pertuzumab) in early HER2+ breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | BCD-178 vs. Perjeta as neoadjuvant therapy in HER2+, ER/PR-negative breast cancer |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalation of adjuvant chemotherapy in HER2+/ER-negative/node-negative early breast cancer after pCR with dual HER2 blockade |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab preoperative therapy; examines impact of HER2 heterogeneity on treatment response |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023: lapatinib + trastuzumab ± endocrine therapy (12 vs. 24 weeks) in HER2-overexpressing breast cancer |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | NEOADAPT: neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab without chemotherapy in HR+/HER2+ localized breast cancer |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective multicenter study on HER2-low prevalence, treatment patterns and outcomes in metastatic breast cancer |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Weekly neoadjuvant paclitaxel in Nigerian women with breast cancer; withdrawn, no enrollment |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2, PERTAIN) | J Clin Oncol | Trastuzumab + aromatase inhibitor ± pertuzumab as first-line therapy in HER2+/HR+ metastatic/locally advanced breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (final analysis) | Ann Oncol | WSG-ADAPT HER2+/HR- trial: 12-week neoadjuvant dual HER2 blockade ± weekly paclitaxel, de-escalation strategy |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (biosimilar equivalence) | Br J Cancer | QL1209 (pertuzumab biosimilar) equivalence trial vs. reference pertuzumab in HER2+, ER/PR-negative breast cancer |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT (DECRESCENDO) | Future Oncol | Chemotherapy de-escalation trial design in HR-negative, HER2-positive, node-negative early breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Long-term follow-up cohort | Lancet Oncol | NeoSphere 5-year analysis: neoadjuvant pertuzumab + trastuzumab improves pathological complete response |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | Comparative cohort | JAMA Oncol | WSG-TP-II: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [40282499](https://pubmed.ncbi.nlm.nih.gov/40282499/) | 2025 | Cohort | Cancers | Adjuvant metronomic chemotherapy plus targeted/anti-hormonal therapy proposal for HER2+/ER-PR+ breast cancer |
| [40739524](https://pubmed.ncbi.nlm.nih.gov/40739524/) | 2025 | Real-world cohort | Br J Clin Pharmacol | Real-world treatment patterns in HR-positive metastatic breast cancer in the USA |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline/Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | Review of HR+/HER2+ breast cancer biology and treatment landscape |

## US Market Information

Pertuzumab currently has **no NDA/license records** in this evidence pack (`total_licenses = 0`, market status "Not Marketed"). No product, dosage form, or approved-indication data is available to tabulate.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; HER2/HER3 dimerization inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as monotherapy; increases to moderate when combined with taxane chemotherapy (as in standard pertuzumab regimens) — please refer to the package insert for specifics |
| Emetogenicity Classification | Low (as monoclonal antibody); combination regimens follow the emetogenicity of the co-administered chemotherapy |
| Monitoring Items | Cardiac function (LVEF) at baseline and during treatment — a class-characteristic risk for anti-HER2 antibodies; CBC and infusion-reaction monitoring when combined with chemotherapy |
| Handling Protection | Standard biologic/monoclonal antibody handling precautions; not classified as a conventional cytotoxic requiring cytotoxic drug handling protocols |

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are available in this evidence pack — DG001 identifies TFDA/US labeling warnings and contraindications as a blocking data gap.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (PR-positive breast cancer) is supported by L1-level evidence, including multiple completed/ongoing RCTs directly evaluating pertuzumab-based regimens in HR+/HER2+ populations (e.g., PERTAIN, WSG-ADAPT, WSG-TP-II, DECRESCENDO). However, this predicted indication is a hormone-receptor subgroup within the drug's existing HER2-positive approved population, not an independent mechanistic extension — HER2-positive status remains a prerequisite. Lower-ranked predictions (ranks 5–10: ectomesenchymoma, HHV-8-related tumor, etc.) have no clinical or literature support (L4–L5) and should be held.

**To proceed, the following is needed:**
- TFDA/FDA labeling data — warnings, contraindications, and DDI information (blocking gap DG001)
- Confirmed mechanism of action documentation (gap DG002)
- Verification of HER2 status as an eligibility criterion in any protocol targeting PR+ breast cancer
- Clarification of current US market/licensing status, since pertuzumab (Perjeta®) is known to be marketed elsewhere but shows zero licenses in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

