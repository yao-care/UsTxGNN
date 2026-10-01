---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 682
evidence_level: L5
indication_count: 1
---

# Ethosuximide
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

# Ethosuximide: From Absence Seizures to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ethosuximide is an anticonvulsant used for absence seizures. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this direction. The prediction is a model output only and has no mechanistic support in the available data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence seizures (from the drug's known use; the US license records do not list indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Ethosuximide is generally known as a T-type calcium channel (Cav3.x) blocker used for absence seizures.

NSIAD is caused by gain-of-function variants in *AVPR2* (for example R137C or R137L). These make the vasopressin V2 receptor constitutively active. The result is higher cAMP, aquaporin-2 insertion into the membrane, and hyponatremia even though vasopressin is undetectable.

Nothing in the provided data links T-type calcium channel blockade to V2 receptor signaling or AQP2 trafficking. The very high TxGNN score is a knowledge-graph proximity signal only. Anticonvulsants as a class are more often associated with causing hyponatremia or SIADH-like effects than with treating them, so even the direction of any effect is unclear. The prediction is more likely a graph artifact, such as shared hyponatremia or antidiuresis neighbors, than a rational hypothesis.

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
| ANDA210654 | Ethosuximide (Epic Pharma, LLC) | Capsule | Not listed in the source record |
| ANDA200892 | Ethosuximide (Chartwell RX, LLC) | Capsule | Not listed in the source record |
| ANDA200892 | Ethosuximide (Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc.) | Capsule | Not listed in the source record |
| NDA012380 | Zarontin (Parke-Davis Div of Pfizer Inc) | Capsule | Not listed in the source record |
| ANDA080258 | Zarontin (Parke-Davis Div of Pfizer Inc) | Solution | Not listed in the source record |

The record lists 11 licenses in total. The table shows the first 5. Forms on the market include oral capsules, liquid-filled capsules and solution.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no registered trials or publications, and the available data show no plausible link between T-type calcium channel blockade and the V2 receptor and AQP2 pathway underlying NSIAD. The class association with hyponatremia also raises doubt about the direction of any effect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- A literature and trial search for ethosuximide in hyponatremia, SIADH or NSIAD, including any preclinical evidence
- A mechanistic rationale connecting Cav3.x blockade to V2 receptor or AQP2 signaling, and a check on the direction of effect, before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

