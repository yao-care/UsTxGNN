---
layout: default
title: Histrelin
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
monitor_inn: "HISTRELIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "pelvic organ prolapse", "female genital tuberculosis", "physiological sexual disorder"]
description: "Histrelin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Histrelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Histrelin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Histrelin is a gonadotropin-releasing hormone (GnRH) agonist, originally used to treat precocious puberty.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no publications** currently support this prediction.
It is most likely a TxGNN model (deep learning) artifact rather than a genuine repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, histrelin is a GnRH agonist. With continuous exposure it desensitizes pituitary GnRH receptors and suppresses LH and FSH, which lowers sex steroids. This is why it works in precocious puberty.

That mechanism does not connect credibly to Ambras syndrome. Ambras syndrome is a genetic hypertrichosis disorder associated with chromosome 8q rearrangements that affect regulation of the TRPS1 gene. It is not a hormone-driven condition, so suppressing the pituitary-gonadal axis would not be expected to change it. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and there is no clinical or published evidence to back it.

A related note on the other top-ranked predictions: the only ones with a plausible mechanism are central precocious puberty entities, which are essentially the drug's existing approved use. Of these, idiopathic central precocious puberty has supporting literature, so it is a re-labeling of known use rather than new repurposing. The remaining top-ten predictions (for example other hypertrichosis or hair shaft disorders, Dandy-Walker syndromes, pelvic organ prolapse and female genital tuberculosis) have no credible mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022058 | SUPPRELIN (Endo USA, Inc.) | Implant | Not specified; status: valid |

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for that information.

- **Knowledge-graph contraindication signals** (not label text): hypertension and hypertensive disorders, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, obesity and monogenic obesity.
- **Drug Interactions**: 100 interactions were recorded, and the 20 shown here are mostly moderate.
  - **Major**: dolasetron.
  - **Moderate, antidiabetic agents**: acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide and dulaglutide.
  - **Moderate, other agents**: famotidine, loperamide, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, clarithromycin and palonosetron.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Ambras type hypertrichosis universalis congenita has no clinical trials, no literature and no credible mechanistic link (Evidence Level L5). The only US product is cancelled, so the high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- Any credible biological rationale linking GnRH agonism to TRPS1-related or other genetic hypertrichosis, plus supporting preclinical data
- Mechanism of action data for histrelin from DrugBank
- FDA package insert warnings and contraindications, to allow safety screening
- Confirmation of current regulatory and supply status, since the only NDA is cancelled
- If the goal is a real use of the drug, a shift in focus to central precocious puberty, with monitoring of growth velocity, bone age and LH suppression, and follow-up for implant removal and recovery of the reproductive axis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

