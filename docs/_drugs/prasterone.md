---
layout: default
title: Prasterone
parent: Model Prediction Only (L5)
nav_order: 1074
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From Marketed Hormone Products to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (DHEA, an adrenal androgen precursor) is marketed in the US as a vaginal insert and as several liquid products.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but **no clinical trials and no publications** support this prediction.
It is a model-only signal, and the mechanism is implausible for an inherited serpin deficiency.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 licenses listed (only 1 distinct NDA number: NDA208470) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for prasterone, and the source data lists no approved indication text. The prediction therefore cannot be tied to a known mechanism.

Heparin cofactor 2 deficiency is an inherited deficiency of a serpin, a coagulation inhibitor. Prasterone is an androgen precursor, and nothing in the supplied data suggests it could correct or compensate for this defect. The high score (0.9999) is a knowledge-graph association only.

Sex-steroid exposure is generally a thrombotic-risk consideration rather than a benefit in prothrombotic states. The direction of any effect is therefore unclear and may be unfavourable.

The other top-10 predictions are mostly coagulation or platelet disorders (factor 5 excess, antithrombin deficiency type 2, protein S deficiency, pseudo-von Willebrand disease, platelet release disorder). They likewise have no trials or literature. Two predictions have some indirect literature:

- **Thrombophilia** (rank 4, L4): four indirect papers, none testing prasterone as a treatment.
- **Scleroderma** (rank 7, L4): six observational papers consistently show low DHEA-S in systemic sclerosis. This is a coherent hypothesis, but these are biomarker association studies, not interventions with prasterone. It is the only prediction tagged "Research Question".

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| NDA208470 | Intrarosa (listed twice in the source data) | Insert | Millicent US, Inc. |
| No number listed | DHEA | Liquid | Deseret Biologicals, Inc. |
| No number listed | DHEA Forte | Liquid | BioActive Nutritionals, Inc. |
| No number listed | Kidney/Ovarian/Adrenal Drops | Liquid | Professional Complementary Health Formulas |

Only the first 5 of the 9 listed licenses are shown here.

---

## Safety Considerations

Please refer to the package insert for safety information.

- **Drug interactions:** No interaction records were found in the queried source.
- **Thrombotic risk:** Androgen and estrogen exposure may raise thrombotic risk, so a safety review is needed before any efficacy question is pursued in coagulation disorders.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature, and no plausible mechanism for an inherited coagulation-inhibitor deficiency. A prothrombotic safety concern also argues against pursuing it.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any mechanistic or clinical evidence linking prasterone to heparin cofactor 2 deficiency
- If a lead is wanted, redirect effort to the scleroderma hypothesis: a review of DHEA-S deficiency data and a proof-of-concept study design

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

