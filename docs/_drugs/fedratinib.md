---
layout: default
title: Fedratinib
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib (brand name Inrebic) is an oral kinase inhibitor marketed in the US. It is generally known as a JAK2 inhibitor for myelofibrosis, though the supplied license data does not state the indication.
The TxGNN model predicts it may be effective for **benign PEComa**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelofibrosis (from general knowledge; the supplied license data lists no approved indication text) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Fedratinib is a kinase inhibitor, and the evidence pack refers to JAK2/FLT3 inhibition as its known targets.

The link to the predicted disease is weak. PEComa biology centers on mTOR pathway activation (TSC1/TSC2 loss), and no direct connection to JAK2/FLT3 inhibition is established in the supplied data. The high score (99.84%) most likely reflects similarity in the knowledge graph rather than a validated mechanism. Any mechanistic link would be speculative.

The top-ranked predictions show the same pattern:

- **PEComa-family and mTOR-driven diseases** (lymphangiomyoma, uterine PEComa, lymphangioleiomyomatosis): mTOR inhibitors are the established approach, and nothing supplied links fedratinib to this pathway.
- **Rhabdoid tumor, familial rhabdoid tumor and dermatofibrosarcoma protuberans:** these are driven by SMARCB1 loss or PDGFR signaling, with no documented link to the drug's targets.
- **Hemophagocytic lymphohistiocytosis (HLH)** (infection-associated and malignancy-associated): these have the most plausible rationale, because JAK-STAT-driven cytokine storm makes JAK inhibition a reasonable hypothesis. They are labeled "Research Question", but still have no fedratinib-specific evidence. Their identical scores suggest a shared graph neighborhood rather than independent support.
- **Familial Mediterranean fever:** a JAK-inhibitor rationale via cytokine signaling is conceivable but unsupported.

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
| NDA212327 | Inrebic (Celgene Corporation) | Capsule (oral) | Not listed in the supplied data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no clinical trials or literature. The mechanistic link between JAK2/FLT3 inhibition and mTOR-driven PEComa is speculative. Safety data and mechanism of action are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), to allow safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic evidence connecting fedratinib to PEComa biology, or a decision to prioritize the HLH-related predictions, which have a more plausible JAK-STAT rationale
- A literature and trial search for class-level JAK inhibitor evidence, with evidence graded separately from fedratinib-specific data

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

