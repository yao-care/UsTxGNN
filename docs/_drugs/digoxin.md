---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 608
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Digoxin: From Undocumented Original Indication to Prinzmetal Angina

## One-Sentence Summary

> Digoxin (DrugBank ID: DB00390) is a long-established cardiac glycoside; however, this evidence pack contains no Taiwan/US license text describing its original approved indication, and mechanism-of-action data is currently a data gap.
> The TxGNN model predicts a potential association with **Prinzmetal angina**, but this is currently supported only by model-level similarity —
> **0 clinical trials** and **2 tangential publications** (neither specific to digoxin in this indication) are available, and the proposed mechanistic rationale actually points in the opposite pharmacological direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license/indication text available) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a High-severity data gap in the evidence pack). Based on general pharmacological knowledge, digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump, producing a positive inotropic and negative chronotropic/dromotropic effect; it is not a vasodilator or coronary spasmolytic agent.

Prinzmetal (variant) angina is caused by transient coronary artery vasospasm, and its standard treatments (calcium channel blockers, nitrates) work by relaxing vascular smooth muscle. Digoxin's known pharmacology does not provide a plausible mechanistic bridge to this indication — if anything, some literature suggests cardiac glycosides may increase vascular tone, which would work against the therapeutic goal in vasospastic angina.

The two literature items retrieved for this prediction are general reviews on chronopharmacology and on the pathophysiology of angina decubitus; neither studies digoxin specifically, nor provides direct evidence of efficacy in Prinzmetal angina. The prediction therefore appears to be driven by knowledge-graph embedding similarity rather than by a coherent mechanistic or clinical signal, and should be treated as low-confidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta physiologica et pharmacologica Bulgarica | General review of circadian rhythms and chronopharmacology in antihypertensive treatment; does not study digoxin or Prinzmetal angina specifically |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chinese Medical Sciences Journal | Re-evaluates the mechanism of angina decubitus (effort-related angina) in 30 patients; digoxin is not discussed as a treatment |

---

## US Market Information

No marketing authorization records available — this evidence pack indicates the drug is currently "Not marketed" (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data for this drug is currently an identified data gap of Blocking severity, which prevents a formal safety pre-screen at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with zero digoxin-specific clinical trials and only two non-specific review articles; the proposed mechanistic link is not plausible and may run counter to the therapeutic need in Prinzmetal angina (vasodilation vs. digoxin's inotropic/vasotonic profile).

**To proceed, the following is needed:**
- Resolution of the Blocking-severity data gap on TFDA warnings/contraindications before any safety pre-screen (S1) can begin
- Confirmed mechanism-of-action data for digoxin (High-severity data gap) to properly assess mechanistic plausibility
- Digoxin-specific preclinical or clinical evidence in coronary vasospasm/Prinzmetal angina, which does not currently exist in the literature searched
- Given the contradictory mechanistic signal, consider deprioritizing this candidate in favor of other TxGNN-predicted indications with stronger rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

