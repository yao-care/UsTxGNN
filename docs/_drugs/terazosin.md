---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 1211
evidence_level: L5
indication_count: 10
monitor_inn: "TERAZOSIN"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
last_modified_at: 2026-10-14
description: "Terazosin: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Terazosin
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

## Terazosin: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker originally used to treat hypertension and benign prostatic hyperplasia.
The TxGNN model ranks **hypotrichosis simplex of the scalp** as its top prediction, but **no clinical trials and no publications** currently support it. The prediction rests on model score alone.
Among the other predicted indications, **Raynaud disease** and **migraine** have the most (still limited and dated) supporting literature, and are better follow-up candidates.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of NDAs | 5 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, terazosin is an alpha-1 adrenergic blocker. Its effect in hypertension and benign prostatic hyperplasia comes from relaxing vascular and prostatic smooth muscle.

For hypotrichosis simplex of the scalp, the mechanistic rationale is weak. Hypotrichosis simplex is a genetic disorder of hair growth. A link to hair follicle biology, for example through the antihypertensive minoxidil, is only an analogy and not evidence. A vasodilatory effect on scalp microcirculation is speculative, and alpha-1 blockade is unlikely to correct an underlying genetic defect. The high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same applies to the other hair-related predictions (congenital hypotrichosis milia, diffuse alopecia areata, Ambras-type hypertrichosis). Alopecia areata is autoimmune, and Ambras syndrome is an excess-hair condition, the opposite phenotype.

Two other predictions are mechanistically more coherent:
- **Raynaud disease (score 0.9983):** Alpha-1 blockade causes peripheral vasodilation, which plausibly reduces vasospastic attacks.
- **Migraine disorder (score 0.9992):** Alpha-1 blockade may modulate vascular tone and sympathetic activity relevant to migraine.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (hypotrichosis simplex of the scalp), nor for any of the other nine predicted indications.

## Literature Evidence

Currently no related literature available for the top predicted indication (hypotrichosis simplex of the scalp).

The literature below relates to other predicted indications from the same candidate list:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical study (design not verifiable) | Minerva Cardioangiologica | Raynaud disease: terazosin was reported to reduce the number, intensity and duration of vasospastic attacks in idiopathic and secondary Raynaud's phenomenon, with improved thermographic and ultrasonographic findings |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Small open clinical study | La Clinica Terapeutica | Migraine: open trial in 46 patients with hemicrania without aura (10 on terazosin, 29 on buflomedil, 7 on both) testing prophylaxis of headache; also the only paper cited for migraine with brainstem aura, where the subtype does not match |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review / case series | Headache | Migraine: 10 patients given terazosin or doxazosin; most had fewer or milder migraines, but 5 stopped because of side effects |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Current Cardiology Reviews | Alopecia: general review of extracardiac effects of cardiovascular drugs (such as minoxidil). It is indirect and does not show terazosin efficacy |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075317 | Terazosin (Jubilant Cadista) | Capsule | Not listed (valid) |
| ANDA074823 | Terazosin Hydrochloride (Aphena Pharma Solutions) | Capsule | Not listed (valid) |
| ANDA075667 | Terazosin (Bionpharma) | Capsule | Not listed (valid) |
| ANDA075614 | Terazosin (Chartwell RX) | Capsule | Not listed (valid) |
| ANDA219482 | Terazosin (Ajanta Pharma USA) | Capsule | Not listed (valid) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Contraindication-related conditions (from the knowledge graph, not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, priapism, and intraoperative floppy iris syndrome.
- **Drug Interactions:** 100 interactions were identified. The listed ones are mostly Moderate, including corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisone, prednisolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), opioids (morphine, liposomal morphine, opium), bupropion, and the cannabinoids dronabinol and nabilone. Several others (calcitriol, pantoprazole, glimepiride) have an unknown severity level.
- **Practical note:** Terazosin's known hypotensive and orthostatic effects would need to be weighed carefully in migraine or Raynaud populations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypotrichosis simplex of the scalp, has a very high model score but no trials or literature, and a weak mechanistic basis for a genetic hair disorder. Every hair-related prediction is at L4 or L5 evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- If pursuing this candidate list, prioritize **Raynaud disease** and **migraine**: these have older, small studies and need controlled trials, with comparison to established agents such as calcium channel blockers for Raynaud disease
- For the hair-related predictions, preclinical evidence on follicle biology before any clinical consideration
- Clarification of the regulatory path, since 5 US licenses are valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

