---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 654
evidence_level: L5
indication_count: 1
monitor_inn: "ENOXAPARIN"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
last_modified_at: 2026-10-14
description: "Enoxaparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism"
---

# Enoxaparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Enoxaparin: From Pulmonary Embolism to Thrombophilia Due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin anticoagulant, originally associated with pulmonary embolism, disseminated intravascular coagulation (DIC) and purpura fulminans.
The TxGNN model predicts it may be useful for **autosomal recessive thrombophilia due to protein C deficiency**,
but the data compiled for this report contain **no clinical trials and no publications** for this indication, so the prediction rests on model output and mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism; disseminated intravascular coagulation; purpura fulminans; acquired purpura fulminans (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 7 (1 NDA and 6 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for enoxaparin are not available in the compiled data. Based on general pharmacology, enoxaparin is a low-molecular-weight heparin. It enhances antithrombin III activity and mainly inhibits factor Xa, and to a lesser degree thrombin. Its anticoagulant effect does not depend on the protein C pathway.

In autosomal recessive (severe or homozygous) protein C deficiency, the body loses a key natural brake on thrombin generation. This leads to thrombosis and purpura fulminans. Because enoxaparin acts on a different, parallel part of the coagulation cascade, anticoagulation could plausibly reduce thrombotic burden in these patients.

The original indications (pulmonary embolism, DIC, purpura fulminans) share the same underlying problem of dysregulated coagulation, which supports the link. However, the TxGNN score is a computational prediction only. Standard care for severe congenital protein C deficiency, such as protein C concentrate, anticoagulation and in some cases liver transplantation, was not evaluated in the supplied data, so enoxaparin's place relative to these options is unknown.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA020164 | Lovenox (Sanofi-Aventis U.S. LLC) | Injection | Cancelled |
| ANDA076726 | Enoxaparin Sodium (Zydus Pharmaceuticals USA Inc.) | Injection, solution | Cancelled |
| ANDA076684 | Enoxaparin Sodium (BluePoint Laboratories) | Injection | Cancelled |
| ANDA077857 | Enoxaparin Sodium (Cardinal Health 107, LLC) | Injection | Cancelled |
| ANDA205660 | Enoxaparin Sodium (Hepalink USA Inc.) | Injection, solution | Cancelled |

Two further cancelled ANDAs (ANDA214646, ANDA206834) are also on record. Approved indication text is not available in the license records. All seven authorizations show as cancelled, so current product availability needs to be verified.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links enoxaparin to contraindications in the following groups:
  - Bleeding and coagulation disorders: hemophilia, blood coagulation disease, antithrombin III deficiency, Glanzmann thrombasthenia, qualitative platelet defect
  - Thrombocytopenia, including heparin-induced thrombocytopenia
  - Intracranial or intracerebral hemorrhage and placental abruption
  - Liver failure, biliary tract disease and obstructive jaundice
  - Gastrointestinal conditions: active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease
  - Retinal disease: diabetic or hypertensive retinopathy, retinitis, diabetic cataract
  - Infective endocarditis (including subacute bacterial endocarditis)
  - Osteoporosis (including postmenopausal) and arteriosclerosis obliterans
- **Drug Interactions:** The query returned 100 interactions; 20 are shown in the compiled data. Major-level interactions include:
  - Antiplatelet and NSAID agents: acetylsalicylic acid, abciximab, ketorolac, ibuprofen
  - Thrombolytic: alteplase
  - Others: deferasirox, acalabrutinib, trastuzumab emtansine, and the radiopharmaceuticals ibritumomab tiuxetan and tositumomab (including I-131)
  - Moderate-level interactions include dexfenfluramine, fenfluramine, sibutramine, aliskiren and sodium iodide I-131/I-123.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is the only support. There are no clinical trials or publications for this indication (evidence level L5), the mechanism-of-action data and label safety data are missing, and all US authorizations are cancelled.

**To proceed, the following is needed:**
- Systematic literature search on heparin or enoxaparin use in severe congenital protein C deficiency (case reports, registries, guidelines)
- Comparison with standard care (protein C concentrate, other anticoagulants, liver transplantation)
- Mechanism-of-action data and the FDA package insert (warnings and contraindications)
- Verification of current US product availability and regulatory status
- Safety review for this population, especially bleeding risk and the thrombocytopenia and coagulation-disorder contraindications listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

