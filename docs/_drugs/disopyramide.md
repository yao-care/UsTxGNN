---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
monitor_inn: "DISOPYRAMIDE"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
last_modified_at: 2026-10-14
description: "Disopyramide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not listed in the available US license records (drug class: antiarrhy…"
---

# Disopyramide
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

# Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a class IA antiarrhythmic drug (a sodium channel blocker with anticholinergic activity). The data compiled for this report show no approved-indication text on its US labels, so the original use is inferred from its drug class.
The TxGNN model predicts it may be effective for **Tourette syndrome** with a very high score, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available US license records (drug class: antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 5 (all cancelled; 2 NDAs and 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, disopyramide is a class IA antiarrhythmic that blocks sodium channels and has anticholinergic activity.

The review of this prediction found **no clear mechanistic link**. Tourette syndrome is mainly associated with dopaminergic dysfunction and abnormal cortico-striato-thalamo-cortical circuits. Sodium channel blockade with anticholinergic effects does not directly address these pathways. The high TxGNN score is a model output only and is not backed by trials or literature.

The other top-ranked predictions show the same pattern. They include ADHD (and its inattentive subtype), trichotillomania, faciodigitogenital syndrome, specific developmental disorder, chondromyxoid fibroma and trigeminal nerve neoplasm, and none has trial or literature support. The only predictions with a biologically plausible rationale are those in the arrhythmia area, such as idiopathic neonatal atrial flutter and multifocal atrial tachycardia. These are still prediction-only or supported by indirect evidence at best.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Tourette syndrome.

## US Market Information

All five US authorizations are cancelled, and the records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018655 | Norpace CR (Pfizer) | Capsule, extended release | Not provided (cancelled) |
| NDA017447 | Norpace (Pfizer) | Capsule, gelatin coated | Not provided (cancelled) |
| ANDA070102 | Disopyramide Phosphate (Teva) | Capsule | Not provided (cancelled) |
| ANDA070173 | Disopyramide Phosphate (Dr. Reddy's) | Capsule | Not provided (cancelled) |
| ANDA070101 | Disopyramide Phosphate (Teva) | Capsule | Not provided (cancelled) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for label safety information.

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not label text): long QT syndrome (including familial), atrioventricular block, cardiomyopathy (including hypertrophic), myocarditis, myocardial disorders, atrial fibrillation and flutter, hypotensive disorder, kidney disease, liver disease, gallbladder disease, potassium deficiency, benign prostatic hyperplasia, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, and hypoglycemia.
- **Drug interactions**: 100 interactions were found in total. The first 20 returned include:
  - **Major**: potassium citrate, clarithromycin, picosulfuric acid.
  - **Moderate**: famotidine, hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, amphotericin B (including lipid complex), hyoscyamine, atropine, glycopyrronium, clidinium, loperamide, aprepitant, bisacodyl, chlorpropamide.
  - **Minor**: cimetidine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests only on a model score. There is no mechanistic rationale, no clinical trial and no publication. The drug also has no active US license, and its known cardiac and anticholinergic safety concerns are significant for a non-cardiac indication.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to assess any link to Tourette syndrome
- Preclinical or literature evidence supporting a plausible mechanism in Tourette syndrome
- A review of the arrhythmia-related predictions (e.g., atrial flutter, multifocal atrial tachycardia), which have more plausible pharmacology and may be a better focus
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

