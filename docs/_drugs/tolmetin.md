---
layout: default
title: Tolmetin
parent: Model Prediction Only (L5)
nav_order: 1240
evidence_level: L5
indication_count: 10
---

# Tolmetin
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

# Tolmetin: From an Oral NSAID to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tolmetin is an oral non-steroidal anti-inflammatory drug (NSAID) marketed in the US as tablets and capsules. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder. **No clinical trials and no publications** currently support this prediction, and the mechanistic link is implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed (approved indication text is empty for all three US licenses) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all are ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tolmetin is an NSAID that inhibits cyclooxygenase (COX), which reduces inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia related to CDMP1/GDF5. It affects skeletal development, and COX inhibition does not act on that pathway. The high TxGNN score most likely reflects proximity in the knowledge graph rather than real pharmacology, so this prediction should be treated as **not mechanistically supported**.

Other predictions for tolmetin are more plausible but are still not evidence-backed:
- **Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis** (score 99.75%, L4) and **spondyloarthropathy, susceptibility to** (score 99.75%, L4). NSAIDs are used symptomatically in these conditions. That support comes from NSAID class knowledge, not from tolmetin-specific data.
- Juvenile arthritis may already be a labeled use, in which case it would not be true repurposing. Check the label before treating it as a candidate.
- **Myosclerosis** and **rheumatoid nodulosis** have only weak, speculative links through symptomatic anti-inflammatory effects.
- The remaining predictions (brachyolmia and related syndromes, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, WHIM syndrome) have no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074473 | Tolmetin Sodium (Atland Pharmaceuticals) | Tablet, film coated | Not listed |
| ANDA073393 | Tolmetin Sodium (Atland Pharmaceuticals) | Capsule | Not listed |
| ANDA074473 | Tolectin (Poly Pharmaceuticals) | Tablet, film coated | Not listed |

All products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a model score. It has no trials, no literature, no plausible mechanism, and a genetic skeletal disorder is not addressed by COX inhibition. Evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- The approved indications from the tolmetin label, to confirm the original use and whether juvenile arthritis is already labeled
- Mechanism of action data (for example from DrugBank)
- Consideration of juvenile idiopathic arthritis and spondyloarthropathy as separate research questions, with tolmetin-specific evidence searches

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

