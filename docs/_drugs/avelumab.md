---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
monitor_inn: "AVELUMAB"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-10-14
description: "Avelumab: predicted new indication Human herpesvirus 8-related tumor (evidence level L5). Approved use: Cutaneous neuroendocrine carcinoma"
---

# Avelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Avelumab: From Cutaneous Neuroendocrine Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab is an anti-PD-L1 antibody, originally used for cutaneous neuroendocrine carcinoma (Merkel cell carcinoma).
The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumor**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score and general mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous neuroendocrine carcinoma |
| Predicted New Indication | Human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761049) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, avelumab is an anti-PD-L1 antibody that blocks the PD-1/PD-L1 immune checkpoint, restoring T-cell activity against tumor cells.

HHV-8-related tumors (for example Kaposi sarcoma and primary effusion lymphoma) involve viral immune evasion and upregulation of the PD-1/PD-L1 axis, so checkpoint blockade is biologically plausible. Other PD-1 inhibitors have shown activity in Kaposi sarcoma. However, this link rests only on the TxGNN prediction and general mechanistic reasoning, with no trials or literature to confirm it.

### Other Predicted Indications

The model also produced other predictions. They fall into three groups with very different credibility:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Prostatic urethra urothelial carcinoma | 99.92% | L4 | Same lineage as the approved urothelial carcinoma use (maintenance therapy after platinum chemotherapy); indirect evidence only, subsite data needed. Flagged as a research question. |
| Kidney pelvis sarcomatoid transitional cell carcinoma | 99.91% | L4 | Upper-tract urothelial carcinoma with sarcomatoid features; indirect rationale only. Flagged as a research question. |
| Middle ear neuroendocrine tumor | 99.97% | L5 | Loose neuroendocrine-lineage rationale; PD-L1 dependence not established. |
| Malignant cutaneous granular cell skin tumor | 99.97% | L5 | Only a generic PD-L1 immune-escape rationale. |
| Ectomesenchymoma | 99.97% | L5 | No specific link to PD-L1 biology. |
| ADA deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-severe combined immunodeficiency | 99.91%–99.95% | L5 | Immunodeficiency disorders with no plausible mechanism; likely graph-based artifacts, and immune activation could be unsafe in these patients. |

Among all ten predictions, the two urothelial carcinoma subsites have the most credible rationale, even though the top-ranked prediction by score is the HHV-8-related tumor.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761049 | BAVENCIO | Injection, solution, concentrate | Not listed (status: cancelled) |

The only US authorization on record is listed as cancelled. The product is an injectable, so any new indication would also need an injectable route.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody) |
| Myelosuppression Risk | Low (not a conventional cytotoxic agent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: Three Major-level interactions were identified, all with immunomodulatory agents: lenalidomide, pomalidomide, and thalidomide.

Please refer to the package insert for other safety information, including warnings and contraindications.

For the immunodeficiency-related predictions, immune activation from checkpoint blockade could carry additional risk in severely immunocompromised patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score (L5) and a plausible but unverified mechanism, with no trials or literature. The product's US license is also cancelled. The two urothelial carcinoma subsite predictions are better candidates for follow-up as research questions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical trials and literature on avelumab in HHV-8-related tumors, such as Kaposi sarcoma
- Subsite-specific data for prostatic urethra and renal pelvis urothelial carcinoma
- Review of the US market status and route compatibility for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

