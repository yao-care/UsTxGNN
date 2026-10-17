---
layout: default
title: Nitrogen
parent: Model Prediction Only (L5)
nav_order: 972
evidence_level: L5
indication_count: 4
monitor_inn: "NITROGEN"
predicted_indications: ["16q24.1 microdeletion syndrome", "primary interstitial lung disease specific to childhood", "isolated pulmonary capillaritis", "congenital pulmonary lymphangiectasia"]
last_modified_at: 2026-10-14
description: "Nitrogen: predicted new indication 16q24.1 microdeletion syndrome (evidence level L5). Approved use: Congenital alveolar capillary dysplasia"
---

# Nitrogen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Nitrogen: From Congenital Alveolar Capillary Dysplasia to 16q24.1 Microdeletion Syndrome

## One-Sentence Summary

Nitrogen is a medical gas that, according to the knowledge graph, is associated with congenital alveolar capillary dysplasia and persistent fetal circulation syndrome.
The TxGNN model predicts it may be effective for **16q24.1 microdeletion syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital alveolar capillary dysplasia; persistent fetal circulation syndrome (from the knowledge graph; no approved indication text is available in US licence records) |
| Predicted New Indication | 16q24.1 microdeletion syndrome |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrogen is an inert gas used in medical gas mixtures, for example to dilute oxygen or to adjust inspired oxygen levels. No disease-modifying pharmacology is established for it.

The predicted disease, 16q24.1 microdeletion syndrome, involves the FOXF1 gene and its regulatory region. It is the genetic cause of alveolar capillary dysplasia with misalignment of pulmonary veins (ACDMPV), which is the same disease spectrum as nitrogen's original knowledge-graph indication. The high score therefore most likely reflects closeness in the disease ontology rather than a new mechanism.

Nitrogen could at most play a supportive role in respiratory management, such as modulating pulmonary vascular resistance through hypoxic gas mixtures. It does not correct the underlying genetic defect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All nine US authorizations are cancelled, and none carries approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205766 | NITROGEN (Keen Compressed Gas Co. Inc.) | Gas | Not stated; cancelled |
| NDA205866 | NITROGEN (Air Source Industries Inc) | Gas | Not stated; cancelled |
| NDA205850 | Nitrogen (NexAir, LLC) | Gas | Not stated; cancelled |
| NDA205713 | Nitrogen (Arcet Equipment Company dba Arc3 Gases North) | Gas | Not stated; cancelled |
| NDA205891 | Nitrogen (TIMS SOUTH TEXAS LLC) | Gas | Not stated; cancelled |

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication edges, not label text): methemoglobinemia, sulfhemoglobinemia, heart failure.
- **Drug Interactions**: No interactions were found in the data compiled for this report.

Please refer to the package insert for further safety information.

## Other Predicted Indications

The model also ranked three further predictions. All have Evidence Level L5, no trials, no publications, and a Hold recommendation.

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Primary interstitial lung disease specific to childhood | 99.72% | No direct mechanistic link. Nitrogen is inert, and any role would be limited to gas-mixture supportive care. |
| Isolated pulmonary capillaritis | 99.72% | This is an immune-mediated vasculopathy treated with immunosuppression. Nitrogen has no anti-inflammatory or immunomodulatory mechanism. |
| Congenital pulmonary lymphangiectasia | 99.68% | This is a developmental lymphatic disorder. Overlap is limited to neonatal respiratory support, which does not treat the underlying abnormality. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model output and disease-network proximity. There are no clinical trials or publications, no mechanism of action data, and all US authorizations are cancelled. Nitrogen is an inert gas and cannot correct the FOXF1-related genetic defect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data
- A literature and trial search on nitrogen or hypoxic gas mixtures in ACDMPV and related neonatal pulmonary conditions
- Clarification of whether the original indications come from labelled use or only from the knowledge graph
- A route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

