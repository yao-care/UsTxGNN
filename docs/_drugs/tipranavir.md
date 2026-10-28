---
layout: default
title: Tipranavir
parent: Model Prediction Only (L5)
nav_order: 1232
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "TIPRANAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
description: "Tipranavir: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: Not recorded in the local data"
---

# Tipranavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tipranavir: Simian immunodeficiency virus infection
{: .text-alpha }

## One-Sentence Summary

Tipranavir is an HIV-1 protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general drug knowledge, tipranavir is a non-peptidic HIV-1 protease inhibitor. Its efficacy in HIV infection is established, and mechanistically it may be applicable to simian immunodeficiency virus (SIV).

SIV is a closely related lentivirus with a homologous protease, so activity is biologically plausible. However, SIV infection is a veterinary and preclinical model disease, not a human clinical indication. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the approved HIV indication, not biological evidence. The mechanistic reasoning above is inferred from general knowledge only, since no trials or literature were available.

Other top-ranked predictions are weaker still:
- **Feline acquired immunodeficiency syndrome** (0.9999): the feline virus protease differs from HIV-1 protease, so cross-reactivity is uncertain.
- **Familial combined hyperlipidemia (obsolete term)** (0.9993): tipranavir is associated with raised triglycerides and cholesterol, so this link reflects an adverse effect, not a therapeutic benefit.
- **Rare neurodevelopmental disorder, prostate fibroma, Brenner tumor, benign reproductive neoplasm and benign prostate phyllodes tumor**: no plausible mechanistic rationale was identified. These appear to be model artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021814 | Aptivus | Capsule, liquid filled (oral) | Not specified (status: valid) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver failure, liver disease, hepatitis (including chronic hepatitis B and C), gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, hyperbilirubinemia (including Gilbert syndrome), blood coagulation disease, hemophilia, intracranial hemorrhage, brain neoplasm, and injury.
- **Drug Interactions**: 100 interactions were identified; 20 are listed in the data compiled for this report, mostly Moderate and two Major.
  - **Major**: acetylsalicylic acid, eluxadoline.
  - **Moderate (selected)**: antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, dulaglutide, albiglutide, chlorpropamide), dexamethasone, clarithromycin, loperamide, eliglustat, cholic acid, magnesium oxide, topical metronidazole.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials or literature (Evidence Level L5). SIV is a veterinary and preclinical model, not a human indication. Tipranavir's only US authorization is cancelled, and the knowledge graph flags substantial hepatic, bleeding and metabolic safety signals.

**To proceed, the following is needed:**
- Preclinical in vitro or in vivo data on tipranavir activity against SIV protease
- Mechanism of action data, which are currently missing
- Package insert warnings and contraindications for a formal safety screening
- Clarification of whether a human-relevant indication exists, since the top predictions are veterinary, within the existing HIV indication, or lack a plausible mechanism
- A review of the regulatory and market situation, given that the only NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

