---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cholecalciferol: From Vitamin D3 Supplementation to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Cholecalciferol (vitamin D3) is marketed in the US in several products, including a combination tablet with alendronate. The record contains no approved-indication text.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty in all US license records) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 licenses (only 1 carries an NDA number: NDA021762) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cholecalciferol is a vitamin D3 form, and its role in calcium and phosphate homeostasis is well known. It is mechanistically related to a disease defined by low PTH and hypocalcemia.

Vitamin D metabolites are used clinically to manage hypocalcemia in hypoparathyroidism. This is symptomatic calcium homeostasis support, not disease modification. Cholecalciferol has a specific limitation here. It must be activated by PTH-dependent renal 1-alpha-hydroxylation, which is impaired when PTH secretion is deficient. Active analogs are therefore usually preferred.

The high TxGNN score reflects proximity in the knowledge graph. It is not evidence of benefit. No trials or literature were retrieved for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The Evidence Pack lists 6 licenses. One product (Fosamax Plus D, NDA021762) appears twice, so 4 distinct products are shown. Only NDA021762 has an authorization number.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021762 | FOSAMAX PLUS D (Organon LLC) | Tablet | Not provided |
| Not listed | GROWTH SUPPORTPATCH, HAUTUKI (CUSTICS) | Patch | Not provided |
| Not listed | Floriva (BonGeo Pharmaceuticals, Inc.) | Liquid | Not provided |
| Not listed | Folvitra (Blue Heron Pharmaceuticals, LLC) | Tablet | Not provided |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature for this indication. Cholecalciferol also has a mechanistic limitation in PTH deficiency, where active vitamin D analogs are normally used. Safety data are missing, and the package insert gap is flagged as blocking.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking data gap)
- Mechanism of action data (for example, from DrugBank)
- A targeted literature search for cholecalciferol versus active vitamin D analogs in hypoparathyroidism
- Approved-indication text for the US products, to confirm the original indication

Other candidates in the same Evidence Pack have more supporting evidence. Renal osteodystrophy (L3) includes NCT00285467, a completed trial comparing cholecalciferol with doxercalciferol. Hypophosphatemic rickets is L4. These are worth evaluating separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

