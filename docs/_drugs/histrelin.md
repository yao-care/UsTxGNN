---
layout: default
title: Histrelin
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
---

# Histrelin
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

# Histrelin: From a GnRH Agonist Implant (Original Indication Not Recorded) to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Histrelin is a GnRH agonist marketed in the US as the SUPPRELIN implant. The source data does not record its original indication.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction appears to be a knowledge-graph artifact rather than a biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Histrelin is a GnRH agonist. Sustained receptor stimulation desensitizes the pituitary and suppresses LH/FSH and downstream sex steroids.

That mechanism does not fit this indication well. Ambras syndrome is a congenital hair disorder linked to chromosome 8q22 rearrangements affecting TRPS1 regulation. It is not driven by the pituitary-gonadal axis, so GnRH suppression has no clear target.

The very high TxGNN score (0.9999) most likely reflects graph-neighbor effects, with hair-related diseases clustering near the drug in the knowledge graph. It does not reflect a real therapeutic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022058 | SUPPRELIN | Implant | Not provided in the source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature, and no plausible mechanism. It is a model-only signal (L5) and should not be pursued.

Among the other predictions for this drug, only **idiopathic central precocious puberty** (rank 10, L3) has histrelin-specific literature. It consists of a pharmacology review, a single-surgeon implant series, and a reproductive axis follow-up study, with no RCTs. This is a well-established GnRH agonist use, so it may already be a labeled indication rather than true repurposing. **Central precocious puberty 1** (rank 6, L4) also has a strong mechanistic fit but no direct evidence of its own.

**To proceed, the following is needed:**
- The approved indication text for NDA022058, to establish the original indication and check whether the precocious puberty entries are already on-label
- Package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A recommendation to re-center this report on the idiopathic central precocious puberty prediction, since the rank 1 hypertrichosis prediction has no supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

