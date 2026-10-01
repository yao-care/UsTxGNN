---
layout: default
title: Peppermint Oil
parent: Model Prediction Only (L5)
nav_order: 1031
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From an Unspecified Original Indication to Leprosy

## One-Sentence Summary

Peppermint oil is marketed in the local dataset only as nail-care liquids and a patch, and no approved indication text is recorded.
The TxGNN model's top-ranked prediction is **leprosy** (score 99.8%), but it has **0 clinical trials** and **0 publications**, so it is a model output with no supporting evidence.
Among the top 10 predictions, only **cardiovascular disease** (rank 9) has human data: **2 relevant small completed trials** and **1 published RCT protocol**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (all license records have empty indication text) |
| Predicted New Indication | Leprosy (rank 1). Best-supported alternative: cardiovascular disease (rank 9) |
| TxGNN Prediction Score | 99.80% (leprosy); 99.13% (cardiovascular disease) |
| Evidence Level | L5 (leprosy); L3 (cardiovascular disease) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold (leprosy); Research Question (cardiovascular disease) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for peppermint oil. The local licenses list no approved indication, so no original-to-new indication relationship can be drawn.

**Leprosy:** There is no identifiable mechanistic link. Peppermint oil shows some general in vitro antimicrobial activity, but nothing specific to *Mycobacterium leprae*. The score of 0.998 has no clinical or literature backing and probably reflects a graph-structure artifact.

**Other top-10 predictions:** Pneumocystosis and echinococcosis have no mechanistic support beyond generic essential-oil antimicrobial activity. The four polyp predictions (vocal cord, uterine, middle ear, frontal sinus) have near-identical scores, which points to a shared "polyp" node artifact rather than a disease-specific signal. Coronary artery disease and myocardial ischemia are indirect, hypothetical links through vasodilation and autonomic modulation.

**Cardiovascular disease (the exception):** The link is plausible but unconfirmed. Menthol may relax vascular smooth muscle through calcium-channel modulation and TRPM8 activation. A human physiology study also found that gastric cooling with menthol increased cardiac parasympathetic efferent activity. Two small human trials in hypertension and cardiometabolic outcomes support a signal, but no Phase 2/3 RCT exists.

---

## Clinical Trial Evidence

There are no registered trials for leprosy. The trials below were matched to the cardiovascular disease prediction (rank 9).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | N/A | Completed | 40 | Peppermint oil in mild-moderate hypertension with cardiometabolic outcomes; directly relevant but small (grade A) |
| [NCT05071833](https://clinicaltrials.gov/study/NCT05071833) | N/A | Completed | 36 | Oral peppermint on cardiometabolic parameters; addresses risk markers, not clinical cardiovascular endpoints (grade B) |
| [NCT04966546](https://clinicaltrials.gov/study/NCT04966546) | Early Phase 1 | Withdrawn | 0 | Spreading depolarization after chronic subdural hematoma surgery; neurosurgical, no cardiovascular data (grade C) |

---

## Literature Evidence

There is no literature for leprosy. The publications below relate to the cardiovascular disease prediction (rank 9). Formulation studies of other drugs (PMIDs 39139335, 28889028) and a breath-analysis method paper (PMID 27277875) were excluded because they contain no peppermint oil efficacy data.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT (protocol) | PloS one | Placebo-controlled trial protocol of peppermint oil in pre- and stage 1 hypertension; appears to correspond to NCT05561543. Results not reported |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Human physiology study | Experimental physiology | Gastric cooling and menthol increased cardiac parasympathetic efferent activity in healthy volunteers |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Review | Explore (New York, N.Y.) | Brief research digest covering peppermint oil for irritable bowel syndrome among other topics; not cardiovascular |
| [17577363](https://pubmed.ncbi.nlm.nih.gov/17577363/) | 2007 | Case report | Contact dermatitis | Allergic contact dermatitis to a peppermint foot spray (safety signal only) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M005 | Gray Nail Essence Oil | Liquid | Not stated |
| M005 | Fungal Nails Repairing Essence | Liquid | Not stated |
| M029 | Gray Nail Essence Oil | Liquid | Not stated |
| No number recorded | iShanCare | Patch | Not stated |

The dataset lists 7 licenses in total. The table shows the distinct products among the 5 records provided, and the M005 Gray Nail Essence Oil record appears twice with identical content. All are topical or other-route forms, and none is an oral cardiovascular product.

---

## Safety Considerations

- **Allergy signal:** A case report documents allergic contact dermatitis from a peppermint foot spray (PMID 17577363).

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold (leprosy); Research Question (cardiovascular disease)**

**Rationale:**
The leprosy prediction has no clinical, literature, or mechanistic support and is most likely a graph artifact. Cardiovascular disease is the only top-10 candidate with human data, but the evidence is limited to two small non-phased trials and one RCT protocol.

**To proceed, the following is needed:**
- Published results of NCT05561543 and NCT05071833, including blood pressure and lipid outcomes
- A Phase 2 RCT in hypertension with clinical endpoints, if the results are positive
- Mechanism of action data for peppermint oil
- Package insert warnings and contraindications, which currently block safety screening
- Dose, route, and formulation confirmation, since the marketed products are topical and the cardiovascular trials used oral peppermint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

