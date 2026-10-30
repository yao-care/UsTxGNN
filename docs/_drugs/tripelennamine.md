---
layout: default
title: Tripelennamine
parent: Model Prediction Only (L5)
nav_order: 1265
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "TRIPELENNAMINE"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis"]
description: "Tripelennamine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Tripelennamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Tripelennamine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Tripelennamine is a first-generation H1 antihistamine, originally used for allergic and vasomotor rhinitis, urticaria, angioedema, conjunctivitis, pharyngitis, and the common cold.
Currently there are **0 clinical trials** and **1 publication** (a 1954 clinical experience report on a combination preparation) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tripelennamine is a first-generation H1 antihistamine. It blocks H1 receptors, which reduces histamine-mediated wheal and flare in the skin.

Urticaria is already among the drug's original indications. Allergic urticaria is a subtype of that labeled condition, so the mechanistic link is strong. The high TxGNN score most likely reflects this overlap, so the prediction should not be read as discovery of a truly new use.

Other predictions from the model are weaker:
- However, no drug-specific evidence exists, and current guidelines prefer second-generation non-sedating antihistamines.
- **Nasal cavity disease** (0.9959): the term is too broad, and it partly restates the existing rhinitis indications.
- Any benefit would be symptomatic relief, for example from anticholinergic drying effects.
- **Recalcitrant atopic dermatitis** (0.9911): histamine is not the main driver of this disease, so the mechanistic link is weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13195608](https://pubmed.ncbi.nlm.nih.gov/13195608/) | 1954 | Clinical experience report | Schweizerische medizinische Wochenschrift | Experience with a new antiallergic combination preparation. No abstract is available, and the relevance has not been reviewed. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M017 | Blue-Emu THRIVE Cooling (valid) | Cream | Not specified |
| nan | Stomach Drops (valid) | Liquid | Not specified |

---

## Safety Considerations

- **Disease contraindications from the knowledge graph** (not label text): hypertension and hypertensive disorders, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure (closed-angle) glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), and bladder neck obstruction. These are consistent with the anticholinergic and sympathomimetic-type cautions of first-generation antihistamines.
- **Drug Interactions**: 100 interactions were found. The listed ones are mainly Moderate.
  - **Major**: potassium citrate and potassium chloride.
  - **Moderate**, anticholinergics (additive effects): atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate, clidinium.
  - **Moderate**, others: opioids and related drugs (morphine, opium, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), and metoclopramide.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no registered clinical trials and only a 1954 report with no abstract. As a result, the repurposing value is limited.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank.
- Drug-specific clinical evidence for allergic urticaria or cold urticaria, with comparison against second-generation antihistamines.
- A decision on the target indication, since the current ones overlap with existing uses or have a weak mechanistic link (nasal cavity disease, atopic dermatitis).
- A route and formulation plan, since the only past products were a topical cream and an oral liquid and are now cancelled.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

