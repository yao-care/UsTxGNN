---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is an NK1-receptor antagonist antiemetic. The label indication text was not supplied in the Evidence Pack, so this comes from general drug knowledge, and it is marketed in oral and injectable forms (including fosaprepitant and CINVANTI).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a very high score of 99.97%.
However, there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (general knowledge; not listed in the supplied licence data) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% (rank 1,274 in the model's overall ranking) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licences (NDA and ANDA combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the Evidence Pack. Aprepitant is generally known as a substance P/neurokinin-1 (NK1) receptor antagonist. Its efficacy in nausea and vomiting is well established, but that does not by itself explain a link to a renal water-handling disorder.

NSIAD is caused by activating mutations in the vasopressin V2 receptor gene (*AVPR2*). This leads to inappropriate water retention and hyponatraemia despite low vasopressin levels. No pathway from NK1 antagonism to this disease is evident in the supplied data.

The high score most likely reflects proximity in the knowledge graph rather than a drug-specific mechanism. **No mechanistic link is established at this stage.** The prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Five of the 20 authorisations are shown. Approved indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA214616 | Fosaprepitant | Lyophilized powder for injection | NorthStar Rx LLC |
| ANDA214616 | Fosaprepitant | Lyophilized powder for injection | Camber Pharmaceuticals, Inc. |
| ANDA209965 | Fosaprepitant | Lyophilized powder for injection | Dr. Reddy's Laboratories Inc. |
| ANDA207777 | Aprepitant | Capsule | Glenmark Pharmaceuticals Inc., USA |
| NDA209296 | CINVANTI | Injectable emulsion | Heron Therapeutics, Inc. |

Other dosage forms on the US market include powder for suspension and emulsion.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no documented mechanism, and the disease biology (activating *AVPR2* mutations) does not point to an NK1-antagonist pathway. Model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Mechanism-of-action data for aprepitant, plus preclinical evidence, if any, linking NK1 signalling to vasopressin V2 receptor activity or renal water handling
- The US package insert (warnings, contraindications, drug interactions), since safety data are currently missing
- A systematic literature and trial search using drug-specific terms (aprepitant or NK1 antagonist with NSIAD or hyponatraemia), because the current search returned nothing
- Route and dosing feasibility assessment, since route compatibility is still pending

For reference, two other candidates in the same pack are flagged as "Research Question" (pulmonary hypertension and subarachnoid haemorrhage). Both have a plausible NK1-related biological hypothesis but no supporting clinical evidence, and preclinical support would need to be verified first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

