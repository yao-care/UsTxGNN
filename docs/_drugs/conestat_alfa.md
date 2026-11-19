---
layout: default
title: Conestat Alfa
parent: Model Prediction Only (L5)
nav_order: 549
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-20
monitor_inn: "CONESTAT ALFA"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "fetal and neonatal alloimmune thrombocytopenia"]
description: "Conestat Alfa: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Conestat Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Conestat Alfa: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Conestat alfa is a recombinant C1 esterase inhibitor (a serine protease inhibitor of the serpin family) marketed in the United States as an injectable biologic.
The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, but **no clinical trials and no publications** were found for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of conestat alfa as: Plasma protease C1 inhibitor exogenous protein ([ChEMBL CHEMBL2108350 (conestat alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2108350), CC BY-SA 3.0; accessed 2026-11-19.) Based on its known identity, conestat alfa is a recombinant C1 inhibitor, which is itself a member of the serpin family. This shared serpin-family annotation is the most likely reason the model gives a high score.

The mechanistic fit, however, is weak. Toxic polymerization serpinopathies arise from intracellular misfolding and accumulation of mutant serpin proteins. Supplying functional serpin from outside the cell is unlikely to correct that intracellular problem. The high score should therefore be read as a signal of annotation similarity, not as evidence of likely benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125495 | Ruconest (Pharming Healthcare Inc.) | Injection, powder, for solution | Not recorded in the local data |

## Safety Considerations

**Drug Interactions:** 41 interactions are recorded in total. Most are of Moderate level. The one Major interaction in the listed records is with:
- Carfilzomib (Major)

Moderate-level interactions listed include:
- Androgens and anabolic steroids: oxandrolone, oxymetholone, stanozolol, testosterone, danazol, prasterone enantate
- Estrogens: ethinylestradiol, estradiol (including topical), conjugated estrogens (including topical), esterified estrogens, dienestrol (topical), diethylstilbestrol
- Drospirenone
- Fibrinolytics: alteplase, anistreplase
- Erythropoiesis-stimulating agents: darbepoetin alfa, erythropoietin

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5). The proposed mechanism is also implausible, since extracellular serpin replacement is unlikely to fix intracellular polymer formation. The high score most likely reflects serpin-family annotation.

**To proceed, the following is needed:**
- Preclinical evidence showing that exogenous C1 inhibitor can affect serpin polymerization or its toxic effects
- Detailed mechanism-of-action data for conestat alfa
- Package insert warnings and contraindications for a safety review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for conestat alfa is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL2108350 (conestat alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2108350) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

