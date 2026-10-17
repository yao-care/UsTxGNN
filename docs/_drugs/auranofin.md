---
layout: default
title: Auranofin
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 2
monitor_inn: "AURANOFIN"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-10-14
description: "Auranofin: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Auranofin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is an oral gold-based compound originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, an ultra-rare developmental disorder,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, auranofin is a gold-based compound with thiol-reactive and thioredoxin reductase-inhibiting activity. Its efficacy in rheumatoid arthritis rests on anti-inflammatory and immunomodulatory effects.

No plausible mechanistic link to the predicted disease has been established. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an ultra-rare developmental malformation syndrome, and no known pathway connects auranofin pharmacology to its pathogenesis. The high TxGNN score is a computational output, not clinical or experimental evidence, and may reflect network proximity artifacts in the knowledge graph.

The second-ranked prediction, **brachydactyly-syndactyly syndrome** (score 99.24%), has the same limitations. It is a congenital limb malformation typically driven by developmental gene variants. Postnatal drug treatment is unlikely to reverse structural anomalies, so it should be treated as hypothesis-generating only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018689 (cancelled) | Auranofin (Coral Way Pharma, LLC) | Capsule (oral) | Not listed in the data compiled for this report |

## Cytotoxicity

Auranofin is not classified as a conventional antineoplastic drug in the data compiled for this report, so this section is omitted.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): hypertensive disorder, kidney disease, liver disease, hepatitis, gallbladder disease, hematologic disease, thrombocytopenia, neutropenia, leukopenia, agranulocytosis, systemic lupus erythematosus, diabetes mellitus, diabetic ketoacidosis, colitis, necrotizing enterocolitis, pulmonary fibrosis, exfoliative dermatitis, exanthem, urticaria, angioedema, atopic eczema, dermatitis, Sjogren syndrome, dry eye syndrome, and others.
- **Drug Interactions**: 86 interactions were identified in total. The main ones listed:
  - **Major**: deferiprone, proguanil, chloroquine
  - **Moderate**: metronidazole, tinidazole, rosuvastatin, simvastatin, benznidazole, disulfiram
  - **Unknown severity**: warfarin, prednisone, prednisolone, proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), ranitidine, misoprostol, clarithromycin, calcitriol, folic acid

Official package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indications are supported only by a computational score, with no clinical trials, no literature, and no plausible mechanism. The drug has no currently valid US authorization, and safety data from the package insert are missing.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- FDA package insert warnings and contraindications, to allow safety screening
- A biologically plausible mechanistic hypothesis linking auranofin to the predicted disease, supported by preclinical or literature evidence
- Evaluation of route compatibility and of the relevance of the predicted rare developmental disorders to postnatal drug treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

