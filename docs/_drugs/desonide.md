---
layout: default
title: Desonide
parent: 僅模型預測 (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: From Inflammatory Skin Conditions to Polyp of Vocal Cord

## One-Sentence Summary

Desonide is a low-potency synthetic topical corticosteroid (Class VI), primarily used to treat mild-to-moderate inflammatory skin conditions such as atopic dermatitis and eczema.
The TxGNN model predicts it may be effective for **Polyp of Vocal Cord**, with **0 clinical trials** and **0 publications** currently identified to support this direction.
The current evidence rests entirely on model prediction (Level L5), and this repurposing direction requires substantial preclinical and clinical investigation before further development can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory skin conditions (atopic dermatitis, eczema) |
| Predicted New Indication | Polyp of Vocal Cord |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Desonide is a synthetic non-fluorinated corticosteroid belonging to Class VI (low-potency) on the topical steroid potency scale. Although detailed MOA data is not available from the current evidence pack, desonide shares the glucocorticoid class mechanism: binding to intracellular glucocorticoid receptors, leading to downstream suppression of pro-inflammatory cytokines (including IL-6 and TNF-α), reduced capillary permeability, and inhibition of leukocyte infiltration — all of which attenuate local mucosal edema and inflammation.

Vocal cord polyps develop from chronic mechanical irritation (vocal overuse, vocal abuse) combined with local mucosal edema and inflammatory cell infiltration. In otolaryngology practice, corticosteroids — particularly triamcinolone acetonide injected intralesionally — are used off-label to reduce vocal cord lesion volume by suppressing local inflammatory and early fibrotic processes. This provides a distant mechanistic analogy for desonide's predicted utility: the drug class is mechanistically active in the relevant tissue process, even if desonide itself has never been studied in this context.

However, this analogy is substantially weakened by two critical barriers. First, desonide is formulated exclusively for topical (dermal) and otic use; no established delivery route to the vocal cord mucosa exists, and nebulized or injectable formulations have not been investigated. Second, its potency class (Class VI — the lowest tier) is far below the corticosteroids routinely used in ENT practice (e.g., Class I triamcinolone). The TxGNN prediction most likely captures a broad "corticosteroid–polyp" co-occurrence signal in the knowledge graph rather than a drug-specific mechanistic prediction. No preclinical or clinical evidence supports this specific application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Desonide is not currently registered or marketed in Taiwan. No active licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications are at Evidence Level L5 (model prediction only), with zero supporting clinical trials or published literature across any of the predicted polyp-type targets. For the top-ranked indication (polyp of vocal cord), there is no feasible established delivery route, and desonide's low potency class further undermines mechanistic plausibility compared to corticosteroids already in ENT use.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank to confirm glucocorticoid receptor binding profile and pharmacokinetic parameters
- Download and parse the Taiwan/US package insert (TFDA/FDA) to complete the safety and contraindication assessment
- Identify whether any nebulized, injectable, or intralaryngeal corticosteroid delivery system could be adapted for desonide
- Conduct a systematic literature review on intralaryngeal and intratracheal corticosteroid use as a surrogate mechanistic model
- Perform preclinical feasibility assessment on vocal cord mucosal tissue models before any clinical translation is considered
- Flag **neoplastic polyp (Rank 8)** as explicitly unsuitable for future study design, as corticosteroid use in Wnt/β-catenin–driven premalignant lesions lacks mechanistic rationale and may carry immunosuppression risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

