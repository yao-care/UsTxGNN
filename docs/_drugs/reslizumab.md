---
layout: default
title: Reslizumab
parent: Model Prediction Only (L5)
nav_order: 1117
evidence_level: L5
indication_count: 2
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
last_modified_at: 2026-10-30
description: "Reslizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Reslizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Reslizumab: Thrombocytopenia due to immune destruction
{: .text-alpha }

## One-Sentence Summary

Reslizumab is an anti-IL-5 monoclonal antibody, originally associated with eosinophilic lung conditions (eosinophilic pneumonia and pulmonary eosinophilia).
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, reslizumab is an anti-IL-5 monoclonal antibody that reduces eosinophil survival and activation signals, and this is relevant to eosinophil-driven diseases such as eosinophilic pneumonia.

A link to immune thrombocytopenia is not established. Any connection would be indirect, for example through modulation of Th2/eosinophil-driven immune dysregulation, and this is speculative. The very high TxGNN score (0.9953) is a computational prediction only and should not be read as clinical evidence.

A second prediction, **primary release disorder of platelets** (score 0.9925), has the same limitation. Its only linked publication is a 2010 review of hypereosinophilic syndrome management (including mepolizumab, another anti-IL-5 agent). That review addresses eosinophilic disorders, not platelet function disorders, so it offers no direct support.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

Currently no related literature available for the top predicted indication (thrombocytopenia due to immune destruction).

For the second prediction (primary release disorder of platelets), one publication was linked, but it is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Review | Current Medical Research and Opinion | Review of hypereosinophilic syndrome management, including mepolizumab, aimed at reducing blood and tissue eosinophilia; not specific to platelet disorders |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761033 (cancelled) | CINQAIR (Teva Respiratory, LLC) | Injection, solution, concentrate | Indication text not available |

## Safety Considerations

No drug-interaction records were found, and no knowledge-graph contraindications were identified. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials and no directly relevant literature, so the evidence level is L5. The only US license is cancelled, and the mechanism and label safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (FDA label), a blocking gap for safety screening
- Mechanism of action data (e.g., from DrugBank) to assess any link between IL-5/eosinophil biology and immune thrombocytopenia
- A targeted literature search on anti-IL-5 therapy and immune thrombocytopenia or platelet function disorders
- Clarification of current regulatory status, given the cancelled US license, and route compatibility (injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

