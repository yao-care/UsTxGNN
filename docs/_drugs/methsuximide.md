---
layout: default
title: Methsuximide
parent: Model Prediction Only (L5)
nav_order: 914
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "METHSUXIMIDE"
predicted_indications: ["insomnia (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "sleep disorder, initiating and maintaining sleep", "nephrogenic diabetes insipidus", "restless legs syndrome", "trichotillomania", "Wernicke-Korsakoff syndrome"]
description: "Methsuximide: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Methsuximide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Methsuximide: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Methsuximide is a succinimide anticonvulsant, originally used to treat epilepsy and absence epilepsy.
The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials** and **no publications** currently support this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |


## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacological knowledge, methsuximide is a succinimide anticonvulsant thought to act mainly by inhibiting T-type calcium channels in thalamic neurons. These channels help shape thalamocortical rhythms and sedation, so an effect on sleep is plausible.

However, no direct link between methsuximide and insomnia is documented. The high score (0.9997) is a computational prediction only. A closely related prediction, "sleep disorder, initiating and maintaining sleep" (score 0.9970), relies on the same speculative hypothesis and likewise has no trials or literature.

Other top-ranked predictions are weaker or not credible:
- **Nephrogenic syndrome of inappropriate antidiuresis and nephrogenic diabetes insipidus:** these involve vasopressin-pathway defects (AVPR2/AQP2), and methsuximide has no known action there.
- **Childhood absence epilepsy susceptibility and familial mesial temporal lobe epilepsy:** these are extensions of the existing anticonvulsant use rather than true repurposing, and no supporting studies were found.
- **Acute encephalopathy with biphasic seizures:** the rationale is indirect, and no trials or literature exist.
- **Wernicke-Korsakoff syndrome:** caused by thiamine deficiency, with no mechanistic connection to methsuximide.
- **Trichotillomania:** no direct mechanistic rationale.
- **Restless legs syndrome:** see the literature section below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the lead prediction (insomnia). The only publication found among the top 10 predictions concerns restless legs syndrome (rank 7):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3145164](https://pubmed.ncbi.nlm.nih.gov/3145164/) | 1988 | Case report/series | Clinical Neurology and Neurosurgery | Two patients with complex partial and secondarily generalized seizures developed restless legs while taking methsuximide and phenytoin. This reports an association with the drugs, not a benefit, so it does not support efficacy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217213 (cancelled) | Methsuximide (ANI Pharmaceuticals) | Capsule | Not stated in the available records |
| NDA010596 (cancelled) | Celontin (Parke-Davis, Pfizer) | Capsule | Not stated in the available records |

## Safety Considerations

- **Key Warnings and Contraindications:** Label-based warnings and contraindications were not available. Please refer to the package insert for safety information.
- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, systemic lupus erythematosus (including pediatric), neutropenia, agranulocytosis, and acute intermittent porphyria. These should be verified against the official label.
- **Drug Interactions:** 48 interactions were identified, all of the ones shown being Moderate severity. Main examples:
  - CNS depressants and opioids: morphine (including liposomal), codeine, hydrocodone, opium
  - Cannabinoids: dronabinol, nabilone
  - Sedating antihistamines and related drugs: promethazine, chlorpheniramine, cetirizine, azelastine (nasal)
  - Antimalarials: chloroquine, mefloquine, hydroxychloroquine
  - Folate products: folic acid, leucovorin, levoleucovorin
  - Others: metoclopramide, sibutramine, ethanol

  The CNS-depressant interactions matter particularly for a sleep indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by a model score, with no clinical trials or literature (Evidence Level L5). The mechanistic link is speculative.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data (for example, from DrugBank)
- Preclinical or early clinical evidence of methsuximide's effect on sleep
- Review of the sedation and CNS-depressant interaction risks in a sleep population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

