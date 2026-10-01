---
layout: default
title: Tecovirimat
parent: Model Prediction Only (L5)
nav_order: 1204
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Smallpox to Hordeolum

## One-Sentence Summary

Tecovirimat (TPOXX) is an antiviral that targets orthopoxviruses, and the literature in the pack describes its US approval for smallpox.
The TxGNN model predicts it may be effective for **hordeolum** (a stye, a bacterial eyelid infection) with a high score of 99.66%.
There are **0 clinical trials** and **0 publications** supporting this prediction, and there is no plausible mechanistic link, so it should be treated as a model artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox (from the literature, PMID 30120738; the license records contain no indication text) |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Published literature (PMID 30120738) describes tecovirimat as inhibiting the orthopoxvirus VP37 (F13) envelope wrapping protein. This prevents the formation of egress-competent enveloped virions and limits viral spread within the host.

Hordeolum is a localized, usually staphylococcal bacterial infection of the eyelid. Tecovirimat is a narrow-spectrum antiviral with no known antibacterial activity, and its target is specific to orthopoxviruses. The high TxGNN score reflects graph-based association only and does not reflect a biological rationale, so the prediction is not considered reasonable.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208627 | TPOXX | Capsule (oral) | Not stated in the license record |
| NDA214518 | TPOXX | Injection, solution, concentrate (IV) | Not stated in the license record |

Both products are made by SIGA Technologies, Inc.

## Other Predicted Indications Worth Noting

Several lower-ranked predictions have far more support than hordeolum. They are shown here for context only.

| Predicted Indication | TxGNN Score | Pack Evidence Level | Comment |
|---------|------|------|------|
| Human infection by orthopoxvirus | 99.62% | L3 | Strong mechanistic fit and close to the smallpox label. About 20 publications, mostly reviews, an organoid model and case reports. PMID 40239067 (NEJM 2025, clade I mpox in the DRC) appears to be a randomized trial, but its abstract was not supplied. Its efficacy result should be verified. Other articles in the pack describe recent trial efficacy as unsatisfactory. |
| Vaccinia | 99.62% | L2 | Strong mechanistic fit. The three registered trials are an expanded-access protocol (no longer available), a Phase 2 JYNNEOS drug-vaccine interaction study (NCT04957485, active, not recruiting) and a different agent (NIOCH-14). None is a completed efficacy trial, so L2 looks generous by the stated rules. |
| Coinfection | 99.62% | L4 | Non-specific term. The literature is mpox coinfection case reports, not an independent signal. |

The remaining predictions (vibrio, Klebsiella, noma, pneumococcemia, phlebotomus fever, lumpy skin disease) have no supporting evidence.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hordeolum prediction has no trials, no literature and no mechanistic basis. Tecovirimat is an antiviral and hordeolum is a bacterial infection. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- Re-prioritize the candidate list toward orthopoxvirus infection and vaccinia, which have real evidence, rather than following the raw TxGNN rank.
- Retrieve and grade PMID 40239067 (abstract, trial phase, primary efficacy result) before any evidence-level upgrade.
- Obtain the FDA package insert (warnings, contraindications, drug interactions) and the official approved indication text for NDA208627 and NDA214518.
- Obtain formal mechanism-of-action data from DrugBank.
- Complete the route compatibility assessment (oral capsule and IV formulations are available).

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

