---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 1115
evidence_level: L5
indication_count: 8
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Regorafenib: From [Data Gap] to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multikinase inhibitor already approved in the US for colorectal cancer, GIST, and hepatocellular carcinoma, though its detailed original indication text is not available in this evidence pack. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **2 clinical trials** and **9 publications** currently identified — though notably the largest and most direct evidence (REGOSARC, SARC024) shows regorafenib does **not** work well in this specific histologic subtype. This is a case where mechanistic plausibility and prediction score are high, but the direct clinical evidence points toward a negative result, so this candidate requires careful reading rather than straightforward advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no original_indications on file) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not marketed in this jurisdiction) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (marked as a data gap). Based on known pharmacology, regorafenib is an oral diphenylurea multikinase inhibitor targeting angiogenic receptors (VEGFR1-3, TIE2), stromal receptors (PDGFR-β, FGFR1), and oncogenic kinases (KIT, RET, RAF1/BRAF). It is established in colorectal cancer and GIST on the strength of this anti-angiogenic and anti-stromal activity.

Soft tissue sarcomas, including liposarcoma, are highly vascular tumors, and anti-angiogenic TKIs are an established therapeutic class in this space — pazopanib, a mechanistically similar multikinase inhibitor, is already approved for non-adipocytic soft tissue sarcoma. This class effect is the rationale behind TxGNN's high prediction score for regorafenib in liposarcoma.

**However, the direct clinical evidence tells a more specific story than the mechanism alone suggests.** The REGOSARC trial (PMID 27751846) explicitly found regorafenib effective in leiomyosarcoma and synovial sarcoma but **not in liposarcoma** — the adipocytic subtype appears to behave differently, likely due to distinct underlying biology (e.g., MDM2/CDK4 amplification in well-differentiated/dedifferentiated liposarcoma) rather than pure vascular dependence. This was independently confirmed by the dedicated SARC024 liposarcoma cohort (PMID 32701199), which concluded results "do not support the routine use of regorafenib in this patient population." This is a good example of a mechanistically plausible, high-scoring TxGNN prediction that direct trial data has already largely refuted for this specific tumor subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) (SARC024) | Phase 2 | Completed | 131 | Basket protocol testing oral regorafenib across sarcoma subtypes including a dedicated liposarcoma cohort; per the linked publication (PMID 32701199), results did not support routine use of regorafenib in liposarcoma. |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) (REGOSARC) | Phase 2 | Completed | 219 | International randomized, double-blind, placebo-controlled trial with 5 cohorts including Cohort A (Liposarcoma); overall efficacy shown in leiomyosarcoma/synovial sarcoma but not confirmed for liposarcoma specifically. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: results confirm prior data and **do not support routine use** of regorafenib in treatment-refractory liposarcoma. |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC primary results: regorafenib improved PFS in advanced soft tissue sarcoma overall, driven by non-adipocytic subtypes. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (secondary analysis) | Eur J Cancer | Updated REGOSARC analysis including cross-over: confirms efficacy in leiomyosarcoma/synovial sarcoma "but not in liposarcoma." |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | Review of maintenance therapy strategies after first-line treatment in advanced soft tissue sarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial Protocol | BMC Cancer | REGOSARC study protocol describing rationale for testing regorafenib across sarcoma cohorts. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT (secondary analysis) | Cancer | Quality-adjusted time-without-symptoms analysis of REGOSARC, showing clinical benefit in doxorubicin-refractory non-adipocytic sarcoma. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's expanding role in sarcoma treatment across subtypes. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | RCT (different drug: anlotinib) | Anti-Cancer Drugs | Retrospective study of a different TKI (anlotinib) in liposarcoma; references regorafenib as an approved comparator in non-adipocytic STS. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Cohort (different drug: pazopanib) | Rare Tumors | Case report of pazopanib activity in Ewing sarcoma, cited as rationale for adding an Ewing arm to SARC024. |

---

## US Market Information

Not available — `taiwan_regulatory.market_status` indicates 未上市 (not marketed) with 0 licenses on file for this jurisdiction.

---

## Cytotoxicity

Regorafenib is a targeted small-molecule multikinase (tyrosine kinase) inhibitor, not a conventional cytotoxic chemotherapy agent, and the original indication/classification data needed to confirm antineoplastic categorization is incomplete in this evidence pack (data gap on original_moa and original_indications). Based on well-established external pharmacology for this molecule class:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase/anti-angiogenic TKI — VEGFR1-3, TIE2, PDGFR-β, FGFR1, KIT, RET, RAF1/BRAF) |
| Myelosuppression Risk | Low (class is not primarily myelosuppressive; toxicity is dominated by hand-foot skin reaction, hypertension, and hepatotoxicity per literature, e.g., PMID 23700287, 23981115) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests, blood pressure, skin/hand-foot reaction assessment, proteinuria (per class-wide TKI safety literature, e.g., PMID 32105149, 38761350) |
| Handling Protection | Standard oral oncolytic handling precautions; not classified with conventional cytotoxic handling requirements |

---

## Safety Considerations

Please refer to the package insert for safety information. (`safety.key_warnings`, `contraindications`, and `ddi` are all marked as data gaps or not found in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before proceeding to a full safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is very high (99.76%) and the mechanistic rationale (anti-angiogenic TKI class effect in vascular sarcomas) is sound, the two most directly relevant and highest-quality clinical trials specifically dedicated to liposarcoma (REGOSARC, SARC024) both concluded that regorafenib does **not** show meaningful efficacy in this histologic subtype — this is negative, not merely absent, evidence. Combined with a Blocking data gap on safety labeling (warnings/contraindications/DDI) and no original indication or MOA data on file, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/US label warnings and contraindications) before any S1 safety screening
- Resolve DG002 (confirmed original MOA/indications from DrugBank) to properly benchmark similarity to the original indication
- If pursuing further, a re-analysis focused on liposarcoma molecular subtypes (e.g., well-differentiated/dedifferentiated with MDM2/CDK4 amplification vs. myxoid/round cell) may be warranted, since the negative trial results may not generalize to all liposarcoma biology — but absent new data, this indication should not advance
- Note: the same drug shows a more promising signal for non-adipocytic soft tissue sarcoma and for clear cell renal cell carcinoma (rank 3, L2/S2, "Research Question") — consider evaluating those candidates separately rather than liposarcoma specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

