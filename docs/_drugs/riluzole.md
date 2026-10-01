---
layout: default
title: Riluzole
parent: Model Prediction Only (L5)
nav_order: 1124
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis (ALS) to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a marketed oral drug. The supplied literature identifies it as an established ALS therapy, although the US license records contain no indication text.
The TxGNN model predicts it may be effective for **bilateral parasagittal parieto-occipital polymicrogyria**, a rare cortical malformation.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a graph-based signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US license data; the literature describes riluzole as an ALS treatment |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Riluzole is generally understood to reduce glutamate release and excitotoxicity and to inhibit voltage-gated sodium channels. The supplied ALS literature supports glutamate excitotoxicity as a disease mechanism (e.g., PMID 9178165).

For this prediction, no clear mechanistic link was identified. Polymicrogyria is a developmental cortical malformation, and glutamate modulation and sodium-channel effects have no established relevance to it. The high TxGNN score reflects graph proximity in the knowledge graph, not biological or clinical support.

By contrast, several lower-ranked predictions are motor neuron disorders (lower motor neuron syndrome, monomelic amyotrophy, Mills syndrome, ALS subtypes). These are more plausible by analogy to ALS, but none has trials or disease-specific literature in the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204048 | Riluzole (Ascend Laboratories) | Tablet | Not listed |
| ANDA091417 | Riluzole (Sun Pharmaceutical Industries) | Tablet, film coated | Not listed |
| Not available | Teglutik (EDW Pharma) | Liquid | Not listed |
| ANDA091394 | Riluzole (Glenmark Pharmaceuticals) | Tablet, film coated | Not listed |
| ANDA206045 | Riluzole (AvKARE) | Tablet, film coated | Not listed |

Eight authorizations are recorded in total; five are shown. Routes are oral (tablet, film-coated tablet) and a liquid formulation.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials or literature and no plausible mechanistic link to riluzole's pharmacology, so it stays at Evidence Level L5. The supplied data do not justify moving it forward.

**To proceed, the following is needed:**
- Any disease-specific mechanistic, preclinical, or clinical evidence for polymicrogyria. Absent that, this candidate should be deprioritized.
- The FDA package insert (warnings, contraindications, approved indication), which is currently missing and blocks safety screening.
- Mechanism of action data from DrugBank.
- Route and formulation compatibility assessment, which is still pending.
- A closer look at the ALS-related predictions instead. The ALS entry (rank 8) is not a true repurposing case, since riluzole is a known ALS therapy. It is graded L4 only because the supplied data contain reviews and no ALS approval or pivotal RCTs, and adding those would likely raise it to L1.
- For the ALS type 22 entry (rank 10), rerun the literature search with the corrected disease name ("amyotrophic"), because the source spelling ("amyotrohpic") may have blocked matching.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

