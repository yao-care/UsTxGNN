---
layout: default
title: Polyethylene Glycol 3500
parent: Model Prediction Only (L5)
nav_order: 1060
evidence_level: L5
indication_count: 3
---

# Polyethylene Glycol 3500
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Polyethylene Glycol 3500: From Osmotic Laxative Use to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polyethylene glycol (PEG) 3500 is a non-absorbed osmotic laxative. The original indication is not recorded in the dataset.
The TxGNN model predicts it may be effective for **Congenital Ichthyosiform Erythroderma**, but there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data (the US license record has no indication text) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (the record is an ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. PEG 3500 is an osmotic laxative that is not absorbed from the gut. It acts by holding water in the intestinal lumen, and it has no known action on skin biology.

Congenital ichthyosiform erythroderma is a keratinization disorder with a defective epidermal barrier (for example, TGM1 or ALOX12B variants). No direct mechanistic link to an oral laxative is supported. The only plausible connection is indirect: PEGs are used as humectants and vehicles in topical emollients. That is a formulation role on a different route, not a repurposing signal for the oral drug.

The high score (0.997) most likely reflects proximity in the knowledge graph rather than a validated pharmacological effect. The other two top predictions, self-healing collodion baby (99.60%) and lamellar ichthyosis (99.38%), are also ichthyosis-type skin disorders. They likewise have no trials or publications, and the same reasoning applies. In neonates with a compromised skin barrier, systemic absorption of PEG through impaired skin is an additional unaddressed safety concern.

The data lists the ingredient as PEG 3500 while the US product is labeled PEG 3350. This naming difference should be confirmed.

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
| ANDA078915 | Polyethylene Glycol (3350) (Mylan Institutional Inc.) | Powder, for solution | Not specified in the data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (evidence level L5), and no mechanistic link is established between an oral, non-absorbed laxative and a keratinization disorder. Safety and mechanism data are also missing, so the candidate cannot advance past the initial stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism of action data and the original indication
- A literature and trial search on PEG in ichthyosis, to determine whether any signal concerns the active drug or only topical vehicles
- Route compatibility assessment, since the oral powder is not a topical formulation
- Safety assessment of PEG exposure in neonates with impaired skin barrier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

