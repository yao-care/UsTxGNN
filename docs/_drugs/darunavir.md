---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Darunavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor marketed in the US for HIV-1 infection. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, but the evidence is very weak: **1 clinical trial** and **0 publications**, and the trial studied HIV-1 in humans, not FIV.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the license records in the input carry no indication text, so this comes from darunavir's established use) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (the pack labels this L4, but it contains no FIV-specific preclinical or mechanism study) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (US authorizations, brand NDA and generic ANDAs combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Darunavir is an HIV-1 protease inhibitor, and its efficacy in HIV-1 infection is well established. FIV is a related lentivirus, so the prediction is understandable at a superficial level.

However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so activity against FIV cannot be assumed. The very high TxGNN score most likely reflects darunavir's HIV-1 antiviral annotation spreading to related lentiviral disease nodes in the knowledge graph. It is not independent evidence for a feline indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Randomized open-label study of boosted darunavir plus lamivudine vs. boosted darunavir plus tenofovir/emtricitabine or tenofovir/lamivudine in treatment-naïve HIV-1 patients. It does not study FIV and only supports darunavir's existing HIV-1 use (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021976 | PREZISTA (Janssen Products LP) | Film-coated tablet | Not listed in the input |
| ANDA216168 | Darunavir (Camber Pharmaceuticals) | Film-coated tablet | Not listed in the input |
| ANDA214085 | Darunavir (Viona Pharmaceuticals) | Film-coated tablet | Not listed in the input |
| ANDA212493 | Darunavir (Amneal Pharmaceuticals NY) | Film-coated tablet | Not listed in the input |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. No study tests darunavir against FIV, and the one trial found is a human HIV-1 study that only reflects the approved use. The other predicted indications are also weak. Simian immunodeficiency virus infection has only four non-human primate studies, where darunavir's role is unconfirmed and would at most be part of a background regimen. The remaining two (a rare neurodevelopmental disorder and an obsolete hyperlipidemia term) have no evidence and no plausible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data for darunavir
- In vitro data on darunavir inhibition of FIV protease and FIV replication
- Veterinary-specific evidence and regulatory pathway assessment, since this would be a human drug used in cats
- Full-text check of whether darunavir was actually part of the regimens in the SIV studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

