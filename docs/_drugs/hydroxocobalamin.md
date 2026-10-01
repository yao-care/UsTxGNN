---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 779
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Vitamin B12 Deficiency and Cyanide Poisoning to Esophageal Varices with Bleeding

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, used for B12 deficiency and cyanide poisoning.
The TxGNN model predicts it may be effective for **esophageal varices with bleeding** (and the non-bleeding variant), but there are currently **0 clinical trials** and **0 publications** supporting this direction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US licence data (generally used for vitamin B12 deficiency and cyanide poisoning) |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (1 NDA, 1 ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hydroxocobalamin is a vitamin B12 form used for B12 deficiency and cyanide poisoning. It has no known effect on portal hypertension or variceal hemorrhage, and no established mechanistic link to this indication was found.

One purely speculative route is that hydroxocobalamin scavenges nitric oxide and hydrogen sulfide, both implicated in splanchnic vasodilation in portal hypertension. No supporting data were available for this hypothesis.

The very high TxGNN score should be interpreted cautiously. The bleeding and non-bleeding varices indications received an identical score (99.23%), which suggests a knowledge-graph neighbourhood artifact rather than a drug-specific signal. Standard care for these conditions (non-selective beta-blockers, endoscopic band ligation) works through unrelated mechanisms. The prediction also cannot be cross-checked against known pharmacology, because original indication and mechanism data are missing from the input.

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
| ANDA085998 | Hydroxocobalamin (Actavis Pharma, Inc.) | Injection, solution | Not listed in the source data |
| NDA022041 | Cyanokit (BTG International Inc.) | Injection, powder, lyophilized, for solution | Not listed in the source data |

Both products are injectable.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or publications, no established mechanistic link, and the identical scores for the two varices indications point to a likely knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text (currently blocking safety screening)
- Mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic evidence for the nitric oxide / hydrogen sulfide scavenging hypothesis in portal hypertension
- A literature and trial search using variceal bleeding and portal hypertension terms
- Route and formulation compatibility assessment (injectable products only)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

