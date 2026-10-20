---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "CODEINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
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

# Codeine: From Allergic Rhinitis and Upper-Airway Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid originally associated with upper-respiratory and headache-related indications, such as allergic rhinitis, pharyngitis, the common cold and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this rests on a model score alone, with **0 clinical trials** and **1 publication** (a case report describing an adverse event, not a benefit).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, nasopharyngitis, headache disorder (knowledge-graph indications; no approved indication text is available in the US license records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is an opioid analgesic and antitussive, and it is already linked to rhinitis, nasopharyngitis, pharyngitis and the common cold in the knowledge graph. These links most likely reflect symptomatic relief, such as cough suppression and pain relief, and not treatment of the underlying disease.

The high TxGNN score (0.999) most likely reflects the overlap between "nasal cavity disease" and the nasal and upper-airway conditions codeine is already linked to. It is therefore probably an extension of existing indications and not a true new-use signal. The only publication found describes a rhinolith (a nasal stone) that formed around a foreign body made of hardened codeine and opium. That is an incidental or adverse event, not a therapeutic effect. No disease-modifying mechanism for structural nasal cavity disease is supported by the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a unilateral rhinolith formed around a foreign body that was a hardened codeine and opium mixture (an "opioma"). It was removed under local anesthesia. This is not evidence of therapeutic benefit. |

## US Market Information

All five US authorizations are cancelled, and none has approved indication text on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203046 | Codeine Sulfate (Lannett) | Tablet | Not available (cancelled) |
| NDA022402 | Codeine sulfate (Hikma) | Tablet | Not available (cancelled) |
| M012 | Codeine-Guaifenesin (Westminster) | Solution | Not available (cancelled) |
| MO12 | Guaifenesin and Codeine Phosphate (Preferred Pharmaceuticals) | Solution | Not available (cancelled) |
| M013 | Codeine-Guaifenesin (NuCare) | Solution | Not available (cancelled) |

## Safety Considerations

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for them.

- **Disease contraindications from the knowledge graph** (these come from knowledge-graph drug-disease edges, not label text): hypertension, liver failure and liver disease, epilepsy, insomnia, COPD, anxiety disorder, porphyria, kidney disease, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, psychotic and other mental disorders, gastritis, dermatitis herpetiformis.
- **Drug interactions:** 100 interactions were found. Of the 20 listed, two are rated **Major**: alvimopan and bupropion. The others are rated Moderate, including atropine, cimetidine, dexamethasone, dicyclomine, glycopyrronium, granisetron, hyoscyamine, loperamide, eluxadoline, fenfluramine and dronabinol.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the single case report describes an adverse event and not a benefit. The prediction most likely overlaps with codeine's existing symptomatic upper-airway indications, and all US licenses are cancelled.

**To proceed, the following is needed:**
- The mechanism of action data
- The package insert warnings and contraindications
- A clear definition of which nasal cavity condition would be treated, and evidence of benefit beyond symptomatic relief
- Any prospective clinical or observational data in the target population
- A risk assessment for dependence, respiratory depression and pediatric safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

