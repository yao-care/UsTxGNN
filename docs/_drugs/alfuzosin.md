---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
monitor_inn: "ALFUZOSIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
last_modified_at: 2026-10-14
description: "Alfuzosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic receptor antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction, so it rests on a model-based graph prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, alfuzosin is a uroselective alpha-1 adrenergic receptor antagonist, and its efficacy in BPH rests on relaxing smooth muscle in the prostate and bladder neck.

No established mechanistic link to the predicted indication was identified. Ambras syndrome is a rare genetic disorder caused by chromosomal rearrangements near 8q22 that affect regulation of the *TRPS1* gene. Alpha-1 blockade is not known to act on this pathway. The very high score most likely reflects network proximity to hair-related phenotypes in the knowledge graph. It may also reflect an adverse-effect-like association, since hypertrichosis is a known side effect of some vasodilators such as minoxidil, rather than a therapeutic effect.

The other top-ranked predictions show the same pattern. They are mostly hair-related or rare congenital conditions (hypertrichosis, trichomegaly, hair shaft abnormalities, hypotrichosis), along with allergic urticaria and persistent fetal circulation syndrome. None has supporting clinical or literature evidence. Several have a safety concern or a mechanism pointing the wrong way. For example, alfuzosin has reported hypersensitivity and urticarial reactions, and systemic alpha-1 blockade in neonates risks hypotension.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021287 | Uroxatral (Advanz Pharma (US) Corp.) | Extended-release tablet | Cancelled |
| ANDA079013 | Alfuzosin Hydrochloride (Apotex Corp.) | Extended-release tablet | Cancelled |
| ANDA079057 | Alfuzosin Hydrochloride (Northwind Health Company, LLC) | Extended-release tablet | Cancelled |
| ANDA079060 | Alfuzosin Hydrochloride (Rising Pharma Holdings, Inc.) | Film-coated extended-release tablet | Cancelled |
| ANDA090284 | Alfuzosin hydrochloride (Aphena Pharma Solutions - Tennessee, LLC) | Extended-release tablet | Cancelled |

All 6 US authorizations are cancelled (one further generic, ANDA203192 from Unichem, is not shown). Approved indication text was not available for any of them.

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (these come from drug-disease relationships in the graph, not from package insert text):
  - Multiple system atrophy
  - Postural orthostatic tachycardia syndrome
  - Orthostatic hypotension
  - Hypotensive disorder
  - Long QT syndrome (including the familial form)
  - Torsades de pointes
  - Liver failure and liver disease
  - Gallbladder disease
  - Intraoperative floppy iris syndrome
- **Drug Interactions**: 100 interactions were found. The 20 reviewed here include:
  - **Major**: cisapride, clarithromycin, dolasetron
  - **Moderate**: famotidine, aprepitant, bupropion, levofloxacin, granisetron, dronabinol, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), clotrimazole, and several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose)
  - **Minor**: cimetidine

  The major interactions suggest additive QT-prolongation risk or CYP3A4 inhibition.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no literature behind it, so it sits at evidence level L5 despite the very high model score. No plausible mechanism links alpha-1 blockade to Ambras syndrome, and the signal may reflect an adverse-effect association instead of a therapeutic one. All US licenses are also cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for safety screening
- Mechanism of action data to test whether any biological link to the *TRPS1* or hair-follicle pathway exists
- Preclinical or mechanistic evidence, such as hair-follicle models, showing a therapeutic rather than adverse direction of effect
- A review of whether any other predicted indication has more plausible support, since the other nine predictions are also at L5 and rated Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

