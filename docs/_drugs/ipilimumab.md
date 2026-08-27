---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 2
---

# Ipilimumab
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

# Ipilimumab: From Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab is an anti-CTLA-4 immune checkpoint inhibitor historically used in melanoma immunotherapy. The TxGNN model predicts it may be effective for **Choroideremia**, but currently **0 clinical trials** and **0 publications** support this specific direction, and the mechanistic rationale is judged biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma (official approved-indication text unavailable — see data gap DG001) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on known information, ipilimumab is a monoclonal antibody that blocks CTLA-4, releasing inhibition of T-cell activation to enhance the immune response against tumor antigens — a mechanism established through its use in melanoma.

Choroideremia, however, is a monogenic disease caused by CHM gene mutations leading to Rab escort protein 1 (REP1) deficiency, resulting in progressive choroidoretinal degeneration through a protein-trafficking defect. This pathophysiology has no known biological connection to CTLA-4-mediated immune checkpoint signaling.

Given the absence of any supporting clinical trial or literature evidence despite a high TxGNN score, this prediction is best interpreted as a knowledge-graph embedding artifact (a statistical co-occurrence pattern) rather than a mechanistically grounded repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

*(Included because the original indication, melanoma, is an oncologic condition.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.06%), there is no clinical trial or literature evidence supporting ipilimumab for choroideremia, and the proposed mechanistic link (CTLA-4 immune checkpoint blockade vs. a REP1 protein-trafficking defect) has no established biological basis. This candidate should not advance without independent mechanistic or preclinical justification.

**To proceed, the following is needed:**
- Preclinical or mechanistic data establishing a plausible link between CTLA-4 pathway modulation and CHM/REP1-related choroidoretinal degeneration
- TFDA label data (warnings/contraindications) to close data gap DG001
- Confirmed mechanism of action (MOA) documentation to close data gap DG002

---
**Note:** This evidence pack also contains a second candidate for ipilimumab — **non-cutaneous melanoma** (TxGNN score 99.02%, Evidence Level L1, recommendation "Proceed with Guardrails") — supported by a Phase 3 RCT (NCT02506153) and peer-reviewed literature (e.g., PMID 24999899 on uveal/mucosal melanoma). Given its substantially stronger evidence base, it may warrant a separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

