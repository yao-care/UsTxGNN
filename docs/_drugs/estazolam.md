---
layout: default
title: Estazolam
parent: Model Prediction Only (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
---

# Estazolam
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

# Estazolam: From Sedative-Hypnotic (Original Indication Not Recorded) to Insomnia

## One-Sentence Summary

Estazolam is a benzodiazepine sedative-hypnotic sold in the US as generic tablets, but the US license records supplied here contain no indication text.
The TxGNN model predicts it may be effective for **insomnia**, with **12 clinical trials** and **18 publications** retrieved for this direction.
Insomnia is already a recognized use of estazolam, so this is closer to confirming an existing use than to true repurposing. Only one completed Phase 3 trial was found, and estazolam's role in it (test drug or comparator) is unconfirmed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no indication text in the US license records) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 licenses reported (all ANDA generics; only 3 unique ANDA numbers appear in the list) |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** The pack's scoring section labels this L1. Under the L1–L5 rules, L1 needs at least 2 completed Phase 3 RCTs. Only one completed Phase 3 trial was found (NCT00347295), and its estazolam role is unconfirmed. I have therefore assigned L2 here.

---

## Why is This Prediction Reasonable?

Estazolam is a triazolo-benzodiazepine. It acts as a positive allosteric modulator of GABA-A receptors, which produces sedative-hypnotic effects. This drug-mechanism-disease link is direct and well established. Detailed mechanism data were not supplied in the pack's MOA field; the mechanism described here comes from the pack's repurposing rationale.

Insomnia is an established use of the drug, and an older US clinical review (PMID 1968721) reports that estazolam 1 mg and 2 mg improved sleep latency, total sleep time and sleep quality in adults with chronic insomnia. The empty "original indication" field is a gap in the input data, not evidence against the prediction.

---

## Clinical Trial Evidence

Only trials with a plausible estazolam link are listed. Several are trials of acupuncture or herbal products in which estazolam is only a comparator or background therapy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Phase 3 | Completed | 253 | Randomized, double-blind, double-dummy, multicenter trial of brotizolam vs estazolam in insomnia outpatients. No results summary in the pack. |
| [NCT00956319](https://clinicaltrials.gov/study/NCT00956319) | Phase 4 | Completed | 42 | Zolpidem modified release vs estazolam (Eurodin) as the comparator in primary insomnia. |
| [NCT06859190](https://clinicaltrials.gov/study/NCT06859190) | Phase 3 | Recruiting | 60 | Auricular pressure beans plus electroacupuncture combined with estazolam for cancer-related insomnia. The test intervention is the non-drug therapy. |
| [NCT03997058](https://clinicaltrials.gov/study/NCT03997058) | Phase 4 | Unknown | 120 | Auricular acupoint pressing vs oral estazolam for insomnia in maintenance hemodialysis patients. |
| [NCT07306494](https://clinicaltrials.gov/study/NCT07306494) | Phase 4 | Not yet recruiting | 1200 | Compound Ciwujia Granules vs estazolam (double-dummy) in chronic insomnia. Estazolam is a comparator. |
| [NCT06212934](https://clinicaltrials.gov/study/NCT06212934) | N/A | Unknown | 96 | Acupuncture at "Chou's Tiaoshen" acupoints, tested for non-inferiority to estazolam in short-term insomnia. |
| [NCT06258226](https://clinicaltrials.gov/study/NCT06258226) | N/A | Unknown | 108 | Auricular acupressure to reduce estazolam use in drug-dependent insomnia. |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1400 | Prospective cohort of hypnotic use, efficacy and safety in elderly patients at a Taiwanese medical center. |
| [NCT03420105](https://clinicaltrials.gov/study/NCT03420105) | N/A | Completed | 75 | Prospective memory and sleep in breast cancer. No direct estazolam efficacy question. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | Clinical review | Am J Med | US clinical experience: estazolam 1 mg and 2 mg improved sleep latency, total sleep time, awakenings and sleep quality in chronic insomnia. The 2 mg dose remained effective for at least 6 weeks of nightly use. |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | RCT | Zhen Ci Yan Jiu | Shallow-needle therapy combined with estazolam in insomnia (liver stagnation transforming into fire pattern), with ACTH and cortisol measured. |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | Clinical study | Zhongguo Zhen Jiu | Syndrome-differentiation acupuncture vs estazolam in chronic insomnia, including effects on cognitive function. |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Clinical observation | Zhongguo Zhen Jiu | Baduanjin plus auricular point sticking vs oral estazolam for COVID-19-related insomnia. |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | "Drugs for chronic insomnia" (no abstract available). |
| [31013432](https://pubmed.ncbi.nlm.nih.gov/31013432/) | 2019 | Systematic review | J Altern Complement Med | Updated systematic review of RCTs on acupuncture for primary insomnia. Not estazolam-specific. |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Scoping review | Integr Med Res | Chinese herbal medicine and acupuncture for insomnia comorbid with chronic pain. Not estazolam-specific. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world analysis | Zhongguo Zhong Yao Za Zhi | Concurrent diseases and medicine use among insomnia patients in 20 hospitals (1,067 cases). |
| [40827342](https://pubmed.ncbi.nlm.nih.gov/40827342/) | 2025 | Cross-sectional | Psychiatry Clin Psychopharmacol | Drug use for insomnia in a Chinese medicine hospital in Shenzhen. |
| [38007723](https://pubmed.ncbi.nlm.nih.gov/38007723/) | 2023 | Preclinical | Stud Health Technol Inform | Flos Daturae sedative-hypnotic effects in mice, with estazolam as the positive control. |

---

## US Market Information

Three unique ANDA numbers appear in the license list, and two of them are listed twice. All products are oral tablets. No approved-indication text was provided for any license.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA074818 | Estazolam | Tablet | Actavis Pharma, Inc. |
| ANDA074921 | Estazolam | Tablet | Dr. Reddy's Laboratories Inc. |
| ANDA074826 | Estazolam | Tablet | Novitium Pharma LLC |

---

## Safety Considerations

The package insert warnings and contraindications were not retrieved, so please refer to the package insert for safety information. No drug-interaction records were found.

The pack's repurposing rationale lists these guardrails:
- Estazolam is a controlled substance.
- Risks include dependence, tolerance, next-day impairment and falls, especially in elderly patients.
- Short-term use is preferred.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct and the insomnia use is long established. However, the trial evidence is weaker than it looks. Only one Phase 3 trial is completed, and most other trials test acupuncture or herbal products with estazolam as a comparator. Controlled-substance risks also call for guardrails.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, labeled indication) to close the safety and indication gaps.
- Confirmation of estazolam's role (test drug or comparator) in NCT00347295 and NCT00956319, and retrieval of their results.
- A short-term-use and elderly-patient monitoring plan covering dependence, next-day impairment and fall risk.

The other nine predicted indications (ranks 2–10) are all seizure, withdrawal, restless legs and pain conditions. They rest on class-level or preclinical evidence only and are not recommended for advancement at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

