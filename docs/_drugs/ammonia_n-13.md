---
layout: default
title: Ammonia N-13
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 2
---

# Ammonia N-13
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

# Ammonia N-13: From Cardiac Perfusion Imaging to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ammonia N-13 is a short-lived positron-emitting radiotracer used in PET scanning for cardiac perfusion imaging — a diagnostic, not therapeutic, application.
The TxGNN model predicts it may be effective for **Non-Syndromic Esophageal Malformation**,
yet **no clinical trials** and **no publications** currently support this direction, and the mechanistic link has been assessed as not biologically feasible.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indication on record |
| Predicted New Indication | Non-Syndromic Esophageal Malformation |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Ammonia N-13 is a positron-emitting radiopharmaceutical with an approximately 10-minute physical half-life. Its established role is as a diagnostic imaging agent for myocardial perfusion PET scans, not as a therapeutic drug in any approved indication. This diagnostic-only classification is a fundamental barrier to repurposing.

The TxGNN model's high prediction score (99.73%) most likely originates from indirect node pathways within the underlying knowledge graph rather than a direct therapeutic mechanism. Specifically, connections between ammonia metabolism, the urea cycle, and gastrointestinal tissue may create graph-level proximity — for example, the pathway linking H. pylori urease activity → ammonia production → GI tissue damage may bring this compound into the neighborhood of esophageal conditions within the graph topology. This is a known artifact when knowledge graph models are applied to diagnostic radiopharmaceuticals.

Three critical barriers prevent any viable mechanistic link from being established: (1) Ammonia N-13 is a diagnostic tracer, not a therapeutic agent; (2) non-syndromic esophageal malformation is a congenital structural birth defect where pharmacological intervention windows are undefined; and (3) the 10-minute physical half-life makes sustained systemic therapeutic exposure pharmacokinetically impossible. Furthermore, no specific ammonia uptake mechanism in esophageal tissue has been described in the literature. The mechanistic link is assessed as **not feasible**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ammonia N-13 is a short-lived PET diagnostic radiotracer with no known therapeutic mechanism that is applicable to non-syndromic esophageal malformation; the high TxGNN score reflects knowledge graph topology rather than a biologically plausible repurposing opportunity, and there is zero supporting clinical or preclinical evidence.

**To proceed, the following is needed:**
- A methodological review of whether TxGNN's training corpus appropriately handles diagnostic radiopharmaceuticals, as including them alongside therapeutic agents may produce systematically inflated but uninformative predictions
- An independent mechanistic assessment to determine whether any biological pathway plausibly connects ammonia metabolism to esophageal structural development
- If any credible biological signal is identified through that review, in vitro and in vivo preclinical studies would be required as a first step before any clinical evidence generation could be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

