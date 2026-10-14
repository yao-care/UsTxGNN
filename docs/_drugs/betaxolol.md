---
layout: default
title: Betaxolol
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 1
---

# Betaxolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Betaxolol: From Hypertension and Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a beta-1 selective adrenergic blocker, originally used to treat hypertension, open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ocular hypertension (from knowledge graph indication edges; no approved indication text in the US license records) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 licenses in total (1 NDA, 2 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, betaxolol is a beta-1 selective adrenergic antagonist. In the eye, it lowers intraocular pressure (IOP) by reducing aqueous humor production at the ciliary body. Its efficacy in open-angle glaucoma and ocular hypertension is established.

Primary hereditary glaucoma (for example, primary congenital or juvenile-onset forms) shares elevated IOP as the key modifiable driver, so a mechanistic link is plausible. The very high TxGNN score likely reflects how close this disease sits to the approved glaucoma indications in the knowledge graph.

There are important caveats:
- Hereditary forms often arise from developmental abnormalities of the anterior-chamber angle (e.g., variants in CYP1B1, MYOC, FOXC1). In these cases medical therapy is frequently only a temporizing measure before surgery.
- Systemic absorption of beta-blockers raises pediatric safety concerns, such as bradycardia and bronchospasm.
- The prediction is based on indication similarity, not on any independent clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078962 | Betaxolol Hydrochloride (KVK-Tech) | Tablet, coated (oral) | Not specified; status cancelled |
| ANDA075541 | Betaxolol (PuraCap Laboratories) | Tablet, film coated (oral) | Not specified; status cancelled |
| NDA019270 | Betaxolol Hydrochloride (Sandoz) | Solution/drops (ophthalmic) | Not specified; status cancelled |

All three licenses are cancelled, so there is no currently valid US-marketed betaxolol product in the data compiled for this report.

---

## Safety Considerations

No label warnings or contraindication text were available. The following comes from the knowledge graph and drug interaction data.

- **Contraindication signals (knowledge graph, not label text)**: The graph links betaxolol to the following disease areas:
  - Respiratory: asthma (intrinsic and allergic), pulmonary emphysema, bronchial disease
  - Cardiac conduction: atrioventricular block, atrioventricular dissociation
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hypoglycemia
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Organ disease: kidney, liver and gallbladder disease
  - Adrenal and tumour-related: pheochromocytoma, paraganglioma, adrenal gland cancer, and several other cancers
  - Skin: psoriasis, parapsoriasis
  - Psychiatric: anxiety, neurotic and dysthymic disorders
- **Drug interactions**: 100 interactions were recorded. The 20 shown are mostly Moderate, with a few Minor:
  - Moderate: epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, atropine, dexamethasone, betamethasone, acetohexamide, budesonide, and several calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate)
  - Minor: acetylsalicylic acid, aluminum hydroxide, attapulgite
- **Pediatric consideration**: Systemic absorption of beta-blockers may cause bradycardia and bronchospasm, which is particularly relevant for congenital and juvenile glaucoma.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications behind it (Evidence Level L5). All US licenses are cancelled, and label-level safety information is missing. Hereditary glaucoma is often managed surgically, and beta-blocker use in children carries safety concerns.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- A literature and trial search for betaxolol in congenital, juvenile and other hereditary glaucoma
- Assessment of ophthalmic route compatibility and of the current availability of the ophthalmic formulation
- A pediatric safety review covering systemic beta-blocker exposure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

