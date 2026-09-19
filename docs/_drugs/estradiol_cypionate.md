---
layout: default
title: Estradiol Cypionate
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Estradiol Cypionate
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

# Estradiol Cypionate: From Treatment of Estrogen Deficiency Symptoms to Potential Adjunctive Therapy for BPES-Related Premature Ovarian Insufficiency

## Summary

Estradiol cypionate is a long-acting estrogen ester (intramuscular injection formulation) known pharmacologically for hormone replacement therapy in estrogen deficiency-related symptoms (menopausal vasomotor symptoms, hypogonadism, primary ovarian insufficiency); this drug is Not marketed in Taiwan, with no TFDA-approved indication data available for comparison.

TxGNN yielded a total of 10 candidate new indications for this drug, but upon individual mechanism-of-action review, 8 of them (symptomatic form of fragile X syndrome, 4 chromosomal trisomy/tetrasomy syndromes, ovarian remnant syndrome, blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement, partial autosomal trisomy/tetrasomy, luteoma of pregnancy) **were determined to be knowledge graph proximity-based link artifacts**, lacking rational mechanisms and supported by 0 trials and 0 publications; another 1 item (anovulation) has 41 trials and 3 publications, but the direction is opposite to the therapeutic goal (estrogen inhibits ovulation rather than inducing ovulation, and the attached publication even concludes that estradiol cypionate "prolongs" the postpartum anovulation period in cattle).

This report focuses on **the only candidate with mechanism-of-action consistency: Blepharophimosis-Epicanthus Inversus-Ptosis (BPES)** (TxGNN score 99.59%, rank 10311). BPES type I is caused by *FOXL2* gene mutations; this gene is also expressed in ovarian granulosa cells, and mutations lead to abnormal follicle development and premature ovarian insufficiency (POI); hormone replacement therapy with estrogen is already standard clinical management in POI patients, consistent with this drug's original pharmacological use. However, **the dataset currently contains no direct trials or publications supporting this link**, belonging to the level of mechanism-based inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original use | Hormone replacement therapy for estrogen deficiency-related symptoms (known pharmacological use; this drug is not marketed in Taiwan, with no TFDA-approved indication text) |
| Predicted new indication | Blepharophimosis-Epicanthus Inversus-Ptosis (BPES)-related premature ovarian insufficiency |
| TxGNN prediction score | 99.59% |
| Evidence level | L4 (mechanism-based/theoretical inference, without direct clinical evidence) |
| Taiwan market status | Not marketed |
| Number of Taiwan drug approvals | 0 |
| Recommended decision | Hold |

---

## Why is This Prediction Worth Attention?

Currently, there is no detailed DrugBank MOA data (Data Gap). Based on known pharmacological information, estradiol cypionate belongs to long-acting estrogen esters, with its mechanism of action being the activation of estrogen receptors, used clinically to supplement endogenous estrogen insufficiency.

BPES is divided into two types: type I, in addition to the triad of narrow palpebral fissures, epicanthus inversus, and ptosis, is associated with POI; type II shows no reproductive manifestations. Published literature confirms that *FOXL2* gene, besides determining eyelid development, is also a key transcription factor in ovarian granulosa cell differentiation and follicle maintenance, and its mutations accelerate follicle depletion, leading to POI (PMID 29378385, 31366388, not included in this Evidence Pack, requiring separate verification of citation details). Regardless of the underlying etiology, standard treatment in POI patients includes estrogen supplementation to control vasomotor symptoms and protect bone and cardiovascular systems—this is mechanistically consistent with this drug's original pharmacological use (treatment of estrogen deficiency symptoms).

In other words, what TxGNN found is not "a drug for BPES," but rather the existing clinical logic between "the subpopulation of BPES patients with concurrent POI" and "estrogen replacement therapy." This is an indirect but mechanistically sound pathway, distinct from the other 8 candidates determined to be link artifacts.

---

## Clinical Trial Evidence

Currently no relevant clinical trial registrations.

---

## Literature Evidence

Currently no relevant literature data.

---

## Safety Considerations

Currently there is no available package insert warning, contraindications, or drug interaction data; please refer to package insert safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**

BPES type I with concurrent POI is a known pathophysiological pathway; estrogen supplementation has clinical rationale in this population; however, this candidate is the only one among TxGNN's high-scoring predictions with a defensible mechanism, and the dataset still contains no direct clinical trial or literature evidence to support it, and the score itself (99.59%) is close to the other 8 candidates already determined to be artifacts, indicating that the score itself cannot distinguish true signal from noise.

**To proceed, the following gaps must be filled:**

- Complete DrugBank MOA data (DG002, High severity)
- TFDA/manufacturer package insert warnings and contraindications (DG001, Blocking severity, currently Cannot proceed to S1 safety screening)
- Direct verification of POI prevalence in BPES type I patients and evidence for estrogen supplementation therapy (currently only mechanism-based inference; PMID 29378385, 31366388 have not been verified through this Evidence Pack collection process)
- Confirm the formulation applicability of estradiol cypionate (intramuscular injection formulation) in long-term POI hormone replacement therapy, and clarify its clinical role compared to conventional oral/patch estrogen preparations

**Management of the remaining 9 candidate indications:**

- Anovulation (rank 6): mechanism direction is opposite to the therapeutic goal, advancement not recommended, Hold.
- Fragile X-related symptoms, 4 chromosomal trisomy/tetrasomy syndromes, ovarian remnant syndrome, BPES due to 3q23 rearrangement, partial autosomal trisomy/tetrasomy, luteoma of pregnancy (total 8 items): determined to be KG proximity-based link artifacts, evidence level L5, Hold, further resource investment for verification not recommended.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

