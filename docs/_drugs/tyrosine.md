---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 1273
evidence_level: L5
indication_count: 10
monitor_inn: "TYROSINE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "aqueous misdirection", "traumatic glaucoma", "neovascular glaucoma"]
last_modified_at: 2026-10-28
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not available"
---

# Tyrosine
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

## Tyrosine: From an Unspecified Original Indication to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Tyrosine is an amino acid and a precursor of catecholamines and thyroid hormones. No approved indication is recorded for it in the data compiled for this report.
The TxGNN model ranks **Cauda Equina Syndrome** as its top prediction, but this is a model signal only, with **0 clinical trials** and **0 publications** behind it.
Across all ten predicted indications, only **1 clinical trial** (for hyperthyroidism, testing a multi-ingredient supplement) was found. The literature is mostly background reviews and does not test tyrosine as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only license on record has no approved indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is known as a precursor of dopamine and norepinephrine (catecholamines) and as a building block of thyroid hormones, but no original indication is documented for it here.

For cauda equina syndrome, no mechanistic link has been established. It is a compressive injury to the lumbosacral nerve roots, and there is no plausible pathway from tyrosine to its treatment. The high score (0.9977) is a prediction-only signal with no clinical or literature support.

Other predictions look no stronger on mechanism:
- **Hyperthyroidism and hyperthyroxinemia:** Tyrosine is a substrate for thyroid hormone synthesis, so supplementation is biologically implausible as a treatment and could theoretically be counterproductive.
- **Resistance to thyroid hormone (THRB mutation):** This is a receptor defect that a hormone precursor would not correct.
- **Postural orthostatic tachycardia syndrome (POTS):** This is the most biologically coherent link, since catecholamines are relevant to autonomic dysregulation. Its only evidence is a case report on alpha-methyl-p-tyrosine, which inhibits tyrosine hydroxylase and acts opposite to tyrosine. It is therefore classed as a research question, not a supported indication.
- **Neurogenic bladder (obsolete term):** Catecholamine signaling could in theory affect bladder autonomic control. The disease term is flagged as obsolete and should be mapped to a current term.
- **Glaucoma types and aqueous misdirection:** No tyrosine-specific evidence and no evident connection to tyrosine metabolism.

## Clinical Trial Evidence

For the top-ranked indication (cauda equina syndrome), currently no related clinical trials are registered.

The only trial found across the predicted indications relates to rank 4, hyperthyroidism:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Randomized, double-blind, placebo-controlled trial of a zinc, selenium and L-tyrosine supplement to prevent thyrotoxicosis in adults with elevated TPOAb and the SEPP1 r25191G/A polymorphism. It does not isolate tyrosine, so it gives no direct evidence for it. |

## Literature Evidence

For the top-ranked indication (cauda equina syndrome), currently no related literature is available.

Selected publications retrieved for lower-ranked predictions, none testing tyrosine as an intervention:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome patient responded to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor (POTS prediction). This is indirect, anecdotal, and opposite in mechanism to tyrosine. |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | Plasma amino acid alterations in early primary angle-closure glaucoma. This is an association study, not a treatment test. |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism causes, diagnosis and management. |
| [30886364](https://pubmed.ncbi.nlm.nih.gov/30886364/) | 2019 | Review | Nat Rev Endocrinol | Role of thyroglobulin tyrosine iodination in thyroid hormone synthesis (mechanistic background). |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Preclinical | Endocrinology | Serine 314 mutations in the thyroid hormone beta receptor impair ligand binding (resistance to thyroid hormone). |
| [19169471](https://pubmed.ncbi.nlm.nih.gov/19169471/) | 2008 | Case report | Arq Bras Endocrinol Metabol | E449X THRB mutation with autoimmune thyroid disease and neuropsychomotor involvement. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma etiopathogenesis and treatment. No tyrosine evidence. |
| [22568104](https://pubmed.ncbi.nlm.nih.gov/22568104/) | 2012 | Review | Nippon Ganka Gakkai Zasshi | Review of glaucoma care and angle-closure screening. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | L-Tyrosine (Professional Complementary Health Formulas) | Liquid | Not specified (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, cauda equina syndrome, is supported only by the model score, with no trials, no literature, and no plausible mechanism. The same is true of the other predictions, and several (hyperthyroidism, hyperthyroxinemia, THRB resistance) run against known biology. The only drug license on record is cancelled. POTS is the sole prediction that merits follow-up, as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Safety information from the package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- A documented original indication and active regulatory status
- A mechanistic rationale for cauda equina syndrome, or a decision to deprioritize it
- Mapping of the obsolete neurogenic bladder term to a current disease term
- For POTS, direct evidence on tyrosine itself (preclinical or small clinical studies) before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

