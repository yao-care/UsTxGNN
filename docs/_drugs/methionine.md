---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 908
evidence_level: L5
indication_count: 10
---

# Methionine
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

# Methionine: From No Established Indication to Acne (disease)

## One-Sentence Summary

Methionine (DrugBank DB00134) has no recorded original indication or marketing authorization in this dataset — it is currently **not marketed** and no license records exist. TxGNN predicts potential efficacy for **Acne (disease)**, but this prediction is currently backed only by the model score, with **0 clinical trials** and **4 loosely related publications**, none of which establish a mechanistic or clinical link to acne.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available — drug not marketed, no license records on file |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methionine is not available in this evidence pack, and no original approved indication is on record to anchor a mechanistic comparison against acne.

Reviewing the supporting literature, none of the four retrieved papers actually connect methionine to acne treatment. One paper reports elevated plasma homocysteine (a downstream metabolite of methionine metabolism) in patients undergoing **isotretinoin** therapy for cystic acne — this is an adverse-effect biomarker of a different drug's toxicity profile, not evidence that methionine treats acne. A second paper concerns an MTHFR mutation causing neonatal encephalopathy (with "neonatal acne" as an incidental clinical feature, unrelated to methionine therapy). The remaining two papers discuss neutrophil chemotactic function and Sweet's syndrome chemoattractants in inflammatory skin disease generally, sharing no direct link to methionine or acne pathophysiology.

In short, this prediction is currently supported only by the TxGNN model's ranking score. No mechanistic rationale or clinical signal in the retrieved evidence corroborates a therapeutic role for methionine in acne.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | International Journal of Dermatology | Elevated plasma homocysteine (a methionine metabolite) observed in cystic acne patients on isotretinoin — reflects a drug side-effect biomarker, not a methionine treatment effect |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case Report | BMJ Case Reports | Neonate with MTHFR mutation presenting with encephalopathy; neonatal acne noted as an incidental dysmorphic feature, unrelated to methionine therapy |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Basic Research | Journal of Investigative Dermatology | Neutrophil C5a chemotactic function studied across several inflammatory skin diseases including acne conglobata; no methionine involvement |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Basic Research | Journal of the American Academy of Dermatology | Plasma chemoattractant activity in a Sweet's syndrome patient with cystonodular acne; no methionine involvement |

---

## US Market Information

Methionine holds no marketing authorization on record in this dataset (market status: Not Marketed; 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Acne (disease) prediction is supported only by the TxGNN score — there are no clinical trials, and none of the four available publications provide a mechanistic or clinical basis linking methionine to acne. Combined with the absence of MOA and safety data, there is insufficient evidence to advance this indication.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently blocking — required before any S1 safety review)
- Methionine's mechanism of action (currently a data gap; needed to assess biological plausibility)
- Original, real-world dosing/indication context, since no license or original-indication data exists in this dataset
- Dedicated preclinical or clinical studies directly testing methionine in acne, rather than incidental literature mentions
- *Separately worth noting*: among this drug's 10 predicted indications, **diabetic cataract** (rank 10) shows materially stronger, methionine-specific mechanistic evidence (MsrB1/S-adenosylmethionine pathway in lens oxidative defense) and was flagged at decision stage S1 ("Research Question") — it may merit independent follow-up ahead of the acne candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

