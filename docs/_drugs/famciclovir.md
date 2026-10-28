---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 691
evidence_level: L5
indication_count: 9
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
last_modified_at: 2026-10-14
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L4). Approved use: Herpes zoster"
---

# Famciclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia
{: .text-alpha }

## One-Sentence Summary

Famciclovir is an oral antiviral prodrug of penciclovir, originally used to treat herpes zoster (shingles).
The TxGNN model predicts it may be effective for **post-infectious neuralgia** (postherpetic neuralgia), but the only clinical trial found tests a different drug (oxycodone), and **no publications** directly support this prediction.
Evidence is therefore limited to model prediction and indirect mechanistic reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 4) |
| Number of NDAs | 4 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, famciclovir is a prodrug of penciclovir, whose triphosphate form inhibits varicella-zoster virus (VZV) DNA polymerase.

Postherpetic neuralgia is the most common complication of herpes zoster. Starting antiviral treatment early in acute shingles may limit viral replication and nerve damage, which could in turn reduce the risk or severity of subsequent neuralgia.

This link is indirect. Famciclovir is already used for the acute zoster episode, and no study retrieved here shows that it prevents or treats postherpetic neuralgia once established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the investigational agent, so this offers background context only. |

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## US Market Information

Famciclovir is marketed in the US, and 4 US authorizations are currently valid. No approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202438 | Famciclovir (Proficient Rx LP) | Film-coated tablet | Not recorded (valid) |
| ANDA201022 | Famciclovir (Macleods Pharmaceuticals) | Film-coated tablet | Not recorded (valid) |
| ANDA091114 | Famciclovir (Rising Pharma) | Film-coated tablet | Not recorded (valid) |
| ANDA077487 | Famciclovir (Teva Pharmaceuticals USA) | Film-coated tablet | Not recorded (valid) |

---

## Safety Considerations

- **Contraindications (model-derived associations, not label text)**: kidney disease and pyoureter are flagged for famciclovir by the TxGNN model (deep learning). This output may reflect similarities the model learned between related diseases, not biological evidence.
- **Drug Interactions**: 84 potential interactions were identified, but severity levels are unclassified. Examples include calcitriol, doxycycline, metformin, omeprazole, morphine, prednisone, simvastatin and vancomycin.

For warnings and full safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the supporting evidence is only a model prediction plus an indirect mechanistic argument. The sole trial found studies oxycodone rather than famciclovir, and no literature was retrieved.

**To proceed, the following is needed:**
- Clinical studies or systematic reviews testing whether famciclovir reduces the incidence or severity of postherpetic neuralgia
- Detailed mechanism of action data
- Package insert warnings and contraindications (not yet obtained, and required for safety screening)
- Clarification of current US market and supply status
- Renal safety assessment, given the knowledge-graph link to kidney disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

