---
layout: default
title: Undecylenic Acid
parent: Model Prediction Only (L5)
nav_order: 1275
evidence_level: L5
indication_count: 3
monitor_inn: "UNDECYLENIC ACID"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease", "pityriasis versicolor"]
last_modified_at: 2026-10-23
description: "Undecylenic Acid: predicted new indication Ectothrix infectious disease (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection"
---

# Undecylenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Undecylenic Acid: From Tinea Infections to Ectothrix Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Undecylenic acid is a topical fatty-acid antifungal, with tinea pedis, tinea corporis and related tinea infections recorded as its original uses in the knowledge graph.
The TxGNN model predicts it may be effective for **ectothrix infectious disease** (with endothrix infectious disease and pityriasis versicolor as further candidates),
but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection (relations recorded in the knowledge graph; the US licence records contain no indication text) |
| Predicted New Indication | Ectothrix infectious disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of NDAs | at least 3 |
| Number of approvals | At least 3 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Undecylenic acid is generally described as a fatty-acid antifungal that inhibits fungal morphogenesis and disrupts fatty acid and cell membrane function, but this could not be verified from the data compiled for this report.

Ectothrix infection is a dermatophyte infection in which the fungus forms spores on the outside of the hair shaft (for example *Microsporum* and *Trichophyton* species). The tinea infections linked to undecylenic acid are caused by the same group of organisms, which gives the prediction some biological plausibility.

There is an important practical limit. Hair-shaft and follicular infections usually require systemic therapy because topical agents penetrate poorly, so a topical-only product is unlikely to be adequate. The same applies, even more strongly, to the second prediction, endothrix infection (fungus growing inside the hair shaft).

The third prediction, **pityriasis versicolor** (TxGNN score 0.9901), is a superficial skin infection caused by *Malassezia* yeasts, not dermatophytes. It is more accessible to topical therapy, so it is the more testable hypothesis, for example through in vitro *Malassezia* susceptibility testing. Established topical azoles and selenium sulfide are already available, so any added value of undecylenic acid would need to be justified.

All three predictions are computational only.

| Predicted indication | TxGNN score | Evidence level | Trials / publications |
|------|------|------|------|
| Ectothrix infectious disease | 0.9908 | L5 | 0 / 0 |
| Endothrix infectious disease | 0.9903 | L5 | 0 / 0 |
| Pityriasis versicolor | 0.9901 | L5 | 0 / 0 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

At least 3 licences are on record; the list may be partial. None of the records contains approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M005 | ViLLsure Antifungal Pen | Liquid | Not stated in the record |
| part333C | CVS Pharmacy | Liquid | Not stated in the record |
| M002 | SFEIXE Antifungal Pen | Paste | Not stated in the record |

All three are single-ingredient products. Other dosage forms on record include cream and spray.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predictions rest on model scores alone, with no clinical trials or publications. The two leading predictions (ectothrix and endothrix infection) involve hair-shaft infections that topical products are unlikely to treat adequately. Pityriasis versicolor is the most plausible candidate to explore as a research question, but it is not yet supported by any evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data for undecylenic acid
- In vitro susceptibility data against *Malassezia* and hair-infecting dermatophytes
- A literature search for any clinical use in pityriasis versicolor or tinea capitis
- A justification of added value over existing topical azoles and selenium sulfide
- Confirmation of the approved indication wording on the US licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

