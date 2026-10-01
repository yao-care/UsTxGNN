---
layout: default
title: Benzphetamine
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
---

# Benzphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Benzphetamine: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

Benzphetamine is a sympathomimetic amine appetite suppressant, marketed in the US for short-term management of obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The prediction should be treated as a likely knowledge-graph artifact until independent evidence appears.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Short-term obesity management (the US license records list no indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all listed under ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general pharmacology, benzphetamine is a sympathomimetic amine anorectic. It is used for weight reduction, and nothing in its known pharmacology relates to vitamin excess.

**No plausible mechanistic link to hypervitaminosis was identified.** Treating vitamin toxicity generally means stopping the vitamin source and giving supportive care. It does not involve an appetite-suppressing agent. The high score (0.9998) reflects proximity in the knowledge-graph embedding, not a demonstrated biological or clinical rationale.

The other top-ranked predictions show the same pattern:

- **Proximal 16p11.2 microdeletion syndrome:** This syndrome is associated with obesity, so the graph link probably reflects a shared phenotype rather than a disease-modifying effect. A sympathomimetic in a neurodevelopmental genetic syndrome would also raise safety concerns.
- **Hypertelorism (flagged obsolete in the ontology) and frontorhiny:** These are congenital craniofacial malformations that a pharmacological anorectic cannot plausibly treat. Both predictions rest on embedding proximity alone.

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
| ANDA090968 | Benzphetamine hydrochloride (Calvin Scott & Co., Inc.) | Tablet | Not provided in source record |
| ANDA090968 | Benzphetamine hydrochloride (PD-Rx Pharmaceuticals, Inc.) | Tablet | Not provided in source record |
| ANDA090968 | Benzphetamine hydrochloride (Bryant Ranch Prepack) | Tablet | Not provided in source record |
| ANDA090346 | Benzphetamine hydrochloride (Epic Pharma, LLC) | Film-coated tablet | Not provided in source record |
| ANDA090968 | Benzphetamine hydrochloride (KVK-TECH, INC) | Tablet | Not provided in source record |

All products are oral tablets.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support (evidence level L5). Benzphetamine's pharmacology has no plausible connection to vitamin excess. Its use in the other predicted conditions is either implausible or carries safety concerns.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- A plausible biological rationale linking benzphetamine to hypervitaminosis, or independent evidence that supports it
- A check of whether the top predicted diseases are valid targets. One is flagged obsolete in the ontology, and the others look like phenotype-association artifacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

