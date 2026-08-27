---
layout: default
title: Leuprolide
parent: 僅模型預測 (L5)
nav_order: 849
evidence_level: L5
indication_count: 2
---

# Leuprolide
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

Using this Evidence Pack directly (no additional skills apply — this is a self-contained report-writing task per the v5 template instructions already provided). Below is the report.

---

# Leuprolide: From GnRH-Agonist Hormone Suppression Therapy to Osteoarthritis

## One-Sentence Summary

> Leuprolide is a GnRH (LHRH) agonist historically used to suppress sex-hormone secretion in hormone-dependent conditions (e.g., androgen deprivation therapy in prostate cancer).
> The TxGNN model predicts it may be effective for **Osteoarthritis**, but this direction is supported by only **1 clinical trial** and **1 publication**, neither of which actually studies leuprolide in osteoarthritis — and the drug's known pharmacology points in the **opposite** direction (GnRH agonists are associated with *increased* bone loss and joint pain, not improvement).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from Taiwan regulatory data (drug is not marketed/licensed in this dataset); pharmacological context indicates hormone-dependent conditions treated via androgen/estrogen suppression (e.g., ADT for prostate cancer) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only — no genuine disease-relevant studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for leuprolide is flagged as a data gap in this evidence pack (DG002). Based on the pharmacological context available, leuprolide is a GnRH (LHRH) agonist that, with continuous administration, downregulates pituitary GnRH receptors and suppresses downstream sex-hormone (testosterone/estrogen) production — a mechanism used therapeutically in hormone-dependent conditions such as androgen deprivation therapy (ADT) for prostate cancer.

The TxGNN score of 0.9969 (rank 8002) reflects topological similarity within the knowledge graph rather than a validated pharmacological rationale for osteoarthritis. Critically, the mechanistic review embedded in this evidence pack notes that the *known clinical effect* of GnRH agonists on the musculoskeletal system runs opposite to what would be needed to treat osteoarthritis: long-term hormone suppression (as with ADT) is a well-documented cause of *accelerated* bone loss, osteoporosis, and arthralgia/myalgia — it does not alleviate joint disease. There is no known pathway by which leuprolide would reduce cartilage degeneration or joint inflammation.

For this reason, the mechanistic link should be read as a **contradictory signal rather than supporting evidence**. The single clinical trial and single publication retrieved for this pairing were both about metastatic prostate cancer and were captured only because they involve an LHRH analog — not because they studied osteoarthritis outcomes. This pattern is consistent with a false-positive prediction driven by graph co-occurrence rather than genuine therapeutic plausibility, and it should be treated with a high degree of skepticism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | N/A | Randomized trial of orchiectomy/LHRH analog + flutamide ± suramin/hydrocortisone in **metastatic prostate cancer**. No osteoarthritis endpoint; trial was matched only because it uses an LHRH analog. Relevance graded **C (low/mismatched)** — does not support the osteoarthritis prediction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case Report | Clinical Breast Cancer | Describes metastatic prostatic adenocarcinoma mimicking inflammatory breast carcinoma. Unrelated to osteoarthritis; not relevant supporting evidence. |

---

## US Market Information

Currently no marketing authorization records available — leuprolide is not marketed under this dataset (0 licenses on file), so no license/product table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently unavailable — a TFDA label/warnings lookup is flagged as a blocking data gap for safety pre-screening, see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — the only "supporting" trial and publication are both about unrelated metastatic prostate cancer and were captured due to LHRH-analog keyword overlap, not genuine osteoarthritis relevance. More importantly, the known pharmacology of GnRH agonists (worsening bone loss/arthralgia via hormone suppression) contradicts rather than supports a therapeutic role in osteoarthritis, making this look like a likely false-positive TxGNN signal.

**To proceed, the following is needed:**
- TFDA/FDA label data on warnings and contraindications (currently a **blocking** data gap — required before any safety pre-screening, DG001)
- Verified mechanism-of-action documentation via DrugBank API (currently missing, DG002)
- Disease-specific pharmacological or preclinical rationale explaining how GnRH suppression could plausibly benefit osteoarthritis, given the contradictory clinical signal noted above
- If this candidate is still pursued, independent expert review to rule out a knowledge-graph artifact before any further investment

**Note on secondary candidate:** A second, lower-ranked prediction (pseudoachondroplasia, TxGNN score 99.69%, rank 8263) was also flagged for leuprolide but has **zero** supporting clinical trials or literature and an even weaker mechanistic rationale (a genetic/structural cartilage disorder with no known GnRH-pathway involvement). This candidate should also be held pending stronger evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

