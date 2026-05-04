---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Pseudo
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Pseudo
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

# ACETAMINOPHEN / DEXTROMETHORPHAN / PSEUDOEPHEDRINE: Combination Cold Remedy — Repurposing Assessment Incomplete

## One-Sentence Summary

ACETAMINOPHEN / DEXTROMETHORPHAN HYDROBROMIDE / PSEUDOEPHEDRINE is a classic OTC triple-combination cold remedy targeting pain/fever, cough, and nasal congestion simultaneously.
The TxGNN model returned **no predicted new indications** for this combination entry, most likely because no single DrugBank ID could be resolved for the multi-ingredient query.
With **0 clinical trials**, **0 publications**, and **0 regulatory licenses** retrieved, a full repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved (data gap) |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and even that is absent) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this query, so a mechanistic rationale for a new indication cannot be constructed from the Evidence Pack.

For context, this fixed-dose combination contains three well-characterized ingredients acting on distinct targets:

- **Acetaminophen** — centrally and peripherally inhibits prostaglandin synthesis; used for analgesia and antipyresis.
- **Dextromethorphan HBr** — NMDA receptor antagonist and sigma-1 receptor agonist acting on the cough center in the medulla; used as an antitussive.
- **Pseudoephedrine** — sympathomimetic amine (α- and β-adrenergic agonist); causes vasoconstriction of nasal mucosa for decongestion.

Because the pipeline could not resolve a single DrugBank ID for this combination string, the knowledge-graph traversal did not produce repurposing candidates. Each individual component (e.g., dextromethorphan alone) has separately documented repurposing literature (e.g., dextromethorphan/quinidine for pseudobulbar affect, NMDA-related neuropathic pain), but those signals are not captured here.

---

## Clinical Trial Evidence

Currently no related clinical trials retrieved for this combination query.

---

## Literature Evidence

Currently no related literature retrieved for this combination query.

---

## Taiwan Market Information

This drug combination holds **no Taiwan (TFDA) marketing authorizations**. No license table can be generated.

---

## Safety Considerations

All safety fields contain data gaps. Before any further evaluation, the following must be retrieved from official sources:

- **Key Warnings**: Not available — retrieve from TFDA package insert PDF or FDA label (DailyMed)
- **Contraindications**: Not available — pseudoephedrine carries known contraindications (MAOIs, severe hypertension, hyperthyroidism); dextromethorphan interacts with serotonergic agents
- **Drug Interactions**: DDI query returned no results — manual review strongly recommended given pseudoephedrine's adrenergic profile and dextromethorphan's serotonin-related risk

> Please refer to the individual component package inserts for safety information until a consolidated review is complete.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no DrugBank ID was resolved, no TxGNN predictions were generated, and all safety fields are flagged as data gaps. There is no basis for a repurposing recommendation at this stage.

**To proceed, the following is needed:**

- **Decompose the query**: Run TxGNN predictions separately for each active ingredient (acetaminophen `DB00316`, dextromethorphan `DB00514`, pseudoephedrine `DB00852`) and aggregate results
- **Resolve DrugBank ID**: Map the combination string to component IDs to enable knowledge-graph traversal
- **Retrieve MOA data**: Query DrugBank API for each component to support mechanistic analysis
- **Retrieve safety data**: Download TFDA package insert PDF and parse warnings/contraindications (Data Gap DG001)
- **Re-run Evidence Pack generation**: With corrected inputs, re-execute the full pipeline to obtain clinical trial and literature evidence
- **Confirm Taiwan regulatory status**: Verify whether any branded products containing this combination (e.g., compounded products or OTC imports) hold TFDA approval under different trade names
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

