---
layout: default
title: Denileukin Diftitox
parent: Model Prediction Only (L5)
nav_order: 581
evidence_level: L5
indication_count: 4
---

# Denileukin Diftitox
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Denileukin Diftitox: From Cutaneous T-Cell Lymphoma to Plasmacytoma

## One-Sentence Summary

Denileukin diftitox (US brand LYMPHIR) is an IL-2/diphtheria toxin fusion protein approved for cutaneous T-cell lymphoma (CTCL).
The TxGNN model predicts it may be effective for **plasmacytoma**, with a very high score (99.87%).
However, there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (CTCL) |
| Predicted New Indication | Plasmacytoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761312) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the database. From the supplied information, denileukin diftitox fuses interleukin-2 (IL-2) to diphtheria toxin. It targets cells that express the IL-2 receptor (CD25) and kills them. This is the basis of its use in CTCL, a lymphoid malignancy.

The link to plasmacytoma is weak on current data. Plasma cell neoplasms do not typically express CD25 as a defining feature, so the drug's targeting logic may not carry over. This is an inference, not evidence from the supplied data. The high TxGNN score reflects a knowledge-graph pattern (a lymphoid or hematologic cancer drug matched to another blood cancer). It is not a demonstrated mechanistic or clinical connection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA 761312 | LYMPHIR (Citius Pharmaceuticals, Inc.) | Injection, powder, lyophilized, for solution |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (IL-2/diphtheria toxin fusion protein, an immunotoxin) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or publications for plasmacytoma. The CD25-targeting mechanism also fits poorly with plasma cell neoplasms.

**To proceed, the following is needed:**
- Evidence that plasmacytoma cells express CD25 (or another route to drug sensitivity), plus preclinical data
- Full package insert warnings and contraindications
- Formal mechanism of action data
- A separate look at other predicted indications. Of these, only *metastatic neoplasm* (rank 4) has supporting studies. It has 13 registered trials and 7 publications, but the evidence is mixed and no Phase 3 RCT exists. Whether the drug actually depletes regulatory T cells is disputed (PMID 16224276 reports it did not), so this remains a research question rather than a ready candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

