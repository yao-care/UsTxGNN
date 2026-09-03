---
layout: default
title: Salsalate
parent: 僅模型預測 (L5)
nav_order: 1144
evidence_level: L5
indication_count: 8
---

# Salsalate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Salsalate: From NSAID Analgesic/Anti-inflammatory Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Salsalate is a salicylate-class NSAID, originally used for anti-inflammatory and analgesic purposes (COX inhibition, antiplatelet effect); detailed original-indication and label data have not yet been collected for this evidence pack.
> The TxGNN model predicts a possible link to **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare monogenic skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely graph-embedding artifact rather than a genuine pharmacological relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not yet documented in this evidence pack (Salsalate is classified as a salicylate NSAID per available rationale text) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is currently a data gap for Salsalate. Based on information available elsewhere in this evidence pack, Salsalate is a salicylate-class NSAID whose activity is mediated through COX inhibition, anti-inflammatory effects, and antiplatelet action — a mechanism class typically relevant to inflammatory, pain, and cardiovascular-risk conditions.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare monogenic disorder caused by *NPR2* mutations, affecting the natriuretic peptide/CNP signaling pathway that governs growth-plate chondrocyte development. This is a developmental, non-inflammatory pathway with no known mechanistic overlap with COX inhibition or salicylate pharmacology.

The evidence pack's own repurposing rationale explicitly assesses this connection as unlikely to reflect true pharmacology, attributing the high TxGNN score instead to embedding-space clustering among rare skeletal-disease nodes in the knowledge graph. Of the eight predicted indications reviewed for this candidate, seven (including this top-ranked one) share this same pattern — rare monogenic skeletal/developmental syndromes with no plausible link to an NSAID mechanism. Only the eighth-ranked prediction, spondyloarthropathy susceptibility, has any class-level pharmacological rationale (NSAIDs, including salicylates, are an established symptomatic treatment class for spondyloarthropathies), but even this is framed in the pack as a research question rather than an actionable candidate, since it concerns genetic *susceptibility* rather than active disease, and no salsalate-specific studies exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Salsalate is currently **not marketed** in the reference dataset (0 NDAs / licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/FDA label warnings and contraindications for Salsalate have not yet been collected (flagged as a **Blocking** data gap), which by itself precludes any safety-based go/no-go decision for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an unvalidated TxGNN score (L5) with no supporting clinical trials or literature, and the evidence pack's own mechanistic analysis assesses the drug–disease link as mechanistically implausible (likely a knowledge-graph embedding artifact rather than true pharmacology). Combined with the absence of label/safety data (a Blocking gap) and the drug's unmarketed status, there is no basis to advance this indication.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/FDA label warnings and contraindications) before any safety-relevant evaluation can proceed
- Resolve DG002 (confirmed mechanism of action from DrugBank) to properly assess mechanistic plausibility
- If pursuing further research, redirect attention to the more mechanistically plausible spondyloarthropathy-susceptibility signal (rank 8) via targeted literature search on salicylates/NSAIDs in spondyloarthropathy, rather than the top-ranked rare skeletal dysplasia predictions
- Deprioritize the seven rare monogenic skeletal/developmental disease predictions absent new mechanistic or experimental evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

