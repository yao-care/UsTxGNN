---
layout: default
title: Guselkumab
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Plaque Psoriasis to Drug-Induced Osteoporosis

## One-Sentence Summary

Guselkumab (brand name TREMFYA) is an anti-IL-23 antibody. The Evidence Pack treats plaque psoriasis as its established use, though the license records list no indication text.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records; the Evidence Pack rationale identifies plaque psoriasis as an established marketed use |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (all under BLA761061) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank field. The Evidence Pack's rationale identifies guselkumab as a monoclonal antibody against the p19 subunit of IL-23. IL-23 drives Th17 differentiation and IL-17/IL-22 signaling, which underlie psoriatic skin inflammation.

The link to osteoporosis is speculative. The IL-23/IL-17 axis can influence osteoclast formation and bone remodeling, so blocking it could in theory affect bone loss. However, no trial or publication tests this in drug-induced osteoporosis, and the very high TxGNN score is a model output, not a clinical signal. Osteoporosis caused by drugs such as glucocorticoids has different drivers from psoriatic inflammation, so the similarity to the original indication is unestablished.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761061 | TREMFYA (Janssen Biotech, Inc.) | Injection | Not listed in the record |

The three license records are duplicates of the same BLA and product.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the mechanistic link is only speculative. The TxGNN score alone is not enough to justify moving forward.

**Other predictions in the pack (not the focus of this report):**
- **Psoriasis (rank 3):** L1 evidence with completed Phase 3 RCTs (e.g., VOYAGE 1 and 2). The pack flags this as confirmation of a known use, not a novel repurposing finding.
- **Ulcerative colitis (rank 6):** L1 evidence from the QUASAR Phase 3 program. The pack suggests this may already be a labeled use.
- **Other Hold predictions (ranks 2, 4, 5, 7-10):** All L5 with no supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the pack marks this as a blocking gap)
- Verification of the current label and indication registry to confirm which indications are already approved
- Preclinical or mechanistic evidence for IL-23 blockade in bone loss
- Observational data on bone density or fracture outcomes in patients treated with IL-23 inhibitors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

