---
layout: default
title: Oritavancin
parent: Model Prediction Only (L5)
nav_order: 995
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: From Acute Bacterial Skin Infections to Bacteroidaceae Infectious Disease

## One-Sentence Summary

Oritavancin is an injectable lipoglycopeptide antibiotic marketed in the US, and its labeled use is for Gram-positive skin and soft-tissue infections.
The TxGNN model predicts it may be effective for **Bacteroidaceae infectious disease**, but **0 clinical trials** and **0 publications** support this direction.
The prediction rests on the model score alone and is biologically questionable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute bacterial skin and skin structure infections (the supplied license records do not list indication text; this reflects general knowledge of the product labeling) |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Oritavancin is a lipoglycopeptide that inhibits cell wall synthesis in Gram-positive bacteria and disrupts their membranes.

The predicted indication is hard to reconcile with that mechanism. Bacteroidaceae are Gram-negative anaerobes, and their outer membrane normally blocks glycopeptides from reaching their target. The high score (0.995) is most likely a graph-proximity artifact in the knowledge graph. It should not be read as a clinical signal without in vitro susceptibility data.

The other two top predictions are weaker still:
- **Ophthalmic herpes zoster (score 99.03%):** this is a viral disease, and oritavancin has no recognized antiviral target.
- **Mycoplasma pneumoniae pneumonia (score 99.01%):** Mycoplasma lacks a cell wall, so a cell-wall-targeting agent is expected to be ineffective. This is a mechanistic contradiction, not just a gap in the data.

All three predictions are Evidence Level L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA214155 | Kimyrsa (Melinta Therapeutics, LLC) | Injection, powder, lyophilized, for solution | — |
| NDA206334 | Orbactiv (Melinta Therapeutics, LLC) | Injection, powder, lyophilized, for solution | — |

Both products are injectable only. No drug interactions were found in the queried data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trial or literature support (L5), and the known mechanism argues against it. Oritavancin acts on Gram-positive cell walls, while Bacteroidaceae are Gram-negative anaerobes protected by an outer membrane. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- In vitro susceptibility (MIC) data for oritavancin against Bacteroidaceae isolates
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Indication text for the two NDAs, to confirm the original indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

