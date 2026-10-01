---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is an oral nonsteroidal androgen receptor antagonist, an established therapy for prostate cancer.
The TxGNN model predicts it may be relevant to **prostate cancer/brain cancer susceptibility**, a composite disease term.
This top-ranked prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (established use of flutamide; the license records list no indication text) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both are ANDA075298, listed twice) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Flutamide blocks the androgen receptor, so the prostate cancer half of this term is mechanistically plausible. The DrugBank mechanism-of-action field is missing from the input, so this rests on flutamide's known pharmacology rather than a retrieved MOA record.

The predicted term is a composite "susceptibility" entry, not a treatable disease. Nothing in the input links androgen receptor blockade to the brain cancer component. The score of 0.9998 comes from the knowledge graph alone, with no clinical or literature support to confirm it.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific prediction.

## Literature Evidence

Currently no related literature available for this specific prediction.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075298 | Eulexin (Waylis Therapeutics LLC) | Capsule (oral) | Not stated in the records |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal antiandrogen), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (see the hepatotoxicity warning below); other items per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Key Warnings**: The evidence pack's rationale notes a boxed hepatotoxicity warning for flutamide. The full warning text was not retrieved. The pack also says this warning makes exploratory use in other diseases unattractive.

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a composite susceptibility term with no trials, no literature and no clear mechanism for the brain cancer component. The score reflects graph proximity only.

**To proceed, the following is needed:**
- A clinically meaningful disease definition in place of the composite term
- Retrieval of the full package insert (warnings, contraindications)
- DrugBank mechanism-of-action data
- A review of the other predictions, which have more support:
  - **Male reproductive organ cancer (rank 6):** the input lists many prostate cancer androgen-suppression trials, but flutamide arms are unconfirmed. This is effectively flutamide's existing prostate cancer use, not true repurposing. It is rated L2, Proceed with Guardrails.
  - **Benign reproductive system neoplasm (rank 4):** one human benign prostatic hyperplasia study (PMID 1722793) plus mostly pathology and mechanistic papers. It is rated L3, Research Question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

