---
layout: default
title: Sonidegib
parent: Model Prediction Only (L5)
nav_order: 1174
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Sonidegib (Odomzo) is an oral Hedgehog pathway inhibitor, used for advanced basal cell carcinoma (BCC).
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**, but this prediction currently has **0 clinical trials** and **0 publications** behind it. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal cell carcinoma (from general knowledge; the license record has no indication text) |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on general knowledge, sonidegib inhibits Smoothened (SMO), a key transducer of Hedgehog signaling. Aberrant Hedgehog activation is the main driver of BCC, and this is the basis for sonidegib's use there.

A subset of medulloblastomas is also driven by Hedgehog signaling, so the link is biologically plausible. However, the input contains no trials or literature for this indication. The prediction rests on the graph-based score and general pathway knowledge alone. The input also does not say whether the extensive-nodularity subtype is Hedgehog-dependent, so subtype-level applicability is unconfirmed.

Other predictions for this drug have more support. For "skin cancer", the input lists a completed randomized Phase 2 trial in advanced BCC (NCT01327053, n=230) and its 42-month follow-up (PMID 31545507). That evidence concerns BCC, which is likely on-label, and does not transfer to medulloblastoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205266 | Odomzo (Sun Pharmaceutical Industries, Inc.) | Capsule (oral) | Not listed in the input |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; class toxicities to watch include musculoskeletal effects |
| Handling Protection | Please refer to the package insert; embryo-fetal risk is a known class concern for SMO inhibitors |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. The prediction is model-only, with no trials or publications for medulloblastoma with extensive nodularity. The Hedgehog rationale is plausible but unverified for this subtype. The package insert has not been reviewed, so safety screening cannot start.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (obtain and parse the FDA label)
- Mechanism of action data from DrugBank
- Preclinical or clinical data on SMO inhibition in Hedgehog-driven medulloblastoma, especially the nodular subtype
- Assessment of pediatric use and embryo-fetal toxicity risk, since medulloblastoma commonly occurs in children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

