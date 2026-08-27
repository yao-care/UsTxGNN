---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 842
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leflunomide: Original Indication Not on File → Predicted New Indication: Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide's original approved indication and mechanism of action are not documented in this evidence pack (flagged as Blocking/High-severity data gaps). The TxGNN model predicts potential efficacy for **brachydactyly-syndactyly syndrome**, a rare congenital limb-development disorder, but this prediction is supported by **zero clinical trials and zero publications**, and the model's own rationale flags the mechanistic link as biologically implausible — likely a statistical artifact from shared gene nodes in the knowledge graph rather than a genuine therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (see Data Gaps) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for leflunomide is not available in this evidence pack (Data Gap DG002, High severity). Leflunomide is known in general pharmacology as a DHODH (dihydroorotate dehydrogenase) inhibitor that suppresses pyrimidine synthesis, producing anti-inflammatory/immunomodulatory effects — but this is not sourced from the evidence pack itself and cannot be treated as verified for this report.

More importantly, the model's own repurposing rationale argues **against** a plausible mechanistic connection: brachydactyly-syndactyly syndrome is a congenital limb-development disorder driven by developmental gene regulation, not an inflammatory or immune-mediated pathology. There is no documented mechanistic pathway linking a pyrimidine-synthesis inhibitor to skeletal/limb morphogenesis. The evidence pack explicitly attributes the high TxGNN score to likely indirect graph associations (e.g., shared gene nodes between skeletal-development pathways and the drug's targets) rather than a treatment-relevant relationship.

The same caveat applies to the second-ranked candidate, colobomatous microphthalmia-rhizomelic dysplasia syndrome — another rare congenital malformation syndrome (ocular and proximal skeletal dysplasia) with no plausible link to leflunomide's known pharmacology and no corroborating trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No marketing authorizations are on file for leflunomide in this jurisdiction (0 licenses; market status recorded as Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are an unresolved **Blocking** data gap — DG001 — and drug-drug interaction data was not found.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are Evidence Level L5 (model prediction only) with no supporting clinical trials or literature, and the mechanistic rationale itself suggests the high TxGNN scores likely reflect indirect knowledge-graph associations rather than true biological plausibility. In addition, a Blocking safety data gap (missing TFDA label/warnings) prevents even a preliminary safety screen.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — Blocking gap, required before any safety pre-screen
- Verified mechanism of action data (e.g., via DrugBank API) to properly assess mechanistic plausibility
- Independent literature/preclinical validation specifically testing leflunomide in developmental/skeletal disorders, given the model's own flag that this signal may be a graph artifact
- If no independent support emerges, deprioritize both candidates rather than advancing to further evaluation stages
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

