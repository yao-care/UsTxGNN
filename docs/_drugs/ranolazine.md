---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 1111
evidence_level: L5
indication_count: 1
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-10-28
description: "Ranolazine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ranolazine
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

## Ranolazine: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ranolazine is an antianginal drug that inhibits the late sodium current. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | 9 (all cancelled; these are ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ranolazine is generally described as an antianginal agent that inhibits the late sodium current (INa) and, to a lesser extent, the rapid delayed rectifier potassium current (IKr).

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations cause constitutive receptor activation and unsuppressed water reabsorption, which leads to hyponatremia.

No established mechanistic link has been identified between ranolazine and this condition. No published data show that ranolazine acts on V2 receptor signaling, cAMP production, or aquaporin-2 trafficking. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It has not been supported by any clinical or experimental evidence, so it should be read as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| ANDA201046 | Ranolazine (Lupin Pharmaceuticals) | Film-coated extended-release tablet | Not provided | Valid |
| ANDA210054 | Ranolazine (Ajanta Pharma USA) | Extended-release tablet | Not provided | Valid |
| ANDA210188 | Ranolazine (Vangard Labs) | Extended-release tablet | Not provided | Valid |
| ANDA211829 | Ranolazine (ScieGen Pharmaceuticals) | Film-coated extended-release tablet | Not provided | Valid |
| ANDA209953 | Ranolazine (Ascend Laboratories) | Film-coated extended-release tablet | Not provided | Valid |

Nine licenses are recorded in total, all cancelled. Only the first five are listed here.

## Safety Considerations

- **Disease contraindications from the knowledge graph** (these come from the TxGNN knowledge graph, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, and cirrhosis of liver.
- **Drug Interactions**: 100 interactions were found in total. Examples at the **Major** level include aprepitant, dexamethasone, clarithromycin, dolasetron, and eliglustat. Moderate-level examples include famotidine, metformin, loperamide, budesonide, canagliflozin, dapagliflozin, and empagliflozin. Minor-level examples include bupropion, lorcaserin, and cimetidine.

Both the QT-related contraindications and the kidney disease contraindication deserve attention for a possible renal indication such as NSIAD. Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanistic link to the V2 receptor pathway.

**To proceed, the following is needed:**
- Mechanism of action data for ranolazine, and any experimental evidence of an effect on V2 receptor signaling, cAMP production, or aquaporin-2 trafficking
- Preclinical studies (for example, cell-based AVPR2 gain-of-function models) to test the hypothesis
- Package insert warnings and contraindications, to allow a proper safety screening, particularly for renal impairment and QT prolongation
- Clarification of the original approved indication and of the regulatory status (the drug is marketed, with 9 valid licenses)
- Assessment of route and formulation compatibility, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

