---
layout: default
title: Aluminum Zirconium Octachlorohydrate Anhydrous
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 0
---

# Aluminum Zirconium Octachlorohydrate Anhydrous
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

# Aluminum Zirconium Octachlorohydrate Anhydrous: Evaluation Not Feasible — Insufficient Data

## One-Sentence Summary

Aluminum Zirconium Octachlorohydrate Anhydrous is an aluminum-zirconium salt compound used primarily as an active ingredient in topical antiperspirant formulations; it is not recognized as a systemic pharmaceutical in standard drug registries.
The TxGNN model generated **no repurposing predictions** for this compound, as it could not be mapped to a DrugBank entry and therefore has no node in the knowledge graph.
Due to the complete absence of regulatory approval records, predicted indications, and retrievable safety data, a formal repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established — no regulatory approvals found |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not applicable |
| Evidence Level | L5 (no model predictions, no clinical studies, no literature) |
| US Market Status | Not marketed as a pharmaceutical |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action data for Aluminum Zirconium Octachlorohydrate Anhydrous is not available from DrugBank (no DrugBank ID could be resolved). Based on general scientific knowledge, this compound is an inorganic aluminum-zirconium salt that works topically by forming temporary plugs within eccrine sweat gland ducts, reducing the outward flow of perspiration. It has no known systemic pharmacological targets and is not classified as a pharmaceutical drug in major regulatory frameworks.

The TxGNN knowledge graph requires a valid DrugBank node to compute drug–disease association scores. Because this compound could not be matched to a DrugBank ID during the pipeline run, it was excluded from prediction entirely. This is a pipeline limitation rather than a finding of therapeutic irrelevance — the compound may still have scientific interest if properly registered in reference databases.

No original pharmaceutical indication was identified: the TFDA registry query returned zero results, consistent with the compound's status as a cosmetic/OTC ingredient. Without an established pharmaceutical indication and without TxGNN output, the standard repurposing evaluation workflow cannot proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The compound lacks both a DrugBank ID and TxGNN predictions, making it impossible to perform knowledge-graph-based repurposing analysis; additionally, zero regulatory approvals were found, suggesting this substance falls outside the scope of the current pharmaceutical repurposing pipeline.

**To proceed, the following is needed:**
- Resolve whether a DrugBank ID exists for this compound (search by CAS number or INCI name: *Aluminum Zirconium Octachlorohydrate*)
- Clarify regulatory classification: cosmetic active ingredient vs. OTC drug vs. prescription pharmaceutical
- Obtain mechanism of action data from DrugBank, PubChem, or peer-reviewed literature
- If a valid DrugBank ID is confirmed, re-ingest the compound into the TxGNN pipeline and re-run KG and DL predictions
- Retrieve any available safety data (TSCA listing, SDS, FDA Monograph for OTC antiperspirants) to populate the safety section before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

