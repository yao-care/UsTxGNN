---
layout: default
title: Dinutuximab
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Dinutuximab: predicted new indication Vertebral anomalies and variable endocrine and T-cell dysfunction (evidence level L5). Approved use: Neuroblastoma"
monitor_inn: "DINUTUXIMAB"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Dinutuximab
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

## Dinutuximab: From Neuroblastoma to Vertebral Anomalies and Variable Endocrine and T-Cell Dysfunction
{: .text-alpha }

## One-Sentence Summary

Dinutuximab is an anti-GD2 chimeric monoclonal antibody, originally used to treat neuroblastoma.
The TxGNN model's top-ranked prediction is **vertebral anomalies and variable endocrine and T-cell dysfunction**, but this rests on model output alone, with **0 clinical trials** and **0 publications** supporting it.
The more biologically plausible candidate is the second-ranked **ganglioneuroblastoma**, which has only indirect literature support (3 publications, mostly about neuroblastoma).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuroblastoma |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

For comparison, the other predictions are:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 3 | Retroperitoneal neoplasm | 0.9935 | L5 | Hold |
| 4 | Chronic myelogenous leukemia, BCR-ABL1 positive | 0.9931 | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, dinutuximab is an anti-GD2 chimeric monoclonal antibody. It targets GD2-expressing tumor cells through antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC). Its efficacy in neuroblastoma, a GD2-expressing tumor, is the basis of its original indication.

**Top-ranked prediction (vertebral anomalies with endocrine and T-cell dysfunction):** No mechanistic link was identified. This rare syndrome is a developmental disorder, not a GD2-expressing malignancy. The high score (0.9942) is a computational prediction only and should not be treated as evidence of benefit.

**Ganglioneuroblastoma (rank 2):** This is the most plausible candidate. It belongs to the same neuroblastic tumor spectrum as neuroblastoma, and these tumors commonly express GD2. However, the retrieved literature concerns mainly neuroblastoma rather than ganglioneuroblastoma. Differentiated ganglioneuroblastoma or ganglioneuroma components may have lower proliferative activity and different GD2 expression, so benefit in this subtype is unestablished.

**Retroperitoneal neoplasm and CML (ranks 3 and 4):** There is no supporting rationale. Only GD2-expressing retroperitoneal tumors, such as neuroblastoma, would plausibly respond, and those are already covered by the original indication. CML is driven by the BCR-ABL1 fusion kinase and treated with tyrosine kinase inhibitors, and GD2 is not an established target there.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for any of the other three predicted indications.

## Literature Evidence

No literature is available for the top-ranked prediction. The literature below relates to the second-ranked candidate, ganglioneuroblastoma, and is indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28549783](https://pubmed.ncbi.nlm.nih.gov/28549783/) | 2017 | Randomized phase 2 trial | The Lancet. Oncology | COG ANBL1221: irinotecan-temozolomide combined with temsirolimus or dinutuximab in children with relapsed or refractory neuroblastoma |
| [37929737](https://pubmed.ncbi.nlm.nih.gov/37929737/) | 2025 | Case report with review | Current Pediatric Reviews | Late relapse in neuroblastoma; relapsed or refractory disease has a dismal survival rate |
| [42811141](https://pubmed.ncbi.nlm.nih.gov/42811141/) | 2026 | Case report with systematic review | European Spine Journal | Cervicothoracic dumbbell ganglioneuroblastoma with spinal canal involvement and bone marrow metastasis; evidence on management is limited |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125516 | Unituxin (United Therapeutics Corporation) | Injection | Not listed in the compiled data (status: valid) |

## Safety Considerations

**Drug Interactions:** 100 interactions were identified in the interaction database. The main ones in the data reviewed are listed below.

- **Major:** the corticosteroids hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisolone and prednisone; also deferiprone and samarium (153Sm) lexidronam.
- **Moderate:** metronidazole, tinidazole, secnidazole, benznidazole, rosuvastatin, simvastatin, strontium chloride Sr-89, chloroquine, hydroxychloroquine and disulfiram.

Please refer to the package insert for warnings and contraindications. Label-based safety data was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no supporting trials or literature and no plausible mechanistic link to GD2 targeting. The high TxGNN score is a model output only. In addition, the only US license for dinutuximab is listed as cancelled, and label-based safety data is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, since safety screening cannot proceed without them
- Detailed mechanism of action data
- Confirmation of the current US regulatory and marketing status of dinutuximab
- Evidence of GD2 expression in the predicted disease, if any, before further investigation of the top-ranked prediction
- For ganglioneuroblastoma, the most plausible alternative, GD2 expression data and subtype-specific clinical evidence (it is currently a research question, not a Go candidate)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

