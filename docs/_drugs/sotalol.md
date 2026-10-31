---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 1178
evidence_level: L5
indication_count: 6
monitor_inn: "SOTALOL"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
last_modified_at: 2026-10-31
description: "Sotalol: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). Approved use: Not recorded in the local data"
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sotalol: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Sotalol is a beta-blocker with class III antiarrhythmic activity, originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** currently support this prediction, and the known pharmacology points in the opposite direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | at least 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. From general pharmacology, sotalol is a beta-blocker that also blocks potassium channels (class III antiarrhythmic activity). It slows sinus rate and atrioventricular conduction, which is how it controls rhythm in atrial fibrillation.

The prediction is **not mechanistically convincing**. Sick sinus syndrome type 2 is linked to HCN4 variants, and in sick sinus syndrome the problem is a sinus node that is already too slow or unreliable. A drug that slows the sinus rate and conduction can worsen sinus bradycardia, sinus arrest and conduction block. The knowledge graph itself lists sick sinus syndrome (including the familial form) as a contraindication for sotalol. The high score most likely reflects proximity within the cardiac-rhythm network rather than a true therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

Currently no related literature available for the predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019865 | BETAPACE AF (Legacy Pharma USA) | Tablet | Not available; status valid |
| ANDA207428 | Sotalol (Unichem) | Tablet | Not available; status valid |
| ANDA075563 | Sotalol Hydrochloride (Proficient Rx) | Tablet | Not available; status valid |
| ANDA075500 | Sotalol Hydrochloride (Bryant Ranch Prepack) | Tablet | Not available; status valid |
| ANDA076140 | Sotalol Hydrochloride (Bryant Ranch Prepack) | Tablet | Not available; status valid |

Two further cancelled ANDAs (Epic Pharma, Aphena Pharma Solutions) are not shown. All 7 licenses are oral tablets.

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence):** long QT syndrome (including familial), torsades de pointes, sick sinus syndrome (including familial), atrioventricular block, asthma (intrinsic and allergic) and other bronchial disease, hypotensive disorder, impaired renal function, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, anaphylaxis.
- **Drug Interactions:** 100 interactions were identified. Major-level examples include epinephrine, clarithromycin, picosulfuric acid and polyethylene glycol 3350 with electrolytes. Moderate-level examples include famotidine, cimetidine, bupropion, morphine, loperamide, atropine, dicyclomine, canagliflozin, dapagliflozin and chlorpropamide.
- **Proarrhythmia:** Sotalol prolongs the QT interval and carries a risk of torsades de pointes. Its QT-prolonging effect is additive with antipsychotics and other QT-prolonging drugs.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or publications. The drug's pharmacology (slowing the sinus rate and conduction) and its knowledge-graph contraindication in sick sinus syndrome argue against benefit and suggest potential harm. The drug is marketed in the US, with 7 valid licenses.

Other predicted indications are also at Hold: Wildervanck syndrome, sarcoglycanopathy, macrocephaly with dysmorphic facies and psychomotor retardation, and the obsolete ischemic stroke susceptibility entry have no evidence (L5). Stroke (L4) and manic bipolar affective disorder (L5) show only indirect links. The stroke link runs through atrial fibrillation rhythm management, and the one trial retrieved (NCT00007605, a completed Phase 3 study of amiodarone and sotalol for sinus rhythm maintenance in atrial fibrillation) concerns the original indication. The bipolar disorder papers concern drug-interaction safety, not efficacy.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Detailed mechanism of action data
- Any mechanistic or clinical rationale for benefit in HCN4-related sick sinus syndrome, given that sotalol is cautioned or contraindicated in sick sinus syndrome without a pacemaker
- A review of whether the model's high score is an artifact of cardiac-rhythm network proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

