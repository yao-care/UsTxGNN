---
layout: default
title: Dalteparin
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 5
monitor_inn: "DALTEPARIN"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
last_modified_at: 2026-10-14
description: "Dalteparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
---

# Dalteparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dalteparin: From Pulmonary Embolism to Protein C Deficiency Thrombophilia
{: .text-alpha }

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin, originally used for thrombotic and coagulation disorders such as pulmonary embolism, disseminated intravascular coagulation, and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans (from the knowledge graph; no approved indication text available in US labeling data) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dalteparin is a low-molecular-weight heparin that potentiates antithrombin and inhibits factor Xa.

This is biologically plausible for a prothrombotic state such as protein C deficiency. It also overlaps with the original indication of purpura fulminans, which is often caused by severe protein C deficiency. However, standard care for severe congenital protein C deficiency is protein C concentrate plus anticoagulation, so any role for dalteparin would be adjunctive and is unverified here. The high score is a computational prediction without clinical or literature support.

**Other predicted indications (all L5, Hold):**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|---|---|---|---|
| 2 | Primary release disorder of platelets | 99.67% | No clear mechanistic link. This is a bleeding-tendency condition, and an anticoagulant could increase bleeding risk. |
| 3 | Pseudo-von Willebrand disease | 99.52% | No corrective mechanism, with added bleeding risk. |
| 4 | Atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 99.34% | Only an indirect rationale. The core pathology is complement dysregulation, and renal impairment complicates heparin use. |
| 5 | Neuropathy, painful | 99.19% | No mechanistic link. The one associated trial appears to be an indication-mapping mismatch. |

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication.

For reference, one trial was linked to a lower-ranked prediction (painful neuropathy). It is not relevant evidence for that indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00445328](https://clinicaltrials.gov/study/NCT00445328) | Phase 4 | Terminated | 84 | Open-label comparison of dalteparin vs unfractionated heparin for VTE prevention in hospitalized acutely ill medical patients. Not related to painful neuropathy. |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020287 | Fragmin (Pfizer Laboratories Div Pfizer Inc) | Injection | Not listed; license status: cancelled |

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver failure, thrombocytopenia, heparin-induced thrombocytopenia, hemophilia, blood coagulation disorders, antithrombin III deficiency, Glanzmann thrombasthenia and qualitative platelet defects, intracranial/intracerebral hemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis/inflammatory bowel disease, infective endocarditis, retinal diseases (including diabetic and hypertensive retinopathy), biliary tract disease, obstructive jaundice, osteoporosis, and arteriosclerosis obliterans.
- **Drug Interactions:** 100 interactions were found in total. Major ones among those listed include:
  - Acetylsalicylic acid, ibuprofen, and ketorolac (increased bleeding risk)
  - Fondaparinux, abciximab, and acalabrutinib
  - Deferasirox and trastuzumab emtansine
  - Ibritumomab tiuxetan and tositumomab (including I-131 tositumomab)

  Moderate ones include fluvoxamine, fosinopril, sibutramine, fenfluramine, dexfenfluramine, sugammadex, and iodide I-123/I-131.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications are supported by model scores only, with no relevant trials or literature (L5). The only trial found is unrelated to the predicted indication. Several predictions (platelet and von Willebrand disorders) are potentially harmful given dalteparin's bleeding risk. The US license is also cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and registry search for dalteparin or LMWH use in protein C deficiency and purpura fulminans (case series, guidelines)
- A comparison against standard care (protein C concentrate plus anticoagulation)
- Route compatibility and formulation assessment (the current form is injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

