---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
monitor_inn: "IOPROMIDE"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-14
description: "Iopromide: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the data compiled for this report (diagnostic contrast…"
---

# Iopromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Iopromide: From Contrast Imaging to Osteoarthritis Susceptibility
{: .text-alpha }

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent (US brand Ultravist), used for diagnostic imaging rather than treatment.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (diagnostic contrast imaging agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is an iodinated, non-ionic contrast agent. It is used to visualize structures during imaging and has no known disease-modifying pharmacology.

On review, the prediction is hard to justify biologically. "Osteoarthritis susceptibility" is a genetic risk concept, not a treatable clinical condition. The high score (0.996) most likely reflects proximity to arthritis-related nodes in the knowledge graph rather than any real therapeutic link. Iopromide can be used in joint imaging (arthrography), but that is a diagnostic use and does not act on cartilage or joint inflammation.

The other top predictions show the same pattern: osteoarthritis, rheumatoid arthritis, rare skeletal dysplasias (brachyolmia, Hunter-Thompson acromesomelic dysplasia, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy. None has a documented mechanistic link, and all have 0 trials and 0 publications. For hemoglobinopathy, the prediction runs against clinical practice, because iodinated contrast media are used with caution in conditions such as sickle cell disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020220 | Ultravist (Bayer HealthCare Pharmaceuticals Inc.) | Injection | Not listed; status: cancelled |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. Most of those listed are rated Major, including:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Vancomycin
  - Polymyxin B
  - Aminosalicylates and related agents: mesalazine, balsalazide, olsalazine, sulfasalazine
- Mannitol is rated Moderate.
- Clotrimazole, acetylsalicylic acid, bupropion, dexamethasone and pantoprazole have an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (L5), no plausible mechanism, and no active US market authorization. A diagnostic contrast agent is not expected to treat osteoarthritis or any of the other predicted conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data
- Any preclinical or clinical signal for the predicted indication
- A clearer, treatable disease definition in place of "osteoarthritis susceptibility"; if the osteoarthritis direction is revisited, the broader "osteoarthritis" prediction is the more clinically meaningful one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

