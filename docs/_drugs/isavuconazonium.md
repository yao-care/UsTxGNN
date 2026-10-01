---
layout: default
title: Isavuconazonium
parent: Model Prediction Only (L5)
nav_order: 812
evidence_level: L5
indication_count: 2
---

# Isavuconazonium
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

# Isavuconazonium: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Isavuconazonium (marketed in the US as CRESEMBA) is an azole antifungal, but the approved indication text was not provided in the Evidence Pack.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
It rests on the model score alone, and the biological link is weak, so this is a **Hold** candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided (approved indication text is empty in all NDA records) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (2 distinct NDA numbers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. The mechanistic notes state that isavuconazole inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis. This is the standard mechanism of azole antifungals.

For pneumocystosis, this mechanism is a poor fit. *Pneumocystis* membranes contain little ergosterol and mainly use cholesterol, so azole antifungals are generally considered poorly effective. Standard therapy is trimethoprim-sulfamethoxazole.

The high TxGNN score (99.56%, model rank 10,923) is a graph-based prediction only. Neither the mechanism nor any clinical data provided supports it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pneumocystosis.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA207500 | CRESEMBA | Capsule | Astellas Pharma US, Inc. |
| NDA207501 | CRESEMBA | Lyophilized powder for injection (solution) | Astellas Pharma US, Inc. |

Approved indication text is empty in all records. NDA207500 appears twice in the input and is listed once here. Routes available: oral (capsule) and injectable.

---

## Safety Considerations

Please refer to the package insert for safety information. Warnings and contraindications were not available in the input, and no drug interaction data was found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trials or publications exist, and the mechanism is weak for *Pneumocystis*, which has little ergosterol and is not expected to respond to azoles. Safety data is also missing.

**To proceed, the following is needed:**
- FDA package insert (approved indications, warnings, contraindications). This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank
- Preclinical or in vitro evidence of activity against *Pneumocystis*
- Route compatibility assessment for pneumocystosis

**Note on the second prediction (mycetoma, score 99.34%):**
Eumycetoma is a fungal infection, and azoles such as itraconazole are already used against it, so an azole mechanism is plausible. It would not apply to bacterial actinomycetoma. The only evidence is one 2023 review of the neglected tropical disease drug pipeline ([PMID 37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/), *Parasites & Vectors*). How it treats isavuconazole cannot be confirmed from the provided (truncated) data. It is classed as L4 and a research question, and it is a more plausible direction than pneumocystosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

