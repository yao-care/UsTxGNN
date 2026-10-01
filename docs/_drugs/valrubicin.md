---
layout: default
title: Valrubicin
parent: Model Prediction Only (L5)
nav_order: 1281
evidence_level: L5
indication_count: 10
---

# Valrubicin
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

# Valrubicin: From BCG-Refractory Bladder Carcinoma In Situ to Colonic Neoplasm

## One-Sentence Summary

Valrubicin is an anthracycline (a doxorubicin derivative) given directly into the bladder (intravesical) for bladder cancer.
The TxGNN model predicts it may be effective for **colonic neoplasm**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BCG-refractory bladder carcinoma in situ (intravesical use). The license records contain no indication text, so this comes from the Evidence Pack's mechanistic rationale. |
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.96% (model rank 1498) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (1 NDA, 1 ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Valrubicin is an anthracycline that intercalates into DNA and inhibits topoisomerase II. This cytotoxic mechanism is plausible for malignant tumours in general. Detailed mechanism-of-action data is not yet available in the Evidence Pack.

The link between the original and new indication is weak. Valrubicin is approved only for intravesical use, with minimal systemic absorption. Reaching colonic tissue would need a different route or formulation, and the route compatibility assessment is still pending. The high score likely reflects proximity of colon-related nodes in the knowledge graph rather than direct biological evidence.

The nine other top predictions are all colon or cecum conditions, also with no trials or literature. Most are benign lesions (lymphangioma, lipoma, leiomyoma, hemangioma, benign cecal neoplasm) where a cytotoxic agent has no clear rationale. Rectosigmoid neoplasm is probably a near-duplicate of the colonic neoplasm signal. Cecum villous adenoma and neuroendocrine tumour G1 have only weak theoretical links.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206430 | Valrubicin Intravesical Solution (Hikma Pharmaceuticals USA Inc.) | Solution, concentrate | Not provided in the record |
| NDA020892 | Valstar (Endo USA, Inc.) | Solution, concentrate | Not provided in the record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Systemic exposure is minimal with intravesical use, but this has not been established for any other route. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials or literature (L5). The approved route is intravesical with minimal systemic exposure, and no route or formulation for colonic delivery has been established.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking data gap; safety screening cannot proceed without it)
- Detailed mechanism of action data from DrugBank
- A route compatibility assessment for colonic delivery
- Preclinical evidence of activity in colorectal models
- A review of related colorectal neoplasm indications to consolidate duplicate predictions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

