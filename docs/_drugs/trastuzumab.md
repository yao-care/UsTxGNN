---
layout: default
title: Trastuzumab
parent: Model Prediction Only (L5)
nav_order: 1250
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: predicted new indication Malignant cutaneous granular cell skin tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## One-Sentence Summary

Trastuzumab is a HER2-targeted monoclonal antibody, originally used to treat HER2-positive breast carcinoma.
This is best understood as an extension within the already established HER2-positive breast cancer indication rather than a true repurposing, because benefit depends on HER2 status, not progesterone receptor (PR) status.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant cutaneous granular cell skin tumor |
| TxGNN Prediction Score | 0.9948 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 9 of 9) |
| Number of NDAs | 9 (valid: 9) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established knowledge, trastuzumab binds the extracellular domain of HER2. This inhibits downstream signaling and engages immune-mediated killing (antibody-dependent cellular cytotoxicity). Its efficacy in HER2-positive breast cancer is well proven.

PR status does not change this mechanism. Tumours that are both HER2-positive and hormone receptor-positive are an established setting for trastuzumab-based therapy, usually with endocrine therapy added. The prediction therefore mostly reflects an overlap with the approved indication. Benefit applies only to HER2-positive tumours, so patients must be selected by HER2 status. Trastuzumab has no established role in PR-positive tumours that are HER2-negative.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy with or without trastuzumab in node-positive or high-risk node-negative breast cancer; the most direct Phase 3 evidence |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 vs pertuzumab, each with trastuzumab and docetaxel, in HER2+/ER/PR-negative disease |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Completed | 92 | Neoadjuvant paclitaxel and cyclophosphamide with or without trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | Completed | 50 | Neoadjuvant chemotherapy sequence in HER2-positive breast cancer; supportive only |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | Completed | 36 | Cabozantinib alone or with trastuzumab in breast cancer with brain metastases; small, exploratory |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole plus trastuzumab in ErbB2+ and ER/PR+ metastatic breast cancer |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Unknown | 34 | Palbociclib, trastuzumab, pyrotinib and fulvestrant for brain metastases from ER/PR+ HER2+ disease |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib, endocrine therapy and trastuzumab in ER+ HER2+ cancers |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus, letrozole and trastuzumab in HR+ HER2+ advanced cancers |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Withdrawn | 0 | Trastuzumab with or without tamoxifen in HR+ HER2+ stage IV disease; no patients enrolled, so no evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciclib plus trastuzumab, with or without fulvestrant, vs trastuzumab plus chemotherapy in HR+ HER2+ advanced breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: de-escalation with 12 weeks of neoadjuvant trastuzumab and pertuzumab, with or without paclitaxel |
| [41780642](https://pubmed.ncbi.nlm.nih.gov/41780642/) | 2026 | RCT | Ann Oncol | DESTINY-Breast06: trastuzumab deruxtecan in HR+ HER2-low/-ultralow metastatic breast cancer (a different agent) |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis | Lancet | Overview of randomised trials of chemotherapy and hormonal therapy in early breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort | Lancet Oncol | NeoSphere 5-year analysis of neoadjuvant pertuzumab and trastuzumab in HER2+ disease |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Observational | Theranostics | Molecular portraits and trastuzumab responsiveness of ER+/PR+/HER2+ (triple-positive) breast cancer |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Review | Nat Rev Clin Oncol | HER2+/HR+ breast cancer: aromatase inhibitors plus anti-HER2 therapy as a strategy |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | Phase 2a | Lancet Oncol | Zanidatamab plus palbociclib and fulvestrant in HR+ HER2+ metastatic breast cancer (a different agent) |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Targeted and cytotoxic inhibitors in breast cancer, organized by HER2/HR status |

## US Market Information

All nine US listings for trastuzumab products are marked as cancelled. The data compiled for this report do not include approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103792 | Herceptin | Injection, powder, lyophilized, for solution | Not available |
| BLA761106 | Herceptin Hylecta | Injection, solution | Not available |
| BLA761170 | Phesgo | Injection, solution | Not available |
| BLA761073 | Kanjinti | Injection, powder, lyophilized, for solution | Not available |
| BLA761081 | Trazimera | Injection, powder, lyophilized, for solution | Not available |

Four further listings are not shown: HERZUMA (BLA761091), OGIVRI (BLA761074), HERCESSI (BLA761346) and Ontruzant (BLA761100).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low as a single agent; may increase when combined with chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (left ventricular ejection fraction) before and during treatment; CBC when combined with chemotherapy; liver and renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Cardiotoxicity**: The literature compiled for this report discusses trastuzumab-related cardiotoxicity and questions how reversible it is (PMID 17687157). Cardiac monitoring is therefore advisable.
- **Drug Interactions**: 94 interactions were recorded. Examples at **Major** level include deferiprone, samarium (153Sm) lexidronam, adalimumab and baricitinib. Examples at **Moderate** level include paclitaxel, warfarin, azathioprine, alemtuzumab, anakinra and zidovudine.

Warnings and contraindications from the package insert were not available. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 adjuvant trial with 3,270 patients (NCT01275677), plus randomised Phase 2 and Phase 3 literature, supports trastuzumab in HER2-positive disease that includes hormone receptor-positive tumours. This is an extension of the approved HER2-positive indication, so the guardrail is strict HER2 selection. Evidence cannot be extended to HER2-negative PR-positive tumours.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Confirmation of current US marketing status, since all listings show as cancelled
- A cardiac monitoring plan and a HER2 testing requirement for patient selection

---

### Other Predicted Indications (Brief)

- Trastuzumab has no established role in triple-negative disease unless HER2 is expressed.
- Rationale is limited to the HER2-positive luminal B subset.
- The only trial is a not-yet-recruiting study of a different agent.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

