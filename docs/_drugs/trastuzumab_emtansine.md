---
layout: default
title: Trastuzumab Emtansine
parent: Model Prediction Only (L5)
nav_order: 1252
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab emtansine (T-DM1, brand name Kadcyla) is a HER2-targeted antibody-drug conjugate. It is established in HER2-positive breast cancer, but the approved indication text is not in this record.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**.
This prediction is supported by **4 clinical trials** and **15 publications**, mostly indirect HER2-axis evidence rather than PR-specific results.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 (per Evidence Pack scoring; no completed T-DM1 trial specific to PR-positive disease is confirmed) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 entries, both under the same application (BLA125427) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Based on known information, T-DM1 combines trastuzumab with the microtubule inhibitor DM1. It delivers DM1 to HER2-overexpressing cells and keeps trastuzumab's HER2 signaling blockade. Its activity depends on HER2 overexpression, not on progesterone-receptor (PR) status.

PR-positive disease is relevant mainly in the HR+/HER2+ (luminal HER2-positive) subgroup. The TxGNN score of 0.998 reflects graph proximity to HER2-positive breast cancer, not a PR-specific mechanism. Many breast tumors are both PR-positive and HER2-positive, so the prediction is best read as a subpopulation of established HER2-positive use. It is not a separate new disease.

The guardrail is to restrict use to **confirmed HER2-positive** disease. PR-positive, HER2-negative tumors have no mechanistic rationale for T-DM1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Preoperative T-DM1 plus pertuzumab in early HER2-positive breast cancer, studying the impact of HER2 heterogeneity. It is on the HER2 axis but shows no PR-stratified results. |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (observational) | Completed | 1151 | Retrospective study of HER2-low prevalence and treatment patterns in metastatic breast cancer. It is not T-DM1 efficacy evidence. |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | Chemotherapy de-escalation in ER-negative, node-negative HER2+ disease after pathological complete response. The population does not match PR-positive disease. |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | Randomized, double-blind trial (IMpassion050) of atezolizumab vs placebo with neoadjuvant chemotherapy plus trastuzumab and pertuzumab in early HER2+ breast cancer. T-DM1 is not confirmed as the test agent, so it cannot count as direct evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer. |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline | J Clin Oncol | Earlier ASCO guideline update for advanced HER2-positive breast cancer, based on a systematic review of 622 articles. |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guideline | J Clin Oncol | Original ASCO guideline on systemic therapy for advanced HER2-positive breast cancer. |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline | Eur J Cancer | EGTM biomarker guideline. ER and PR guide endocrine therapy, while HER2 status determines anti-HER2 therapy, including ado-trastuzumab emtansine. |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | Review of HR+/HER2+ treatment. Hormone plus anti-HER2 combinations without chemotherapy give long-term control in some patients, and T-DM1 is among the novel agents discussed. |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Review of targeted and cytotoxic inhibitors in breast cancer, framed by HER2, HR, ER and PR status. |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohort (real-world) | Sci Rep | ChangeHER analysis of HER2-positivity gain in metastatic breast cancer treated with pertuzumab and/or T-DM1. |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Review | Clin Adv Hematol Oncol | Overview of metastatic breast cancer subtypes (including HER2+ with ER+ or ER−) and recent data. |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Case report | Case Rep Oncol | Dose-reduced T-DM1 was active and safe in a patient with acute hepatic dysfunction. |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Case report | BMJ Case Rep | Receptor conversion occurs in up to 32% of breast cancer patients, so receptor status may need re-testing. |

No randomized controlled trial of T-DM1 specific to PR-positive disease appears in this record.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA125427 | KADCYLA (Genentech, Inc.) | Injection, powder, lyophilized, for solution (injectable) |

The record lists two entries, both for BLA125427 with identical product details. The approved indication text is blank, so the label indication could not be confirmed from this record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed antibody-drug conjugate carrying the microtubule inhibitor DM1) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions; follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
T-DM1 has strong clinical grounding in HER2-positive breast cancer, and PR-positive tumors often co-express HER2. However, benefit follows HER2 status, not PR status. The returned trials and publications are mostly indirect, and none is a completed T-DM1 trial specific to PR-positive disease.

**To proceed, the following is needed:**
- Restrict use to confirmed HER2-positive disease, and exclude PR-positive, HER2-negative tumors.
- Obtain PR-stratified outcomes from the pivotal T-DM1 trials.
- Confirm whether T-DM1 is the test agent in NCT03726879.
- Review the HR+/HER2+ randomized evidence (e.g., the WSG-ADAPT-TP trial, PMID 36809046) that sits under the luminal indication record.
- Obtain the package insert, including the approved indication text, warnings and contraindications. The safety data and mechanism of action are currently missing and block safety screening.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

