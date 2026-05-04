---
layout: default
title: Acer Rubrum Pollen Acer Saccharinum Pollen Acer Sa
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 0
---

# Acer Rubrum Pollen Acer Saccharinum Pollen Acer Sa
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

# Multi-Component Tree Pollen Allergen Extract: Drug Repurposing Assessment Report

---

## One-Sentence Summary

This product is a 21-component tree pollen allergen extract spanning eight genera (maple, alder, birch, paper mulberry, hickory, mulberry, poplar, and elm), formulated for use in allergen-specific immunotherapy for seasonal allergic disease.
The TxGNN model did not generate any repurposing predictions for this compound, and the product has no current market authorization in Taiwan.
Without prediction output or supporting evidence, a formal drug repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established in this Evidence Pack (likely seasonal allergic rhinitis via immunotherapy) |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no model prediction, no supporting studies |
| US Market Status | Not marketed in Taiwan |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Can't a Standard Prediction Be Made?

This compound is a **multi-allergen extract mixture** composed of 21 distinct tree pollen antigens across eight genera:

| Genus | Common Name | Species Included |
|-------|-------------|-----------------|
| *Acer* | Maple | *A. rubrum*, *A. saccharinum*, *A. saccharum* |
| *Alnus* | Alder | *A. rhombifolia*, *A. rubra*, *A. serrulata* |
| *Betula* | Birch | *B. lenta*, *B. nigra*, *B. populifolia* |
| *Broussonetia* | Paper Mulberry | *B. papyrifera* |
| *Carya* | Hickory | *C. alba*, *C. glabra*, *C. laciniosa*, *C. ovata* |
| *Morus* | Mulberry | *M. alba*, *M. rubra* |
| *Populus* | Poplar/Cottonwood | *P. balsamifera*, *P. deltoides* subsp. *deltoides*, *P. deltoides* subsp. *monilifera* |
| *Ulmus* | Elm | *U. americana*, *U. pumila* |

These are characteristic **North American springtime tree pollens** — the combination profile is consistent with subcutaneous allergen immunotherapy (SCIT) or sublingual immunotherapy (SLIT) products for seasonal allergic rhinitis and/or allergic asthma.

Allergen immunotherapy works through a distinct biological mechanism: repeated allergen exposure gradually shifts immune response from **Th2-mediated allergic inflammation** (IgE, IL-4, IL-5, IL-13) toward **Th1/Treg-mediated tolerance** (IgG4, IL-10, TGF-β). Because this product consists of whole-antigen biological extracts rather than a single small molecule or biologic with a defined receptor target, standard TxGNN knowledge-graph-based repurposing — which relies on molecular-level interaction mapping — is not directly applicable in its current form.

Currently, detailed mechanism of action data is not available. The Evidence Pack returns no DrugBank ID, no original_moa, and no predicted_indications. Without a TxGNN prediction score, no repurposing hypothesis can be formally evaluated.

---

## US Market Information

No products from this compound have been registered in Taiwan (0 licenses, market status: Not marketed).

> **Note:** Allergen extract products in the United States are regulated as **biologics** under the Public Health Service Act and licensed via a Biologics License Application (BLA), not a standard NDA. They would not appear in typical NDA databases. Corresponding records should be verified through the FDA's Biologics Approvals database or the CBER product list.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Known class-level safety considerations for allergen immunotherapy products include: risk of local injection-site reactions, risk of systemic allergic reactions including anaphylaxis (particularly in subcutaneous formulations), and contraindication in patients with severe or unstable asthma. These are general class observations and do not replace product-specific labeling review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for this compound contains no TxGNN-predicted indications, no market authorization data, and no retrievable safety or MOA data. The compound's multi-allergen biological nature also limits direct applicability of small-molecule repurposing models. There is currently no basis on which to evaluate a novel indication hypothesis.

**To proceed, the following is needed:**

- **Clarify regulatory pathway**: Confirm whether this product should be evaluated as a biologic (BLA/CBER pathway) rather than a small-molecule drug (NDA). TxGNN pipeline may need to be bypassed or supplemented for biological allergen extracts.
- **Resolve DrugBank mapping**: Obtain individual DrugBank entries for component allergen proteins (e.g., Bet v 1 for birch, Aln g 1 for alder). Individual allergen proteins may have separate DrugBank records.
- **Obtain original indication documentation**: Retrieve the FDA-approved labeling for an equivalent licensed allergen extract product to confirm the intended indication (seasonal allergic rhinoconjunctivitis, allergic asthma).
- **Retrieve safety data**: Download and parse the package insert to identify black box warnings, contraindications, and special population restrictions.
- **Re-run TxGNN with resolved identifiers**: If individual allergen components can be mapped to DrugBank IDs, re-submit to the TxGNN prediction pipeline separately.
- **Consider immunology-specific evidence sources**: Standard repurposing evidence from ClinicalTrials.gov and PubMed should be searched using component allergen names (e.g., "birch pollen immunotherapy", "alder pollen allergy") rather than the combined INN string.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

