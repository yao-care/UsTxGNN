---
layout: default
title: Sodium Acetate
parent: Model Prediction Only (L5)
nav_order: 1167
evidence_level: L5
indication_count: 10
---

# Sodium Acetate
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

# Sodium Acetate: From an Electrolyte/Alkalinizing Agent to Congenital Prothrombin Deficiency

## One-Sentence Summary

Sodium acetate is an electrolyte and alkalinizing agent, and a source of sodium. It is also used as an excipient or buffer in many other products.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The high score appears to be a graph-based artifact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is available in the US licence records |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 12 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, sodium acetate is an electrolyte source. Acetate is metabolised to bicarbonate, giving it an alkalinizing effect.

Congenital prothrombin deficiency is a monogenic coagulation disorder (F2 gene) that is treated by replacing the missing clotting factor. No plausible mechanistic link between sodium acetate and prothrombin function was identified. The high TxGNN score is most likely a knowledge-graph artifact and is not supported by clinical or literature evidence.

The other top-ranked predictions are similarly weak, including epiglottitis, urinary tract infection, sclerosing cholangitis, Ureaplasma and gonococcal urethritis, dyspepsia, uterine inflammatory disease, gastroparesis and xanthogranulomatous pyelonephritis. Most are infections treated with antibiotics, which sodium acetate does not provide. The only speculative link is for urinary tract infection, where urine alkalinization could change urine pH. This is not an established therapy and may even favour some pathogens.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

Literature retrieved for lower-ranked predictions does not support a therapeutic role either. For dyspepsia and gastroparesis, the papers use acetate (e.g., the ¹³C-sodium acetate breath test) only as a diagnostic tracer for gastric emptying. They evaluate other agents (nizatidine, rikkunshi-to, maropitant) or are physiology studies, and none test sodium acetate as a treatment.

## US Market Information

All 12 US licences are cancelled and none has approved indication text. The products below are those in the compiled data, and many contain sodium acetate as a component or excipient rather than as the active ingredient.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204890 | Pemetrexed | Lyophilized powder for injection | Not specified |
| ANDA211899 | Pemetrexed | Lyophilized powder for injection | Not specified |
| NDA209387 | NIPRIDE RTU | Injection, solution | Not specified |
| ANDA204071 | Sodium Polystyrene Sulfonate | Powder for suspension | Not specified |
| ANDA087859 | Sodium Polystyrene Sulfonate | Suspension | Not specified |

## Safety Considerations

- **Drug Interactions**: 30 interactions were recorded. Those listed include the following:
  - Moderate: doxycycline, tetracycline, minocycline, acetylsalicylic acid, choline salicylate, ephedrine, pseudoephedrine, amphetamine, dextroamphetamine, benzphetamine, methenamine
  - Minor: chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide, memantine, methotrexate
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text):
  - Kidney disease: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
  - Cardiac: heart disease, cardiovascular disease, atrioventricular block, ventricular fibrillation, digitalis poisoning
  - Metabolic: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease, hypoaldosteronism, phenylketonuria and other disorders of phenylalanine metabolism
  - Neuromuscular: hyperkalemic periodic paralysis, periodic paralysis, myotonia congenita

Please refer to the package insert for label-based warnings and contraindications, as these were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or supporting literature and no plausible mechanistic link to prothrombin deficiency. Standard treatment is factor replacement, and the market status is cancelled only.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence linking acetate to coagulation
- Route compatibility and similarity-to-original-indication analyses
- A review of whether a higher-priority candidate indication should be pursued instead, since none of the top 10 predictions has supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

