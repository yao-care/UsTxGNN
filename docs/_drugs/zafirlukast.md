---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 1300
evidence_level: L5
indication_count: 2
---

# Zafirlukast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Zafirlukast: From Asthma to Bronchitis

## One-Sentence Summary

Zafirlukast is an oral leukotriene receptor antagonist. The literature in the Evidence Pack describes it as indicated for prophylaxis and treatment of chronic asthma.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** retrieved for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic asthma (per literature; the US licence records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 (licences on record, including NDA and ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the supplied literature, zafirlukast is a selective CysLT1 (cysteinyl leukotriene) receptor antagonist. Its efficacy in asthma has been described extensively in reviews.

Cysteinyl leukotrienes cause bronchoconstriction, mucus secretion, increased vascular permeability and eosinophil recruitment. Bronchitis shares airway inflammation and mucus hypersecretion with asthma, so blocking this pathway could plausibly help. This reasoning is an inference and is not supported by any retrieved study on bronchitis.

The TxGNN score is very high, but the knowledge-graph basis cannot be checked because the original indications and mechanism of action are missing. A high model score without supporting studies should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The licence records contain no approved-indication text. The table therefore shows the manufacturer instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA213163 | Zafirlukast | Tablet, film coated | Aurobindo Pharma Limited |
| NDA020547 | Zafirlukast | Tablet, coated | Strides Pharma Science Limited |
| ANDA090372 | Zafirlukast | Tablet, film coated | American Health Packaging |
| ANDA090372 | Zafirlukast | Tablet, film coated | Dr. Reddys Laboratories Limited |
| NDA020547 | ACCOLATE | Tablet, film coated | Strides Pharma Science Limited |

All listed products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

The literature in the Evidence Pack includes a review of liver injury associated with leukotriene antagonists (PMID 12879996). Hepatic monitoring should be considered in any development plan.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but no trials or publications support bronchitis, so this remains a model prediction only (L5). The pack lists the package insert warnings and contraindications as a blocking data gap, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking), from the FDA label
- Mechanism of action and original indication data, from DrugBank
- A systematic search for bronchitis-specific trials and literature, including acute versus chronic bronchitis
- A mechanistic and clinical case that separates bronchitis from the existing asthma use
- Route compatibility assessment, which is pending

**Note:** The second prediction, obstructive lung disease (including COPD), has more support. It is rated L3 with 19 publications, including two COPD-related clinical studies (PMID 12877822, PMID 11694805). Its study designs and sample sizes are unverified, and no trials are registered. It is a better candidate for follow-up as a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

