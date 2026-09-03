---
layout: default
title: Sulindac
parent: 僅模型預測 (L5)
nav_order: 1188
evidence_level: L5
indication_count: 10
---

# Sulindac
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

Using no additional skill — this is a direct content-generation task with an explicit, fully-specified template, not a coding or debugging task requiring a process skill.

# Sulindac: From NSAID Anti-Inflammatory Use to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

> Sulindac is an NSAID (indole acetic acid class); this evidence pack does not confirm a specific approved indication in Taiwan, as the drug currently holds no Taiwan marketing license.
> The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, but the evidence pack's own analysis flags this as likely a knowledge-graph artifact rather than a genuine signal —
> **0 clinical trials** and **0 publications** support it, and no other candidate among the 10 predicted indications has any direct trial or literature evidence either.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license on file; drug is a known NSAID (indole acetic acid class) per class references in this evidence pack, but no specific original indication text is provided |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type (top TxGNN score; see caveat below) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Market Status (Taiwan) | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Sulindac in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological class knowledge referenced within this evidence pack's own candidate rationales, Sulindac is an NSAID that works primarily through COX-1/COX-2 inhibition, with some COX-independent, pro-apoptotic effects noted in the literature for other tissues.

For the top-ranked candidate, **acromesomelic dysplasia (Hunter-Thompson type)**, the evidence pack's own mechanistic assessment is explicit: this is a skeletal developmental disorder caused by *GDF5/CDMP1* mutations, not an inflammatory condition, and there is **no plausible pathophysiological link** to Sulindac's COX-inhibition/pro-apoptotic mechanism. The evidence pack states this high score is likely graph-embedding noise rather than a real pharmacological signal. The same pattern — high TxGNN score, but no mechanistic plausibility — applies to most of the top-ranked candidates (rank 1–8: acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, brachyolmia, myosclerosis, pseudoachondroplasia, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, WHIM syndrome), all of which are rare structural/genetic disorders with no inflammatory component and are scored "Hold."

By contrast, two lower-scoring but mechanistically more coherent candidates were staged further along in the internal review process (S1, "Research Question" rather than "Hold"):

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.92% | L5 | S0 | Hold |
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.90% | L5 | S0 | Hold |
| 3 | Brachyolmia | 99.90% | L5 | S0 | Hold |
| 4 | Myosclerosis | 99.89% | L5 | S0 | Hold |
| 5 | Pseudoachondroplasia | 99.85% | L5 | S0 | Hold |
| 6 | Brachydactyly-syndactyly syndrome | 99.82% | L5 | S0 | Hold |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.81% | L5 | S0 | Hold |
| 8 | WHIM syndrome | 99.74% | L5 | S0 | Hold |
| 9 | Rheumatoid vasculitis | 99.63% | L5 | S1 | Research Question |
| 10 | Hypermobility of coccyx | 99.56% | L5 | S1 | Research Question |

**Rheumatoid vasculitis** (rank 9) is a severe inflammatory vascular complication of rheumatoid arthritis; NSAIDs including sulindac have long-standing clinical use for RA symptom control, giving a theoretical (though unproven for this specific indication) mechanistic basis via COX-mediated anti-inflammatory activity — though standard treatment for vasculitis itself is steroids/immunosuppressants, with NSAIDs typically an adjunct at most. **Hypermobility of coccyx** (rank 10) commonly presents with sacrococcygeal joint inflammation and mechanical pain; NSAIDs are empirically used for coccydynia-type pain in clinical practice, giving this candidate a defensible pharmacological rationale despite the absence of direct supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorization is currently registered for Sulindac in Taiwan (market status: 未上市 / Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for sulindac are supported only by model score, with zero clinical trials or literature (Evidence Level L5) across the board. The drug has no Taiwan marketing license, and both mechanism-of-action data and TFDA label warnings/contraindications are missing — the latter being a Blocking-severity gap (DG001) that prevents any safety pre-screening (S1). The single highest-scoring candidate is explicitly identified within the evidence pack itself as a likely knowledge-graph artifact rather than a genuine signal, so it should not be treated as the strongest lead by default.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — Blocking gap, required before any S1 safety review (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Direct clinical trial or literature evidence, prioritizing the two mechanistically plausible candidates already advanced to "Research Question" stage: rheumatoid vasculitis and hypermobility of coccyx
- Independent review of the top-ranked "acromesomelic dysplasia" prediction to confirm/rule out embedding artifact before allocating further review resources to it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

