---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 1152
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Selinexor: From Hematologic Malignancies to Drug-Induced Osteoporosis

## One-Sentence Summary

Selinexor (brand name XPOVIO) is an oral drug marketed in the US for hematologic malignancies.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but the prediction rests on a computational score alone, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hematologic malignancies (the approved indication text was not supplied in the source data) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 licence records (all listed records carry NDA212306) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Selinexor is generally described as a selective inhibitor of nuclear export (XPO1/CRM1), and it is marketed for hematologic malignancies rather than for bone-loss conditions.

The only support for the new indication is the very high TxGNN knowledge-graph score (0.992, model rank 17,172). This is a computational prediction, not clinical evidence. Any effect on bone remodeling, for example through osteoclast or osteoblast signaling, would be a hypothesis from outside this dataset and has not been verified here.

The link between the original and predicted indications therefore cannot be checked against the supplied data. Oncology and bone-loss conditions differ substantially. Any bone effect would first need to be shown in preclinical or clinical studies.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212306 | XPOVIO (Karyopharm Therapeutics Inc.) | Film-coated tablet (oral) | Not listed in the source record |

The source lists 5 identical records for NDA212306, shown here once. The reported total is 6 licence records.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (nuclear export inhibitor), used in hematologic malignancies |
| Myelosuppression Risk | Cytopenias are associated with the drug; severity grading is not available. Please refer to the package insert. |
| Emetogenicity Classification | Nausea is associated with the drug; classification is not available. Please refer to the package insert. |
| Monitoring Items | CBC (with differential) is reasonable given the cytopenia risk; please refer to the package insert for the full schedule |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

Systemic adverse effects such as fatigue, nausea, weight loss and cytopenias are associated with selinexor. No bone-safety data were provided, and a safety review would be needed before any repurposing in a population at risk of osteoporosis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score and no registered trials or publications (Evidence Level L5). Neither the mechanism nor the package insert safety data were available to support it. Bone-safety data are also missing, and systemic toxicity is a concern in an osteoporosis-risk population.

**To proceed, the following is needed:**
- Retrieve the package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain verified mechanism of action data, for example from DrugBank
- Search for preclinical or clinical evidence on selinexor and bone metabolism, such as osteoclast/osteoblast studies and bone-density findings in existing patients
- Assess route and formulation compatibility with the target population (currently pending)
- Confirm the approved indication text for NDA212306 so the original-to-new indication comparison can be made

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

