---
layout: default
title: Diclofenac
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From a Marketed NSAID to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a marketed nonsteroidal anti-inflammatory drug (NSAID) that inhibits COX-1 and COX-2.
The TxGNN model ranks **hypotrichosis simplex of the scalp**, a rare hereditary hair-loss disorder, as its top prediction, but **0 clinical trials** and **0 publications** support it.
The score most likely reflects knowledge-graph proximity, not a biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Diclofenac is an NSAID, and its known pharmacology is COX inhibition, which reduces prostaglandin-mediated inflammation and pain.

The predicted disease is a rare hereditary hair-loss disorder, and COX inhibition has no established role in it. A link through prostaglandin D2 in hair-follicle inhibition has been proposed, but it is speculative and unsupported by any evidence here. The high score most likely comes from proximity in the knowledge graph, not from a biological rationale.

The same pattern appears in the other top-ranked predictions, such as skeletal dysplasias, other congenital hair disorders, and WHIM syndrome. None has a plausible mechanistic link or supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The table lists 5 of the 20 authorizations. The pack also shows oral, topical gel, extended-release and other forms across the full set.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA216275 | Diclofenac sodium | Film-coated tablet | Sportpharm LLC |
| ANDA215375 | Diclofenac potassium | Powder for solution | Camber Pharmaceuticals, Inc. |
| ANDA202769 | Diclofenac Sodium | Solution | Proficient Rx LP |
| ANDA075185 | Diclofenac Sodium | Delayed-release tablet | AvKARE |
| NDA022202 | ZIPSOR | Liquid-filled capsule | Assertio Therapeutics, Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism, so it is a computational signal only (L5).
Among the top 10 predictions, only juvenile idiopathic arthritis has any evidence (L3). That evidence is two small studies from 1983 and 1988, and it may reflect established NSAID use rather than true repurposing. It is a better candidate for follow-up, though it is not the top-ranked one.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are missing and block safety screening
- Mechanism of action data from DrugBank
- Original indication data, which was empty in the Evidence Pack, to be verified against US labelling
- Mechanistic or preclinical evidence linking COX or prostaglandin signalling to hair-follicle biology, before any further work on this indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

