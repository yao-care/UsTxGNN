---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 1
---

# Brinzolamide
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

The txgnn-pipeline skill is about pipeline management, not report generation — the detailed format is already defined in the system prompt. Proceeding directly to generate the report.

---

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a carbonic anhydrase inhibitor (CAI), FDA-approved since 1998 under the brand name Azopt, used to lower intraocular pressure in open-angle glaucoma and ocular hypertension by reducing aqueous humor production.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, the top-ranked repurposing candidate with a score of **99.48%**.
However, **no clinical trials** and **no publications** specifically investigating Brinzolamide in this genetic glaucoma subtype were identified, leaving support at the mechanistic inference level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Intraocular hypertension (FDA-approved 1998, brand: Azopt) ⚠️ Data gap: US regulatory records absent from this Evidence Pack |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 |
| US Market Status | Not marketed (data gap — Azopt is in fact FDA-approved; records absent from source query) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the known pharmacology included in the repurposing rationale, Brinzolamide is a **Carbonic Anhydrase Inhibitor (CAI)** that acts by inhibiting carbonic anhydrase isoforms II and XII in the ciliary body, thereby reducing aqueous humor formation and directly lowering intraocular pressure (IOP).

Primary hereditary glaucoma is a genetically driven condition — most commonly caused by mutations in *MYOC*, *CYP1B1*, or *LTBP2* — whose defining downstream pathology is **chronically elevated IOP leading to progressive optic nerve damage**. This is precisely the endpoint Brinzolamide addresses. The mechanistic overlap is therefore not incidental but direct: regardless of the upstream genetic trigger, Brinzolamide targets the final common pressure pathway.

Indirect class-effect evidence further reinforces this prediction. Related CAIs — Dorzolamide (topical) and Acetazolamide (systemic) — are already documented as adjunctive therapies in congenital and hereditary glaucoma management. The TxGNN model's knowledge graph likely captures this drug–disease relationship density, which is reflected in the 99.48% prediction score (rank 12,267 of model outputs). The absence of specific clinical trials for Brinzolamide in primary hereditary glaucoma most likely reflects the rarity of this subtype and the precedent for off-label CAI use rather than mechanistic doubt.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US NDA records were returned by the data pipeline for Brinzolamide. This represents a known data gap: Brinzolamide (Azopt®, Alcon) received FDA approval in 1998 for the treatment of elevated intraocular pressure in patients with ocular hypertension or open-angle glaucoma. Downstream pipeline queries should re-run against the FDA Orange Book and Drugs@FDA to recover the correct NDA record before advancing this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently at L4 (mechanistic inference and class-effect analogy only) with no clinical trials or publications directly linking Brinzolamide to primary hereditary glaucoma; while the IOP-lowering mechanism is highly plausible for this indication, regulatory and safety data are also missing from this Evidence Pack, making formal advancement premature.

**To proceed, the following is needed:**

- **Regulatory record recovery**: Re-query FDA Orange Book / Drugs@FDA to restore the correct Azopt NDA record, confirm approved labeling, and extract current prescribing warnings and contraindications
- **MOA documentation**: Retrieve full pharmacodynamic/pharmacokinetic profile from DrugBank (DB01194) including carbonic anhydrase isoform selectivity data
- **Literature sweep — class effect**: Conduct a targeted PubMed search for Dorzolamide or Acetazolamide in primary hereditary / congenital glaucoma to establish class-level L3 evidence that can contextualise this prediction
- **Genetic subtype mapping**: Clarify whether "primary hereditary glaucoma" in the TxGNN disease vocabulary maps to OMIM-defined entities (e.g., GLC1A/MYOC, GLC3A/CYP1B1) to enable more precise literature and trial matching
- **Safety profile extraction**: Parse the Azopt package insert for key warnings, contraindications, and drug–drug interactions to complete the S1 safety pre-screen
- **Exploratory case series search**: Search for any case reports or retrospective series of topical CAI use in genetically confirmed hereditary glaucoma patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

