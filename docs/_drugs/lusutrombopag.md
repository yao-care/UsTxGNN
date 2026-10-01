---
layout: default
title: Lusutrombopag
parent: Model Prediction Only (L5)
nav_order: 880
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From Thrombocytopenia in Chronic Liver Disease to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Lusutrombopag is an oral thrombopoietin receptor (TPO-R) agonist marketed in the US as Mulpleta, and is used to raise platelet counts in adults with chronic liver disease.
The TxGNN model predicts it may be effective for **hereditary thrombocytopenia with normal platelets**.
Currently there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia in adults with chronic liver disease (inferred from the pack's rationale text; the license records list no indication text) |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (three manufacturer entries under NDA210923) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lusutrombopag is a TPO-R agonist. It stimulates megakaryocyte proliferation and platelet production. Detailed mechanism of action data is not available in the source record. The description here comes from the pack's mechanistic rationale and the drug's known class.

Its approved use addresses low platelet counts by increasing platelet production. Inherited thrombocytopenias caused by impaired platelet production could plausibly respond to the same approach, and other TPO-R agonists have been explored in inherited forms. This link is mechanistic inference only. There is no drug-specific clinical or literature data, and the score reflects model prediction alone.

The other nine predictions in the pack are weaker:
- **Related thrombocytopenias** (marcothrombocytopenia with mitral valve insufficiency, transient neonatal thrombocytopenia): conceptually relevant, but the platelet defect may not respond to more TPO signaling, or the condition is self-limiting and no neonatal safety data exist.
- **Platelet function defects** (dense granule disease, platelet storage pool deficiency): these are qualitative defects, and raising platelet count is not expected to correct them.
- **Neurological and skeletal conditions** (ALS and related entries, polymicrogyria, axial spondylometaphyseal dysplasia): no plausible mechanistic link, likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA210923 | Mulpleta | Film-coated tablet (oral) | VANCOCIN ITALIA SRL |
| NDA210923 | Mulpleta | Film-coated tablet (oral) | Eddingpharm (U.S.) Inc. |
| NDA210923 | Mulpleta | Film-coated tablet (oral) | SHIONOGI INC. |

## Safety Considerations

Please refer to the package insert for safety information.

The record contains no drug interaction data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the TxGNN score, with no trials, no literature, and no safety data in the record. The top candidate, hereditary thrombocytopenia with normal platelets, is worth keeping as a research question. The remaining candidates are weak or implausible.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for TPO-R agonists in inherited thrombocytopenias
- Confirmation of the approved indication text
- Pediatric safety data, if any neonatal or childhood use is considered
- Route compatibility assessment for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

