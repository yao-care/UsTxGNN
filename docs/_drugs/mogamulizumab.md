---
layout: default
title: Mogamulizumab
parent: Model Prediction Only (L5)
nav_order: 939
evidence_level: L5
indication_count: 7
monitor_inn: "MOGAMULIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
last_modified_at: 2026-10-14
description: "Mogamulizumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Mycosis fungoides and variants"
---

# Mogamulizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is an anti-CCR4 monoclonal antibody originally used for cutaneous T-cell lymphomas such as mycosis fungoides and other T-cell lymphomas.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mycosis fungoides and variants; primary cutaneous T-cell lymphoma; peripheral T-cell lymphoma and related T-cell/NK-cell lymphomas |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761051) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, mogamulizumab is an anti-CCR4 monoclonal antibody. It mediates antibody-dependent cellular cytotoxicity against CCR4-expressing cells, mainly malignant T cells and regulatory T cells (Tregs). Its efficacy in cutaneous T-cell lymphoma comes from targeting these CCR4-expressing malignant cells.

The possible link to urothelial carcinoma is Treg depletion in the tumour microenvironment, which could enhance anti-tumour immunity and might complement checkpoint-based immunotherapy. This is a generic immuno-oncology hypothesis and is speculative. No data were provided showing CCR4 dependence in this tumour type.

The top predictions are also clustered: several related urothelial entities (prostatic urethra, renal pelvis, bladder sarcomatoid variants) have near-identical scores of about 99.4%. This suggests a shared model signal rather than independent evidence. The score should be read as a computational hypothesis only.

Other predicted indications, all also at L5 with a Hold recommendation, include HHV-8-related tumours (a somewhat more biologically coherent hypothesis, since Tregs and CCR4-expressing cells may contribute to immune evasion), ectomesenchymoma, and malignant cutaneous granular cell tumour.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761051 | POTELIGEO (Kyowa Kirin, Inc.) | Injection | Not listed in the compiled data; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / immunotherapy (monoclonal antibody against CCR4); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 83 interactions were identified in the interaction database. Examples from the data compiled for this report:
  - **Major**: deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib
  - **Moderate**: strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, alemtuzumab, alefacept, anakinra, canakinumab, azathioprine, anthrax vaccine, tetanus toxoid
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride)

  Many of the flagged agents are immunosuppressive or immunomodulatory, so combined use deserves careful review.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5). The mechanistic link is a generic Treg-depletion hypothesis, and the high score is shared across several closely related urothelial entities. The US BLA is also listed as cancelled.

**To proceed, the following is needed:**
- Confirmation of CCR4 expression and Treg involvement in urothelial carcinoma tissue (preclinical or translational data)
- A literature and trial search specific to anti-CCR4 therapy in urothelial or other solid tumours
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications, which are required for any safety screening
- Clarification of the regulatory status of BLA761051 and the availability of the product
- Comparison with the HHV-8-related tumour prediction, which has a more coherent biological rationale and may be a better lead to prioritise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

