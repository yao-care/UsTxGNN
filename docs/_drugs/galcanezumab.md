---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 744
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Galcanezumab: From Migraine/Cluster Headache Prevention to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab is an anti-CGRP monoclonal antibody used for migraine and cluster headache prevention. The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, a rare inherited coagulation disorder, with a prediction score of **99.50%** — but currently **0 clinical trials** and **0 publications** support this direction, and the proposed mechanistic link is biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine and cluster headache prevention (not confirmed via Taiwan license data — see note below) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not marketed in Taiwan (TFDA) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, high severity — DG002). Based on known information, Galcanezumab is an anti-CGRP (calcitonin gene-related peptide) monoclonal antibody: it neutralizes the CGRP ligand and blocks receptor binding, and it is clinically used for migraine and cluster headache prevention.

Heparin Cofactor 2 (HCF2) deficiency is a hereditary thrombophilia caused by mutations in a serpin (serine protease inhibitor) gene, related to coagulation-inhibition pathways. There is no known biological connection between CGRP signaling and the HCF2/coagulation regulatory pathway.

Notably, this same pattern repeats: the two next-ranked TxGNN predictions for this drug — Antithrombin Deficiency Type 2 (score 99.41%) and Factor 5 Excess with Spontaneous Thrombosis (score 99.41%) — are also rare, hereditary coagulation/thrombosis disorders, clustered within a narrow score range (0.994–0.995). This tight clustering across an entire disease family, combined with the complete absence of clinical or literature evidence for all three, strongly suggests the high score reflects topological similarity in the knowledge-graph embedding space rather than a genuine pharmacological relationship. A CGRP-targeting monoclonal antibody has no established mechanism for modulating coagulation factor activity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Galcanezumab is not currently marketed in Taiwan (TFDA) — no license records are available (0 licenses on file). TFDA label/warning data required for safety evaluation is also outstanding (data gap, blocking — DG001).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.50%), there is zero clinical trial or literature evidence (Evidence Level L5), and the proposed mechanistic link between CGRP inhibition and a hereditary coagulation disorder lacks biological plausibility. The same score pattern appears across two other unrelated rare coagulation diseases, pointing to a likely graph-embedding artifact rather than three independent real signals.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindication data (blocking data gap, DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Independent biological/pharmacological plausibility review of the CGRP–coagulation pathway hypothesis before any further evaluation stage is initiated
- At minimum, preclinical or case-level evidence before this candidate can be reconsidered above Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

