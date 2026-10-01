---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Bacterial Infections to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic that blocks bacterial cell-wall synthesis. The US license record does not list an approved indication, so the original use is inferred from the drug class.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **0 clinical trials** and **0 publications** support this prediction.
The high score is unsupported and biologically implausible (see below), so it should be treated as a model artifact until proven otherwise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license record (fosfomycin is an antibacterial) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA, an enzyme in the first step of bacterial cell-wall synthesis. The drug record itself has no mechanism of action entry, so this comes from the evaluation's own rationale. It explains why fosfomycin works against many bacteria, especially in the urinary tract.

The prediction is **not mechanistically reasonable**. *Ureaplasma* has no cell wall, so a drug that blocks cell-wall synthesis is not expected to kill it. Ureaplasma urethritis is usually treated with agents that act on protein synthesis rather than the cell wall. The TxGNN score of 99.99% most likely reflects a similarity to other urethritis or urinary infections in the knowledge graph, not a real biological link.

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
| NDA 212271 | Contepo (Meitheal Pharmaceuticals Inc.) | Injection, powder, for solution | Not listed in the record provided |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There is no trial or literature support, and *Ureaplasma* lacks the cell wall that fosfomycin targets. There is no reason to advance this indication.

**To proceed, the following is needed:**
- In-vitro susceptibility data for fosfomycin against *Ureaplasma* species, which would be the minimum bar to justify any further work
- The package insert warnings and contraindications for the US product, which are currently missing
- A mechanism of action entry for the drug record
- The approved indication text for NDA 212271

**Note on other predictions for this drug:** Some other predicted indications in the Evidence Pack have far stronger support. Pyelitis (acute pyelonephritis and complicated urinary tract infection) is backed by the ZEUS phase 2/3 randomized trial (PMID 30861061) and is graded L1. Gonococcal urethritis has one 2016 randomized trial (PMID 27064136) and is graded L2. Both should be evaluated in their own reports. They are closer to extensions of fosfomycin's existing use than true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

