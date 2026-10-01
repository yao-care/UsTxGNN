---
layout: default
title: Cevimeline
parent: Model Prediction Only (L5)
nav_order: 517
evidence_level: L5
indication_count: 4
---

# Cevimeline
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

# Cevimeline: From an Oral Muscarinic Agonist to Hypertrichosis

## One-Sentence Summary

Cevimeline is an oral muscarinic (M1/M3) agonist marketed in the US as capsules.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** specific to this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (US labeling is generally for dry mouth, but this is not confirmed by the input) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Cevimeline is understood to be a muscarinic M1/M3 receptor agonist that stimulates glandular secretion.

Cholinergic signaling in hair follicle biology is a speculative link. No direct mechanism connecting muscarinic agonism to hair growth or to hypertrichosis has been established. The high score most likely reflects network proximity in the knowledge graph rather than a pharmacological rationale. Hypertrichosis is also a phenotype (often congenital or drug-induced) that is not obviously treatable by a secretagogue, and a "treatment" direction is unclear.

The other top predictions are weaker still:

| Rank | Predicted Disease | Score | Comment |
|------|------|------|------|
| 2 | Ambras type hypertrichosis universalis congenita | 99.08% | Rare genetic disorder, no plausible pharmacologic link. Score probably inherited from the parent hypertrichosis node. |
| 3 | Malformation syndrome with odontal and/or periodontal component | 99.07% | Only weak, indirect link (increased salivary flow might support oral health). Does not address a developmental malformation. |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.06% | Congenital posterior fossa defect, no plausible mechanism. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hypertrichosis.

The 20 publications retrieved for the rank 3 candidate (periodontal malformation syndrome) are general periodontitis reviews and guidelines, for example the EFP S3 guideline on stage IV periodontitis (PMID 35688447) and a Cochrane review on periodontitis and glycaemic control (PMID 35420698). None concern cevimeline, so they are background only and not drug-specific evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020989 | cevimeline hydrochloride (Cosette Pharmaceuticals) | Capsule | Not listed |
| NDA020989 | Evoxac (Cosette Pharmaceuticals) | Capsule | Not listed |
| ANDA216682 | Cevimeline Hydrochloride (Bryant Ranch Prepack) | Capsule | Not listed |
| ANDA215056 | Cevimeline Hydrochloride (Aurobindo Pharma) | Capsule | Not listed |
| ANDA091591 | Cevimeline Hydrochloride (Hikma Pharmaceuticals USA) | Capsule | Not listed |

Only the oral capsule route is recorded. 15 authorizations exist in total, and 5 are shown.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph score, with no clinical trials, no drug-specific literature, and no plausible mechanistic link. Hypertrichosis and the other top predictions (congenital or developmental syndromes) are not credible targets for muscarinic agonism.

**To proceed, the following is needed:**
- Mechanism of action data (for example, via DrugBank) to test any cholinergic–hair follicle hypothesis
- Package insert warnings and contraindications for safety screening
- Preclinical or mechanistic evidence linking muscarinic signaling to hair growth
- Confirmation of the approved indication text from US labeling
- A clear definition of the intended therapeutic goal, since hypertrichosis is typically treated by reducing hair growth

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

