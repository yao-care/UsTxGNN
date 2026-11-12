---
layout: default
title: Omidenepag Isopropyl
parent: Model Prediction Only (L5)
nav_order: 994
evidence_level: L5
indication_count: 7
monitor_inn: "OMIDENEPAG ISOPROPYL"
predicted_indications: ["pancreatitis", "hyperphosphatemia (disease)", "esophageal varices without bleeding", "esophageal varices with bleeding", "blepharospasm", "familial visceral myopathy", "alcoholic cardiomyopathy"]
last_modified_at: 2026-11-12
description: "Omidenepag Isopropyl: predicted new indication Pancreatitis (evidence level L5). Approved use: Ocular hypertension"
---

# Omidenepag Isopropyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Omidenepag Isopropyl: From Ocular Hypertension/Glaucoma to Pancreatitis
{: .text-alpha }

## One-Sentence Summary

Omidenepag isopropyl is a topical ophthalmic prodrug originally used to lower intraocular pressure in ocular hypertension and glaucoma.
The TxGNN model predicts it may be effective for **pancreatitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular hypertension; glaucoma |
| Predicted New Indication | Pancreatitis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omidenepag isopropyl is a prodrug. Its active metabolite, omidenepag, is a selective EP2 receptor agonist. EP2 signaling raises intracellular cAMP and has anti-inflammatory and smooth-muscle-relaxing effects, which could plausibly bear on pancreatic inflammation. Detailed mechanism-of-action data are not currently available in the compiled data, so this reasoning is based on the known pharmacology of the drug class.

The link between the original and new indications is weak. Glaucoma treatment relies on increasing aqueous humour outflow in the eye, while pancreatitis is an inflammatory disease of an internal organ. The drug is a topical eye drop with minimal systemic exposure, and no pancreatic data exist. The high TxGNN score (0.9976, model rank 6,557) is a computational prediction only.

Other predicted indications in the data have similarly high scores but also lack any supporting trials or literature:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hyperphosphatemia | 0.9973 | L5 | No plausible mechanistic link to phosphate homeostasis identified |
| 3 | Esophageal varices without bleeding | 0.9931 | L5 | Vasodilation could be counterproductive in portal hypertension |
| 4 | Esophageal varices with bleeding | 0.9931 | L5 | Same score as rank 3; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; acute bleeding needs systemic therapy |
| 5 | Blepharospasm | 0.9927 | L5 | Anatomically close, but EP2 agonism has no established role in dystonia; prostaglandin analogs have periocular adverse effects |
| 6 | Familial visceral myopathy | 0.9919 | L5 | Would not address the underlying genetic defect |
| 7 | Alcoholic cardiomyopathy | 0.9916 | L5 | Only indirect preclinical EP2 rationale; cardiac exposure unlikely |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA215092 | OMLONTI | OCUVEX THERAP | Solution; ophthalmic | Valid |

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report, and no disease-level contraindications were recorded.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pancreatitis prediction is supported only by a model score, with no clinical trials or publications (Evidence Level L5). Safety and mechanism data are also incomplete, so the evaluation cannot move beyond the earliest screening stage.

<!-- review:begin us-lic-20261031-omidenepag_isopropyl-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The pancreatitis prediction is supported only by a model score, with no clinical trials or publications (Evidence Level L5). The drug is a topical ocular product with minimal systemic exposure, and its only US authorization is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-omidenepag_isopropyl-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data for the active metabolite
- Preclinical evidence (in vitro or animal models) that EP2 agonism affects pancreatic inflammation
- Assessment of route compatibility, since a systemic formulation would likely be needed and none exists

<!-- review:begin us-lic-20261106-omidenepag_isopropyl-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Assessment of route compatibility, since a systemic formulation would likely be needed and none exists / Clarification of the cancelled NDA status and the reasons for it" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-omidenepag_isopropyl-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The drug is a topical ocular product with minimal systemic exposure, and its only US authorization is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Clarification of the cancelled NDA status and the reasons for it" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

