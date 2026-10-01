---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 848
evidence_level: L1
indication_count: 10
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Letrozole: From Breast Cancer (Established Use) to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is an oral aromatase inhibitor already marketed in the US, and its established use is hormone-dependent breast cancer.
The TxGNN model predicts it for **female breast carcinoma**, which largely confirms this existing indication rather than proposing a new one.
The prediction is backed by **50 clinical trials** and **20 publications**, including completed Phase 3 randomized trials.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed entries are generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

The license records contain no approved-indication text, so the original indication is taken from the pack's own rationale (breast cancer is an established, marketed use).

## Why is This Prediction Reasonable?

Letrozole is a non-steroidal aromatase inhibitor. It blocks the final step of estrogen synthesis. This lowers estrogen, which drives growth in hormone-dependent breast tumors. The mechanism-of-action field in the Evidence Pack is empty. The description above comes from the pack's rationale text and the literature (for example PMID 17912633, on the discovery and mechanism of letrozole).

Breast cancer is the drug's established use. The prediction is therefore best read as confirmation, not true repurposing. Direct efficacy evidence exists in the ER-positive setting, including the adjuvant letrozole vs tamoxifen trial published in NEJM. Completed Phase 3 trials also support the use, including a neoadjuvant letrozole vs tamoxifen trial (n=177).

The same score pattern appears across many breast cancer sub-terms, such as ER-negative, bilateral disease and expression subtypes. Those are covered in the conclusion.

## Clinical Trial Evidence

The pack lists 50 trials. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949598](https://clinicaltrials.gov/study/NCT00949598) | Phase 3 | Completed | 177 | Randomized, double-blind neoadjuvant letrozole vs tamoxifen in postmenopausal ER+ breast cancer |
| [NCT00673335](https://clinicaltrials.gov/study/NCT00673335) | Phase 3 | Completed | 170 | Letrozole vs placebo for preventing breast cancer in BRCA1/2 carriers |
| [NCT07085767](https://clinicaltrials.gov/study/NCT07085767) | Phase 3 | Recruiting | 1000 | Palazestrant + ribociclib vs letrozole + ribociclib; letrozole is the standard-of-care comparator |
| [NCT00369850](https://clinicaltrials.gov/study/NCT00369850) | Phase 3 | Completed | 458 | Bone density and bone loss in women treated on IBCSG 1-98 (safety monitoring, not efficacy) |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Effects of letrozole and tamoxifen on bone and lipids in early breast cancer |
| [NCT02214004](https://clinicaltrials.gov/study/NCT02214004) | Phase 2 | Unknown | 132 | Preoperative trastuzumab + letrozole in HR+/HER2+ postmenopausal patients |
| [NCT05183828](https://clinicaltrials.gov/study/NCT05183828) | Phase 4 | Recruiting | 68 | HSD3B1 genotype and response to preoperative letrozole (patient selection) |
| [NCT02679755](https://clinicaltrials.gov/study/NCT02679755) | Phase 4 | Completed | 252 | Palbociclib + letrozole in postmenopausal HR+/HER2- advanced breast cancer |
| [NCT02520063](https://clinicaltrials.gov/study/NCT02520063) | Phase 1/2 | Completed | 15 | Neoadjuvant letrozole + everolimus + TRC105 in HR+/HER2- breast cancer |
| [NCT04571437](https://clinicaltrials.gov/study/NCT04571437) | Phase 2 | Unknown | 204 | Letrozole with or without metronomic capecitabine in first-line ER+ advanced disease |

## Literature Evidence

The pack lists 20 publications. The 10 most relevant are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | Randomized adjuvant trial | N Engl J Med | Letrozole vs tamoxifen as adjuvant therapy in postmenopausal, hormone-receptor-positive early breast cancer |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Pharmacology, toxicity and potential therapeutic effects of letrozole |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics, pharmacokinetics, efficacy and safety of letrozole |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opin Pharmacother | Comparison of anastrozole, letrozole and exemestane in early breast cancer; aromatase inhibitors consistently superior to tamoxifen |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opin Pharmacother | Third-generation aromatase inhibitors have changed standard hormonal therapy |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast | Development of letrozole, its use in advanced disease and in the neoadjuvant setting |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Mechanism review | Breast Cancer Res Treat | Discovery and mechanism of action of letrozole (aromatase inhibition) |
| [18829517](https://pubmed.ncbi.nlm.nih.gov/18829517/) | 2008 | Clinical study | Clin Cancer Res | Letrozole suppressed tissue and plasma estrogen levels more than anastrozole |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | Cohort | Comput Math Methods Med | Tamoxifen-then-letrozole sequence vs letrozole alone for breast carcinoma |
| [41519129](https://pubmed.ncbi.nlm.nih.gov/41519129/) | 2026 | Trial analysis | Cell Rep Med | NeoPAL: molecular changes after neoadjuvant letrozole + palbociclib vs chemotherapy (n=103) |

## US Market Information

The pack reports 20 licenses in total. All five listed here are generic ANDAs for oral tablets. No approved-indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA200161 | Letrozole | Tablet | Bryant Ranch Prepack |
| ANDA200161 | Letrozole | Tablet | Natco Pharma Limited |
| ANDA205869 | Letrozole | Tablet, film coated | Avet Pharmaceuticals Inc. |
| ANDA090289 | Letrozole | Tablet, film coated | Proficient Rx LP |
| ANDA090934 | Letrozole | Tablet, film coated | Bryant Ranch Prepack |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, non-steroidal aromatase inhibitor; not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Bone density and lipid profile (the focus of completed Phase 3 trials NCT00369850 and NCT00171704); other items per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. The pack has no warnings, contraindications or drug-interaction data, and the interaction query returned no results.

The trials and literature point to some issues worth monitoring:
- Bone loss and lipid changes.
- Aromatase-inhibitor-associated musculoskeletal and joint symptoms.
- A rare case report of letrozole-related maculopathy (PMID 37602160).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast cancer is an established, marketed use of letrozole, and multiple completed Phase 3 randomized trials support it (L1). The guardrails are use within labeled populations, mainly ER-positive disease, under clinician oversight. Other predicted terms should not be adopted as new indications:
- ER-negative breast cancer (Hold): aromatase inhibition depends on estrogen signaling, so no benefit is expected. The high score and trial volume appear to come from ER-positive records mapped to this term.
- Bilateral carcinoma, expression subtypes and hormone-resistant disease (Research Question): the trials are general breast cancer studies or combination regimens.
- Nipple carcinoma (Research Question): only indirect evidence, with no site-specific data.
- Ehrlich tumor, fibrocystic disease and benign mammary dysplasia (Hold): a mouse model with preclinical work only, or model prediction alone.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, indications), which is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- A safety monitoring plan covering bone density, lipids and musculoskeletal symptoms.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

