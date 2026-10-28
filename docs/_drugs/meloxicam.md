---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 895
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Meloxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Meloxicam: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID originally used for rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of NDAs | 8 (all cancelled; all are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, meloxicam is a COX-2-preferential NSAID that reduces inflammation and pain. Its efficacy in arthritis conditions is established.

For this prediction, however, no mechanistic link is established. Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function variants in CDMP1/GDF5, a developmental bone-growth defect. Meloxicam would not be expected to correct this genetic defect. The very high TxGNN score most likely reflects a TxGNN model (deep learning) artifact, in which a shared musculoskeletal phenotype with arthropathy places the two close together, rather than real biological plausibility.

**Other top-ranked predictions** were also reviewed:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9992 | L5 | No credible mechanistic link; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 3 | Myosclerosis | 0.9990 | L5 | Weak and speculative; possible symptomatic relief only, no evidence on fibrosis |
| 4 | Brachyolmia | 0.9989 | L5 | No credible mechanistic link |
| 5 | Pseudoachondroplasia | 0.9981 | L5 | Indirect; NSAIDs are generic supportive care for joint pain |
| 7 | Rheumatoid nodulosis | 0.9951 | L5 | Indirect; possible joint-pain benefit, no evidence on nodules |
| 9 | WHIM syndrome | 0.9938 | L5 | No mechanistic link (CXCR4 gain-of-function disease) |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9936 | L5 | No credible mechanistic link; likely artifact |

Rank 8 (RF-positive polyarticular juvenile idiopathic arthritis) is the only prediction with a plausible link and any supporting publication. It is also closely related to meloxicam's existing use in juvenile arthritis, so it is not a distinct repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For the rank 8 prediction, one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort/safety study (inferred from title) | Pediatric Rheumatology Online Journal | Phase 4 registry on the long-term safety and development of children with juvenile idiopathic arthritis treated with celecoxib or nonselective NSAIDs; indirect for meloxicam and supports safety rather than efficacy |

## US Market Information

All 8 US authorizations are generic tablets and are currently cancelled. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077920 | Meloxicam (AiPing Pharmaceutical) | Tablet | Not available (valid) |
| ANDA077927 | Meloxicam (RemedyRepack) | Tablet | Not available (valid) |
| ANDA077918 | Meloxicam (Aphena Pharma Solutions) | Tablet | Not available (valid) |
| ANDA217579 | Meloxicam (XLCare Pharmaceuticals) | Tablet | Not available (valid) |
| ANDA077929 | Meloxicam (Northwind Health) | Tablet | Not available (valid) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Disease-level contraindication signals (knowledge graph, not label text)**: hypertension, congestive heart failure, myocardial infarction and other cardiovascular disease, stroke and cerebrovascular disorders, kidney disease and impaired renal function, active peptic ulcer disease, gastritis, blood coagulation disease, anaemia, diabetes mellitus and diabetic ketoacidosis, hyperlipidaemia, and substance abuse/dependence. These are consistent with the known cardiovascular, gastrointestinal and renal risks of NSAIDs but should be confirmed against the label.
- **Drug Interactions**: 100 interactions were identified. The sample reviewed was mostly Moderate, with one Minor (linaclotide). Examples of Moderate interactions include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Acetylsalicylic acid
  - Mesalazine and balsalazide
  - Metformin, glimepiride and chlorpropamide
  - Aprepitant
  - Vancomycin and kanamycin
  - Potassium citrate and potassium bicarbonate
  - Bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials or literature and no plausible mechanism. Its high score appears to be a TxGNN model (deep learning) artifact. All nine other top predictions are also at L4-L5, and the most plausible ones largely overlap with meloxicam's existing indications. The cancelled US license status and missing label safety data further limit progress.

**To proceed, the following is needed:**
- Mechanism-of-action data for meloxicam, to support any mechanistic-link analysis
- FDA package insert warnings and contraindications, to allow safety screening
- A biological rationale connecting COX inhibition to GDF5-related skeletal development, or reprioritization toward predictions with real support (for example, rank 8, RF-positive polyarticular JIA)
- Meloxicam-specific efficacy data for any selected indication
- Clarification of the cancelled US market status and the current availability of the drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

