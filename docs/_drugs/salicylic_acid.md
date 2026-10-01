---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 1143
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Salicylic Acid: From Topical Skin Care (Acne and Wart Products) to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is marketed in the US mainly as a topical skin-care ingredient, judging by product names such as acne pads, a wart remover patch, and a blemish-clearing foundation. The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the regulatory data. Product names suggest acne and wart use |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, salicylic acid is a topical keratolytic and anti-inflammatory agent, and salicylates as a class inhibit COX enzymes. Mechanistically, this could relate to an inflammatory ocular surface condition such as papillary conjunctivitis. This link is speculative and is not backed by any supplied study.

The route of use is also a concern. All 20 US products in the data are skin-care or topical forms (powder, patch, liquid, cream, gel, emulsion), and none is ophthalmic. The input contains no ocular safety data for salicylic acid, so its use near or in the eye cannot be supported.

The model's other top predictions are mostly rare genetic skeletal or developmental syndromes, such as brachyolmia, pseudoachondroplasia, and acromesomelic dysplasia. They have no plausible mechanistic link to salicylic acid and are likely knowledge-graph artifacts. Rosacea conjunctivitis (rank 5) and spondyloarthropathy susceptibility (rank 10) have only indirect conceptual plausibility. Papillary conjunctivitis is the most biologically plausible of the top 10 predictions, but it is still unsupported by evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The regulatory data lists no approved indication text for these products. The table shows 5 of the 20 authorizations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M006 | bareMinerals Blemish Rescue Skin-Clearing Loose Foundation | Powder | Orveon Global US LLC |
| M030 | Salicylic acid | Patch | Wal-Mart Stores Inc |
| M028 | REINREDE TAG WART REMOVER | Patch | Jiangxi Yudexi Pharmaceutical Co., LTD |
| M006 | Dermatouch Acnecare Pads | Liquid | Spa de Soleil |
| M030 | Salicylic Acid | Cream | SANSAR, LLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interactions were found in the queried data. The input also contains no ocular safety information for topical or systemic salicylate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no registered trials and no literature. The mechanistic link is speculative, and all marketed forms are non-ophthalmic skin products with no ocular safety data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Literature and trial searches specific to salicylates and conjunctivitis
- Ocular safety and route-compatibility assessment, since no ophthalmic formulation is currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

