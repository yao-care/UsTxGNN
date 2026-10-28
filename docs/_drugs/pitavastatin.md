---
layout: default
title: Pitavastatin
parent: Model Prediction Only (L5)
nav_order: 1051
evidence_level: L5
indication_count: 4
monitor_inn: "PITAVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-10-23
description: "Pitavastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Pitavastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Pitavastatin: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Pitavastatin is a statin (HMG-CoA reductase inhibitor) used to lower cholesterol.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, but **no clinical trials and no publications** in the data compiled for this report support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | at least 9 |
| Number of approvals | At least 9 (2 NDAs and 7 ANDAs; the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Pitavastatin is generally known as an HMG-CoA reductase inhibitor that lowers LDL cholesterol.

CETP deficiency is a genetic condition marked by markedly elevated HDL cholesterol and altered lipoprotein metabolism. The prediction most likely reflects closeness within the lipid-metabolism network, not a demonstrated treatment effect. CETP deficiency is a lipid phenotype rather than a condition that clearly needs drug treatment, and no plausible therapeutic rationale is evident. The high score should be read as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The compiled records list 9 authorizations for single-ingredient pitavastatin tablets, all currently valid. The list may be partial, and no approved-indication text was available in the records. The five main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022363 | Livalo | Tablet, film coated | Kowa Pharmaceuticals America, Inc. |
| NDA208379 | ZYPITAMAG | Tablet, film coated | Medicure International Inc |
| ANDA205977 | Pitavastatin calcium | Tablet, film coated | Camber Pharmaceuticals, Inc. |
| ANDA206047 | Pitavastatin calcium | Tablet | Zydus Lifesciences Limited |
| ANDA206070 | Pitavastatin calcium | Tablet, film coated | Mylan Pharmaceuticals Inc. |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links pitavastatin to the following contraindication-type relations: liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, rhabdomyolysis, nodular fasciitis, impaired renal function, and injury.
- **Drug Interactions:** 86 interactions are recorded in total. The one rated Major is **erythromycin**. Moderate interactions include other statins (rosuvastatin, simvastatin), cobicistat, eltrombopag, metronidazole, tinidazole, chloroquine, hydroxychloroquine, disulfiram, naltrexone, eluxadoline, zafirlukast, chloramphenicol, dapsone, and ethanol. Warfarin and dicoumarol are rated Minor.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, so it stays at L5. CETP deficiency is a lipid phenotype with no clear need for treatment, so there is no evident clinical rationale.

**To proceed, the following is needed:**
- Any direct clinical or mechanistic study of pitavastatin in CETP deficiency
- A clear definition of the clinical problem to be treated in this condition
- Detailed mechanism of action data
- Package insert warnings and contraindications, to complete the safety review

**Note on other predictions:** The same drug's second-ranked prediction, HIV infectious disease, has substantially stronger support. The REPRIEVE randomized trial (NEJM 2023, PMID 37486775) showed that pitavastatin reduced major adverse cardiovascular events in people with HIV. This is cardiovascular risk prevention rather than antiviral treatment, and it is better evaluated as a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

