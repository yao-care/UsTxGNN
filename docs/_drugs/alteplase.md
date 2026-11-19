---
layout: default
title: Alteplase
parent: Model Prediction Only (L5)
nav_order: 270
evidence_level: L5
indication_count: 6
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
last_modified_at: 2026-11-06
description: "Alteplase: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Alteplase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Alteplase: thrombolytic (tissue plasminogen activator) → heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator that dissolves fibrin clots.
The TxGNN model predicts it may be relevant for **heparin cofactor 2 deficiency**,
but **no clinical trials and no publications** were found for this disease, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for alteplase: "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), label version 2026-01-20; accessed 2026-11-19.) Based on general knowledge, alteplase converts plasminogen to plasmin and so breaks down fibrin-rich thrombi.

Heparin cofactor II deficiency is an inherited thrombophilia, meaning a tendency to form clots. In principle, alteplase could treat an acute clot in a patient with this condition. However, it does not correct the underlying deficiency, and the link is therefore weak. No trials or literature were found to test this idea, so the prediction remains unsupported by clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103172 | Cathflo Activase | Injection, powder, lyophilized, for solution | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified in the data compiled for this report. Examples of **major** interactions include:
  - Abciximab
  - Acalabrutinib
  - Apixaban
  - Anisindione
  - Fondaparinux
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab

  Examples of **moderate** interactions include acetylsalicylic acid, ibuprofen, ketorolac, fluvoxamine, aminocaproic acid and aprotinin. Combining alteplase with other agents that affect clotting generally raises the bleeding risk.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is high (0.9972), but there is no clinical trial or publication for heparin cofactor 2 deficiency, and alteplase does not address the underlying deficiency. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Clinical or case-based evidence of alteplase use in patients with heparin cofactor II deficiency
- Mechanism-of-action data and the package insert warnings and contraindications
- A bleeding-risk assessment for patients with inherited coagulation abnormalities

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

