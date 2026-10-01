---
layout: default
title: Rifaximin
parent: Moderate Evidence (L3-L4)
nav_order: 1122
evidence_level: L4
indication_count: 6
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Rifaximin: From Gut-Restricted Antibacterial to Oral Candidiasis

## One-Sentence Summary

Rifaximin is an oral, poorly absorbed antibiotic that is marketed in the US as XIFAXAN tablets. The TxGNN model predicts it may be effective for **oral candidiasis** with a very high score, but there are **0 clinical trials** and only **1 publication**. That publication points to a possible harm signal rather than a treatment benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US license records |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license entries (all under NDA021361) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is a non-absorbed oral antibacterial that acts mainly in the gut. It has no established antifungal activity, so a direct therapeutic link to oral candidiasis is not supported.

The high TxGNN score (0.997) most likely reflects proximity in the knowledge graph, such as shared oral-disease and infection neighbors, rather than biology. The only linked paper suggests the opposite direction. In allogeneic stem cell transplant recipients, rifaximin use was associated with micafungin-resistant *Candida* infections. Suppressing gut bacteria may favor fungal overgrowth, so this is a safety concern rather than support for treatment.

The other four predictions from the same run also have no supporting evidence and no plausible mechanism:
- commissural lip fistula
- osteoradionecrosis of the mandible
- oral leukoedema
- burning mouth syndrome

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | Rifaximin prophylaxis in allogeneic stem cell transplant patients was associated with more micafungin-resistant *Candida* infections. This is a possible harm signal, not evidence of benefit. Based on the title and a truncated abstract. |

Note: the broader "candidiasis" prediction (rank 6) also cites a 2021 case-control study of candidemia risk factors in cirrhosis ([32360775](https://pubmed.ncbi.nlm.nih.gov/32360775/)). It describes risk factors, not treatment benefit, and is confounded by underlying liver disease.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021361 | XIFAXAN | Tablet | Cardinal Health 107, LLC |
| NDA021361 | XIFAXAN | Tablet | Salix Pharmaceuticals, Inc. |
| NDA021361 | XIFAXAN | Tablet | A-S Medication Solutions |
| NDA021361 | XIFAXAN | Tablet | Salix Pharmaceuticals, Inc. |

The route of administration is oral only. Approved indication text was empty in the supplied records.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found in the queried data. The only literature signal is the association between rifaximin use and resistant *Candida* infections in transplant recipients (see above).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no plausible antifungal mechanism, and the only related literature suggests a possible risk rather than a benefit. The high TxGNN score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indications), which is required for safety screening
- Detailed mechanism of action data from DrugBank
- A full-text review of PMID 34180023 to clarify whether rifaximin promotes resistant *Candida* infection
- In vitro antifungal activity data against *Candida* species, if any exist
- Evidence that a gut-restricted, minimally absorbed drug can reach oral mucosal sites at relevant concentrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

