---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 953
evidence_level: L5
indication_count: 10
monitor_inn: "NAPHAZOLINE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-10-14
description: "Naphazoline: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not stated in the US license records"
---

# Naphazoline
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

# Naphazoline: From Ocular/Nasal Decongestion to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is a topical alpha-adrenergic vasoconstrictor, used to temporarily relieve eye redness and nasal congestion.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on knowledge-graph proximity alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; pharmacology data describes use for reducing eye redness |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on pharmacology records, naphazoline binds alpha-1A, alpha-2A and alpha-2C adrenoceptors, and it is used as a vasoconstrictor that narrows swollen blood vessels, for example to reduce eye redness.

The prediction is difficult to justify mechanistically. No plausible link has been established between an alpha-adrenergic vasoconstrictor and hair follicle biology or the genetic basis of hypotrichosis simplex (for example CDSN, APCDD1 or RPL21 variants). Vasoconstriction is also the opposite of the vasodilator-based approach of hair growth agents such as minoxidil.

The high score is a graph-based prediction only. The other top-ranked predictions (other hair disorders, including both hypotrichosis and hypertrichosis, as well as unrelated congenital malformation syndromes) suggest the model is reflecting network topology rather than biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

For context, the only publication retrieved across the top ten predictions concerns open-angle glaucoma (rank 8): [PMID 1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) (1992, Australian and New Zealand Journal of Ophthalmology) examined topical corticosteroids and laser-induced peripheral anterior synechiae after argon laser trabeculoplasty. It does not evaluate naphazoline and is not direct evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 (cancelled) | SERYNTH FAST RELIEF NASAL | Spray | Not stated |
| M018 (cancelled) | Sato Clear | Solution/drops | Not stated |
| part341 (cancelled) | Pi Yuan Chin | Solution/drops | Not stated |

## Safety Considerations

- **Target pharmacology**: Naphazoline acts on alpha-1A, alpha-2A and alpha-2C adrenoceptors (human). A mouse trace amine receptor (Taar4) is also listed. No drug-drug interaction levels were reported.
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): hypertension and hypertensive disorder, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, angle-closure (closed-angle) glaucoma, cardiovascular and heart disease, hyperthyroidism, Graves disease, thyrotoxicosis, eye infectious disease, and conjunctivitis.
- Relevant to the glaucoma predictions: as a nonselective alpha agonist, naphazoline may cause mydriasis, which could precipitate angle closure.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are supported only by model scores, with no clinical trials and no relevant publications. For the top prediction, there is no mechanistic basis, and the drug's vasoconstrictive action may even work against hair growth. The product also has no currently valid US license.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to allow mechanistic-link analysis
- A credible biological rationale linking alpha-adrenergic agonism to hair follicle or the other predicted conditions
- Any preclinical or clinical evidence for naphazoline in the predicted indication
- Route and formulation compatibility assessment (current forms are nasal spray and ophthalmic drops, not scalp-appropriate)
- Consideration of whether the glaucoma predictions (ranks 5 and 8) merit review, given the angle-closure risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

