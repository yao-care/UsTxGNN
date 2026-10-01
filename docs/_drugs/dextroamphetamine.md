---
layout: default
title: Dextroamphetamine
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 7
---

# Dextroamphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Dextroamphetamine: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Dextroamphetamine is a central nervous system stimulant marketed in the US, and the literature in the Evidence Pack describes it as approved for attention deficit hyperactivity disorder (ADHD) and narcolepsy.
The TxGNN model ranks **faciodigitogenital syndrome** as its top prediction, but there are **0 clinical trials** and **0 publications** for this pairing, so the score is a graph-model output with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD and narcolepsy (taken from the literature in the pack; the US license records have no indication text) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total US licenses, including ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Dextroamphetamine is a CNS stimulant that increases synaptic dopamine and norepinephrine by promoting their release and blocking reuptake. This is how it improves attention and reduces hyperactivity in ADHD.

Faciodigitogenital syndrome is a rare developmental disorder. **No plausible mechanistic link to dextroamphetamine was identified.** The score of 0.9999 comes from the graph model alone. It is not backed by any trial, publication or known pharmacology, so it should not be read as a therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The source data lists 20 US licenses. The five main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090533 | Zenzedi | Tablet | Azurity Pharmaceuticals, Inc. |
| ANDA210059 | Dextroamphetamine Sulfate | Tablet | Bryant Ranch Prepack |
| ANDA203644 | Dextroamphetamine | Solution | Bryant Ranch Prepack |
| ANDA212160 | Dextroamphetamine Sulfate | Tablet | Winder Laboratories LLC |
| NDA215401 | XELSTRYM | Extended-release patch | Noven Therapeutics, LLC |

Other available forms include extended-release capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature and no plausible mechanism, so it rests entirely on the graph score. It should not advance.

Other candidates in the pack, for context:
- **Specific developmental disorder** (rank 2, L2, Proceed with Guardrails) appears to be a proxy label for ADHD and related neurodevelopmental conditions. Its evidence reflects existing ADHD use, not new repurposing. A Phase 4 trial in ADHD with autism (NCT05916339) is recruiting.
- **Postural orthostatic tachycardia syndrome** (rank 6, L4, Hold) has only indirect literature and a possible cardiovascular safety concern.
- **Trichotillomania** (rank 7, L4, Hold) shows an adverse-event signal, with new-onset cases reported during stimulant treatment. It does not support repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any independent evidence linking dextroamphetamine to faciodigitogenital syndrome; without it, further work on this prediction is not justified
- For the rank 2 label, confirmation of the exact target condition (for example ADHD, learning disorder, or ADHD with autism) before it is treated as a new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

