---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 643
evidence_level: L5
indication_count: 2
---

# Eflornithine
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

# Eflornithine: Predicted New Indication, Esotropia (Model Prediction Only)

## One-Sentence Summary

Eflornithine is an oral tablet marketed in the US (Iwilfin, NDA215500). The evidence pack does not include its approved indication text.
The TxGNN model predicts it may be effective for **esotropia**, with a second, weaker candidate of **neurotrophic keratopathy**.
Currently there are **0 clinical trials** and **0 publications** supporting either prediction, so this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level mechanism field is empty in the input. The candidate-level rationale describes eflornithine as an irreversible inhibitor of ornithine decarboxylase (ODC), the rate-limiting enzyme in polyamine synthesis.

**Esotropia** is an eye-alignment disorder driven by extraocular muscle, neural control, or refractive factors. It has no established polyamine-dependent mechanism, so no credible mechanistic link to ODC inhibition was identified. The very high score (99.85%) may reflect knowledge-graph topology artifacts rather than real pharmacology. The drug's original indication is also missing from the input, which limits any independent plausibility check.

**Neurotrophic keratopathy** (rank 2, score 99.38%) has only a speculative, indirect link. Polyamines contribute to epithelial proliferation and wound healing, so a corneal role for the ODC pathway is conceivable. However, ODC inhibition would be expected to suppress epithelial proliferation and migration, which could impair rather than promote corneal healing. The disease stems from impaired trigeminal corneal innervation, and its approved treatments target nerve growth factor signaling, not polyamine synthesis. The direction of effect is unresolved and potentially unfavorable.

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
| NDA215500 | Iwilfin (USWM, LLC) | Tablet (oral) | Not provided in the input |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions are supported only by model scores, with no trials, no literature, and no credible mechanistic link. For neurotrophic keratopathy, the expected effect of ODC inhibition on corneal healing may even be unfavorable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication and detailed mechanism of action for the drug
- A literature and trial search, including preclinical work on polyamine/ODC biology in ocular alignment and corneal healing
- An assessment of whether an oral tablet is a suitable route for the proposed ocular indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

