---
layout: default
title: Trastuzumab
parent: Moderate Evidence (L3-L4)
nav_order: 1250
evidence_level: L3
indication_count: 10
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Trastuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab is a HER2-targeted monoclonal antibody, established in HER2-positive breast cancer.
The TxGNN model predicts it may be effective for the **normal breast-like subtype of breast carcinoma**,
with **12 registered clinical trials** and **1 publication** returned. Most of that evidence concerns HER2-positive disease rather than this subtype, so support is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 (all listed products are BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, trastuzumab binds the extracellular domain of HER2, mediates antibody-dependent cellular cytotoxicity (ADCC) and blocks HER2 signaling. This effect is well established in HER2-positive breast cancer.

"Normal breast-like" is a PAM50 molecular-subtype label, not a distinct clinical indication. The model likely scores it highly because it sits close to approved breast cancer terms in the knowledge graph. The returned trials mostly enroll HER2-positive or HER2-targeted populations. They do not show that tumors of this subtype respond to trastuzumab, so the mechanistic link here is indirect.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, not recruiting | 55 | Atezolizumab + trastuzumab + vinorelbine in HER2-positive advanced breast cancer; cohorts defined by ER-negative or PAM50 non-luminal disease. Closest subtype overlap, but small and uncontrolled |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Phase 2 | Recruiting | 65 | Neoadjuvant pyrotinib + trastuzumab + nab-paclitaxel in HER2-enriched early or locally advanced breast cancer |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab pre-operative therapy in inflammatory breast cancer |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant weekly paclitaxel with or without carboplatin in triple-negative breast cancer; trastuzumab's role cannot be confirmed |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | Trastuzumab deruxtecan (a different agent) vs CDK4/6 inhibitors; withdrawn with no participants |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | ARIADNE: trastuzumab deruxtecan vs standard preoperative treatment in HER2-positive breast cancer, with biomarker-driven selection |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Neoadjuvant therapy guided by in vitro drug screening on patient-derived tumor-like cell clusters in HER2-positive early breast cancer |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine with neoadjuvant chemotherapy and HER2-targeted antibody therapy |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2-positive breast cancer |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib alone or with fulvestrant in HER2-mutant, non-amplified metastatic breast cancer |

Two further registered trials (NCT05582499, NCT06328387) are not listed; both are unrelated to this subtype and add no direct evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Cohort | Breast Cancer (Tokyo) | Describes morphological and cytopathological features of the basal-like subtype. It mentions "normal breast-like" only as one of five expression-profiling subtypes and has no trastuzumab efficacy data |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761073 | Kanjinti | Lyophilized powder for injection | Amgen, Inc |
| BLA761091 | HERZUMA | Lyophilized powder for injection | Cephalon, Inc. |
| BLA103792 | Herceptin | Lyophilized powder for injection | Genentech, Inc. |
| BLA761074 | OGIVRI | Lyophilized powder for injection | Biocon Biologics Inc. |

The source data lists 13 licenses in total and includes no approved-indication text. Kanjinti appears twice in the extract and is shown once above.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low as a single agent; neutropenia mainly reflects combined chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (LVEF), CBC when combined with chemotherapy, infusion-related reactions |
| Handling Protection | Please refer to the package insert warnings and precautions |

These entries come from general drug-class knowledge, not from the Evidence Pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a molecular-subtype label, not a distinct clinical indication. No trial or publication tests trastuzumab in normal-like tumors, and the evidence reaches only L3. Trastuzumab's benefit depends on HER2 status, and the model score alone does not show that this subtype is HER2-driven.

The other breast cancer predictions are hormone-receptor subgroups of the already-approved HER2-positive indication, not new repurposing. Progesterone-receptor positive (L1) and progesterone-receptor negative (L1) can proceed with guardrails, conditional on confirmed HER2 positivity. Luminal A or B has literature support only (L2), and the remaining predictions are model-only (L5) or indirect (L4) and should be held.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which is a blocking gap for safety screening
- Mechanism of action data, queried from DrugBank
- Evidence on HER2 status in normal breast-like tumors, such as PAM50 subtype versus HER2 IHC/ISH concordance
- Trial or cohort data in a PAM50 normal-like population receiving trastuzumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

