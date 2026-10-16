---
layout: default
title: Candesartan Cilexetil
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 5
monitor_inn: "CANDESARTAN CILEXETIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil was originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 directly relevant publications** supporting this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 6 listings cancelled) |
| Number of NDAs | 6 listings (1 NDA, 5 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known class information, candesartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertension damages the kidney through severe blood pressure elevation, renal vascular injury, and glomerular hypertension. Blocking AT1 receptors could plausibly reduce this injury. The indication is closely related to the original one, since both involve blood pressure control.

This link is a model-based prediction only. The TxGNN score is high, but no trials or literature were found to confirm it directly.

Other predicted indications from the model (all also at evidence level L5, all Hold):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.68% | Mechanistically coherent (renin-angiotensin system), but ARBs can precipitate acute renal failure in bilateral renal artery stenosis or a solitary kidney |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.67% | Speculative link from preclinical angiotensin II remodeling data; the heterogeneous indication makes this uncertain |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | Plausible but indirect; retrieved papers do not support it directly |
| 5 | Braddock syndrome | 99.56% | No mechanistic link can be established from the available data |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication (malignant hypertensive renal disease). Two papers were retrieved for the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), and neither supports it directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Preclinical (mouse) | Front Immunol | Candesartan cilexetil, an anti-inflammatory compound, improved neurological outcomes in a mouse model of neonatal hypoxia; not a pulmonary hypertension study |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Preclinical (rat) | Evid Based Complement Alternat Med | Hachimijiogan (a Kampo herbal formula) was compared with an angiotensin II receptor blocker in a remnant kidney model, with a focus on HIF-1α; does not study candesartan in pulmonary hypertension |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020838 | Candesartan cilexetil (Golden State Medical Supply) | Tablet | Not available; cancelled |
| ANDA210302 | Candesartan cilexetil (Alembic Pharmaceuticals Inc.) | Tablet | Not available; cancelled |
| ANDA209119 | Candesartan cilexetil (Alembic Pharmaceuticals Limited) | Tablet | Not available; cancelled |
| ANDA078702 | Candesartan cilexetil (Mylan Pharmaceuticals) | Tablet | Not available; cancelled |
| ANDA203813 | Candesartan (Macleods Pharmaceuticals) | Tablet | Not available; cancelled |

One further listing (ANDA091390, Zydus Lifesciences) is also cancelled. All 6 US listings are cancelled, and there are no currently valid single-ingredient or combination authorizations in the data compiled for this report.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. The following is drawn from the knowledge graph's drug-disease contraindication links, not from label text, and should be verified against the official label:

- **Conditions flagged in the knowledge graph:** pancreatitis, liver disease, gallbladder disease, hepatic coma/encephalopathy, systemic lupus erythematosus (including pediatric), diabetes mellitus, diabetic ketoacidosis, gout, hyperuricemia, hypotensive disorder, potassium deficiency, hypercalcemia, hyperparathyroidism, osteitis fibrosa, nephrocalcinosis, phosphorus metabolism disorders, neonatal jaundice, anuria, renal artery obstruction, and impaired renal function.
- **Relevance to the predicted indications:** Renal artery obstruction and impaired renal function are flagged, which matters directly for malignant hypertensive renal disease and renovascular hypertension. Angiotensin receptor blockers can precipitate acute renal failure in bilateral renal artery stenosis or a solitary kidney.
- **Drug interactions:** No interaction data were found.

Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a plausible class mechanism (AT1 blockade). There are no clinical trials and no directly relevant literature, so the evidence level is L5. Renal contraindication signals add a safety concern for the renal-related indications. All US listings are also cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label (currently a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- A targeted literature search on ARBs in malignant hypertension with renal involvement
- A review of renal safety in patients with renal artery stenosis, a solitary kidney, or impaired renal function
- Clarification of current US market status, since all listings are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

