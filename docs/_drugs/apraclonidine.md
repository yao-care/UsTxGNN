---
layout: default
title: Apraclonidine
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 1
---

# Apraclonidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Apraclonidine: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Apraclonidine is an eye-drop medicine originally used for short-term treatment of open-angle glaucoma.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently **0 clinical trials** and **0 publications** support this direction, so the prediction rests on computational modelling alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacological knowledge, apraclonidine is an alpha-2 adrenergic agonist that lowers intraocular pressure (IOP) by reducing aqueous humor production. Its efficacy in open-angle glaucoma is established.

Primary hereditary (congenital or juvenile) glaucoma shares the same therapeutic target, elevated IOP, so a mechanistic overlap is plausible. However, the very high TxGNN score most likely reflects the close relationship between the two glaucoma conditions in the knowledge graph, not independent evidence of benefit.

There is also a safety concern specific to this population: alpha-2 agonists are associated with CNS depression and apnea in infants, and hereditary glaucoma often presents early in life. In addition, the product is no longer actively marketed in the US, which limits practical development.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020258 (Cancelled) | Apraclonidine (Sandoz Inc) | Solution | Not listed |
| NDA019779 (Cancelled) | IOPIDINE 1% (Harrow Eye, LLC) | Solution / Drops | Not listed |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension and hypertensive disorder; blood disorders (thrombocytopenia, thrombocytopenic purpura, neutropenia, agranulocytosis, Diamond-Blackfan anemia, inherited aplastic anemia, blood coagulation disease, leukemia); lipid disorders (hyperlipidemia, familial hyperlipidemia); liver conditions (cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis); active peptic ulcer disease; intracerebral hemorrhage; ascorbic acid deficiency and scurvy. These come from model-derived relationships and need verification against the official label.
- **Drug Interactions:** 60 interactions were identified in total. The only one rated Major among those listed is **methylene blue**. The others listed are Moderate, including loperamide, dronabinol, metoclopramide, morphine (including liposomal), nabilone, opium, papaverine, scopolamine, sibutramine, difenoxin, diphenoxylate, ethanol, amyl nitrite, diazoxide, promethazine, epoprostenol, iloprost, and selexipag.
- **Pediatric consideration:** CNS depression and apnea have been reported with alpha-2 agonists in infants, which is highly relevant to early-onset hereditary glaucoma.

Please refer to the package insert for official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5), the product's US licenses are all cancelled, and pediatric safety concerns apply to the likely target population. The high model score alone is not enough to justify advancing.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or clinical evidence in primary hereditary glaucoma, with particular attention to pediatric safety
- Assessment of route compatibility and whether reformulation or relaunch is feasible given the cancelled market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

