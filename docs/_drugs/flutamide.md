---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer (Androgen Deprivation Therapy) to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide's formal original-indication record is a data gap in this pack, but the clinical trial and literature evidence collected under other predicted indications consistently describe it as a nonsteroidal antiandrogen used in androgen deprivation therapy (ADT) for prostate cancer. The TxGNN model's top-ranked prediction is **Prostate Cancer/Brain Cancer Susceptibility** (score 99.98%), but this specific prediction is supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no corroborating evidence in the current data pull.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as structured data (DrugBank `original_indications` and TFDA `licenses` are both empty). Contextually, trial/literature evidence elsewhere in this pack repeatedly identifies flutamide as an antiandrogen component of prostate cancer hormone therapy. |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on the surrounding evidence in this pack — dozens of clinical trials and papers on other predicted indications — flutamide is a nonsteroidal antiandrogen that blocks androgen receptor signaling, and is used clinically as part of combined androgen blockade (with LHRH agonists) in prostate cancer.

The rank-1 predicted indication, "prostate cancer/brain cancer susceptibility," appears to be a composite ontology label (a susceptibility-gene co-morbidity tag) rather than a distinct, well-defined disease entity, and it carries no supporting clinical trial or literature evidence in this data pull. Given that flutamide's own established use already centers on prostate cancer, this top prediction reads less like a genuinely *new* repurposing opportunity and more like the model re-identifying a known association — it should not be treated as a novel signal without further investigation.

It is worth noting that other, lower-ranked predictions in this same evidence pack carry substantially stronger evidence: rank 4 ("benign reproductive system neoplasm," L4/S1, 19 literature hits) and rank 6 ("male reproductive organ cancer," 50 clinical trials incl. multiple completed Phase 3 RCTs, 20 publications) are far better candidates for further evaluation than the nominal rank-1 entry, and reviewers may want to prioritize those instead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Flutamide is currently not marketed under this pack's regulatory source (`market_status`: 未上市), with 0 licenses/NDAs on record. No authorization table is available.

---

## Cytotoxicity

Flutamide is an antineoplastic agent by clinical use (established antiandrogen component of prostate cancer treatment per the surrounding trial evidence), though it acts via hormonal/receptor blockade rather than direct cytotoxicity.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/endocrine therapy (nonsteroidal antiandrogen) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (antiandrogens are associated with hepatotoxicity in class); please refer to the package insert for full monitoring requirements |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this evidence pack — TFDA label data is flagged as a **Blocking** data gap, DG001, preventing S1 safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 predicted indication has evidence level L5 (model prediction only, no clinical trials or literature), and the TFDA label/warning data needed for even a preliminary safety screen is a Blocking gap (DG001). There is no basis to advance this specific candidate past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Drug mechanism of action confirmation via DrugBank API (DG002, High)
- Confirmed original-indication record (regulatory or DrugBank source), since none is currently populated
- Consider re-scoping the evaluation toward rank 4 ("benign reproductive system neoplasm") or rank 6 ("male reproductive organ cancer"), which carry materially stronger clinical trial and literature support than the current rank-1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

