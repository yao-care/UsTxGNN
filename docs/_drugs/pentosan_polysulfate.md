---
layout: default
title: Pentosan Polysulfate
parent: 僅模型預測 (L5)
nav_order: 1029
evidence_level: L5
indication_count: 3
---

# Pentosan Polysulfate
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

# PENTOSAN POLYSULFATE: From No Recorded Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Pentosan Polysulfate (DrugBank DB00686) is not currently marketed in this jurisdiction, and no original indication or approved-label data is on file. TxGNN predicts a possible link to **Primary Release Disorder of Platelets** (score 99.71%), but this prediction is based purely on knowledge-graph topology, with **zero clinical trials** and **zero publications** supporting it — and the drug's known antiplatelet pharmacology runs mechanistically counter to a disorder that requires improved platelet function.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed and no license/indication record exists |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for pentosan polysulfate is not available in DrugBank (data gap). Based on the pharmacological characterization available in the evidence pack, PPS is a semi-synthetic sulfated polysaccharide (heparinoid) with known **anticoagulant and antiplatelet activity**, including inhibition of platelet factor 4 and interference with the vWF–platelet interaction.

Primary release disorder of platelets (a storage pool disease) is a **bleeding disorder** caused by impaired platelet granule release — the clinical need is to *restore* platelet function, not suppress it. PPS's antiplatelet mechanism points in the opposite direction of what this indication requires, so the pharmacological rationale for repurposing is weak and potentially unsafe rather than supportive.

Notably, TxGNN's next two ranked candidates for this drug — Glanzmann thrombasthenia (rank 9071) and pseudo-von Willebrand disease (rank 9651) — follow the same pattern: all three are platelet-function bleeding disorders where an antiplatelet/heparinoid agent is mechanistically discordant. This consistent clustering suggests the model is picking up graph-topology similarity among platelet-related disease nodes rather than a genuine therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information

This drug currently holds no market authorization in the reviewed jurisdiction (Not Marketed, 0 licenses). No approved-indication text is available for comparison.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged internally as a **blocking** data gap (DG001) and must be resolved before any safety evaluation can proceed to Stage 1.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN graph-topology similarity (L5, no clinical or literature evidence), and the drug's known antiplatelet/heparinoid pharmacology is mechanistically discordant with a bleeding disorder that requires enhanced platelet function — raising a plausible safety concern rather than supporting efficacy. The drug is also unmarketed in this jurisdiction with no label data on file.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings/contraindications (blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Preclinical or in vitro pharmacology data clarifying PPS's net effect on platelet granule release/aggregation
- Any case reports or off-label use data in platelet storage pool disease, Glanzmann thrombasthenia, or pseudo-von Willebrand disease before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

