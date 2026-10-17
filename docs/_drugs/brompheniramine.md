---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 474
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Brompheniramine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, common cold…"
---

# Brompheniramine
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

# Brompheniramine: From Allergic Rhinitis and Urticaria to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation antihistamine, originally used for allergic rhinitis, the common cold, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **Allergic Urticaria** (and secondarily **Cold Urticaria**), but **no clinical trials and no publications** were found in the data compiled for this report. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, common cold, atopic/vernal/papillary conjunctivitis, familial dermatographia, urticaria, angioedema (from the knowledge graph; no US label text available) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketed product) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on drug class knowledge, brompheniramine is a first-generation H1-receptor antagonist (alkylamine class). Allergic urticaria is driven largely by histamine released from mast cells, so H1 blockade is mechanistically plausible.

The high score most likely reflects overlap with indications the drug already carries in the knowledge graph (urticaria, angioedema, allergic rhinitis). The prediction is therefore closer to a restatement of an existing indication than a novel repurposing.

The second-ranked prediction, **cold urticaria** (score 99.55%), follows the same logic. It is a physical urticaria in which cold exposure triggers mast cell degranulation, and H1 antihistamines are standard first-line therapy. However, no brompheniramine-specific evidence was supplied. Sedating first-generation agents are also generally less favored than second-generation antihistamines for chronic use, which limits practical value.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 (cancelled) | CVS Pharmacy (CVS Pharmacy, Inc.) | Liquid | Not stated |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived relationships, not package insert text): hypertension, coronary artery disease, myocardial infarction, liver failure and liver disease, kidney disease, epilepsy, COPD, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, hypothyroidism, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, ocular hypertension, hypotensive disorder, substance abuse/dependence, hemoglobinopathy, *Clostridium difficile* colitis, and necrotizing enterocolitis.
- **Drug interactions**: 100 interactions were identified, of which 20 are listed in the compiled data.
  - **Major**: potassium chloride and potassium citrate.
  - **Moderate** (mostly additive anticholinergic or CNS-depressant effects): atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, clidinium, mepenzolate, methscopolamine, propantheline, morphine (including liposomal), opium, loperamide, eluxadoline, metoclopramide, dronabinol, and nabilone.

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and it largely duplicates indications the drug already has. There is also no active US-marketed product, and the package insert safety review has not been completed.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to brompheniramine in allergic and cold urticaria
- A comparison against second-generation antihistamines to establish practical value
- Confirmation of route and formulation availability, since the only US authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

