---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 1257
evidence_level: L5
indication_count: 9
monitor_inn: "TRETINOIN"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
last_modified_at: 2026-11-24
description: "Tretinoin: predicted new indication Rheumatoid nodulosis (evidence level L5). In the US: 55 FDA applications (42 active)"
---

# Tretinoin
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

## Tretinoin: Rheumatoid nodulosis
{: .text-alpha }

## One-Sentence Summary

Tretinoin is a retinoid originally used for acne, acute promyelocytic leukemia, acquired keratosis and palmoplantar keratoderma.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but **no clinical trials** and **no relevant publications** currently support this prediction.
The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 42 of 55) |
| Number of FDA Applications | 55 (active: 42) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for tretinoin: "Tretinoin induces cytodifferentiation and decreased proliferation of APL cells in culture and in vivo. In APL patients, tretinoin treatment produces an initial maturation of the primitive promyelocytes derived from the leukemic clone, followed by a repopulation of the bone marrow and peripheral blood by normal, polyclonal hematopoietic cells in patients achieving complete remission (CR)." ([DailyMed: tretinoin prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c4ae9d9-c2a0-4995-a27a-e3f0f0284db9), label version 2026-08-20; accessed 2026-11-19.) Tretinoin is a retinoid (a vitamin A derivative) with established efficacy in acne and acute promyelocytic leukemia. Mechanistically, it may be applicable to rheumatoid nodulosis, but this has not been tested.

A plausible but unverified link is retinoid-mediated modulation of inflammation and of fibroblast and tissue remodeling. The high TxGNN score (0.9984) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Rheumatoid nodulosis is also very different from the original indications (skin keratinization disorders and a blood cancer), so the similarity to the original use has not been established.

The other top predictions are mostly juvenile and rheumatoid-type arthritis conditions (for example rheumatoid factor-positive polyarticular juvenile idiopathic arthritis, juvenile idiopathic arthritis, and juvenile chronic polyarthritis) and skeletal dysplasias. None has trial or literature support. The pediatric and skeletal ones also raise safety concerns, because retinoids can harm bone growth.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

For reference, the only publications retrieved for any top-ranked prediction concern osteoarthritis (rank 7), and neither supports tretinoin use:
- [34745498](https://pubmed.ncbi.nlm.nih.gov/34745498/) (2021): intra-articular PRP for knee osteoarthritis; unrelated to tretinoin.
- [18463343](https://pubmed.ncbi.nlm.nih.gov/18463343/) (2008): case report of adverse events after arsenic trioxide in acute promyelocytic leukemia; not relevant to osteoarthritis efficacy.

## US Market Information

No approved-indication text is on record. The five main ones are:

<!-- review:begin us-lic-20261106-tretinoin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "There are 16 valid US licenses and no approved-indication text is on record." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tretinoin-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA075213 | TRETINOIN | PADAGIS US | Cream; topical | Valid |
| ANDA075264 | TRETINOIN | PADAGIS US | Cream; topical | Valid |
| ANDA075265 | TRETINOIN | PADAGIS US | Cream; topical | Valid |
| ANDA075529 | TRETINOIN | PADAGIS US | Gel; topical | Valid |
| ANDA075589 | TRETINOIN | PADAGIS US | Gel; topical | Valid |

Showing 5 of 55 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

All listed products are topical (gel, cream, lotion). No systemic formulation appears in the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Differentiating agent (retinoid) used in acute promyelocytic leukemia; not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text) cover many conditions. Examples are:
  - Liver, kidney, pancreatic and gallbladder disease
  - Congestive heart failure
  - Diabetes mellitus and diabetic ketoacidosis
  - Osteoporosis
  - Inflammatory bowel disease and Crohn disease
  - Atopic eczema and sunburn
  - Psychiatric disorders (anxiety, psychotic and other mental disorders)
  - Adrenocortical insufficiency
  - Mycosis fungoides and primary cutaneous T-cell lymphoma
- **Drug Interactions**: 100 interactions were found. The major-level ones are:
  - Doxycycline
  - Tetracycline
  - Minocycline
  - Vitamin A

  Moderate-level interactions include aprepitant, clarithromycin and naltrexone. Levofloxacin is a minor interaction.
- **Pediatric and skeletal concern**: systemic retinoids can cause bone toxicity, including premature epiphyseal closure in growing children. This matters for the juvenile arthritis and skeletal dysplasia predictions.

Please refer to the package insert for full warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a computational score. There are no clinical trials or supporting publications, and the evidence level is L5.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies linking retinoic acid signaling to rheumatoid nodulosis
- An assessment of route and formulation compatibility, since the licensed products are topical and the predicted disease is systemic
- A review of systemic retinoid toxicity relevant to the predicted populations

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "There are 16 valid US licenses and n" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: tretinoin prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c4ae9d9-c2a0-4995-a27a-e3f0f0284db9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

