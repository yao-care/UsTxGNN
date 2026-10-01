---
layout: default
title: Landiolol
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 6
---

# Landiolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Landiolol: From Rapid Heart-Rate Control to Lingual-Facial-Buccal Dyskinesia

## One-Sentence Summary

Landiolol is an ultra-short-acting intravenous beta-1 selective blocker, marketed in the US as RAPIBLYK. The TxGNN model predicts it may be effective for **lingual-facial-buccal dyskinesia**, but **0 clinical trials** and **0 publications** support this, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (the class is IV beta-blockers for rapid heart-rate control) |
| Predicted New Indication | Lingual-facial-buccal dyskinesia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license entries (both under NDA217202, from two manufacturers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology, landiolol is a hydrophilic, beta-1 selective adrenergic blocker given intravenously. It has an ultra-short duration of action and limited CNS penetration.

The prediction is weakly supported. Lipophilic, non-selective beta-blockers such as propranolol have been reported for tardive and orofacial dyskinesia, which may explain the high graph score. Landiolol differs from them in selectivity, lipophilicity and route. Because its mechanism is undocumented in the record, the score cannot be checked against a known mechanism.

The other predictions (chronic tic disorder, psychogenic movement disorders, extrapyramidal and movement disease, benign shuddering attacks, primary orthostatic tremor) all score 0.990–0.991 and share the same weaknesses. All have L5 evidence, and none has trial or literature support. Several of these conditions are chronic, oral-treatment, non-drug-managed or self-limited, which fits poorly with an IV-only, short-acting agent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA217202 | RAPIBLYK (AOP Orphan Pharmaceuticals GmbH) | Injection, powder, lyophilized, for solution | Not listed in the source record |
| NDA217202 | RAPIBLYK (AOP Health US, LLC) | Injection, powder, lyophilized, for solution | Not listed in the source record |

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records (0 interactions found). This is not evidence of no interactions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trial or literature evidence (L5). It has a weak mechanistic rationale, since landiolol is IV-only, short-acting, beta-1 selective and peripherally restricted. The proposed conditions are mostly chronic or non-pharmacologically managed.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A literature and trial search for beta-blockers in dyskinesia and tic disorders, to test the class-level link
- An assessment of route compatibility (IV-only versus chronic or oral needs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

