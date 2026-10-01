---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 474
evidence_level: L5
indication_count: 2
---

# Brompheniramine
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

# Brompheniramine: From First-Generation Antihistamine to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation H1 antihistamine sold in the US in liquid and solution products. The TxGNN model predicts it may be effective for **allergic urticaria** (and, as a second candidate, **cold urticaria**). **No clinical trials and no publications** currently support either prediction, so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (no approved indication text in the license records) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Brompheniramine belongs to the first-generation H1 histamine receptor antagonist class. That class link is inferred from general drug knowledge, not from the supplied records.

Histamine released from mast cells is the main driver of wheals and itch in allergic urticaria, so H1 blockade is mechanistically plausible. The same reasoning applies to the second prediction, cold urticaria (score 99.55%). In cold urticaria, cold exposure triggers mast cell degranulation and histamine release.

Two cautions apply:
- The TxGNN scores are model predictions, not clinical evidence.
- Because the drug is already an antihistamine, allergic urticaria may be a class-consistent or on-label use, not true repurposing. This needs checking against the product labeling, since no approved indication text was supplied.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available. A targeted search is needed to see whether brompheniramine has been studied for urticaria specifically, or whether the evidence covers only other H1 antihistamines.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M012 | CVS PHARMACY | Liquid | CVS Pharmacy, Inc. |
| M012 | Dimetapp | Solution | Foundation Consumer Healthcare |
| M012 | Chlo Hist | Liquid | R. A. McNeil Company |

No approved indication text was provided for any of these authorizations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score and class-level mechanistic reasoning (L5), with no trials or publications. The package insert warnings and contraindications are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert (warnings, contraindications, approved indications) to confirm whether urticaria is already an on-label use
- Mechanism of action data from DrugBank
- A targeted literature and trial search for brompheniramine in allergic and cold urticaria
- Route and dosage form compatibility assessment (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

