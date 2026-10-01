---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 1251
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From HER2-Directed Cancer Therapy to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan (Enhertu) is a HER2-directed antibody-drug conjugate (ADC) used in oncology.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761139) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trastuzumab deruxtecan is an antibody-drug conjugate that targets HER2 and carries a topoisomerase I inhibitor payload (deruxtecan). It is a cytotoxic oncology agent with no known anti-resorptive or bone-anabolic activity. Detailed mechanism-of-action data are not available in the source record.

**No credible direct mechanistic link to osteoporosis was identified.** The high score most likely reflects proximity in the knowledge graph. Patients with HER2-positive breast cancer often receive aromatase inhibitors, which cause drug-induced bone loss. The model has probably linked the drug to osteoporosis through this shared patient population, not through any therapeutic effect on bone.

The drug's own risks, including interstitial lung disease and myelosuppression, make benefit in a non-oncologic bone indication implausible. Treat this as an association artifact, not a repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761139 | Enhertu | Lyophilized powder for injection solution | Daiichi Sankyo Inc. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (targeted therapy) |
| Myelosuppression Risk | Present (myelosuppression is a recognized risk); please refer to the package insert warnings and precautions for severity details |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential); respiratory symptoms and imaging for interstitial lung disease; refer to the package insert for full monitoring requirements |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Key Risks Noted in the Assessment**: Interstitial lung disease and myelosuppression.
- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (Evidence Level L5), and no plausible mechanistic link to bone loss was identified. The cytotoxic payload and its known toxicities make benefit in a non-oncologic bone indication unlikely.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for safety screening
- Detailed mechanism-of-action data
- Any preclinical or clinical evidence showing a direct effect on bone metabolism, which would be needed to move beyond the knowledge-graph association

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

