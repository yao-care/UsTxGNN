---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Benazepril
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **0 clinical trials** and **0 relevant publications** currently support this direction, so the prediction rests on a computational score and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 (no clinical trials or literature; indirect, class-level mechanistic support only) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 4 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, benazepril belongs to the ACE inhibitor class. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension.

Malignant renovascular hypertension is driven by marked activation of the renin-angiotensin system. ACE inhibition therefore makes mechanistic sense, since it reduces angiotensin II formation and lowers blood pressure.

There is an important safety concern. ACE inhibitors are known to risk precipitating acute renal failure in patients with bilateral renal artery stenosis or stenosis in a solitary kidney, which is the population at issue here. The high TxGNN score is a computational prediction only and is not a substitute for clinical evidence.

**Other predicted indications (for reference):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 99.65% | L4 | Research Question |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.60% | L5 | Hold |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.60% | L5 | Hold |
| 5 | Braddock syndrome | 99.44% | L5 | Hold |

Malignant hypertensive renal disease is a close extension of the approved indication, because ACE inhibitors lower blood pressure and intraglomerular pressure and reduce proteinuria. The pulmonary hypertension predictions are speculative, as ACE inhibitors are not an established treatment there and hypotension is a concern. For Braddock syndrome, no mechanistic link could be established from the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

(For the rank 4 prediction, three publications were retrieved, but they concern traditional Chinese medicine formulations in renal and cardiac fibrosis models. They do not study benazepril or pulmonary hypertension and were judged not relevant.)

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA076118 | Benazepril Hydrochloride (PD-Rx Pharmaceuticals) | Tablet, coated | Cancelled |
| ANDA076820 | Benazepril Hydrochloride (Bryant Ranch Prepack) | Tablet | Cancelled |
| ANDA078212 | Benazepril Hydrochloride (Preferred Pharmaceuticals) | Tablet, film coated | Cancelled |
| ANDA076267 | Benazepril Hydrochloride (Chartwell RX) | Tablet | Cancelled |

All four licenses are oral single-ingredient products and all are cancelled. No approved indication text was recorded for them.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** Liver failure, kidney disease, pancreatitis, liver disease, gallbladder disease, angioedema (including hereditary, acquired, and RAAS-blocker-induced forms), systemic lupus erythematosus, potassium deficiency disease, diabetes mellitus and diabetic ketoacidosis, neutropenia, agranulocytosis, hypotensive disorder, hyperparathyroidism, hepatic coma and encephalopathy, connective tissue disease, neonatal jaundice, and anuria.
- **Drug Interactions:** 100 interactions were found, and the main ones listed are all moderate. They are mostly with glucose-lowering agents, including insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), alogliptin, dapagliflozin, and exenatide. Hydrocortisone and glycerin are also listed.
- **Setting-specific concern:** In renovascular disease, ACE inhibition carries a risk of acute renal failure, so renal function and potassium would need close monitoring.

Please refer to the package insert for the full warnings, since label-based warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but has no supporting trials or literature, and the renal safety risk in renovascular stenosis is significant. All US licenses are also cancelled, which limits near-term development.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Targeted literature and trial searches for ACE inhibitors in malignant renovascular hypertension and malignant hypertensive nephrosclerosis
- A renal safety assessment for patients with bilateral renal artery stenosis or a solitary kidney
- Expert review of the lower-ranked predictions, especially Braddock syndrome, before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

