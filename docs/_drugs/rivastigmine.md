---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 1131
evidence_level: L5
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Rivastigmine: From Alzheimer's Disease to Glaucoma

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor originally developed for Alzheimer's disease and dementia-related cognitive decline. The TxGNN model predicts it may lower intraocular pressure and be effective for **Glaucoma**, but this direction is currently supported only by preclinical (animal) and mechanistic literature — **no clinical trials** have been conducted for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no marketed license record) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in structured form, but the repurposing rationale supplied with this candidate describes rivastigmine as a dual inhibitor of acetylcholinesterase (AChE) and butyrylcholinesterase (BuChE). By inhibiting these enzymes, rivastigmine increases local acetylcholine concentration — a mechanism pharmacologically similar to established cholinergic agonists (e.g., pilocarpine) that are used to treat glaucoma by contracting the ciliary muscle and increasing trabecular outflow, thereby lowering intraocular pressure (IOP).

This provides reasonable mechanistic plausibility: rivastigmine's known pharmacology (cholinergic enhancement) overlaps with a validated drug class for glaucoma treatment. However, rivastigmine is currently formulated and used systemically (oral or transdermal patch) for dementia, not as a topical ophthalmic agent. There is no clinical or pharmacokinetic data on ocular penetration, local tolerability, or systemic exposure risk if reformulated for topical eye use — this is a substantial gap between the mechanistic hypothesis and a deliverable product.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical (Animal - Rabbit) | J Ocul Pharmacol Ther | Topical rivastigmine lowered intraocular pressure in normotensive rabbits over an 8-hour monitoring period, providing direct in vivo evidence for the IOP-lowering hypothesis. |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review | Front Mol Biosci | Reviews cholinergic agents (muscarinic receptor agonists) for IOP reduction via the trabecular meshwork, noting systemic adverse effects limit current FDA-approved agents. |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opin Ther Pat | Notes that mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis, and glaucoma, supporting the class-level rationale. |

---

## US Market Information

Not applicable — the drug currently has no marketed license record in this jurisdiction (0 NDAs, market status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and MOA data are flagged as data gaps — see below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is biologically plausible and supported by one preclinical animal study, but there are zero clinical trials, no human safety/PK data for topical ocular use, and blocking data gaps in TFDA labeling and formal MOA documentation. Evidence level is L4 (preclinical/mechanistic only) — insufficient to proceed toward clinical evaluation.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any S1 safety review)
- Formal MOA documentation from DrugBank (High-priority data gap affecting mechanistic analysis)
- Human pharmacokinetic/ocular penetration data if a topical formulation is considered
- At least one Phase 1/2 clinical study evaluating IOP-lowering effect and local/systemic tolerability in humans
- Drug interaction (DDI) profile specific to ophthalmic or systemic use in glaucoma patients (currently not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

