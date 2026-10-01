---
layout: default
title: Levocarnitine
parent: Model Prediction Only (L5)
nav_order: 853
evidence_level: L5
indication_count: 10
---

# Levocarnitine
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

# Levocarnitine: From an Established Marketed Drug to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Levocarnitine is a marketed US drug with 15 NDA/ANDA authorizations, but the source data do not list its approved indication.
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available data (all approved-indication fields are empty) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Levocarnitine is a marketed drug with a long US regulatory history. However, its original indication could not be extracted from the data, so the relationship between the original and predicted indications cannot be assessed.

The data support no mechanistic link for this prediction. The score comes from the knowledge graph alone, with no trials or literature. The disease is an ultra-rare genetic syndrome, so a high graph score should not be read as a clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019257 | Carnitor SF (Leadiant Biosciences) | Solution | Not listed in source data |
| ANDA076851 | Levocarnitine (Rising Pharma) | Solution | Not listed in source data |
| ANDA076858 | Levocarnitine (Rising Pharma) | Tablet | Not listed in source data |
| ANDA211676 | Levocarnitine (ANI Pharmaceuticals) | Solution | Not listed in source data |
| ANDA212533 | Levocarnitine (TRUPHARMA) | Solution | Not listed in source data |

Routes and forms across all 15 authorizations include oral tablet, oral/other solution, and injection.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials, no literature and no supported mechanism (Evidence Level L5). A graph score alone is not enough to justify further investment.

Other predicted indications for levocarnitine have more support and may be better candidates:
- **Congestive heart failure** (Evidence Level L2): includes a completed Phase 2/3 randomized, placebo-controlled trial (NCT01580553, n=268). No results are provided, so efficacy is unverified.
- **Rheumatoid arthritis** (Evidence Level L2): three direct trials (NCT06753565, NCT05792527, NCT03953703). All are small, and NCT03953703 is a Sjögren's syndrome trial.
- **Diabetic nephropathy** (Evidence Level L4): preclinical and observational support only.

**To proceed, the following is needed:**
- Original approved indication text and package insert warnings and contraindications (blocking data gap for safety screening)
- Mechanism of action data (from DrugBank)
- For this specific prediction: any mechanistic or genetic evidence linking carnitine metabolism to the disease. If none exists, deprioritize it in favor of the higher-evidence candidates above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

