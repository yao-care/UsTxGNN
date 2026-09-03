---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 1089
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Hormone Replacement Therapy to Amenorrhea Treatment

## One-Sentence Summary

> Progesterone is a natural steroid hormone widely used in reproductive endocrinology and hormone replacement therapy, though this specific evidence pack contains no documented original indication or MOA data for the product record queried.
> The TxGNN model predicts it may be effective for **Amenorrhea**,
> with **50+ clinical trials** and **18 publications** currently identified as related evidence (a subset directly supporting progestin-based mechanisms).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (progesterone is a natural steroid hormone generally used in reproductive endocrinology; no specific approved-indication text was returned for this record) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed (per this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this record. Based on well-established pharmacology, progesterone is a natural agonist at the progesterone receptor, and exogenous administration followed by withdrawal is the classic basis of the **"progestin withdrawal test"** — a standard diagnostic and therapeutic tool in gynecologic endocrinology. If the endometrium has been adequately primed by estrogen, stopping progesterone triggers withdrawal bleeding that can both diagnose the cause of amenorrhea (hypothalamic-pituitary-ovarian axis integrity) and restore menstrual cyclicity.

This mechanism is textbook-level and non-novel, which explains the very high TxGNN prediction score. However, most of the clinical trial evidence in this pack involves related progestins (medroxyprogesterone acetate, elagolix, relugolix) rather than progesterone itself, so drug-to-indication specificity should be verified before advancing.

Because amenorrhea and normal menstrual cycle regulation sit directly within progesterone's core physiological role (luteal support, endometrial withdrawal bleeding), the mechanistic distance between "reproductive hormone therapy" broadly and "amenorrhea treatment" specifically is minimal — this is less a novel repurposing signal and more a confirmation of an already-recognized clinical use pattern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-endometrial-ablation medroxyprogesterone acetate for amenorrhea rates after heavy menstrual bleeding surgery (progestin analog, not progesterone itself; trial halted early) |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Evaluated whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction with clomiphene in women with oligo-/amenorrhea |
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Compared gonadotropin therapies in subjects with Amenorrhea I or anovulatory cycles (hypothalamic/pituitary dysfunction) |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1,845 | Large RCT of combined estradiol + progesterone for vasomotor symptoms in postmenopausal women with an intact uterus |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A (multicenter RCT) | Unknown | 330 | Compared Progesterone Capsules, a Chinese herbal formula, and their combination for treating menstrual disorders in adult women |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Phase 3 | Unknown | 90 | Luteal-phase subcutaneous progesterone vs watch-and-wait for regression of endometrial polyps in premenopausal women |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | Completed | 271 | Proof-of-concept RCT of elagolix (GnRH antagonist, mechanistically distinct from progesterone) vs placebo for heavy uterine bleeding with fibroids |
| [NCT01927432](https://clinicaltrials.gov/study/NCT01927432) | N/A | Completed | 73 | Ultrasound characterization of ovarian follicle wave dynamics in women with amenorrhea (observational natural-history study, not interventional) |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | Goserelin (LHRH analog) during chemotherapy to prevent ovarian failure/early menopause in breast cancer patients |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | RCT on timing of postpartum depot medroxyprogesterone acetate administration and its effect on breastfeeding/contraceptive continuation |

**Note:** Only a minority of listed trials test progesterone itself; several use pharmacologically related progestins (MPA, DMPA) or mechanistically distinct agents (elagolix, relugolix, goserelin) for overlapping indications. Drug-specific confirmation is needed.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Comprehensive review of diagnostic and therapeutic uses of oral micronized progesterone, including its role via kisspeptin/neurokinin B/dynorphin neurons in regulating LH/FSH pulsatility |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Review of etiology and management of amenorrhea in adolescents/young women, centered on hypothalamic-pituitary-ovarian axis dysfunction |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Updated meta-analysis on chemotherapy-induced amenorrhea and its prognostic significance in premenopausal breast cancer patients |
| [40474175](https://pubmed.ncbi.nlm.nih.gov/40474175/) | 2025 | Retrospective Cohort | BMC Surgery | High-dose estrogen + progesterone sequential therapy combined with hysteroscopic adhesiolysis improved uterine cavity recovery in severe intrauterine-adhesion-related infertility/amenorrhea |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Classic clinical review on evaluation of amenorrhea; recommends prolactin/TSH screening and progestin challenge test |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Overview of etiology, symptomatology, and treatment options for Premature Ovarian Insufficiency (POI), a major cause of secondary amenorrhea |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Review of intrauterine adhesions (Asherman's syndrome), a structural cause of amenorrhea |
| [945033](https://pubmed.ncbi.nlm.nih.gov/945033/) | 1976 | Case Series | Annals of Internal Medicine | Classic study of galactorrhea-amenorrhea syndromes showing absent LH/progesterone ovulatory peaks prior to treatment |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | Review of hormonal treatments for endometriosis, discussing estrogen-dependency and progesterone-resistance pathogenesis |
| [12222332](https://pubmed.ncbi.nlm.nih.gov/12222332/) | 1991 | Review | Entre Nous | Overview of once-a-month combined estrogen/progestogen injectable contraceptives and menstrual cycle effects |

---

## US Market Information

No NDA/license records are present in this dataset (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`). This indicates the queried product record has no marketing authorization in this dataset — it does not necessarily reflect progesterone's overall global regulatory status, since progesterone products are marketed elsewhere under various brand names.

---

## Safety Considerations

Please refer to the package insert for safety information. All key warnings, contraindications, and drug-interaction data in this evidence pack are marked as unavailable — this is flagged as a **Blocking** data gap (see Conclusion below) and must be resolved before any safety assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Progesterone's role in inducing withdrawal bleeding to treat/diagnose amenorrhea is a well-established, mechanistically sound clinical use, and several Phase 3/4 trials (large-enrollment estradiol+progesterone RCT, gonadotropin-comparator trial in Amenorrhea I, postpartum DMPA RCT) support the broader progestin-amenorrhea relationship (L2 evidence). However, most listed trials evaluate related progestins or mechanistically distinct agents rather than progesterone itself, so this should be treated as a plausibility signal rather than confirmed efficacy for the specific molecule.

**To proceed, the following is needed:**
- **[Blocking]** TFDA/FDA package-insert warnings and contraindications (DG001) — required before any S1 safety assessment can proceed
- **[High]** Confirmed mechanism of action data via DrugBank (DG002) to validate the mechanistic rationale above
- Drug-interaction (DDI) data, currently returning no results
- Direct clinical evidence isolating progesterone (vs. MPA/DMPA/other progestins) specifically for amenorrhea treatment
- Confirmation of actual marketing/licensing status, since this record shows no active NDA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

