---
layout: default
title: Estradiol Valerate
parent: Model Prediction Only (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
monitor_inn: "ESTRADIOL VALERATE"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "anovulation", "ovarian remnant syndrome", "luteoma of pregnancy", "ovarian dysfunction"]
last_modified_at: 2026-10-14
description: "Estradiol Valerate: predicted new indication Symptomatic form of fragile X syndrome in female carrier (evidence level L5). Approved use: Primary ovarian failure"
---

# Estradiol Valerate
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

# Estradiol Valerate: From Primary Ovarian Failure to Fragile X Carrier Symptoms

## One-Sentence Summary

Estradiol valerate is an injectable estrogen, originally used for primary ovarian failure.
The TxGNN model predicts it may be effective for **symptomatic form of fragile X syndrome in female carrier**,
but **no clinical trials and no publications** currently support this specific prediction. It rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary ovarian failure (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carrier |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 4 licenses cancelled) |
| Number of NDAs | 4 (1 NDA and 3 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, estradiol valerate is an ester of estradiol, the natural estrogen, delivered by injection. Its efficacy in replacing estrogen in ovarian hypofunction is established, and mechanistically it may be applicable to conditions that involve a low-estrogen state.

Female carriers of an FMR1 premutation can develop fragile X-associated primary ovarian insufficiency (FXPOI). This overlaps with the original indication of primary ovarian failure, so estrogen replacement is plausible for the hypoestrogenic part of the condition. Replacement would address the ovarian insufficiency symptoms, not the underlying FMR1 disorder. The prediction is therefore best read as a narrow, symptom-level link.

Other high-ranking predictions share the same limitation. Blepharophimosis-epicanthus inversus-ptosis (BPES, including the 3q23 rearrangement form) is linked through FOXL2 and ovarian insufficiency, and estrogen could address only the ovarian component, not the eyelid malformations. The partial trisomy/tetrasomy conditions (chromosome 5p, 12p, 18p) have no identified direct mechanism, and their scores likely reflect network similarity. Ovarian remnant syndrome and luteoma of pregnancy have no clear rationale for estrogen treatment, and estrogen could be harmful in these conditions.

For completeness, two lower-ranked predictions have some supporting material:
- **Anovulation (rank 7):** one Phase 4 trial and literature at evidence level L3. The literature is mostly animal models in which estradiol valerate *induces* anovulation and polycystic ovaries, so the drug acts as a cause rather than a treatment.
- **Ovarian dysfunction (rank 10):** literature at evidence level L4, again mostly disease-model studies in rodents and cattle.

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction (fragile X carrier symptoms).

For reference, the only trial in the compiled data relates to the rank-7 prediction, anovulation:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | Clomiphene citrate plus estradiol versus clomiphene alone for ovulation induction in infertile women. No results provided, and the estradiol formulation is not specified. |

## Literature Evidence

Currently no related literature available for the lead prediction (fragile X carrier symptoms).

For reference, the most relevant human-focused items found for the rank-7 and rank-10 predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36063826](https://pubmed.ncbi.nlm.nih.gov/36063826/) | 2022 | Randomized trial | Gynecol Endocrinol | Different estradiol valerate doses (4, 6, 9 mg/d) and their effects on endometrial estrogen receptor expression and ovarian function in unexplained recurrent abortion |
| [1472813](https://pubmed.ncbi.nlm.nih.gov/1472813/) | 1992 | Clinical report | J Assist Reprod Genet | Oral estradiol valerate 6 mg/d with progesterone in an oocyte donation program for women with ovarian failure or abnormal ovarian function |
| [33749482](https://pubmed.ncbi.nlm.nih.gov/33749482/) | 2021 | Clinical study (design unverified) | Gynecol Endocrinol | Estradiol valerate/nomegestrol acetate for ovarian endometriomas and deep infiltrating endometriosis |
| [9024224](https://pubmed.ncbi.nlm.nih.gov/9024224/) | 1997 | Clinical study | J Clin Endocrinol Metab | Effects of estradiol valerate-based hormone replacement on nitric oxide levels in postmenopausal women |
| [40774400](https://pubmed.ncbi.nlm.nih.gov/40774400/) | 2025 | Review | J Steroid Biochem Mol Biol | Review of agents used to induce PCOS in animal models |
| [12960066](https://pubmed.ncbi.nlm.nih.gov/12960066/) | 2003 | Animal study | Endocrinology | Prepubertal estradiol valerate disrupts cyclicity and causes cystic ovarian morphology in rats |

Most of the remaining retrieved publications are rodent PCOS-model studies in which estradiol valerate is the inducing agent. They are not treatment evidence for the drug.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA009402 | Delestrogen (Par Health USA, LLC) | Injection | Not available (cancelled) |
| ANDA203723 | Estradiol Valerate (Hikma Pharmaceuticals USA Inc.) | Injection | Not available (cancelled) |
| ANDA216656 | Estradiol valerate (Xiromed, LLC) | Injection | Not available (cancelled) |
| ANDA090920 | Estradiol Valerate (American Regent, Inc.) | Injection, solution | Not available (cancelled) |

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

Supplementary information from the knowledge graph (not label text) lists diseases linked to contraindication with estradiol valerate. It includes:
- **Cardiovascular and metabolic:** hypertension, congestive heart failure, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia
- **Hepatic, biliary and renal:** liver disease, gallbladder disease, kidney disease
- **Endocrine and other:** hypothyroidism, hypercalcemia (including humoral hypercalcemia of malignancy), systemic lupus erythematosus, asthma, epilepsy, porphyria, benign prostatic hyperplasia, gynecomastia
- **Psychiatric:** anxiety and dysthymic disorders

These should be checked against the official label. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The fragile X carrier prediction has a high model score (99.94%) but no clinical trials or literature. Evidence level is L5. Any benefit would be limited to estrogen replacement for the ovarian insufficiency component and would not address the underlying FMR1 disorder. All four US licenses are cancelled, and the safety label data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap), obtained from the FDA label
- Mechanism of action data from DrugBank
- Clinical or observational evidence of estrogen replacement in FXPOI (fragile X-associated primary ovarian insufficiency), to clarify whether the prediction adds anything beyond the existing ovarian failure indication
- Confirmation of route and formulation compatibility, since the injectable products are no longer marketed in the US
- A decision on whether to pursue the better-supported but still weak rank-7 (anovulation) and rank-10 (ovarian dysfunction) predictions as separate research questions. The trial and animal-model literature there does not show that estradiol valerate treats these conditions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

