---
layout: default
title: Rotigotine
parent: Model Prediction Only (L5)
nav_order: 1137
evidence_level: L5
indication_count: 10
monitor_inn: "ROTIGOTINE"
predicted_indications: ["attention deficit-hyperactivity disorder", "schizophrenia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "faciodigitogenital syndrome", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "atypical glycine encephalopathy", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited"]
last_modified_at: 2026-11-20
description: "Rotigotine: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Restless legs syndrome, Parkinson disease"
---

# Rotigotine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Rotigotine: From Restless Legs Syndrome and Parkinson Disease to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Rotigotine is a dopamine agonist originally used to treat Parkinson disease and restless legs syndrome.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**,
but there are currently **0 clinical trials** and only **3 publications** (reviews and mechanistic studies) behind this prediction, so it remains a hypothesis-level finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Restless legs syndrome, Parkinson disease (the US license record contains no approved indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for rotigotine: "Rotigotine is a non-ergoline dopamine agonist. The precise mechanism of action of rotigotine as a treatment for Parkinson's disease is unknown, although it is thought to be related to its ability to stimulate dopamine receptors within the caudate-putamen in the brain." ([DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0), label version 2026-11-11; accessed 2026-11-19.) Based on the literature retrieved, rotigotine is a dopamine agonist that acts on D1 to D5 receptors, with notable activity at D3, D2 and D1. It also shows some activity at 5-HT1A and alpha-2B adrenergic receptors.

ADHD involves dysregulation of dopamine and noradrenaline signalling. The retrieved literature discusses heteromerization between the dopamine D4 receptor and the α2A adrenoceptor, both of which have been genetically linked to ADHD. In addition, restless legs syndrome (one of rotigotine's original indications) frequently co-occurs with ADHD, and the two conditions share dopaminergic involvement.

This is indirect, hypothesis-level support. No ADHD-specific rotigotine data are available, so the link remains a research question rather than an established finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | Overview of restless legs syndrome, a sensorimotor disorder affecting 2–3% of people in Western countries |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | Review of pharmacological options for restless legs syndrome in children |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical/Mechanistic | Pharmacological research | Heteromerization of α2A adrenoceptors with dopamine D4 receptor variants; relevant to ADHD and impulse-control disorders |

None of these publications tests rotigotine in ADHD.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA021829 | NEUPRO | UCB INC | Film, extended release; transdermal | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: hypertensive disorder, hypertension, multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, drug-induced dyskinesia.
- **Drug Interactions**: 51 interactions were identified, and the 20 listed are all rated Moderate. They include:
  - Opioids and related drugs: morphine (including liposomal), codeine, opium, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Sedating antihistamines: promethazine, chlorpheniramine, cetirizine, brompheniramine, carbinoxamine, clemastine, azelastine (nasal)
  - Others: metoclopramide, sibutramine, ethanol, dextromethorphan, ioflupane I-123

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (1.0000), but there are no clinical trials and the literature is indirect: two restless legs reviews and one receptor-level preclinical study. The evidence level is L4, with no rotigotine-specific ADHD data.

<!-- review:begin us-lic-20261031-rotigotine-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The evidence level is L4, with no rotigotine-specific ADHD data. Moreover, the only US NDA is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-rotigotine-1 -->

**To proceed, the following is needed:**
- Rotigotine-specific preclinical or clinical data in ADHD
- Detailed mechanism of action data, especially for D4 and α2 receptor activity
- FDA package insert warnings and contraindications
- Review of the knowledge-graph contraindication signals (hypertension, orthostatic hypotension) and the moderate drug interactions, particularly for a paediatric ADHD population
- Clarification of the regulatory and formulation situation

<!-- review:begin us-lic-20261106-rotigotine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the regulatory and formulation situation, given the cancelled US license" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-rotigotine-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Moreover, the only US NDA is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given the cancelled US license" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

