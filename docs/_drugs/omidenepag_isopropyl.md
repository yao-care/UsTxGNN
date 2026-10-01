---
layout: default
title: Omidenepag Isopropyl
parent: Model Prediction Only (L5)
nav_order: 994
evidence_level: L5
indication_count: 7
---

# Omidenepag Isopropyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Omidenepag Isopropyl: From Glaucoma / Ocular Hypertension to Pancreatitis

## One-Sentence Summary

Omidenepag isopropyl is a topical ophthalmic prodrug of a selective EP2 receptor agonist, marketed in the US as Omlonti for glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **pancreatitis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (drug-class knowledge; the license record has no indication text) |
| Predicted New Indication | Pancreatitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omidenepag isopropyl is a prodrug of a selective EP2 receptor agonist. EP2 activation raises intracellular cAMP. The drug is approved as an eye drop to lower intraocular pressure.

Prostanoid signaling has been discussed in inflammation, which is the only loose conceptual link to pancreatitis. The supplied data contains no direct evidence connecting EP2 agonism to pancreatitis. Because the drug is applied to the eye, systemic exposure is very low, so it is unlikely to reach the pancreas at meaningful levels. The high score (0.998) therefore reflects knowledge-graph topology rather than demonstrated biology.

The other six predictions are weaker still, and all are L5 with no trials or literature:

- **Hyperphosphatemia:** no plausible link to EP2 agonism.
- **Esophageal varices (with and without bleeding):** identical scores, so likely a duplicate. Portal hypertension is not obviously modulated by EP2 agonism.
- **Blepharospasm:** the only anatomically plausible one, but it is a centrally driven focal dystonia of skeletal muscle. EP2-mediated smooth muscle relaxation does not address it.
- **Familial visceral myopathy:** smooth muscle relaxation could be counterproductive in a hypomotility disorder.
- **Alcoholic cardiomyopathy:** EP2 has been studied in cardiac remodeling preclinically, but nothing links this drug to alcohol-induced injury.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA215092 | Omlonti (Ocuvex Therapeutics, Inc.) | Solution / drops | Indication text not provided in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it and no supported mechanistic link. The topical ocular route also gives very low systemic exposure, so the high TxGNN score is not enough to justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data, to test whether EP2 signaling is relevant to pancreatic inflammation
- Preclinical or observational evidence linking EP2 agonism to pancreatitis
- An assessment of route compatibility, since a systemic formulation would be needed to reach a non-ocular target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

