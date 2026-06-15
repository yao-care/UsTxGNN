---
layout: default
title: Benzoic Acid
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Benzoic Acid: From Antimicrobial Preservative to Bronchitis

## One-Sentence Summary

Benzoic acid is a simple aromatic carboxylic acid widely used as an antimicrobial preservative and pharmaceutical excipient, with no established standalone therapeutic indication on record.
The TxGNN model predicts it may be effective for **Bronchitis**, currently supported by **0 clinical trials** and **2 publications** — both of which discuss benzoic acid *derivatives* rather than the compound itself.
Overall evidence is minimal and highly indirect; this prediction should be treated as a hypothesis-generating signal only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established pharmaceutical indication (used as preservative/excipient) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (0 registered authorizations found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzoic acid is primarily recognized as an antimicrobial preservative (E210) used in food and pharmaceutical products. It holds no active NDA or standalone therapeutic registration in the queried databases, and its original_indications list is empty — meaning TxGNN is predicting a **de novo** therapeutic role rather than extending an existing one.

Benzoic acid does exhibit mild intrinsic antimicrobial activity against certain respiratory pathogens, including *Streptococcus pneumoniae*. Beyond direct antimicrobial action, the TxGNN knowledge graph likely connected benzoic acid to bronchitis via its structural derivatives: benzoic acid–derived soluble epoxide hydrolase (sEH) inhibitors can modulate the arachidonic acid metabolic pathway, suppressing pro-inflammatory eicosanoids and theoretically reducing bronchial inflammation. A second pathway may involve benzoic acid's known antioxidant properties, which could partially suppress inflammatory cascades in the airways.

It is essential to flag that these remain **indirect mechanistic inferences** based on structurally related compounds. The biological activity of a derivative does not automatically transfer to the parent scaffold. No direct preclinical or clinical data exists for benzoic acid as a bronchitis therapeutic, and the knowledge graph connection likely reflects structural/chemical proximity noise rather than a validated pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ Both retrieved publications are **indirect background references** — neither directly studies benzoic acid as a treatment for bronchitis.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | *Drugs* | Review of repaglinide, described as a "carbamoylmethyl benzoic acid derivative," for type 2 diabetes. Retrieved due to the benzoic acid scaffold; has no relevance to bronchitis. |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Animal Study | *Am J Respir Cell Mol Biol* | A soluble epoxide hydrolase (sEH) inhibitor — a benzoic acid derivative — showed anti-inflammatory effects in a rat model of tobacco smoke–induced COPD/bronchitis. Provides indirect mechanistic background only; does not test benzoic acid itself. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** An important known safety concern is that benzoic acid, when used as a preservative in ophthalmic solutions, is associated with corneal epithelial damage. Any repurposing development should carefully assess systemic toxicity, route-of-administration safety, and acceptable therapeutic dosing ranges, as benzoic acid was not developed with systemic therapeutic intent.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for benzoic acid are rated L5 — model prediction only — with no supporting clinical trials and no directly relevant literature for any indication. The top prediction (bronchitis, score 99.98%) is grounded in mechanistic analogies from structural derivatives, not from the parent compound. Benzoic acid has no established therapeutic role and no market authorizations in any queried database. This profile does not meet the minimum evidence threshold to proceed.

**To proceed, the following is needed:**

- **Compound identity clarification**: Confirm whether TxGNN's prediction targets benzoic acid as a standalone therapeutic agent or as a structural template — the distinction has major implications for drug development feasibility.
- **Preclinical bronchitis studies**: Direct in vitro and in vivo experiments testing benzoic acid in respiratory inflammation models are required before any translational discussion.
- **MOA data retrieval**: Query the DrugBank API (DB03793) to confirm any documented targets, pathways, or pharmacological activities for benzoic acid itself.
- **Full safety/toxicology profile**: Characterize systemic toxicity, bioavailability, and acceptable dose range for potential therapeutic routes of administration.
- **Knowledge graph audit**: Investigate whether the TxGNN bronchitis prediction results from a legitimate mechanistic path or from graph-level conflation of benzoic acid with its pharmacologically active derivatives (e.g., sEH inhibitors, repaglinide, retinoids).
- **TFDA prescribing information**: Retrieve and review the full package insert to complete the blocking safety gap (DG001) before any regulatory or clinical planning can proceed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

