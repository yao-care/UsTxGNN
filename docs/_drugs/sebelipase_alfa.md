---
layout: default
title: Sebelipase Alfa
parent: Model Prediction Only (L5)
nav_order: 1146
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

Sebelipase alfa (KANUMA) is a recombinant human lysosomal acid lipase used as enzyme replacement therapy for lysosomal acid lipase deficiency (LAL-D).
The TxGNN model ranks **Scheie syndrome** as its top predicted new indication, but this is a graph-based signal only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal acid lipase deficiency (LAL-D). The license record has no indication text; this comes from the published literature. |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125561) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. From the literature, sebelipase alfa replaces the missing lysosomal acid lipase enzyme. This clears the cholesteryl esters and triglycerides that build up in lysosomes in LAL-D.

Scheie syndrome is a mild form of MPS I, caused by a deficiency of a different enzyme, alpha-L-iduronidase. Sebelipase alfa does not replace that enzyme and acts on different substrates. The only shared feature is that both are lysosomal storage disorders.

The high score (0.998) therefore reflects patterns in the knowledge graph rather than a plausible mechanism. No trial or publication supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125561 | KANUMA (Alexion Pharmaceuticals, Inc.) | Injection, solution, concentrate | Not stated in the source record. The literature describes it as approved for LAL-D. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Scheie syndrome prediction has no trials or literature, and sebelipase alfa does not replace the enzyme that is deficient in this disease. The score alone is not enough to justify further work.

Other predictions in the same Evidence Pack are stronger, but they are on-label uses rather than new repurposing findings:
- **Cholesteryl ester storage disease** (rank 4): L1, supported by the Phase 3 ARISE RCT (NCT01757184). This is the established LAL-D indication, so it validates the model rather than repurposing the drug. Recommendation: Proceed with Guardrails.
- **Wolman disease** (rank 5): L3, supported by cohorts and case reports. It is the infantile form of LAL-D. Recommendation: Proceed with Guardrails.

**To proceed, the following is needed:**
- A disease-matched mechanistic rationale for Scheie syndrome, or a decision to deprioritize it.
- The approved indication text and package insert warnings and contraindications for BLA125561.
- Detailed mechanism of action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

