---
layout: default
title: Lurbinectedin
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: From Small Cell Lung Cancer to Multiple Endocrine Neoplasia

## One-Sentence Summary

Lurbinectedin (ZEPZELCA) is a cytotoxic oncology drug marketed in the US for small cell lung cancer. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the graph model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung cancer (the approved indication text is blank in the US license record; this comes from the evidence pack's mechanism notes) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lurbinectedin is an alkylating agent that binds the DNA minor groove and inhibits RNA polymerase II-driven transcription. It is marketed for small cell lung cancer, which is a neuroendocrine-type tumor.

Because of that neuroendocrine link, activity in endocrine or neuroendocrine tumors is conceivable. The link is **indirect and speculative**. No trial or literature evidence was retrieved for multiple endocrine neoplasia syndromes, and the score is a graph prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213702 | ZEPZELCA (Jazz Pharmaceuticals, Inc.) | Injection, powder, lyophilized, for solution | — |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, DNA minor groove binder) |
| Myelosuppression Risk | High (marked myelosuppression noted in the evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential); please also refer to the package insert |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were retrieved. The only safety signal in the evidence pack is marked myelosuppression, which is a particular concern in immunocompromised patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score (Evidence Level L5). The mechanistic link is speculative, no clinical trials or publications were found, and safety data have not been obtained. The other nine ranked predictions (HIV, rheumatoid arthritis, ALS, CMV and others) are also L5 and Hold. Four of them are veterinary or animal-model diseases, which suggests knowledge-graph artifacts.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication text), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence in multiple endocrine neoplasia or other neuroendocrine tumors
- A review of the myelosuppression risk against the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

