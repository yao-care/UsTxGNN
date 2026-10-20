---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 1258
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Triamterene: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, congestive heart failure"
monitor_inn: "TRIAMTERENE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Triamterene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Triamterene: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no supporting publications** are currently available for this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure (the approved-indication text in the US license records is empty; this comes from the knowledge-graph indication data) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (1 NDA, 2 ANDAs; all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron. It is already used for hypertension and heart failure, and mechanistically it may contribute to blood pressure and volume control in hypertensive kidney disease.

The link between the original and predicted indications is plausible but weak. Malignant hypertension is a medical emergency that generally needs rapid, titratable parenteral therapy, so an oral diuretic is unlikely to be suitable as primary treatment. Reduced kidney function also raises the risk of hyperkalaemia with a potassium-sparing agent. The high TxGNN score likely reflects network proximity to hypertension-related terms rather than direct evidence.

Other predictions in the same list are weaker or only indirectly supported:
- **Malignant renovascular hypertension** (score 99.89%): driven mainly by renin-angiotensin-aldosterone system activation, where a potassium-sparing diuretic may add little and carries hyperkalaemia risk, especially with ACE inhibitors or ARBs.
- **Pulmonary hypertension (lung disease/hypoxia-related, and unclear multifactorial)** (99.88%): any benefit would be limited to symptomatic volume management.
- **Braddock syndrome** (99.84%): no clear mechanistic rationale; likely knowledge-graph noise.
- **Chronic pulmonary heart disease** (99.75%): the most plausible secondary candidate, because diuretics are standard supportive therapy for right-heart failure with fluid retention (Evidence Level L4, "Research Question"). The support is indirect, since the papers cover heart failure generally.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication, malignant hypertensive renal disease.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the related candidate chronic pulmonary heart disease, two indirect publications were retrieved:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Clinical study (hemodynamic) | Fortschritte der Medizin | In 12 patients with chronic heart failure (NYHA II-III), a fixed combination of verapamil, triamterene and hydrochlorothiazide over 4 weeks lowered blood pressure (145/93 to 133/86 mmHg) and heart rate (79 to 75 bpm) |
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Review (as classified) | Deutsche medizinische Wochenschrift | 16 heart-failure patients were randomised in a crossover between hydrochlorothiazide + triamterene and a digitalis glycoside; the abstract was truncated, so outcomes are not fully available |

These studies concern heart failure in general, not cor pulmonale or triamterene alone, so they are indirect evidence only.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA013174 | Triamterene (Prasco Laboratories) | Capsule | Not stated in the available data (cancelled) |
| ANDA211581 | Triamterene (Bryant Ranch Prepack) | Capsule | Not stated in the available data (cancelled) |
| ANDA214768 | Triamterene (Biocon Pharma Inc.) | Capsule | Not stated in the available data (cancelled) |

All three authorizations are single-ingredient oral capsules and all are cancelled.

## Safety Considerations

**Contraindications (from knowledge-graph drug-disease contraindication links, not package-insert text):**
- Kidney and urinary: kidney disease, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- Liver and biliary: liver disease, liver failure, hepatic coma/encephalopathy, gallbladder disease, pancreatitis
- Metabolic: type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, acidosis disorders, acquired lactic acidosis, hyperuricaemia, gout, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease
- Other: systemic lupus erythematosus (including paediatric), folic acid deficiency anaemia, neonatal jaundice

**Drug Interactions** (100 interactions were found; the first 20 reviewed are summarised here):
- **Major**: potassium citrate (risk of hyperkalaemia)
- **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), metformin, bupropion, morphine, bisacodyl, canagliflozin, dapagliflozin, dronabinol, picosulfuric acid, polyethylene glycol with electrolytes
- **Minor**: famotidine, ranitidine, cimetidine, doxycycline, minocycline

Package-insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information. Hyperkalaemia and renal risk deserve particular attention in any hypertensive kidney disease setting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). There are no clinical trials or relevant literature. The clinical setting (malignant hypertension with kidney involvement) needs rapid parenteral therapy and carries a high hyperkalaemia risk with a potassium-sparing diuretic. The drug also has no currently valid US licenses.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or observational evidence directly linking triamterene to hypertensive kidney disease
- A clinical rationale for oral use in this setting, plus a hyperkalaemia and renal function monitoring plan
- Consideration of chronic pulmonary heart disease as a more plausible, lower-priority research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

