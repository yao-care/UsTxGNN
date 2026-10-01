---
layout: default
title: Estrone
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 2
---

# Estrone
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

# Estrone: From an Unspecified Original Indication to Elevated Plasma Zinc

## One-Sentence Summary

Estrone is an estrogen hormone. The Evidence Pack does not record an approved indication for it.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but there are **0 clinical trials** and only **2 loosely related publications**, so this is a knowledge-graph prediction with no real supporting evidence yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 (as assigned in the Evidence Pack; the two papers are only loosely related) |
| US Market Status | ✓ Marketed |
| Number of Licenses | 20 (license numbers not recorded) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. No established pharmacological mechanism links estrone to plasma zinc levels.

The two retrieved papers are only indirectly related. One studies gonadal hormone status in malnourished men, a setting where zinc status is a known confounder. The other studies soy protein and iron/antioxidant indexes in perimenopausal women, where estrogen status is a covariate and zinc is not the outcome.

The very high TxGNN score (0.998) reflects a knowledge-graph association only. Without a documented mechanism or original indication, it cannot be checked pharmacologically.

A second prediction, **pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome** (score 99.30%, evidence level L5), has no trials or literature. PAPA is a rare IL-1-driven autoinflammatory disorder, and no link to estrone is documented in the supplied data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [807594](https://pubmed.ncbi.nlm.nih.gov/807594/) | 1975 | Observational | J Clin Endocrinol Metab | In 28 men with severe protein-calorie malnutrition, clinical hypogonadism and low testosterone were seen with high LH. Testosterone recovered to normal after 2-5 months of refeeding. Zinc is not the study outcome. |
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Clinical study | Am J Clin Nutr | Examined iron indexes and antioxidant status with soy protein intake in perimenopausal women. The outcome is iron, not zinc, and the design was not verified. |

---

## US Market Information

The Evidence Pack lists 5 main entries. They are identical: product **Folliculinum**, dosage form **pellet**, manufacturer **Boiron**. License numbers and approved-indication text are not recorded.

Across all 20 licenses, the recorded dosage forms are pellet, liquid, spray, oral tablet, and solution/drops.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, the two papers do not address zinc, no mechanism is documented, and the original indication and safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), for example from DrugBank
- Package insert warnings and contraindications, which are blocking for safety screening
- The original approved indication and license numbers for the marketed products
- A targeted literature search on estrogen exposure and plasma zinc, to test whether a plausible link exists
- Reassessment of the evidence level if no direct evidence is found (L5 would be more appropriate)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

