---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 1103
evidence_level: L5
indication_count: 2
---

# Rabeprazole
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

# Rabeprazole: From Acid Suppression (Proton Pump Inhibitor) to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) that suppresses gastric acid and is marketed in the US as a delayed-release oral tablet.
The TxGNN model predicts it may be relevant to **Smouldering systemic mastocytosis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Rabeprazole is a proton pump inhibitor that acts on the gastric H+/K+ ATPase. Its approved-indication text was also not supplied, so no drug-specific mechanism for the new indication can be verified from the data provided.

The only plausible link is symptomatic and indirect. Mast cell mediator release (e.g., histamine) can drive gastric acid hypersecretion and reflux-type symptoms. Acid suppression is commonly used as supportive care in systemic mastocytosis. This is background reasoning, not evidence from the supplied data. A PPI would not change the disease course, which is driven by KIT-dependent clonal mast cell proliferation. A high TxGNN score alone does not establish a therapeutic effect.

TxGNN also ranks a second, related indication: **lymphoadenopathic mastocytosis with eosinophilia** (score 99.35%, L5, Hold). It has no trials or literature either. The same indirect acid-suppression argument applies, and no mechanism by which a PPI would affect the underlying clonal or eosinophilic disease has been identified. Both scores likely reflect proximity to related mastocytosis nodes in the knowledge graph rather than a drug-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090678 | Rabeprazole Sodium | Tablet, delayed release | Lannett Company, Inc. |
| ANDA208644 | Rabeprazole Sodium | Tablet, delayed release | REMEDYREPACK INC. |
| ANDA204237 | Rabeprazole Sodium | Tablet, delayed release | Advanced Rx of Tennessee, LLC |
| ANDA205761 | Rabeprazole Sodium | Tablet, delayed release | DIRECT RX |
| ANDA204237 | Rabeprazole Sodium | Tablet, delayed release | Advagen Pharma Limited |

Approved-indication text was not provided for these authorizations. Only the oral route is listed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions have only a model score behind them, with no registered trials, no literature and no verified mechanism. At best, rabeprazole might serve as symptom-level supportive care in mastocytosis, not as disease-modifying therapy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and approved-indication data (e.g., from DrugBank)
- A literature and trial search for PPI use in systemic mastocytosis, including supportive-care evidence
- A clear definition of the intended use (symptom control vs. disease modification) before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

