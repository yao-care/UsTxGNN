---
layout: default
title: Dexrazoxane
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Dexrazoxane
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

# Dexrazoxane: From Chemotherapy Cardioprotection to Sclerosing Cholangitis

## One-Sentence Summary

Dexrazoxane is a marketed injectable, generally known as a chemoprotectant used alongside anthracycline chemotherapy. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **no clinical trials and no publications** currently support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (approved indication text is empty in all listed licenses). The title uses the drug's general known role as a chemoprotectant. |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.99% (model rank 482) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 licenses (the five listed are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in the Evidence Pack. The analysis notes describe dexrazoxane as an iron chelator (through its metabolite ADR-925) and a topoisomerase II catalytic inhibitor.

A link to sclerosing cholangitis is conceivable but speculative. Iron-related and oxidative injury could play a role in cholestatic liver disease, and dexrazoxane's iron chelation might counter that. The Evidence Pack contains no data supporting this idea, and no similarity assessment between the original and predicted indications has been done.

The score of 0.9999 comes from the knowledge graph alone. Many other predictions for this drug have similarly high scores but no plausible rationale (for example bronchitis, conjunctivitis and urinary tract infection). The score should therefore not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA207321 | Dexrazoxane (Fosun Pharma USA Inc.) | Lyophilized powder for injection |
| ANDA076068 | Dexrazoxane (Hikma Pharmaceuticals USA Inc.) | Lyophilized powder for injection |
| ANDA207321 | Dexrazoxane (Almaject, Inc.) | Lyophilized powder for injection |
| ANDA207321 | Dexrazoxane (Gland Pharma Limited) | Lyophilized powder for injection |

Only the injectable route is listed, and approved indication text is not provided for any license. Some authorization numbers appear more than once because different manufacturers share them.

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack's rationale notes also flag the drug's myelosuppressive profile as a concern. FDA package insert warnings and contraindications have not been retrieved, and this is a blocking gap for safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score, with no trials or literature. Original MOA and package insert safety data are also missing, so the candidate cannot advance past the initial stage.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking)
- Mechanism of action data from DrugBank
- A targeted literature search on dexrazoxane, iron chelation and cholestatic or sclerosing cholangitis disease
- Approved indication text for the US licenses, to confirm the original indication
- Evidence on route compatibility with the target indication (currently pending)

Among the other predicted indications, only **cystitis** has indirect supporting material (preclinical ferroptosis studies and chemoprotectant reviews, evidence level L4). It is worth a separate hypothesis-level look, such as a chemotherapy-induced hemorrhagic cystitis model. It is not evidence for sclerosing cholangitis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

