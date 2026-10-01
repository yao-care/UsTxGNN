---
layout: default
title: Asfotase Alfa
parent: Model Prediction Only (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase Alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies

## One-Sentence Summary

Asfotase alfa is a bone-targeted recombinant enzyme, marketed in the US as STRENSIQ, and used for hypophosphatasia (the Evidence Pack lists no indication text, so this comes from general knowledge).
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The high score is a graph-based prediction only, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypophosphatasia (not listed in the Evidence Pack; based on general knowledge) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records (all under BLA125513) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Asfotase alfa is a recombinant tissue-nonspecific alkaline phosphatase with a bone-targeting domain. It hydrolyzes inorganic pyrophosphate and pyridoxal-5'-phosphate, which supports bone mineralization in hypophosphatasia.

The predicted indication is a disorder of nuclear-encoded respiratory chain components and OXPHOS assembly. Asfotase alfa does not act on these pathways, so **no plausible mechanistic link was identified**. The score of 0.9995 most likely reflects knowledge-graph topology, not biology.

The other nine predictions in the top 10 are also weak, and all are L5 with a Hold recommendation:
- **Steel syndrome:** a collagen matrix defect, unrelated to pyrophosphate-mediated mineralization.
- **Exocrine pancreatic insufficiency:** requires digestive enzymes delivered to the gut lumen, whereas asfotase alfa is given systemically.
- **Scheie syndrome, Hurler syndrome, lysosomal storage disease with skeletal involvement:** the overlap is limited to the enzyme-replacement modality and skeletal involvement, and asfotase alfa does not supply the missing lysosomal enzymes.
- **Familial apolipoprotein C-II deficiency:** no role in lipid metabolism; likely a graph artifact.
- **Esophageal varices with and without bleeding:** identical scores suggest a duplicate signal, and there is no vascular mechanism.
- **Cystinosis:** no effect on cystine transport or clearance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125513 | STRENSIQ | Solution | Alexion Pharmaceuticals, Inc. |

The Evidence Pack contains four identical records for this authorization, shown here once. Approved indication text was not supplied.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link, so it rests on the model score alone (evidence level L5). Asfotase alfa's mechanism (pyrophosphate and PLP hydrolysis for bone mineralization) does not intersect with mitochondrial OXPHOS pathways.

**To proceed, the following is needed:**
- Mechanistic or preclinical data (for example, cell or animal models) showing any effect on mitochondrial function
- Package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism of action data from DrugBank
- Approved indication text for the US licenses
- Route and dosing compatibility assessment, currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

