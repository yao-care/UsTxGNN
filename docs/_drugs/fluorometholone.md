---
layout: default
title: Fluorometholone
parent: Model Prediction Only (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Fluorometholone
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

# Fluorometholone: From Uveitis and Ocular Inflammation to Postinfectious Vasculitis

## One-Sentence Summary

Fluorometholone is a topical ophthalmic corticosteroid, originally used to treat uveitis, iridocyclitis, conjunctivitis and related eye inflammation.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uveitis and other ocular inflammatory conditions (iridocyclitis, atopic/vernal conjunctivitis, corneal ulcer, among others). The market-authorization records compiled for this report contain no approved-indication text. |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all authorizations cancelled) |
| Number of NDAs | 4 (4 cancelled, 0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Fluorometholone is a synthetic corticosteroid that acts on the glucocorticoid receptor (NR3C1), giving it anti-inflammatory and immunosuppressive effects. Its recognized use is treating inflammatory conditions of the eye surface and anterior segment.

Corticosteroids are generally relevant to immune-mediated vasculitis, which is the basis of the model's prediction. However, there is an important practical barrier: fluorometholone is formulated only as an eye-drop suspension with low systemic penetration. Postinfectious vasculitis is a systemic disease, so a topical ocular product is unlikely to reach relevant exposure. The link is a model prediction only, with no clinical or literature support, and route compatibility with the new indication has not been established.

### Other Predicted Indications Worth Noting

The top-ranked prediction is weakly supported. Some lower-ranked predictions are more biologically plausible because they sit closer to the drug's known ocular use:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 6 | Punctate epithelial keratoconjunctivitis | 99.89% | L4 | The most plausible candidate. Two indirect papers were found, neither testing fluorometholone. Steroids may worsen some infections. |
| 9 | Lens-induced iridocyclitis | 99.82% | L4 | Effectively a subtype of an existing indication. Definitive treatment is usually surgical. |
| 10 | Glaucomatocyclitic crisis | 99.82% | L4 | Steroids are standard for the inflammation, and fluorometholone tends to raise eye pressure less than other steroids. IOP monitoring is essential. |
| 3 | Otitis externa | 99.90% | L5 | Mechanism plausible, but ear-canal use of an ophthalmic suspension is unvalidated. |

Ranks 2, 4, 5, 7 and 8 (post-bacterial disorder, infective urethral stricture, post-infectious syndrome, infection-related hemolytic uremic syndrome, Chagas cardiomyopathy) are systemic or non-specific conditions with no plausible exposure from a topical eye drop and no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for postinfectious vasculitis.

For reference, two indirect papers were retrieved for the rank-6 prediction (punctate epithelial keratoconjunctivitis). Neither tests fluorometholone efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Review | Indian Journal of Ophthalmology | Characterizes the sequelae of microsporidial keratoconjunctivitis and outlines its management |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Cohort | Journal of Current Ophthalmology | Uses anterior segment OCT to describe the phases of epidemic keratoconjunctivitis and the effect of topical steroid on its course |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019079 | Flarex (Harrow Eye, LLC) | Suspension/drops | Not available (cancelled) |
| NDA019216 | FML Forte (Allergan, Inc.) | Suspension/drops | Not available (cancelled) |
| NDA016851 | FML (Allergan, Inc.) | Suspension/drops | Not available (cancelled) |
| ANDA216348 | Fluorometholone ophthalmic suspension (Amneal Pharmaceuticals NY LLC) | Suspension/drops | Not available (cancelled) |

All four authorizations are listed as cancelled, so no currently valid US product was found in the compiled data.

---

## Safety Considerations

- **Disease-level cautions (from knowledge-graph contraindication links, not label text):** herpes simplex virus keratitis, viral/fungal/other eye infections, ocular tuberculosis, open-angle glaucoma, ocular hypertension, diabetes mellitus, diabetic ketoacidosis, porphyria and related porphyrin disorders, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, conjunctivitis (disease) and corneal pigmentation. These should be verified against the official label.
- **Drug Interactions:** The interaction screen returned 11 drug-pair entries, all with an unclassified severity level: doxycycline, salbutamol, cyclosporine, acetaminophen, digoxin, brimonidine, cephalexin, alendronic acid, acyclovir, diazepam and fenofibrate. Their clinical significance has not been graded.
- Steroid use in infection-related conditions (such as the infectious predictions above) needs caution, as steroids may worsen some infections.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for postinfectious vasculitis is supported only by a model score (L5), with no trials or publications. A topical eye drop is also unlikely to treat a systemic vasculitis, and all US authorizations are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing and blocking safety screening)
- Detailed mechanism-of-action data
- Evidence that a route and formulation can reach the target tissue for a systemic indication
- Consider redirecting the evaluation toward ocular-adjacent predictions (punctate epithelial keratoconjunctivitis, lens-induced iridocyclitis, glaucomatocyclitic crisis), which are better aligned with the drug's known use and could be framed as research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

