---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
monitor_inn: "DUTASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
last_modified_at: 2026-10-14
description: "Dutasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha-reductase inhibitor, originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 7 (all cancelled; includes 1 NDA and 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dutasteride inhibits type 1 and type 2 5-alpha-reductase and lowers dihydrotestosterone (DHT). This is the basis for its efficacy in BPH, where prostate growth is DHT-driven.

The link to the predicted indication is weak. Ambras syndrome is a congenital hypertrichosis tied to genetic changes affecting hair follicle development, and it is not known to be androgen-driven. Lowering DHT would not be expected to correct the underlying genetic defect. The very high TxGNN score (0.99998) most likely reflects proximity in the knowledge graph rather than a biological rationale.

Other top predictions show the same pattern. Most are genetic or developmental conditions (hypertrichosis, hair shaft abnormalities, hypotrichosis, dental and brain malformation syndromes) with no established androgen-mediated mechanism. The one partial exception is diffuse alopecia areata (rank 8). Dutasteride has an evidence base in androgenetic alopecia, but alopecia areata is autoimmune, so the connection is indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

For context, the only publication retrieved across the top 10 predictions concerns the rank 8 prediction, diffuse alopecia areata:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Review | American Journal of Clinical Dermatology | Narrative review of the pathophysiology, evaluation and treatment of androgenetic alopecia in women. It concerns a different condition from alopecia areata, so it is only indirectly relevant. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021319 | AVODART (Waylis Therapeutics LLC) | Capsule, liquid filled | Not listed (cancelled) |
| ANDA203118 | Dutasteride (Amneal Pharmaceuticals LLC) | Capsule | Not listed (cancelled) |
| ANDA204376 | Dutasteride (Marksans Pharma Limited) | Capsule, liquid filled | Not listed (cancelled) |
| ANDA204705 | Dutasteride (Banyan Pharma LLC) | Capsule | Not listed (cancelled) |
| ANDA206574 | Dutasteride (Bryant Ranch Prepack) | Capsule, liquid filled | Not listed (cancelled) |

Two more cancelled ANDAs (ANDA209909 and ANDA202660, both A-S Medication Solutions) are also on record. All 7 authorizations are cancelled and none is currently valid.

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, intraoperative floppy iris syndrome.
- **Pregnancy**: 5-alpha-reductase inhibitors carry a risk of fetal virilization, which matters for any developmental or congenital indication.
- **Drug Interactions**: 100 interactions were identified. Moderate-level interactions include aprepitant, cimetidine, clarithromycin, clotrimazole and miconazole. Other listed interactions (e.g., simvastatin, metformin, omeprazole, prednisone) have an unknown severity level.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no literature (Evidence Level L5). The mechanistic link is speculative, because Ambras syndrome is genetic and not androgen-driven. Dutasteride is also currently cancelled in the US market, with no valid authorizations.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or mechanistic evidence linking DHT suppression to the pathology of Ambras syndrome
- A review of the other top predictions for any with a stronger rationale, such as androgen-related hair disorders, before committing resources
- Clarification of the regulatory and market status, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

