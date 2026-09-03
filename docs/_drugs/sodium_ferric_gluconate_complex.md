---
layout: default
title: Sodium Ferric Gluconate Complex
parent: 僅模型預測 (L5)
nav_order: 1169
evidence_level: L5
indication_count: 6
---

# Sodium Ferric Gluconate Complex
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Sodium Ferric Gluconate Complex: From Iron Deficiency Anemia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Sodium ferric gluconate complex (SFGC, brand name Ferrlecit) is an intravenous iron replacement product used to treat iron deficiency anemia, most commonly in hemodialysis and chronic kidney disease patients.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but **no clinical trials and no literature** currently support this specific prediction, and the underlying pharmacology appears to point in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (inferred from literature context; not present in structured regulatory data) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for SFGC in this evidence pack. Based on the literature context that *is* available (collected under other predicted indications in this same pack), SFGC is an intravenous iron-carbohydrate complex used to correct iron deficiency in dialysis and CKD populations — its efficacy there is well established and it was developed specifically as a safer alternative to iron dextran.

The predicted link to severe nonproliferative diabetic retinopathy, however, lacks a plausible mechanistic basis. Diabetic retinopathy progression is driven substantially by oxidative stress and microvascular damage. Iron is a pro-oxidant that can catalyze reactive oxygen species generation via the Fenton reaction — if anything, iron loading would be expected to *worsen* oxidative microvascular injury rather than treat it. This is the opposite direction implied by the model's high confidence score.

Given the complete absence of clinical trials or literature evidence directly connecting SFGC to this indication, and a mechanistic rationale that runs counter to the prediction, this candidate should be treated as a low-confidence, likely spurious signal rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

SFGC has no marketed authorizations on record in this evidence pack (0 licenses, market status: Not Marketed). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

No structured safety data (warnings, contraindications, DDI) is currently available for SFGC in this evidence pack.

**Important safety signal identified during evidence review (not from structured safety fields, but from literature collected under a separate candidate indication):**
- A substantial body of literature (12 publications, including RCTs, pharmacovigilance reviews, and case reports) documents that SFGC itself can **cause** anaphylactic/anaphylactoid reactions — including a case during pregnancy and a 2024 case report of a severe reaction requiring epinephrine and steroids. This appears to be a knowledge-graph mislabeling issue: TxGNN ranked "anaphylaxis" as a *predicted indication* (rank 3, score 99.5%), when the underlying evidence actually describes SFGC as a *cause* of anaphylactoid reactions, not a treatment for them. This should be treated as a drug safety finding, not a repurposing signal.

Please refer to the official package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the top predicted indications in this evidence pack (including the top-ranked severe nonproliferative diabetic retinopathy) are supported by clinical trials or literature specific to that indication, and the proposed mechanism runs counter to known iron pharmacology. In addition, one candidate ("anaphylaxis," rank 3) appears to reflect a reverse-causality error in the knowledge graph — the cited evidence describes SFGC causing anaphylactoid reactions, not treating them — which raises broader concern about the reliability of this prediction set for SFGC. Two other candidates (bronchitis-related trials) also appear to be mismapped anemia trials unrelated to the stated indication.

**To proceed, the following is needed:**
- TFDA/FDA package insert with confirmed warnings and contraindications (currently blocking, per data gap DG001)
- Verified mechanism of action data from DrugBank (data gap DG002)
- Independent confirmation of the diabetic retinopathy hypothesis in preclinical or mechanistic studies before any further investment
- Correction/review of the TxGNN knowledge graph edge for "anaphylaxis" to prevent this adverse-event-as-indication error from propagating to other drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

