---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin eye drop originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **0 clinical trials** and **0 publications** are currently available to support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; includes 3 NDAs and 7 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, latanoprost is a prostaglandin F2-alpha analog that lowers intraocular pressure (IOP) by increasing uveoscleral outflow of aqueous humour.

Hereditary glaucoma is also characterised by elevated IOP, so an IOP-lowering mechanism is plausible. The very high TxGNN score is probably driven largely by the drug's proximity to the approved glaucoma indications in the knowledge graph, rather than by independent evidence.

Caution is needed. Primary congenital forms of glaucoma are typically managed surgically, and prostaglandin analogs are reported to have variable efficacy in paediatric patients. This is background knowledge, not part of the compiled evidence.

Other predictions for this drug (ranked by score) are weaker. Hair-growth conditions (hypotrichosis simplex of the scalp, congenital hypotrichosis milia) have a biologically plausible link, since prostaglandin F2-alpha analogs stimulate hair growth. Vascular, thoracic outlet, gastric and lymphatic conditions (visceral calciphylaxis, thoracic outlet syndromes, angiodysplasia of stomach, blue toe syndrome, lymphangiectasis) have no credible mechanistic link and are likely knowledge-graph artifacts. None has any supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 10 listed authorizations are cancelled. No approved-indication text was available for any of them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA091449 | Latanoprost (Sandoz Inc) | Solution | Cancelled |
| ANDA218257 | Latanoprost (Sagent Pharmaceuticals) | Solution/drops | Cancelled |
| ANDA202442 | Latanoprost (Rising Pharma Holdings) | Solution | Cancelled |
| ANDA201786 | Latanoprost (Somerset Therapeutics) | Solution/drops | Cancelled |
| NDA020597 | Latanoprost (Mylan Pharmaceuticals) | Solution | Cancelled |

Other cancelled authorizations include NDA216472 (IYUZEH, Thea Pharma) and NDA206185 (XELPROS, Sun Pharmaceutical), plus three further ANDAs.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, conjunctivitis, and acute contagious conjunctivitis. These should be treated as potential cautions or contraindications for use in patients with such conditions.
- **Drug Interactions:** The interaction screen returned 100 entries, but all reviewed entries have an unknown severity level. Examples include calcitriol, glimepiride, doxycycline, atropine, metformin, omeprazole, morphine, prednisone, triamcinolone, and simvastatin. Their clinical significance cannot be judged from the available data.

Please refer to the package insert for warnings and contraindications, as label-based safety text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no clinical trials or literature. The mechanism is plausible for hereditary glaucoma, but the score likely reflects proximity to the approved glaucoma indication. Label-based safety information is also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label, which is a blocking gap for safety screening
- Detailed mechanism of action data
- Literature and trial searches specific to hereditary and congenital glaucoma, including paediatric efficacy and safety
- Route compatibility and similarity-to-original assessments, which are still pending
- Clarification of current US market status, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

