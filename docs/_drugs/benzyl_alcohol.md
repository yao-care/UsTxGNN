---
layout: default
title: Benzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
monitor_inn: "BENZYL ALCOHOL"
predicted_indications: ["bronchitis"]
last_modified_at: 2026-10-14
description: "Benzyl Alcohol: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
---

# Benzyl Alcohol
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

# Benzyl Alcohol: From Dermatitis to Bronchitis

## One-Sentence Summary

Benzyl alcohol is a topical ingredient (used in products such as throat/mouth gels and pain-relief sprays) and is listed in the knowledge graph for dermatitis. The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **2 loosely related publications**, one of which suggests that inhaled benzyl alcohol may *cause* bronchitis rather than treat it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available in US license records) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzyl alcohol has weak antimicrobial and preservative properties, and it is also used as a local anaesthetic-type ingredient in topical products. In theory, antimicrobial activity could be relevant to infectious bronchitis.

This rationale is weak. The high TxGNN score (99.46%) is a computational prediction without clinical support. The relationship between a skin condition (dermatitis) and an airway condition (bronchitis) is not mechanistically clear from the available data. The literature points in the opposite direction: a study of nebulized bacteriostatic saline, which contains benzyl alcohol as a preservative, examined whether it irritates the airway lining and reported bronchitis as a possible adverse effect. This is a safety signal, not a therapeutic one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Case report / case series (adverse event) | The Journal of Family Practice | Tested whether nebulized bacteriostatic saline, which contains the preservative benzyl alcohol, irritates the tracheobronchial lining in healthy adults; the title reports it as a cause of bronchitis (a harm signal) |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | In vitro phytochemical study | Heliyon | Studied Senna tora leaf extracts for antioxidant, anti-inflammatory and antibacterial activity; bronchitis is mentioned only as a traditional use of the plant, and the study is not directly relevant to benzyl alcohol |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M022 | Zilactin | Gel | Not specified (cancelled) |
| M017 | Lidocaine Plus Pain Relieving | Liquid | Not specified (cancelled) |
| 505G(a)(3) | CVS Maximum Strength LIDOCAINE PLUS | Spray | Not specified (cancelled) |
| part348 | Ivy-Dry Super | Spray | Not specified (cancelled) |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links benzyl alcohol to possible contraindications in the following conditions:
  - Cardiovascular: hypertension, coronary artery disease, atherosclerosis
  - Respiratory: chronic obstructive pulmonary disease (COPD)
  - Gastrointestinal: peptic ulcer disease
  - Skin: contact dermatitis, occupational dermatitis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Urological: benign prostatic hyperplasia, bladder neck obstruction
  - Eye: angle-closure glaucoma
- **Airway irritation:** The published report on nebulized saline preserved with benzyl alcohol raises concern about airway irritation when the compound is inhaled. This is directly relevant to the predicted bronchitis use.
- **Drug interactions:** No interaction records were found.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials, no supportive literature, and no mechanism data. The only relevant publication suggests that inhaled benzyl alcohol may irritate the airways. In addition, all US licenses are cancelled, and the available dosage forms (gel, liquid, spray) are not designed for treating bronchitis.

**To proceed, the following is needed:**
- Mechanism of action data for benzyl alcohol
- FDA package insert warnings and contraindications, to allow safety screening
- Evidence that benzyl alcohol has therapeutic activity in bronchitis, including preclinical data
- A safety assessment of inhaled exposure, given the reported airway irritation
- Clarification of a suitable route and formulation for respiratory use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

