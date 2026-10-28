---
layout: default
title: Lenograstim
parent: Model Prediction Only (L5)
nav_order: 845
evidence_level: L5
indication_count: 4
monitor_inn: "LENOGRASTIM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-10-28
description: "Lenograstim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Lenograstim
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

## Lenograstim: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Lenograstim is a recombinant human granulocyte colony-stimulating factor (G-CSF) that stimulates neutrophil production.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, lenograstim is a recombinant human G-CSF that acts through the G-CSF receptor to drive proliferation and differentiation of the neutrophil (granulocyte) lineage.

Primary release disorder of platelets is a qualitative platelet function defect, not a shortage of white blood cells. No direct mechanistic link between G-CSF signaling and this condition is evident. The high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and nothing in the compiled data supports it with clinical or laboratory evidence. This prediction should therefore be treated as a hypothesis to be tested, not as a finding.

### Other Predicted Indications (for reference)

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Glanzmann thrombasthenia | 0.9989 | L5 | Caused by a defect in platelet integrin αIIbβ3 (GPIIb/IIIa). G-CSF does not target this pathway, and neutrophil stimulation would not be expected to correct the defect. |
| 3 | Pseudo-von Willebrand disease | 0.9988 | L5 | Caused by a gain-of-function defect in platelet GPIbα. Lenograstim has no known action on this receptor or on VWF biology. |
| 4 | Severe nonproliferative diabetic retinopathy | 0.9961 | L5 | G-CSF has been discussed in endothelial progenitor cell mobilization and vascular repair, which is a speculative link. G-CSF could also promote pathological neovascularization, so the direction of effect is uncertain. |

All four predictions have no supporting clinical trials or literature in the compiled data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | GUNA-GCSF (Guna spa) | Solution / drops | Not available (cancelled) |
| BLA761134 | RYZNEUTA (Acrotech Biopharma Inc) | Injection | Not available (valid) |


## Safety Considerations

No drug interactions were found in the queried database, and no disease contraindications were identified from the knowledge graph.

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to a platelet function defect.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank to allow a proper mechanistic analysis
- Original approved indication text for the drug
- Preclinical or mechanistic studies showing any plausible effect of G-CSF on platelet function
- Confirmation of the regulatory status and route compatibility if development is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

