---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 521
evidence_level: L5
indication_count: 4
---

# Chloroquine
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

# Chloroquine: From Antimalarial Use to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is a long-established antimalarial drug (general pharmacological knowledge; the Evidence Pack contains no label indication text).
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)**,
but this specific prediction has **0 clinical trials** and only **2 publications**, and neither publication tests chloroquine directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antimalarial (label indication text not provided in the Evidence Pack) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chloroquine is an antimalarial (4-aminoquinoline) drug. Antimalarials are used more broadly as immunomodulatory agents in rheumatic disease, so it may be mechanistically applicable to juvenile arthritis. The Evidence Pack does not document this link, so it remains a hypothesis.

The TxGNN score (0.994) is a knowledge-graph prediction only. No chloroquine-specific mechanism, similarity analysis, or route-compatibility assessment is available.

Two related predicted indications have more direct drug-specific history. **Juvenile chronic polyarthritis** includes a small randomized comparison of chloroquine (Delagil) versus sulphasalazine (PMID 1688268). **Juvenile idiopathic arthritis** includes a 1974 chloroquine/hydroxychloroquine dosing study (PMID 4848261). Both are old, small, and low-tier evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort | J Rheumatol | Long-term real-life experience with leflunomide in JIA. This is not a chloroquine study, so it is background only. |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case series | J Pediatr | Two RF-positive polyarticular JRA patients developed accelerated nodulosis on methotrexate. In one, nodules were arrested after adding hydroxychloroquine (a related drug, not chloroquine). |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040516 | Chloroquine Phosphate (Amneal Pharmaceuticals of New York LLC) | Tablet | Not listed in the Evidence Pack |
| ANDA040516 | Chloroquine Phosphate (AvKARE) | Tablet | Not listed in the Evidence Pack |
| ANDA214756 | Chloroquine Phosphate (Suven Pharmaceuticals Limited) | Tablet, coated | Not listed in the Evidence Pack |
| No number assigned | Chloroquinum Phos. (Hahnemann Laboratories, INC.) | Pellet | Not listed in the Evidence Pack |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no registered clinical trials, and its two publications do not test chloroquine directly. Evidence is at the model-prediction level (L5), and the package insert and mechanism data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Chloroquine mechanism of action data, for example via the DrugBank API
- Chloroquine-specific clinical evidence in JIA. Start with the related indications above (PMIDs 1688268 and 4848261) and separate chloroquine data from hydroxychloroquine data.
- A decision on which JIA subtype to prioritize, since the related, better-documented predictions may be a stronger starting point than this RF-positive polyarticular subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

