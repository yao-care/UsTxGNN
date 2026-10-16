---
layout: default
title: Benznidazole
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 3
monitor_inn: "BENZNIDAZOLE"
predicted_indications: ["congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Benznidazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Benznidazole: From Chagas Disease to Congenital Analbuminemia

## One-Sentence Summary

Benznidazole is an oral nitroimidazole antiparasitic originally used to treat Chagas disease.
The TxGNN model predicts it may be effective for **congenital analbuminemia**,
but currently **0 clinical trials** and **0 publications** support this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chagas disease |
| Predicted New Indication | Congenital analbuminemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, benznidazole is a nitroimidazole antiparasitic prodrug that is activated by parasite nitroreductases, and its efficacy in Chagas disease is established.

No plausible mechanistic link to congenital analbuminemia could be established. This is a rare autosomal recessive disorder caused by mutations in the albumin (*ALB*) gene, resulting in absent or very low serum albumin. Benznidazole's antiparasitic mechanism has no evident connection to this process. The high TxGNN score is a knowledge-graph prediction only, and no clinical or literature evidence supports it.

The other two predictions in the data (polyclonal hyperviscosity syndrome, 99.32%; hyperamylasemia, 99.32%) are likewise without a mechanistic link or any supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209570 | Benznidazole (Exeltis USA, Inc.) | Tablet | Not stated; license status: cancelled |

## Cytotoxicity

Benznidazole is not classified as an antineoplastic drug, so no cytotoxicity assessment is provided.

## Safety Considerations

- **Drug Interactions**: 94 drug-drug interactions are recorded. Among the 20 listed in the compiled data, one is rated **Major** and the rest **Moderate**.
  - **Major**: Ethanol (a disulfiram-like reaction is a known concern with nitroimidazoles).
  - **Moderate (examples)**: Metronidazole, tinidazole, statins (atorvastatin, rosuvastatin, simvastatin), amiodarone, levodopa, paclitaxel, cabazitaxel, carboplatin, bortezomib, carfilzomib, brentuximab vedotin, trastuzumab emtansine, adalimumab, auranofin, picosulfuric acid, iodide I-123 and I-131.
- Benznidazole is known to cause hypersensitivity dermatitis, gastrointestinal effects, and neuropathy, but the compiled data contain no label-based warnings or contraindications. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanistic link to congenital analbuminemia. The only US license is cancelled, so the practical path to development is also unclear.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for benznidazole
- Preclinical or mechanistic evidence connecting benznidazole to albumin biology
- A review of the clinical rationale for each predicted indication, given that albumin deficiency is a genetic disorder not expected to respond to an antiparasitic
- Clarification of regulatory and supply status given the cancelled US license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

