---
layout: default
title: Carteolol
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Carteolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension, open-angle glaucoma, ocular hypertension"
---

# Carteolol
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

## Carteolol: From Hypertension and Open-Angle Glaucoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Carteolol is a non-selective beta-blocker originally used for hypertension and for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ocular hypertension (the US label text is not available in the data compiled for this report; these indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (ANDA075476, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, carteolol is a non-selective beta-adrenergic antagonist with intrinsic sympathomimetic activity. In open-angle glaucoma and ocular hypertension, it lowers intraocular pressure (IOP) by reducing aqueous humor production at the ciliary body.

Primary hereditary glaucoma (for example, primary congenital glaucoma or juvenile open-angle glaucoma) is a genetically determined form of glaucoma. Its clinical hallmark is also elevated IOP. The shared IOP-lowering pharmacology is a plausible link, and it likely explains the very high TxGNN score.

This remains a prediction based on graph proximity to the approved glaucoma indications, not on independent clinical evidence. Two caveats apply:
- Primary congenital glaucoma is mainly managed surgically.
- Beta-blocker use in infants carries systemic safety concerns, including bronchospasm, bradycardia and apnea.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075476 (Cancelled) | Carteolol Hydrochloride (Sandoz Inc) | Solution | Not available |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Carteolol is linked to contraindications in bronchitis, asthma (including intrinsic and allergic asthma), pulmonary emphysema, diabetes mellitus, diabetic ketoacidosis, myasthenia gravis and other neuromuscular junction diseases, atrioventricular block, congestive heart failure and heart failure, and anaphylaxis.
- **Drug Interactions**: The interaction query returned 100 records. Those listed in the compiled data include:
  - **Major**: epinephrine, dolasetron.
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), anticholinergics (atropine, hyoscyamine, methscopolamine, dicyclomine), bupropion, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, calcium phosphate and calcium acetate.
  - **Minor**: acetylsalicylic acid, magnesium oxide.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and a plausible IOP-lowering mechanism. There are no clinical trials or publications, and the only US license is cancelled. Surgery is the main treatment for primary congenital glaucoma, and beta-blockers pose systemic risks in infants.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, to allow safety screening
- Mechanism-of-action data from DrugBank
- A literature and trial search for carteolol or topical beta-blockers in hereditary or congenital glaucoma
- A pediatric safety assessment (bronchospasm, bradycardia, apnea)
- Route and formulation compatibility analysis, and confirmation of an active regulatory pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

