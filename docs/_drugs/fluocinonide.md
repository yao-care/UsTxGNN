---
layout: default
title: Fluocinonide
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 7
monitor_inn: "FLUOCINONIDE"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "alopecia areata", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome"]
---

# Fluocinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fluocinonide: From Inflammatory Skin Diseases to Alopecia Mucinosa

## One-Sentence Summary

Fluocinonide is a high-potency topical corticosteroid, originally used for inflammatory skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **alopecia mucinosa**, but **no clinical trials and no publications** currently support this prediction.
Among the other top predictions, only alopecia areata has any related material (1 trial in a different disease and 1 case report), and neither directly tests fluocinonide.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis, contact dermatitis, seborrheic dermatitis, discoid lupus erythematosus and other inflammatory skin conditions (the US licence records contain no indication text) |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 13 (all ANDA generic applications, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fluocinonide is a high-potency topical corticosteroid with anti-inflammatory and immunosuppressive effects, and its efficacy in inflammatory skin diseases is established.

Alopecia mucinosa (follicular mucinosis) is an inflammatory disorder of the hair follicle, so local anti-inflammatory therapy is mechanistically plausible. It can also overlap with cutaneous T-cell lymphoma, which is already among fluocinonide's listed original indications. This overlap is an inference, not evidence.

The TxGNN score is a computational prediction only. Other high-ranking predictions are weakly supported or implausible:
- **Alopecia areata** (score 99.59%): an autoimmune, T-cell-mediated disease for which corticosteroids are an established drug class, so the mechanism is plausible.
- **Telogen effluvium, hereditary hypotrichosis with recurrent skin vesicles, alopecia antibody deficiency, and alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome**: little biological rationale for a topical corticosteroid. The high scores probably reflect network proximity to other alopecia terms.
- **Folliculitis decalvans**: only an indirect, adjunctive rationale.

## Clinical Trial Evidence

For alopecia mucinosa, currently no related clinical trials are registered.

The only trial found among the top predictions relates to alopecia areata (rank 3):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicentre prospective study comparing before-and-after photos of patients with central centrifugal cicatricial alopecia across treatment groups. This is a different, scarring alopecia, and fluocinonide is not shown as a studied intervention, so support is only indirect. |

## Literature Evidence

For alopecia mucinosa, currently no related literature is available.

The only publication found among the top predictions relates to alopecia areata (rank 3):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | Journal of the American Academy of Dermatology | Four cases of congenital alopecia areata followed for 3 to 5 years, with prolonged quiescent periods. Treatments included minoxidil 2% and a range of topical agents. It does not specifically test fluocinonide. |

## US Market Information

All 13 licences are generic applications and all are cancelled. No approved indication text is recorded. Up to 5 are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA209030 | Fluocinonide (Padagis Israel) | Gel | Not recorded |
| ANDA210554 | Fluocinonide Cream (Preferred Pharmaceuticals) | Cream | Not recorded |
| ANDA211111 | Fluocinonide (Asclemed USA) | Cream | Not recorded |
| ANDA216389 | Fluocinonide (Quagen Pharmaceuticals) | Solution | Not recorded |
| ANDA212976 | Fluocinonide (Bryant Ranch Prepack) | Ointment | Not recorded |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Contraindication-related disease associations (knowledge graph, not label text)**: the knowledge graph links fluocinonide to caution in hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, Cushing syndrome and adrenal gland hyperfunction, as well as pituitary hormone deficiencies (hypopituitarism, growth hormone deficiency, Sheehan syndrome) and hypogonadotropic hypogonadism (including Kallmann syndrome). These are consistent with systemic corticosteroid effects and should be verified against the label.
- **Drug interactions**: 64 interactions were found, but the severity level of every one listed is "Unknown". Examples include other corticosteroids (triamcinolone, prednisone, budesonide, dexamethasone, fluticasone), cyclosporine, clopidogrel, acetylsalicylic acid, ibuprofen, and several antihistamines and proton pump inhibitors.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, alopecia mucinosa, has only a computational score (L5), with no trials or literature. Alopecia areata has a more plausible mechanism but only tangential evidence (L4). The basic safety data needed for screening is also missing, and all US licences are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from FDA (currently blocking for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- A targeted literature search on topical corticosteroids in follicular mucinosis and alopecia areata
- Confirmation of the route of administration and formulation suited to scalp or follicular disease
- Clarification of the current US market and licensing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

