---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 654
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Enoxaparin: From Thromboprophylaxis to Protein C Deficiency Thrombophilia

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin anticoagulant, and the supplied data do not list its approved indications.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (the approved indication text is blank for all licenses). Enoxaparin is generally used for thromboprophylaxis and thrombosis treatment, and this should be confirmed against the label. |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, enoxaparin is a low-molecular-weight heparin that potentiates antithrombin and mainly inhibits factor Xa. This reduces thrombin generation and clot formation.

Severe protein C deficiency impairs the protein C anticoagulant pathway, which normally inactivates factors Va and VIIIa. The result is a hypercoagulable state with a high risk of thrombosis. Anticoagulation is therefore biologically plausible for preventing or treating thrombosis in this condition. This reasoning comes from general pharmacology, not from the supplied dataset, and it could not be checked against source data.

There is also a caveat. Enoxaparin's existing thromboprophylaxis and thrombosis treatment indications are probably related to this prediction. The high score may therefore reflect an existing use rather than a new repurposing signal. The prediction should be checked against current labeling and clinical guidelines before further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214646 | Enoxaparin sodium (BE Pharmaceuticals Inc.) | Injection | Not provided in source data |
| ANDA076726 | Enoxaparin Sodium (Zydus Pharmaceuticals USA Inc.) | Injection, solution | Not provided in source data |
| ANDA076726 | Enoxaparin Sodium (Italfarmaco SpA) | Injection, solution | Not provided in source data |
| NDA020164 | Lovenox (Sanofi-Aventis U.S. LLC) | Injection | Not provided in source data |
| ANDA206834 | Enoxaparin Sodium (BluePoint Laboratories) | Injection | Not provided in source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score and a plausible anticoagulant rationale, but it has no supporting trials or publications (L5). The safety and mechanism data are also missing, so the case cannot advance to safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indications from the current US label, to check whether this prediction overlaps with existing thromboprophylaxis and treatment uses
- Mechanism of action data from DrugBank, to verify the mechanistic link
- A targeted literature and trial search on anticoagulation in severe (autosomal recessive) protein C deficiency, plus review of current clinical guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

