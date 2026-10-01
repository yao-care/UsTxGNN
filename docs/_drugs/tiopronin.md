---
layout: default
title: Tiopronin
parent: Model Prediction Only (L5)
nav_order: 1231
evidence_level: L5
indication_count: 10
---

# Tiopronin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tiopronin: From Cystinuria to Renal Tubular Acidosis

## One-Sentence Summary

Tiopronin is a thiol drug that binds cystine in the urine, and its established use is cystinuria (a kidney cystine-transporter defect). The TxGNN model predicts it may be effective for **Renal Tubular Acidosis** with a very high score, but **0 clinical trials** and **0 publications** support this direction. The prediction is likely a network-proximity artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystinuria (not stated in the US license records; the approved indication text is empty) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 authorizations in total (a mix of NDA and ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Tiopronin is a thiol that forms soluble mixed disulfides with cystine, which keeps cystine from crystallizing into stones. This is the basis of its established use in cystinuria.

Renal tubular acidosis is a defect in how the kidney handles acid and bicarbonate. It is not a problem of cystine solubility. The two conditions both involve the kidney, but there is no clear mechanistic link. The high TxGNN score most likely reflects closeness in the knowledge graph rather than a real pharmacological rationale. No trials or literature were supplied to support the prediction.

The other nine top-ranked predictions have the same limitation. They include glycogen branching enzyme deficiency subtypes, tricarboxylic acid cycle disorder and pyruvate metabolism disorder, and none has a plausible mechanism for tiopronin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Tiopronin is marketed in the US as oral delayed-release tablets. The record does not list an approved indication text for any of these authorizations. The table shows 5 distinct authorizations from the 15 on record.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216456 | Tiopronin | Tablet, delayed release | Teva Pharmaceuticals, Inc. |
| ANDA217219 | Tiopronin | Tablet, delayed release | Endo USA, Inc. |
| ANDA216990 | VENXXIVA | Tablet, delayed release | Cycle Pharmaceuticals Ltd. |
| NDA211843 | Tiopronin | Tablet, delayed release | BioComp Pharma, Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials or literature, and the mechanism does not connect a cystine-binding thiol to an acid-base transport defect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- A literature and trial search specific to tiopronin in renal tubular acidosis
- A mechanistic hypothesis that explains the link, if the search finds any signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

