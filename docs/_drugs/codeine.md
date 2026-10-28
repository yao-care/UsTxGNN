---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 3
monitor_inn: "CODEINE"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-10-27
description: "Codeine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Codeine
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

## Codeine: opioid analgesic and antitussive → nasal cavity disease (nasal cavity disease)
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid medicine marketed in the United States as single-ingredient tablets and as oral solutions combined with guaifenesin.
The TxGNN model predicts it may be relevant to **nasal cavity disease**, but the support is very thin: **no clinical trials** and **1 publication**, a case report that describes an adverse event rather than a benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Codeine is an opioid, and opioids are generally used for pain relief and cough suppression. Nothing in the data shows how this would translate into treating structural or inflammatory disease of the nasal cavity.

The only publication retrieved describes a rhinolith (a stone in the nose) that formed around a hardened mixture of codeine and opium, an "opioma", which was a foreign body. That is an unusual complication, not a therapeutic effect. The very high TxGNN score therefore appears to reflect a model association and not a plausible disease-modifying mechanism. At this point the prediction should be treated as a hypothesis with no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a unilateral rhinolith formed around an impacted foreign body, which turned out to be a hardened codeine and opium mixture; it was removed under local anesthesia. This is an adverse or incidental event, not evidence of benefit. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203046 | Codeine Sulfate | Tablet | Not recorded |
| NDA022402 | Codeine sulfate | Tablet | Not recorded |
| M012 | Codeine-Guaifenesin | Solution | Not recorded |
| MO12 | Guaifenesin and Codeine Phosphate | Solution | Not recorded |
| M013 | Codeine-Guaifenesin | Solution | Not recorded |

---

## Safety Considerations

- **Disease-related cautions (from relationship data, not label text)**: Codeine has recorded contraindication relations with several conditions, including hypertension, liver failure and liver disease, kidney disease, epilepsy, chronic obstructive pulmonary disease, pancreatitis, gallbladder disease, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, porphyria, thrombocytopenia, psychotic and anxiety disorders, and insomnia. These should be checked against the actual package insert.
- **Drug Interactions**: 100 interactions were found. Major ones include **alvimopan** and **bupropion**. Moderate ones include atropine, cimetidine, dexamethasone, dicyclomine, glycopyrronium, granisetron, hyoscyamine, loperamide, dronabinol and eliglustat. Anticholinergic and other gut-slowing drugs are common among these.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9993), but no study supports codeine as a treatment for nasal cavity disease. The only publication is a case report of a foreign-body complication, so the evidence level is L5.

**To proceed, the following is needed:**
- A clear mechanistic hypothesis linking codeine to nasal cavity disease, and its mechanism of action data
- Any clinical or observational study that directly examines codeine for this condition
- Package insert warnings and contraindications for safety screening
- A review of opioid-specific risks (dependence, respiratory depression, drug interactions) against any plausible benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

