---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 1024
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: From Unspecified Indication to Fibromatosis, Gingival

## One-Sentence Summary

Pembrolizumab's original approved indication data is not available in this Evidence Pack, and the drug is currently marked as **not marketed** with zero registered NDAs.
The TxGNN model's top-ranked prediction is **Fibromatosis, Gingival**, with a raw similarity score of **99.40%** — but this candidate has **zero supporting clinical trials and zero literature**, and the model's own rationale flags it as lacking any biological basis.
Across all 10 predicted indications reviewed in this pack, none reach a credible evidence tier, and several are explicitly identified as disease-term mismatches rather than genuine drug-disease signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no approved indication text was returned |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.40% (rank #13,775 by raw score ordering — near the bottom of the candidate pool, not a top hit) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for pembrolizumab in this Evidence Pack (`original_moa` is unrecorded, flagged as a High-severity data gap, DG002).

Based on the evidence embedded elsewhere in this pack (literature attached to other candidate indications), pembrolizumab is a PD-1 immune checkpoint inhibitor that restores T-cell antitumor activity in malignancies with immune evasion phenotypes (e.g., NSCLC, melanoma, hepatocellular carcinoma, MSI-H/dMMR tumors). This mechanism is well-documented but was **not** the mechanism invoked for the top-ranked prediction.

For the actual top candidate — gingival fibromatosis — the model's own rationale states there is **no known mechanistic relationship**: gingival fibromatosis is a benign connective-tissue overgrowth condition (associated with SOS1 mutations/collagen metabolism), unrelated to PD-1/PD-L1 blockade. The high TxGNN score appears to reflect knowledge-graph embedding similarity rather than a real pharmacological or clinical signal. This is consistent with the pattern seen across all 10 candidates in this pack (see note below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No NDA or marketing authorization records are present in this Evidence Pack (`total_licenses = 0`, `market_status = 未上市/Not Marketed`). No product/dosage-form/indication table can be constructed from available data.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Pembrolizumab is an antineoplastic (immune checkpoint inhibitor), based on literature embedded in this pack describing its approved use in NSCLC, melanoma, hepatocellular carcinoma, head-and-neck squamous cell carcinoma, and MSI-H/dMMR solid tumors.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors are not primarily myelosuppressive; toxicity is immune-mediated rather than cytotoxic |
| Emetogenicity Classification | Low |
| Monitoring Items | Immune-related adverse event (irAE) monitoring: thyroid function, liver function tests, renal function, pituitary/adrenal axis (hypophysitis reported), pulmonary status (pneumonitis), skin, and baseline CBC |
| Handling Protection | Standard IV monoclonal antibody infusion precautions; no cytotoxic hazardous-drug handling protocol required (distinct from conventional chemotherapy) |

*Note: this summary is derived from literature attached to other candidate indications in this pack, not from a dedicated pembrolizumab toxicity dataset.*

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI data are all unavailable in this Evidence Pack; DG001 — TFDA label warnings/contraindications — is flagged as a Blocking data gap.)

---

## Additional Note: Pattern Across All 10 Candidates

This Evidence Pack evaluated 10 TxGNN-predicted indications for pembrolizumab (ranks #13,775–#16,101 by score, i.e., far outside the model's highest-confidence range). All 10 received an evidence level of **L4 or L5** and a **Hold** recommendation. Several are worth flagging explicitly:

- **Rank 4 (lung hilum carcinoma)** and **Rank 8 (pulmonary sulcus neoplasm)** are anatomic subtypes of NSCLC — mechanistically plausible given pembrolizumab's approved NSCLC indication — but supporting literature consists only of adverse-event case reports, not efficacy data.
- **Ranks 6, 9, and 10** returned literature/trials that, on manual review, are **disease-term mismatches**: retrieved records concern pembrolizumab's already-approved malignant indications (NSCLC, melanoma, colorectal, hepatocellular) rather than the benign or unrelated conditions actually predicted (e.g., "lung benign neoplasm," rare syndromes). These appear to be false positives from evidence-retrieval keyword overlap, not genuine support.
- **Ranks 1, 2, 3, 5, 7** have zero clinical trial or literature evidence and no mechanistic rationale.

No candidate in this batch meets the bar for progression beyond S0.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (gingival fibromatosis) has no supporting evidence and no plausible mechanism, and this pattern holds across all 10 reviewed candidates — most are either evidence-free or rely on mismatched/false-positive literature. There is currently no credible repurposing signal for pembrolizumab in this Evidence Pack.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/US label warnings, contraindications) — currently Blocking
- Resolve DG002 (mechanism of action) — currently High severity
- Re-run or audit the evidence-matching pipeline, given the high rate of disease-term mismatches identified in ranks 6, 9, and 10
- Re-examine TxGNN candidates at higher confidence ranks (closer to rank #1 by score) rather than this batch (#13,775–#16,101), which sits far outside the model's top predictions
- If gingival fibromatosis specifically is to be pursued, obtain preclinical/mechanistic data connecting PD-1 blockade to connective-tissue overgrowth pathways before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

