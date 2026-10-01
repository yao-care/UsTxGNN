---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic diuretic that is widely marketed in the US as an injectable solution. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but this prediction has **0 clinical trials** and only **1 general review** behind it, and that review does not study mannitol. The prediction is a model output without supporting evidence, and the pack's own mechanistic analysis argues against it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the label data provided (mannitol is generally known as an osmotic diuretic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% (model rank 1472) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (NDA and ANDA authorizations combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. In general, mannitol is an osmotic diuretic. It raises the osmolarity of the fluid in the kidney tubules, which draws water into the urine.

NSIAD is a gain-of-function disorder of the vasopressin V2 receptor. It causes the body to retain water and leads to low blood sodium (hyponatremia). Mannitol works independently of vasopressin signaling, so it does not act on the cause of NSIAD.

**The prediction is therefore not mechanistically supported.** The only citation is a general review of pitfalls in evaluating hyponatremia, and it does not assess mannitol as a treatment. The high score most likely reflects the drug's proximity to hyponatremia and other osmotic agents in the knowledge graph, not a real therapeutic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes ten common pitfalls in evaluating hyponatremia and the risks of under- or over-treating it. It does not evaluate mannitol. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016269 (Henry Schein, Inc.) | Mannitol | Injection, solution | Not stated in the provided data |
| ANDA080677 (Fresenius Kabi USA, LLC) | Mannitol | Injection, solution | Not stated in the provided data |
| ANDA080677 (ProPharma Distribution) | Mannitol | Injection, solution | Not stated in the provided data |
| NDA016269 (Hospira, Inc.) | Mannitol | Injection, solution | Not stated in the provided data |
| NDA020006 (B. Braun Medical Inc.) | Mannitol | Injection, solution | Not stated in the provided data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no trials, the single citation does not test mannitol, and mannitol's mechanism does not target the V2 receptor defect behind NSIAD. The other nine predicted indications in the pack are also rated Hold, at L4 or L5.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications), so safety screening can begin
- Mechanism of action data from DrugBank
- A targeted literature search for any direct evidence of mannitol use in NSIAD or hyponatremia due to excess antidiuresis
- Evidence that mannitol's osmotic diuresis can benefit this disease at all, given the concern that it does not address V2 receptor gain of function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

