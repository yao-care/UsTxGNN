---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 689
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is an irreversible steroidal aromatase inhibitor that lowers estrogen and is marketed in the US as Aromasin and several generics.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but this is a knowledge-graph prediction only.
There are **0 clinical trials** and **0 publications** supporting it, and no plausible mechanistic link was found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (the license records contain no indication text; this is inferred from the drug class and the retrieved literature) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 (one NDA plus generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the Evidence Pack. Based on known information, exemestane blocks the aromatase enzyme irreversibly, which reduces the conversion of androgens into estrogens and lowers circulating estrogen.

That mechanism does not connect to the predicted disease. Antithrombin deficiency type 2 is an inherited defect in the antithrombin protein (SERPINC1), and lowering estrogen does not correct it. The high score (0.998) most likely reflects clustering of coagulation-related disease nodes in the knowledge graph, not drug-specific biology.

Three other high-scoring predictions for this drug (factor V excess, heparin cofactor 2 deficiency and thrombophilia) have similar scores. They appear to come from the same knowledge-graph neighborhood and should not be read as independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records contain no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA209208 | Exemestane | Tablet | Upsher-Smith Laboratories, Inc. |
| ANDA210323 | Exemestane | Tablet | Cipla USA Inc. |
| NDA020753 | Aromasin | Tablet | Pharmacia & Upjohn Company LLC |
| ANDA216454 | Exemestane | Film-coated tablet | NorthStar Rx LLC |
| ANDA213547 | Exemestane | Film-coated tablet | Florida Pharmaceutical Products, LLC |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, a steroidal aromatase inhibitor. It is not a conventional cytotoxic chemotherapy. |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

Antithrombin deficiency is a thrombotic disorder, so any use in that setting would need a dedicated thromboembolic safety review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or literature, and the estrogen-lowering mechanism does not address an inherited antithrombin protein defect.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking aromatase inhibition to antithrombin function. Without one, this candidate should be deprioritized.
- Package insert warnings and contraindications (a blocking gap for safety screening) and detailed MOA data from DrugBank.
- Any preclinical or clinical signal for this indication. None currently exists.

Also on hold (all Hold): amenorrhea (literature is indirect, and amenorrhea is a treatment outcome in these studies, not something exemestane treats), factor V excess, heparin cofactor 2 deficiency, thrombophilia, migraine disorder and migraine with brainstem aura. None has trial evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

