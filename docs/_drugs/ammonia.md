---
layout: default
title: Ammonia
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
---

# Ammonia
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

# Ammonia: From No Established Therapeutic Indication to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Ammonia (NH₃, DrugBank DB11118) is a simple inorganic compound with no established therapeutic indication in available US regulatory records.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans (ACA)** with a prediction score of **99.70%**;
however, **no clinical trials and no published literature** currently support this direction, and the mechanistic rationale is considered biologically implausible across all 6 predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established therapeutic indication on record |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Ammonia (DB11118). From a biochemical standpoint, ammonia is a simple nitrogenous compound that arises endogenously as a byproduct of amino acid catabolism. Under normal physiological conditions it is rapidly converted to urea in the liver via the urea cycle. At elevated concentrations, ammonia is neurotoxic and disrupts cellular energy metabolism — properties that define it primarily as a metabolic intermediate and toxin, not a therapeutic agent.

Acrodermatitis chronica atrophicans (ACA) is a late-stage skin manifestation of Lyme disease caused by *Borrelia burgdorferi* infection. Its hallmark is progressive dermal atrophy and it requires prolonged antibiotic therapy (typically doxycycline) to eradicate the underlying infection. There is no established biological mechanism by which exogenous ammonia administration would inhibit *Borrelia* replication, suppress the associated inflammatory cascade, or reverse atrophic skin changes. The same absence of mechanistic plausibility applies across all 6 predicted indications, which span autoimmune dermatomyositis variants, fibroproliferative acne keloid, childhood interstitial lung disease, and a rare EBV-linked photosensitivity disorder — disease categories whose standard-of-care therapies (immunosuppressants, antibiotics, targeted biologics) share no overlap with ammonia's known biochemistry.

This pattern strongly suggests a **model false positive** arising from ammonia's ubiquitous representation in metabolic pathways within the TxGNN knowledge graph, creating spurious co-occurrence associations with diverse disease nodes. The high raw prediction scores (all >99.5%) paradoxically reflect network topology artifacts rather than true biological signal. This prediction should not be interpreted as a credible repurposing opportunity without an independent mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ammonia in any of the 6 predicted indications.

---

## Literature Evidence

Currently no related literature available for Ammonia in any of the 6 predicted indications.

---

## US Market Information

No NDA or marketing authorization found for Ammonia in the United States. The drug has no current US market presence.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important context**: Ammonia is a recognized respiratory irritant and systemic toxin. Inhalation of concentrated ammonia causes chemical burns to the airways, and systemic exposure at supratherapeutic levels produces hyperammonemia with encephalopathy. Any experimental administration in humans would require extensive toxicological justification.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 6 TxGNN-predicted indications for Ammonia are rated L5 with zero supporting clinical trials or published literature; each mechanistic rationale provided in the Evidence Pack independently concludes that the prediction lacks biological plausibility, and the drug's inherent toxicity profile creates an unfavorable risk baseline that cannot be offset without a credible therapeutic hypothesis.

**To proceed, the following is needed:**
- **Expert triage review**: Confirm whether these high-score predictions are systematic knowledge-graph artifacts for metabolic compounds in TxGNN, and consider flagging Ammonia for exclusion from active repurposing pipelines
- **Mechanistic hypothesis generation**: Before any experimental consideration, a peer-reviewable mechanistic rationale connecting ammonia to at least one predicted indication must be established
- **Full toxicological safety profile**: Retrieve complete package insert, occupational exposure limits, and NOAEL/LOAEL data before advancing to any preclinical study design
- **Model calibration note**: The pattern of high scores across biologically unrelated indications warrants review of how endogenous metabolites are represented in the TxGNN training graph, to reduce false-positive burden in future prediction runs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

