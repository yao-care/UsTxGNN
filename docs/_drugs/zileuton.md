---
layout: default
title: Zileuton
parent: High Evidence (L1-L2)
nav_order: 1305
evidence_level: L1
indication_count: 10
---

# Zileuton
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Zileuton: From Chronic Asthma to Bronchitis

## One-Sentence Summary

Zileuton is an oral 5-lipoxygenase inhibitor that blocks leukotriene synthesis and is used for chronic asthma. The TxGNN model predicts it may be effective for **bronchitis** (its top-ranked prediction), but this prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic asthma (the license records contain no indication text; this comes from the evidence pack's rationale notes) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From the pack's literature, zileuton inhibits 5-lipoxygenase and so blocks production of leukotrienes (LTB4 and the cysteinyl-leukotrienes). These mediators drive bronchoconstriction, mucus secretion and airway inflammation.

Bronchitis is also an inflammatory airway condition with mucus hypersecretion, so a leukotriene-mediated link is plausible. However, no trial or publication in the dataset tests zileuton in bronchitis. The 99.99% score alone does not justify advancing this indication.

The pack also lists other predictions with much stronger support, and these are better starting points:

| Predicted Indication | Evidence Level | Pack Recommendation | Comment |
|------|------|------|------|
| Asthma | L1 | Proceed with Guardrails | Already the labeled use, so not true repurposing. 10 trials and 19 publications, including RCTs. |
| Obstructive lung disease (asthma/COPD) | L2 | Research Question | The only COPD-specific Phase 3 trial (NCT00493974) was terminated early. |
| Bronchial neoplasm | L2 | Research Question | Small Phase 2 chemoprevention and biomarker studies. |
| Atopic eczema | L3 | Research Question | Small human pilot study plus reviews. |
| Heart disease | L4 | Research Question | Preclinical evidence only. |
| Asthma-related traits, Laubry-Pezzi syndrome, interventricular septum aneurysm, Pierre Robin syndrome | L5 | Hold | No evidence. Most likely knowledge-graph artifacts. |

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

## Literature Evidence

Currently no related literature available for bronchitis.

## US Market Information

The license records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215742 | Zileuton | Film-coated extended-release tablet | Camber Pharmaceuticals, Inc. |
| ANDA212670 | Zileuton | Multilayer extended-release tablet | Strides Pharma Science Limited |
| ANDA204929 | Zileuton | Extended-release tablet | Rising Pharma Holdings, Inc. |
| ANDA215742 | Zileuton | Film-coated extended-release tablet | NorthStar RxLLC |
| ANDA212670 | Zileuton | Multilayer extended-release tablet | Golden State Medical Supply, Inc. |

All forms are oral. ANDA215742 and ANDA212670 each appear twice, under different distributors.

## Safety Considerations

Please refer to the package insert for safety information. FDA label warnings and contraindications are not in the Evidence Pack, and the pack lists this as a blocking data gap. No drug interaction records were found.

Published asthma data note reversible liver enzyme elevations in about 2% of patients in controlled trials (PMID 10181070), so liver function monitoring is a relevant consideration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has a very high model score but no trials, no literature and no safety data to support it. Evidence is L5, so it should not advance as a standalone repurposing candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any bronchitis-specific clinical or preclinical evidence
- A decision on whether to prioritize the better-supported candidates, such as COPD or obstructive lung disease (L2), instead of bronchitis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

