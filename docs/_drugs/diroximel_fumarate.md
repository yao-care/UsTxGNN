---
layout: default
title: Diroximel Fumarate
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
monitor_inn: "DIROXIMEL FUMARATE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "tetanic cataract", "immature cataract", "craniostenosis cataract", "nuclear senile cataract", "cortical cataract", "diabetes mellitus type 2 associated cataract", "mature cataract"]
last_modified_at: 2026-10-14
description: "Diroximel Fumarate: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not listed in the available regulatory data"
---

# Diroximel Fumarate
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

## Diroximel Fumarate: From an Unspecified Original Indication to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Diroximel fumarate is an oral capsule marketed in the US as Vumerity, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **diabetic cataract** (along with diabetic retinopathy and several other cataract subtypes),
but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available regulatory data |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Diroximel fumarate is a prodrug of monomethyl fumarate (MMF), which is known to activate the Nrf2 pathway and has antioxidative and anti-inflammatory effects.

Oxidative stress and polyol-pathway damage are plausible contributors to diabetic lens opacity. This gives a hypothetical link between Nrf2 activation and diabetic cataract. The same reasoning could apply to diabetic retinopathy, where oxidative stress and inflammation contribute to retinal microvascular damage. However, this link has not been tested for diroximel fumarate.

Several cautions apply:
- The score is nearly identical (about 1.0000) across many cataract subtypes, which suggests a non-specific model signal rather than a disease-specific mechanism.
- Oral systemic dosing for a lens condition raises questions about lens exposure and risk-benefit.
- For diabetic retinopathy, established therapies (anti-VEGF, laser, corticosteroids) set a high bar.
- Other predicted entries (tetanic, craniostenosis-associated, mature cataract) have even weaker mechanistic rationale. Surgery remains the definitive treatment for cataract.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211855 (cancelled) | Vumerity (Biogen Inc.) | Capsule (oral) | Not listed in the available data |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 entries; the first 20 reviewed are all rated Moderate. Main groups include:
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone (including ophthalmic)
  - Cytotoxic or immunosuppressive agents and radiopharmaceuticals: mercaptopurine, trimetrexate, dexrazoxane, levamisole, ibritumomab tiuxetan, tositumomab, iobenguane (I-131)
  - Others: naltrexone, ethanol, roflumilast, dupilumab

  Corticosteroid co-use is relevant in eye disease settings.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for diabetic cataract (and the other predicted eye conditions) is a model score. There are no trials or publications, the mechanism data are incomplete, and the US license is cancelled. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical evidence (e.g., lens or retinal models of diabetic oxidative damage) showing MMF effect
- Assessment of whether oral dosing can reach the lens or retina at tolerable exposure, or whether another delivery route is needed
- A literature and trial search specific to Nrf2 activators or fumarates in diabetic eye disease
- A review of the interaction profile, especially with corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

