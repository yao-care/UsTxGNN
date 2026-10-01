---
layout: default
title: Linaclotide
parent: Model Prediction Only (L5)
nav_order: 861
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Linaclotide: From Its Approved Use to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide is an orally administered, gut-acting drug marketed in the US as Linzess. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a model prediction only: **0 clinical trials** and **0 publications** support it so far.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all under NDA202811) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack, and no original indication text was recorded. From general pharmacology, linaclotide is a locally acting guanylate cyclase-C agonist. It raises cGMP in the intestine and speeds transit, and very little of it is absorbed into the body.

The only plausible link to cauda equina syndrome is indirect. The syndrome can cause neurogenic bowel dysfunction, including constipation, and linaclotide could relieve that symptom. It would not treat the underlying nerve compression or nerve injury. The very high TxGNN score is therefore best read as a graph-based signal, not as evidence of efficacy.

Two other predictions ranked lower, and both look even weaker:
- **Obsolete neurogenic bladder (99.89%)**: No direct mechanistic link is evident. The disease term is marked obsolete in the ontology, so the prediction may be an artifact shared with the cauda equina prediction.
- **Insomnia (99.51%)**: No plausible mechanistic link is identified. Linaclotide has negligible systemic exposure and no known central sleep-regulating activity, so this is likely a false positive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA202811 | Linzess | Capsule, gelatin coated (oral) | Allergan, Inc. |

The pack lists three license entries with the same number, product, and form, shown here once. No approved indication text was provided.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no publications, and only an indirect, symptom-level mechanistic link. Linaclotide is not expected to act on the nervous system, so the evidence does not yet justify moving forward (Evidence Level L5, stage S0).

**To proceed, the following is needed:**
- The package insert's warnings and contraindications, which are required before any safety screening
- Mechanism of action data and the original approved indications from DrugBank and the US label
- A literature and trial search for linaclotide in neurogenic bowel dysfunction related to cauda equina syndrome or spinal cord conditions
- A check on whether the obsolete neurogenic bladder term is an ontology artifact
- Route compatibility and similarity-to-original-indication analysis, both still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

