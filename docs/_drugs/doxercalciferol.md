---
layout: default
title: Doxercalciferol
parent: Model Prediction Only (L5)
nav_order: 625
evidence_level: L5
indication_count: 1
monitor_inn: "DOXERCALCIFEROL"
predicted_indications: ["obsolete vitamin D deficiency"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Doxercalciferol: From Vitamin D–Related Disorders to Vitamin D Deficiency (Obsolete Term)

## One-Sentence Summary

Doxercalciferol is a synthetic vitamin D2 analog. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **"obsolete vitamin D deficiency"** with a very high score (99.48%), but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (the approved indication text is empty for all authorizations) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 5 (all cancelled; these are ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled record. Based on general knowledge of the drug class, doxercalciferol is a prohormone of vitamin D2. It is hydroxylated in the liver to 1α,25-dihydroxyvitamin D2, the active form, which binds the vitamin D receptor. This is biologically consistent with correcting vitamin D deficiency and helps explain the high TxGNN score.

However, the prediction should be read with caution. The disease label is "obsolete", which suggests a deprecated ontology term rather than a currently used diagnosis. The drug's established use, secondary hyperparathyroidism in chronic kidney disease, relies on the same vitamin D pathway. The prediction is therefore likely a restatement of known pharmacology rather than a novel repurposing signal. The link to the original indication could not be assessed further because no approved indication text was available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All five authorizations are cancelled. The approved indication text is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA210452 | Doxercalciferol (Dr. Reddy's Laboratories Inc) | Injection | Cancelled |
| ANDA213717 | Doxercalciferol (Eugia US LLC) | Injection, solution | Cancelled |
| ANDA215810 | Doxercalciferol (Alembic Pharmaceuticals Inc.) | Injection, solution | Cancelled |
| ANDA211670 | Doxercalciferol (Meitheal Pharmaceuticals Inc.) | Injection, solution | Cancelled |
| ANDA205360 | Doxercalciferol (Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc.) | Capsule | Cancelled |

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
The prediction rests on the model score alone (Evidence Level L5), with no trials or publications. The target disease term is obsolete, and the prediction likely restates the drug's known vitamin D pharmacology rather than a new use. The drug also has no currently valid US authorization, and its safety label data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism of action data
- The approved indication text, to define the original indication
- Mapping of the obsolete disease term to a current vitamin D deficiency definition
- Searches for clinical trials and literature on vitamin D deficiency
- Route compatibility assessment and clarification of the US market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

