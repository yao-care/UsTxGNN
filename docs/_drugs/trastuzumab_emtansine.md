---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 1252
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate originally developed and used for HER2-positive breast cancer, combining the anti-HER2 antibody trastuzumab with the cytotoxic payload DM1.
The TxGNN model predicts it may also be effective for **Progesterone-Receptor Positive Breast Cancer**,
with **4 clinical trials** and **15 publications** currently retrieved in support of this direction — though, as discussed below, several of these overlap with the drug's already-established HER2-positive population rather than representing a wholly independent disease target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established global indication for T-DM1/Kadcyla; no formal local approved-indication text is available because the drug is not currently marketed in this jurisdiction) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known information, trastuzumab emtansine is an antibody-drug conjugate (ADC) that couples trastuzumab, an antibody targeting HER2, with DM1, a cytotoxic maytansinoid microtubule inhibitor. Upon binding to HER2-overexpressing tumor cells, the conjugate is internalized and releases DM1 intracellularly, producing a targeted cytotoxic effect. Its efficacy in HER2-positive breast cancer is well established through numerous completed Phase 2/3 trials.

Progesterone-receptor (PR) status is a separate biomarker from HER2 amplification, and a substantial proportion of HER2-positive breast cancers are also hormone-receptor (HR/PR) positive. Anti-HER2 therapies, including T-DM1, are already used in this HR+/HER2+ overlap population regardless of PR status — meaning the TxGNN prediction likely reflects a real, mechanistically grounded overlap rather than an entirely novel disease indication. This is consistent with the underlying mechanism: HER2 expression, not PR status, determines eligibility for T-DM1 binding and cytotoxic delivery.

That said, the retrieved evidence should be interpreted with caution. Of the four clinical trials returned, only two (NCT02326974, NCT04675827) actually administer T-DM1; one (NCT06131424) is a retrospective observational registry on HER2-low disease unrelated to PR status; and one Phase 3 trial (NCT03726879) does not include T-DM1 in its treatment arms at all. This suggests the automated evidence match was driven largely by shared "HER2-positive breast cancer" terminology rather than PR-specific outcome data, and the evidence base should be manually re-curated before advancing beyond an early evaluation stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Evaluates T-DM1 + pertuzumab in the preoperative setting for early-stage HER2-positive breast cancer, examining impact of HER2 heterogeneity on response |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | De-escalation study of neoadjuvant chemotherapy + dual HER2 blockade in HER2-positive, ER-negative, node-negative early breast cancer achieving pathological complete response |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (observational) | Completed | 1,151 | Retrospective study on prevalence and treatment patterns of HER2-low metastatic breast cancer; not specific to PR status or T-DM1 use |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs placebo with neoadjuvant chemo + trastuzumab + pertuzumab in early HER2-positive breast cancer — does **not** include T-DM1 as a study arm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline/Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer, encompassing HR+ and HR- subgroups |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline/Review | J Clin Oncol | ASCO clinical practice guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guideline/Review | J Clin Oncol | ASCO clinical practice guideline for advanced HER2-positive breast cancer, first establishing T-DM1's role in later-line therapy |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline/Review | Eur J Cancer | EGTM biomarker guideline confirming ER/PR and HER2 as co-determinants for selecting anti-HER2 therapy, including T-DM1 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacological Research | Reviews targeted and cytotoxic inhibitors in breast cancer, discussing HER2/HR-stratified management |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Reviews current treatment trends in HR+/HER2+ breast cancer, explicitly discussing T-DM1's role in this overlapping subgroup |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohort/Real-world | Scientific Reports | ChangeHER trial data on prognostic relevance of HER2-positivity gain in metastatic breast cancer treated with pertuzumab/T-DM1 |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Report | Frontiers in Oncology | Case report on pyrotinib + metronomic vinorelbine in HER2-positive breast cancer with leptomeningeal disease |
| [40642740](https://pubmed.ncbi.nlm.nih.gov/40642740/) | 2025 | Case Report | J Medical Cases | Long-term follow-up case of durable response with trastuzumab deruxtecan in HER2-mutated metastatic breast cancer |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Case Report | Case Reports in Oncology | Dose-reduced T-DM1 shown to be active and safe in a patient with acute hepatic dysfunction |

---

## US Market Information

This drug is not currently marketed in this jurisdiction (0 licenses on record); no authorization or approved-indication text is available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-targeted antibody-drug conjugate with cytotoxic maytansinoid [DM1] payload) |
| Myelosuppression Risk | Medium — thrombocytopenia is the most characteristic hematologic toxicity of T-DM1; neutropenia is less prominent than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Platelet count and CBC, liver function tests (hepatotoxicity is a known class effect), left ventricular ejection fraction (cardiac monitoring due to the trastuzumab antibody component) |
| Handling Protection | Yes — as a cytotoxic conjugate, standard hazardous drug handling/reconstitution precautions should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound — PR-positive tumors that co-express HER2 already fall within T-DM1's established therapeutic mechanism — but the automatically retrieved evidence base is only moderate quality (L3) and includes at least one mismatched trial that does not actually use T-DM1, so this should not yet be treated as a validated, independent new indication.

**To proceed, the following is needed:**
- DrugBank MOA data and official approved-indication text (currently data gaps, including the blocking TFDA/local label warnings gap noted in the evidence pack)
- Manual re-review of the four retrieved trials to confirm which genuinely test T-DM1 in a PR-positive (vs. HR-negative or HER2-low) population
- A dedicated subgroup analysis or trial specifically powered on PR status, rather than relying on HER2-positive trials that only incidentally report PR status
- Local safety and drug-interaction data before any market-facing communication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

