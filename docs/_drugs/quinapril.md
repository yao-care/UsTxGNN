---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 1101
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Quinapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Quinapril
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

## Quinapril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Quinapril is an ACE inhibitor originally used to treat hypertension.
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of FDA Applications | at least 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, quinapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension, which is strongly driven by activation of the renin-angiotensin system.

The new indication is closely related to the original one. It is largely an extension of the hypertension indication rather than a distinct repurposing opportunity. There is also a notable caution: ACE inhibitors carry a known risk of acute renal failure in patients with bilateral renal artery stenosis, a common cause of renovascular hypertension, so any use would require careful caution.

**Other predicted indications (for reference):**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Malignant hypertensive renal disease | 0.9986 | L5 | Plausible link through reduced angiotensin II-mediated vascular injury and glomerular hypertension, but prediction-only |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9985 | L5 | Two animal studies, including one showing reduced hypoxic pulmonary hypertension in rats; no human data (Research Question) |
| Pulmonary hypertension with unclear multifactorial mechanism | 0.9985 | L5 | Only indirect extrapolation; prediction-only |
| Braddock syndrome | 0.9979 | L5 | No clear mechanistic link; may reflect a TxGNN model (deep learning) artifact |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For the closest related prediction (pulmonary hypertension owing to lung disease and/or hypoxia), the following preclinical studies were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Animal study | Circulation | Inhibiting tissue ACE with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodeling in rats |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Animal study | J Cardiovasc Pharmacol | Quinapril preserved left ventricular function and energy metabolism in rats after myocardial infarction (indirect relevance) |

---

## US Market Information


| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078457 (Cipla USA) | Quinapril | Tablet | Not available (cancelled) |
| ANDA077690 (Lupin) | Quinapril | Tablet | Not available (cancelled) |
| ANDA205823 (Solco Healthcare) | Quinapril | Tablet | Not available (cancelled) |
| ANDA202725 (Aurobindo) | Quinapril | Tablet, film coated | Not available (cancelled) |
| ANDA076803 (Chartwell RX) | Quinapril | Tablet, film coated | Not available (cancelled) |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report; please refer to the package insert for label safety information.

- **Disease contraindications from the knowledge graph (not label text):** kidney disease, angioedema (including hereditary, acquired, and RAAS-blocker-induced forms), pancreatitis, liver disease, hepatic coma/encephalopathy, gallbladder disease, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hypotensive disorder, neutropenia/agranulocytosis, hyperparathyroidism, connective tissue disease, gout, anuria, and neonatal jaundice.
- **Drug Interactions:** 100 interactions were identified. The one rated **Major** is **potassium citrate** (risk of hyperkalaemia). Many others are rated Moderate, including metformin, canagliflozin, dapagliflozin, chlorpropamide, acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), tetracyclines (doxycycline, tetracycline), bupropion, morphine, and atropine.
- **Indication-specific cautions:** risk of acute renal failure in bilateral renal artery stenosis; renal function and potassium monitoring needed; possible systemic hypotension if considered for pulmonary hypertension.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9986 TxGNN score is not backed by any clinical trial or publication, and the new indication largely overlaps with the original hypertension indication.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clinical or observational evidence of quinapril in renovascular or malignant hypertension, especially renal safety in renal artery stenosis
- Clarification of why US authorizations were cancelled, and the route and formulation requirements
- If pursuing the pulmonary hypertension direction, human data to supplement the animal-only evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

