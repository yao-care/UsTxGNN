---
layout: default
title: Flortaucipir F-18
parent: Model Prediction Only (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
monitor_inn: "Flortaucipir F-18"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "hairy cell leukemia", "hairy cell leukemia variant", "hereditary neurocutaneous angioma", "placental hemangioma", "pseudoallergy", "skin disease", "primary bone lymphoma", "early T cell progenitor acute lymphoblastic leukemia"]
---

# Flortaucipir F-18
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

# Flortaucipir F-18: From Tau PET Imaging to Anaphylaxis (Prediction Not Supported)

## One-Sentence Summary

Flortaucipir F-18 is a diagnostic PET radiotracer that binds tau protein aggregates in the brain; it is not a therapeutic drug.
The TxGNN model predicts it may be effective for **Anaphylaxis**, but **0 clinical trials** and **0 publications** support this direction.
The prediction appears to be a computational artifact, not a credible therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available US license data (known use: tau PET imaging, per the drug's mechanism) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, flortaucipir F-18 is a diagnostic PET radiotracer that binds tau aggregates (paired helical filaments) in the brain.

The prediction is **not mechanistically reasonable**. Flortaucipir has no known immunomodulatory or mast-cell-stabilizing activity relevant to anaphylaxis. The high score (0.982) most likely reflects graph-based propagation in a sparsely annotated drug record rather than real biology. If anything, hypersensitivity is a potential adverse event of injected agents, not a therapeutic target.

The same applies to the other top-ranked predictions:

- **Anaphylaxis cluster** (food-dependent exercise-induced anaphylaxis, pseudoallergy): no plausible mechanism, likely the same graph artifact.
- **Hematologic malignancies** (hairy cell leukemia and its variant, primary bone lymphoma, early T cell progenitor ALL): the drug has no cytotoxic or targeted activity, and a microdose tracer is not a therapeutic agent.
- **Vascular disorders** (hereditary neurocutaneous angioma, placental hemangioma): no antiangiogenic activity. Off-target PET binding is an imaging artifact, not a therapeutic effect.
- **Skin disease**: too broad to assess, with no documented dermatologic activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212123 (Cancelled) | TAUVID (Eli Lilly and Company) | Injection, solution | Not available in the compiled data |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support (Evidence Level L5, all top-10 predictions on hold). Flortaucipir is a diagnostic tracer given at microdose levels, and the high TxGNN score appears to be an artifact of sparse drug annotation. The only US license is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A credible mechanistic hypothesis connecting tau binding to the predicted disease, plus any preclinical evidence
- Confirmation of the regulatory status of the cancelled license and the original approved indication
- A review of whether a diagnostic microdose tracer can reasonably be repurposed as a therapeutic at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

