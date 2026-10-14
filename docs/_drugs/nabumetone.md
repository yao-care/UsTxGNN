---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is a nonsteroidal anti-inflammatory drug (NSAID) originally used to treat rheumatoid arthritis, osteoarthritis and other arthropathies.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all ANDA generic applications, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Nabumetone is known to be an NSAID and a prodrug of 6-MNA, a preferential COX-2 inhibitor. Its efficacy in rheumatoid arthritis and osteoarthritis comes from reducing prostaglandin-mediated inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5, which disrupt BMP signaling and cartilage formation. COX inhibition has no known corrective effect on this pathway. The high score most likely reflects proximity in the knowledge graph to skeletal and arthropathy phenotypes, not a biological rationale. At most, an NSAID might relieve secondary joint pain, and no data support even that.

**Other predictions reviewed:** Among the top 10 predictions, the others are also weakly supported. Most are rare genetic or developmental disorders with no mechanistic link (brachyolmia, brachydactyly-syndactyly syndrome, WHIM syndrome and others). Two have class-level indirect support and are marked as research questions (evidence level L4):
- **Spondyloarthropathy, susceptibility to**: NSAIDs are standard first-line symptomatic therapy for spondyloarthritis, but there is no nabumetone-specific evidence.
- **Rheumatoid nodulosis**: related to rheumatoid arthritis, a labeled indication, so joint symptoms might be relieved, but the nodules themselves would not be treated.

Pseudoachondroplasia (rank 7) could involve palliative pain relief for early-onset osteoarthritis, but this is not disease-modifying and is unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078420 | Nabumetone (Proficient Rx LP) | Tablet | Not available (cancelled) |
| ANDA078671 | Nabumetone (Northwind Health Company, LLC) | Film-coated tablet | Not available (cancelled) |
| ANDA091083 | Nabumetone (Proficient Rx LP) | Film-coated tablet | Not available (cancelled) |
| ANDA203166 | Nabumetone 500 mg (LGM Pharma Solutions, LLC) | Film-coated tablet | Not available (cancelled) |

All four authorizations are for oral products and all are cancelled.

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** hypertension and hypertensive disorders, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), substance abuse/dependence, blood coagulation disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, cardiovascular disease and heart disease. These are consistent with the known risks of NSAIDs.
- **Drug Interactions:** The interaction query returned 100 records. Most of those shown are Moderate, and a few are Minor. The main ones are:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide (Moderate)
  - Antidiabetic drugs: metformin, glimepiride, chlorpropamide (Moderate)
  - Aspirin (acetylsalicylic acid) (Moderate)
  - Mesalazine and balsalazide (Moderate)
  - Potassium citrate, potassium bicarbonate, sodium sulfate, picosulfuric acid, polyethylene glycol with electrolytes and vancomycin (Moderate)
  - Ranitidine, cimetidine and linaclotide (Minor)

Please refer to the package insert for the full warnings, as label warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acromesomelic dysplasia, Hunter-Thompson type, has no clinical trials or literature, no plausible mechanism (a BMP/GDF5 signaling defect that COX inhibition does not address), and all US licenses for nabumetone are cancelled. Evidence is model prediction only (L5).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence for any link between COX-2 inhibition and GDF5/BMP signaling or chondrogenesis
- If a symptom-focused route is pursued, shift attention to the L4 candidates (spondyloarthropathy, rheumatoid nodulosis) and look for nabumetone-specific studies
- Route and formulation compatibility assessment and clarification of the cancelled market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

