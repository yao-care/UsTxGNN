---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "FLURBIPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
---

# Flurbiprofen
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

# Flurbiprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a nonsteroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and related joint disorders.
The TxGNN model's top-ranked prediction is **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This prediction has **no supporting clinical trials and no publications**, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from knowledge-graph indication data; the US authorization records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active authorizations) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, flurbiprofen is a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory and degenerative joint disease is well established.

The predicted indication is a different kind of disease. Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal disorder linked to the CDMP1/GDF5 pathway. It is a developmental defect, not a COX-dependent inflammatory condition. There is no recognized mechanistic reason for an NSAID to alter its course.

The high score most likely reflects proximity in the knowledge graph between this drug and skeletal or joint-related phenotypes, not a pharmacological rationale. The prediction should be treated as a computational signal, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074447 | Flurbiprofen Sodium | Solution/drops | Not listed (cancelled) |
| ANDA074431 | Flurbiprofen | Tablet | Not listed (cancelled) |
| Not available | Rinol-STroche | Troche | Not listed (cancelled) |

All three authorizations are cancelled, so no active US product is currently on the market.

## Safety Considerations

- **Contraindication signals (knowledge-graph associations, not label text):** hypertension and hypertensive disorders, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, pyoureter, and substance abuse/dependence.
- **Drug Interactions:** The data compiled for this report records 100 interactions. The first 20 reviewed are mostly Moderate, with a few Minor.
  - **Moderate:** acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, aprepitant, potassium citrate, potassium bicarbonate, picosulfuric acid, sodium sulfate, and polyethylene glycol with electrolytes.
  - **Minor:** famotidine, cimetidine, linaclotide.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only a model score behind it, with no trials, no literature and no plausible NSAID mechanism for a genetic skeletal developmental disorder. All US authorizations are also cancelled, which further limits practical development.

**Other findings from the data:**
The lower-ranked prediction **ankylosing spondylitis** (rank 8, score 99.97%) has about 20 publications. These are mostly 1974-1986 double-blind comparisons of flurbiprofen against indomethacin, phenylbutazone and naproxen, which found comparable pain relief. This is Evidence Level L3 pending verification of study design. However, it is a symptomatic use within the NSAID class and overlaps with the drug's original rheumatic indications, so it is an expansion within the same therapeutic area and not a novel repurposing.

**To proceed, the following is needed:**
- Obtain the FDA package insert to verify warnings and contraindications. This is required before any safety screening.
- Obtain mechanism of action data from DrugBank.
- Confirm the study designs (randomization, blinding) of the ankylosing spondylitis comparisons if that indication is pursued instead.
- Identify any preclinical rationale linking COX inhibition to the predicted skeletal dysplasia before further investment.
- Reassess regulatory and commercial feasibility given the cancelled-only market status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

