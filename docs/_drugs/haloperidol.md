---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Antipsychotic Use to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is a dopamine D2 receptor antagonist antipsychotic with 20 US generic authorizations.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**, but this rests on a model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed entries are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Haloperidol is a dopamine D2 receptor antagonist, and its known use is in psychiatric conditions.

Congenital disorder of glycosylation with defective fucosylation is an inherited defect in glycan synthesis. No plausible mechanistic link to D2 antagonism was identified. The high TxGNN score (99.91%, model rank 2958) reflects the model's prediction only, and nothing supports it in trials or literature. It should be treated as a low-confidence signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216004 | Haloperidol | Tablet | Novadoz Pharmaceuticals LLC |
| ANDA070278 | Haloperidol | Tablet | Mylan Pharmaceuticals Inc. |
| ANDA218789 | Haloperidol | Tablet | Coupler LLC |
| ANDA074893 | Haloperidol Decanoate | Injection | Fresenius Kabi USA, LLC |

The record contains no approved-indication text for these products. Only the first five of the 20 authorizations were provided, and one of them (ANDA216004) appeared twice, so it is shown once here. Routes available are oral (tablet) and injectable.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link, so it is a model output only (L5, stage S0).

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, plus a check of the record's original indication (empty in the record)
- Any preclinical or mechanistic evidence linking haloperidol to fucosylation or glycosylation pathways

**Note on other candidates:** Among the lower-ranked predictions, *manic bipolar affective disorder* (rank 10) has L1 evidence, including several completed Phase 3 RCTs with haloperidol arms and a network meta-analysis. It appears to be an established or off-label use rather than a novel repurposing finding. Its label status should be confirmed first. If it proceeds, guardrails apply for extrapyramidal symptoms, QT prolongation and tardive dyskinesia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

