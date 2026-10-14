---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 1038
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Phenol: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Phenol is an antiseptic and protein-denaturing agent, listed in the knowledge graph for dermatitis and sold in the US in sore throat sprays, homeopathic pellets and pain-relieving salves.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available on the US product records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, phenol is an antiseptic with protein-denaturing properties, and it has been used on skin and mucosa. The knowledge graph links it to dermatitis, which likely explains why skin-related diseases score highly.

Acrodermatitis chronica atrophicans is the late skin stage of *Borrelia* infection (Lyme disease) and is treated with systemic antibiotics. No plausible role for topical phenol has been established. The high score (rank 1879 among all predictions) is a network-based association rather than a mechanistic or clinical finding, so it should be treated as a hypothesis only.

Other predictions fall into two groups:
- **Skin and immune-related diseases, with no supporting evidence:** neonatal dermatomyositis, amyopathic dermatomyositis, familial hydroa vacciniforme, and childhood connective-tissue-disease-associated interstitial lung disease. All are Hold. Phenol has no known immunomodulatory mechanism, and neonatal or inhaled exposure raises toxicity concerns.
- **Acne keloid (score 99.94%):** this is the only prediction with a plausible link. Phenol is used as a chemical peeling agent that causes controlled dermal injury and remodeling. This is indirect evidence only, and the one supporting report concerns acne scars rather than acne keloid.

Severe nonproliferative diabetic retinopathy (99.46%) and dry eye syndrome (99.04%) are also Hold. Phenol is neurolytic, cytotoxic and irritating to the eye, so these uses are unfavorable.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications are available for the top-ranked prediction. The closest supporting item is for the fifth-ranked prediction, acne keloid:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Uncontrolled clinical report (design not confirmed) | The Journal of Dermatology | Evaluated a modified phenol peel (Exoderm) for facial wrinkles, acne scars and other skin problems in Asian patients. The formulation was designed to reduce side effects such as arrhythmia, long-lasting erythema, hypopigmentation, hypertrophic scar and keloid. |

For dry eye syndrome (rank 8), 20 publications were retrieved, but none involve phenol. They concern dry eye biology and other compounds such as berberine, evodiamine and chrysin, so they are not evidence for phenol.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M022 (cancelled) | CVS Sore Throat | Spray | Not listed |
| nan (cancelled) | Carbolicum acidum | Pellet | Not listed |
| M017 (cancelled) | Pain Relieving | Salve | Not listed |

All three authorizations are cancelled, and no valid product is currently on the US market.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): epilepsy, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, sudden cardiac arrest, heart conduction disease, atrioventricular block, respiratory failure, peripheral vascular disease, appendicitis, active peptic ulcer disease, cancer and lymphoma, herpes simplex, herpes zoster, cytomegalovirus infection, anogenital HPV infection, common wart, and progressive multifocal leukoencephalopathy.
- **Context-specific concerns noted in the prediction review:** phenol is caustic and toxic, so systemic, inhaled, ocular or neonatal exposure raises safety concerns. Phenol peels have been associated with arrhythmia and hypopigmentation.

Please refer to the package insert for label warnings and contraindications. No drug interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, acrodermatitis chronica atrophicans, rests on a network score alone, with no trials or literature and no plausible mechanism. The drug has no active US authorization, and safety data are limited.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data
- For acne keloid, the only plausible lead: a review of the study design and results of the 2007 modified phenol peel report, and a literature search for controlled studies on scars or keloids
- Confirmation of an appropriate route and formulation, since route compatibility has not been assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

