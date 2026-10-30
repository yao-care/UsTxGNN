---
layout: default
title: Aluminum Chloride
parent: Model Prediction Only (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
monitor_inn: "ALUMINUM CHLORIDE"
predicted_indications: ["seborrheic keratosis", "congenital prothrombin deficiency", "seborrheic dermatitis", "acne (disease)", "vulvar inverted follicular keratosis", "skin disease", "dry eye syndrome", "eye disease", "von Hippel anomaly", "chronic relapsing inflammatory optic neuropathy"]
last_modified_at: 2026-10-30
description: "Aluminum Chloride: predicted new indication seborrheic keratosis (evidence level L5). Approved use: Not specified in the data compiled for this report"
---

# Aluminum Chloride
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

## Aluminum Chloride: From Antiperspirant Use to Seborrheic Keratosis
{: .text-alpha }

## One-Sentence Summary

Aluminum chloride is a topical astringent and antiperspirant ingredient, and its US products are currently all cancelled.
The TxGNN model's top-ranked predictions lack supporting evidence, so this report focuses on the best-supported candidate, **skin disease** (essentially hyperhidrosis and related conditions), with **3 clinical trials** and **19 publications** retrieved.
The evidence is mostly reviews and early-phase studies, and it does not demonstrate therapeutic benefit across skin disease in general.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report (the license records list no approved indication text; products are antiperspirants) |
| Predicted New Indication | Skin disease (best-supported candidate; the top TxGNN-ranked prediction is seborrheic keratosis, which has no supporting evidence) |
| TxGNN Prediction Score | 0.9935 (skin disease); 0.9968 (seborrheic keratosis, rank 1) |
| Evidence Level | L5 (skin disease); L5 for the other nine predictions, except as noted below |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of FDA Applications | 3 (all cancelled) |
| Recommended Decision | Hold (research question: re-define the target as hyperhidrosis) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature retrieved, aluminum chloride is the established first-line topical antiperspirant for primary focal hyperhidrosis. Aluminum salts form plugs in eccrine sweat ducts, and aluminum chloride has been linked to glandular epithelial atrophy and apoptosis.

"Skin disease" is a very broad category. The strongest evidence supports hyperhidrosis only, not skin disease in general. A better framing is to evaluate hyperhidrosis as a specific indication, along with adjacent uses such as hand-foot skin reactions caused by regorafenib (a single-arm trial) and Frey's syndrome (a single case report).

Several other predictions are weak. Congenital prothrombin deficiency, von Hippel anomaly and chronic relapsing inflammatory optic neuropathy show no plausible mechanistic link; their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Seborrheic dermatitis and acne are speculative, and aluminum is a recognized contact allergen. Dry eye syndrome and eye disease are supported only by an unrelated formulation paper and toxicity studies.

---

## Clinical Trial Evidence

Trials retrieved for skin disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03416348](https://clinicaltrials.gov/study/NCT03416348) | Phase 1 | Completed | 95 | Residual-limb hyperhidrosis in amputees; building a treatment algorithm. The specific role of aluminum chloride is not confirmed. |
| [NCT07401277](https://clinicaltrials.gov/study/NCT07401277) | Phase 1 | Recruiting | 32 | Exploratory study of 5-fluorouracil plus aluminum chloride hexahydrate for actinic keratoses. Early-stage and indirect signal. |
| [NCT02028208](https://clinicaltrials.gov/study/NCT02028208) | Phase 2 | Completed | 56 | Patch-test dose-response study of mercury, aluminum and palladium allergens. It addresses hypersensitivity (a safety signal), not therapeutic benefit. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30710603](https://pubmed.ncbi.nlm.nih.gov/30710603/) | 2019 | Review | J Am Acad Dermatol | Antiperspirants are first-line therapy for primary focal hyperhidrosis |
| [25152341](https://pubmed.ncbi.nlm.nih.gov/25152341/) | 2014 | Review | Dermatol Clin | Aluminum salts plug eccrine sweat ducts; topical therapies in hyperhidrosis |
| [30215934](https://pubmed.ncbi.nlm.nih.gov/30215934/) | 2018 | Review | Am Fam Physician | Management options for hyperhidrosis |
| [41839170](https://pubmed.ncbi.nlm.nih.gov/41839170/) | 2026 | Review | Skin Therapy Lett | Aluminum chloride hexahydrate is a conventional hyperhidrosis treatment; newer options reviewed |
| [41572865](https://pubmed.ncbi.nlm.nih.gov/41572865/) | 2026 | Review | Dtsch Arztebl Int | Prevalence, diagnosis and stepwise treatment of hyperhidrosis |
| [40396355](https://pubmed.ncbi.nlm.nih.gov/40396355/) | 2025 | Comparative study | J Cutan Med Surg | Aluminum chloride vs oxybutynin vs botulinum toxin in primary focal hyperhidrosis |
| [37142953](https://pubmed.ncbi.nlm.nih.gov/37142953/) | 2023 | Single-arm trial | BMC Cancer | Topical aluminum chloride for severe regorafenib-associated hand-foot skin reactions |
| [35029347](https://pubmed.ncbi.nlm.nih.gov/35029347/) | 2022 | Review | Dermatitis | Aluminum named Allergen of the Year 2022; pruritic nodules and eczematous dermatitis |
| [31567135](https://pubmed.ncbi.nlm.nih.gov/31567135/) | 2020 | Mouse study | Am J Dermatopathol | 20% aluminum chloride induced apoptosis, keratinization arrest and granular parakeratosis |
| [3771053](https://pubmed.ncbi.nlm.nih.gov/3771053/) | 1986 | Case report | Int J Dermatol | Frey's syndrome responded to 20% aluminum chloride in anhydrous ethyl alcohol |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M019 | Duradry Sweat Minimizing Gel | Gel | Not specified (valid) |
| M017 | Certain Dri Clinical Strength Prescription Protection Rollon | Liquid | Not specified (valid) |
| Not available | Antiperspirant Antisudorifique | Spray | Not specified (cancelled) |

---

## Safety Considerations

- **Knowledge-graph contraindication signals**: exanthem and dermatitis.
- **Contact allergy**: aluminum is a documented contact allergen, and the patch-test study (NCT02028208) addresses this.
- **Skin effects**: one mouse study linked 20% aluminum chloride to keratinization arrest and granular parakeratosis.
- **Mucosal and ocular use**: application to vulvar mucosa or the eye raises irritation and toxicity concerns. Toxicity studies of aluminum also show neurotoxic potential in cell and animal models.

Please refer to the package insert for further warnings, contraindications and drug interaction information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of the ten predictions have no supporting clinical evidence (L5). The only one with meaningful support, skin disease, rests on hyperhidrosis reviews and early-phase or exploratory studies (L3). The category is too broad to act on, and all three US products are cancelled.

**To proceed, the following is needed:**
- Re-frame the target as a specific indication (hyperhidrosis), and assess it against existing OTC and prescription antiperspirant products
- Obtain the FDA package insert warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Review randomized trial data for hyperhidrosis and the regorafenib hand-foot skin reaction trial
- Assess contact allergy and skin irritation risk for any new topical indication
- Confirm the original approved indication, since no indication text is available in the license records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

