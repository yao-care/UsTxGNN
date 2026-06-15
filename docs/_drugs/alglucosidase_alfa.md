---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa (Myozyme/Lumizyme) is a recombinant human acid alpha-glucosidase (GAA) enzyme replacement therapy, originally approved for Pompe disease (glycogen storage disease type II, GSD-II) — a lysosomal glycogen metabolism disorder.
The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease (APBD)**,
however, **0 clinical trials** and **0 publications** currently support this specific direction, making this a model-only prediction at present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pompe disease (GSD-II / acid maltase deficiency) |
| Predicted New Indication | Adult Polyglucosan Body Disease (APBD) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | Not registered in current dataset (0 licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, alglucosidase alfa is a recombinant form of human lysosomal acid alpha-glucosidase (GAA). It functions as enzyme replacement therapy (ERT) for Pompe disease, in which GAA deficiency leads to progressive lysosomal glycogen accumulation in cardiac and skeletal muscle — ultimately causing cardiomyopathy, respiratory failure, and limb girdle weakness.

Adult Polyglucosan Body Disease (APBD) is a distinct glycogen metabolism disorder caused by mutations in the *GBE1* gene (glycogen branching enzyme), leading to accumulation of abnormally structured polyglucosan bodies primarily in neurons and axons — an extralysosmal pathway. Both conditions belong to the broader family of glycogen storage disorders (GSDs), which explains the high TxGNN prediction score (0.9947): the model likely detects topological proximity between these two diseases within the GSD family graph, rather than enzyme target overlap.

The mechanistic connection is therefore indirect. Alglucosidase alfa targets GAA within lysosomes, whereas APBD involves GBE1 deficiency outside the lysosomal compartment. There is no published human trial or case report supporting ERT with alglucosidase alfa for APBD. The TxGNN high score reflects GSD family graph proximity — not enzymatic functional homology — and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Status

No licenses found in the current dataset. The regulatory query for alglucosidase alfa returned 0 results.

> **Note:** This may reflect a data pipeline gap. Alglucosidase alfa is known to have received regulatory approval in major markets under the brand names Myozyme (infantile-onset Pompe disease) and Lumizyme (late-onset Pompe disease). A direct regulatory database query is recommended to confirm current licensure status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.47%) to APBD based on glycogen storage disorder family proximity in the knowledge graph, but the enzyme targets are fundamentally different — alglucosidase alfa corrects GAA deficiency, while APBD involves GBE1 deficiency in a distinct metabolic pathway. No clinical trials, case reports, or published literature currently support this repurposing direction. The high-ranking ophthalmic predictions (ranks 4–10: congenital entropion, ectropion, Horner syndrome, epiblepharon, etc.) are assessed as model false positives with no mechanistic basis.

**To proceed, the following is needed:**
- Confirm whether any preclinical or in vitro studies have tested alglucosidase alfa or any GAA-modifying therapy in polyglucosan accumulation models
- Obtain TFDA/FDA package insert to fill safety data gaps (warnings, contraindications)
- Clarify regulatory dataset completeness — verify whether alglucosidase alfa holds any active US NDA records
- If mechanistic rationale for APBD is pursued further, literature review on glycogen metabolism crosstalk between lysosomal and cytoplasmic pathways would be the recommended first step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

