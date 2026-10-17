---
layout: default
title: Magnesium Salicylate
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Magnesium Salicylate: predicted new indication Spondyloarthropathy, susceptibility to (evidence level L5). Approved use: Bursitis, synovitis, tenosynovitis, rheumatoid arthritis…"
monitor_inn: "MAGNESIUM SALICYLATE"
predicted_indications: ["spondyloarthropathy, susceptibility to", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachydactyly-syndactyly syndrome", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
---

# Magnesium Salicylate
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

# Magnesium Salicylate: From Arthropathy and Pain Conditions to Spondyloarthropathy (Susceptibility)

## One-Sentence Summary

Magnesium salicylate is a salicylate-class anti-inflammatory and analgesic, originally used for joint and musculoskeletal conditions such as rheumatoid arthritis, osteoarthritis, bursitis and headache disorders.
The TxGNN model predicts it may be effective for **spondyloarthropathy, susceptibility to**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, synovitis, tenosynovitis, rheumatoid arthritis, headache disorder, osteoarthritis, arthropathy (from the knowledge-graph indication list; no approved indication text on the US licenses) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketing) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium salicylate is a non-selective COX-inhibiting salicylate (NSAID class) with anti-inflammatory activity. Its use in inflammatory joint conditions is established, and mechanistically it may be applicable to inflammatory spondyloarthropathies, where NSAIDs are first-line symptomatic therapy.

Important caveats:
- "Spondyloarthropathy, susceptibility to" is a genetic susceptibility category rather than a treatable clinical entity. The very high score most likely reflects proximity in the knowledge graph to the drug's existing arthropathy indications.
- The link is inferred only from drug class and the model prediction. No drug-specific trial or literature evidence was compiled.
- Of the other top-10 predictions, **ankylosing spondylitis** (score 99.96%) is biologically the most plausible. NSAIDs are guideline-recommended first-line therapy, but salicylates are generally considered less effective than other NSAIDs (e.g., naproxen, celecoxib) for axial spondyloarthritis, so any added value would be incremental. Most of the remaining predictions (rare skeletal dysplasias and malformation syndromes such as acromesomelic dysplasia, brachyolmia and brachydactyly-syndactyly syndrome) have no plausible mechanistic link and look like graph artifacts. Pseudoachondroplasia and hypermobility of coccyx offer only indirect, symptomatic pain-relief rationales.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| M013 | Percogesic | Coated tablet | Not specified | Cancelled |
| part343 | Doans | Tablet | Not specified | Cancelled |
| M027 | Diurex | Coated tablet | Not specified | Cancelled |

All three authorizations are single-ingredient products and have been cancelled, so there is currently no actively marketed US product.

## Safety Considerations

No label-based warnings, contraindications or drug-interaction data were available for this report. Please refer to the package insert for safety information.

Knowledge-graph contraindication associations (not label text) flag the following disease areas for caution:
- **Hepatic and renal:** liver failure, liver disease, kidney disease, impaired renal function
- **Gastrointestinal:** peptic ulcer disease, gastritis, gallbladder disease
- **Bleeding and blood:** thrombocytopenia, blood coagulation disease, hemophilia, anemia (including macrocytic anemia)
- **Cardiovascular:** hypertension, hypertensive disorder, cardiovascular disease, heart disease, sudden cardiac arrest, heart conduction disease
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, gout
- **Eye:** angle-closure glaucoma, closed-angle glaucoma, ocular hypertension
- **Other:** epilepsy, insomnia, benign prostatic hyperplasia, pyoureter, substance abuse/dependence, paracetamol poisoning

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and a class-based rationale (L5). The predicted indication is a genetic susceptibility category rather than a clinical disease, no trials or literature were found, other NSAIDs have much stronger evidence in spondyloarthritis, and all US licenses are cancelled. Ankylosing spondylitis could be kept as a research question, but it does not justify advancing development at this stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic literature search for salicylates in ankylosing spondylitis and axial spondyloarthritis
- A comparison against standard NSAIDs and a commercial-viability assessment given the cancelled market status
- Route and formulation compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

