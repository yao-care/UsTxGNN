---
layout: default
title: Desonide
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
monitor_inn: "DESONIDE"
predicted_indications: ["polyp of vocal cord", "polyp of middle ear", "polyp of external auditory canal", "polyp of frontal sinus", "polyp of ureter", "polyp of vulva", "fibroepithelial polyp", "neoplastic polyp", "epulis", "uterine polyp"]
last_modified_at: 2026-10-30
description: "Desonide: predicted new indication Polyp of vocal cord (evidence level L5). Approved use: Not recorded in the local data"
---

# Desonide
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

## Desonide: Polyp of vocal cord
{: .text-alpha }

## One-Sentence Summary

Desonide is a low-potency topical corticosteroid, originally used for inflammatory and allergic conditions such as atopic dermatitis, contact dermatitis, and seborrheic dermatitis.
The TxGNN model predicts it may be effective for **polyp of vocal cord**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyp of vocal cord |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of FDA Applications | 13 authorizations in total (2 NDAs, 11 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, desonide is a low-potency topical glucocorticoid with anti-inflammatory activity. Its efficacy in inflammatory skin disease is established, and it may mechanistically be applicable to inflammation-driven lesions.

Vocal cord polyps are largely related to vocal trauma and chronic inflammation or edema, so a glucocorticoid effect is conceivable. This is the only link between the original indications and the predicted one.

There are significant practical obstacles. Desonide is marketed only as topical cream, ointment, lotion, and gel, and these are not suited to delivery to the larynx. No supporting data were found. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

### Other Predicted Indications

The model also ranked nine other polyp-type conditions with similar scores (0.9990–0.9991). None has clinical trials or literature, and all are rated L5 with a Hold recommendation.

| Rank | Predicted Indication | Score | Rationale Summary |
|----|------|------|------|
| 2 | Polyp of middle ear | 0.9991 | Arises from chronic middle ear inflammation; no otic desonide formulation; treatment is usually surgical |
| 3 | Polyp of external auditory canal | 0.9991 | Topical steroids are used for ear canal dermatitis, an indirect link only |
| 4 | Polyp of frontal sinus | 0.9991 | Steroids are established for sinonasal polyps, but with intranasal agents, not desonide |
| 5 | Polyp of ureter | 0.9990 | Benign lesions managed surgically; no plausible mechanism or delivery route |
| 6 | Polyp of vulva | 0.9990 | Topical application is feasible, but these lesions are treated by excision |
| 7 | Fibroepithelial polyp | 0.9990 | Benign connective tissue lesions; no anti-inflammatory regression expected |
| 8 | Neoplastic polyp | 0.9990 | Driven by oncogenic pathways; negligible systemic exposure from topical use |
| 9 | Epulis | 0.9990 | Reactive gingival overgrowth; standard care is excision |
| 10 | Uterine polyp | 0.9990 | Hormone-responsive lesions; hysteroscopic polypectomy is standard |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 13 authorizations are valid. The main ones are listed below; approved indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| NDA017426 | Desonide | Ointment | Padagis Israel Pharmaceuticals Ltd | Valid |
| NDA019048 | Desonide | Cream | Proficient Rx LP | Valid |
| ANDA073548 | Desonide | Cream | Northstar Rx LLC | Valid |
| ANDA213632 | Desonide | Lotion | Alembic Pharmaceuticals Limited | Valid |
| ANDA202470 | Desonide | Gel | Cintex Services, LLC | Valid |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not from label text):** The graph links desonide with potential contraindication or caution for hypertension, congestive heart failure, hyperglycemia, liver disease, gallbladder disease, epilepsy, and herpes simplex virus keratitis. It also flags measles, urea cycle disorders (such as citrullinemia, hyperargininemia, and carbamoyl phosphate synthetase I deficiency), and several pituitary and growth hormone deficiency conditions, including hypopituitarism and hypogonadotropic hypogonadism. These come from graph relationships and should be verified against the official label.

Please refer to the package insert for further safety information, including warnings, contraindications, and drug interactions. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and the available topical formulations are not suited to the predicted site of disease. Most predicted polyp conditions are managed surgically or with other established therapies.

**To proceed, the following is needed:**
- Mechanism of action data for desonide
- FDA package insert warnings and contraindications for safety screening
- Preclinical or clinical evidence that a corticosteroid affects vocal cord polyps
- A feasibility assessment of a delivery route suited to the larynx (for example, inhaled or injectable steroid formulations), since current topical products do not fit
- Comparison against established treatments (voice therapy, surgery, and other corticosteroids with proven laryngeal or intranasal use)
- Clarification of the regulatory status, given that 13 US authorizations are currently valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

