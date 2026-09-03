---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 975
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nizatidine: From Acid-Suppressive Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

> Nizatidine is a histamine H2-receptor antagonist historically used to suppress gastric acid secretion, though this evidence pack contains no formal license record of its original approved indication and the drug currently holds **zero active NDAs** (Not Marketed status in the US).
> The TxGNN model's top-ranked prediction, **Active Peptic Ulcer Disease**, scores **99.96%**, but the model's own rationale flags this as the drug class's already-established indication rather than a novel hypothesis.
> No trials or literature are attached directly to this top-ranked entry; the strongest supporting evidence (20 publications, including multiple RCTs) sits under closely related predictions in this same pack (gastrojejunal ulcer, gastroduodenitis).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally recorded in this dataset (no licenses on file); historically an H2-receptor antagonist used for peptic ulcer disease |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (DrugBank) is currently a data gap (DG002). Based on the rationale text embedded in this evidence pack, nizatidine is a histamine H2-receptor antagonist that directly inhibits histamine-induced gastric acid secretion at the parietal cell — the classic pharmacology shared by all H2RA drugs (e.g., ranitidine, famotidine, cimetidine).

The predicted new indication, active peptic ulcer disease, is mechanistically identical to nizatidine's known historical use — the evidence pack itself notes this is "the core known indication of the H2RA class, not a novel repurposing hypothesis." This explains why no dedicated trials or literature are attached to this specific entry: it is not a discovery, but a confirmation of expected pharmacology.

Stronger, disease-adjacent evidence exists elsewhere in this same pack. Closely related entries — **gastrojejunal ulcer** (rank 2, 20 publications) and **gastroduodenitis** (rank 6, 6 publications) — share the same acid-related pathophysiology and include multiple randomized controlled trials directly testing nizatidine in duodenal and gastric ulcer healing (e.g., PMID 2568086, 2570656, 7960687, 1526089). These indirectly reinforce the plausibility of the rank-1 prediction even though they are not filed under it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this specific indication entry.

*Note: Substantial nizatidine-specific RCT evidence for the same underlying acid-peptic pathophysiology exists under related predicted entries in this pack (gastrojejunal ulcer, gastroduodenitis), including double-blind trials on duodenal and gastric ulcer healing (e.g., PMID 2568086, 2570656, 8888720, 7960687, 1982108, 1526089, 1742515, 2570012). These were not filed under the "active peptic ulcer disease" entry itself.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack — flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis is sound and reinforced by class-wide RCT evidence documented elsewhere in this pack, but the top-ranked prediction itself is not novel (it restates nizatidine's known H2RA use), carries no directly attached trial or literature evidence, and the drug currently has no active US marketing authorization.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-priority gap, DG002)
- Historical original-indication/license records, since none are on file for this drug
- Clarification of current market status — nizatidine (brand Axid) was withdrawn in several markets over NDMA impurity concerns; this should be verified before any further development steps
- If pursuing repurposing, prioritize **gastrojejunal ulcer** or **gastroduodenitis** as the lead candidate, given their substantially richer literature base compared to the rank-1 entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

