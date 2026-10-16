---
layout: default
title: Tripelennamine
parent: Moderate Evidence (L3-L4)
nav_order: 1265
evidence_level: L4
indication_count: 5
monitor_inn: "TRIPELENNAMINE"
predicted_indications: ["allergic urticaria", "cold urticaria", "nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis"]
---

# Tripelennamine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Tripelennamine: From Allergic Rhinitis and Urticaria to Allergic Urticaria

## One-Sentence Summary

Tripelennamine is a first-generation H1 antihistamine, originally used for allergic and vasomotor rhinitis, urticaria, angioedema, conjunctivitis, pharyngitis, and the common cold.
The TxGNN model predicts it may be effective for **allergic urticaria**, but this is largely an overlap with an existing labeled use rather than a true new indication.
Currently there are **0 clinical trials** and **1 publication** (a 1954 clinical experience report on a combination preparation) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, conjunctivitis (atopic, papillary, vernal), familial dermatographia, urticaria, angioedema |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tripelennamine is a first-generation H1 antihistamine. It blocks H1 receptors, which reduces histamine-mediated wheal and flare in the skin.

Urticaria is already among the drug's original indications. Allergic urticaria is a subtype of that labeled condition, so the mechanistic link is strong. The high TxGNN score most likely reflects this overlap, so the prediction should not be read as discovery of a truly new use.

Other predictions from the model are weaker:
- **Cold urticaria** (99.87%): H1 antihistamines are first-line therapy for this inducible urticaria, so there is a class-level rationale. However, no drug-specific evidence exists, and current guidelines prefer second-generation non-sedating antihistamines.
- **Nasal cavity disease** (99.59%): the term is too broad, and it partly restates the existing rhinitis indications.
- **Acute laryngopharyngitis** (99.53%): this is adjacent to the existing pharyngitis and common cold uses. Any benefit would be symptomatic relief, for example from anticholinergic drying effects.
- **Recalcitrant atopic dermatitis** (99.11%): histamine is not the main driver of this disease, so the mechanistic link is weak.

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
| M017 | Blue-Emu THRIVE Cooling (cancelled) | Cream | Not specified |
| nan | Stomach Drops (cancelled) | Liquid | Not specified |

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
The predicted indication, allergic urticaria, largely overlaps with the drug's existing urticaria indication. There are no registered clinical trials and only a 1954 report with no abstract. The drug has no valid US marketing authorization (both licenses are cancelled), and current guidelines favor second-generation antihistamines. As a result, the repurposing value is limited.

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

