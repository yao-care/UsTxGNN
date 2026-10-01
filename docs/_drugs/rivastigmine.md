---
layout: default
title: Rivastigmine
parent: Model Prediction Only (L5)
nav_order: 1131
evidence_level: L5
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Rivastigmine: From Alzheimer's-Type Dementia to Glaucoma

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor, generally known for treating dementia (this comes from general knowledge, since the supplied record lists no original indication).
The TxGNN model predicts it may be effective for **glaucoma**, but the support is thin: **0 clinical trials** and **3 publications**, only one of which tests the drug itself, and that was in rabbits.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record (generally known: dementia associated with Alzheimer's and Parkinson's disease) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 (preclinical only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the record counts NDAs and ANDAs together) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not in the supplied record. Rivastigmine is generally known to inhibit acetylcholinesterase and butyrylcholinesterase, which raises acetylcholine levels. This attribution comes from general knowledge, not from the record.

Elevated acetylcholine is a plausible route to lower intraocular pressure (IOP), the main modifiable risk factor in glaucoma. Cholinergic agents such as pilocarpine and physostigmine are established IOP-lowering drugs that increase aqueous humor outflow through the trabecular meshwork. Rivastigmine acts on the same cholinergic system, so the prediction is biologically sensible.

The link has limits. The only direct evidence is a 2000 study of **topical** rivastigmine in normotensive rabbits. The marketed products are oral capsules and transdermal patches, so it is unknown whether they deliver enough drug to the eye. No human data were provided. The high TxGNN score is a computational output and does not count as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical animal study (rabbit) | J Ocul Pharmacol Ther | Tested topical rivastigmine, a selective carbamate-type AChE inhibitor, for IOP reduction in normotensive rabbits. The title reports that it lowered IOP. This is the only study that tests the drug directly. |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review (patent literature) | Expert Opin Ther Pat | Reviews acetylcholinesterase inhibitors and reactivators. It notes that mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis and glaucoma. Class-level support only. |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Systems genetics / computational mechanistic study | Front Mol Biosci | Examines how muscarinic receptor signaling in the anterior eye regulates IOP. It notes that FDA-approved M3 agonists are limited by systemic cholinergic side effects. Indirect support. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022083 | Exelon | Extended-release patch | Sandoz Inc |
| ANDA209063 | Rivastigmine Transdermal System | Extended-release patch | Breckenridge Pharmaceutical, Inc. |
| ANDA206318 | Rivastigmine | Extended-release patch | Zydus Lifesciences Limited |
| ANDA091689 | Rivastigmine Tartrate | Capsule | Alembic Pharmaceuticals Inc. |
| ANDA203844 | Rivastigmine Tartrate | Capsule | Cadila Pharmaceuticals Limited |

The record lists no approved-indication text for these products. Marketed forms are oral (capsule) and transdermal (patch). No ophthalmic form is listed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is L4: a single old rabbit study of topical dosing, plus indirect class-level literature and a model score. There are no human data or registered trials. The package-insert safety review has not been done, which blocks progression to safety screening. The marketed oral and transdermal forms are also not known to reach the eye at effective concentrations.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to complete the safety screen
- Confirmed mechanism-of-action and original-indication data (e.g., from DrugBank)
- Confirmation of the 2000 rabbit findings (effect size, duration, dose) and replication in a glaucoma or ocular hypertension model
- An assessment of ocular exposure: whether systemic dosing can reach the eye, or whether a topical ophthalmic formulation would be required
- Review of systemic cholinergic adverse effects against the risk-benefit profile in glaucoma patients

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

