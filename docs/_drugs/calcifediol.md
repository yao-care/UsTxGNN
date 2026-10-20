---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Calcifediol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Hypercalcemia, nephrocalcinosis, phosphorus metabolism disease…"
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
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

# Calcifediol: From Vitamin D–Related Mineral Disorders to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D3) is a vitamin D metabolite, originally associated with disorders of calcium and phosphate metabolism, rickets, and renal bone disease.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency** (a deprecated ontology term), with **0 clinical trials** and **0 publications** directly supporting this top prediction.
Evidence is limited to model prediction, though two lower-ranked predictions (hereditary hypophosphatemic rickets and vitamin D-dependent rickets) have one publication each.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia, rickets, osteomalacia, renal osteodystrophy (from the knowledge graph; no approved indication text is available in the US licence data) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, calcifediol is the main circulating form of vitamin D and the direct precursor of calcitriol, the active hormone. It is produced by hepatic 25-hydroxylation and is the standard biomarker of vitamin D status. Repletion in vitamin D deficiency is therefore mechanistically plausible.

However, this is the drug's native physiological role rather than a true repurposing. The disease term is also flagged as obsolete in the ontology. The very high TxGNN score likely reflects close pharmacological and graph proximity rather than new evidence.

Other predictions follow a similar pattern:

- **Renal tubular acidosis (99.86%)**: The link is indirect. Vitamin D metabolites might help secondary bone disease, but they would not correct the tubular acidification defect.
- **Hereditary hypophosphatemic rickets (99.76%)**: Active vitamin D (calcitriol or alfacalcidol) plus phosphate is standard care. Calcifediol is not a typical agent here.
- **Vitamin D-dependent rickets (99.18%)**: This is the best mechanistic match for type 1B (CYP2R1 25-hydroxylase deficiency), because calcifediol bypasses the enzymatic block. Types 1A and 2 would not be expected to respond.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the four predicted indications.

## Literature Evidence

No literature is available for the top prediction (obsolete vitamin D deficiency). Literature found for lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Overview of rickets types and treatment with vitamin D and its analogues (relates to hereditary hypophosphatemic rickets); indirect support only |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Case report/Review | J Bone Miner Res | Vitamin D-dependent rickets type 1B (25-hydroxylase deficiency) described in 7 patients from 2 families; supports the mechanistic rationale indirectly |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208010 | Rayaldee (OPKO Pharmaceuticals LLC) | Capsule, extended release (oral) | Not available; status: cancelled |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not package insert text): kidney disease, pyoureter, sarcoidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, hyperphosphatemia, hypervitaminosis, arteriosclerosis obliterans. These reflect the risk of excess calcium and phosphate.
- **Drug Interactions**: 57 interactions were identified. Major ones include:
  - Cholecalciferol
  - Calcitriol
  - Burosumab

  Moderate ones include:
  - Thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide)
  - Anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital)
  - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
  - Aluminum hydroxide
  - Digitoxin
  - Topical vitamin D analogues (calcipotriol, calcitriol)

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction relies on the model score alone (L5). It reflects the drug's native role and uses an obsolete disease term, so it is not genuine repurposing. The US licence is cancelled, and the package insert safety data is missing, which is a blocking gap for safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Mechanism of action data (for example from DrugBank)
- Re-mapping the prediction to a current disease term and defining the target population
- For vitamin D-dependent rickets type 1B, a focused evidence review and a feasibility assessment, since it is a very rare condition and currently a research question
- A review of the current regulatory status, since the only NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

