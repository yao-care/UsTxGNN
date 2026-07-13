---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab (brand name: Tepezza) is a fully human IgG1 monoclonal antibody that inhibits the insulin-like growth factor-1 receptor (IGF-1R), originally approved by the US FDA for thyroid eye disease (Graves' ophthalmopathy).
The TxGNN model predicts **Monosomy X (classical Turner syndrome, 45,X)** as the top new indication with a score of **99.79%**, but mechanistic analysis reveals this is a direct counterindication — Turner syndrome patients already have deficient IGF-1/IGF-1R signaling, making further inhibition therapeutically contradictory.
No clinical trials or published literature support any of the 10 predicted indications; all are rated **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thyroid Eye Disease (US FDA-approved as Tepezza; not registered in Taiwan) |
| Predicted New Indication (Rank 1) | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Teprotumumab blocks IGF-1R, a receptor that is abnormally overactivated in thyroid eye disease. In TED, co-stimulation of IGF-1R and the TSH receptor on orbital fibroblasts drives tissue inflammation, glycosaminoglycan accumulation, and proptosis. By selectively neutralizing IGF-1R, Teprotumumab disrupts this signaling loop, reducing orbital congestion. It received FDA approval in January 2020 as the first disease-modifying therapy for TED.

Monosomy X (Turner syndrome, 45,X) presents the opposite problem: patients characteristically have a hypoactive IGF-1/IGF-1R axis, manifesting as short stature and impaired somatic growth. The standard of care is recombinant growth hormone therapy — a treatment explicitly designed to *enhance* IGF-1R-mediated signaling. Introducing an IGF-1R inhibitor into this context would directly oppose the therapeutic goal, making this prediction not merely unsupported but mechanistically counterindicated.

This pattern repeats across nearly all top-10 TxGNN predictions. The high scores most likely reflect knowledge graph node-sharing — both Teprotumumab and Turner-spectrum disorders connect through the IGF-1R node — rather than genuine treatment hypotheses. The three vascular predictions (esophageal varices, varicose disease) represent a distinct mechanistic cluster: IGF-1R inhibition might theoretically slow hepatic stellate cell activation or vascular smooth muscle cell proliferation, but these are extremely indirect, second-order effects with zero preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## US Market Information

Teprotumumab is not registered in Taiwan (0 approved licenses on record). It is marketed in the United States under the brand name **Tepezza** (teprotumumab-trbw) by Horizon Therapeutics for thyroid eye disease. Taiwan regulatory filing has not been initiated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Full Prediction Landscape

All 10 TxGNN predictions are at evidence level **L5** with no clinical or preclinical evidence retrieved. The table below provides a mechanistic verdict for each:

| Rank | Predicted Indication | TxGNN Score | Decision | Mechanistic Note |
|------|---------------------|-------------|----------|-----------------|
| 1 | Monosomy X | 99.79% | **Hold** | IGF-1R already deficient in 45,X; inhibition is counterindicated and opposes GH therapy |
| 2 | Esophageal varices with bleeding | 99.64% | Research Question | Indirect pathway: IGF-1R → hepatic stellate cell activation → fibrosis → portal hypertension; no mechanism for acute hemorrhage |
| 3 | Esophageal varices without bleeding | 99.64% | Research Question | Same indirect pathway; preventive framing slightly more plausible but lacks any evidence |
| 4 | Mixed gonadal dysgenesis | 99.50% | **Hold** | Developmental disorder driven by chromosomal anomaly; IGF-1R inhibition during development is counterindicated |
| 5 | Mitochondrial OXPHOS disorder (nuclear DNA) | 99.44% | **Hold** | IGF-1R inhibition suppresses PI3K/AKT/mTOR → impairs mitochondrial biogenesis; directly worsens the target pathology |
| 6 | Turner syndrome (structural X anomaly) | 99.37% | **Hold** | Identical counterindication to monosomy X; structural anomaly variant does not change the logic |
| 7 | Mosaic monosomy X | 99.37% | **Hold** | Milder 45,X/46,XX phenotype, but the same mechanistic counterindication applies |
| 8 | Sex chromosome DSD | 99.34% | **Hold** | Broad developmental category; IGF-1R inhibition has no therapeutic rationale in sex-determination disorders |
| 9 | Varicose disease | 99.33% | Research Question | Biologically plausible: IGF-1R drives VSMC proliferation and venous wall remodeling; warranting basic science inquiry only |
| 10 | X chromosome number anomaly | 99.32% | **Hold** | Parent ontology concept of the Turner group; same mechanistic counterindication propagated by disease ontology hierarchy |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Seven of the ten predictions involve chromosomal or developmental disorders where IGF-1R inhibition directly opposes the existing therapeutic strategy (growth hormone enhancement), making them mechanistic counterindications rather than repurposing opportunities. The remaining three vascular predictions are biologically speculative with no preclinical or clinical evidence, insufficient to justify a development program.

**To proceed, the following is needed:**

- **For vascular indications (Research Question tier):** In vitro studies testing IGF-1R blockade in hepatic stellate cell or vascular smooth muscle cell models to establish proof-of-concept before any human research is considered
- **Full MOA and safety profile:** Retrieve complete Teprotumumab mechanism of action, boxed warnings, and contraindications from DrugBank and the FDA-approved package insert (Tepezza PI)
- **Re-evaluate with broader evidence scope:** The current Evidence Pack was queried against Teprotumumab + each predicted disease as a paired search; broadening to IGF-1R inhibitor class-level searches may surface additional mechanistic literature
- **Taiwan regulatory pathway:** If any preclinical data emerges for the vascular indications, assess TFDA requirements for IND filing and whether the US FDA approval package (TED indication) can support a regulatory bridging strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

