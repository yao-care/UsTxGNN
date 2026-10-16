---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 6
monitor_inn: "AMILORIDE"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-14
description: "Amiloride: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
---

# Amiloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Amiloride: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiloride blocks the epithelial sodium channel (ENaC) in the distal nephron. This reduces sodium reabsorption and helps lower blood pressure. Detailed mechanism-of-action data is not available in the data compiled for this report, so this description reflects the commonly known pharmacology of the drug.

The original indications (hypertension and heart failure) are closely related to hypertensive renal disease, since sustained high blood pressure damages the kidney. Mechanistically, a drug that controls sodium and volume-dependent hypertension could plausibly help here.

The very high TxGNN score (0.998) is probably driven by the similarity to the existing hypertension indication. It is a computational prediction only. No trials or literature were found for the malignant or renal-injury phenotype, and malignant hypertension is an acute, severe condition that is not typically managed with a mild diuretic like amiloride.

Other predictions in the same set are weaker or equally unsupported:

- **Malignant renovascular hypertension** (score 99.82%): Only one paper was retrieved, a 2003 review on investigating mineralocorticoid hypertension. It does not test amiloride, so the link is indirect. Evidence level L5, Hold.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.81%): Preclinical and mechanistic papers suggest a plausible link. Hypoxia downregulates alveolar sodium channels, and ASIC1 is implicated in hypoxic pulmonary hypertension. No paper shows clinical efficacy of amiloride, and many retrieved papers are off-topic. Evidence level L4, Research Question.
- **Chronic pulmonary heart disease** (score 99.68%): Two small heart-failure studies of amiloride exist, but they address general or left-sided heart failure rather than cor pulmonale. Evidence level L4, Research Question.
- **Pulmonary hypertension with unclear multifactorial mechanism** and **Braddock syndrome**: No trials, literature or clear rationale. Evidence level L5, Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication. The closest supporting papers for the related predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Clinical study (double-blind crossover) | Cardiovasc Drugs Ther | Amiloride improved hemodynamics in 11 patients with chronic heart failure on digoxin and diuretics |
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT | Lancet | Captopril alone vs frusemide plus amiloride in mild heart failure (14 patients); 4 of 14 on captopril alone deteriorated |
| [25398716](https://pubmed.ncbi.nlm.nih.gov/25398716/) | 2015 | Review | Exp Physiol | Smooth muscle ASIC1 is implicated in hypoxic pulmonary hypertension |
| [9376126](https://pubmed.ncbi.nlm.nih.gov/9376126/) | 1997 | Preclinical (cell) | Am J Respir Cell Mol Biol | Hypoxia reduced amiloride-sensitive sodium channel activity in rat alveolar cells |
| [15219007](https://pubmed.ncbi.nlm.nih.gov/15219007/) | 2004 | Observational human physiology | Eur Respir J | High altitude impaired nasal sodium transport in HAPE-prone subjects |
| [16222038](https://pubmed.ncbi.nlm.nih.gov/16222038/) | 2005 | Review | Proc Am Thorac Soc | Effects of hypoxia on alveolar epithelial function |
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Diagnostic work-up of mineralocorticoid hypertension; does not test amiloride |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case report | Am J Med Sci | Severe hyperkalemia (K 9.3 mEq/L) in a geriatric patient on trimethoprim-sulfamethoxazole; a hyperkalemia risk to consider |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA070346 | Amiloride Hydrochloride (Bryant Ranch Prepack) | Tablet | Not available (cancelled) |
| ANDA079133 | Amiloride Hydrochloride (Sigmapharm Laboratories) | Tablet | Not available (cancelled) |
| NDA018200 | Amiloride hydrochloride (Padagis US) | Tablet | Not available (cancelled) |

All three authorizations are cancelled, so amiloride currently has no valid US marketing authorization in the data compiled for this report.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): kidney disease, anuria, diabetic nephropathy, diabetes mellitus, diabetic ketoacidosis, liver disease, hepatic coma and encephalopathy, pancreatitis, gallbladder disease, gout, hyperuricemia, acidosis (including lactic acidosis), potassium deficiency disease, hyperparathyroidism, osteitis fibrosa, systemic lupus erythematosus (including pediatric), pyoureter, and neonatal jaundice. Several of these, especially kidney disease and diabetic nephropathy, overlap with the proposed renal indication and need careful review.
- **Drug Interactions**: 100 interactions were found. Most of those listed are Moderate, including corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), metformin, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, bupropion, dronabinol, and laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose). Minor interactions include doxycycline, amoxicillin and cimetidine.
- **Hyperkalemia risk**: A case report describes severe hyperkalemia with trimethoprim-sulfamethoxazole. This is a general concern for potassium-sparing diuretics, particularly in patients with impaired kidney function.

Please refer to the package insert for official warnings, as label-based warnings were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease rests only on a TxGNN score, with no trials or literature (Evidence Level L5). Amiloride also has no valid US authorization in the compiled data, and the knowledge graph lists kidney disease and diabetic nephropathy as contraindications, which conflicts with a renal indication. Of the related predictions, pulmonary hypertension owing to lung disease/hypoxia and chronic pulmonary heart disease (both L4) are better framed as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical or well-designed preclinical evidence of amiloride in malignant hypertensive renal disease or hypertensive nephropathy
- A kidney-specific safety assessment, particularly for hyperkalemia and use in impaired renal function
- Confirmation of current US regulatory and commercial availability
- If pursuing the pulmonary hypertension direction, targeted preclinical studies of ENaC/ASIC1/NHE1 inhibition in pulmonary vascular models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

