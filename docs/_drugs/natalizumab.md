---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 956
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a humanized monoclonal antibody against α4-integrin (VLA-4), publicly known to be used for relapsing multiple sclerosis and Crohn's disease (original indication data was not captured in this evidence pack — see DG002). The TxGNN model's top prediction is **Bronchitis** with a **99.46%** score, but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the pack's own mechanistic review flags it as likely unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack (data gap — see DG002). Publicly known use: relapsing multiple sclerosis, Crohn's disease |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved for this evidence pack (DG002, High severity). Based on the α4-integrin/VLA-4 pathway referenced in the pack's own rationale text, natalizumab blocks lymphocyte adhesion and migration across endothelial barriers — a mechanism explored in airway inflammatory disease (e.g., asthma) but with no established treatment rationale for bronchitis.

The evidence pack's own analysis for this candidate is explicit that the prediction is **not well supported**: bronchitis is predominantly infectious or irritant in etiology, blocking lymphocyte trafficking has no therapeutic rationale for it, and the resulting immunosuppression could plausibly *increase* infection risk. The pack flags this as a suspected knowledge-graph mis-connection through the respiratory/inflammation node cluster rather than a genuine mechanistic signal.

For context, the pack's lower-ranked candidates (psoriasis, parapsoriasis, acute lichenoid pityriasis) are supported only by case-report literature in which natalizumab **induces or aggravates** dermatologic disease during MS treatment — the opposite therapeutic direction — with one isolated case report of comorbid psoriasis improving. None of the five ranked candidates in this pack currently have positive, disease-directed clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Natalizumab is currently **not marketed** in the reference regulatory dataset (0 licenses/NDAs on record), so no authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: this pack's `safety` block (key warnings, contraindications, DDI) is fully a data gap (DG001, Blocking). Separately, literature surfaced while researching other ranked candidates (psoriasis) repeatedly documents progressive multifocal leukoencephalopathy (PML) as a serious class-level risk associated with natalizumab — this is not sourced from the formal safety fields but should be flagged for any follow-up safety review.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (bronchitis) has no clinical trial or literature support, and the pack's own mechanistic review assesses it as an unsupported, likely spurious knowledge-graph link with a plausible risk of harm (immunosuppression in an infection-driven disease). None of the five ranked candidates in this pack show positive disease-directed evidence.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking — required before any S1 safety screen)
- Confirmed original indication and MOA documentation (DG002)
- Independent review of the TxGNN knowledge-graph edge for natalizumab–bronchitis to rule out node mis-linkage
- If the psoriasis signal is pursued instead, prospective controlled data — existing literature trends toward natalizumab causing/aggravating psoriasis, not treating it
- Regulatory pathway assessment, given the drug is not currently marketed (0 NDAs on record)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

