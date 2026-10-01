---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 805
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: From Radiographic Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic, iodinated radiographic contrast agent marketed in the US as OMNIPAQUE.
The TxGNN model predicts it may be effective for **insomnia**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Radiographic contrast imaging (the approved indication text is not listed in the source records) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iohexol is an iodinated contrast agent used to enhance X-ray and CT imaging. It has no known pharmacological activity at sleep-related targets.

No plausible mechanistic link between iohexol and insomnia has been identified. The very high TxGNN score (99.87%) is a model output only. It is most likely a knowledge-graph artifact rather than a real biological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018956 | OMNIPAQUE (GE Healthcare Inc.) | Injection, solution; Solution | Not listed in the source records |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for iohexol in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction has no clinical, literature, or mechanistic support and sits at evidence level L5 (model prediction only). Iohexol is an inert contrast agent, so there is no basis to advance this indication.

The second-ranked prediction, anxiety, has 6 retrieved trials and 6 publications, but none tests iohexol as a treatment. Iohexol appears in them only as a contrast or kidney-function measurement agent, so this prediction is also unsupported.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, currently a blocking gap for safety screening
- Mechanism of action data (e.g., from DrugBank) to test for any link to sleep regulation
- Any preclinical or clinical study of iohexol in insomnia; none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

