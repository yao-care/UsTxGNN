---
layout: default
title: Salsalate
parent: Model Prediction Only (L5)
nav_order: 1144
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "SALSALATE"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia"]
description: "Salsalate: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Salsalate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Salsalate: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Salsalate is an oral salicylate anti-inflammatory drug, originally used for rheumatoid arthritis, osteoarthritis and other joint conditions.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, salsalate is a salicylate prodrug with NF-κB inhibitory and AMPK-activating activity. Its efficacy in joint inflammation and pain is the basis of its original indications.

Hunter-Thompson type acromesomelic dysplasia is a rare skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5, which disrupt BMP signaling and cartilage formation. No plausible mechanistic link between salsalate and GDF5/BMP signaling has been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction should be regarded as a hypothesis only.

Other predictions for this drug were also reviewed. All are L5 and rated Hold. One of them is pseudoachondroplasia (0.9978), where salsalate might relieve secondary joint pain, though it would not address the underlying disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Salsalate (Amneal Pharmaceuticals LLC) | Tablet (oral) | Not available |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationships in the graph, not from label text): liver failure, liver disease, kidney disease, gallbladder disease, active peptic ulcer disease, gastritis, gastroesophageal reflux disease, esophagitis, blood coagulation disorders (including hemophilia, congenital prothrombin deficiency, vitamin K deficiency hemorrhagic disease), thrombocytopenic purpura, anemia, cardiovascular and heart disease, diabetes mellitus and diabetic ketoacidosis, thyroid overactivity (hyperthyroidism, Graves disease, thyrotoxicosis), and nasal polyps.
- **Drug Interactions**: The data compiled for this report show 100 recorded interactions, and 20 are listed. Most are Moderate:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - Other salicylate and aminosalicylate drugs: mesalazine, balsalazide
  - Blood glucose-lowering drugs: chlorpropamide, glimepiride, repaglinide, insulin aspart, insulin degludec, insulin detemir
  - Bowel preparations and alkalinizing agents: potassium citrate, picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes
  - Minor interactions: proton pump inhibitors (rabeprazole, dexlansoprazole, omeprazole)

Please refer to the package insert for official warnings and contraindications, because label data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, with no clinical trials or literature. It has no plausible mechanistic link to the underlying genetic defect. Salsalate is also cancelled-only in the US market, so there is no marketed product to build on.

**To proceed, the following is needed:**
- A targeted literature and trial search for each predicted indication, especially spondyloarthropathy, where NSAID-class evidence could support an upgrade to L4
- Detailed mechanism of action data
- FDA package insert warnings and contraindications for safety screening
- Confirmation of the regulatory and supply situation, given the cancelled US license
- Route and formulation compatibility assessment for any candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

