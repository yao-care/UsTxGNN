---
layout: default
title: Sincalide
parent: Model Prediction Only (L5)
nav_order: 1164
evidence_level: L5
indication_count: 10
monitor_inn: "SINCALIDE"
predicted_indications: ["malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "thrombotic disease", "hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia", "homozygous familial hypercholesterolemia", "Prinzmetal angina", "amenorrhea (disease)"]
last_modified_at: 2026-10-14
description: "Sincalide: predicted new indication Malignant catarrh (malignant catarrhal fever… (evidence level L5). Approved use: Not stated in the US license records compiled for this report (gallbl…"
---

# Sincalide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Sincalide: From Gallbladder Diagnostic Use to Malignant Catarrh (Model Prediction Only)
{: .text-alpha }

## One-Sentence Summary

Sincalide is a synthetic C-terminal octapeptide of cholecystokinin (CCK-8) that stimulates gallbladder contraction and pancreatic secretion, and it is used as a gastrointestinal diagnostic agent.
The TxGNN model predicts it may be effective for **malignant catarrh**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone and has no identified biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records compiled for this report (gallbladder and pancreatic diagnostic use is inferred from the drug's pharmacology) |
| Predicted New Indication | Malignant catarrh (malignant catarrhal fever, a viral disease of ruminants) |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sincalide is a synthetic CCK-8 peptide that stimulates gallbladder contraction and pancreatic secretion.

The predicted indication, malignant catarrhal fever, is a viral disease of ruminants, and no mechanistic link to sincalide has been identified. The score is a model prediction only and has no supporting biological rationale. The prediction is therefore not considered reasonable on current evidence.

The same pattern applies to the other top-ranked predictions. Malignant catarrh and infectious bovine rhinotracheitis have identical scores (0.9996). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The thyroid-related predictions (hyperthyroidism, resistance to thyroid hormone due to a THRB mutation, hyperthyroxinemia) form a cluster. Other predicted conditions include cytomegalovirus infection, thrombotic disease, homozygous familial hypercholesterolemia, Prinzmetal angina and amenorrhea. None has a known mechanism or supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017697 (cancelled) | KINEVAC (Bracco Diagnostics Inc.) | Lyophilized powder for injection | Not available |
| NDA210850 (cancelled) | Sincalide (Fosun Pharma USA Inc.) | Lyophilized powder for injection | Not available |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found, and no disease contraindications were identified from the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, no plausible mechanism, and the predicted condition is a veterinary viral disease. Both US licenses are cancelled, and safety and mechanism data are incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap that prevents safety screening)
- Mechanism of action data from DrugBank
- A biologically plausible link between CCK receptor agonism and the predicted disease
- A review of whether the shared-score and thyroid-cluster patterns reflect model artifacts
- Consideration of other candidates in the list or of drug-related indications with human relevance, since none of the top 10 predictions has supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

