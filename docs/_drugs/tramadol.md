---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 1246
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Osteoarthritis (also osteoarthritis susceptibility and arthropathy)"
monitor_inn: "TRAMADOL"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
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

## Tramadol: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Tramadol is an opioid-type analgesic, originally associated with osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**,
but **no clinical trials** and **no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis (also osteoarthritis susceptibility and arthropathy) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of FDA Applications | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, tramadol is a mu-opioid receptor agonist that also inhibits serotonin and norepinephrine reuptake, which gives it symptomatic pain-relieving effects.

The predicted disease is a rare genetic skeletal dysplasia caused by a defect in the CDMP1/GDF5 pathway that affects bone growth. Tramadol does not address this underlying pathology. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, tramadol could offer symptomatic analgesia.

Other top-ranked predictions show the same pattern: rare skeletal dysplasias (brachyolmia, pseudoachondroplasia), juvenile arthritis subtypes and related connective-tissue conditions. None has a credible disease-modifying link to tramadol.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only publication found among the top 10 predictions (for juvenile idiopathic arthritis, rank 7) is a review of ketoprofen in children ([20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/), 2010, *Paediatric Drugs*). It concerns a different drug and provides no direct evidence for tramadol.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022370 | ConZip | Capsule, extended release | Not available |
| ANDA200503 | Tramadol Hydrochloride | Tablet, extended release | Not available |
| ANDA208708 | Tramadol Hydrochloride | Tablet, coated | Not available |
| ANDA076003 | Tramadol Hydrochloride | Tablet, coated | Not available |
| ANDA075968 | Tramadol Hydrochloride | Tablet | Not available |

All 10 authorizations are listed as valid; the five main ones are shown above.

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text)**: hypertension, liver failure, liver disease, cirrhosis, epilepsy, anxiety disorder, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, substance withdrawal syndrome, alcohol withdrawal, respiratory failure, paracetamol poisoning, serotonin syndrome, intracranial hypertension, pseudotumor cerebri, hyperlipidemia, gallbladder disease, Wernicke-Korsakoff syndrome and central nervous system infections.
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Examples of **Major** interactions include alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine and fenfluramine. **Moderate** interactions include atropine, bisacodyl, cimetidine, clarithromycin, famotidine and eliglustat.
- **Pediatric caution**: Pediatric opioid safety concerns and regulatory restrictions on tramadol in children are relevant to the juvenile arthritis predictions.

Please refer to the package insert for the full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no credible mechanistic link. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Tramadol would at best provide symptomatic pain relief, not treatment of the underlying genetic disorder. Its 10 US authorizations are also all valid.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Any clinical or preclinical evidence linking tramadol to the predicted disease
- A reconsideration of the target: symptomatic pain management in conditions with a plausible analgesic need (e.g., pseudoachondroplasia-related joint pain) may be more realistic than disease modification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

