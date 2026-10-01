---
layout: default
title: Povidone
parent: Model Prediction Only (L5)
nav_order: 1072
evidence_level: L5
indication_count: 1
---

# Povidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Povidone: From Ophthalmic Lubricant Use to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Povidone (PVP) is a synthetic polymer, widely used as a pharmaceutical excipient. In the US it is marketed in eye-lubricant products such as iVIZIA Dry Eye and Rohto.
The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**, a rare inherited skin-scaling disorder.
Currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is recorded in the source data. The marketed products are eye-lubricant and dry-eye products. |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Povidone is mainly used as a binder, film former and solubilizer in pharmaceutical products. Its iodine complex, povidone-iodine, is a topical antiseptic. In the marketed products listed here, povidone acts as a lubricant for the eye surface.

Congenital ichthyosiform erythroderma is a genetic keratinization disorder. It is typically linked to variants in genes such as *TGM1*, *ALOXE3* and *ALOX12B*, and causes impaired skin barrier function and scaling. Povidone has no known action on these pathways. The only speculative links are nonspecific:

- a topical film-forming or humectant effect;
- antiseptic control of secondary skin infection, if used as povidone-iodine.

Neither would change the course of the disease, and no data in this record support either.

The high score (0.991, model rank 19,302) comes from knowledge-graph topology, not from clinical or literature evidence. It may partly reflect a graph artifact, because povidone is a highly connected excipient node. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M018 | iVIZIA Dry Eye | Solution/drops | Thea Pharma Inc. |
| M018 | iVIZIA Lubricant Eye Gel | Gel | Thea Pharma Inc. |
| M018 | Rohto | Liquid | The Mentholatum Company |
| M018 | Rohto Dry-Aid | Liquid | The Mentholatum Company |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (L5). Povidone has no known mechanism that would act on the biology of congenital ichthyosiform erythroderma. The high model score is likely inflated by povidone's position as a common excipient in the knowledge graph.

**To proceed, the following is needed:**
- Mechanism of action data for povidone, and a plausible link to keratinization or skin-barrier pathways
- A literature and trial search for povidone or PVP in ichthyosis or related genetic skin disorders
- Package insert warnings and contraindications, which are required before any safety screening
- Confirmation of whether a suitable topical formulation exists, since the current US products are ophthalmic

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

