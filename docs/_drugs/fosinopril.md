---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosinopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Fosinopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fosinopril is an ACE inhibitor, its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-driven renal disease.

Malignant hypertensive renal disease is a severe kidney complication of very high blood pressure, and activation of the renin-angiotensin-aldosterone system (RAAS) plays a central role. Blocking this pathway with an ACE inhibitor is therefore biologically plausible.

However, this is better viewed as an extension of the original indication to a more severe form of the same disease than as true repurposing. The only support is the high model score; no trials or publications were found.

Other predicted indications in the data (all L5, all Hold):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.87% | RAAS-driven, so plausible. In bilateral renal artery stenosis or a solitary kidney, ACE inhibitors can precipitate acute renal failure, a significant safety concern. |
| 3 | Pulmonary hypertension, unclear multifactorial mechanism | 99.87% | Only an indirect link; ACE inhibitors have generally not shown clear benefit in pulmonary hypertension. |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.87% | Theoretical rationale only; the retrieved literature does not support efficacy and includes an adverse-event signal. |
| 5 | Braddock syndrome | 99.81% | No plausible mechanistic link is evident; likely a knowledge-graph artifact. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked indication. For the rank 4 indication (pulmonary hypertension owing to lung disease and/or hypoxia), two publications were retrieved, and neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report (adverse event) | Revue des maladies respiratoires | Two patients treated with enalapril and fosinopril for hypertension developed hypoxic eosinophilic pneumonia with sub-acute respiratory failure; improvement followed. This is a safety signal, not evidence of benefit. |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinical (bioinformatics) | Experimental and therapeutic medicine | Gene-expression analysis of mouse mesangial cells in a diabetic nephropathy context; not relevant to pulmonary hypertension. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077222 (Cipla USA Inc.) | Fosinopril Sodium | Tablet | Not listed (cancelled) |
| ANDA091163 (Aurobindo Pharma Limited) | Fosinopril Sodium | Tablet | Not listed (cancelled) |
| ANDA205670 (Bryant Ranch Prepack) | Fosinopril sodium | Tablet | Not listed (cancelled) |
| ANDA076483 (Chartwell RX, LLC) | Fosinopril Sodium | Tablet | Not listed (cancelled) |

All four authorizations are single-ingredient oral tablets and all are cancelled.

## Safety Considerations

**Contraindications / conditions of concern (from a knowledge graph, not label text):**
- Kidney disease, liver disease, hepatic coma/encephalopathy
- Pancreatitis, gallbladder disease
- Angioedema (including hereditary, acquired, and RAAS-blocker-induced forms)
- Systemic lupus erythematosus and other connective tissue disease
- Diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Neutropenia, agranulocytosis
- Aortic stenosis and related aortic valve disease
- Hypotensive disorder
- Hyperparathyroidism, osteitis fibrosa, bone disease

**Drug Interactions:** 100 interactions were found; the first 20 retrieved are summarized here.
- **Major:** Potassium bicarbonate, potassium citrate (risk of hyperkalaemia).
- **Moderate:** Corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone, dexamethasone); antidiabetic agents (alogliptin, saxagliptin, metformin, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin); acetylsalicylic acid; bupropion; morphine; dronabinol; bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes).

**Additional concern:** Renovascular disease carries a risk of acute renal failure with ACE inhibition, and a case-report signal of hypoxic eosinophilic pneumonia exists.

Package insert warnings and contraindications were not available. Please refer to the package insert for the official safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (99.87%), with no clinical trials or literature. It is largely an extension of the existing hypertension indication, and there are no currently valid US licenses. Safety review cannot proceed without the package insert.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence for ACE inhibitors in malignant hypertensive nephropathy
- Review of renal safety, especially in renovascular disease
- Clarification of the regulatory status, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

