---
layout: default
title: Tyrosine
parent: 僅模型預測 (L5)
nav_order: 1273
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From No Approved Indication to Cauda Equina Syndrome

## One-Sentence Summary

> Tyrosine is a naturally occurring amino acid and precursor to catecholamines and thyroid hormones; it currently holds no approved drug indication and is not marketed in the US.
> The TxGNN model's top prediction suggests possible relevance to **Cauda Equina Syndrome**,
> but this is supported by **0 clinical trials** and only **1 unrelated case report**, with the underlying analysis explicitly flagging no plausible mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no approved indication on record |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for tyrosine as a therapeutic agent is not available. Based on known pharmacology, tyrosine is a non-essential amino acid that serves as the metabolic precursor for catecholamines (dopamine, norepinephrine, epinephrine) and thyroid hormones (T3/T4). It has no approved drug indication and no NDAs on record in the US market.

For the top-ranked prediction (cauda equina syndrome), the knowledge-graph model assigns a high raw confidence score (99.77%), but the accompanying rationale explicitly finds **no plausible mechanistic link**: cauda equina syndrome is a mechanical/compressive neurological emergency involving nerve root injury, and tyrosine's known amino-acid/catecholamine-precursor pathways have no established relevance to that pathophysiology. The single associated literature citation is an unrelated case report on clear cell sarcoma of a spinal nerve root, which does not discuss tyrosine as a treatment. This pattern is consistent with a knowledge-graph embedding false positive rather than a genuine biological signal.

It is also worth noting that across all 10 candidate indications in this evidence pack, the same pattern repeats: several candidates (e.g., hyperthyroidism, hyperthyroxinemia) show a mechanistically *contradictory* direction (tyrosine is a hormone precursor, not an antagonist), and multiple clinical trials/literature hits were driven by keyword confusion with unrelated "tyrosine kinase inhibitor" drugs rather than the amino acid itself. This suggests systematic noise in the underlying evidence retrieval for this candidate rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical Focus | Case report of clear cell sarcoma originating in the S-1 nerve root, previously misdiagnosed as psammomatous melanotic schwannoma; does not discuss tyrosine as a treatment and is not directly relevant to cauda equina syndrome management |

## US Market Information

Tyrosine is not currently marketed in the US and has no NDAs on record.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are currently unavailable in this evidence pack. A blocking data gap has been flagged for FDA/TFDA label warnings and contraindications, meaning safety review cannot proceed until this is resolved.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN score, this candidate has no clinical trial support, only one irrelevant literature citation, and an explicit mechanistic assessment finding no plausible biological rationale — most consistent with a model false positive rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for tyrosine as a therapeutic agent
- FDA/TFDA label data (warnings, contraindications) — currently blocking (DG001)
- Independent mechanistic or preclinical validation specific to cauda equina syndrome pathophysiology
- Re-screening of the remaining 9 ranked candidates for the same drug, as several show contradictory mechanistic direction or keyword-confusion artifacts (tyrosine vs. tyrosine kinase inhibitors) that should be resolved before any candidate in this set advances past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

