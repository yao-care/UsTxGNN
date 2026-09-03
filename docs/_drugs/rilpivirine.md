---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 1123
evidence_level: L5
indication_count: 5
---

# Rilpivirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rilpivirine: From HIV-1 Infection to Multiple TxGNN-Predicted Indications

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose established use — referenced within this evidence pack's own rationale annotations — is HIV-1 infection treatment, though formal Taiwan license and MOA records are currently empty in this dataset. TxGNN generated **5 candidate indications** for this drug, ranging from a low-risk extension within the existing HIV/AIDS disease spectrum (backed by a Phase 3 RCT) to cross-species translational models (feline/simian immunodeficiency virus) and one prediction with no plausible mechanistic link. Evidence strength varies sharply by candidate — **do not treat the single highest TxGNN score as the strongest lead**; the highest-scored candidate here is a veterinary condition with only preclinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan license data (0 licenses on file). Evidence-pack annotations describe rilpivirine as an NNRTI approved for HIV-1 infection treatment. |
| Top-Ranked Predicted Indication | Feline acquired immunodeficiency syndrome (predicted_indications[0]) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (one preclinical/mechanism study, no clinical trials) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision (top-ranked candidate) | Hold — veterinary indication, not applicable to human clinical development |

⚠️ The top TxGNN score does not correspond to the best clinical opportunity. See the candidate comparison below — **AIDS related complex** (rank 5) has by far the strongest human clinical evidence.

## Candidate Indications Overview

| Rank | Predicted Indication | TxGNN Score | TxGNN Rank | Evidence Level | Recommendation |
|---|---|---|---|---|---|
| 1 | Feline acquired immunodeficiency syndrome | 99.97% | 1382 | L4 (computed) | Hold — animal disease, not human-applicable |
| 2 | Simian immunodeficiency virus infection | 99.97% | 1383 | L3 | Research Question (translational/PrEP-PEP model, not a human indication) |
| 3 | Neurodevelopmental disorder w/ ataxic gait, absent speech, decreased cortical white matter | 99.97% | 1468 | L5 | Hold — no mechanistic plausibility, likely graph noise |
| 4 | Congenital human immunodeficiency virus (perinatal HIV exposure) | 99.56% | 10772 | L3 (computed) | Proceed with Guardrails — pregnancy safety monitoring required |
| 5 | AIDS related complex | 99.56% | 10773 | L1 | **Proceed with Guardrails** |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on annotations embedded in the pack's own repurposing rationale, rilpivirine is an NNRTI already approved for HIV-1 infection treatment; its efficacy in that setting is well established, and its reverse-transcriptase-inhibition mechanism plausibly extends to related retroviral contexts.

**AIDS related complex (rank 5)** is not a novel-mechanism repurposing candidate — it is a symptomatic sub-classification within HIV-1 disease, i.e., an extension within rilpivirine's existing approved indication space. This explains why it has the strongest evidence (a Phase 3 RCT directly testing rilpivirine-based dual therapy) and the lowest translational risk; the main open question is drug-drug interaction (DDI) management in comorbid populations (e.g., transplant recipients).

**SIV infection (rank 2) and feline AIDS (rank 1)** are cross-species lentivirus models. SIV shares high reverse-transcriptase homology with HIV-1, and long-acting cabotegravir/rilpivirine has been studied in SIV/SHIV-infected macaques as a translational model for human PrEP/PEP — but SIV and FIV are veterinary/preclinical research constructs, not human clinical indications in their own right.

**Congenital HIV (rank 4)** reflects perinatal/pregnancy-related use of rilpivirine-containing regimens — an important real-world safety question (transplacental exposure, pediatric PK) rather than a new mechanistic indication.

**Neurodevelopmental disorder (rank 3)**, despite an equally high TxGNN score, has zero supporting trials or literature and no plausible mechanistic path from an HIV reverse-transcriptase inhibitor to this rare genetic condition — most likely a knowledge-graph artifact (shared neighbor noise) rather than a real signal.

## Clinical Trial Evidence

### AIDS related complex (strongest candidate)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT01792570](https://clinicaltrials.gov/study/NCT01792570) | Phase 3 | Completed | 37 | Darunavir/ritonavir + rilpivirine dual therapy vs. triple therapy in virologically suppressed patients — direct RCT evidence (Grade A relevance) |
| [NCT01076179](https://clinicaltrials.gov/study/NCT01076179) | N/A | Completed | 502 | Lopinavir/ritonavir combined with new agents including NNRTIs — indirect relevance (Grade C) |

### Congenital human immunodeficiency virus (pregnancy/perinatal exposure)

Selected as most directly relevant of the 26 trials returned for this candidate (remainder are general adult switch-therapy trials not specific to perinatal transmission):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT07412977](https://clinicaltrials.gov/study/NCT07412977) | N/A | Not yet recruiting | 5,160 | VIROPREG — French prospective cohort assessing mother-to-child transmission and antiviral treatment impact in pregnancy |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A (Phase 4) | Completed | 1,578 | IMPAACT P1026s — pharmacokinetics of antiretrovirals in pregnant women and infants |
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | PK of darunavir/ritonavir, etravirine, and rilpivirine in HIV-1 infected pregnant women |
| [NCT02494986](https://clinicaltrials.gov/study/NCT02494986) | Phase 2 | Active, not recruiting | 48 | Roll-over access study for pediatric rilpivirine trial participants |
| [NCT03497676](https://clinicaltrials.gov/study/NCT03497676) | Phase 1/2 | Completed | 168 | Safety, tolerability, and PK of oral/long-acting cabotegravir + long-acting rilpivirine in virologically suppressed children and adolescents |

### Simian immunodeficiency virus infection / Feline acquired immunodeficiency syndrome

Currently no related clinical trials registered (preclinical/translational evidence only — see Literature Evidence).

### Neurodevelopmental disorder w/ ataxic gait, absent speech, decreased cortical white matter

Currently no related clinical trials registered.

## Literature Evidence

### AIDS related complex

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [37568163](https://pubmed.ncbi.nlm.nih.gov/37568163/) | 2023 | Case Report | AIDS Research and Therapy | Heart transplantation in a person with HIV — navigating DDIs between ART (rilpivirine-containing regimen) and post-transplant immunosuppression |

### Congenital human immunodeficiency virus (pregnancy exposure)

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [41225339](https://pubmed.ncbi.nlm.nih.gov/41225339/) | 2025 | Systematic Review | BMC Infectious Diseases | Safety of long-acting cabotegravir in pregnancy — systematic review and meta-analysis |
| [36411596](https://pubmed.ncbi.nlm.nih.gov/36411596/) | 2023 | Observational | HIV Medicine | Pregnancy outcomes and PK in women exposed to long-acting cabotegravir/rilpivirine in clinical trials |
| [38864586](https://pubmed.ncbi.nlm.nih.gov/38864586/) | 2024 | Cohort | AIDS (London) | First-trimester exposure to newer antiretrovirals and congenital anomalies, US cohort |
| [38703388](https://pubmed.ncbi.nlm.nih.gov/38703388/) | 2024 | Case Report | Clin Infect Dis | Long-acting CAB/RPV throughout pregnancy — reduced RPV concentrations, no vertical transmission or malformation |
| [41268510](https://pubmed.ncbi.nlm.nih.gov/41268510/) | 2025 | Case Report + Review | Case Reports in Infectious Diseases | CAB/RPV maintained suppression throughout pregnancy in a perinatally-acquired HIV patient |

### Simian immunodeficiency virus infection

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Curr Opin HIV AIDS | Review of cabotegravir (rilpivirine's long-acting combination partner) for ART and PrEP |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal Study (macaque) | Nature Communications | Long-acting CAB/RPV contributes to SHIV remission in macaques with early treatment |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical Animal Study (macaque) | EBioMedicine | Long-acting CAB/RPV as single-injection post-exposure prophylaxis in a macaque model |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Animal Study (macaque) | Antimicrob Agents Chemother | Low frequency of drug-resistant variants selected by long-acting rilpivirine PrEP in SIV-infected macaques |

### Feline acquired immunodeficiency syndrome

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical/Biochemical | J Vet Sci | Structural comparison of NNRTIs (including rilpivirine) against feline vs. human immunodeficiency virus reverse transcriptase |

### Neurodevelopmental disorder w/ ataxic gait, absent speech, decreased cortical white matter

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were available in this evidence pack (safety fields returned no findings, and DDI query status is "not_found").

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the AIDS related complex candidate specifically — the only candidate with direct Phase 3 RCT support and clinical actionability)

**Rationale:**
- AIDS related complex sits within rilpivirine's existing HIV/AIDS treatment space and is supported by a direct Phase 3 RCT; the main risk is DDI management in comorbid populations (e.g., transplant patients), not efficacy uncertainty.
- The congenital HIV / perinatal exposure candidate has real-world observational and case-report safety data supporting continued use with monitoring, but no dedicated RCT.
- SIV and feline AIDS candidates are non-human translational models, not human indications — useful mechanistically but out of scope for a human formulary decision (**Hold**).
- The neurodevelopmental disorder candidate has no supporting evidence and should be discarded as likely knowledge-graph noise (**Hold**).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — flagged as a **Blocking** data gap (DG001) in this evidence pack; required before any S1 safety review.
- Formal drug-level MOA data from DrugBank (DG002, High severity) to replace the currently inferred NNRTI/HIV-1 mechanism.
- Taiwan licensing status confirmation — 0 licenses on file conflicts with rilpivirine's known global marketing status and should be re-verified against source data before regulatory conclusions are drawn.
- DDI dataset population (currently `not_found`) before advancing the AIDS-related-complex or transplant-comorbidity use cases.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

