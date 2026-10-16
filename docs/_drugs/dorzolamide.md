---
layout: default
title: Dorzolamide
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
monitor_inn: "DORZOLAMIDE"
predicted_indications: ["primary hereditary glaucoma", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "glaucoma 1, open angle", "open angle glaucoma", "congestive heart failure", "acute pulmonary heart disease", "respiratory failure"]
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma** (score 99.99%), but there are currently **0 clinical trials** and **0 publications** for this specific indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid license in the data) |
| Number of NDAs | 9 (all listed as cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dorzolamide inhibits carbonic anhydrase II in the ciliary body of the eye. This reduces aqueous humor secretion and lowers intraocular pressure (IOP). The data compiled for this report also show that it binds other carbonic anhydrase isoforms (CA1, CA7, CA12 and CA14). Detailed mechanism-of-action data are not otherwise available.

Hereditary glaucoma, like open-angle glaucoma, is driven by elevated IOP. Lowering aqueous humor production is therefore mechanistically plausible. This is the same pharmacological effect as the original indication, not a new mechanism.

No trials or publications were found for hereditary glaucoma specifically. The case rests on the high model score and this mechanistic reasoning.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

## US Market Information

All 9 US authorizations are generic ANDAs with status "cancelled". The data compiled for this report contain no approved-indication text for them. The first 5 are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215660 | Dorzolamide Hydrochloride | Solution | Fosun Pharma USA Inc |
| ANDA204778 | Dorzolamide Hydrochloride Ophthalmic Solution | Solution/Drops | Micro Labs Limited |
| ANDA078395 | Dorzolamide Hydrochloride | Solution | Advagen Pharma Ltd. |
| ANDA202053 | Dorzolamide Hydrochloride Ophthalmic | Solution | Florida Pharmaceutical Products, LLC |
| ANDA078981 | Dorzolamide Hydrochloride | Solution/Drops | Sandoz Inc |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): diabetes mellitus, diabetic ketoacidosis, myasthenia gravis and other neuromuscular junction disease, hyperthyroidism (including Graves disease and thyrotoxicosis), hypoglycemia, atrioventricular block, pulmonary emphysema, bronchial disease, and anaphylaxis.
- **Pharmacological targets**: dorzolamide acts on carbonic anhydrase 1, 7, 12 and 14. No drug-drug interaction entries were returned.
- Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hereditary glaucoma has a very high model score and a plausible mechanism, but no clinical trials or publications support it (L5). All 9 US licenses are cancelled, so current availability is unclear. Separately, the open-angle glaucoma predictions have much stronger evidence (L1: Phase 3 and Phase 4 trials, systematic reviews). That evidence confirms the original indication rather than supporting new repurposing. The other predictions (alopecia, hypotrichosis, congestive heart failure, respiratory conditions) have no supporting mechanism or evidence.

**To proceed, the following is needed:**
- Clinical or literature evidence of IOP-lowering with dorzolamide in hereditary or primary congenital glaucoma. A Phase 2 pediatric glaucoma trial (NCT01527682) exists and could be reviewed for relevance.
- Confirmation of current US availability, since all listed ANDAs are cancelled. Other dorzolamide products and combinations (e.g., dorzolamide/timolol) should also be checked.
- Package insert warnings and contraindications, including sulfonamide hypersensitivity.
- Detailed mechanism-of-action data to strengthen the mechanistic-link analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

