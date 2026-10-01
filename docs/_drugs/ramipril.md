---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 1107
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Antihypertensive Use to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Ramipril is an ACE inhibitor, a class used to lower blood pressure and protect the kidneys and blood vessels.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**.
The prediction rests on the model score alone: **0 clinical trials** are registered, and none of the **20 retrieved publications** studies ramipril in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied US label text; ramipril is an ACE inhibitor (antihypertensive/renoprotective class) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (mix of ANDA and NDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ramipril is not available in the supplied record. Ramipril is an ACE inhibitor. It lowers angiotensin II-mediated vasoconstriction and vascular remodeling. Since the renin-angiotensin system is thought to contribute to pulmonary vascular remodeling, the link to pulmonary hypertension is plausible.

The link is also non-specific and unproven. The model score is the only support for this pair. ACE inhibitors can also blunt hypoxic pulmonary vasoconstriction. In patients with lung disease this could worsen gas exchange, so the drug could be harmful in this specific setting.

A closely related prediction, pulmonary hypertension with unclear multifactorial mechanism (rank 2, same score), has no trials or literature either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The search returned 20 papers, but they are general hypoxia biology reviews and basic research. None examines ramipril or ACE inhibitors, and none addresses pulmonary hypertension treatment. They are not evidence for this prediction. Examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia and brain aging; neurodegeneration vs. neuroprotection |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Clinical evidence and molecular mechanisms of hypoxia-induced cognitive impairment |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | Four basic mechanisms of hypoxemia; no drug data |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | Cellular responses to hypoxia in vascular disease, inflammation and cancer |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic research | Adv Sci (Weinh) | Hypoxia tolerance and glycolysis in gastric cancer cells; unrelated to ramipril |

## US Market Information

The supplied records contain no approved-indication text for any authorization.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091604 | Ramipril | Capsule | A-S Medication Solutions |
| ANDA091604 | Ramipril | Capsule | Rising Pharma Holdings, Inc. |
| ANDA078832 | Ramipril | Capsule | Zydus Lifesciences Limited |
| ANDA078832 | Ramipril | Capsule | Zydus Pharmaceuticals USA Inc. |
| NDA219757 | Vostally | Solution | Metacel Pharmaceuticals, LLC |

The oral capsule is the established route. Vostally is a solution formulation.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.93% score is a model prediction with no supporting trials or on-target literature. ACE inhibition may also worsen oxygenation in hypoxic lung disease, so the mechanistic argument is weak and possibly unfavorable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the current safety gap blocks safety screening)
- Mechanism-of-action data from DrugBank
- A targeted literature search for ACE inhibitors and pulmonary hypertension, especially effects on hypoxic pulmonary vasoconstriction and gas exchange
- Preclinical or early clinical data in hypoxic pulmonary hypertension models before any further investment

For comparison, **cerebral artery occlusion** (rank 10) has better support: one completed Phase 2 trial (NCT00005928, indirect vascular endpoints) and several rodent and human cerebral blood flow studies. It is at L4 and stage S1 (Research Question), and is the stronger candidate for follow-up among the predictions reviewed.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

