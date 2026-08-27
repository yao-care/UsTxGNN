---
layout: default
title: Estrone
parent: 僅模型預測 (L5)
nav_order: 677
evidence_level: L5
indication_count: 2
---

# Estrone
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

# Estrone: From Unrecorded Original Indication to Elevated Plasma Zinc (Likely Spurious Signal)

## One-Sentence Summary

Estrone's original approved indication and mechanism of action are not documented in the available data (DrugBank and TFDA records return no confirmed original indication for this entry). TxGNN's top prediction links Estrone to **"elevated plasma zinc"** with a 99.81% score, but this is supported by only **0 clinical trials** and **2 tangentially related publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph artifact rather than a genuine repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no approved indication data available for Estrone |
| Predicted New Indication | Elevated plasma zinc (a lab finding, not a formal disease diagnosis) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Estrone is not available in this evidence pack, and no confirmed original approved indication is on file. This absence limits any formal assessment of mechanistic plausibility between Estrone and either predicted target.

For the top-ranked prediction, **"zinc, elevated plasma,"** the evidence pack's own rationale flags this as likely model noise: elevated plasma zinc is a laboratory finding rather than a clinical diagnosis, and TxGNN's knowledge graph is known to occasionally match drugs to lab-value nodes instead of genuine disease indications. While estrogens can theoretically influence ceruloplasmin and trace-element metabolism, no retrieved literature directly supports Estrone lowering plasma zinc — the two associated publications discuss unrelated topics (pituitary-gonadal recovery in malnourished men; iron/antioxidant status with soy protein in perimenopausal women). This prediction should be treated as a spurious node match rather than a real repurposing hypothesis.

The second-ranked prediction, **pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome**, is a PSTPIP1-driven autoinflammatory disease centered on IL-1β pathway hyperactivation, typically treated with IL-1 or TNF inhibitors. Estrone, as an estrogen receptor agonist, has no established mechanistic link to this inflammasome pathway — only a weak, unsupported hypothesis about general estrogen-immune modulation exists, with zero clinical trials or literature to substantiate it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [807594](https://pubmed.ncbi.nlm.nih.gov/807594/) | 1975 | Cohort | The Journal of Clinical Endocrinology and Metabolism | Studied the pituitary-gonadal axis in malnourished men; testosterone/LH normalized with refeeding. No direct mention of estrone or zinc. |
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Cohort | The American Journal of Clinical Nutrition | Examined iron indexes and antioxidant status with soy protein intake in perimenopausal women; notes estrogen deficiency may relate to oxidative stress and iron stores, but does not address plasma zinc or Estrone directly. |

---

## US Market Information

Currently no US market authorization records available (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available for Estrone in this evidence pack — this is flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications carry Evidence Level L5 (model prediction only), with zero clinical trials for either candidate and only two loosely related publications for the top candidate. The top-ranked "zinc, elevated plasma" signal is explicitly assessed as a likely spurious knowledge-graph match rather than a genuine indication, and Estrone is not currently marketed in the US.

**To proceed, the following is needed:**
- Estrone's original approved indication and mechanism of action (currently missing — DG002, High severity)
- TFDA/US labeling warnings and contraindications (currently missing — DG001, Blocking severity, required before any S1 safety review)
- A data-quality review of whether "zinc, elevated plasma" should be excluded from TxGNN's disease vocabulary as a non-disease lab-finding node
- If PAPA syndrome is pursued further, preclinical mechanistic studies connecting estrogen signaling to IL-1β/inflammasome activity, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

