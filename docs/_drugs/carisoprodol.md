---
layout: default
title: Carisoprodol
parent: Model Prediction Only (L5)
nav_order: 500
evidence_level: L5
indication_count: 1
---

# Carisoprodol
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

# Carisoprodol: From Muscle Relaxant Use to Insomnia

## One-Sentence Summary

Carisoprodol is a marketed oral tablet in the US, but the supplied record does not state its approved indication. The TxGNN model predicts it may be relevant to **insomnia**, but this is a model prediction only, with **0 clinical trials** and **1 publication** (a review that does not test carisoprodol for insomnia).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the record (all approved indication fields are empty) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L5 (the source record lists L4, but no mechanism or preclinical study is supplied, so L5 applies under the scoring rules) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs, i.e. generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Carisoprodol is a generic oral tablet, and its original indication is not recorded, so the link to insomnia cannot be drawn from the supplied data.

A plausible link comes from general pharmacology, not from the record. Carisoprodol is metabolized to meprobamate, and both are thought to modulate GABA-A receptors and cause sedation. That could explain why a knowledge graph associates the drug with sleep disturbance.

Sedation from a muscle relaxant is not the same as a proven treatment effect on insomnia. Carisoprodol is also known for dependence and abuse liability, CNS depression, and additive risk with other sedatives. Any move toward a sleep indication would have to weigh these risks heavily.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review | American Family Physician | Review of nocturnal leg cramps, which are common in adults and can cause severe insomnia. The available abstract text does not show that carisoprodol was tested for insomnia, so this is indirect and weak support. |

## US Market Information

The record lists 20 licenses in total; the 5 main ones are shown below. Approved indication text is empty for all of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040188 | Carisoprodol (Bryant Ranch Prepack) | Tablet | Not stated in record |
| ANDA040792 | Carisoprodol (Bryant Ranch Prepack) | Tablet | Not stated in record |
| ANDA040188 | Carisoprodol (Aphena Pharma Solutions - Tennessee, LLC) | Tablet | Not stated in record |
| ANDA040188 | Carisoprodol (REMEDYREPACK INC.) | Tablet | Not stated in record |
| ANDA040245 | Carisoprodol (Chartwell RX, LLC) | Tablet | Not stated in record |

## Safety Considerations

Please refer to the package insert for safety information. The record contains no warnings or contraindications, and the drug-interaction query returned no records. Neither should be read as evidence of safety.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.02%) is a model output, not clinical evidence. There are no registered trials, and the only publication is an indirect review on leg cramps. Safety and mechanism data are also missing, and the dependence and CNS-depression risks make a sleep indication a serious concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- The approved indication text, to define the original indication
- Direct clinical or preclinical evidence of carisoprodol or meprobamate in insomnia
- A dependence, abuse and sedative co-use risk assessment for any sleep-related use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

