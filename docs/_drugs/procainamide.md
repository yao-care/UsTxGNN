---
layout: default
title: Procainamide
parent: Model Prediction Only (L5)
nav_order: 1085
evidence_level: L5
indication_count: 10
monitor_inn: "PROCAINAMIDE"
predicted_indications: ["Tourette syndrome", "hyperthyroidism", "Prinzmetal angina", "methemoglobinemia, alpha type", "methemoglobinemia", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "methemoglobin reductase deficiency", "rheumatoid arthritis"]
---

# Procainamide
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

# Procainamide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Procainamide is a class Ia sodium channel blocker antiarrhythmic, and no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no actual supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available approval records (the drug is known as an antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, procainamide is a class Ia sodium channel blocker used for cardiac arrhythmias.

Nothing in its known pharmacology connects to the dopaminergic or cortico-striato-thalamo-cortical circuitry implicated in Tourette syndrome. The high TxGNN score (99.46%) reflects a graph-based prediction only, and no credible mechanistic rationale supports it.

Other top-ranked predictions show the same pattern. Most are also L5 predictions with no plausible mechanism (e.g., methemoglobinemia, trichotillomania, nephrogenic syndrome of inappropriate antidiuresis). Hyperthyroidism and Prinzmetal angina have only tangential literature. Rheumatoid arthritis has literature that points toward harm, as described in the safety section.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Tourette syndrome.

For context, literature was retrieved for other lower-ranked predictions, but it does not support efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2242063](https://pubmed.ncbi.nlm.nih.gov/2242063/) | 1990 | Cohort | Arthritis Rheum | Procainamide inhibits T cell DNA methylation and induces autoreactivity; impaired methylation also found in SLE and rheumatoid arthritis patients (rheumatoid arthritis prediction) |
| [1734911](https://pubmed.ncbi.nlm.nih.gov/1734911/) | 1992 | Cohort | Arthritis Rheum | 83% of 52 asymptomatic patients on procainamide developed antinuclear antibodies (rheumatoid arthritis prediction) |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | Procainamide listed among drugs causing pulmonary fibrosis (rheumatoid arthritis prediction) |
| [15336799](https://pubmed.ncbi.nlm.nih.gov/15336799/) | 2004 | Review | Int J Cardiol | Acute ventricular rate control in atrial fibrillation and flutter (hyperthyroidism prediction; symptomatic relevance only) |
| [6977958](https://pubmed.ncbi.nlm.nih.gov/6977958/) | 1981 | Case report | Acta Cardiol | Torsades de pointes with variant angina was refractory to procainamide and responded to verapamil (Prinzmetal angina prediction) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206332 (cancelled) | Procainamide Hydrochloride (Nexus Pharmaceuticals) | Injection | Not available |
| ANDA218674 (cancelled) | Procainamide Hydrochloride (Caplin Steriles) | Injection, solution | Not available |
| ANDA218135 (cancelled) | Procainamide Hydrochloride (Sagent) | Injection, solution | Not available |
| ANDA088636 (cancelled) | Procainamide Hydrochloride (ProPharma Distribution) | Injection | Not available |
| ANDA089069 (cancelled) | Procainamide HCl (HF Acquisition Co, HealthFirst) | Injection, solution | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

- **Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text):
  - Cardiac: long QT syndrome (including familial), torsades de pointes, atrioventricular block, hypotensive disorder, digitalis poisoning
  - Haematological: agranulocytosis, neutropenia (including multiple congenital forms), thrombocytopenia
  - Organ function: kidney disease, liver disease, gallbladder disease
  - Immune and neuromuscular: systemic lupus erythematosus (including pediatric), myasthenia gravis, neuromuscular junction disease
  - Other: potassium deficiency disease, pyoureter
- **Autoimmunity signal**: The retrieved literature consistently shows procainamide inducing antinuclear antibodies and drug-induced lupus. This argues against use in rheumatoid arthritis and other autoimmune conditions.
- **Drug interactions**: The interaction search returned 100 records; 20 are shown in the data. Major interactions include:
  - Clarithromycin
  - Levofloxacin
  - Dolasetron
  - Palonosetron
  - Eliglustat
  - Picosulfuric acid
  - Sodium sulfate
  - Polyethylene glycol (3350 with electrolytes)

  Moderate interactions include famotidine, ranitidine, cimetidine, metformin, loperamide, metoclopramide, and bisacodyl. Many of the major interactions likely relate to QT prolongation or electrolyte disturbance.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests solely on a graph-based score. There are no clinical trials, no literature, and no plausible mechanism. Procainamide also carries significant safety signals (QT prolongation, blood dyscrasias, drug-induced lupus), and all of its US licenses are cancelled.

**To proceed, the following is needed:**
- A documented mechanistic hypothesis linking sodium channel blockade to Tourette syndrome pathophysiology
- Preclinical or exploratory data supporting any effect on tic disorders
- Package insert warnings and contraindications, and approved indication text
- Mechanism of action data from DrugBank
- A risk-benefit analysis addressing proarrhythmic, haematological, and autoimmune risks, particularly in a younger Tourette population
- A review of the commercial availability of the drug, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

