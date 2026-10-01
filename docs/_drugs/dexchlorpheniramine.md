---
layout: default
title: Dexchlorpheniramine
parent: Model Prediction Only (L5)
nav_order: 592
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dexchlorpheniramine: From an Unspecified Original Indication to Allergic Urticaria

## One-Sentence Summary

Dexchlorpheniramine is a first-generation H1-antihistamine marketed in the US as oral liquid products. The provided data does not state its original approved indication.
The TxGNN model predicts it may be effective for **allergic urticaria** (and, as a second candidate, **cold urticaria**), but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it rests on model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided data (all license indication fields are empty) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on the drug class, dexchlorpheniramine is a first-generation H1-receptor antagonist (inverse agonist). In allergic urticaria, histamine released from mast cells drives the wheal-and-flare response, so blocking H1 receptors is mechanistically plausible. Antihistamines are also a standard therapy class for urticaria.

Because the original indication is not recorded, this prediction may not be true repurposing. Dexchlorpheniramine is labeled for urticaria in some markets, so this could be an existing indication. The provided data cannot confirm this either way.

The second-ranked prediction, **cold urticaria** (score 99.61%), is a chronic inducible urticaria in which cold exposure triggers mast-cell degranulation and histamine release. H1 antagonism is the plausible mechanism, and antihistamines are the usual first-line class. The score most likely reflects a shared H1-antihistamine class signal in the knowledge graph rather than drug-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202520 | Corphena (BluCrest Pharmaceuticals LLC) | Solution | Not stated in the data |
| ANDA202520 | RYCLORA (Carwin Pharmaceutical Associates, LLC) | Liquid | Not stated in the data |
| M012 | VanaCof 2 (GM Pharmaceuticals, Inc.) | Solution | Not stated in the data |

The first two products share the same authorization number in the source data, which should be checked against the FDA record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support is limited to a model prediction (L5), with no trials or literature for either predicted indication. The original indication and mechanism are also missing, so it is unclear whether allergic urticaria is a new use at all.

**To proceed, the following is needed:**
- The US package insert (approved indications, warnings, contraindications), to confirm whether urticaria is already labeled
- Mechanism of action data from DrugBank
- A targeted literature and trial search for dexchlorpheniramine in allergic urticaria and cold urticaria
- Route and formulation compatibility assessment for the predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

