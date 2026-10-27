---
layout: default
title: Nitisinone
parent: Model Prediction Only (L5)
nav_order: 969
evidence_level: L5
indication_count: 10
monitor_inn: "NITISINONE"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
last_modified_at: 2026-10-14
description: "Nitisinone: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Tyrosinemia"
---

# Nitisinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Nitisinone: From Tyrosinemia to Renal Tubular Acidosis
{: .text-alpha }

## One-Sentence Summary

Nitisinone is an HPPD inhibitor originally used to treat hereditary tyrosinemia.
The TxGNN model predicts it may be effective for **renal tubular acidosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tyrosinemia |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (all cancelled; includes NDA and ANDA entries) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), blocking tyrosine breakdown upstream of toxic metabolites such as fumarylacetoacetate and succinylacetone. This is how it treats hereditary tyrosinemia type 1.

Proximal renal tubular dysfunction (Fanconi-type) is a recognized feature of hereditary tyrosinemia type 1. This gives a plausible link between the original indication and renal tubular acidosis, because the kidney problem may arise through the underlying disease. However, no independent evidence supports nitisinone for renal tubular acidosis of other causes. The very high TxGNN score is a model output only and does not by itself show clinical benefit.

The data compiled for this report did not include a detailed mechanism-of-action entry from DrugBank, so the mechanistic discussion above relies on general pharmacological knowledge.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for renal tubular acidosis.

For context, the second-ranked prediction (galactosemia) and the fifth-ranked prediction (glycogen storage disease) are supported only by general reviews of pediatric inborn errors of metabolism with liver involvement. These reviews discuss the diseases together but do not report nitisinone use in them. The remaining top-10 predictions have no trials or literature and show no clear mechanistic link.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209449 | NITYR | Tablet | Not specified (status: cancelled) |
| NDA021232 | Orfadin | Capsule | Not specified (status: cancelled) |
| ANDA216201 | Nitisinone (Eton Pharmaceuticals) | Capsule | Not specified (status: cancelled) |
| ANDA211041 | Nitisinone (Endo USA) | Capsule | Not specified (status: cancelled) |
| NDA206356 | ORFADIN | Suspension | Not specified (status: cancelled) |

A sixth entry, ANDA212390 (Nitisinone, Analog Pharma, capsule), is also cancelled.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not from label text): kidney disease, pyoureter, thrombocytopenia, leukopenia, hypophosphatemia, and tyrosinemia. These should be verified against the official label. The kidney-related signal deserves particular attention given the predicted renal indication.
- **Drug Interactions**: 100 interactions were found in total. The sample reviewed was mostly Moderate, with one Minor. Notable moderate-level interacting drugs include:
  - Amiodarone
  - Amlodipine
  - Nifedipine
  - Ibuprofen
  - Dexamethasone
  - Pioglitazone
  - Isotretinoin
  - Abiraterone
  - Atazanavir
  - Apalutamide
  - Bicalutamide
  - Baricitinib
  - Aprepitant

  Minor: Armodafinil.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for renal tubular acidosis has a high model score but no clinical trials or publications. The mechanistic link is indirect (through Fanconi-type tubular dysfunction in tyrosinemia type 1). All six US licenses are cancelled, and knowledge-graph signals flag kidney disease as a contraindication.

**To proceed, the following is needed:**
- Retrieve and review the current FDA package insert (warnings and contraindications)
- Confirm the mechanism of action from DrugBank
- Literature search and preclinical or case-level evidence for nitisinone in renal tubular acidosis, separating tyrosinemia-related tubulopathy from other causes
- Clarify the regulatory and market status, since all listed US licenses are cancelled
- Review the kidney-disease contraindication signal and assess a safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

