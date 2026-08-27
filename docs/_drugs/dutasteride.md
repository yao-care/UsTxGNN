---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Androgen-Dependent Conditions to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5α-reductase inhibitor best known for use in androgen-dependent conditions (e.g., benign prostatic hyperplasia, androgenetic alopecia); its formal original-indication and MOA records are flagged as a data gap in this evidence pack (DG001, DG002). The TxGNN model's top prediction is **Ambras Type Hypertrichosis Universalis Congenita**, but this is supported by **0 clinical trials** and **0 publications**, and the mechanism runs in the opposite pharmacological direction from what the disease would require.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no TFDA license records; `original_indications` is empty). Rationale text references androgen-dependent conditions (e.g., BPH/AGA) as the drug's known use area — see DG002. |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data is not available for this drug (DG002, High severity — remediation: query DrugBank API). Based on information embedded in the model's own repurposing rationale, dutasteride is a 5α-reductase inhibitor that lowers dihydrotestosterone (DHT); pharmacologically this direction is "reduce androgen-driven hair growth," which is why it is used for conditions like benign prostatic hyperplasia and androgenetic alopecia.

Ambras type hypertrichosis universalis congenita is a congenital, autosomal-dominant disorder (linked to 8q chromosomal rearrangement) driven by structural follicular activation that is **not** androgen-dependent. The evidence pack's own rationale explicitly flags this mismatch: dutasteride's DHT-lowering mechanism points toward *reducing* hair growth, while this condition would require the opposite. The rationale attributes the model's high score to graph-embedding proximity (hair-related node clustering in the knowledge graph) rather than a genuine mechanistic relationship.

Given this, the prediction should be treated as a signal for further investigation of the TxGNN graph topology rather than a clinically plausible repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Dutasteride is not marketed in this jurisdiction (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — DG001, Blocking severity, blocks the S1 safety pre-screen; remediation requires downloading and parsing the TFDA package insert.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trial or literature support (L5, decision stage S0), and the drug's own known mechanism (DHT reduction) runs counter to what Ambras type hypertrichosis would require — the rationale itself attributes the score to likely graph-embedding noise rather than a real signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Verified mechanism of action and original indication data via DrugBank API (DG002)
- Investigation of why the TxGNN graph clusters dutasteride with structural/congenital hair disorders, to rule out embedding artifacts
- Note: rank 8, **diffuse alopecia areata**, was separately scored L4/S1 ("Research Question") based on one retrieved review — but that review discusses androgenetic alopecia, not alopecia areata, so the disease-node mapping should be manually verified before treating it as a stronger candidate than rank 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

