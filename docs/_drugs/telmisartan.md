---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 1206
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB) marketed in the US as an oral tablet, used for hypertension.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this top-ranked prediction has **0 clinical trials** and **0 publications** behind it.
Stronger evidence exists for two lower-ranked predictions, cerebral artery occlusion and intracerebral hemorrhage (see the last section before the conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from the Evidence Pack rationale text; the US license records contain no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for telmisartan is not available in the Evidence Pack. Based on known information, telmisartan blocks the angiotensin II type 1 (AT1) receptor and also acts as a partial PPARγ agonist. Its efficacy in hypertension is established.

Angiotensin II-mediated vasoconstriction and endothelial dysfunction are plausible contributors to coronary vasospasm, which is the basis of Prinzmetal angina. That gives the prediction some biological plausibility.

However, calcium channel blockers and nitrates are the established therapy for this condition. No telmisartan-specific trial or publication was supplied, so the score reflects the knowledge-graph relationship only, not clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202397 | Telmisartan | Tablet | A-S Medication Solutions |
| ANDA205150 | telmisartan | Tablet | Bryant Ranch Prepack |
| ANDA203986 | Telmisartan | Tablet | NorthStar RxLLC |
| ANDA208605 | Telmisartan | Tablet | Bryant Ranch Prepack |
| ANDA090032 | Telmisartan | Tablet | Glenmark Pharmaceuticals Inc., USA |

Only the oral route (tablet) is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Predicted Indications With Evidence

Two lower-ranked predictions carry more evidence than the top-ranked one.

| Rank | Indication | Score | Evidence Level | What the Evidence Shows |
|------|------|------|------|---------|
| 4 | Cerebral artery occlusion | 99.95% | L4 | 1 Phase 4 trial ([NCT01075698](https://clinicaltrials.gov/study/NCT01958698), completed, n=1228, cardiovascular prevention) plus mostly rodent studies (tMCAO models) showing reduced infarct volume, oxidative stress and inflammation. No human treatment data for acute occlusion. |
| 9 | Intracerebral hemorrhage | 99.93% | L2 | [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) (TRIDENT, Phase 3, completed, n=1671) tested a triple low-dose antihypertensive pill, with telmisartan as one component, for preventing recurrent stroke. No results were supplied, and telmisartan's own contribution cannot be isolated. |

Both are classified "Research Question" in the Evidence Pack. The remaining predictions (brain stem infarction, ABri amyloidosis, the two pulmonary hypertension entries, malignant renovascular hypertension, malignant hypertensive renal disease, Braddock syndrome) are prediction-only with no supporting trials or literature. For malignant renovascular hypertension, RAAS blockade also carries a risk of acute renal function decline, which argues against advancing it.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Prinzmetal angina is supported only by a model score. There are no trials or publications, and established therapies already exist. Any further work is better directed at the cerebral ischemia and intracerebral hemorrhage candidates.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A telmisartan-specific literature and trial search for Prinzmetal angina
- For intracerebral hemorrhage, TRIDENT results and any analysis separating telmisartan's contribution
- For cerebral artery occlusion, human data beyond the rodent studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

