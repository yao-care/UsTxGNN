---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 927
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Midodrine is an oral drug used to raise blood pressure in autonomic disorders such as orthostatic hypotension, postural orthostatic tachycardia syndrome (POTS) and multiple system atrophy.
The TxGNN model predicts it may be effective for **variably protease-sensitive prionopathy**, a rare prion disease.
This is a graph-based prediction only: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Orthostatic hypotension (also POTS and multiple system atrophy per the knowledge graph; no approved-indication text was available in the US license records) |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all are ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data. Midodrine is known to be a peripherally acting alpha-1 adrenergic agonist. Its active metabolite, desglymidodrine, constricts arterioles and veins and raises blood pressure. This explains its use in orthostatic hypotension, POTS and autonomic failure in multiple system atrophy.

The link to a prion disorder is weak. No plausible mechanism connects alpha-1 agonism to modifying the course of a prion disease. At most, midodrine could treat autonomic symptoms such as low blood pressure on standing, and that would not be a repurposing claim for the underlying disease. The very high TxGNN score most likely reflects network relationships in the knowledge graph, not biological or clinical support.

Among the top 10 predictions, only **hypotensive disorder** (rank 4) has meaningful support: a completed Phase 2 trial, NCT02893553, and many guideline and review articles. That indication is essentially on-label, so it is not true repurposing. Most of the other predictions (for example ADHD, monogenic obesity and sinoatrial node disease) have no evidence or a doubtful mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 10 midodrine hydrochloride tablet authorizations are cancelled. The records contain no approved-indication text. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212774 | Midodrine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not specified |
| ANDA217271 | Midodrine Hydrochloride (First Nation Group, LLC) | Tablet | Not specified |
| ANDA207169 | Midodrine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not specified |
| ANDA214734 | Midodrine Hydrochloride (Alembic Pharmaceuticals Inc.) | Tablet | Not specified |
| ANDA212543 | Midodrine Hydrochloride (TruPharma, LLC) | Tablet | Not specified |

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not taken from label text): adrenal gland pheochromocytoma, phaeochromocytoma, sympathetic paraganglioma, adrenal gland cancer, duodenum cancer, small intestine cancer, heart cancer, thyrotoxicosis, hyperthyroidism and Graves disease. These should be verified against the current package insert.
- **Drug Interactions**: 81 interactions are recorded. Most of those listed are Moderate, mainly with other sympathomimetics and appetite suppressants: epinephrine (including ophthalmic and topical forms), ephedrine (including nasal), isometheptene, phentermine, diethylpropion, mazindol and sibutramine. Other Moderate interactions include bupropion, lorcaserin, trospium, rolapitant and glycerol phenylbutyrate. Minor interactions include ranitidine, cimetidine and metformin.
- **Theoretical concern**: the pressor effect can cause reflex bradycardia, so use in conduction disorders such as sinoatrial node disease or sinoatrial block needs caution.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for variably protease-sensitive prionopathy rests only on a graph-based score. There are no trials or publications, and no plausible mechanism links an alpha-1 agonist to a prion disease. Midodrine is also currently listed as "Cancelled only" in the US.

**To proceed, the following is needed:**
- A mechanistic hypothesis and preclinical data showing that midodrine affects prion disease biology, not just autonomic symptoms
- Detailed mechanism-of-action data
- Package insert warnings and contraindications, to complete safety screening
- Verification of US availability and regulatory status
- Consideration of the better-supported **hypotensive disorder** prediction (rank 4, L2, Proceed with Guardrails) as a separate, largely on-label track. Its guardrails are supine hypertension risk and the drug-interaction burden.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

