---
layout: default
title: Antipyrine Arnica Montana Barium Carbonate Bismuth
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 0
---

# Antipyrine Arnica Montana Barium Carbonate Bismuth
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Multi-Ingredient Homeopathic Formula: No Drug Repurposing Predictions Generated

> **Ingredients**: Antipyrine · Arnica Montana · Barium Carbonate · Bismuth Subnitrate · Calcium Fluoride · Delphinium Staphisagria Seed · Hypericum Perforatum · Iron · Matricaria Chamomilla · Plantago Major · Sepia Officinalis Juice · Spigelia Anthelmia · Strychnos Nux-Vomica Seed · Veratrum Album Root

---

## One-Sentence Summary

This product is a complex mixture of 14 components spanning a synthetic analgesic (antipyrine), homeopathic botanicals, and mineral preparations, with no formal market registration found in the evaluated jurisdiction.
The TxGNN model did not generate any repurposing predictions for this compound, most likely because no recognized DrugBank identifier could be resolved for the multi-ingredient entry as a whole.
Without a prediction target and with all regulatory and safety fields absent, no evidence-level evaluation can be conducted at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No licensed indications on record |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — TxGNN produced no output for this entry |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

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
No DrugBank ID could be resolved for this multi-ingredient homeopathic preparation, preventing TxGNN from generating any repurposing candidates; combined with zero market registrations and absent safety data, there is no actionable basis to proceed.

**To proceed, the following is needed:**

- **Ingredient decomposition**: Identify which component(s) should serve as the primary active ingredient and resolve a corresponding DrugBank ID (e.g., Antipyrine → DB04946; Hypericum Perforatum → DB01070)
- **Mechanism of action (MOA)**: Retrieve pharmacological mechanism for the lead component via DrugBank API — currently a High-severity data gap (DG002)
- **Original indication**: Clarify the approved therapeutic use in at least one reference jurisdiction
- **Safety data**: Download and parse the product package insert to fill the Blocking-severity gap on warnings and contraindications (DG001)
- **Re-run TxGNN**: Once a single INN or DrugBank ID is confirmed, resubmit as a single-ingredient query to obtain a valid prediction score and ranked indication list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

