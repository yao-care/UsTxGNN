---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 858
evidence_level: L5
indication_count: 4
monitor_inn: "LEVOTHYROXINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-30
description: "Levothyroxine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Hypothyroidism"
---

# Levothyroxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Levothyroxine: From Hypothyroidism to Renal Hypodysplasia/Aplasia
{: .text-alpha }

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone, recorded in the knowledge graph for hypothyroidism and other thyroid conditions.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (relation recorded in the knowledge graph; the licence records contain no indication text) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of FDA Applications | at least 11 |
| Number of approvals | At least 11 (NDAs and ANDAs; the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Levothyroxine is a thyroid hormone replacement, and its use in thyroid disease is an established indication.

There is no established mechanistic link to the predicted disease. Thyroid hormone contributes to normal kidney development and function, and congenital hypothyroidism has been associated with a higher rate of congenital anomalies of the kidney and urinary tract. That is an epidemiological association only. Renal hypodysplasia and aplasia are structural malformations that form before birth, and replacing a hormone after birth is not expected to reverse them. The high score (0.9967) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a treatable mechanism.

Other predictions for this drug (bilateral renal agenesis, Potter sequence, Carney complex) are likewise supported by no trials or publications. Only Carney complex has a tissue-level link to the thyroid, through thyroid nodules, where TSH suppression might be an adjunctive use. That remains speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The records below are single-ingredient levothyroxine products. Indication text is not included in the licence records. The list shows 5 of at least 11 approvals and may be partial.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021402 | Synthroid (AbbVie Inc.) | Tablet | Not stated in the records |
| NDA021924 | Tirosint (IBSA Pharma Inc.) | Capsule | Not stated in the records |
| NDA202231 | Levothyroxine Sodium (Fresenius Kabi USA, LLC) | Lyophilized powder for injection | Not stated in the records |
| NDA021116 | Levothyroxine sodium (Preferred Pharmaceuticals, Inc.) | Tablet | Not stated in the records |
| ANDA216729 | Levothyroxine Sodium (OneSource Specialty Pharma Limited) | Lyophilized powder for injection | Not stated in the records |

Available routes: oral (tablet, capsule) and injectable (lyophilized powder).

## Safety Considerations

**Knowledge-graph contraindication relations** (not label text): hypertension, hypopituitarism and other pituitary hormone deficiencies, Kallmann syndrome and hypogonadotropic hypogonadism, osteoporosis (including postmenopausal), diabetes mellitus, diabetic ketoacidosis, coronary artery disease, myocardial infarction, and thymus gland disease.

**Drug Interactions** (100 recorded; mostly moderate severity). Main examples:
- Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, dulaglutide, albiglutide, chlorpropamide
- Acid-reducing agents: omeprazole, rabeprazole, dexlansoprazole (moderate); cimetidine (minor)
- Minerals and antacids: calcium phosphate, calcium acetate, magnesium oxide
- Sympathomimetics: epinephrine, isometheptene, diethylpropion

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications and no plausible mechanism for reversing a structural renal malformation. Renal hypodysplasia/aplasia is a developmental condition that is unlikely to respond to postnatal thyroid hormone replacement.

**To proceed, the following is needed:**
- Any clinical or preclinical study directly addressing levothyroxine in renal hypodysplasia/aplasia
- A mechanistic rationale for how thyroid hormone could affect renal development in this condition
- Package insert warnings and contraindications, and mechanism of action data
- If a related use is pursued, review the Carney complex thyroid-nodule (TSH suppression) idea separately, with attention to cardiac and bone risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

