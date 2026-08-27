---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity to Diabetic Cataract

## One-Sentence Summary

Glucarpidase is a recombinant bacterial enzyme (carboxypeptidase G2) used as emergency rescue therapy to hydrolyze toxic plasma concentrations of methotrexate; it is not currently marketed in the US/Taiwan reference dataset. The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own known mechanism shows no biological link to cataract pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Toxic methotrexate plasma concentrations (rescue therapy) — per DrugBank classification; no formal TFDA/US license text available |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not available in the regulatory record, but the evidence pack itself documents glucarpidase's known pharmacology: it is a recombinant bacterial carboxypeptidase (carboxypeptidase G2) whose only established function is hydrolyzing methotrexate into inactive metabolites, used to accelerate clearance of toxic methotrexate concentrations in overdose settings.

There is no identified relationship between this original use and diabetic cataract. Diabetic cataract pathology involves hyperglycemia-driven lens protein glycation and osmotic changes in the crystalline lens — a pathway with no known biochemical overlap with folate-analog metabolism or methotrexate clearance.

Given the drug has no recorded original indications, no DDI data, and a narrow, single-purpose enzymatic function, the high TxGNN score across this drug's entire top-10 list (all cataract/retinopathy nodes clustered within a 0.15% score range) is more consistent with sparse knowledge-graph connectivity producing noisy embedding similarity than with a genuine biological signal. The rationale text accompanying multiple ranked predictions in this evidence pack independently reaches the same conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No license records are available — glucarpidase has no marketed NDA/license entries in this dataset (market status: Not Marketed, total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence-level L5 (model output only, zero clinical trials, zero literature), and the drug's own documented mechanism (methotrexate-specific hydrolysis) has no plausible biological connection to diabetic cataract. The uniformly clustered high scores across all ten predicted cataract/retinopathy indications for this drug further suggest a knowledge-graph sparsity artifact rather than a genuine signal.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to close the current Blocking data gap before any safety pre-screening
- Confirmed detailed mechanism-of-action data from DrugBank/primary literature
- Preclinical or mechanistic evidence establishing any plausible ophthalmologic pathway before allocating further evaluation resources
- Re-screening once additional KG edges (indications, DDI) are populated for this drug, since current predictions likely reflect data sparsity rather than efficacy signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

