---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Durvalumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Transitional cell carcinoma (urothelial carcinoma)"
monitor_inn: "DURVALUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Durvalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Durvalumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 antibody, originally associated with the treatment of transitional cell carcinoma (urothelial carcinoma).
The TxGNN model ranks **prostatic urethra urothelial carcinoma** as its top prediction, but **no clinical trials or publications** were found for this specific indication.
Related urothelial and variant-histology cancers have limited supporting evidence: a few small early-phase or terminated trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (urothelial carcinoma) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (the single BLA is listed as cancelled) |
| Number of NDAs | 1 (BLA761069) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, durvalumab is an anti-PD-L1 monoclonal antibody. Blocking PD-L1 can release the immune system's suppression of tumour cells. Its association with urothelial carcinoma has been established, and mechanistically it may be applicable to urothelial cancers arising at other sites.

The prostatic urethra is lined by urothelium, so urothelial carcinoma at this site shares its histology with bladder cancer, the original indication. PD-L1 blockade is therefore biologically plausible. However, no trials or publications were found for this specific site, so the prediction rests on model output and biological reasoning alone.

The other top-ranked predictions are also urothelial or gynecologic cancers. Notable examples:
- **Kidney pelvis sarcomatoid transitional cell carcinoma** and **infiltrating bladder urothelial carcinoma, sarcomatoid variant** (L3): supported by small early-phase or terminated trials.
- **Endocervical carcinoma** (L3): supported by one completed Phase 1 trial and limited literature.

## Clinical Trial Evidence

No trials are registered for the top-ranked indication (prostatic urethra urothelial carcinoma). The table below lists trials found for closely related predicted indications (ranks 2, 3 and 6).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab with neoadjuvant chemotherapy in variant-histology bladder cancer. Directly matches the sarcomatoid variant, but only 7 patients were enrolled, so it cannot support efficacy conclusions. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, not recruiting | 54 | Pre-surgical pilot of durvalumab plus tremelimumab in cisplatin-ineligible, muscle-invasive, high-risk urothelial carcinoma. Evaluates safety and immune effects. Not specific to sarcomatoid disease. |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy plus durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer. Early safety and feasibility data only. |

## Literature Evidence

No publications were found for the top-ranked indication. The table below lists publications found for the related endocervical carcinoma prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Nonrandomized clinical trial | Oncology and Therapy | Phase 1 study of ceralasertib (an ATR inhibitor) plus durvalumab in Chinese patients with advanced solid tumours that were resistant to prior anti-PD-(L)1 therapy or had no standard of care. Assesses safety, pharmacokinetics and antitumour activity. Not specific to cervical cancer. |
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Review of small cell neuroendocrine carcinoma of the cervix, covering molecular basis and therapeutic advances. Notes that evidence is limited to case series and case reports. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761069 (cancelled) | IMFINZI | Injection, solution | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 81 interactions were recorded. The most notable are:
  - **Major**: adalimumab.
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, tetanus toxoid vaccine and anthrax vaccine.
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).

  Interactions with corticosteroids and other immunomodulators are likely relevant because these agents may counteract immune-checkpoint activity.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a very high model score (99.98%) and a plausible mechanism, since the prostatic urethra is lined by urothelium. However, there are no clinical trials or publications for this site (L5). Evidence for neighbouring predictions is limited to small, early-phase or terminated studies (L3). The US market status is also "cancelled only," which further limits the near-term case.

**To proceed, the following is needed:**
- Clinical or real-world data on durvalumab in prostatic urethral or other upper-tract urothelial carcinoma
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Confirmation of the current US regulatory status of IMFINZI, since the data show the BLA as cancelled
- A literature review of related variant-histology cohorts, such as sarcomatoid urothelial carcinoma, to inform trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

