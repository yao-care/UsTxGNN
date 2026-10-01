---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 1176
evidence_level: L5
indication_count: 1
---

# Sorbitol
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

# Sorbitol: From Osmotic Laxative and Irrigant Use to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is a sugar alcohol (polyol) marketed in the US as a bladder irrigation solution, an oral solution and a dental product ingredient. The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The high score most likely reflects knowledge-graph proximity, not a therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the US license records (all approved indication text is blank) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.40% (model rank 13,663) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license records (only one has an NDA number) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sorbitol. It is a polyol used as an osmotic laxative, sweetener and pharmaceutical excipient. Its use in a bladder irrigant is consistent with an osmotic, non-metabolized solute role. No efficacy in any disease resembling the predicted indication has been documented in the data provided.

Malignant hyperthermia is a pharmacogenetic disorder of skeletal muscle calcium handling, typically involving RYR1 or CACNA1S variants. The standard treatment is dantrolene. Nothing in sorbitol's known pharmacology connects it to this pathway.

**No credible mechanistic link is established.** The score of 0.994 most likely reflects proximity in the knowledge graph, such as shared carbohydrate-metabolism neighbors or excipient-related associations. It is not evidence of benefit. Any hypothesis, such as an osmotic or metabolic effect on muscle, would be speculative and unsupported by the provided data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017863 | Sorbitol (Baxter Healthcare Corporation) | Irrigant | Not specified in record |
| M007 | GeriCare Sorbitol Solution (Geri-Care Pharmaceuticals, Corp) | Liquid | Not specified in record |
| Not available | Plaque identifying (Shenzhen Yagao Technology Co., Ltd.) | Powder, dentifrice | Not specified in record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for sorbitol in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanism. Sorbitol is not known to act on muscle calcium regulation, and an established treatment (dantrolene) already exists. This is most likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Mechanism of action data for sorbitol, and a testable hypothesis linking it to malignant hyperthermia pathophysiology
- Preclinical evidence (for example, a muscle contracture test or RYR1 model) showing any effect
- FDA package insert warnings and contraindications, which are required before any safety screening
- Approved indication text for the listed products, to confirm the original indication
- A route-compatibility assessment, since the marketed forms (irrigant, oral liquid, dentifrice) do not match a plausible treatment route for this condition

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

