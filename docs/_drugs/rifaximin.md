---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 1122
evidence_level: L5
indication_count: 6
monitor_inn: "RIFAXIMIN"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
last_modified_at: 2026-10-30
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L4). Approved use: Hepatic encephalopathy, hepatic coma"
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis
{: .text-alpha }

## One-Sentence Summary

Rifaximin is a poorly absorbed oral antibiotic, originally used to treat hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **Oral Candidiasis**, but there are **no registered clinical trials** and only **1 publication**, and that publication points to a possible harm signal rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, rifaximin is a non-absorbable, gut-restricted antibacterial. It has no known direct antifungal activity.

The available literature does not support the prediction. The only linked report describes rifaximin use *favouring* micafungin-resistant Candida infections in allogeneic hematopoietic cell transplant recipients. This suggests a plausible harm mechanism: antibiotic-driven disruption of the gut microbiome can allow Candida overgrowth. The high TxGNN score therefore conflicts with the available evidence and is likely an artifact of co-occurrence in the literature rather than a true therapeutic signal.

The other top-ranked predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome) also lack any clinical or literature support. Candidiasis (general, score 0.9915) is likewise supported only by risk-oriented literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients given rifaximin prophylaxis, rifaximin use favoured micafungin-resistant Candida infections, which suggests harm rather than benefit |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021361 | XIFAXAN (Cardinal Health 107, LLC) | Tablet | Not listed (status: valid) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: *Clostridium difficile* colitis; perinatal necrotizing enterocolitis.
- **Drug Interactions**: 69 interactions were identified. Most are Moderate, and one is Major:
  - **Major**: Live cholera vaccine (*Vibrio cholerae* CVD 103-HgR strain)
  - **Moderate (examples)**: Warfarin, cyclosporine, tolvaptan, alpelisib, apalutamide, cabozantinib, daclatasvir, ledipasvir, encorafenib, picosulfuric acid

Please refer to the package insert for other safety information, such as key warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only supporting literature suggests rifaximin may promote Candida infections, and no clinical trials exist. Rifaximin also has no known antifungal activity, so the evidence does not justify further investment at this stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Evidence of antifungal activity or clinical benefit in candidiasis, such as in vitro or preclinical studies
- Review of whether the Candida risk signal outweighs any potential benefit
- Clarification of the current US marketing status, since the only NDA on record is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

