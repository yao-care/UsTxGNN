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

# Talimogene Laherparepvec: From Cutaneous Melanoma to CMM7

## One-Sentence Summary

Talimogene laherparepvec (T-VEC, marketed as Imlygic) is an oncolytic herpes virus, marketed in the US for injectable, unresectable cutaneous melanoma lesions.
The TxGNN model predicts it may be effective for **CMM7**, an ambiguous knowledge-graph disease label.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unresectable cutaneous melanoma lesions (from the mechanism-of-action rationale; the license record has no indication text) |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records carry the same number, BLA125518) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. The rationale notes that T-VEC is an oncolytic HSV-1 engineered to express GM-CSF. It is thought to lyse tumor cells directly and to draw in dendritic cells that prime an anti-tumor immune response.

The predicted indication "CMM7" is likely a melanoma-related label, which would make the prediction biologically plausible. But the label is ambiguous and has not been mapped to a defined melanoma subtype. Until that mapping is done, the link to cutaneous melanoma cannot be confirmed.

The model also ranked six other indications, all with scores of about 99% and all at evidence level L5:
- pediatric leptomeningeal melanoma
- epithelioid cell uveal melanoma
- glottis squamous cell carcinoma
- lung occult squamous cell carcinoma
- rectal cloacogenic carcinoma
- gallbladder adenosquamous carcinoma

Several of these raise practical concerns, including CNS delivery, tumor sites that cannot be injected, airway safety, and biology that differs from cutaneous melanoma. No route compatibility or safety data were provided for any of them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125518 | Imlygic (Amgen Inc) | Injection, suspension | Not listed in the provided data |

The same BLA appears twice in the source data, so it is listed once here. The only route is injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (oncolytic viral therapy), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert; this is a live replicating virus, so handling should follow label instructions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5), with no registered trials or publications. The top-ranked disease label, CMM7, is ambiguous and has not been mapped to a defined disease. The drug's safety and indication data are also incomplete.

**To proceed, the following is needed:**
- Map "CMM7" to a defined melanoma subtype and confirm its relationship to cutaneous melanoma
- Obtain the FDA package insert (warnings, contraindications, approved indication text). The absence of this data is a blocking gap for safety screening.
- Obtain DrugBank mechanism-of-action data
- Search for clinical trials and literature on the mapped indication
- Assess route feasibility, since intralesional injection may not be possible in many of the predicted tumor sites
- Evaluate the safety of a live replicating herpesvirus in each proposed setting, especially pediatric and CNS disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

