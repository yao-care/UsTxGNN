---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From an Unrecorded Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is a selective FGFR1-3 inhibitor marketed in the US as an oral tablet (PEMAZYRE). The Evidence Pack does not record its approved indication.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** with a score of 99.71%. However, **0 clinical trials** and **0 publications** support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data (approved indication text is empty in all license records) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license records (all under NDA213736) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not currently available. What is known is that pemigatinib is a selective inhibitor of FGFR1, FGFR2 and FGFR3. FGF/FGFR signaling has a loose biological connection to endocrine tumor growth.

The link is weak, though. The defining drivers of multiple endocrine neoplasia (MEN1 and RET) are not FGFR-dependent, so there is no clear mechanistic path from FGFR inhibition to this disease. No supporting trial or paper was found. The high score is best read as a knowledge-graph signal that needs independent validation.

Other predicted indications are ranked below this one, and most are weaker:
- **HER2-positive breast carcinoma** (score 99.49%) is biologically plausible, because FGFR1 amplification is implicated in breast cancer biology and in resistance to HER2-directed therapy. The only paper retrieved is a general review of kinase inhibitors with no indication-specific data.
- **Axial spondylometaphyseal dysplasia** touches on FGFR's role in skeletal development, but inhibiting FGFR in a developing skeleton carries risk.
- **Amenorrhea, cytomegalovirus infection and ALS-related entries** have no plausible mechanism and no evidence.
- **Two veterinary diseases** (infectious bovine rhinotracheitis and malignant catarrh) are likely knowledge-graph artifacts with no human relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213736 (3 identical records) | PEMAZYRE (Incyte Corporation) | Tablet (oral) | Not listed in the data |

## Cytotoxicity

Pemigatinib is a kinase inhibitor developed for oncology, so it is treated here as an antineoplastic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Other Safety Concerns**: The Evidence Pack notes hyperphosphatemia and ocular toxicity as safety concerns. It also notes that CNS data are limited.

Please refer to the package insert for the full warnings and contraindications. The Evidence Pack does not include them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5), with no trials or literature. The MEN-defining drivers are not FGFR-dependent, so the mechanistic link is weak. Package insert warnings are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), which is a blocking gap
- The approved indication text and mechanism-of-action data (DrugBank)
- Preclinical or literature evidence that FGFR signaling drives endocrine tumors in MEN
- A review of whether the HER2-positive breast carcinoma prediction, the only one with any retrieved literature, warrants a closer look

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

