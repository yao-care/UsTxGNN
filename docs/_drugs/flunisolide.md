---
layout: default
title: Flunisolide
parent: Model Prediction Only (L5)
nav_order: 717
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "FLUNISOLIDE"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "2-hydroxyethyl methacrylate sensitization", "polyp of vocal cord", "polyp of middle ear", "fibroepithelial polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
description: "Flunisolide: predicted new indication Atopic eczema (evidence level L5). Approved use: Not recorded in the local data"
---

# Flunisolide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Flunisolide: Atopic eczema
{: .text-alpha }

## One-Sentence Summary

Flunisolide is a corticosteroid originally used for asthma and allergic or vasomotor rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but there are **0 clinical trials** and only **1 publication** (an observational study) behind this direction.
The evidence is indirect and rests mainly on class-level corticosteroid pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, flunisolide is a corticosteroid with anti-inflammatory activity. Its efficacy in asthma and allergic rhinitis is established, and mechanistically it may be applicable to atopic eczema.

Asthma, allergic rhinitis and atopic dermatitis are closely related allergic (atopic) conditions that often occur together. Atopic dermatitis is also considered a risk factor for later asthma. Corticosteroids as a class are an established treatment for atopic dermatitis. This makes the prediction biologically plausible.

However, the link is indirect. The only retrieved paper is an observational study of exhaled breath condensate cytokines and pH in children with asthma and atopic dermatitis. It does not test flunisolide as a treatment for eczema. The same prediction also appears under the synonym "dermatitis, atopic" (score 0.9985), with the same single paper.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18926054](https://pubmed.ncbi.nlm.nih.gov/18926054/) | 2008 | Cohort | Allergy and Asthma Proceedings | Measured exhaled breath condensate cytokines (Th1, Th2, regulatory T cells) and pH in children with asthma and atopic dermatitis, and looked at the effect of a short course of inhaled corticosteroid. It is a biomarker study, not an efficacy trial of flunisolide for eczema. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074805 (cancelled) | Flunisolide (Oceanside Pharmaceuticals) | Solution | Not listed |
| ANDA207802 (cancelled) | Flunisolide (Ingenus Pharmaceuticals, LLC) | Solution | Not listed |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** liver disease, gallbladder disease, measles, herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, varicella zoster infection, fungal infectious disease, dermatophytosis, glaucoma, parasitic infection, infectious disease, lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, upper respiratory tract disease. These come from a knowledge graph and should be checked against the official label.
- **Drug Interactions:** 100 interactions were found in the interaction database. Those graded Moderate are clarithromycin, inhaled rapid-acting human insulin and cobicistat. Others, including prednisone, dexamethasone, omeprazole, simvastatin, glyburide, glipizide and rosiglitazone, are of unknown severity. Systemic corticosteroids and CYP3A4 inhibitors (such as clarithromycin and cobicistat) merit particular attention.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials, and the only paper is an observational study that does not test flunisolide in eczema. The evidence is L4 and rests on class-level corticosteroid pharmacology. Many established topical corticosteroids already exist for atopic dermatitis, so the added value of flunisolide is unclear.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Direct evidence for flunisolide in atopic dermatitis, or a comparison against existing topical corticosteroids
- A route and formulation assessment, since only a solution form is on record
- A check of other predictions for stronger candidates. Bronchitis (L3) has a small, old 1981 clinical evaluation of flunisolide, which makes it the most directly supported of the ten predictions, although the evidence is dated and low-grade.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

