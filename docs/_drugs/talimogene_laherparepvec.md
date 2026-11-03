---
layout: default
title: Talimogene Laherparepvec
parent: Model Prediction Only (L5)
nav_order: 1197
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-03
monitor_inn: "TALIMOGENE LAHERPAREPVEC"
predicted_indications: ["glottis squamous cell carcinoma", "lung occult squamous cell carcinoma", "rectal cloacogenic carcinoma", "gallbladder adenosquamous carcinoma"]
description: "Talimogene Laherparepvec: predicted new indication Glottis squamous cell carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Talimogene Laherparepvec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Talimogene Laherparepvec: Glottis squamous cell carcinoma
{: .text-alpha }

## One-Sentence Summary

Talimogene laherparepvec (T-VEC) is an oncolytic herpes virus originally used to treat melanoma.
However, **no clinical trials and no publications** were found in the data compiled for this report, so this remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Glottis squamous cell carcinoma |
| TxGNN Prediction Score | 0.9907 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge, T-VEC is an oncolytic herpes simplex virus type 1. It replicates inside tumour cells and expresses GM-CSF to promote anti-tumour immunity. It is used for melanoma, so a cutaneous malignant melanoma subtype is biologically plausible.

The label "CMM7" is ambiguous and should be checked against the disease ontology before further work. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature support this specific subtype.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Main Concern |
|------|------|------|------|
| 4 | Glottis squamous cell carcinoma | 0.9907 | Conceptual rationale from head and neck cancer work, but airway-adjacent injection is risky. |
| 5 | Lung occult squamous cell carcinoma | 0.9905 | No visible lesion to inject. |
| 6 | Rectal cloacogenic carcinoma | 0.9901 | Only a weak, indirect rationale. |
| 7 | Gallbladder adenosquamous carcinoma | 0.9901 | Deep-seated tumours that are hard to inject. The rationale is speculative. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125518 | Imlygic (Amgen Inc) | Injection, suspension | Status: valid |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (oncolytic virus) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records, and 20 were reviewed here. Most are rated Major. Key groups:
  - **Corticosteroids (Major):** hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisone, prednisolone.
  - **Immunosuppressive or cytotoxic agents (Major):** dexrazoxane, mercaptopurine, trimetrexate, levamisole.
  - **Radiopharmaceuticals and radio-immunotherapy (Major):** iobenguane (I-131), ibritumomab tiuxetan, tositumomab (with and without I-131).
  - **Other biologics (Major):** dupilumab.
  - **Antivirals (Moderate):** acyclovir (including topical) and topical penciclovir.

Other safety information, including warnings and contraindications, is not available here. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no trials or publications. The US license is cancelled, and the mechanism-of-action and label safety data are missing.

**To proceed, the following is needed:**
- Verify what "CMM7" refers to in the disease ontology.
- Obtain the US package insert (warnings and contraindications), which is a blocking gap for safety screening.
- Obtain mechanism-of-action data from DrugBank.
- Run a targeted search of trials and literature for T-VEC in the predicted indications.
- Clarify the reason for the license cancellation and the current availability of the product.
- Assess route compatibility, since T-VEC requires intralesional injection into accessible lesions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

