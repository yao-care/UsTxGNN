---
layout: default
title: Metreleptin
parent: Model Prediction Only (L5)
nav_order: 920
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: From Generalized Lipodystrophy to Familial Generalized Lentiginosis

## One-Sentence Summary

Metreleptin (brand name Myalept) is a recombinant leptin analog, originally used to treat leptin deficiency in generalized lipodystrophy.
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**, a rare pigmentary skin disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leptin deficiency in generalized lipodystrophy (the license records in the Evidence Pack contain no indication text) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both under BLA125390) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, metreleptin is a recombinant analog of human leptin. It replaces missing leptin in patients with generalized lipodystrophy, and this replacement is its established use.

No mechanistic link to familial generalized lentiginosis has been established. This is a pigmentary genodermatosis with no known involvement of the leptin pathway. The high score (0.997) reflects proximity in the knowledge graph, not biological or clinical evidence.

The other top-ranked predictions show the same pattern. They are mostly rare pigmentary or syndromic disorders (gastrocutaneous syndrome, Moynahan syndrome, acromelanosis and others) plus a few tumors (rhabdoid tumor, adrenal adenoma, schwannoma). All are L5 with no trials or literature. Two of them have identical scores, which suggests a shared graph neighborhood rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The Evidence Pack contains no approved-indication text for either license, so the manufacturer is shown instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125390 | Myalept | Lyophilized powder for injection (solution) | Amryt Pharmaceuticals Designated Activity Company |
| BLA125390 | Myalept | Lyophilized powder for injection (solution) | Chiesi USA, Inc. |

The only available route is injectable.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or literature, and no plausible leptin-related mechanism. Leptin's growth-promoting effects also raise a theoretical concern for the tumor candidates in the list.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A literature and trial search that finds any biological link between leptin signaling and the predicted disease
- Route compatibility and similarity-to-original-indication assessments (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

