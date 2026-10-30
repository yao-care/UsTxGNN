---
layout: default
title: Magnesium Hydroxide
parent: Model Prediction Only (L5)
nav_order: 883
evidence_level: L5
indication_count: 1
monitor_inn: "MAGNESIUM HYDROXIDE"
predicted_indications: ["stomach disease"]
last_modified_at: 2026-10-30
description: "Magnesium Hydroxide: predicted new indication Stomach disease (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
---

# Magnesium Hydroxide
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

## Magnesium Hydroxide: From Acid-Related Gastrointestinal Conditions to Stomach Disease
{: .text-alpha }

## One-Sentence Summary

Magnesium hydroxide is an antacid and osmotic laxative whose knowledge-graph-recorded uses include peptic ulcer disease, reflux disease, dyspepsia and constipation.
The TxGNN model predicts it may be useful for **stomach disease**, but this is a broad category that largely overlaps with those existing uses.
Currently there are **0 registered clinical trials** and **20 publications** (mostly old reviews, animal studies and pharmacology studies) for this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, constipation, dyspepsia (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of FDA Applications | at least 3 |
| Number of approvals | At least 3 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, magnesium hydroxide is an antacid that neutralizes gastric hydrochloric acid and raises intragastric pH. This gives a plausible link to acid-related stomach conditions.

"Stomach disease" is a broad parent category covering related conditions (peptic ulcer disease, dyspepsia, reflux). The high score (0.9923) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a genuinely new repurposing signal.

The cited studies mostly concern acid-related conditions, antacid combinations (aluminium/magnesium hydroxide) or animals. None studies "stomach disease" itself as a defined disease, so the evidence level is capped at L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Most items below involve combination antacids (aluminium hydroxide plus magnesium hydroxide), not magnesium hydroxide alone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7267678](https://pubmed.ncbi.nlm.nih.gov/7267678/) | 1981 | Double-blind randomized trial | Pharmatherapeutica | In 36 patients with symptomatic gastritis, Mg/Al hydroxide suspension gave more symptom improvement than hydrotalcite/dimethicone |
| [3903784](https://pubmed.ncbi.nlm.nih.gov/3903784/) | 1985 | Controlled trial | Pharmatherapeutica | Al/Mg hydroxide antacids used as the comparator in 30 gastric or duodenal ulcer patients, against triletide |
| [8520743](https://pubmed.ncbi.nlm.nih.gov/8520743/) | 1995 | Randomized double-blind trial | Am J Respir Crit Care Med | Sucralfate versus antacids for stress ulcer prophylaxis in ventilated ICU patients |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical study | J Clin Gastroenterol | Sodium bicarbonate versus Al/Mg hydroxide on postprandial gastric acid in duodenal ulcer patients |
| [6613216](https://pubmed.ncbi.nlm.nih.gov/6613216/) | 1983 | Pharmacokinetic study | Z Gastroenterol | No interaction of an Al/Mg hydroxide antacid with cimetidine in peptic ulcer patients |
| [236651](https://pubmed.ncbi.nlm.nih.gov/236651/) | 1975 | Review | Am J Hosp Pharm | Pharmacology and clinical use of antacids in acid-peptic disease |
| [6755653](https://pubmed.ncbi.nlm.nih.gov/6755653/) | 1982 | Review | Scand J Gastroenterol Suppl | Antacids hasten ulcer healing and prevent stress-ulcer bleeding; discusses acid rebound |
| [6293043](https://pubmed.ncbi.nlm.nih.gov/6293043/) | 1982 | Review | Scand J Gastroenterol Suppl | Antacid-related changes in mineral metabolism and side effects |
| [8641951](https://pubmed.ncbi.nlm.nih.gov/8641951/) | 1996 | Pharmacodynamic study (horses) | J Am Vet Med Assoc | Effect of Al/Mg hydroxide antacid on gastric pH in horses |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Animal study (rat) | Scand J Gastroenterol | An Al/Mg hydroxide antacid prevented experimental gastric lesions dose-dependently |

## US Market Information

The list below may be partial. The records compiled for this report contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M007 | Milk of Magnesia Cherry (CVS) | Liquid | Not stated in available records |
| 505G(a)(3) | Dulcolax (Chattem, Inc.) | Liquid | Not stated in available records |
| M001 | Humco Milk of Magnesia (Humco Holding Group, Inc.) | Suspension | Not stated in available records |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links magnesium hydroxide to contraindication relations with kidney disease and impaired renal function, liver disease, gallbladder disease, hypercalcemia, hyperparathyroidism, nephrolithiasis, nephrocalcinosis, sarcoidosis, hypophosphatemia, diarrheal disease, appendicitis, intestinal impaction, hemorrhoid, and gastric cancer or neoplasm. These should be verified against the product label.
- **Drug Interactions:** 100 interactions were found in the interaction database. Examples:
  - Major: dolutegravir
  - Moderate: doxycycline, alendronic acid, amiodarone, tramadol, acetazolamide, hydrochlorothiazide, hydrocortisone, salbutamol
  - Minor: famotidine, ranitidine, ibuprofen

Warnings and contraindications from the package insert are not available. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
"Stomach disease" is a broad category that mostly overlaps with the drug's existing acid-related uses, so the high score is not a clear new-indication signal. No registered trials exist, and the available literature is old, combination-based, or from animals, with no direct study of the predicted disease. The evidence level is therefore L5.

**To proceed, the following is needed:**
- A specific, clinically defined target condition (for example gastritis or functional dyspepsia) instead of the broad "stomach disease"
- Modern controlled studies of magnesium hydroxide alone
- Package insert warnings and contraindications, and the approved indication text
- Mechanism of action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

