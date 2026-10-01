---
layout: default
title: Mogamulizumab
parent: Model Prediction Only (L5)
nav_order: 939
evidence_level: L5
indication_count: 7
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab (brand name POTELIGEO) is an anti-CCR4 antibody. By general knowledge it is used for cutaneous T-cell lymphomas, although the Evidence Pack does not list an approved indication.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**.
This is a model prediction only: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack. General knowledge: relapsed/refractory cutaneous T-cell lymphoma (mycosis fungoides / Sézary syndrome) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761051) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Mogamulizumab is generally known as an antibody against CCR4, a chemokine receptor found on some T cells, including regulatory T cells (Tregs). It depletes CCR4-positive cells.

One possible link is that removing Tregs could reduce immunosuppression in the tumor microenvironment and strengthen the anti-tumor immune response. Urothelial tumors are often immunologically active, so this idea is not implausible. However, it is speculative. No trial, publication, or preclinical evidence in the data shows that CCR4 is relevant in this disease.

The same drug also ranks high for six other rare tumors:
- kidney pelvis sarcomatoid transitional cell carcinoma
- infiltrating bladder urothelial carcinoma, sarcomatoid variant
- renal pelvis papillary urothelial carcinoma
- human herpesvirus 8-related tumor
- ectomesenchymoma
- malignant cutaneous granular cell skin tumor

All seven have scores of 0.99 or higher. The four urothelial predictions likely share one graph-derived signal rather than providing independent support. For the last two, the data suggest the prediction may reflect graph-topology artifacts or a general "skin tumor" association.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761051 | POTELIGEO (Kyowa Kirin, Inc.) | Injection | — |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / immunotherapy (monoclonal antibody), not a conventional cytotoxic chemotherapy |

Please refer to the package insert warnings and precautions for myelosuppression risk, emetogenicity, monitoring items, and handling requirements.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score, with no clinical trials, no literature, and no supported mechanism. Package insert safety data are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Preclinical evidence that CCR4 or CCR4-positive Tregs matter in urothelial carcinoma
- A literature and trial search that confirms the absence of evidence and tests the CCR4 hypothesis
- A route compatibility assessment (currently pending)
- The approved indication text, to define the original indication and its similarity to the predicted one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

