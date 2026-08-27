---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 857
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
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

# Levonorgestrel: From Contraception to Acne (Disease)

## One-Sentence Summary

Levonorgestrel is a synthetic progestin widely used in hormonal contraceptive products (oral contraceptives, IUDs, implants). The TxGNN model predicts it may be effective for **Acne (disease)**, with **5 clinical trials** and **20 publications** currently retrieved for this drug-disease pair — though only a subset directly addresses acne as a primary outcome.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved-indication text available (drug is not marketed in this jurisdiction; no license records) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Levonorgestrel. Based on the evidence retrieved, Levonorgestrel is a synthetic 19-nortestosterone-derived progestin used across hormonal contraceptive platforms (combined oral contraceptives, progestin-only implants, and the levonorgestrel-releasing intrauterine system). Its efficacy in contraception is well established, and the literature base consistently describes androgenic activity as an inherent property of this drug class.

The link to acne is mechanistic rather than indication-adjacent: several retrieved publications (e.g., PMID 12196750, PMID 10717776) directly studied levonorgestrel-containing combined oral contraceptives and their effect on androgenic markers and acne severity, since androgens are known drivers of acne pathophysiology. Other combined hormonal products with antiandrogenic progestins (e.g., chlormadinone acetate, drospirenone) have documented dermatological benefits including acne improvement, which is used in the literature as a comparator to levonorgestrel-containing regimens (PMID 21895044, PMID 15025547, PMID 16796485). This suggests the acne signal is plausible but is tied to specific combined-hormone formulations rather than levonorgestrel monotherapy, and the direction of effect (levonorgestrel is comparatively more androgenic than antiandrogenic progestins) requires careful interpretation before further development.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | LNG-IUS (Mirena) studied for endometrial cancer prevention in obese women; oral progestin side effects (including acne) noted as background rationale, not a primary acne outcome |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large safety cohort comparing nomegestrol acetate/estradiol vs. levonorgestrel-containing combined oral contraceptives; not acne-focused |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Doxycycline added to continuous oral contraception to reduce breakthrough bleeding; acne mentioned only as an example doxycycline indication |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Subdermal gestrinone implant for endometriosis-related pelvic pain; not levonorgestrel- or acne-specific |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | LNG-IUS (Mirena) vs. megestrol for fertility-sparing treatment of atypical endometrial hyperplasia; not acne-related |

*Note: none of the retrieved trials use acne as a primary endpoint; relevance to the predicted indication is weak and largely incidental.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | Randomized, placebo-controlled trial of ethinyl estradiol/levonorgestrel (20/100 mcg) showing efficacy for moderate acne |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | RCT | Contraception | Multicenter randomized study comparing androgenic markers and acne outcomes across low-dose OC progestins including levonorgestrel |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | Reviews dermatological (acne, hirsutism, seborrhea) benefits of antiandrogenic hormonal contraceptive components |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | Ethinylestradiol/chlormadinone acetate shown more effective than ethinylestradiol/levonorgestrel for papulopustular acne |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | Reviews drospirenone vs. levonorgestrel/medroxyprogesterone regarding acne and hirsutism outcomes |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Reviews progestin androgenicity, the mechanistic basis for progestin-related acne effects |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Systematic Review | Cochrane Database Syst Rev | Cochrane review of levonorgestrel-releasing intrauterine system for endometrial hyperplasia (background/mechanism reference, not acne) |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | Overview of levonorgestrel-releasing intrauterine system pharmacology and endometrial effects |
| [1773615](https://pubmed.ncbi.nlm.nih.gov/1773615/) | 1991 | Review | Contraception | Evaluation of levonorgestrel-releasing IUD versus copper IUDs |
| [8489751](https://pubmed.ncbi.nlm.nih.gov/8489751/) | 1993 | Review | Ann Med | Review of hormonal intrauterine devices releasing levonorgestrel |

## US Market Information

No FDA/NDA license records were retrieved for Levonorgestrel in this Evidence Pack (`total_licenses: 0`, market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction data were retrieved for this evaluation (DDI query status: not found).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted acne indication is supported by plausible mechanism and several published RCTs, but no clinical trial directly tests levonorgestrel for acne, and safety data (warnings, contraindications, DDI) are completely missing — a blocking gap that prevents entry into the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data (DG002)
- A dedicated review of whether levonorgestrel's androgenic profile helps or worsens acne relative to antiandrogenic comparators cited in the literature, given the mixed direction of evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

