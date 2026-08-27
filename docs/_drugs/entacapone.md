---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a peripheral COMT inhibitor originally used as an adjunct to levodopa/carbidopa therapy for Parkinson's disease. The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**, but this is currently a pure model prediction with **0 clinical trials** and **0 publications** supporting the link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease (adjunctive therapy with levodopa/carbidopa) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record (drug.original_moa is flagged as a data gap). However, based on the repurposing rationale annotations attached to other candidates in this evidence pack, entacapone's established clinical role is as a peripheral catechol-O-methyltransferase (COMT) inhibitor, used to prolong the central availability of levodopa in Parkinson's disease. It does not cross the blood-brain barrier and has no known direct disease-modifying action of its own.

PLA2G6-associated neurodegeneration (PLAN) is a genetic neurodegenerative disorder; its adult-onset form can present with parkinsonian symptoms. The theoretical link proposed by TxGNN is that patients with this parkinsonian phenotype might, like Parkinson's disease patients, be managed with levodopa-based regimens in which entacapone could serve as an adjunct. This is a plausible symptomatic-management hypothesis rather than a disease-modifying mechanism, and it is not supported by any clinical or literature evidence at this time — the connection should be treated as a knowledge-graph-derived hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Entacapone currently has no marketing authorization on file in Taiwan (market status: not marketed; 0 licenses recorded). No approved indication text is available from local regulatory data.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are marked as a **Blocking** data gap (DG001) — this must be resolved before any formal safety (S1) evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on a TxGNN knowledge-graph score (L5, decision stage S0), with zero supporting clinical trials or literature after targeted searches. Combined with a blocking data gap on TFDA safety labeling, there is currently no basis to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA label PDF (warnings/contraindications) — DG001, blocking
- Confirmed mechanism of action from DrugBank — DG002
- Preclinical or case-level evidence linking COMT inhibition to PLA2G6-associated neurodegeneration symptom management
- Note: other predicted indications for entacapone in this evidence pack — Lewy body dementia (rank 7) and progressive supranuclear palsy-corticobasal syndrome (rank 10) — reached decision stage S1 with at least weak trial/literature signals, and may be a more productive focus than this rank-1 candidate if resources are limited.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

