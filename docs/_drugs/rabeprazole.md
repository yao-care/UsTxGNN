---
layout: default
title: Rabeprazole
parent: 僅模型預測 (L5)
nav_order: 1103
evidence_level: L5
indication_count: 2
---

# Rabeprazole
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

# Rabeprazole: From an Undocumented Original Indication to Smouldering Systemic Mastocytosis

## One-Sentence Summary

> Rabeprazole (DrugBank ID: DB01129) has no recorded original indication or market authorization in this evidence pack.
> The TxGNN model predicts a possible link to **Smouldering Systemic Mastocytosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (0 licenses in evidence pack) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for rabeprazole is not currently available in this evidence pack, and no original indication is on record. This is flagged as a **High-severity data gap (DG002)** and should be resolved before further mechanistic assessment.

Based on the model's own rationale, the link between rabeprazole and smouldering systemic mastocytosis is **indirect and symptomatic, not disease-modifying**: patients with systemic mastocytosis can develop excess gastric acid secretion (a Zollinger-Ellison–like syndrome) driven by histamine release from mast cells, for which proton pump inhibitors (PPI)-class agents are sometimes used as symptomatic support. The high TxGNN score (0.994) likely reflects this kind of pharmacological co-morbidity association picked up from the knowledge graph, rather than a mechanism that treats the underlying clonal mast cell disease (e.g., KIT mutation-driven proliferation).

A second, closely related prediction — lymphoadenopathic mastocytosis with eosinophilia (score 0.993) — shows the same pattern: no direct mechanistic link to the disease's core immunological/hematological pathology. Both predictions point to a shared theme (mastocytosis spectrum disorders with acid-related symptom management), but neither is disease-modifying evidence, and neither is corroborated by any clinical trial or literature evidence at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No market authorization records found — rabeprazole is currently listed as **Not Marketed** (0 licenses) in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings and contraindications for this drug are marked as a **Blocking data gap (DG001)** in this evidence pack — this must be resolved before any safety-related decision can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by the TxGNN model score (Evidence Level L5), with zero clinical trials or publications, and the model's own rationale describes the mechanistic link as indirect/symptomatic rather than disease-modifying. Combined with a Blocking-severity gap in TFDA safety data and no recorded market authorization, this candidate does not meet the bar to advance past initial screening (S0).

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — Blocking, resolve first)
- Rabeprazole mechanism of action data (DG002 — High)
- Targeted literature/clinical trial search specifically for PPI use in mastocytosis-related acid hypersecretion
- Verification of rabeprazole's actual original indication and any Taiwan/US market status, since none is currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

