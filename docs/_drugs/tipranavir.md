---
layout: default
title: Tipranavir
parent: Model Prediction Only (L5)
nav_order: 1232
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tipranavir is a non-peptidic HIV-1 protease inhibitor, marketed in the US as Aptivus for HIV-1 infection.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, an animal-model lentiviral disease.
This prediction has **0 clinical trials** and **0 publications** supporting it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the license record contains no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, tipranavir is an HIV-1 protease inhibitor. Its efficacy in HIV-1 infection is established, and mechanistically it may be applicable to SIV.

SIV is a lentivirus closely related to HIV-1, so a protease-inhibitor rationale is plausible. The high score most likely reflects the drug's strong association with HIV-1 in the knowledge graph. However, SIV is a veterinary and animal-model disease with little direct human clinical relevance. No trials or literature were supplied to show that tipranavir actually works against SIV, so activity should not be assumed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021814 | Aptivus (Boehringer Ingelheim Pharmaceuticals, Inc.) | Capsule, liquid filled (oral) | Not stated in the source record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, so the evidence level is L5. The target is an animal-model disease. The package insert warnings and the mechanism of action are also missing from the source data.

**Other predicted indications:**
- **Congenital HIV** (rank 5, score 99.83%) is the only candidate with any trial evidence. Nine HIV trials matched at the disease level, but none confirms tipranavir as an intervention, so the level is L4 (indirect evidence only). This is also a direct fit with the approved HIV-1 use rather than true repurposing.
- **Feline AIDS** (rank 2) is also a veterinary indication. Its protease substrate specificity differs from HIV-1, so activity cannot be assumed.
- **Familial combined hyperlipidemia** (rank 4) is mechanistically unfavorable, because protease inhibitors, tipranavir/ritonavir in particular, are known to raise triglycerides and cholesterol.
- **The remaining candidates** (rare neurodevelopmental disorder, prostate fibroma, Brenner tumor, benign reproductive neoplasm, benign prostate phyllodes tumor) have no identified mechanistic link and are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism of action data, for example from the DrugBank API
- Any in vitro or animal-model evidence of tipranavir activity against SIV or FIV
- If pursuing the human HIV direction, verification of the intervention arms of the matched trials and of pediatric or perinatal tipranavir use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

