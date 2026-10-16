---
layout: default
title: Risdiplam
parent: Model Prediction Only (L5)
nav_order: 1127
evidence_level: L5
indication_count: 1
monitor_inn: "RISDIPLAM"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
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

# Risdiplam: From Spinal Muscular Atrophy to Acne

## One-Sentence Summary

Risdiplam is an SMN2 pre-mRNA splicing modifier that is known as a treatment for spinal muscular atrophy, though the US license records compiled for this report do not list an indication text.
The TxGNN model predicts it may be effective for **acne**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on a model score alone and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (based on general knowledge of the drug; the license records contain no indication text) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the records show no currently valid license) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, risdiplam is a small-molecule modifier of SMN2 pre-mRNA splicing and is used for spinal muscular atrophy. That mechanism is not obviously related to acne.

No plausible link to acne biology can be established from the available data. Acne involves sebaceous gland activity, *Cutibacterium acnes* colonization, follicular hyperkeratinization and inflammation, and nothing here connects risdiplam to these processes.

The high score (rank 12,794 among predictions) may reflect knowledge-graph topology, such as shared gene or pathway neighbors, rather than a true biological relationship. Any link remains hypothetical and unverified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213535 | EVRYSDI | Powder, for solution | Not listed in the records (status: cancelled) |
| NDA219285 | EVRYSDI | Tablet | Not listed in the records (status: cancelled) |

Both authorizations are held by Genentech, Inc. and are recorded as cancelled. The records should be checked against the current FDA database before any conclusion is drawn about market availability.

## Cytotoxicity

Omitted. Risdiplam is not an antineoplastic drug.

## Safety Considerations

- **Drug Interactions**: Two moderate-level interactions were identified (DDInter):
  - Metformin
  - Methylnaltrexone

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no identifiable mechanistic link to acne. Package insert safety data and mechanism data are also missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to test whether any link to acne biology exists
- Confirmation of current US marketing status, since both NDAs are recorded as cancelled
- Preclinical or mechanistic evidence that risdiplam acts on acne-relevant pathways
- A route-of-administration assessment for acne, since oral and solution forms are the only forms recorded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

