---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
---

# Famotidine
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

# Famotidine: From [Regulatory Data Not Available] to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is a histamine H2-receptor antagonist (H2RA); no structured original-indication or license data is available for this drug in the current dataset, though the broader evidence base consistently documents its established use in acid-related upper GI disease (e.g., peptic ulcer, GERD).
The TxGNN model's top-ranked prediction for this candidate is **Duodenogastric Reflux**, with a **99.99% prediction score**, but currently only **0 clinical trials** and **2 publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Taiwan regulatory dataset shows 0 licenses on record for this product |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for famotidine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in the evidence pack's clinical rationale fields, famotidine is a histamine H2-receptor antagonist — it blocks parietal cell H2 receptors to suppress gastric acid secretion, a mechanism well documented across the drug's extensive peptic ulcer and GERD literature.

Duodenogastric reflux (DGR) involves acid-containing gastric contents refluxing alongside duodenal contents into the esophagus, so H2-mediated acid suppression could plausibly reduce the acid-related component of associated symptoms. However, per the evidence pack's own rationale: *"H2 blockade reduces gastric acid secretion, which may alleviate acid-related symptoms of reflux; however, duodenogastric reflux is primarily driven by bile/alkaline reflux rather than acid alone, so famotidine's mechanism only partially addresses the underlying pathophysiology."*

In short, the mechanistic link is real but **partial** — famotidine targets only the acid component of a condition whose primary driver (bile/alkaline reflux) lies outside its mechanism of action. This is consistent with the model's own moderate evidence level (L3) and early decision stage (S2, "Research Question") rather than a stronger "Go" signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Cohort | World Journal of Gastroenterology | Investigated famotidine's effect on gastroesophageal reflux (GER) and duodeno-gastro-esophageal reflux (DGER) in critically ill patients, exploring possible mechanisms and relevant contributing factors |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Review | Eksperimental'naia i Klinicheskaia Gastroenterologiia | Reviewed efficacy of famotidine 20 mg BID at early stages of gastroduodenal reflux disease, based on clinical and endoscopic findings (Savary-Miller grades 0–1) |

---

## US Market Information

No regulatory license records are available for this drug — `taiwan_regulatory.total_licenses = 0` and market status is "未上市" (Not Marketed). No product/dosage-form/indication table can be generated from current data.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap, DG001 — this must be resolved before any Stage 1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (duodenogastric reflux) has no registered clinical trials and only two non-RCT publications (a cohort study and a review), consistent with the model's own L3/S2 "Research Question" classification. The mechanistic rationale is only partial, since DGR is primarily bile-driven rather than acid-driven.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking gap (DG001)
- Famotidine mechanism of action documentation — currently a High-severity gap (DG002)
- Original indication / regulatory license data (none on record)
- Dedicated clinical trial evidence for famotidine in duodenogastric reflux specifically
- Consider evaluating **peptic ulcer disease** (rank 8, evidence level L1, 14+ trials) as a stronger-evidence alternative candidate from this same prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

