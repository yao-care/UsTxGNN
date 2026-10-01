---
layout: default
title: Formaldehyde
parent: Model Prediction Only (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
---

# Formaldehyde
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

# Formaldehyde: From No Labeled Indication to Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Formaldehyde is a reactive chemical widely used as a tissue fixative and disinfectant. In the US it appears in marketed homeopathic products (for example "Formalinum"), but the data provided lists no approved indication.
The TxGNN model predicts it may be relevant to **diffuse cutaneous leishmaniasis**, but there are **0 clinical trials** and only **1 publication**, a laboratory diagnostic study in which formalin fixes tissue samples and is not a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data |
| Predicted New Indication | Leishmaniasis, diffuse cutaneous |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Formaldehyde is a reactive, cytotoxic electrophile that cross-links proteins and DNA. That is why it is used as a fixative, a disinfectant and a vaccine-inactivating agent.

The prediction does not look therapeutically grounded. The only supporting paper compares how well *Leishmania* DNA can be detected by PCR in formalin-fixed, ethanol-fixed and frozen skin biopsies. Formaldehyde appears there as a specimen preservative, not as a treatment. The high graph score most likely reflects the fixation and disinfection context rather than antileishmanial activity.

The other top predictions show the same pattern. Most are supported only by fixation-method papers, or by nothing at all.

- **Pyelonephritis** is the only one with an indirect signal. Methenamine hippurate releases formaldehyde in acidic urine and is used to prevent recurrent urinary tract infection. Two Phase 4 trials tested methenamine, not formaldehyde itself.
- **Streptococcal pneumonia and malaria** are supported only by papers where formaldehyde is a vaccine or laboratory reagent.
- **X-linked lymphoproliferative syndrome** is supported mainly by occupational-exposure studies that point toward harm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9830259](https://pubmed.ncbi.nlm.nih.gov/9830259/) | 1998 | Diagnostic methods comparison | J Dermatol | Compared detection of *Leishmania* by PCR and Southern blotting in formalin-fixed, ethanol-fixed and frozen skin biopsies from 19 leishmaniasis patients. Formalin is used only as a fixative; no treatment effect was assessed. |

## US Market Information

The data lists 11 authorizations, and 5 are shown here. None has a license number or approved indication in the source data. All appear to be homeopathic products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Formalinum (Hahnemann Laboratories) | Pellet | Not stated |
| Not listed | Formalinum (Hahnemann Laboratories) | Pellet | Not stated |
| Not listed | Formalinum (Hahnemann Laboratories) | Pellet | Not stated |
| Not listed | Formaldehyde (Professional Complementary Health Formulas) | Liquid | Not stated |
| Not listed | Formalinum (Boiron) | Pellet | Not stated |

## Safety Considerations

No package insert warnings, contraindications or drug interaction records were available. Please refer to the package insert for safety information.

The retrieved literature also raises these concerns:
- **Carcinogenicity**: Formaldehyde is considered a human carcinogen. A meta-analysis (PMID 31870335) examined occupational exposure and non-Hodgkin lymphoma risk, and other epidemiology links exposure to lymphohematopoietic cancers.
- **Local tissue toxicity**: A case report (PMID 3822522) describes ureteric stenosis, fibrotic contraction of the renal pelves and recurrent pyelonephritis after intravesical formalin instillation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for diffuse cutaneous leishmaniasis is a model output with no clinical trials. Its only publication is a diagnostic study in which formaldehyde is a specimen fixative. There is no plausible therapeutic mechanism, and formaldehyde has documented toxicity and carcinogenicity concerns.

**To proceed, the following is needed:**
- Package insert safety data (warnings, contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Any future work on the pyelonephritis or recurrent UTI signal should focus on methenamine as a formaldehyde-releasing prodrug and should not test formaldehyde directly
- Evidence of actual antileishmanial activity (in vitro or in vivo) before any further evaluation for leishmaniasis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

