---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 5
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-11-24
description: "Ergocalciferol: predicted new indication Acromesomelic dysplasia, Campailla Martinelli type (evidence level L5). In the US: 23 FDA applications (5 active), plus 4 OTC monograph/unapproved NDC listings"
---

# Ergocalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ergocalciferol: Acromesomelic dysplasia, Campailla Martinelli type
{: .text-alpha }

## One-Sentence Summary

Ergocalciferol (vitamin D2) is a vitamin D product used in vitamin D deficiency and bone and mineral disorders such as rickets, osteomalacia and osteoporosis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Campailla Martinelli type**, a rare skeletal dysplasia.
Evidence is minimal: **0 clinical trials** and **0 publications** support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Campailla Martinelli type |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 5 of 23; OTC monograph / unapproved listings: 4) |
| Number of FDA Applications | 23 (active: 5) |
| Number of approvals | At least 5 (4 ANDAs and 1 NDA listed; the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for ergocalciferol: "The in vivo synthesis of the major biologically active metabolites of vitamin D occurs in two steps. The first hydroxylation of ergocalciferol takes place in the liver (to 25-hydroxyvitamin D) and the second in the kidneys (to 1, 25-dihydroxyvitamin D)." ([DailyMed: Vitamin D (ergocalciferol) prescribing information, Preferred Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba2076ef-1650-45e1-b092-a4c449dd6210), label version 2026-11-02; accessed 2026-11-19.) Ergocalciferol is a vitamin D analogue whose efficacy in vitamin D deficiency and related bone disorders is well known. Mechanistically it might be applicable to skeletal disease, but no specific link to this condition has been established.

The predicted condition is a rare inherited skeletal dysplasia. The score of 0.9983 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No mechanistic or clinical evidence connects ergocalciferol to this disease, so the prediction should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- review:begin us-lic-20261124b-ergocalciferol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All five listed licences are single-ingredient products with valid status." Removed: this statement described the earlier model-written license table, which has been replaced by the program-generated table under US Market Information (Drugs@FDA and the NDC Directory). Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-ergocalciferol-1 -->

<!-- review:begin us-lic-20261124b-ergocalciferol-2 -->

> **Review correction (2026-11-24)**: Originally stated: "All listed forms are oral." Removed: the dosage-form statement did not match the dosage forms of all FDA applications on record (Drugs@FDA and the NDC Directory); see the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-ergocalciferol-2 -->

The licence records do not include approved-indication text, so no label indication is cited here. 

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040833 | ERGOCALCIFEROL | CHARTWELL RX | Capsule; oral | Valid |
| ANDA080704 | VITAMIN D | BIONPHARMA | Capsule; oral | Valid |
| ANDA090455 | ERGOCALCIFEROL | ONESOURCE | Capsule; oral | Valid |
| ANDA204276 | ERGOCALCIFEROL | PURACAP PHARM LLC | Capsule; oral | Valid |
| NDA003444 | DRISDOL | ESJAY PHARMA | Capsule; oral | Valid |

Showing 5 of 27 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

 The total number of licences is "at least 5", so this list may be partial.

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

- **Contraindication relations recorded in the knowledge graph (not label text):** hypercalcemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, hypertension, diabetes mellitus, atrial fibrillation, primary hyperoxaluria, Wilson disease, hyperlipidemia, and prostate and breast cancers, among others.
- **Drug interactions (55 recorded):**
  - Major: other vitamin D agents (cholecalciferol, calcifediol, calcitriol, doxercalciferol), because of additive hypercalcemia risk.
  - Moderate: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone), bile acid sequestrants (cholestyramine, colestipol, colesevelam), sevelamer, digoxin, carbamazepine, rifabutin, barbiturates (amobarbital, butalbital) and magnesium oxide.
  - Minor: cimetidine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no trials or publications for acromesomelic dysplasia, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a biological rationale linking vitamin D2 to the genetic basis of this dysplasia
- Preclinical or case-level evidence in this condition
- Label warnings and contraindications from the package insert, to complete safety screening

**Note on other candidates:** Among the other predictions for this drug, renal osteodystrophy has the most supporting data. It has one Phase 4 trial (NCT01799317, n=60, status unknown) and a randomized comparison of ergocalciferol versus calcitriol in CKD mineral bone disorder (PMID 27401037). It is a more promising direction for further evaluation than the top-ranked prediction. Calcium-alkali syndrome, on the other hand, may be harmful, because vitamin D can aggravate hypercalcemia.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vitamin D (ergocalciferol) prescribing information, Preferred Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba2076ef-1650-45e1-b092-a4c449dd6210) |
| 2026-11-24 | Removed: "All five listed licences are single-ingredient products with valid status." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-24 | Removed: "All listed forms are oral." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

