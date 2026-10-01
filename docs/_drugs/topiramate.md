---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 1242
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is an oral antiseizure drug, and the literature in the Evidence Pack also describes its use in migraine prevention. The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** with a very high score (99.70%). However, there are **0 clinical trials** and **0 publications** supporting this prediction, and it is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the US license records contain no indication text, so this comes from the literature and general drug knowledge) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sample records shown are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. The mechanism rationale in the Evidence Pack states that topiramate acts on voltage-gated sodium channels, GABA-A receptors, AMPA/kainate receptors and carbonic anhydrase. These actions explain its antiseizure effect and its use in migraine.

None of these mechanisms is known to be antineoplastic. The link between epilepsy and a tumor of the trigeminal nerve is therefore weak. The high score (0.997) probably reflects the drug sitting close to trigeminal neuralgia or neuropathic pain nodes in the knowledge graph, not any effect on tumor biology.

This prediction should be treated as a likely knowledge-graph artifact until independent evidence says otherwise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The US license records do not include approved indication text, so that column is omitted. Five of the 20 authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078235 | topiramate | Tablet, film coated | Zydus Pharmaceuticals USA Inc. |
| ANDA078235 | topiramate | Tablet, film coated | Zydus Lifesciences Limited |
| ANDA090278 | Topiramate | Tablet, film coated | Proficient Rx LP |
| ANDA078235 | topiramate | Tablet, film coated | REMEDYREPACK INC. |
| ANDA216683 | Topiramate | Capsule | Advagen Pharma Ltd |

All are oral products. Across the full set of authorizations, the dosage forms are tablet, film-coated tablet, capsule, extended-release capsule and coated-pellet capsule.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and the mechanism gives no biological reason to expect an effect on tumors of the trigeminal nerve. The high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Any independent evidence (preclinical, case reports or mechanistic studies) for topiramate in trigeminal or nerve-sheath tumors
- Package insert warnings and contraindications, which are still missing
- Verification of whether the score is driven by trigeminal neuralgia or neuropathic pain proximity in the graph

**Note on other predictions:** The same pack lists **visual epilepsy** (L4, "Research Question"). It has a completed Phase 3 epilepsy monotherapy trial (NCT00231556, n=750) and several systematic reviews, though none is restricted to visually induced seizures. This is a far better-supported direction than the trigeminal tumor prediction and may deserve priority review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

