---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 1224
evidence_level: L5
indication_count: 1
monitor_inn: "THREONINE"
predicted_indications: ["gastroparesis (disease)"]
---

# Threonine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Threonine: From No Recorded Original Indication to Gastroparesis

## One-Sentence Summary

Threonine is an essential amino acid. In the data compiled for this report, no approved original indication is recorded for it.
The TxGNN model predicts it may be relevant to **Gastroparesis**, but the support is the model score alone: **0 clinical trials** and **0 publications** were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the only US license has no indication text) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketing) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Threonine is an essential amino acid and a precursor of glycine and serine. It is also a major component of intestinal mucins. No original indication is recorded, so the relationship between an original and a new indication cannot be established.

A link to gastric or intestinal mucosal function, or to enteric neurotransmission, is conceivable. However, it is speculative and has no supporting clinical or literature evidence in the data compiled for this report. The high score (0.993) may reflect proximity within the knowledge graph rather than a true therapeutic effect. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | L-Threonine High (Professional Complementary Health Formulas) | Liquid | Not stated; status: cancelled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): phenylketonuria and disorders of phenylalanine metabolism.
- **Drug Interactions**: No interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no literature, no verified mechanism, and no active US marketing authorization. This evidence is at L5, the lowest level.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example, from DrugBank), to test a link between threonine and gastric motility or mucosal function
- A literature and trial search specific to threonine and gastroparesis, including preclinical studies
- Route and formulation compatibility assessment, since only one cancelled liquid product exists
- A review of the knowledge-graph contraindication signals (phenylketonuria and phenylalanine metabolism disorders) for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

