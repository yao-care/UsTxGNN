---
layout: default
title: Triheptanoin
parent: Model Prediction Only (L5)
nav_order: 1262
evidence_level: L5
indication_count: 10
monitor_inn: "TRIHEPTANOIN"
predicted_indications: ["tetanic cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "craniostenosis cataract", "immature cataract", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "antithrombin deficiency type 2"]
last_modified_at: 2026-10-14
description: "Triheptanoin: predicted new indication Tetanic cataract (evidence level L5). Approved use: Not available"
---

# Triheptanoin
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

# Triheptanoin: From an Unspecified Original Indication to Tetanic Cataract

## One-Sentence Summary

Triheptanoin is a synthetic triglyceride of heptanoate (a seven-carbon fatty acid). It was marketed in the US as DOJOLVI, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **tetanic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text is empty in the US license record) |
| Predicted New Indication | Tetanic cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of its chemistry, triheptanoin is a triglyceride of heptanoate (C7). It is thought to supply anaplerotic substrates, such as propionyl-CoA and succinyl-CoA, to the TCA cycle, which supports cellular energy metabolism.

The link to the predicted indication is speculative. Tetanic cataract is a lens opacity associated with low blood calcium. No connection between triheptanoin's metabolic action and calcium-related lens changes has been identified, and no trial or publication tests it.

The same score (99.98%) is shared by many other cataract subtypes, including diabetic, mature, immature, cortical and senile cataract. This pattern suggests the prediction may reflect the structure of the knowledge graph rather than a disease-specific signal. Other top-ranked predictions, such as type 2 antithrombin deficiency, also lack any plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213687 (cancelled) | DOJOLVI (Ultragenyx Pharmaceutical Inc.) | Liquid | Not listed in the available data |

## Safety Considerations

- **Drug Interactions**: One interaction is recorded in the DDInter database. **Orlistat** carries a **Major** interaction level with triheptanoin. Orlistat reduces dietary fat absorption, so this pairing should be avoided or reviewed carefully.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for tetanic cataract is supported only by a model score, with no clinical trials, literature or plausible mechanism. The US license is also cancelled, and the key safety labeling is missing. The evidence level is L5.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking anaplerotic metabolism to lens physiology or calcium-related cataract
- Route and formulation feasibility for an ocular or systemic indication, which has not been assessed
- Review of the other top-ranked predictions, since their scores are essentially identical and none has supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

