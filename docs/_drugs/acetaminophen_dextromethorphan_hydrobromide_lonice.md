---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Lonice
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Lonice
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

# Acetaminophen / Dextromethorphan / Lonicera Caprifolium: Cold-Relief Combination — Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This three-component combination — comprising the analgesic/antipyretic acetaminophen, the antitussive dextromethorphan hydrobromide, and the traditional herbal anti-inflammatory Lonicera caprifolium flower — is structurally consistent with an over-the-counter cold and flu remedy.
The TxGNN model returned **no predicted new indications** for this compound combination, likely because the multi-ingredient query string could not be mapped to a single DrugBank node.
Without a valid TxGNN output, a formal drug-repurposing evaluation **cannot be conducted at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication (0 active licenses found) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — model returned no output |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was produced for this query, so a mechanistic repurposing argument cannot be constructed. The likely reason is that the query string was submitted as a combined multi-ingredient name, and the mapping pipeline could not resolve it to a single DrugBank identifier — `drugbank_id` is `null` in the Evidence Pack.

Each individual active ingredient is well-characterised:
- **Acetaminophen** inhibits prostaglandin synthesis centrally, producing antipyretic and analgesic effects.
- **Dextromethorphan HBr** is an NMDA receptor antagonist and sigma-1 agonist used clinically as a non-opioid antitussive; it has also attracted interest in neurological repurposing (e.g., pseudobulbar affect, treatment-resistant depression).
- **Lonicera caprifolium flower** (honeysuckle) contains chlorogenic acid and luteolin and is used in traditional medicine for anti-inflammatory and antiviral properties.

To enable a proper repurposing analysis, each component should be evaluated **individually** against the TxGNN knowledge graph rather than as a single combined query.

---

## US Market Information

No active licenses are recorded for this combination in the regulatory database. The product is not currently marketed.

---

## Safety Considerations

Please refer to the package inserts of the individual components (acetaminophen, dextromethorphan hydrobromide) for safety information. No DDI data was returned for the combined query string, and no warnings or contraindications are available in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no predictions because the multi-ingredient query string could not be resolved to a DrugBank entity. Without a valid model output there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

1. **Decompose the query** — resubmit each active ingredient (acetaminophen, dextromethorphan, Lonicera caprifolium / chlorogenic acid / luteolin) as a separate TxGNN query and retrieve individual prediction scores.
2. **Resolve DrugBank IDs** — map each component to its canonical DrugBank identifier so the knowledge-graph edges can be traversed correctly.
3. **Confirm product intent** — clarify whether the combination is intended as an OTC cold remedy or has a separate therapeutic target; this determines which repurposing angle is commercially relevant.
4. **Collect regulatory data** — if the combination is to be developed, obtain TFDA package-insert PDFs to populate warnings, contraindications, and MOA fields (Data Gaps DG001 and DG002).
5. **Re-run the full pipeline** — once individual DrugBank IDs are confirmed, re-execute the evidence-collection pipeline (ClinicalTrials.gov, PubMed) per component to build a complete Evidence Pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

