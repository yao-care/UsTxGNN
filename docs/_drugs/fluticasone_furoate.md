---
layout: default
title: Fluticasone Furoate
parent: Model Prediction Only (L5)
nav_order: 730
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "FLUTICASONE FUROATE"
predicted_indications: ["atopic eczema", "bronchitis", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
description: "Fluticasone Furoate: predicted new indication Atopic eczema (evidence level L5). Approved use: Not recorded in the local data"
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Fluticasone Furoate: Atopic eczema
{: .text-alpha }

## One-Sentence Summary

Fluticasone furoate is a potent corticosteroid, originally used for asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but there are currently **0 registered clinical trials** and only **2 publications**, neither of which evaluates the drug for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, fluticasone furoate is a glucocorticoid receptor agonist with anti-inflammatory and immunosuppressive activity. It is already established for allergic airway disease (asthma and allergic rhinitis).

Atopic eczema is a Th2-driven allergic skin inflammation, which shares an allergic-inflammatory basis with the drug's original indications. Topical corticosteroids are an established class treatment for atopic eczema, so the prediction is biologically plausible.

However, the plausibility comes from the drug class, not from direct evidence for this molecule. The very high TxGNN score is a model prediction and not clinical evidence. The retrieved literature does not test fluticasone furoate in atopic eczema.

Other predicted indications were also reviewed. Bronchitis has indirect evidence (L3) from COPD and chronic cough studies, and is a more evidence-supported research question than atopic eczema. The remaining predictions (contact dermatitis, occupational dermatitis, phototoxic dermatitis, 2-hydroxyethyl methacrylate sensitization, asthma-related traits) rest on model prediction only. "Dermatitis, atopic" is a duplicate of atopic eczema, and "asthma-related traits, susceptibility to" is a genetic trait concept closely tied to the existing asthma indication, so it is not a true repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and adrenal suppression. It discusses how to assess HPA-axis effects in allergic rhinitis patients, who often also have asthma or atopic dermatitis. This is a safety paper and does not evaluate efficacy in eczema. |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Case study of allergen immunotherapy in a patient with autoimmune disease. It mentions atopic dermatitis only in passing and does not involve fluticasone furoate. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205625 | Fluticasone Furoate Ellipta (Prasco Laboratories) | Powder | Not stated (valid) |
| NDA022051 | FLONASE SENSIMIST (A-S Medication Solutions) | Metered spray | Not stated (valid) |
| BLA101833 | Oat Food (Greer Laboratories) | Solution | Not stated (valid) |
| NDA204275 | Fluticasone Furoate and Vilanterol (Prasco Laboratories) | Powder | Not stated (valid) |
| NDA209482 | Trelegy Ellipta (GlaxoSmithKline LLC) | Powder | Not stated (valid) |

Five of five authorizations are currently valid in the US market, as a single-ingredient or combination product, in the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication links, not package insert text): measles, herpes simplex virus keratitis, varicella zoster infection, fungal infectious disease, dermatophytosis, pulmonary tuberculosis, parasitic infection, infectious disease, adrenocortical insufficiency, Addison disease, adrenal gland hyperfunction, Cushing syndrome, ocular hypertension, glaucoma, lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, upper respiratory tract disease.
- **Systemic corticosteroid effects**: the retrieved review highlights HPA-axis (adrenal) suppression as a concern with intranasal corticosteroids. This is relevant if the drug were used on large skin areas or over long periods.
- **Drug interactions**: no interaction records were found.

Please refer to the package insert for official warnings and contraindications, since label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The atopic eczema prediction is mechanistically plausible through the corticosteroid class, but there are no clinical trials and no literature evaluating fluticasone furoate for this condition. The drug is marketed in the US with 5 valid authorizations of 5, but the package insert safety data are missing, so the evidence stays at L4.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Evidence of fluticasone furoate use in atopic eczema, such as trials or comparative studies against established topical corticosteroids
- Assessment of a suitable topical formulation and route, since current products are inhaled or intranasal
- Verification of the regulatory and commercial path, given that the drug is marketed with 5 valid US authorizations of 5
- Consideration of bronchitis (L3) as a more evidence-supported alternative research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

