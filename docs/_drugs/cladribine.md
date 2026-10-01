---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 533
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cladribine: From an Established Antimetabolite to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a marketed deoxyadenosine analog, known mainly for activity in lymphoid cells.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US license data |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Based on general pharmacology, cladribine is a deoxyadenosine analog that is most active in lymphoid cells. Its efficacy in lymphoid malignancies is established, but the supplied data give no plausible mechanistic link to embryonal rhabdomyosarcoma, a mesenchymal solid tumor.

The high score is more likely a knowledge-graph artifact than an independent signal. The top six predictions for cladribine are all rhabdomyosarcoma subtypes (vaginal botryoid, extrahepatic bile duct, prostate and others). They share one graph neighborhood, so they do not confirm one another.

A seventh prediction, liver sarcoma, has one indirect publication. It is a 2004 report of cladribine in smoldering systemic mastocytosis, a hematologic neoplasm, so it does not support efficacy in sarcoma.

If this direction is pursued, a preclinical check should come first, for example dCK and 5'-nucleotidase expression in rhabdomyosarcoma models.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210856 | Cladribine | Injection, solution | Hisun Pharmaceuticals USA, Inc. |
| ANDA218425 | Cladribine | Tablet | Genvion Corporation |
| ANDA076571 | Cladribine | Injection | Fresenius Kabi USA, LLC |
| ANDA075405 | Cladribine | Injection | Hikma Pharmaceuticals USA Inc. |
| ANDA218425 | Cladribine | Tablet | Apotex Corp. |

Approved indication text was not supplied for any license. The data lists 6 licenses in total but details only 5. Both injectable and oral tablet forms are marketed.

## Cytotoxicity

This section is based on general drug-class knowledge, since the Evidence Pack contains no toxicity data. Please refer to the package insert warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog) |
| Myelosuppression Risk | High (expected for this class; confirm against the label) |
| Emetogenicity Classification | Low (confirm against the label) |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature. The supplied data show no mechanistic link between cladribine and rhabdomyosarcoma, and the high score likely reflects clustering of related subtypes in the knowledge graph. Package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (DG001, blocking)
- Mechanism of action data from DrugBank (DG002)
- Preclinical evidence in rhabdomyosarcoma models (dCK and 5'-nucleotidase expression, cell-line sensitivity)
- Approved indication text for the US licenses, to establish the original-indication baseline
- A literature and trial search specific to cladribine in rhabdomyosarcoma or other pediatric solid tumors

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

