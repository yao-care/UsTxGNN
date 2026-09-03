---
layout: default
title: Tolmetin
parent: 僅模型預測 (L5)
nav_order: 1240
evidence_level: L5
indication_count: 10
---

# Tolmetin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tolmetin: From NSAID Anti-Inflammatory Use to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Tolmetin is a non-steroidal anti-inflammatory drug (NSAID) that inhibits COX-1/COX-2 to reduce prostaglandin-mediated inflammation and pain; detailed original-indication and MOA records are currently missing from this dataset.
> The TxGNN model's most credible prediction — after excluding several rare monogenic skeletal-dysplasia hits flagged internally as likely graph noise — points to **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)**.
> This is currently supported only by mechanistic rationale and historical labeling precedent; **no clinical trials or published literature** are present in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (`original_indications` is empty). Historical labeling notes cited in the evidence pack indicate Tolmetin (Tolectin) was used as an NSAID in rheumatoid-spectrum arthritis, including juvenile rheumatoid arthritis in some markets. |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 (mechanistic/historical rationale, no trials or literature on file) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's top 5 raw-ranked predictions (acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, pseudoachondroplasia) are rare monogenic skeletal/structural disorders. The evidence pack's own rationale annotates all of these as lacking any plausible mechanistic link to an NSAID and scores them "Hold" (L5, S0). The candidate selected above (rank 7 overall) is the only one that reached decision stage S1 with a "Proceed with Guardrails" recommendation, so it is used here as the primary evaluation subject.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tolmetin is not available from DrugBank (Data Gap). Based on the pharmacological class information present in the evidence pack, Tolmetin is an NSAID that inhibits COX-1/COX-2, thereby reducing prostaglandin synthesis and producing anti-inflammatory and analgesic effects.

Rheumatoid factor-positive polyarticular JIA is a pediatric disease within the rheumatoid arthritis spectrum, driven by prostaglandin-mediated synovial inflammation — the same pathway targeted by NSAIDs. The evidence pack notes that Tolmetin (brand name Tolectin) was historically approved in some markets specifically for juvenile rheumatoid arthritis (JRA), the older nomenclature for this disease group. This gives the prediction a real-world precedent beyond the model score alone.

The main limitation is that this dataset contains **no confirmatory clinical trials or literature** for this specific indication, and Tolmetin is currently **Not Marketed**, which limits near-term practical feasibility until sourcing/registration pathways are clarified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No license records are present in the dataset (`total_licenses = 0`). Market status is recorded as **Not Marketed**, meaning there is currently no active NDA/marketing authorization on file for Tolmetin in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all flagged as Data Gaps in this evidence pack, including a **Blocking**-severity gap for TFDA label warnings/contraindications — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The rheumatoid factor-positive polyarticular JIA hypothesis has a coherent mechanistic basis (COX inhibition → reduced synovial inflammation) and historical labeling precedent, reaching evidence level L4 — clearly stronger than the other candidates in this batch, most of which were internally flagged as graph noise. However, no clinical trials or literature currently substantiate this specific use, and a Blocking-severity safety data gap prevents a full S1 safety review.

**To proceed, the following is needed:**
- Retrieve TFDA label warnings and contraindications (DG001, Blocking — required before any S1 safety sign-off)
- Obtain formal DrugBank MOA documentation (DG002)
- Search for confirmatory trials/literature specifically on Tolmetin (or class-level NSAID evidence) in RF+ polyarticular JIA
- Clarify the regulatory/sourcing pathway given the drug's current "Not Marketed" status
- Lower-priority hypotheses worth monitoring only as research questions: rheumatoid nodulosis (rank 6) and spondyloarthropathy susceptibility locus (rank 8) — neither currently warrants active development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

