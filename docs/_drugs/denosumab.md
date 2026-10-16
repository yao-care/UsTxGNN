---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a RANKL inhibitor antibody, originally used to treat osteoporosis (including postmenopausal and drug-induced osteoporosis).
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but currently there are **0 clinical trials** and **0 directly relevant publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (postmenopausal osteoporosis, drug-induced osteoporosis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 10 listed authorizations are cancelled) |
| Number of NDAs | 10 (all BLAs) |
| Recommended Decision | Hold |

A second, related prediction, **diabetic retinopathy** (score 99.23%, Evidence Level L4, Hold), is discussed in the evidence sections below because it is the only prediction with any supporting literature.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, denosumab is a monoclonal antibody that inhibits RANKL, a key signal for bone resorption, and its efficacy in osteoporosis is established. Mechanistically, it may be applicable to diabetic retinopathy only through speculative routes.

RANKL/RANK signaling has been linked to inflammation, vascular calcification and bone-vascular crosstalk. This could plausibly relate to microvascular disease, but this link is **not established for the retina**, and the supplied data do not support any direct retinal mechanism.

The only indirect signal comes from a 2024 cohort analysis with meta-analysis, which suggests denosumab-treated osteoporosis patients had a lower incidence of type 2 diabetes and fewer foot ulcers compared with bisphosphonates. This points to possible diabetes-level benefits, but any retinopathy benefit would be inferred, not demonstrated.

## Clinical Trial Evidence

Currently no related clinical trials registered, for either severe nonproliferative diabetic retinopathy or diabetic retinopathy.

## Literature Evidence

No literature was found for severe nonproliferative diabetic retinopathy. For the related prediction of diabetic retinopathy, two indirect publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Likely observational cohort with meta-analysis (design not fully verified) | Diabetes, Obesity & Metabolism | Evaluates denosumab's effect on type 2 diabetes incidence and on microvascular (including retinopathy) and macrovascular complications and mortality, versus bisphosphonates. Suggests reduced diabetes incidence, foot ulceration and mortality; no retinopathy-specific benefit is shown. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observational / risk assessment | Cureus | Fracture risk assessment with the FRAX tool in adults with type 2 diabetes. Not specific to denosumab and unrelated to retinopathy efficacy. |

## US Market Information

All 10 authorizations are listed as cancelled; none are currently valid. Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761439 | XTRENBO | Injection | Not available |
| BLA761398 | CONEXXENCE | Injection | Not available |
| BLA761362 | JUBBONTI | Injection | Not available |
| BLA761404 | Denosumab-BMWO | Injection | Not available |
| BLA761444 | BILDYOS | Injection, solution | Not available |

Five further authorizations are also cancelled: XGEVA (BLA125320), OSPOMYV (BLA761392), BOSAYA (BLA761436), Oziltus (BLA761457) and Boncresa (BLA761456).

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The 20 retrieved are all rated Moderate. The main groups are:
  - Corticosteroids: hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone
  - Immunosuppressants and immunomodulators: tacrolimus, mercaptopurine, levamisole, dupilumab
  - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, iobenguane (I-131), tositumomab (with and without I-131)
  - Others: trimetrexate, corticotropin, tetracosactide

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions have high TxGNN scores (99.63% and 99.23%) but no clinical trials and no literature that directly shows a benefit on retinopathy. The mechanistic link is speculative, and the drug's US authorizations are all cancelled. Evidence is insufficient to advance.

**To proceed, the following is needed:**
- Mechanism of action data, and preclinical evidence on whether RANKL/RANK signaling affects retinal microvasculature
- Targeted literature review for denosumab and diabetic retinopathy, including whether the 2024 cohort study reports retinopathy outcomes separately
- FDA package insert warnings and contraindications (currently blocking for safety screening)
- Clarification of the current US regulatory status, since all listed authorizations are marked cancelled
- Assessment of route compatibility (denosumab is injectable; any ocular indication would need route and dosing evaluation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

