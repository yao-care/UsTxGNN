---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From NSAID Anti-Inflammatory Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation, and it is marketed in the US as tablets and ophthalmic drops.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied US license records |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 (the five listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Flurbiprofen belongs to the NSAID class, which works by non-selective COX-1/COX-2 inhibition and so reduces prostaglandin-mediated inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia in the CDMP1/GDF5 pathway. COX inhibition has no plausible disease-modifying link to this pathway.

The very high score most likely reflects proximity to other skeletal phenotypes in the knowledge graph rather than real pharmacology. The prediction should be treated as a probable graph artifact until independent evidence appears.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074447 | Flurbiprofen Sodium (Proficient Rx LP) | Solution/drops | Not provided in the record |
| ANDA074447 | Flurbiprofen Sodium (Bausch & Lomb Incorporated) | Solution/drops | Not provided in the record |
| ANDA074447 | Flurbiprofen Sodium (Amici Pharmaceuticals LLC) | Solution/drops | Not provided in the record |
| ANDA074431 | Flurbiprofen (Genus Lifesciences) | Tablet | Not provided in the record |
| ANDA074431 | Flurbiprofen (Bryant Ranch Prepack) | Tablet, film coated | Not provided in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature and no plausible mechanism. It is Level L5, a model prediction only, so it should not advance.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications and labeled indications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Any independent evidence, such as case reports or preclinical data, linking COX inhibition to this condition

**Note on other predictions:** Among the ten predicted indications for this drug, only **ankylosing spondylitis** (rank 8, score 99.97%) has supporting evidence. It has 20 PMIDs, including several 1974–1986 double-blind comparative trials against indomethacin, phenylbutazone and naproxen. It is rated L2 and "Proceed with Guardrails". It is probably an established NSAID use rather than true repurposing, so check it against the label and the full texts. It would be the better candidate for a dedicated report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

