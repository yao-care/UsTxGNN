---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Hemin
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

# Hemin: From Unavailable Original Indication to Thrombocytopenic Purpura

## One-Sentence Summary

Hemin (DrugBank DB03404) has no recorded original indication or mechanism-of-action data in this evidence pack, and it is not currently marketed in Taiwan. The TxGNN model's top prediction is **Thrombocytopenic Purpura**, but this is a **model score only** — no clinical trials or published literature currently support the connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license/indication data on record) |
| Predicted New Indication | Thrombocytopenic Purpura |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Hemin is not available, and no original indication is recorded in this evidence pack, so the drug's historical use cannot be compared against the predicted indication.

More importantly, the evidence pack's own rationale for this specific prediction states there is **no known mechanistic link** between Hemin and thrombocytopenic purpura: the high TxGNN score is attributed to clustering of hematologic disease nodes within the knowledge graph's topology, rather than any pharmacological or biological evidence. No clinical trials, ICTRP trials, or PubMed literature were found linking Hemin to thrombocytopenic purpura in any of the underlying searches.

For context, a lower-ranked candidate in this same evidence pack (hemophilia, rank 2) does have some preclinical support — an animal study showing heme oxygenase-1 (HO-1) induction reduces immune response to factor VIII in FVIII-deficient mice — but even that reaches only evidence level L4 and reflects an immune-modulation hypothesis rather than a direct hemostatic mechanism. The top-ranked thrombocytopenic purpura prediction has no comparable support at all.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data for Hemin is currently a blocking data gap — see remediation below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The thrombocytopenic purpura prediction is supported only by a TxGNN model score (L5) with an explicit note in the evidence pack that no biological mechanism is known — no clinical trials or literature exist. Combined with the drug's non-marketed status in Taiwan (0 licenses) and a blocking gap in TFDA safety data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label/monograph (warnings, contraindications) — currently a blocking data gap
- Hemin mechanism of action (MOA) data from DrugBank or primary literature
- Any preclinical or clinical evidence directly linking heme/HO-1 pathways to platelet destruction or thrombocytopenic purpura pathophysiology
- If pursuing an alternative candidate instead, hemophilia (rank 2, L4) has a weak preclinical signal worth a closer look, though it would need dedicated evaluation outside this report's scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

