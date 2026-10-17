---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 817
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isotretinoin: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "ISOTRETINOIN"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

According to the data compiled for this report, isotretinoin is listed with hypertensive disorder and hypertension as its original indications. This listing most likely comes from the knowledge graph and is probably a data artifact, because isotretinoin is a systemic retinoid normally used for severe acne.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (and, with an identical score, malignant hypertensive renal disease). However, **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from knowledge graph indication edges; no approved indication text is available in the US license records) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 10 (1 NDA and 9 ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The only support for this prediction is a high TxGNN score of 0.99, which is a computational prediction from a knowledge graph. No mechanistic rationale can be assessed from the data compiled for this report.

Isotretinoin is a systemic retinoid, and the "hypertension" original indication is likely a data artifact rather than an established use. Retinoids have been studied preclinically for effects on renin-angiotensin signaling and vascular remodeling. These ideas are not supported by the data compiled here and are not a validated link to malignant renovascular hypertension.

The second predicted indication, **malignant hypertensive renal disease**, has the same score (99.01%). This suggests both predictions come from the same graph neighborhood and are not independent. Preclinical work on retinoid signaling in renal fibrosis and glomerular injury could in theory relate to hypertensive kidney damage, but it is unvalidated here.

Isotretinoin is also teratogenic and can affect lipids and, in some patients, blood pressure. These properties raise safety concerns for a cardiovascular or renal indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All 10 US authorizations are cancelled, and none is currently valid. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA218194 | Isotretinoin (Aurobindo Pharma) | Capsule | Not available (cancelled) |
| ANDA211568 | Isotretinoin (Zydus Pharmaceuticals USA) | Capsule | Not available (cancelled) |
| ANDA216633 | Isotretinoin (Zydus Lifesciences) | Capsule | Not available (cancelled) |
| NDA021951 | Isotretinoin (Sun Pharmaceutical) | Capsule | Not available (cancelled) |
| ANDA076135 | Claravis (Teva) | Capsule, liquid filled | Not available (cancelled) |

Five more cancelled authorizations are on record, including ZENATANE (Dr. Reddy's) and products from Amneal and Mayne Pharma.

---

## Cytotoxicity

Isotretinoin is not an antineoplastic drug under the criteria used for this report, so this section is omitted.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (computational associations, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, kidney disease, liver disease, gallbladder disease, pancreatitis, inflammatory bowel disease, osteoporosis (including postmenopausal), systemic lupus erythematosus, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, neutropenia, agranulocytosis, angioedema (several forms, including hereditary), hypotensive disorder, and others.
  - Kidney disease is directly relevant to the predicted renal indication.
- **Drug Interactions**: 98 interactions are recorded. Those with **Major** severity:
  - Doxycycline, minocycline, tetracycline
  - Vitamin A
- Examples of **Moderate** severity interactions: corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), warfarin, dicoumarol, ethanol, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor.
- **Other concerns noted in the evaluation**: teratogenicity, lipid effects, and possible blood pressure effects.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no literature and no mechanism data (L5). The "original indication" of hypertension is probably a data artifact. All US licenses are cancelled, and the safety profile (teratogenicity, lipid effects, and a long list of knowledge-graph contraindications including kidney disease) is unfavorable for a cardiovascular or renal indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Verification of the original indication, to confirm whether hypertension is an artifact
- Preclinical or mechanistic evidence linking retinoid signaling to malignant renovascular hypertension or malignant hypertensive renal disease
- A review of whether the two predictions are independent
- An assessment of the teratogenicity risk management and the practical feasibility of development, given the cancelled market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

