---
layout: default
title: Atrasentan
parent: Model Prediction Only (L5)
nav_order: 427
evidence_level: L5
indication_count: 1
---

# Atrasentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Atrasentan: From an Unrecorded Original Indication to Amenorrhea

## One-Sentence Summary

Atrasentan is marketed in the US as VANRAFIA (a film-coated tablet), but the Evidence Pack does not record its approved indication.
The TxGNN model predicts it may be effective for **amenorrhea**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone and is best treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology (not verified against the supplied data), atrasentan is a selective endothelin A receptor antagonist. Endothelin signaling has been implicated in ovarian and uterine vascular and smooth-muscle physiology, so a mechanistic link is conceivable. This link is speculative.

Several factors weaken the prediction:
- **No supporting path:** The only support is the TxGNN score of 0.996, and no score-derived path was provided for review.
- **Heterogeneous condition:** Amenorrhea is a symptom with many distinct causes (hypothalamic, pituitary, ovarian, uterine, pregnancy). A single drug–disease link is biologically implausible without a defined subtype.
- **Pregnancy risk:** Endothelin receptor antagonists carry embryo-fetal toxicity warnings and require pregnancy exclusion in people of reproductive potential. This complicates any use in amenorrhea.

A high score with no corroborating evidence is more likely a knowledge-graph artifact than a real signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA219208 | VANRAFIA (Novartis Pharmaceuticals Corporation) | Tablet, film coated (oral) | Not provided in source data |

## Safety Considerations

Please refer to the package insert for safety information.

One caution comes from general knowledge of the endothelin receptor antagonist class, not from the Evidence Pack. These drugs carry embryo-fetal toxicity warnings and require pregnancy exclusion before use. This is directly relevant to a condition where pregnancy is one of the causes.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score, with no clinical trials, no literature and no mechanistic path. The drug class's embryo-fetal toxicity warnings also make an amenorrhea indication hard to justify without stronger evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Approved indication and mechanism of action data (via DrugBank)
- The TxGNN score-derived path, to check whether the prediction has any biological basis
- A literature and trial registry search for endothelin antagonists in amenorrhea or related reproductive conditions
- A defined amenorrhea subtype and a plan for pregnancy exclusion and embryo-fetal risk management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

