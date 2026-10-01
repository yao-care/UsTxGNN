---
layout: default
title: Metyrapone
parent: Model Prediction Only (L5)
nav_order: 922
evidence_level: L5
indication_count: 10
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

# Metyrapone: From Adrenal Cortisol Inhibition to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Metyrapone is an oral drug that blocks cortisol production in the adrenal gland (11-beta-hydroxylase inhibition), and it is marketed in the US as Metopirone.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but this rests on the model score alone.
There are **0 clinical trials** and **0 publications** for this indication, so the prediction is not yet supported by evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory record (the drug's known action is inhibition of adrenal cortisol synthesis) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% (model rank 1807) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 listings (both under NDA012911, from two manufacturers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available. Metyrapone is known to inhibit adrenal 11-beta-hydroxylase (CYP11B1), which lowers cortisol. Malignant hyperthermia is a different kind of disease. It is mainly a disorder of calcium handling in skeletal muscle, driven by variants in genes such as RYR1 and CACNA1S.

**No clear mechanistic link was found.** Cortisol synthesis inhibition is not a recognized way to modulate this pathway. The high score most likely reflects the knowledge graph placing malignant hyperthermia, related muscle diseases and hyperthermia phenotypes close together. It does not reflect a demonstrated pharmacological rationale.

The same pattern appears across the other top predictions. Most are RYR1-related myopathies or malignant hyperthermia variants, including malignant hyperthermia susceptibility, King-Denborough syndrome, central core myopathy and centronuclear myopathy. All are Level L5 with no trials or literature. Together they look like one cluster of graph-derived predictions rather than ten independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for exercise-induced malignant hyperthermia.

One lower-ranked prediction, **familial periodic paralysis** (rank 8, score 99.40%, Level L4), did return two old papers. They are listed below for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Clinical physiology study | J Clin Invest | In one patient with hyperkalemic periodic paralysis, paralysis was induced by potassium chloride, corticotropin and several glucocorticoids. It was not induced by mineralocorticoids or by ACTH plus metyrapone. Metyrapone appears to have been used as a physiological probe, not as a treatment. |
| [4301626](https://pubmed.ncbi.nlm.nih.gov/4301626/) | 1968 | Case report / small case series | Eur Neurol | Primary periodic paralysis with hyperkalemic and hypokalemic attacks and hemolytic bilirubinemia. No abstract is available, and the relevance to metyrapone is unconfirmed. |

Neither paper shows a therapeutic effect. A full-text review is needed before drawing any conclusion.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA012911 | Metopirone | Capsule, gelatin coated (oral) | ESTEVE Pharmaceuticals, S.A. |
| NDA012911 | Metopirone | Capsule, gelatin coated (oral) | HRA Pharma Rare Diseases |

The record does not include approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the queried source. Because metyrapone lowers cortisol, any speculative use raises the concern of adrenal insufficiency and electrolyte disturbance, such as low potassium. This concern comes from the pharmacology of the drug, not from a retrieved label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature and no plausible mechanism linking cortisol synthesis inhibition to malignant hyperthermia. It is best treated as a likely graph-proximity artifact.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), since safety screening cannot start without it
- Detailed mechanism of action data from DrugBank
- A targeted literature search covering metyrapone with RYR1 and calcium-handling biology, and a full-text review of the two periodic paralysis papers
- If the team wants to pursue this direction, a preclinical mechanistic study before any clinical consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

