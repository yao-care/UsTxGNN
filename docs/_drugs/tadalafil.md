---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 1192
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Tadalafil: From a Marketed PDE5 Inhibitor to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a marketed oral PDE5 inhibitor with 20 U.S. authorizations, but the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**.
There are **0 clinical trials** and **0 publications** for this pair, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the provided data (approved indication text is empty for all listed licenses) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tadalafil is a PDE5 inhibitor, which raises cGMP. No established link exists between this pathway and hair-follicle development.

Ambras syndrome is a rare genetic condition caused by a chromosomal rearrangement, not by a cGMP-related disorder. The very high score (0.9998) most likely reflects the shared hypertrichosis and hair-phenotype cluster in the knowledge graph, not a causal pathway.

The prediction is therefore a statistical association only. Other predicted entries show the same pattern: hypertrichosis, isolated genetic hair shaft abnormality and familial isolated trichomegaly. For hypertrichosis, the graph may encode an adverse-effect neighborhood rather than a treatment target. Vasodilator-associated hypertrichosis is known (e.g., minoxidil), but it works through a different mechanism (K-ATP channel opening).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For reference, one lower-ranked prediction (malformation syndrome with odontal and/or periodontal component) returned 20 publications. They are general periodontitis literature, and none of the titles mention tadalafil or PDE5 inhibition. They are not evidence for this drug.

---

## Other Predicted Indications (All Prediction-Only)

| Rank | Predicted Indication | TxGNN Score | Trials / Publications | Note |
|------|------|------|------|------|
| 2 | Hypertrichosis (disease) | 99.98% | 0 / 0 | Direction unclear; may reflect adverse-effect association |
| 3 | Malformation syndrome with odontal and/or periodontal component | 99.97% | 0 / 20 (not drug-specific) | Retrieved literature is a poor fit |
| 4 | Syndrome with a Dandy-Walker malformation as major feature | 99.97% | 0 / 0 | Structural defect; no mechanistic rationale |
| 5 | Isolated genetic hair shaft abnormality | 99.96% | 0 / 0 | Gene-driven structural defect |
| 6 | Familial isolated trichomegaly | 99.65% | 0 / 0 | Hair-phenotype cluster |
| 7 | Kyphoscoliotic heart disease | 99.43% | 0 / 0 | Only conceivable rationale (pulmonary hypertension and right heart strain) |
| 8 | Migraine with brainstem aura | 99.08% | 0 / 0 | Caution: headache and migraine are known PDE5 inhibitor adverse effects |

---

## US Market Information

Five of the 20 authorizations are shown. The approved indication text is empty in the provided data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA205885 | Tadalafil | Tablet, film coated | Teva Pharmaceuticals, Inc. |
| ANDA209654 | Tadalafil | Tablet | Preferred Pharmaceuticals Inc. |
| ANDA209654 | Tadalafil | Tablet | NuCare Pharmaceuticals, Inc. |
| ANDA210609 | Tadalafil | Tablet | Preferred Pharmaceuticals Inc. |
| ANDA210609 | Tadalafil | Tablet | NuCare Pharmaceuticals, Inc. |

All listed products are oral tablets.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight predictions are at Evidence Level L5 (model prediction only), with no trials and no drug-specific publications. The top-ranked predictions have no plausible link to PDE5/cGMP signaling. Two entries also raise concerns: hypertrichosis may be an adverse-effect association, and migraine is a known adverse effect of this drug class.

**To proceed, the following is needed:**
- Original indication and mechanism of action data for tadalafil (DrugBank query)
- Package insert warnings and contraindications (blocking for S1 safety screening)
- A drug-specific literature and trial search (tadalafil or PDE5 inhibitor plus each target disease), since the current search returned only disease-term literature
- For kyphoscoliotic heart disease, a dedicated evidence search on the pulmonary hypertension pathway, as the only mechanistically conceivable candidate
- A check of prediction direction (therapeutic vs. adverse-effect association) for the hypertrichosis and migraine entries

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

