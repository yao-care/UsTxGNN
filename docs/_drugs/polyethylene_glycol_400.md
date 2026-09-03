---
layout: default
title: Polyethylene Glycol 400
parent: 僅模型預測 (L5)
nav_order: 1061
evidence_level: L5
indication_count: 2
---

# Polyethylene Glycol 400
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Polyethylene Glycol 400: From Pharmaceutical Excipient to Bronchitis

## One-Sentence Summary

> POLYETHYLENE GLYCOL 400 (PEG 400) is a pharmaceutical excipient with no established original therapeutic indication and is currently not marketed in Taiwan.
> The TxGNN model predicts it may be effective for **Bronchitis**,
> but this prediction is supported only by **5 clinical trials that are mismatched to an unrelated drug (MIRCERA)** and **no relevant literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved therapeutic indication (used as pharmaceutical excipient/solvent/vehicle) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`[Data Gap]`). Based on known information, PEG 400 is a pharmaceutical excipient commonly used as a solvent, lubricant, or osmotic/vehicle agent in drug formulations rather than as an active therapeutic ingredient. It has no registered original indication in the available regulatory data, and it is not currently marketed.

Because PEG 400 has no defined pharmacological indication to begin with, there is no established disease-mechanism relationship to compare against the predicted new indication of bronchitis. All five retrieved clinical trials actually studied **MIRCERA (methoxy polyethylene glycol-epoetin beta)** — a distinct, PEGylated erythropoiesis-stimulating agent for renal anemia — not PEG 400 itself. The evidence-pack review graded all five trials as relevance **"C" (string/entity mismatch)**, indicating this is very likely a knowledge-graph node collision (PEG-containing drug names) rather than a genuine biological signal linking PEG 400 to bronchitis.

Given the absence of a plausible mechanistic hypothesis and the mismatched evidence base, this prediction should be treated as a raw model output requiring independent verification before any further evaluation.

---

## Clinical Trial Evidence

⚠️ **Note:** The trials below were retrieved by the evidence pipeline under this candidate, but per internal relevance grading (all Grade C) they pertain to **MIRCERA (methoxy PEG-epoetin beta)** for renal anemia, not to PEG 400 or bronchitis. They are listed for transparency only and should not be interpreted as supporting evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01379963](https://clinicaltrials.gov/study/NCT01379963) | N/A | Completed | 780 | Retrospective observational study of hemoglobin levels in renal anemia patients treated with MIRCERA — unrelated to PEG 400/bronchitis |
| [NCT01422824](https://clinicaltrials.gov/study/NCT01422824) | N/A | Completed | 185 | Non-interventional safety/efficacy study of MIRCERA in chronic renal anemia on hemodialysis — unrelated to PEG 400/bronchitis |
| [NCT00559273](https://clinicaltrials.gov/study/NCT00559273) | Phase 3 | Completed | 307 | RCT comparing MIRCERA vs darbepoetin alfa for anemia correction in non-dialysis CKD — unrelated to PEG 400/bronchitis |
| [NCT01309295](https://clinicaltrials.gov/study/NCT01309295) | N/A | Completed | 250 | Prospective study of MIRCERA efficacy/safety in pre-dialysis and dialysis CKD patients — unrelated to PEG 400/bronchitis |
| [NCT01519947](https://clinicaltrials.gov/study/NCT01519947) | Phase 4 | Completed | 87 | Effect of altitude on MIRCERA dosage requirements in chronic renal anemia — unrelated to PEG 400/bronchitis |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

PEG 400 currently holds no marketing authorization records (0 NDAs); no license or product information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Detailed TFDA label warnings and contraindications for this substance are currently unavailable (Blocking data gap), which prevents a formal safety pre-assessment (S1 stage).

---

## Additional Predicted Indication (Lower Confidence)

The evidence pack also includes a second, weaker prediction: **Congenital Ichthyosiform Erythroderma** (TxGNN score 99.10%, rank 19,442). This candidate has **no supporting clinical trials or literature at all**, and the proposed rationale (PEG 400's use as a topical moisturizing/vehicle agent) is speculative with no direct mechanistic or clinical data. It is at an even earlier stage (L5/S0) than the bronchitis prediction and is not recommended for further evaluation at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is a pure model prediction (L5) with no genuine supporting clinical or literature evidence — the only retrieved trials are mismatched to an unrelated PEGylated drug. Combined with the missing mechanism-of-action data and a blocking gap in TFDA safety labeling, there is currently no basis to advance this indication beyond initial screening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications for PEG 400 (Blocking gap; required for S1 safety screening)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Verification that the TxGNN association is not an artifact of PEG-name entity collision (e.g., re-run evidence search using strict PEG 400 CAS/synonym filters, excluding PEGylated biologics such as MIRCERA)
- Any genuine preclinical or clinical evidence directly linking PEG 400 (not PEGylated conjugates) to respiratory/bronchial conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

