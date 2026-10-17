---
layout: default
title: Oxaprozin
parent: Model Prediction Only (L5)
nav_order: 1000
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oxaprozin: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "OXAPROZIN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Oxaprozin
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

# Oxaprozin: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Oxaprozin is a non-steroidal anti-inflammatory drug (NSAID) originally used for joint diseases such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled; 4 ANDAs and 1 NDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxaprozin is an NSAID that inhibits cyclooxygenase (COX), reducing prostaglandin-mediated inflammation and pain. Its efficacy in arthritic conditions is established.

Hunter-Thompson type acromesomelic dysplasia is a rare skeletal disorder caused by loss-of-function variants in the CDMP1/GDF5 gene, which disrupt cartilage and bone development. No plausible mechanism links COX inhibition to correcting GDF5 signaling defects. The high score most likely reflects the disease's closeness to arthritis and joint-disorder nodes in the knowledge graph rather than a true biological relationship.

Other top-ranked predictions are also mostly rare skeletal or developmental syndromes (for example brachyolmia, pseudoachondroplasia and brachydactyly-syndactyly syndrome) and share the same weakness. The most biologically plausible candidates are the following, though they largely overlap with existing indications and are not true repurposing:
- **Spondyloarthropathy, susceptibility to** (score 99.93%): NSAIDs are first-line symptomatic therapy.
- **Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis** (score 99.67%): NSAIDs are used for symptom control in juvenile arthritis.
- **Rheumatoid nodulosis** (score 99.73%): related to rheumatoid arthritis, but NSAIDs are not known to treat nodules.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA208633 | Oxaprozin (Bryant Ranch Prepack) | Tablet | Not available (cancelled) |
| ANDA075845 | Oxaprozin (St. Mary's Medical Park Pharmacy) | Tablet | Not available (cancelled) |
| ANDA075855 | Oxaprozin (Bryant Ranch Prepack) | Tablet, film coated | Not available (cancelled) |
| NDA217927 | Oxaprozin (Ayurax, LLC) | Capsule | Not available (cancelled) |
| ANDA075987 | Oxaprozin (Chartwell RX, LLC) | Tablet | Not available (cancelled) |

All listed products are oral formulations and all five authorizations are cancelled.

## Safety Considerations

- **Disease-related cautions (from knowledge graph contraindication links, not label text)**: hypertension and hypertensive disorders, liver failure, kidney disease, peptic ulcer disease (including active ulcer), blood coagulation disorders, myocardial infarction and coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, and pyoureter. These are consistent with the known cardiovascular, gastrointestinal, renal and bleeding risks of NSAIDs.
- **Drug Interactions**: The interaction screen returned 100 entries in total; the 20 reviewed here include the following.
  - Moderate: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, mesalazine and balsalazide, metformin and sulfonylureas (chlorpropamide, acetohexamide), exenatide, potassium citrate, bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes), and fenfluramine and dexfenfluramine.
  - Minor: H2 blockers (famotidine, ranitidine, cimetidine).

Official label warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acromesomelic dysplasia, Hunter-Thompson type has no supporting trials or literature, and no biological mechanism links COX inhibition to the GDF5 defect that causes the disease. In addition, none of oxaprozin's US licenses is currently valid, and NSAID safety concerns (cardiovascular, gastrointestinal, renal) would need careful weighing in any new population.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Official package insert warnings and contraindications
- Preclinical or mechanistic evidence connecting oxaprozin to GDF5/CDMP1 signalling or cartilage biology
- A literature and trial search specific to the predicted disease
- Consideration of the more plausible candidates (spondyloarthropathy, polyarticular juvenile idiopathic arthritis), after checking them against labeled uses to determine whether they are genuinely new indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

