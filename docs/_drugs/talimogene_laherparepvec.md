---
layout: default
title: Talimogene Laherparepvec
parent: Model Prediction Only (L5)
nav_order: 1197
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
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

# Talimogene Laherparepvec: From Melanoma to CMM7 (Cutaneous Malignant Melanoma Subtype, Label to Be Verified)

## One-Sentence Summary

Talimogene laherparepvec (T-VEC) is an oncolytic herpes virus originally used to treat melanoma.
The TxGNN model predicts it may be effective for **CMM7**, with a score of 99.2%.
However, **no clinical trials and no publications** were found in the data compiled for this report, so this remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma (from the knowledge graph; no approved indication text is recorded in the US license data) |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA125518, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge, T-VEC is an oncolytic herpes simplex virus type 1. It replicates inside tumour cells and expresses GM-CSF to promote anti-tumour immunity. It is used for melanoma, so a cutaneous malignant melanoma subtype is biologically plausible.

The label "CMM7" is ambiguous and should be checked against the disease ontology before further work. The TxGNN score reflects graph proximity only. No trials or literature support this specific subtype.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Main Concern |
|------|------|------|------|
| 2 | Pediatric leptomeningeal melanoma | 99.15% | Intrathecal delivery of a replication-competent HSV-1 raises neurovirulence concerns (e.g., encephalitis). Pediatric use adds uncertainty. |
| 3 | Epithelioid cell uveal melanoma | 99.13% | Different drivers (GNAQ/GNA11) and mainly hepatic spread. Ocular or hepatic delivery would be non-standard. |
| 4 | Glottis squamous cell carcinoma | 99.07% | Conceptual rationale from head and neck cancer work, but airway-adjacent injection is risky. |
| 5 | Lung occult squamous cell carcinoma | 99.05% | No visible lesion to inject. |
| 6 | Rectal cloacogenic carcinoma | 99.01% | Only a weak, indirect rationale. |
| 7 | Gallbladder adenosquamous carcinoma | 99.01% | Deep-seated tumours that are hard to inject. The rationale is speculative. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125518 | Imlygic (Amgen Inc) | Injection, suspension | Status: cancelled |

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
The prediction is supported only by the TxGNN model score, with no trials or publications. The predicted label (CMM7) is ambiguous. The US license is cancelled, and the mechanism-of-action and label safety data are missing.

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

