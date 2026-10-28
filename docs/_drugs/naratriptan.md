---
layout: default
title: Naratriptan
parent: Model Prediction Only (L5)
nav_order: 955
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "NARATRIPTAN"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
description: "Naratriptan: predicted new indication Atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Naratriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Naratriptan: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Naratriptan is a triptan originally used to treat migraine.
but there are **0 registered clinical trials** and only **indirect literature** (20 publications on migraine and triptans in general, none specific to this subtype). Triptans have also historically been avoided in this subtype for safety reasons.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known class pharmacology, naratriptan is a selective 5-HT1B/1D receptor agonist approved for acute migraine. Its effect is thought to come from cranial vasoconstriction, inhibition of trigeminal CGRP release, and blocking of trigeminovascular pain transmission.

Migraine with brainstem aura is a subtype of migraine with aura, so the pharmacological rationale overlaps with the approved indication. The very high TxGNN score is consistent with this overlap.

**An important caution:** triptans have historically been avoided, or contraindicated, in migraine with brainstem aura and hemiplegic migraine because of theoretical vasoconstrictive and ischemic risk. The knowledge graph also lists familial or sporadic hemiplegic migraine as a contraindicated condition for this drug. The available evidence does not resolve this concern, so the prediction is best treated as a research question rather than a treatment recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below concern migraine and naratriptan in general. None directly studies migraine with brainstem aura. Randomized trials are listed first, then reviews and other studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized, double-blind crossover comparison of naratriptan vs sumatriptan on headache recurrence in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Naratriptan given during the prodrome to test whether it prevents migraine headache |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | Randomized, placebo-controlled | Headache | Naratriptan 1 mg and 2.5 mg twice daily vs placebo as short-term prophylaxis of menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of drugs for acute migraine treatment in adults |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Sumatriptan was less effective in migraine with aura than without aura |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review | Headache | Use of naratriptan in intractable migraine |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open-label pilot | Neurological Sciences | Naratriptan as short-term prophylaxis in pure menstrual migraine, a six-month non-comparative study |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatric Drugs | Use of triptans for pediatric migraine |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Whether treatment in the premonitory phase is a useful migraine strategy |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Case report | Brain & Development | Naratriptan relieved intractable migraine-like headaches in a patient with Sturge-Weber syndrome and a history of cerebral infarction |

## US Market Information

All three US authorizations are generic applications that are now cancelled, and no approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA200502 | Naratriptan (Avet Pharmaceuticals) | Tablet | Not recorded (valid) |
| ANDA091441 | Naratriptan (Bionpharma) | Film-coated tablet | Not recorded (valid) |
| ANDA090381 | Naratriptan (Hikma) | Tablet | Not recorded (valid) |

## Safety Considerations

- **Contraindicated conditions (knowledge graph, not label text):** The TxGNN knowledge graph lists the following conditions as contraindications:
  - **Cardiovascular:** hypertension, coronary artery disease, myocardial infarction, myocardial ischemia, Prinzmetal angina, coronary thrombosis, peripheral vascular disease and peripheral arterial disease, intermittent vascular claudication
  - **Cerebrovascular:** stroke, cerebral infarction, cerebrovascular disorder, transient ischemic attack, vertebrobasilar insufficiency
  - **Metabolic and other:** liver failure, diabetes mellitus, diabetic ketoacidosis, obesity (including monogenic obesity), hemoglobinopathy
  - **Migraine subtype:** familial or sporadic hemiplegic migraine

  The vascular and cerebrovascular entries are especially relevant to the brainstem-aura question.
- **Drug interactions:** 39 interactions were identified. Those rated **Major** are:
  - Lorcaserin
  - Dolasetron
  - Palonosetron
  - Granisetron
  - Ondansetron
  - Dexfenfluramine
  - Fenfluramine
  - Sibutramine
  - Methylene blue

  Most of these involve serotonergic effects. Morphine (including liposomal) is rated Moderate. Several others (e.g., omeprazole, lansoprazole, pantoprazole, ranitidine, clarithromycin, bupropion, prednisone, budesonide, promethazine) have unknown severity ratings.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible because the subtype shares pharmacology with the approved migraine indication. However, there are no clinical trials, no literature specific to brainstem aura, and a recognized safety concern: triptans have historically been avoided in this subtype, and the knowledge graph flags related contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A focused review of ischemic and vasoconstrictive risk of triptans in migraine with brainstem aura
- Evidence from studies that directly enrol patients with this subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

