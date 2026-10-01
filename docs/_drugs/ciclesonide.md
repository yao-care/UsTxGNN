---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ciclesonide: From Inhaled Corticosteroid Use to Atopic Eczema

## One-Sentence Summary

Ciclesonide is a corticosteroid prodrug marketed in the US as an inhaled aerosol (Alvesco) and a nasal spray (Omnaris).
The TxGNN model predicts it may be effective for **atopic eczema**.
**No clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (2 unique NDAs; NDA021658 is listed twice) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Based on known pharmacology, ciclesonide is a glucocorticoid prodrug. It is converted to its active form, des-ciclesonide, which acts as a glucocorticoid receptor agonist.

Glucocorticoid receptor agonism suppresses type 2 inflammation. Atopic eczema is driven by this kind of inflammation, and topical corticosteroids are a standard drug class for the disease. This class-level link is why the prediction is biologically plausible.

Two caveats apply. The approved indication text is missing from the input, so the relationship to the original indications could not be assessed. The choice of route (inhaled or nasal versus topical skin delivery) and skin-specific pharmacology have not been addressed. The knowledge graph also lists "dermatitis, atopic" (rank 3, score 99.73%) as a separate entry for the same condition. The two entries should be merged in downstream review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | 2-hydroxyethyl methacrylate sensitization | 99.76% | L5 | A hapten-driven allergy state, not a treatable disease for an inhaled corticosteroid. It likely reflects knowledge-graph proximity. Hold. |
| 3 | Dermatitis, atopic | 99.73% | L5 | Duplicate of atopic eczema. |
| 4 | Bronchitis | 99.70% | L4 | The only support is a Finnish COPD guideline ([PMID 25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/), 2015). It is indirect evidence and does not show ciclesonide efficacy. |
| 5 | Contact dermatitis | 99.25% | L4 | The only item is a case report ([PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), 2012). It describes systemic allergic dermatitis from inhaled budesonide, with patch-test cross-reactivity to ciclesonide. This is a safety signal, not therapeutic evidence. Hold. |
| 6 | Asthma-related traits, susceptibility to | 99.13% | L5 | Describes genetic susceptibility rather than a treatable condition. Likely overlaps an existing indication or is an ontology artifact. Hold. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021658 | Alvesco | Aerosol, metered | Covis Pharma US, Inc |
| NDA022004 | Omnaris | Spray | Covis Pharma US, Inc |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available.

- **Cross-reactivity signal**: A published case report describes systemic allergic dermatitis from inhaled budesonide, with patch-test cross-reactivity to ciclesonide ([PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)). Corticosteroids can themselves sensitize, which matters for any skin-related use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.96%), but there are no trials or literature for ciclesonide in atopic eczema. Package insert safety data is missing, which blocks safety screening. The only related published item is a sensitization case report.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, obtained from the FDA label
- Mechanism of action data from DrugBank
- Approved indication text for each NDA, to confirm the original indications
- A literature and trial search specific to ciclesonide in atopic eczema
- A route and formulation assessment, since the marketed products are inhaled or nasal and not topical
- A corticosteroid sensitization and cross-reactivity safety review
- Merging of the duplicate "atopic eczema" and "dermatitis, atopic" entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

