---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 1020
evidence_level: L5
indication_count: 2
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

# Pegfilgrastim: From Neutropenia Prevention to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a long-acting, PEGylated form of G-CSF that stimulates neutrophil production. The US approved-indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy** (and the broader **diabetic retinopathy**), but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled data (pegfilgrastim is generally known as a neutrophil-stimulating agent) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 7 (all BLAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, pegfilgrastim is a PEGylated G-CSF analog that stimulates neutrophil production. No mechanistic link to diabetic retinopathy can be verified from the data compiled for this report.

One speculative argument is that G-CSF can mobilize bone marrow-derived progenitor cells, which might support vascular repair. The opposite is also plausible: G-CSF-driven neutrophil activation and inflammation could worsen retinal vascular pathology. The direction of effect is unknown.

The prediction is likely driven by network proximity in the knowledge graph rather than demonstrated biology. The second predicted indication, diabetic retinopathy, is a broader parent of the severe NPDR entry and does not count as independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All seven US biologics licenses for pegfilgrastim are cancelled, and the approved-indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125031 | Neulasta (Amgen, Inc) | Injection | Not available |
| BLA761039 | UDENYCA (Coherus Oncology, Inc.) | Injection, solution | Not available |
| BLA761045 | ZIEXTENZO (Sandoz Inc) | Injection | Not available |
| BLA761075 | Fulphila (Biocon Biologics Inc.) | Injection | Not available |
| BLA761084 | FYLNETRA (Amneal Pharmaceuticals LLC) | Injection | Not available |

Two further licenses, NYVEPRIA (BLA761111, Pfizer) and STIMUFEND (BLA761173, Northstar Rx), are also cancelled.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions, all of the ones listed being Moderate severity. Examples include:
  - Chemotherapy and cytotoxic agents: paclitaxel, mercaptopurine, azacitidine, arsenic trioxide, trimetrexate, altretamine
  - Targeted and biologic agents: abemaciclib, acalabrutinib, avapritinib, alemtuzumab, aldesleukin, belantamab mafodotin
  - Radiopharmaceuticals: I-131 iobenguane, I-131 tositumomab, ibritumomab tiuxetan, fludeoxyglucose (18F)
  - Others: pegvaliase, levamisole

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a very high model score (99.89%). There are no clinical trials or publications, no verifiable mechanism, and all US licenses are cancelled. G-CSF could plausibly help or harm in retinal vascular disease, so the direction of effect is unknown.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search on G-CSF or progenitor cell mobilization in diabetic retinopathy, including any evidence of harm
- Preclinical evidence (e.g., diabetic retinopathy models) showing the direction of effect
- Assessment of route compatibility, since systemic injection would need to be justified against current ocular treatments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

