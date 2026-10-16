---
layout: default
title: Metyrapone
parent: Model Prediction Only (L5)
nav_order: 922
evidence_level: L5
indication_count: 10
monitor_inn: "METYRAPONE"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
last_modified_at: 2026-10-14
description: "Metyrapone: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not stated in the US license data. Pharmacology sources describe use…"
---

# Metyrapone
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

# Metyrapone: From a Diagnostic and Cushing's Syndrome Agent to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Metyrapone is an oral inhibitor of cortisol synthesis, used as a diagnostic test of hypothalamic-pituitary function and occasionally to treat Cushing's syndrome.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but **no clinical trials and no publications** support this prediction.
The prediction rests on computational network proximity only, and no biological rationale was identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data. Pharmacology sources describe use as a diagnostic test of hypothalamic-pituitary function and occasional use in Cushing's syndrome |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Pharmacology data show that metyrapone targets CYP11B1 (11-beta-hydroxylase) and CYP11B2 (aldosterone synthase). Inhibiting these enzymes reduces cortisol synthesis, which explains its use in Cushing's syndrome and in testing pituitary-adrenal function.

The predicted indication is mechanistically unrelated to this action. Malignant hyperthermia is a disorder of skeletal muscle calcium handling, mainly involving RYR1 and CACNA1S. Its acute treatment is dantrolene, which acts directly on the ryanodine receptor. No plausible link between steroidogenesis inhibition and this pathway was identified.

The high TxGNN score most likely reflects proximity in the knowledge graph to a cluster of related myopathy nodes rather than biological rationale. This prediction should be treated as a computational hypothesis, not a supported lead.

### Other Predicted Indications

Nine other predictions were reviewed, and all lack clinical trials. Most are RYR1-related or other congenital myopathies, with no mechanistic link to metyrapone.

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|---|---|---|---|
| 2 | Malignant hyperthermia, susceptibility to | 99.82% | L5 |
| 3 | King-Denborough syndrome | 99.77% | L5 |
| 4 | Central core myopathy | 99.72% | L5 |
| 5 | Moderate multiminicore disease with hand involvement | 99.72% | L5 |
| 6 | Congenital multicore myopathy with external ophthalmoplegia | 99.70% | L5 |
| 7 | Myopathy, centronuclear | 99.47% | L5 |
| 8 | Familial periodic paralysis | 99.40% | L4 |
| 9 | Renal tubular acidosis | 99.28% | L5 |
| 10 | Malignant hyperthermia of anesthesia | 99.23% | L5 |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (exercise-induced malignant hyperthermia), currently no related literature is available.

The only publication identified across the ten predictions concerns the rank 8 prediction, familial periodic paralysis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Mechanistic/physiological study | The Journal of Clinical Investigation | In a 19-year-old man with hyperkalemic periodic paralysis, attacks were induced by potassium chloride, corticotropin-gel and several glucocorticoids, but not by mineralocorticoids or by ACTH-gel plus metyrapone. This is a mechanistic observation, not evidence of therapeutic efficacy. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA012911 | Metopirone (ESTEVE PHARMACEUTICALS, S.A.) | Capsule, gelatin coated (oral) | Not stated in the license data. Status: cancelled |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease edges in the TxGNN knowledge graph, not label text): Addison disease, chronic primary adrenal insufficiency, adrenal insufficiency, adrenocortical insufficiency, congenital adrenal hyperplasia, familial glucocorticoid deficiency, X-linked adrenal hypoplasia congenita, familial adrenal hypoplasia with absent pituitary luteinizing hormone, and inherited isolated adrenal insufficiency due to partial CYP11A1 deficiency. These are consistent with the drug's cortisol-lowering action.
- **Drug interactions**: 10 interactions rated Moderate were found, with estrogens (ethinylestradiol, estradiol, conjugated estrogens, mestranol, esterified estrogens, estrone sulfate, and topical estradiol, conjugated estrogens and estrone sulfate) and with cyproheptadine. Pharmacology records also list CYP11B1 and CYP11B2 as targets.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry or literature support and no plausible mechanism. Metyrapone's CYP11B1 inhibition is unrelated to the RYR1-driven calcium dysregulation underlying malignant hyperthermia. The US license is also cancelled, and adrenal-insufficiency-related safety signals add concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- A biological hypothesis connecting steroidogenesis inhibition to muscle calcium handling, supported by preclinical data
- Confirmation of the original approved indication from the license record
- Route and similarity-to-original assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

