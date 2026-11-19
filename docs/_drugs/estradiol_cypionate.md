---
layout: default
title: Estradiol Cypionate
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
monitor_inn: "ESTRADIOL CYPIONATE"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "partial trisomy/tetrasomy of the short arm of chromosome 12", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 18", "ovarian remnant syndrome", "anovulation", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "blepharophimosis-epicanthus inversus-ptosis", "partial autosomal trisomy/tetrasomy", "luteoma of pregnancy"]
last_modified_at: 2026-11-20
description: "Estradiol Cypionate: predicted new indication Symptomatic form of fragile X syndrome in female carrier (evidence level L5). In the US: 6 FDA applications (1 active)"
---

# Estradiol Cypionate
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

## Estradiol Cypionate: Symptomatic form of fragile X syndrome in female carrier
{: .text-alpha }

## One-Sentence Summary

Estradiol cypionate is a long-acting injectable estrogen, originally used to treat primary ovarian failure.
The TxGNN model predicts it may be effective for **symptomatic form of fragile X syndrome in female carrier**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carrier |
| TxGNN Prediction Score | 0.9969 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 6) |
| Number of FDA Applications | 6 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for estradiol cypionate: "Although circulating estrogens exist in a dynamic equilibrium of metabolic interconversions, estradiol is the principal intracellular human estrogen and is substantially more potent than its metabolites, estrone and estriol, at the receptor level. The primary source of estrogen in normally cycling adult women is the ovarian follicle, which secretes 70 to 500 mcg of estradiol daily, depending on the phase of the menstrual cycle." ([DailyMed: Depo-Estradiol (estradiol cypionate) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9a4229fd-fecd-4ac1-9c4f-6d442533457f), label version 2024-02-28; accessed 2026-11-19.) Based on known pharmacology, estradiol cypionate is an ester of estradiol, given by injection as a long-acting estrogen. It is used to replace estrogen when the ovaries do not produce enough.

Female carriers of an FMR1 premutation can develop fragile X-associated primary ovarian insufficiency (FXPOI). This overlaps directly with the drug's original indication of primary ovarian failure. Estrogen replacement is therefore plausible for the hypoestrogenic manifestations of the condition.

This link is an inference from the original indication and the high TxGNN score, not direct evidence. Estrogen would not be expected to treat other features of fragile X syndrome, such as cognitive or behavioural symptoms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication. The only literature compiled for this report relates to a lower-ranked prediction, **anovulation** (rank 6), and all of it is animal or formulation research, so it does not support the fragile X prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17491141](https://pubmed.ncbi.nlm.nih.gov/17491141/) | 2007 | Review (veterinary) | Society of Reproduction and Fertility Supplement | Strategies to control follicle growth and synchronize ovulation in dairy cattle (Ovsynch program) |
| [12512597](https://pubmed.ncbi.nlm.nih.gov/12512597/) | 2002 | Animal study | Journal of Dairy Science | Estradiol cypionate (10 mg) extended the postpartum anovulatory period in dairy cows |
| [35150853](https://pubmed.ncbi.nlm.nih.gov/35150853/) | 2022 | Preclinical formulation study | Journal of Equine Veterinary Science | SAIB as a delivery vehicle for estradiol cypionate and sulpiride in geldings and seasonally anovulatory mares |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA085470 | DEPO-ESTRADIOL | PFIZER | Injectable; injection | Valid |
| ANDA085620 | ESTRADIOL CYPIONATE | DR REDDYS | Injectable; injection | Discontinued in Drugs@FDA |
| ANDA089310 | ESTRADIOL CYPIONATE | QUAD PHARMS | Injectable; injection | Discontinued in Drugs@FDA |
| ANDA085603 | TESTOSTERONE CYPIONATE-ESTRADIOL CYPIONATE | WATSON LABS | Injectable; injection | Discontinued in Drugs@FDA |
| NDA017968 | DEPO-TESTADIOL | PHARMACIA AND UPJOHN | Injectable; injection | Discontinued in Drugs@FDA |

Showing 5 of 6 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for safety information.

The drug-disease knowledge graph lists a number of conditions associated with contraindication or caution for this drug. These come from the graph, not from label text, and should be verified against the official label. They include:

- **Cardiovascular:** hypertension, congestive heart failure
- **Hepatic and renal:** liver disease, liver failure, gallbladder disease, kidney disease
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, hypothyroidism, humoral hypercalcemia of malignancy
- **Neurological and psychiatric:** epilepsy, anxiety disorder, dysthymic disorder, substance abuse/dependence
- **Other:** asthma, systemic lupus erythematosus, osteoporosis, benign prostatic hyperplasia, gynecomastia

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible for the ovarian insufficiency component of fragile X premutation carriers, but it is supported only by a model score. There are no clinical trials or human literature, and the original mechanism data and label safety data are missing.

<!-- review:begin us-lic-20261106-estradiol_cypionate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials or human literature, and the original mechanism data and label safety data are missing. The drug is also cancelled-only in the US market." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 6 FDA applications or NDC listings for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-estradiol_cypionate-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are blocking for safety screening
- Mechanism of action data (for example, from DrugBank)
- A literature search on estrogen replacement in FXPOI and FMR1 premutation carriers
- A clear definition of the target outcome (ovarian insufficiency symptoms versus other fragile X features)
- Confirmation of an available marketed estradiol product and route
- Review of the knowledge graph contraindication list against the official label

<!-- review:begin us-lic-20261106-estradiol_cypionate-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of an available marketed estradiol product and route, since this license is cancelled" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 6 FDA applications or NDC listings for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-estradiol_cypionate-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The drug is also cancelled-only in the US market" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since this license is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Depo-Estradiol (estradiol cypionate) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9a4229fd-fecd-4ac1-9c4f-6d442533457f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

