---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 837
evidence_level: L5
indication_count: 2
---

# Larotrectinib
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

# Larotrectinib: A Predicted New Indication — Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is not currently marketed in Taiwan, and no original-indication data is on file for this evidence pack. The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, but this direction is currently supported by only **1 clinical trial** (a broad genomic basket trial, not MEN-specific) and **2 review-type publications**, none of which directly test larotrectinib in MEN patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no original indication or Taiwan license data on file) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-indication and formal mechanism-of-action records are not available in this evidence pack (DrugBank MOA lookup flagged as a data gap, severity High). Based on the mechanistic notes attached to this prediction, larotrectinib is known to be a highly selective pan-TRK (NTRK1/2/3) kinase inhibitor.

The predicted new indication, Multiple Endocrine Neoplasia (MEN, including MEN2A/2B), is driven primarily by germline **RET** mutations — a different oncogenic driver than the NTRK fusions larotrectinib targets. The supporting literature actually discusses RET-directed kinase inhibitors (selpercatinib, pralsetinib) and general thyroid-cancer kinase-inhibitor therapy, not larotrectinib itself. The mechanistic overlap is therefore indirect: it would only be relevant in the rare subset of endocrine tumors that happen to carry an NTRK fusion rather than a RET alteration, which the current evidence does not confirm.

A second, lower-ranked candidate from the same model run — HER2-positive breast carcinoma (TxGNN score 99.14%) — shows a similarly indirect link: the supporting study used entrectinib (a different pan-TRK inhibitor) combined with a JAK2 inhibitor in preclinical models, not larotrectinib. Both predictions are best characterized as plausible drug-class hypotheses rather than drug-specific findings at this stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | MATCH is a genomic-marker-directed basket trial across refractory advanced solid tumors, lymphomas, and myelomas. It includes an NTRK-fusion-positive treatment arm, but is not designed for MEN or for a larotrectinib+MEN combination — relevance graded C (architectural co-occurrence only, not direct causal evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Reviews kinase-inhibitor therapy (vandetanib, cabozantinib, sorafenib, lenvatinib, and mutation-specific agents) for advanced thyroid cancer; general oncology-kinase-inhibitor context, not larotrectinib-specific. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Review | NPJ Precision Oncology | Discusses acquired resistance to RET-targeted TKIs (selpercatinib, pralsetinib) in RET-driven medullary thyroid carcinoma; does not address larotrectinib or MEN directly. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective pan-TRK/NTRK1-3 kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link between larotrectinib (pan-TRK inhibitor) and MEN (predominantly RET-driven) is indirect, and the sole clinical trial is a non-indication-specific basket trial with only C-grade relevance. Evidence level is L4 (mechanism/preclinical-level), and the model's own recommendation for this candidate is already "Hold."
- TFDA labeling data (Blocking gap) is missing, which prevents even an initial S1 safety screen from starting.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently blocking
- Confirmed DrugBank mechanism-of-action record
- MEN-subgroup or NTRK-fusion-stratified outcome data from the MATCH trial (or a dedicated larotrectinib+MEN study)
- Confirmation of larotrectinib's original approved indication(s) and Taiwan regulatory/market status, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

