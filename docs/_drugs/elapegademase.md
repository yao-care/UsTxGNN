---
layout: default
title: Elapegademase
parent: Model Prediction Only (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
monitor_inn: "ELAPEGADEMASE"
predicted_indications: ["diabetic retinopathy", "diabetic cataract", "severe nonproliferative diabetic retinopathy", "cortical cataract", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "tetanic cataract", "immature cataract", "craniostenosis cataract"]
last_modified_at: 2026-10-14
description: "Elapegademase: predicted new indication Diabetic retinopathy (evidence level L5). Approved use: Not stated in the US license data (the product is known as an ADA enz…"
---

# Elapegademase
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

## Elapegademase: From ADA-SCID Enzyme Replacement to Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Elapegademase (brand name Revcovi) is a PEGylated adenosine deaminase (ADA) enzyme replacement therapy, originally used for ADA-deficient severe combined immunodeficiency (ADA-SCID).
The TxGNN model predicts it may be effective for **diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data (the product is known as an ADA enzyme replacement therapy for ADA-SCID) |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, elapegademase is a PEGylated form of the ADA enzyme. It replaces the missing enzyme in ADA-SCID, so it works systemically on purine metabolism.

No clear mechanistic link to diabetic retinopathy has been established. The high TxGNN score may reflect network proximity through purine metabolism or adenosine signaling, which has been loosely studied in retinal vascular biology. This is speculation and cannot be checked against known pharmacology without MOA data.

The other top-ranked predictions are also eye diseases: diabetic cataract, severe nonproliferative diabetic retinopathy, and several cataract types (cortical, nuclear senile, mature, immature, tetanic, craniostenosis, and type 2 diabetes-associated). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Cataract formation is driven mainly by polyol pathway activation and oxidative stress, and elapegademase has no known lens-targeted activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761092 | Revcovi (Chiesi USA, Inc.) | Injection | Not stated in the data compiled for this report (status: valid) |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for this drug, and no contraindication edges linking it to specific diseases were found in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no clinical trials, no publications, and no verified mechanism linking ADA enzyme replacement to diabetic retinopathy or cataract. The US license is also listed as cancelled, and package insert safety data are missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank, to test any link to adenosine or purine signaling in retinal tissue
- Preclinical evidence (for example retinal or diabetic models) showing a plausible effect of ADA replacement
- Clarification of the current US regulatory status and original approved indication
- Assessment of route compatibility, since the drug is a systemic injection and ocular delivery would need to be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

