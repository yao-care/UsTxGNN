---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
monitor_inn: "KETOPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
last_modified_at: 2026-10-14
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
---

# Ketoprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ketoprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a nonsteroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis, and other arthropathies.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The high score appears to reflect proximity in the knowledge graph rather than a pharmacological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled; these are ANDA records) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoprofen is a cyclooxygenase (COX) inhibitor of the NSAID class with analgesic and anti-inflammatory activity. Its efficacy in arthritic conditions is established.

For the top prediction, however, **no credible mechanistic link was identified**. Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia caused by loss-of-function variants in CDMP1/GDF5, which affects bone growth. Ketoprofen has no known effect on GDF5/BMP signaling. The high TxGNN score most likely reflects knowledge-graph proximity to skeletal or arthropathy phenotypes rather than a pharmacological rationale.

Other top-ranked predictions are mostly skeletal or developmental genetic disorders (e.g., brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome) and show the same pattern. Only a few have an indirect, symptom-level rationale:
- **Spondyloarthropathy, susceptibility to** (rank 8): NSAIDs are first-line symptomatic therapy for spondyloarthritis, but no ketoprofen-specific evidence was found.
- **Juvenile arthritis due to LACC1 defect** (rank 10): NSAIDs may relieve symptoms, but they do not address the underlying autoinflammatory defect.
- **Pseudoachondroplasia** (rank 7): NSAIDs could provide supportive pain relief for secondary joint degeneration, not disease modification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074014 (cancelled) | Orudis (Allegis Pharmaceuticals, Inc.) | Capsule | Not available |
| ANDA075679 (cancelled) | Ketoprofen (Mylan Pharmaceuticals Inc.) | Extended-release capsule | Not available |

Both products are oral formulations, and neither has a currently valid license.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Ketoprofen is linked to contraindication or caution signals in the following conditions:
  - Cardiovascular: hypertension and hypertensive disorder, myocardial infarction, coronary thrombosis, heart disease, cardiovascular disease
  - Gastrointestinal: peptic ulcer disease, active peptic ulcer disease
  - Organ function: liver failure, kidney disease, pyoureter
  - Haematological: blood coagulation disease, hemoglobinopathy
- **Drug Interactions**: The interaction screening returned 100 records; 20 are shown in the data compiled for this report.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aspirin (acetylsalicylic acid), metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine and balsalazide, naltrexone, potassium citrate and potassium bicarbonate, picosulfuric acid, and polyethylene glycol (3350 with electrolytes)
  - **Minor**: H2 blockers (famotidine, ranitidine, cimetidine) and linaclotide

Please refer to the package insert for the complete label warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, no literature, and no credible mechanistic link (Evidence Level L5). Ketoprofen has no known effect on the GDF5 pathway underlying this disease. In addition, it has no currently valid US license, and its label safety data are incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (required before any safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical or mechanistic evidence for a link between COX inhibition and GDF5/BMP signaling or the disease phenotype
- If a repurposing direction is pursued, consider the lower-ranked, mechanistically more plausible symptom-management candidates (spondyloarthropathy, juvenile arthritis) as research questions, supported by a literature and trial search for ketoprofen or NSAID-class evidence
- A review of regulatory and commercial feasibility, given that all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

