---
layout: default
title: Thyrotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 1225
evidence_level: L5
indication_count: 9
monitor_inn: "THYROTROPIN ALFA"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
last_modified_at: 2026-10-14
description: "Thyrotropin Alfa: predicted new indication Migraine disorder (evidence level L5). Approved use: Not specified in the data compiled for this report (the product is kn…"
---

# Thyrotropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Thyrotropin Alfa: From Thyroid Cancer Diagnostic Support to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Thyrotropin alfa is recombinant human thyroid-stimulating hormone (TSH), used as a diagnostic and adjunctive agent in thyroid cancer management.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and **no publications** currently support this direction.
The prediction is a computational output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report (the product is known as a thyroid cancer diagnostic and adjunctive agent) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, thyrotropin alfa is recombinant human TSH. It binds the TSH receptor on thyroid cells and is used to stimulate thyroid tissue during thyroid cancer diagnosis and radioiodine ablation.

**A plausible mechanism for migraine has not been established.** The high score (0.9998) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no known link between TSH receptor signaling and migraine pathophysiology, and no trials or literature were found to support one.

The other top predictions show the same pattern. One more is a migraine-related term (migraine with brainstem aura), which looks like a redundant result from similarities the TxGNN model (deep learning) learned between related diseases. Others are Raynaud disease, pulmonary hypertension, rare skin disorders and hyperthyroidism, none with supporting evidence. Some are of concern:
- **Hyperthyroidism**: Biologically implausible and likely contraindicated, since TSH stimulates thyroid hormone production.
- **Postural orthostatic tachycardia syndrome and pulmonary hypertension**: Transient increases in thyroid hormone could worsen tachycardia or cardiovascular stress, so the direction of effect may be unfavorable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA020898 (Cancelled) | Thyrogen (Genzyme Corporation) | Injection, powder, lyophilized, for solution | Not available in the compiled data |

---

## Safety Considerations

**Drug Interactions**: The interaction screen identified 45 potential interactions, all of Moderate severity among those listed. They are concentrated in glucose-lowering agents, including:
- Metformin, acarbose, glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide
- DPP-4 inhibitors and SGLT2 inhibitors (alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
- GLP-1 receptor agonists (albiglutide, dulaglutide, exenatide, semaglutide)
- Insulins (human, aspart, aspart protamine)

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, with no clinical trials, no literature and no plausible mechanistic link to migraine. The drug is marketed in the US, with 1 valid license of 1, and the package insert safety data has not yet been obtained.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A mechanistic hypothesis connecting TSH receptor signaling to migraine, followed by a literature and preclinical review
- Clarification of the current regulatory status of the cancelled BLA and its original approved indication
- Route compatibility assessment for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

