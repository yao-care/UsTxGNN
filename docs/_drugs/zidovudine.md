---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 1304
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using no additional tools — this is a direct content-generation task per the exact template already provided by the user; proceeding straight to the report.

# Zidovudine: From HIV Infection to AIDS-Related Complex

## One-Sentence Summary

Zidovudine (AZT) is the original nucleoside reverse transcriptase inhibitor used in antiretroviral therapy for HIV infection.
The TxGNN model predicts strong applicability to **AIDS-Related Complex (ARC)** — historically AZT's first ever approved clinical indication —
with **50 clinical trials** and **20 publications** currently supporting this direction, making this a validation of known efficacy rather than a novel off-label discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current registry dataset; literature evidence describes zidovudine as an antiretroviral used for HIV infection/AIDS |
| Predicted New Indication | AIDS-Related Complex |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in the current dataset. However, the evidence pack's own rationale confirms zidovudine's core pharmacology: it inhibits HIV reverse transcriptase, blocking viral replication. AIDS-Related Complex represents the early-to-moderate immunodeficiency stage of HIV infection, preceding full-blown AIDS.

Notably, this predicted indication is not a distant repurposing target — the underlying evidence explicitly states that ARC was **historically AZT's first-ever approved clinical use**. This means the TxGNN model has successfully "rediscovered" a real, well-established indication for this drug, which serves as a strong internal validation of the prediction methodology rather than an entirely new therapeutic hypothesis.

Because the pharmacological target (HIV reverse transcriptase) is identical between HIV infection, ARC, and full AIDS, the mechanistic link is direct and requires no cross-disease extrapolation — the entire disease continuum shares the same causative virus and the same drug target.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000637](https://clinicaltrials.gov/study/NCT00000637) | Phase 3 | Completed | 819 | AZT vs. ddI vs. AZT+ddI in symptomatic HIV-infected children; compared survival and disease progression |
| [NCT00002334](https://clinicaltrials.gov/study/NCT00002334) | Phase 3 | Completed | 3000 | AZT alone vs. AZT+ddC vs. AZT+saquinavir vs. triple combination in treatment-naive HIV patients |
| [NCT00000679](https://clinicaltrials.gov/study/NCT00000679) | Phase 2 | Completed | 600 | ddC vs. zidovudine in AIDS/advanced ARC comparing efficacy and safety profile |
| [NCT00000979](https://clinicaltrials.gov/study/NCT00000979) | Phase 2 | Completed | 1500 | ddI vs. zidovudine in AIDS, advanced ARC, or asymptomatic infection with CD4 < 200 |
| [NCT00002124](https://clinicaltrials.gov/study/NCT00002124) | Phase 3 | Completed | 1250 | Delavirdine + zidovudine vs. zidovudine alone in HIV-1 infected patients, CD4 200–500 |
| [NCT00002290](https://clinicaltrials.gov/study/NCT00002290) | N/A | Completed | N/A | Concurrent Retrovir (zidovudine) + Zovirax (acyclovir) vs. zidovudine alone in early symptomatic HIV infection |
| [NCT00000831](https://clinicaltrials.gov/study/NCT00000831) | Phase 2 | Completed | 280 | Virologic responses to new nucleoside regimens after prolonged zidovudine or ddI monotherapy |
| [NCT00000986](https://clinicaltrials.gov/study/NCT00000986) | Phase 1 | Completed | 18 | Safety, tolerance, and immunology of IL-2 + zidovudine combination in AIDS/ARC patients |
| [NCT00002081](https://clinicaltrials.gov/study/NCT00002081) | N/A | Completed | N/A | Open-label ddC + zidovudine combination program for advanced HIV disease with toxicity monitoring |
| [NCT00002035](https://clinicaltrials.gov/study/NCT00002035) | N/A | Completed | 300 | Continued zidovudine vs. ddI in AIDS/ARC patients showing clinical deterioration on zidovudine |

*(50 trials total are on record for this indication; the above 10 represent the most clinically pivotal.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3299089](https://pubmed.ncbi.nlm.nih.gov/3299089/) | 1987 | RCT | N Engl J Med | Landmark double-blind, placebo-controlled trial establishing AZT efficacy in AIDS/ARC (Fischl et al.) |
| [2677429](https://pubmed.ncbi.nlm.nih.gov/2677429/) | 1989 | RCT | JAMA | Long-term follow-up: prolonged zidovudine therapy improved survival in AIDS/ARC patients |
| [1777174](https://pubmed.ncbi.nlm.nih.gov/1777174/) | 1991 | RCT | AIDS | European-Australian double-blind trial: zidovudine ± acyclovir for AIDS-related complex |
| [2159707](https://pubmed.ncbi.nlm.nih.gov/2159707/) | 1990 | RCT | Am J Med | ACTG Phase I/II study: ddC + zidovudine combination in AIDS and advanced ARC |
| [2159705](https://pubmed.ncbi.nlm.nih.gov/2159705/) | 1990 | RCT | Am J Med | Alternating/intermittent zidovudine + ddC regimens in AIDS/ARC treatment |
| [2191113](https://pubmed.ncbi.nlm.nih.gov/2191113/) | 1990 | RCT | J Acquir Immune Defic Syndr | Placebo-controlled trial showing quality-of-life benefit of zidovudine in AIDS/ARC |
| [8096703](https://pubmed.ncbi.nlm.nih.gov/8096703/) | 1993 | RCT | AIDS | Double-blind randomized trial: zidovudine alone vs. cotherapy with acyclovir in AIDS/ARC |
| [3059187](https://pubmed.ncbi.nlm.nih.gov/3059187/) | 1988 | RCT | N Engl J Med | Double-blind trial assessing neuropsychological outcomes of zidovudine in AIDS/ARC |
| [1974727](https://pubmed.ncbi.nlm.nih.gov/1974727/) | 1990 | RCT | Rev Infect Dis | Phase I dose-finding trial of ddI in AZT-intolerant AIDS/ARC patients |
| [1894937](https://pubmed.ncbi.nlm.nih.gov/1894937/) | 1991 | Cohort | J Infect Dis | Zidovudine treatment associated with improved pneumococcal vaccine antibody response in AIDS/ARC |

---

## US Market Information

No marketing authorization records are currently on file. According to the regulatory dataset, zidovudine's status is **Not Marketed**, with **0 licenses** registered in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is exceptionally strong (Evidence Level L1) — 50 clinical trials, including multiple completed Phase 3 RCTs, and 20 supporting publications — and this indication corresponds to the drug's own historically approved use, giving high mechanistic and clinical confidence. However, a Blocking data gap on TFDA-equivalent label warnings/contraindications prevents completion of the safety initial assessment (S1), and the drug currently has no active marketing authorization in this jurisdiction.

**To proceed, the following is needed:**
- Official package insert / label warnings and contraindications (Blocking gap, DG001)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (High priority gap, DG002)
- Clarification of current marketing/licensing pathway, since the drug is presently unmarketed with zero NDAs on record
- Confirmation of whether "AIDS-Related Complex" should be treated as a label-expansion/reconfirmation case rather than a novel repurposing indication, given its historical approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

