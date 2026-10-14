---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 2
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antispasmodic/anticholinergic drug, originally used for irritable bowel syndrome and related conditions.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome (also Clostridium difficile colitis and neurocirculatory asthenia, per the knowledge graph) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 13 (all cancelled; listed under ANDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dicyclomine is an antimuscarinic and smooth-muscle relaxant. Its use in irritable bowel syndrome is based on reducing gut spasm, and mechanistically it may be applicable to bladder and bowel dysfunction.

A plausible link is symptomatic control of detrusor overactivity and spasm that can accompany cauda equina syndrome. However, the drug would not treat the underlying cause, which is compression of the lumbosacral nerve roots and requires urgent surgical decompression.

There is also a safety concern. Anticholinergics can worsen urinary retention, which is common in cauda equina syndrome with an areflexic bladder. The high score is a graph-based prediction only.

A second prediction, **neurogenic bladder** (an obsolete ontology term, score 99.50%), is mechanistically more conventional, since antimuscarinics such as oxybutynin are used for detrusor overactivity. It also has no trials or literature, and the term would need to be mapped to current terminology (e.g., neurogenic detrusor overactivity).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 13 licenses are cancelled; no valid license remains. Approved indication text was not available for these entries. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA084285 | Dicyclomine Hydrochloride (NuCare Pharmaceuticals) | Capsule | Not available |
| ANDA216736 | Dicyclomine hydrochloride (Northwind Health) | Tablet | Not available |
| ANDA040319 | Dicyclomine Hydrochloride (RemedyRepack) | Capsule | Not available |
| ANDA208353 | Dicyclomine hydrochloride (American Regent) | Injection, solution | Not available |
| ANDA040465 | Dicyclomine Hydrochloride (Hikma) | Injection | Not available |

## Safety Considerations

- **Disease-level contraindications (from the knowledge graph, not label text):** hypertension, liver failure and liver disease, hepatic encephalopathy, gastric ulcer, kidney disease, gallbladder disease, benign prostatic hyperplasia, angle-closure glaucoma, coronary artery disease, sleep apnea syndromes, porphyria, anxiety and related neurotic disorders, substance abuse/dependence, and blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anemia).
- **Drug Interactions:** 100 interactions were identified. Most of those listed are Moderate, including:
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergics and antihistamines: hyoscyamine, aclidinium, chlorpheniramine, acrivastine, phenyltoloxamine, amitriptyline
  - Others: botulinum toxin type A, loperamide, galantamine, amantadine, acebutolol, ethanol

  Acetaminophen and hydrochlorothiazide are Minor.
- **Relevance to the predicted indication:** anticholinergic burden and urinary retention risk need specific evaluation.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or literature (Evidence Level L5). The drug would only address symptoms, not the cause of cauda equina syndrome, and its anticholinergic effect may worsen urinary retention. All US licenses are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Mechanism of action data
- A literature and trial search, including for neurogenic detrusor overactivity as the better-supported alternative
- Assessment of urinary retention risk and anticholinergic burden in the target population
- Clarification of current US availability and route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

