---
layout: default
title: Activated Charcoal Aesculus Hippocastanum Flower A
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Aesculus Hippocastanum Flower A
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

# Multi-Component Biological Complex: No Repurposing Candidate Identified

## One-Sentence Summary

This submission describes a 15-component mixture combining conventional biologics (Canakinumab, anti-IL-1α rabbit immunoglobulin), botanical extracts (Arnica montana, Atropa belladonna, Hamamelis virginiana, and others), and animal-derived tissues (pork liver, Sus scrofa vein and intestinal mucosa).
No TxGNN repurposing prediction has been generated for this formula, and no original approved indication exists in any of the queried databases.
Without a predicted target indication and with critical data gaps across all evaluation dimensions, a full repurposing evaluation **cannot be completed** at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no approved indication on record |
| Predicted New Indication | None — TxGNN returned no prediction for this formula |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and even this is absent) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

No TxGNN prediction was generated for this formula, so no mechanistic reasoning for a new indication can be offered. Several structural observations help explain why the pipeline produced no output:

**Complexity of the input formula.** The submission lists 15 heterogeneous active ingredients spanning activated charcoal, homeopathic botanicals (Arnica, Belladonna, Nux-vomica, Podophyllum, Paeonia, Hamamelis, Hydrocotyle, Melissa), animal-derived tissues (pork liver, Sus scrofa vein and intestinal lymphoid follicle), and two immunological agents (anti-IL-1α rabbit immunoglobulin G and Canakinumab). The TxGNN knowledge graph is built around single-drug or small-combination entities; a 15-ingredient heterogeneous mixture typically cannot be resolved to a single DrugBank node, which is why `drugbank_id` is null and no KG traversal was possible.

**Presence of a recognised biologic within the mixture.** Canakinumab (Novartis Ilaris®) is a well-characterised fully human anti-IL-1β monoclonal antibody approved for cryopyrin-associated periodic syndromes (CAPS), Still's disease, and gouty arthritis. Were Canakinumab evaluated as a standalone agent, a repurposing analysis would be feasible and likely informative. Its co-listing with homeopathic and botanical ingredients prevents individual DrugBank mapping.

**No MOA data for the composite formula.** Because the components span mechanistic categories (adsorption, anti-inflammatory, adrenergic, cholinergic, alkaloid-mediated), a unified mechanism-of-action narrative for the combination is not available. This is a blocking data gap for the repurposing scoring step.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combined formula.

---

## Literature Evidence

Currently no related literature available for this combined formula as a single entity.

---

## US Market Information

This formula has no NDA or marketing authorisation in any queried jurisdiction. No licence table can be displayed.

> Note: Canakinumab as a standalone biologic holds FDA approval under the brand name **Ilaris®** (NDA/BLA 125319). If the intent of this submission is to evaluate Canakinumab for repurposing, it should be submitted as a separate single-agent Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. The following specific concerns apply to individual components within this formula and should be reviewed before any clinical use:

- **Atropa belladonna** (Belladonna): contains atropine and scopolamine; anticholinergic toxidrome risk at non-homeopathic doses.
- **Strychnos nux-vomica seed**: contains strychnine; glycine antagonist with narrow therapeutic index; seizure risk at supratherapeutic doses.
- **Podophyllum peltatum root**: precursor class to podophyllotoxin (etoposide); cytotoxic potential at non-dilute concentrations.
- **Canakinumab**: immunosuppression risk; contraindicated in active infection; requires pre-treatment tuberculosis screening per approved labelling.
- **Animal-derived tissues** (pork liver, Sus scrofa vein, intestinal lymphoid follicle): allergenicity and prion-safety documentation required for any regulated product submission.

No drug–drug interaction data were returned for this formula as a composite query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pipeline cannot generate a repurposing signal for a 15-ingredient heterogeneous mixture with no DrugBank node, no approved indication, and no TxGNN prediction output. Proceeding to clinical evaluation without decomposing the formula is not warranted.

**To proceed, the following is needed:**

1. **Decompose the formula into evaluable units** — Submit each pharmacologically active component (especially Canakinumab and anti-IL-1α immunoglobulin) as separate Evidence Pack queries to generate individual TxGNN predictions.
2. **Clarify regulatory intent** — Determine whether this is intended as a homeopathic product (different regulatory pathway) or a combination biologic/pharmaceutical (requiring full CMC and efficacy data).
3. **Obtain DrugBank IDs** — At minimum for Canakinumab (DB09035) and any other components with defined molecular targets, to enable KG traversal.
4. **Resolve MOA for the composite** — If the combination formula is the intended candidate, a unified pharmacological rationale must be documented linking all 15 components to a shared therapeutic hypothesis.
5. **Safety documentation** — Obtain Taiwan TFDA package insert data (DG001) and complete contraindication/warning review for components with known narrow therapeutic indices (Belladonna, Nux-vomica, Podophyllum).
6. **Source qualification for animal tissues** — Sus scrofa-derived materials require TSE/prion risk assessment documentation per international biologics standards (Ph.Eur. 5.2.8, FDA 21 CFR 610.13).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

