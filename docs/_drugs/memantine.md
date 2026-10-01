---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 897
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Memantine: From Alzheimer's Disease to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist that is marketed in the US as many generic products.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **0 clinical trials** and **2 publications** that give no direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease dementia (from general drug knowledge; the approved-indication text is blank in the US license records) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed products shown below are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, memantine is an NMDA receptor antagonist. Its efficacy in its original indication is established, and NMDA receptor signaling is the only mechanistic link to pulmonary hypertension.

The retrieved literature does not support that link. One preclinical study connects the glutamate/NMDA receptor axis to insulin sensitivity and lipid metabolism. It mentions pulmonary arterial hypertension only in passing, as background. No retrieved evidence connects memantine to pulmonary vascular remodeling or pulmonary arterial pressure.

The high TxGNN score (99.54%) therefore reflects knowledge-graph patterns, not clinical or mechanistic evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/mechanistic study | Theranostics | NMDA receptor activation regulates insulin sensitivity and lipid metabolism. Pulmonary arterial hypertension is mentioned only as background for the glutamate/NMDAR axis. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 pharmacokinetic study | Clin Drug Investig | Safety, tolerability and pharmacokinetics of MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension, in healthy Chinese volunteers. This is a different compound, not memantine, and healthy volunteers only, so it is not efficacy evidence. |

## US Market Information

The 5 main authorizations are listed below. Approved-indication text is not provided in the license records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA213985 | Memantine Hydrochloride | Extended-release capsule | Vitruvias Therapeutics, Inc. |
| ANDA202840 | Memantine Hydrochloride | Tablet | Macleods Pharmaceuticals Limited |
| ANDA200022 | Memantine Hydrochloride | Film-coated tablet | Unichem Pharmaceuticals (USA), Inc. |
| ANDA200891 | Memantine Hydrochloride | Coated tablet | Alembic Pharmaceuticals Inc. |
| ANDA203293 | Memantine hydrochloride | Extended-release capsule | Zydus Lifesciences Limited |

Available forms include oral capsules and tablets, plus a solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no plausible mechanism in the retrieved evidence, and only preclinical and unrelated-compound literature. A high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a documented link between NMDA receptor antagonism and pulmonary vascular disease
- Preclinical evidence in pulmonary hypertension models, such as pulmonary pressure or vascular remodeling
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Approved-indication text for the US licenses, to confirm the original indication

**Note on other predictions in this pack:** Migraine disorder (TxGNN score 99.52%) has much stronger support and is rated L1. It has a completed Phase 3 trial ([NCT04698525](https://clinicaltrials.gov/study/NCT04698525), memantine vs sodium valproate, n=33), plus meta-analyses and systematic reviews of RCTs. The trials are small and the evidence is still described as limited, so the pack rates it a "Research Question" pending larger placebo-controlled trials. It may be a better lead for follow-up than pulmonary hypertension.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

