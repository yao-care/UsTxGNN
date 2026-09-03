---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 1278
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: From Psoriasis to Dermatitis (Atopic Dermatitis)

## One-Sentence Summary

> Ustekinumab is a human monoclonal antibody targeting the shared p40 subunit of IL-12/IL-23, with globally documented use in moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis (per literature evidence; no official local approval record is available in this dataset).
> The TxGNN model predicts it may be effective for **Dermatitis (Atopic Dermatitis)**,
> with **7 clinical trials** and **20 publications** currently supporting this direction — though the drug is **not currently marketed** in this jurisdiction and key safety documentation is missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in local regulatory data (未上市, no license records). Per literature evidence (PMID 36208443), ustekinumab is approved elsewhere for moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis. |
| Predicted New Indication | Dermatitis (Atopic Dermatitis) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack for this drug (flagged as a High-severity Data Gap). Based on the literature collected, ustekinumab is a human IgG1 monoclonal antibody that binds the shared p40 subunit of interleukin (IL)-12 and IL-23, thereby suppressing Th1, Th17, and Th22 activation (PMID 27304428). It is documented as being used for moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis (PMID 36208443).

Psoriasis and atopic dermatitis are both chronic, immune-mediated inflammatory skin diseases with overlapping cytokine pathways. Since ustekinumab's approved mechanism (IL-12/23 blockade) targets pathways implicated in Th1/Th17/Th22-driven skin inflammation, extension to atopic dermatitis is mechanistically plausible — a hypothesis that has already been directly tested in multiple Phase 2 RCTs (PMID 27304428, PMID 28338223) and mechanistic studies showing down-regulation of Th2/Th22 gene expression in AD skin lesions after treatment (PMID 27745907).

However, the literature evidence is mixed: several sources describe "anecdotal reports with conflicting results" for AD (PMID 33849369) and note that AD is a heterogeneous disease not all patients respond to targeted cytokine therapy for (PMID 30850043). This tempers the strength of the mechanistic rationale despite the very high TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Completed | 79 | Randomized, double-blind, placebo-controlled study of ustekinumab in adult Japanese subjects with severe atopic dermatitis. |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Completed | 32 | Randomized pilot study of ustekinumab in chronic atopic dermatitis with sub-optimal response to prior therapy. |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Recruiting | 45 | Contact dermatitis suction-blister model to study how biologic medications work in skin inflammation. |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice-based intradermal delivery testing FDA-approved medications (including biologics used for AD/psoriasis) directly on skin. |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A (observational) | Completed | 1000 | Pharmacogenetic/observational study on 10-year survival of biologic therapies (including ustekinumab) in cutaneous psoriasis. |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Completed | 676 | Secukinumab vs. ustekinumab in moderate-to-severe plaque psoriasis (CLEAR study; comparator trial, not AD-specific). |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A (observational) | Completed | 126 | Cardiovascular risk assessment in severe psoriasis patients treated with biologic agents. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase 2) | Experimental Dermatology | Double-blind, placebo-controlled study (n=33) of ustekinumab in moderate-to-severe AD; IL-12/23p40 antagonist rationale described. |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase 2) | British Journal of Dermatology | Randomized, double-blind, placebo-controlled Phase 2 study of ustekinumab in Japanese patients with severe atopic dermatitis. |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic Review & Meta-analysis | Allergy | Evidence review for EAACI clinical practice guideline on systemic treatments for moderate-to-severe AD. |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Systematic Review | Journal of Dermatological Treatment | Systematic review evaluating efficacy and safety of ustekinumab specifically in atopic dermatitis. |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Systematic Review & Meta-analysis | American Journal of Clinical Dermatology | Assesses whether biologics (including ustekinumab) are efficacious in AD. |
| [38847375](https://pubmed.ncbi.nlm.nih.gov/38847375/) | 2024 | Systematic Review | Journal of Cutaneous Medicine and Surgery | Biologic therapy response in skin-of-colour participants with moderate-to-severe psoriasis and AD. |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic Review | American Journal of Clinical Dermatology | Systemic therapy management of erythrodermic psoriasis, differential diagnosis includes AD. |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatologic Therapy | Synthesizes off-label uses of ustekinumab beyond its approved indications (psoriasis, PsA, Crohn's, UC). |
| [31514420](https://pubmed.ncbi.nlm.nih.gov/31514420/) | 2019 | Review | Children (Basel) | Reviews biologic treatment options, including off-label use, for pediatric psoriasis and atopic dermatitis. |
| [33282108](https://pubmed.ncbi.nlm.nih.gov/33282108/) | 2020 | Review | Journal of Clinical and Aesthetic Dermatology | Reviews biologic treatment options for pediatric psoriasis and atopic dermatitis. |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are flagged as a **Blocking-severity Data Gap** (DG001) in this evidence pack — no safety initial assessment (S1) can currently be performed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two completed Phase 2 RCTs and several systematic reviews specifically evaluating ustekinumab in atopic dermatitis support a plausible efficacy signal (L2 evidence), but a **Blocking** data gap on official label warnings/contraindications (DG001) means no safety assessment can currently be completed, and the drug is not marketed in this jurisdiction. Real-world literature also reports conflicting efficacy results, further supporting a Hold rather than a "Go" decision.

**To proceed, the following is needed:**
- Official label warnings, contraindications, and boxed-warning data (DG001, Blocking — required before any S1 safety evaluation)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Drug-drug interaction (DDI) profile (currently `not_found`)
- Resolution of conflicting real-world efficacy signals (e.g., PMID 33849369) via updated meta-analysis or additional RCT data
- Regulatory pathway assessment given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

