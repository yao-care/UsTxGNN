---
layout: default
title: Lurbinectedin
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: From an Unrecorded Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Lurbinectedin (DrugBank ID DB12674) is a DNA-binding/transcription-inhibiting cytotoxic antineoplastic agent; its original approved indication is not recorded in the current evidence pack. The TxGNN model predicts a possible association with **Multiple Endocrine Neoplasia**, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale text states no mechanistic or empirical support was found for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (Data Gap DG002 — MOA also missing) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | Not marketed (Taiwan: Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lurbinectedin is not available in this evidence pack (Data Gap DG002, severity: High). Based on the repurposing rationale text generated alongside the prediction, lurbinectedin is characterized as a DNA-alkylating / transcription-inhibiting cytotoxic antineoplastic agent — consistent with its known pharmacological class.

However, the model's own rationale explicitly states that **no data support a mechanistic link** between this cytotoxic, transcription-inhibiting activity and Multiple Endocrine Neoplasia (MEN), an endocrine tumor syndrome. The prediction rests solely on a TxGNN knowledge-graph similarity score (rank 13,032 out of the model's full output), with no corroborating clinical or literature evidence.

Notably, 9 of the other 10 top-ranked predicted indications for this drug include diseases such as HIV infection, rheumatoid arthritis, ALS, and several veterinary/non-human conditions (feline AIDS, simian immunodeficiency virus infection, bovine rhinotracheitis) — none of which have a plausible pharmacological connection to a cytotoxic antineoplastic agent. This pattern suggests the prediction sits in a low-confidence region of the model's output space rather than reflecting a biologically grounded signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Lurbinectedin currently has 0 marketing authorizations on record and is not marketed in Taiwan. No license detail is available in the evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA alkylating / transcription inhibitor), based on repurposing-rationale description |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions should be assumed pending confirmation from the official label |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety (S1) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, decision stage S0), with zero clinical trials or publications, no confirmed mechanistic rationale, and no original-indication or MOA data on file. The surrounding top-10 predictions include multiple biologically implausible and non-human indications, further weakening confidence in this specific signal.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — Blocking gap (DG001)
- Confirmed mechanism of action via DrugBank API — High-priority gap (DG002)
- Confirmation of the drug's original approved indication(s)
- Independent literature or preclinical search specifically for lurbinectedin and endocrine tumor pathways before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

