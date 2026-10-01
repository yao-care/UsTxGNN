---
layout: default
title: Magnesium Salicylate
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 10
---

# Magnesium Salicylate
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

# Magnesium Salicylate: From Oral Analgesic Products (Indication Not Listed) to Spondyloarthropathy, Susceptibility To

## One-Sentence Summary

Magnesium salicylate is a salicylate (NSAID-class) compound sold in the US in oral products, several named for back pain relief. The TxGNN model predicts it may be effective for **spondyloarthropathy, susceptibility to**, but **no clinical trials and no publications** currently support this prediction. It is a model-only signal (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the regulatory data (product names such as "Back Pain Relief" suggest pain relief) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 licenses (5 shown below) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium salicylate is a non-acetylated salicylate in the NSAID class. NSAIDs inhibit COX and prostaglandin synthesis and are used for pain and inflammation. Non-acetylated salicylates inhibit COX only weakly.

"Spondyloarthropathy, susceptibility to" describes a genetic susceptibility phenotype, not a directly treatable clinical condition. Any link to the drug would be indirect, through the class effect of NSAIDs on the symptoms of inflammatory spondyloarthritis. The score of 99.98% therefore should not be read as evidence of efficacy.

The other predicted indications do not clarify the picture:
- **Ankylosing spondylitis** (rank 5, score 99.96%) is the most clinically meaningful candidate. NSAIDs are established symptomatic therapy, so it is classed as L4 (a research question). However, no drug-specific trial or publication was supplied, and efficacy relative to standard NSAIDs is unproven.
- **Rare skeletal and developmental disorders** (for example brachyolmia, pseudoachondroplasia, acromesomelic dysplasia) show no plausible mechanism. These high scores most likely reflect knowledge-graph proximity between skeletal phenotypes, not pharmacology.

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
| M013 | Percogesic | Tablet, coated | Not listed |
| M013 | Maximum Strength Backache Relief | Capsule, coated | Not listed |
| M013 | Medique Back Pain Relief | Tablet, film coated | Not listed |
| part343 | Doans | Tablet | Not listed |
| M013 | Medique at Home Back Pain Relief | Tablet, film coated | Not listed |

All listed products are oral formulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials, no literature, and no confirmed mechanism. The top-ranked disease is a genetic susceptibility phenotype and cannot be treated directly. The only clinically plausible neighbour, ankylosing spondylitis, is supported only by the general NSAID class effect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data for magnesium salicylate
- The approved indication text for the US products
- A focused literature and trial search on magnesium salicylate in ankylosing spondylitis or axial spondyloarthritis, including a comparison against standard NSAIDs
- Route compatibility assessment (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

