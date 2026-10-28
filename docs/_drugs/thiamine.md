---
layout: default
title: Thiamine
parent: Model Prediction Only (L5)
nav_order: 1221
evidence_level: L5
indication_count: 3
monitor_inn: "THIAMINE"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "primary hereditary glaucoma", "open-angle glaucoma"]
last_modified_at: 2026-10-23
description: "Thiamine: predicted new indication resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L5). Approved use: Not available"
---

# Thiamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Thiamine: From an Unspecified Original Indication to resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Thiamine (vitamin B1) is marketed in the United States as injectable products, but the data compiled for this report contain no approved indication text. The TxGNN model's top prediction is **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, which has **0 clinical trials** and **0 publications** behind it. The only prediction with any literature is **open-angle glaucoma** (6 publications, none of them interventional), and that literature is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the compiled data) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (top-ranked); other predictions: primary hereditary glaucoma, open-angle glaucoma |
| TxGNN Prediction Score | 0.9943 (top-ranked prediction) |
| Evidence Level | L5 (top-ranked prediction) |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | at least 11 |
| Number of approvals | At least 11 ANDAs or similar records (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thiamine is a vitamin cofactor for carbohydrate-metabolism enzymes, but the compiled data do not describe its mechanism.

For the top-ranked prediction, **resistance to thyroid hormone**, no mechanistic link is supported. This condition is a monogenic receptor defect (a THRB mutation). Thiamine has no known action on thyroid hormone receptor beta signaling. The score of 0.9943 is a model output only.

For **primary hereditary glaucoma** (score 0.9940), the only link is speculative. Thiamine supports mitochondrial energy metabolism, and mitochondrial dysfunction is implicated in retinal ganglion cell vulnerability. Nothing in the compiled data supports this, and hereditary glaucoma is driven by genetic variants (e.g., MYOC, CYP1B1) that thiamine is not known to address.

For **open-angle glaucoma** (score 0.9936), there is indirect observational evidence. A 1979 study found lower blood thiamine levels in patients with chronic open-angle glaucoma than in controls. A plausible but untested hypothesis is that thiamine supports energy metabolism and reduces oxidative stress in retinal ganglion cells and the trabecular meshwork.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for any of the three predicted indications.

---

## Literature Evidence

The only literature in the compiled data concerns open-angle glaucoma, the third-ranked prediction. No literature is available for the top-ranked prediction. None of these papers is an interventional study of thiamine.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [485004](https://pubmed.ncbi.nlm.nih.gov/485004/) | 1979 | Case-control / observational | Annals of Ophthalmology | Among 38 glaucoma patients and 12 controls, patients had significantly lower blood thiamine (P < 0.001); no difference in ascorbic acid. Poor thiamine absorption was noted in the glaucoma patients. |
| [32214001](https://pubmed.ncbi.nlm.nih.gov/32214001/) | 2020 | Cross-sectional survey | Nutrients | Korean national survey relating obesity and nutrient intake to primary open-angle glaucoma. |
| [29565276](https://pubmed.ncbi.nlm.nih.gov/29565276/) | 2018 | Cross-sectional survey | Nutrients | Korean national survey on dietary niacin and open-angle glaucoma. This concerns niacin, not thiamine. |
| [40402521](https://pubmed.ncbi.nlm.nih.gov/40402521/) | 2025 | Metabolomic profiling | Investigative Ophthalmology & Visual Science | Aqueous humor metabolomics in POAG, with anti-inflammatory and neuroprotective metabolites tested in mice. A link to thiamine cannot be established from the available text. |
| [30025119](https://pubmed.ncbi.nlm.nih.gov/30025119/) | 2018 | Molecular profiling | Investigative Ophthalmology & Visual Science | microRNA profiles in glaucomatous optic neuropathy. Background biology only. |
| [41889963](https://pubmed.ncbi.nlm.nih.gov/41889963/) | 2026 | Preclinical (preprint) | bioRxiv | MIF-CD74 signaling in trabecular meshwork dysfunction. Background biology only. |

---

## US Market Information

The compiled data list at least 11 records, and the list may be partial. None includes approved indication text. All are single-ingredient injectable products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217181 | Thiamine Hydrochloride (OneSource Specialty Pharma) | Injection, solution | Not available |
| ANDA215692 | Thiamine (Caplin Steriles) | Injection, solution | Not available |
| ANDA080571 | Thiamine Hydrochloride (HealthFirst) | Injection, solution | Not available |
| ANDA206106 | Thiamine Hydrochloride (Sagent) | Injection, solution | Not available |
| ANDA217800 | Thiamine Hydrochloride (Gland Pharma) | Injection, solution | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the compiled data, and the knowledge graph records no contraindicated diseases for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (resistance to thyroid hormone) rests on model output alone (evidence level L5), and there is no plausible mechanistic link to a THRB receptor defect.
- Open-angle glaucoma has only indirect observational and background-biology literature, with no interventional trial of thiamine. No cited study tests thiamine as a treatment, so it also stays at L5 under the evidence ceiling rule. It is best treated as a research question rather than a development candidate.
- Safety data from the package insert are missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications, and approved indications
- Mechanism of action data (e.g., from DrugBank)
- For glaucoma: preclinical or interventional studies directly testing thiamine, and a check of the 1979 blood-level finding in modern cohorts
- For thyroid hormone resistance: a biological rationale before any further work, given that it is a monogenic receptor disorder
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

