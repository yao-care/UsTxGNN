---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 1188
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: From NSAID Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Sulindac is an oral non-steroidal anti-inflammatory drug (NSAID) that is marketed in the United States as generic tablets.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal dysplasia.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (approved indication text is empty for all licenses) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 (all listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sulindac is an NSAID that inhibits cyclooxygenase (COX). Its active sulfide metabolite may also have COX-independent effects. The original indication text was not provided, so the link between the original and new indication cannot be assessed from the source data.

The predicted disease is caused by loss of CDMP1/GDF5 signaling, which is part of the BMP pathway. COX inhibition is not known to act on this pathway, so **no clear mechanistic link** was identified. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than biology.

The other nine TxGNN predictions (ranks 2–10, all scoring 99.56–99.90%) show the same pattern:

- **Skeletal and developmental disorders** (brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome and others): the underlying defects are genetic or developmental, and an NSAID would at most give symptomatic pain relief.
- **Rheumatoid vasculitis:** this is biologically understandable, since sulindac is an NSAID used for rheumatoid arthritis symptoms. However, this severe complication is treated with corticosteroids and immunosuppressants, and NSAIDs are not expected to control it.
- **Hypermobility of coccyx:** NSAIDs are commonly used for coccydynia, but this is general class use rather than a sulindac-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA072711 | SULINDAC | Tablet | PuraCap Laboratories LLC dba Blu Pharmaceuticals |
| ANDA072710 | SULINDAC | Tablet | PuraCap Laboratories LLC dba Blu Pharmaceuticals |
| ANDA072051 | SULINDAC | Tablet | Sun Pharmaceutical Industries, Inc. |
| ANDA072051 | SULINDAC | Tablet | PD-Rx Pharmaceuticals, Inc. |
| ANDA072050 | SULINDAC | Tablet | PD-Rx Pharmaceuticals, Inc. |

Approved indication text is not available for these licenses. Only the oral tablet route is recorded.

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found for sulindac in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (evidence level L5). No mechanistic link was identified between COX inhibition and the disease's underlying BMP/GDF5 signaling defect. The high score likely reflects a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap that prevents safety screening)
- Mechanism of action data for sulindac from DrugBank
- The original approved indications, to assess similarity to the predicted indication
- Preclinical or mechanistic evidence linking sulindac to the GDF5/BMP pathway
- Route compatibility assessment (currently pending)
- If a repurposing direction is still wanted, a review of the more biologically plausible symptomatic candidates (rheumatoid vasculitis, hypermobility of coccyx) as adjuncts

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

