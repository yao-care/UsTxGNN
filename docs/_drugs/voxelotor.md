---
layout: default
title: Voxelotor
parent: Model Prediction Only (L5)
nav_order: 1297
evidence_level: L5
indication_count: 7
---

# Voxelotor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Voxelotor: From Sickle Cell Disease to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Voxelotor (brand name OXBRYTA) is a hemoglobin S polymerization inhibitor that raises hemoglobin-oxygen affinity. It was developed for sickle cell disease, which is general knowledge, since the Evidence Pack lists no approved indication text.
The TxGNN model predicts it may be effective for **hereditary thrombocytopenia with normal platelets**, but **0 clinical trials** and **0 publications** support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Sickle cell disease (general knowledge; not listed in the Evidence Pack's license records) |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed (per the Evidence Pack; verify against current status, see Safety Considerations) |
| Number of NDAs | 3 license records (2 distinct NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general knowledge, voxelotor binds hemoglobin, inhibits sickle hemoglobin polymerization, and increases hemoglobin-oxygen affinity. It acts on red blood cells.

**No established mechanistic link to the predicted indication was found.** Voxelotor has no known action on megakaryopoiesis or platelet production. The high score (0.996) most likely reflects graph proximity among hematologic disease nodes in the knowledge graph, not a biological rationale.

The other six predictions are also platelet or hematologic disorders. They are thrombocytopenia, dense granule disease, primary release disorder of platelets, transient neonatal thrombocytopenia, macrothrombocytopenia with mitral valve insufficiency, and light chain-associated Fanconi syndrome. All are L5, with no trials or literature and no plausible mechanism. This pattern supports the view that the predictions are an artifact of the graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA216157 | OXBRYTA | Tablet, for suspension |
| NDA213137 | OXBRYTA | Tablet, film coated (listed twice in the records) |

Manufacturer: Global Blood Therapeutics, Inc., a subsidiary of Pfizer Inc. All forms are oral. No approved indication text is provided in the records.

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no warnings, contraindications, or drug interaction data (the DDI query returned no results).

The "Marketed" status should be verified. To my knowledge, Pfizer withdrew OXBRYTA from the market in 2024 over safety concerns, and this is not reflected in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score. There are no trials or publications, and no plausible mechanistic link between hemoglobin-oxygen affinity modulation and platelet production or function. The drug's own safety and market status also need verification.

**To proceed, the following is needed:**
- Verify the current US regulatory and marketing status of voxelotor
- Obtain the package insert (warnings and contraindications) and the approved indication text
- Obtain mechanism of action data from DrugBank
- Find preclinical or mechanistic evidence linking voxelotor to platelet biology, otherwise deprioritize this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

