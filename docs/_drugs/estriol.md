---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 676
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Estriol: From an Undocumented Original Indication to Amenorrhea

## One-Sentence Summary

Estriol is a naturally occurring, weak estrogen; this dataset does not record its original approved indication or mechanism of action, and it is not currently marketed in Taiwan. The TxGNN model predicts potential efficacy for **Amenorrhea** (specifically functional hypothalamic amenorrhea, FHA) with a high model score of **99.18%**, but the supporting evidence is currently thin: of **3** registered clinical trials, none directly support this drug-indication pair (two test a different compound, estetrol, and one was withdrawn), and of **13** publications identified, only one is a relevant interventional pilot study on estriol in FHA.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset |
| Predicted New Indication | Amenorrhea (functional hypothalamic amenorrhea) |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 (mechanistic/preliminary studies only) |
| Market Status (Taiwan) | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for estriol in this dataset. Based on known pharmacology, estriol is a naturally occurring, low-potency estrogen.

Functional hypothalamic amenorrhea (FHA) is driven by suppression of pulsatile GnRH release from the hypothalamus, resulting in a systemic hypoestrogenic state and loss of menstrual cycling. The repurposing hypothesis is that low-dose exogenous estriol could modulate hypothalamic-pituitary function — for example by altering LH secretion via negative feedback — and partially support recovery of the gonadal axis in FHA patients.

This is a plausible but indirect mechanistic link: it reflects a general pharmacological effect of estrogen replacement rather than an estriol-specific action, and no controlled trial has yet tested "resumption of menstrual cycling" as a primary endpoint. The prediction should therefore be treated as a research hypothesis rather than a clinically validated finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn | 0 | Tested photobiomodulation (not a drug) for postmenopausal vulvovaginal atrophy — unrelated intervention and indication, trial withdrawn with zero enrollment. Not usable as evidence. |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1015 | E4Comfort Study II — tested **estetrol (E4)**, a distinct compound from estriol (E3), for postmenopausal vasomotor symptoms. Unrelated to amenorrhea; appears to be a drug-name mismatch in the source data. |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1570 | E4Comfort Study I — also tests estetrol, not estriol, for vasomotor symptoms. Same mismatch issue as above. |

**None of the identified trials directly support estriol's use in amenorrhea.** All three are excluded on relevance review (wrong drug, wrong indication, or withdrawn/zero enrollment).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Cohort / interventional pilot study | Fertility and Sterility | Evaluated estriol administration's effect on hypothalamic-pituitary function and gonadotropin (LH) secretion in women with functional hypothalamic amenorrhea. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Reviews low-dose estrogens as neuroendocrine modulators in FHA, discussing the mechanism of impaired GnRH pulsatility and potential for restoring positive-feedback signaling. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Cohort | Medicinski Pregled | Examines lipid and hormonal profiles in women with premature primary ovarian failure treated with estro-progestagens; relevant to hypoestrogenic amenorrhea but not estriol-specific. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case report / cohort | Lancet | Endocrinological findings in two patients with premature ovarian failure. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Cohort | Zhong Xi Yi Jie He Za Zhi | Observational study on gonadal function changes in women with amenorrhea/oligomenorrhea (traditional Chinese medicine framework); limited direct relevance. |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | Clinical Obstetrics and Gynecology | Reviews hormonal contraception and neoplasia; only tangentially related. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Review / case series | British Journal of Psychiatry | Discusses anorexia nervosa; not a direct estriol treatment study. |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Case report | American Journal of Obstetrics and Gynecology | Endocrine effects of medroxyprogesterone acetate during pregnancy — different drug. |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Methodology | Die Medizinische Welt | Radioimmunoassay methodology for reproductive hormones including estriol; not a treatment study. |
| [1239569](https://pubmed.ncbi.nlm.nih.gov/1239569/) | 1975 | Review | Rinsho Byori | Reviews hormone assay methods in obstetrics/gynecology; methodological, not treatment-focused. |

Only **PMID 22137494** directly evaluates estriol treatment in FHA patients; the remainder are background, methodological, or indirectly related material.

---

## Market Information

Estriol is **not currently marketed in Taiwan** — no drug licenses are on record (0 total). No original-indication or NDA data is available to summarize here.

---

## Safety Considerations

TFDA label warnings, contraindications, and drug-interaction data for estriol are **not currently available** in this dataset (flagged as a Blocking data gap — this is required before any safety pre-screen can proceed). Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for estriol in functional hypothalamic amenorrhea is biologically plausible but indirect, and is supported by only one relevant pilot study — none of the three registered clinical trials actually test this drug-indication pair. Combined with the absence of TFDA label/safety data (a Blocking gap for the S1 safety pre-screen) and the fact that estriol is not currently marketed in Taiwan, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank or other authoritative source (DG002)
- Direct clinical trial evidence of estriol (not estetrol) in FHA/amenorrhea, ideally with menstrual-cycle resumption as an endpoint
- Clarification of Taiwan import/access pathway given current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

