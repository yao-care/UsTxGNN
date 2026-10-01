---
layout: default
title: Pertuzumab
parent: Model Prediction Only (L5)
nav_order: 1034
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab (Perjeta) is a HER2-targeted antibody. The record lists no original indication, but by general knowledge it is used in HER2-positive breast cancer.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, with **10 clinical trials** and **20 publications** listed for this direction.
This is largely a receptor-subtype label within the existing HER2-positive use, not a fundamentally new disease area.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 (see caveat in the Clinical Trial Evidence section) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125409) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Pertuzumab binds HER2 subdomain II and blocks HER2-HER3 heterodimerization. This suppresses downstream PI3K/AKT and MAPK signaling, which drive tumor growth. Detailed mechanism data from DrugBank is not currently available, so this description comes from the evidence pack's rationale.

About half of HER2-overexpressing breast cancers also express hormone receptors (ER and/or PR), so PR-positive, HER2-positive tumors fall within the approved HER2-positive breast cancer use. The record's original-indication field is empty, so the on-label status rests on general knowledge, not on the regulatory data supplied.

**Guardrails:**
- Benefit applies to HER2-positive disease only, not to HER2-negative PR-positive disease.
- Hormone receptor signaling is a known escape route, which is why the trials pair pertuzumab with endocrine therapy.
- Some trial titles are truncated, so the pertuzumab-specific role in those trials is inferred.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | NEOADAPT: aromatase inhibitor plus pertuzumab/trastuzumab without chemotherapy in HR+/HER2+ early breast cancer (32 patients planned; only 7 enrolled) |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | Randomized neoadjuvant comparison of 4 trastuzumab/docetaxel/pertuzumab regimens (pCR rate); appears to be NeoSphere |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 vs pertuzumab in HER2+, ER/PR-negative disease (equivalence design) |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Biosimilar BCD-178 vs Perjeta as neoadjuvant therapy in HER2+ disease |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs placebo added to neoadjuvant chemotherapy plus trastuzumab/pertuzumab |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: chemotherapy de-escalation with SC pertuzumab/trastuzumab in ER-negative disease |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 plus pertuzumab preoperatively; impact of HER2 heterogeneity |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023: lapatinib plus trastuzumab with or without endocrine therapy (pertuzumab not central) |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective HER2-low prevalence study; does not evaluate pertuzumab efficacy |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Weekly paclitaxel in Nigerian women; no data and no clear pertuzumab link |

**Caveat on the L1 level:** The two completed Phase 3 trials that meet the L1 rule (NCT04629846 and NCT03726879) are a biosimilar equivalence study in ER/PR-negative disease and an atezolizumab add-on study. Neither directly tests pertuzumab in PR-positive tumors. Direct PR-positive evidence comes mainly from small or single-arm Phase 2 studies.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (Phase 2) | Lancet Oncol | NeoSphere 5-year analysis: progression-free survival, disease-free survival and safety after neoadjuvant pertuzumab plus trastuzumab |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 weeks of dual blockade with or without weekly paclitaxel, testing de-escalation |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: endocrine therapy plus trastuzumab/pertuzumab vs de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2) | J Clin Oncol | PERTAIN: trastuzumab plus aromatase inhibitor with or without pertuzumab in HER2+/HR+ metastatic or locally advanced disease |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (Phase 3) | Br J Cancer | Phase 3 equivalence trial of biosimilar QL1209 vs reference pertuzumab in HER2+, ER/PR-negative disease |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | Review of HR+/HER2+ breast cancer, including cross-talk between the HER2 and hormone receptor pathways |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer (Tokyo) | Signaling pathway interactions and clinical translation in HR+/HER2+ breast cancer |
| [40246081](https://pubmed.ncbi.nlm.nih.gov/40246081/) | 2025 | Retrospective cohort | Mod Pathol | Impact of hormone receptor status and HER2 expression on neoadjuvant targeted therapy response |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Review | Eur J Clin Invest | CDK4/6 and PI3K inhibitors in HER2+ breast cancer, including ER-positive tumors |

The evidence pack lists 20 publications. The ten most relevant are shown above. The rest are lower-priority reviews, case reports and one unrelated docetaxel myositis report.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125409 | PERJETA (Genentech, Inc.) | Injection, solution, concentrate | Not listed in the record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
PR-positive, HER2-positive breast cancer is essentially a receptor subtype of pertuzumab's established HER2-positive use, and several randomized studies support the HER2-positive setting, including HR+/HER2+ trials. Direct evidence in PR-positive tumors is mostly small or single-arm Phase 2 work, so use must be restricted to confirmed HER2-positive disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking data gap)
- DrugBank mechanism of action data to complete the mechanistic analysis
- Confirmation of the approved indication text, since the record's field is empty
- Verification of pertuzumab's role in trials with truncated titles, plus PR-stratified efficacy data from HR+/HER2+ trials
- A HER2-confirmation requirement in any development or use plan, since HER2-negative PR-positive disease is not supported
- The other nine predicted indications are not covered in this report. Ranks 2 and 4 are research questions, and ranks 5-10 are on hold with little or no evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

