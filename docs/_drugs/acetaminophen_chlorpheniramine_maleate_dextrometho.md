---
layout: default
title: Acetaminophen Chlorpheniramine Maleate Dextrometho
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 0
---

# Acetaminophen Chlorpheniramine Maleate Dextrometho
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

# ACETAMINOPHEN / CHLORPHENIRAMINE / DEXTROMETHORPHAN / PSEUDOEPHEDRINE Combination: Insufficient Data for Repurposing Prediction

## One-Sentence Summary

This is a classic four-component multi-symptom cold and flu combination (Acetaminophen + Chlorpheniramine Maleate + Dextromethorphan HBr + Pseudoephedrine), widely used in OTC cold remedies worldwide.
The TxGNN model **did not generate any repurposing predictions** for this query, as the multi-component combination string could not be resolved to a single DrugBank entity.
As a result, **no clinical trial or literature evidence** for a new indication was retrieved, and this report primarily documents the data gap findings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multi-symptom cold/flu relief (fever, cough, nasal congestion, runny nose) — inferred from known pharmacology |
| Predicted New Indication | — (No prediction generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — model produced no output |
| US/TW Market Status | 未上市 (Not found in regulatory database) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

TxGNN is a graph-based model that maps **individual drug compounds** to DrugBank node IDs within a knowledge graph. This query submitted a four-ingredient combination string as a single entity:

> `ACETAMINOPHEN; CHLORPHENIRAMINE MALEATE; DEXTROMETHORPHAN HYDROBROMIDE; PSEUDOEPHEDRINE`

The system could not resolve this string to a single `drugbank_id` (returned `null`), which is the required input for the TxGNN prediction pipeline. Without a valid DrugBank node, no knowledge graph traversal or disease association scoring can occur.

Each individual ingredient is a well-characterized compound with its own DrugBank entry:

| Component | Known Role | Likely DrugBank Entry |
|-----------|-----------|----------------------|
| Acetaminophen (APAP) | Antipyretic / Analgesic | DB00316 |
| Chlorpheniramine Maleate | First-generation antihistamine | DB01114 |
| Dextromethorphan HBr | Cough suppressant (NMDA antagonist) | DB00514 |
| Pseudoephedrine | Nasal decongestant (sympathomimetic) | DB00852 |

To obtain meaningful repurposing predictions, each ingredient should be submitted as a **separate query** to the TxGNN pipeline.

---

## Safety Considerations

All safety data fields for this multi-component query returned gaps. However, based on established pharmacology of the four components, the following are known class-level concerns:

- **Acetaminophen**: Hepatotoxicity risk at high doses; contraindicated with hepatic impairment and concurrent alcohol use
- **Pseudoephedrine**: Sympathomimetic effects — contraindicated with MAOIs, hypertension, severe coronary artery disease, and hyperthyroidism
- **Chlorpheniramine**: Anticholinergic effects — caution in elderly patients, glaucoma, BPH; sedation risk
- **Dextromethorphan**: Serotonin syndrome risk when combined with MAOIs or serotonergic agents; CYP2D6 interactions

For complete safety information, refer to each component's individual package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not process this multi-component combination as a single entity — no DrugBank ID was resolved and no predictions were generated. There is no repurposing output to evaluate.

**To proceed, the following is needed:**

1. **Decompose into individual queries**: Re-submit each of the four active ingredients (Acetaminophen, Chlorpheniramine Maleate, Dextromethorphan HBr, Pseudoephedrine) as separate TxGNN candidates
2. **Resolve DrugBank IDs**: Map each component to its respective DrugBank ID before pipeline entry
3. **Clarify the intended repurposing target**: Determine whether the repurposing hypothesis is for the combination as a whole, or for one specific component within it
4. **Review individual MOA data**: Retrieve mechanism of action from DrugBank for each component separately
5. **Retrieve safety data**: Download and parse the package insert PDF from TFDA (or FDA) for each individual component to fill the DG001 and DG002 data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

