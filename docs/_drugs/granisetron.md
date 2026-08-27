---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Antiemetic Therapy (CINV/PONV) to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist generally used to prevent chemotherapy/radiotherapy-induced and postoperative nausea and vomiting. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy/radiotherapy-induced and postoperative nausea and vomiting (general pharmacological knowledge — not confirmed by Taiwan license data, as this drug is not marketed in Taiwan) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (TFDA label and DrugBank MOA fields are both data gaps). Based on the evidence pack's own repurposing rationale, granisetron is a selective 5-HT3 receptor antagonist acting primarily on peripheral and central chemoreceptor trigger zones — the pathway responsible for its established antiemetic effect.

The proposed link to manic bipolar affective disorder is indirect: 5-HT3 receptors are also present in limbic structures, so serotonergic modulation is theorized to influence mood regulation, and small studies of the related agent ondansetron have explored adjunctive use in psychiatric symptoms. However, this is a mechanistic hypothesis only — there is no direct clinical or preclinical evidence connecting granisetron to bipolar mania, and the evidence pack explicitly flags this as an indirect inference rather than a supported indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA label warnings/contraindications for granisetron could not be retrieved (blocking data gap), so a formal safety screening (S1) cannot yet be performed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 — no clinical trials, ICTRP records, or literature support the granisetron–bipolar mania link, and the mechanistic rationale is theoretical (5-HT3/limbic system association) rather than demonstrated. Combined with a blocking gap in TFDA safety data, this candidate is not ready to advance past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank/primary literature
- Preclinical or case-level evidence specifically linking 5-HT3 antagonism to mood stabilization in bipolar disorder
- Ongoing monitoring for any new clinical trial or publication activity on this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

