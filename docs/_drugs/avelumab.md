---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Avelumab: From Merkel Cell and Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab is an anti-PD-L1 antibody marketed in the US as BAVENCIO. The supplied license record does not list an approved indication, so its established uses (Merkel cell carcinoma and urothelial carcinoma) come from the mechanistic notes in the pack. The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumor**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied license record (established use in Merkel cell carcinoma and urothelial carcinoma, per the mechanistic notes) |
| Predicted New Indication | Human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 99.97% (rank 1250; scores for this drug are all near 100%, so the value does not discriminate between candidates) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761049) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Avelumab is an anti-PD-L1 monoclonal antibody. Detailed mechanism-of-action data is not available in the supplied record. The general class mechanism is that blocking PD-L1 releases the brake on T cells, so the immune system can attack tumor cells again.

HHV-8-driven tumors, such as Kaposi sarcoma and primary effusion lymphoma, are virus-associated and may express PD-L1. Checkpoint blockade is therefore biologically plausible. The link is theoretical: no trial, literature or PD-L1 expression data for these tumors was supplied.

The TxGNN score should be read with caution. Because all scores for this drug are close to 1, the model cannot tell strong candidates from weak ones by score alone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761049 | BAVENCIO (EMD Serono, Inc.) | Injection, solution, concentrate | Not specified in the supplied record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (immune checkpoint inhibitor, monoclonal antibody) |
| Myelosuppression Risk | Low, as expected for the class (not a conventional cytotoxic agent); please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low, as expected for the class |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

No drug interactions were found in the queried database. Please refer to the package insert for warnings, contraindications and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests only on a plausible mechanism, with no trials or publications and an L5 evidence level. The package insert safety data has also not yet been obtained.

Other predictions in the same list vary in credibility:
- Prostatic urethra urothelial carcinoma (rank 9) and kidney pelvis sarcomatoid transitional cell carcinoma (rank 10) are the most credible, because they are close to avelumab's established urothelial use. Rank 10 has one completed retrospective observational study (n=79), which is not confirmed to include this subtype.
- The immunodeficiency predictions (adenosine deaminase deficiency, reticular dysgenesis, Immunoerythromyeloid hypoplasia, non-severe combined immunodeficiency) have no plausible mechanism and are likely graph artifacts.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications), which is currently blocking the safety screening
- Detailed mechanism-of-action data from DrugBank
- A search for HHV-8-related tumor (Kaposi sarcoma, primary effusion lymphoma) trials and case reports with anti-PD-(L)1 agents, plus PD-L1 expression data for these tumors
- Consideration of prioritizing the urothelial-related candidates (ranks 9 and 10) for evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

