---
layout: default
title: Magnesium Salicylate
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 9
monitor_inn: "MAGNESIUM SALICYLATE"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "ankylosing spondylitis", "myosclerosis", "brachydactyly-syndactyly syndrome", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
last_modified_at: 2026-10-30
description: "Magnesium Salicylate: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not stated in the US licence text."
---

# Magnesium Salicylate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Magnesium Salicylate: From Joint and Inflammatory Pain Conditions to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Magnesium salicylate is a salicylate-type pain reliever and anti-inflammatory agent. The TxGNN model's top-ranked prediction is **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** support it, so it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US licence text. The knowledge graph records bursitis, synovitis, tenosynovitis, rheumatoid arthritis, headache disorder, osteoarthritis and arthropathy (relations recorded in the knowledge graph, not approved indications). |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of FDA Applications | 3 (valid: 3) |
| Number of approvals | 3 licences (single-ingredient products) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Magnesium salicylate is generally understood as a non-selective COX inhibitor of the NSAID type, which reduces prostaglandin-driven pain and inflammation.

The predicted disease is a rare genetic skeletal dysplasia caused by loss of function in the CDMP1/GDF5 gene, which affects bone growth. The drug does not act on the GDF5/BMP signalling pathway, and anti-inflammatory COX inhibition would not correct a developmental bone defect. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. **No credible mechanistic link was identified.**

For context, the other top predictions are also weak:
- **Ankylosing spondylitis** (score 0.9996) is the only one with a plausible rationale. NSAIDs are first-line symptomatic therapy for it, and the drug's related joint indications support class-level plausibility. However, no drug-specific studies are available, non-acetylated salicylates are generally weaker anti-inflammatory agents than other NSAIDs, and this would be more a class-level label extension than true repurposing.
- **Pseudoachondroplasia** and **hypermobility of coccyx** might at most gain symptomatic pain relief.
- Other predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia-amelogenesis imperfecta syndrome, brachydactyly-syndactyly syndrome, brachyolmia, myosclerosis) are developmental or structural disorders with no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M013 | Percogesic | Tablet, coated | Not stated in the data compiled |
| part343 | Doans | Tablet | Not stated in the data compiled |
| M027 | Diurex | Tablet, coated | Not stated in the data compiled |

All three are valid single-ingredient products. Oral dosage forms recorded include coated tablets, coated capsules, film-coated tablets and tablets.

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

The knowledge graph records the following contraindication relations (these are not label text and should be verified against the package insert):
- **Cardiovascular:** hypertension, heart disease, cardiovascular disease, heart conduction disease, sudden cardiac arrest
- **Liver and kidney:** liver disease, liver failure, kidney disease, impaired renal function
- **Gastrointestinal:** peptic ulcer disease, gastritis, gallbladder disease
- **Blood and clotting:** thrombocytopenia, blood coagulation disease, hemophilia, anemia (including macrocytic anemia)
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, gout
- **Eye:** angle-closure glaucoma, closed-angle glaucoma, ocular hypertension
- **Other:** epilepsy, insomnia, benign prostatic hyperplasia, substance abuse/dependence, paracetamol poisoning, pyoureter

No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted disease is a congenital skeletal dysplasia with no plausible link to COX inhibition. No trials or publications support it, so the evidence is model prediction only (L5). The 0.9996 score should not be read as clinical support.

**To proceed, the following is needed:**
- Mechanism of action data for magnesium salicylate
- The FDA package insert warnings and contraindications, which are currently missing and block safety screening
- If any repurposing direction is pursued, consider evaluating ankylosing spondylitis instead, supported by a systematic literature search and class-level NSAID evidence
- Any trial or literature that directly studies the predicted disease, before the evidence level can be raised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

