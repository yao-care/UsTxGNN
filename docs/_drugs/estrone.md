---
layout: default
title: Estrone
parent: Model Prediction Only (L5)
nav_order: 677
evidence_level: L5
indication_count: 2
monitor_inn: "ESTRONE"
predicted_indications: ["zinc, elevated plasma", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome"]
last_modified_at: 2026-10-14
description: "Estrone: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Estrone: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Estrone is an estrogen, and the only original indication in the data compiled for this report is acne.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but there are **0 clinical trials** and only **1 loosely related publication** behind this prediction.
The prediction rests on a computational score alone and has no direct clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, estrone is an estrogen, and the knowledge graph links it to acne. Whether and how it would affect plasma zinc has not been established.

The only retrieved publication (PMID 12081830) studied soy protein and isoflavone intake in perimenopausal women and measured iron indexes and antioxidant status. It did not test estrone and did not report plasma zinc. Any link would be indirect, for example through estrogen effects on trace metal metabolism, and is speculative. The high TxGNN score (0.998) is a model output and should not be read as clinical validation.

A second predicted indication, pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome (score 99.30%), also has no trials and no literature. It is an autoinflammatory disorder driven by excess IL-1beta, and no evidence connects estrone to that pathway. The score likely reflects network proximity through the acne association.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Clinical study (dietary intervention) | The American Journal of Clinical Nutrition | Soy protein intake in perimenopausal women and its effect on iron indexes and total antioxidant status. It did not test estrone or measure plasma zinc, so relevance is indirect. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Folliculinum (Boiron) | Pellet | Not stated (status: cancelled) |

Other dosage forms recorded for estrone-containing products include liquid, spray, oral tablet and solution/drops.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** Estrone is linked to possible contraindications in many conditions. Examples include:
  - Cardiovascular and metabolic: hypertension, diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypertriglyceridemia, hypercalcemia, nephrocalcinosis.
  - Hepatic and biliary: liver failure, liver disease, gallbladder disease, porphyria.
  - Endocrine: hypothyroidism.
  - Neurological and psychiatric: epilepsy, anxiety disorder, dysthymic disorder, focal hand dystonia, blepharospasm.
  - Immune and respiratory: systemic lupus erythematosus, asthma.
  
  These come from a network resource and need confirmation against official labelling.
- **Drug Interactions:** 100 interactions were recorded, and the 20 listed in the data are mostly moderate. Main examples:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide.
  - Antidiabetic agents: metformin, acarbose, canagliflozin, dapagliflozin, empagliflozin, alogliptin, saxagliptin, albiglutide, dulaglutide, chlorpropamide.
  - Others: aprepitant, clarithromycin, calcitriol (topical), chenodeoxycholic acid.
  - Cimetidine is the one minor interaction listed.

Please refer to the package insert for full safety information, as no label warnings or contraindications were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no direct literature, and no established mechanism. The sole publication is only tangentially related. In addition, the product's US authorization is cancelled and label safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data for estrone, and any evidence linking estrogen activity to zinc homeostasis
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Evidence that elevated plasma zinc is a meaningful clinical target, and studies measuring zinc in estrogen-treated patients
- Clarification of the relationship between the original indication (acne) and the predicted indication
- Route and formulation compatibility assessment, given the cancelled US status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

