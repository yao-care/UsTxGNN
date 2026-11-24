---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 9
monitor_inn: "AVELUMAB"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-11-24
description: "Avelumab: predicted new indication human herpesvirus 8-related tumor (evidence level L5). In the US: 2 FDA applications (2 active)"
---

# Avelumab
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

## Avelumab: anti-PD-L1 antibody → human herpesvirus 8-related tumor
{: .text-alpha }

## One-Sentence Summary

Avelumab is an anti-PD-L1 monoclonal antibody that is marketed in the United States as an injectable product.
The TxGNN model predicts it may be useful for **human herpesvirus 8-related tumor**, but **no clinical trials and no publications** were found in the data compiled for this report to support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for avelumab: "PD-L1 may be expressed on tumor cells and tumor-infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD-L1 to the PD-1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation, and cytokine production. […] Avelumab binds PD-L1 and blocks the interaction between PD-L1 and its receptors PD-1 and B7.1." ([DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118), label version 2026-09-22; accessed 2026-11-19.) Based on general knowledge, avelumab is an antibody that blocks PD-L1, a protein that tumours use to hide from the immune system. Blocking it can allow immune cells to attack the tumour again.

Tumours linked to human herpesvirus 8, such as Kaposi sarcoma and primary effusion lymphoma, are known to involve viral immune evasion and increased activity of the PD-1/PD-L1 pathway. Blocking this pathway is therefore biologically plausible. Other PD-1 inhibitors have shown activity in Kaposi sarcoma.

This link rests only on the TxGNN prediction and general mechanistic reasoning. No trials or publications specific to this disease were supplied, so the prediction remains unverified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA761049 | BAVENCIO | EMD SERONO INC | Injectable; injection | Valid |
| BLA761078 | BAVENCIO | EMD SERONO INC | Injectable; intravenous | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Three major interactions were recorded, with lenalidomide, pomalidomide and thalidomide.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and the biological reasoning is plausible, but there are no clinical trials or publications on this disease. The evidence is model prediction only (L5).

**To proceed, the following is needed:**
- A systematic search for trials and publications on checkpoint inhibitors in HHV-8-related tumours, including Kaposi sarcoma and primary effusion lymphoma
- Detailed mechanism-of-action data for avelumab
- Package insert warnings and contraindications, with a safety review for patients with HHV-8-related disease (including those with HIV or immunosuppression)
- Review of the three major drug interactions (lenalidomide, pomalidomide, thalidomide), which are used in some HHV-8-related settings

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for avelumab is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

