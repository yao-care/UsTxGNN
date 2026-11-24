---
layout: default
title: Doxercalciferol
parent: Model Prediction Only (L5)
nav_order: 625
evidence_level: L5
indication_count: 1
monitor_inn: "DOXERCALCIFEROL"
predicted_indications: ["obsolete vitamin D deficiency"]
last_modified_at: 2026-11-20
description: "Doxercalciferol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). In the US: 18 FDA applications (6 active)"
---

# Doxercalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Doxercalciferol: Obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Doxercalciferol is a synthetic vitamin D2 analog. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **"obsolete vitamin D deficiency"** with a very high score (0.9948), but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9948 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (active FDA-approved applications: 6 of 18) |
| Number of FDA Applications | 18 (active: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for doxercalciferol: "Doxercalciferol is a synthetic vitamin D 2 analog that requires metabolic activation to form the active 1α,25-(OH) 2 D 2 metabolite, which binds to the vitamin D receptor (VDR) to result in the selective activation of vitamin D responsive pathways. Vitamin D and doxercalciferol have been shown to reduce PTH levels by inhibiting PTH synthesis and secretion." ([DailyMed: doxercalciferol prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d07fa4f-f2a2-4c2b-86bf-c0a4691c1a0a), label version 2026-08-05; accessed 2026-11-19.) Based on general knowledge of the drug class, doxercalciferol is a prohormone of vitamin D2. It is hydroxylated in the liver to 1α,25-dihydroxyvitamin D2, the active form, which binds the vitamin D receptor. This is biologically consistent with correcting vitamin D deficiency and helps explain the high TxGNN score.

However, the prediction should be read with caution. The disease label is "obsolete", which suggests a deprecated ontology term rather than a currently used diagnosis. The drug's established use, secondary hyperparathyroidism in chronic kidney disease, relies on the same vitamin D pathway. The prediction is therefore likely a restatement of known pharmacology rather than a novel repurposing signal. The link to the original indication could not be assessed further because no approved indication text was available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The approved indication text is not available in the compiled data.

<!-- review:begin us-lic-20261105-doxercalciferol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All five authorizations are valid. The approved indication text is not available in the compiled data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-doxercalciferol-1 -->

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA210452 | Doxercalciferol (Dr. Reddy's Laboratories Inc) | Injection | Valid |
| ANDA213717 | Doxercalciferol (Eugia US LLC) | Injection, solution | ANDA (Discontinued in Drugs@FDA) |
| ANDA215810 | Doxercalciferol (Alembic Pharmaceuticals Inc.) | Injection, solution | Valid |
| ANDA211670 | Doxercalciferol (Meitheal Pharmaceuticals Inc.) | Injection, solution | Valid |
| ANDA205360 | Doxercalciferol (Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc.) | Capsule | Valid |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data, so please refer to the package insert for them.

- **Disease contraindications from the knowledge graph** (these come from drug–disease relationships in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hyperphosphatemia, hypervitaminosis, and hypoparathyroidism.
- **Drug interactions**: 70 interactions were identified. The main ones from the first 20 reviewed are:
  - **Major**: other vitamin D agents (cholecalciferol, calcifediol, calcitriol, dihydrotachysterol, ergocalciferol), aluminum hydroxide, and sucralfate.
  - **Moderate**: magnesium-containing products (oxide, carbonate, chloride, citrate, gluconate, hydroxide, sulfate), mineral oil, sevelamer, iron sucrose, fostamatinib, and topical calcitriol.
  - **Minor**: orlistat.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5), with no trials or publications. The target disease term is obsolete, and the prediction likely restates the drug's known vitamin D pharmacology rather than a new use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism of action data
- The approved indication text, to define the original indication
- Mapping of the obsolete disease term to a current vitamin D deficiency definition
- Searches for clinical trials and literature on vitamin D deficiency
- Route compatibility assessment and clarification of the US market status

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All five authorizations are valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data are not available in the compiled record" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: doxercalciferol prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d07fa4f-f2a2-4c2b-86bf-c0a4691c1a0a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

