---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 1242
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

> Topiramate is a broad-spectrum anticonvulsant, generally known for treating epilepsy and migraine prophylaxis (formal Taiwan/US license indication text was not available in this evidence pack).
> The TxGNN model's top-ranked prediction for this drug is **Trigeminal Nerve Neoplasm**,
> but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-derived signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory dataset |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (per this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on established clinical knowledge, topiramate is a broad-spectrum antiepileptic agent acting through sodium channel blockade, GABA-A receptor potentiation, AMPA/kainate glutamate receptor antagonism, and carbonic anhydrase inhibition. It has no known antineoplastic or antitumor mechanism.

The relationship between topiramate and trigeminal nerve neoplasm is, by the evidence pack's own assessment, driven purely by TxGNN's knowledge-graph topological similarity — there is no biological plausibility identified. At most, one could speculate that an anticonvulsant/analgesic-adjacent drug might indirectly relieve neuropathic pain associated with a trigeminal nerve tumor, but this would not constitute treatment of the neoplasm itself.

Given the absence of a mechanistic rationale and the complete lack of supporting trials or literature, this specific prediction should be treated as a low-confidence model output rather than a credible repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Trigeminal Nerve Neoplasm) has no clinical trial or literature support, no established mechanistic link, and the drug's MOA and regulatory/safety data are currently unavailable (data gaps DG001, DG002). This does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- DrugBank MOA data and TFDA/FDA label (warnings, contraindications, DDI)
- Any preclinical or case-level evidence connecting topiramate to trigeminal nerve tumor biology, if it exists
- Confirmation of actual US/Taiwan marketing and license status, since this dataset shows 0 licenses despite topiramate being a long-marketed drug elsewhere

**Note:** This evidence pack (`TW-DB00273-multi`) contains eight additional TxGNN predictions for topiramate, several with meaningfully stronger support and a coherent mechanistic story (broad-spectrum anticonvulsant → reflex epilepsy syndromes): **visual epilepsy** (L2, 4 trials incl. a Phase 3 RCT, 20 literature refs), **thinking seizures** (L2, includes Phase 3 evidence), and **reading seizures** (L2, includes a Phase 3 RCT in refractory partial-onset seizures). These are better candidates for a "Research Question" track than the top-ranked trigeminal nerve neoplasm prediction and may warrant a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

