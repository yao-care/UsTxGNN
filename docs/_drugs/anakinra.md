---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From IL-1 Receptor Blockade to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra (marketed as Kineret) is a recombinant interleukin-1 (IL-1) receptor antagonist that is already marketed in the US.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA103950, a biologics license) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the rationale provided, anakinra blocks IL-1 receptor signaling.

Mastocytoma is a neoplastic proliferation of mast cells driven mainly by KIT. No mechanistic rationale connecting IL-1 blockade to this disease is evident from the data provided. The very high TxGNN score reflects a pattern in the knowledge graph, not biological or clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA103950 | Kineret | Injection, solution | Swedish Orphan Biovitrum AB (publ) |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data provided.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on model score alone: no trials, no literature, and no plausible IL-1 mechanism for a KIT-driven neoplasm.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking IL-1 signaling to mast cell neoplasms
- Mechanism of action data (DrugBank) and package insert warnings and contraindications (FDA)

**Other candidates in the same pack are better supported and worth prioritizing instead:**
- **Pyogenic autoinflammatory syndrome** (score 99.83%, L3, Research Question): PSTPIP1 mutations drive excess IL-1 beta. Two anakinra-specific papers were retrieved: a 2023 scoping review of anakinra and canakinumab in PSTPIP1-associated diseases ([PMID 38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/)) and a 2024 case report and review in PAPASH ([PMID 39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/)). There are no interventional trials, and only 10 of the 19 listed publications were provided.
- **Autosomal recessive familial Mediterranean fever** (score 99.89%, L5, Research Question): biologically plausible, but no trials or literature were supplied. Literature on colchicine-resistant FMF should be reviewed before any upgrade.
- **Unclassified autoinflammatory syndrome** (score 99.81%, L3, Research Question): retrospective anakinra experience in pediatric rheumatic diseases ([PMID 36589607](https://pubmed.ncbi.nlm.nih.gov/36589607/)), not specific to this category.
- **Aggressive systemic mastocytosis**: the two retrieved papers concern Schnitzler syndrome and are indirect at best, so they do not support this indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

