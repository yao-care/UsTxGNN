---
layout: default
title: Glucarpidase
parent: Model Prediction Only (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
monitor_inn: "GLUCARPIDASE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "tetanic cataract", "mature cataract", "immature cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "nuclear senile cataract", "senile cataract"]
last_modified_at: 2026-10-31
description: "Glucarpidase: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not listed in the data compiled for this report (the drug's establish…"
---

# Glucarpidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Glucarpidase: From Methotrexate Toxicity Rescue to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Glucarpidase is a recombinant enzyme (marketed as Voraxaze) that breaks down methotrexate in the blood. The TxGNN model predicts it may be useful for **diabetic cataract** and several other eye conditions. There are currently **0 clinical trials** and **0 publications** supporting this prediction, and the mechanistic review found no biological rationale for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (the drug's established use is reducing toxic plasma methotrexate levels in patients with delayed methotrexate clearance due to impaired kidney function) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, glucarpidase is a recombinant bacterial carboxypeptidase G2. It hydrolyzes extracellular methotrexate and other folates into inactive metabolites, which is why it is used to clear toxic methotrexate levels.

The review found no plausible link between this mechanism and diabetic cataract. Diabetic cataract involves the polyol pathway, aldose reductase activity, and oxidative stress in the lens, and glucarpidase acts on none of these. As a large protein given intravenously, it is also unlikely to reach the avascular lens in meaningful amounts.

The prediction should be treated with caution:
- The score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- All ten predicted indications are eye diseases (diabetic cataract, diabetic retinopathy, tetanic, mature, immature, craniostenosis, type 2 diabetes-associated, cortical, nuclear senile, and senile cataract).
- Their scores cluster at nearly identical values (0.9982 to 0.9985). Several cataract subtypes share exactly the same score, which suggests a generic disease-class association rather than a specific mechanistic one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125327 | Voraxaze (BTG International Inc.) | Injection, powder, for solution | Not listed in the compiled data (status: valid) |

## Safety Considerations

- **Drug Interactions**: Eight moderate-level interactions were identified, all involving folate-pathway drugs: proguanil, trimethoprim, levoleucovorin, pemetrexed, pralatrexate, pyrimethamine, leucovorin, and trimetrexate.

Please refer to the package insert for warnings and contraindications, as this information was not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials, no publications, and no plausible mechanism. The repeated near-identical scores across eye diseases point to a model artifact.

**To proceed, the following is needed:**
- Complete mechanism of action data and the FDA package insert warnings and contraindications
- A credible mechanistic hypothesis connecting folate or methotrexate hydrolysis to lens or retinal disease
- Preclinical evidence (for example, lens or retinal models) showing relevant activity
- Assessment of whether ocular delivery is feasible for a large enzyme protein
- Independent confirmation that the prediction is not an artifact of similarities the model learned between related diseases, for example by checking whether other drugs show the same cluster of eye-disease scores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

