---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 934
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Mirtazapine: From Antidepressant Use to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a marketed antidepressant. The evidence pack does not include its approved indication text.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants** with a score of 99.42%, but **0 clinical trials** and **0 publications** support this prediction.
This is a model-only signal with no supporting mechanism, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license records (antidepressant per pharmacological class) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. The pharmacology below comes from the analyst's rationale, not from DrugBank. Mirtazapine is a noradrenergic and specific serotonergic antidepressant. It antagonises alpha-2 adrenergic, 5-HT2, 5-HT3 and H1 receptors.

Ohdo syndrome is a rare congenital developmental disorder, typically linked to KAT6B, a chromatin-modifier gene. No plausible pathway connects monoaminergic modulation to this pathology. The high score is most likely a knowledge-graph artifact from sparse or shared-neighbour annotations rather than a real pharmacological signal.

Two other predictions were reviewed:
- **Blepharophimosis – intellectual disability syndrome, Ohdo type (99.11%)** is the same disease as the top prediction under a different name. It is not independent evidence. At most, symptom-level use (mood or sleep) could be speculated, but that is not disease-modifying and has no supporting data.
- **Benign paroxysmal torticollis of infancy (99.11%)** is considered a migraine equivalent, often associated with CACNA1A variants. Some serotonergic antidepressants are used for migraine prophylaxis, but this is not established for mirtazapine or for infants. The condition is usually self-limiting, so the benefit-risk case for a systemic psychotropic in this age group is weak.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Approved indication text is not included in the records. The first five of 20 authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076921 | Mirtazapine | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA076541 | Mirtazapine | Tablet | Bryant Ranch Prepack |
| ANDA076122 | Mirtazapine | Tablet, film coated | Mylan Pharmaceuticals Inc. |
| ANDA076921 | Mirtazapine | Tablet, film coated | Advanced Rx Pharmacy of Tennessee, LLC |
| ANDA205798 | Mirtazapine | Tablet, orally disintegrating | Viona Pharmaceuticals Inc. |

All products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanistic link to a genetic developmental disorder. The two Ohdo syndrome predictions are one entity, so they are not independent support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data (for example from DrugBank)
- A credible biological link between mirtazapine's pharmacology and KAT6B-related pathology, or a defined symptom-level target
- Any preclinical or clinical study in Ohdo syndrome or benign paroxysmal torticollis of infancy
- Route and age-group compatibility assessment, especially for infants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

