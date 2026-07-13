---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 572
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Darunavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Darunavir is a second-generation HIV protease inhibitor approved globally for HIV-1/HIV-2 infection treatment, though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (feline AIDS)**,
with **1 clinical trial** (Grade C indirect relevance only) and **0 publications** directly supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (no Taiwan license; globally approved for HIV — derived from mechanistic context) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Darunavir is a second-generation HIV protease inhibitor. It works by binding to the active site of the HIV-1/HIV-2 protease enzyme and blocking cleavage of the Gag-Pol polyprotein precursor, thereby preventing the maturation of newly formed viral particles into infectious virions. Detailed mechanism of action data from the Taiwan regulatory database is currently unavailable, but this mode of action is well-established in the global literature.

The prediction is based on structural homology between HIV and Feline Immunodeficiency Virus (FIV). FIV, the causative agent of feline AIDS, belongs to the same lentivirus family as HIV. Because the FIV protease shares structural similarities with the HIV-1 protease, the TxGNN knowledge graph infers a cross-species inhibition potential. In principle, a protease inhibitor designed for HIV may bind to the FIV protease active site to some degree.

However, darunavir was optimized specifically for human HIV-1/HIV-2 protease binding. Its binding affinity to FIV protease has not been measured in any published in vitro or in vivo study. No pharmacokinetic or safety data in cats are available. The only clinical trial retrieved (NCT02770508) is a human HIV-1 treatment study and carries only Grade C (mechanistic reference) relevance to feline disease. This prediction currently rests entirely on knowledge-graph inference, not experimental evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared ritonavir-boosted darunavir + lamivudine versus ritonavir-boosted darunavir + TDF/FTC or TDF/3TC in treatment-naïve human HIV-1 patients. Demonstrates darunavir efficacy and safety in human HIV-1 infection, but has no direct applicability to feline disease, FIV biology, or veterinary indications. **Grade C — mechanistic cross-reference only.** |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Darunavir is not currently licensed or marketed in Taiwan. No NDA or authorization records are on file with the Taiwan FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Because darunavir is not approved in Taiwan, no local label is available. For the global prescribing information (Prezista®, Janssen), refer to the FDA or EMA product label. Clinicians and veterinarians should be aware that HIV protease inhibitors as a class are associated with dyslipidemia, hepatotoxicity, and drug–drug interactions (particularly via CYP3A4 inhibition with ritonavir boosting), none of which have been characterized in cats.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.97%) grounded in the structural homology between HIV and FIV proteases, but no direct experimental evidence exists to support darunavir's use in feline AIDS. The single clinical trial identified concerns human HIV-1 treatment and is not applicable to veterinary medicine. This remains a purely model-driven hypothesis at the L4 (mechanistic inference) level.

**To proceed, the following is needed:**
- In vitro binding affinity assay of darunavir against purified FIV protease (to confirm cross-species inhibition)
- In vitro antiviral activity data against FIV in feline cell lines
- Pharmacokinetic study in cats to determine oral bioavailability, half-life, and safe dosing range
- In vivo proof-of-concept study in a feline FIV infection model
- Veterinary toxicology assessment (especially hepatic and renal parameters in cats, which metabolize drugs differently from humans)
- Evaluation of whether ritonavir boosting is necessary and tolerable in cats
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

