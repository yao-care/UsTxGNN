---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Captopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, hypertensive disorder, diabetic nephropathy"
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Captopril
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

## Captopril: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an ACE inhibitor originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 registered clinical trials** and only **1 publication** (a diagnostic case report), so the support rests almost entirely on computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 5 (all ANDA generic approvals, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, captopril is an ACE inhibitor, and its efficacy in hypertension is established. Mechanistically, it may be applicable to malignant hypertensive renal disease, because the renin-angiotensin system (RAS) plays a central role in malignant hypertension and the associated kidney injury.

The new indication sits very close to the original one. Malignant hypertensive renal disease is a severe form of hypertension-related kidney damage, so this is largely an extension within captopril's existing indication space rather than a true repurposing case. The high score (0.993) is a computational prediction only.

The single retrieved publication does not test treatment. It is a case report on captopril renography, a diagnostic procedure, in a patient with renal cell carcinoma and no renal artery stenosis. It therefore says nothing about therapeutic efficacy.

Other predictions in the same analysis, for context (all rated Hold):
- **Malignant renovascular hypertension** (score 99.28%, Evidence Level L4): RAS activation drives this condition, and captopril inhibits that pathway. Evidence is indirect or consists of old case series and reports, with no controlled data.
- **Pulmonary hypertension, unclear multifactorial mechanism** (score 99.15%, L5): prediction only, with no trials and no literature.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.15%, L5): the retrieved literature is largely off-target, and no study addresses captopril in this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | Positive captopril renography (a diagnostic test) in a patient whose CT showed intact renal arteries but a large chromophobe renal cell carcinoma. Renin-dependent hypertension resolved after nephrectomy. Not a study of therapeutic efficacy. |

For the related prediction **malignant renovascular hypertension**, the literature is also indirect. The most relevant items are a 1984 clinical report on captopril in stable and malignant hypertension ([PMID 6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/)) and a 1979 review of captopril as an ACE inhibitor ([PMID 392136](https://pubmed.ncbi.nlm.nih.gov/392136/)). Most other items concern diagnosis (captopril renography) or causes of hypertension rather than treatment.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212809 | Captopril (Bryant Ranch Prepack) | Tablet | Not stated; licence cancelled |
| ANDA074505 | Captopril (Golden State Medical Supply) | Tablet | Not stated; licence cancelled |
| ANDA074677 | Captopril (Method Pharmaceuticals) | Tablet | Not stated; licence cancelled |
| ANDA074477 | Captopril (Solco Healthcare US) | Tablet | Not stated; licence cancelled |
| ANDA074737 | Captopril (Camber Pharmaceuticals) | Tablet | Not stated; licence cancelled |

All five authorizations are cancelled, and none is currently valid.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label-based safety information.

- **Knowledge-graph contraindication signals** (from a computational knowledge graph, not label text): kidney disease, liver disease, pancreatitis, angioedema (including hereditary and ACE-inhibitor-related forms), systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, aortic stenosis, hypotensive disorder, hyperparathyroidism, hepatic encephalopathy, connective tissue disease, and potassium deficiency, among others.
- **Drug Interactions**: 100 interactions were found in the DDI query. The listed ones are mostly Moderate, including:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - antidiabetic drugs (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide)
  - bupropion, morphine, aspirin, dronabinol
  - Minor interactions: aluminum hydroxide, calcium carbonate
- **Population-specific consideration**: ACE inhibitors carry a known risk of renal function deterioration in bilateral renal artery stenosis, which is relevant to the renovascular predictions. The literature also notes fetal effects of ACE inhibitors.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trials are registered, and the only retrieved publication is a diagnostic case report that does not assess treatment. The indication is also very close to captopril's existing uses, so it is not a clear new-use opportunity. In addition, all US licences are cancelled, and label safety data is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Controlled or observational clinical data on captopril treating malignant hypertensive renal disease or malignant renovascular hypertension
- A review of the renal safety risks (especially bilateral renal artery stenosis) and of the knowledge-graph contraindications in the target population
- Confirmation of current US marketing availability, given that all licences are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

