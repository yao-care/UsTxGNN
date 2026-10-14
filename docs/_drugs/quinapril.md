---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 1101
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Quinapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 5 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, quinapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension, which is strongly driven by activation of the renin-angiotensin system.

The new indication is closely related to the original one. It is largely an extension of the hypertension indication rather than a distinct repurposing opportunity. There is also a notable caution: ACE inhibitors carry a known risk of acute renal failure in patients with bilateral renal artery stenosis, a common cause of renovascular hypertension, so any use would require careful caution.

**Other predicted indications (for reference):**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.86% | L5 | Plausible link through reduced angiotensin II-mediated vascular injury and glomerular hypertension, but prediction-only |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.85% | L4 | Two animal studies, including one showing reduced hypoxic pulmonary hypertension in rats; no human data (Research Question) |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.85% | L5 | Only indirect extrapolation; prediction-only |
| Braddock syndrome | 99.79% | L5 | No clear mechanistic link; may reflect a knowledge-graph artifact |

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

All five US authorizations are cancelled; no valid authorization currently exists.

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
The 99.86% TxGNN score is not backed by any clinical trial or publication, and the new indication largely overlaps with the original hypertension indication. All US authorizations are cancelled, and the kidney-related safety signals are directly relevant to this setting.

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

