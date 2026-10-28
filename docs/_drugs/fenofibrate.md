---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fenofibrate: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a PPARα agonist marketed in the United States for lipid disorders such as hypertriglyceridemia and hyperlipidemia. The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but the data compiled for this report show **0 clinical trials** and only **3 preclinical or mechanistic publications**, none of which studies the disease directly. This is a model-based prediction with an unclear therapeutic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 16) |
| Number of NDAs | at least 16 |
| Number of approvals | At least 16 (1 NDA and 15 ANDAs); the list may be partial |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the mechanistic link in the compiled data, fenofibrate is a PPARα agonist that raises HDL cholesterol and lowers triglycerides. Part of this effect comes from increased apoA-I and apoA-II expression and from induction of phospholipid transfer protein (PLTP), which enlarges HDL particles.

CETP deficiency is characterized by markedly elevated HDL cholesterol and impaired HDL remodeling. The overlap lies in the HDL metabolism pathway, and this likely explains the high TxGNN score. Preclinical work combining CETP inhibition with PPARα agonism in transgenic mice points the same way.

There is an important caveat. People with CETP deficiency already have high HDL cholesterol, so raising it further is not an obvious therapeutic goal. The clinical rationale for fenofibrate in this condition is unclear, and the link is indirect and pathway-level only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical (mouse) | J Cardiovasc Pharmacol Ther | In human ApoB100/CETP transgenic mice, CETP inhibition (torcetrapib) and PPARα agonism (fenofibrate) were tested for effects on lipid profiles |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclinical (mouse) | J Biol Chem | Fenofibrate induced the PLTP gene, accounting for HDL enlargement in treated mice |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Preclinical/mechanistic | Front Physiol | HDL cholesterol did not correlate with fecal cholesterol or efflux capacity, suggesting HDL function matters; no direct evidence for fenofibrate in CETP deficiency |

## US Market Information

At least 16 US authorizations are on record (the list may be partial). Approved indication text is not available in the data compiled for this report. Five are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021695 | ANTARA (Lupin) | Capsule | Not available |
| ANDA076509 | Fenofibrate (Amneal) | Tablet | Not available |
| ANDA209660 | Fenofibrate (Alembic) | Film-coated tablet | Not available |
| ANDA202856 | Fenofibrate (Mylan) | Film-coated tablet | Not available |
| ANDA211407 | Fenofibrate (Chartwell RX) | Capsule | Not available |

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Relations recorded in the knowledge graph (not label text)**: fenofibrate is linked to liver failure, liver disease, pancreatitis, gallbladder disease and cholelithiasis, myopathy and rhabdomyolysis, thrombocytopenia, anemia, leukopenia and neutropenia (including agranulocytosis), and impaired renal function. These need confirmation against the label.
- **Drug Interactions**: The data list 100 interactions in total. The 20 shown are all Moderate and involve:
  - Sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide)
  - Many insulin products
  - Chenodeoxycholic acid
  - Esomeprazole

  Monitoring of glucose-lowering therapy is advisable.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and indirect pathway-level mechanistic overlap. No clinical trial exists, and none of the three publications studies fenofibrate in CETP deficiency, so the evidence level is L5. Because CETP deficiency already involves high HDL cholesterol, the clinical benefit of fenofibrate is unclear.

**To proceed, the following is needed:**
- A clear clinical hypothesis for what benefit fenofibrate would give in CETP deficiency, given already elevated HDL
- Mechanism of action data
- FDA package insert warnings and contraindications, to enable safety screening
- Direct preclinical or clinical studies in CETP deficiency
- Approved indication text for the US licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

