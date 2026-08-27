---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 858
evidence_level: L5
indication_count: 10
---

# Levothyroxine
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

# Levothyroxine: From Hypothyroidism to Endemic Goiter

## One-Sentence Summary

Levothyroxine (LT4) is the synthetic thyroid hormone used as lifelong replacement therapy for hypothyroidism of any cause. The TxGNN model's top-ranked prediction is that it may also be effective for **Endemic Goiter**, with **1 clinical trial** and **20 publications** currently retrieved as supporting evidence — though the single trial found does not test LT4 directly.

*Note on the wider evidence pack:* this candidate set actually contains 10 TxGNN-predicted indications for levothyroxine. Several (nodular goiter, nontoxic goiter, dyshormonogenic goiter, lingual goiter, substernal goiter) are goiter/thyroid-axis conditions with genuine, sometimes strong, LT4 clinical evidence — this cross-validates the model. Three others (renal hypodysplasia/aplasia, bilateral renal agenesis, Potter sequence) are flagged in the evidence pack itself as likely knowledge-graph embedding artifacts with no mechanistic or clinical support, and Carney complex evidence describes disease association, not LT4 treatment. This report follows the requested single-indication format and covers rank 1 (endemic goiter) in full; see the note under "Why is This Prediction Reasonable" for how it compares to the stronger-evidence alternatives in the same pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory data (drug currently unlicensed in Taiwan; 0 license records). Levothyroxine's globally established indication is replacement therapy for hypothyroidism — this is general pharmacological knowledge, not sourced from the evidence pack. |
| Predicted New Indication | Endemic Goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is flagged as a data gap in the evidence pack (DG002, High severity). Based on well-established pharmacology, levothyroxine is the synthetic form of endogenous thyroxine (T4) and is converted peripherally to the active hormone T3; it is the standard replacement therapy wherever endogenous thyroid hormone production is insufficient.

Endemic goiter arises predominantly from chronic iodine deficiency, which impairs thyroid hormone synthesis, lowers circulating T4/T3, and drives compensatory, TSH-mediated thyroid enlargement. LT4 supplementation directly corrects the hormone deficit and, by restoring negative feedback, suppresses the excess TSH drive that causes the goiter. This is described in the evidence pack's own rationale as a "mechanistically clear, public-health/clinical-consensus treatment" — it is closer to an established use than a novel repurposing hypothesis.

The caveat is evidentiary rather than mechanistic: the one clinical trial retrieved (NCT04482907) tested a dill (*Anethum graveolens*) extract, not LT4, in thyroiditis/nodular goiter patients (relevance grade C — title-level match only). Direct LT4 trial data specific to the "endemic goiter" label was not found in this search; the literature base is largely epidemiological/review-level. Within the same evidence pack, rank 3 ("nodular goiter") and rank 8 ("nontoxic goiter") show materially stronger, LT4-specific clinical evidence (a 1,024-patient Phase 4 RCT and a randomized LT4-vs-radioiodine trial, respectively), which supports the plausibility of the endemic goiter link even though a matching high-quality LT4 trial for that specific label is missing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | N/A | Completed | 68 | Randomized placebo-controlled study of Anethum graveolens (dill) extract, not levothyroxine, in thyroiditis and nodular goiter patients; evaluated hormone levels, inflammatory markers, and nodule size over 90 days. Relevance graded C — tests a different intervention than LT4. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Multicenter trial | Deutsche medizinische Wochenschrift | 74 patients with diffuse endemic goiter treated 6 months with LT4 alone vs. LT4 + potassium iodide; both regimens reduced goiter volume, followed by iodide-only maintenance phase. Most directly relevant LT4 evidence in this set. |
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | Cohort/Trial | Current Medical Research and Opinion | Maternal iodine supplementation study (460 pregnant women) in goiter-endemic vs. non-endemic areas; assessed thyroid function and birth outcomes. |
| [4312017](https://pubmed.ncbi.nlm.nih.gov/4312017/) | 1969 | Field trial | American Journal of Clinical Nutrition | Prophylaxis and treatment of endemic goiter with iodized oil in rural Ecuador and Peru. |
| [4310499](https://pubmed.ncbi.nlm.nih.gov/4310499/) | 1969 | Field trial | Journal of Clinical Endocrinology and Metabolism | Prophylaxis and treatment of endemic goiter in Peru with iodized oil. |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Cohort | Journal of Clinical Endocrinology and Metabolism | Maternal/fetal thyroid function study in a severe endemic goiter region (Zaïre); compared untreated mothers to iodized-oil-treated and control groups. |
| [6309889](https://pubmed.ncbi.nlm.nih.gov/6309889/) | 1983 | Cohort | Journal of Clinical Endocrinology and Metabolism | Iodized oil injection in 58 goitrous patients (Greece); goiter size decreased with treatment; thyroid hormone and autoantibody changes tracked over 6 months. |
| [36839362](https://pubmed.ncbi.nlm.nih.gov/36839362/) | 2023 | Review | Nutrients | Overview and update on iodine deficiency and iodine prophylaxis, including populations at higher requirement (infants, pregnancy). |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World Journal of Surgery | Establishes iodine deficiency as the primary cause of endemic goiter and reviews prevention/treatment via iodine supplementation. |
| [7704809](https://pubmed.ncbi.nlm.nih.gov/7704809/) | 1994 | Review | Current Therapy in Endocrinology and Metabolism | General review of endemic goiter pathophysiology and management. |
| [6304776](https://pubmed.ncbi.nlm.nih.gov/6304776/) | 1983 | Review | Progress in Clinical and Biological Research | TSH secretion and regulation in endemic goiter and endemic cretinism; describes elevated TSH in chronic iodine deficiency. |

## Taiwan Market Information

Currently no marketing authorization records for levothyroxine in the Taiwan regulatory dataset (market status: 未上市 / Not Marketed; 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — TFDA label data is flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for LT4 in endemic goiter (correcting iodine-deficiency-driven hypothyroidism and suppressing TSH-mediated thyroid enlargement) is well established and consistent with decades of literature, but the retrieved clinical trial evidence for this specific label is indirect (one dill-extract trial, no direct modern LT4 RCT), placing it at evidence level L3. A Blocking safety data gap (TFDA label) also prevents a full S1 safety review.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking gap (DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Verification of Taiwan market/licensing pathway, since the drug is currently unlicensed (未上市)
- A direct LT4-specific trial or systematic review in endemic-goiter populations, since the one retrieved trial tests a different intervention
- Consider cross-referencing with the same pack's nodular goiter (L1) and nontoxic goiter (L2) predictions, which carry stronger direct LT4 evidence for closely related goiter subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

