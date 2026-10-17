---
layout: default
title: Uric Acid
parent: Model Prediction Only (L5)
nav_order: 1277
evidence_level: L5
indication_count: 4
monitor_inn: "URIC ACID"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "bronchitis"]
last_modified_at: 2026-10-14
description: "Uric Acid: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: No approved indication recorded"
---

# Uric Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Uric Acid: From an Unspecified Original Indication to Rheumatoid Arthritis

## One-Sentence Summary

Uric acid is an endogenous purine metabolite. The data compiled for this report contain no approved indication for it.
The TxGNN model predicts it may be relevant to **Rheumatoid Arthritis**, but the support is weak: **1 registered clinical trial** (which does not test uric acid) and **19 publications**, nearly all of which describe uric acid as a disease biomarker rather than as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication recorded |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Uric acid is an endogenous end product of purine metabolism. The only US authorization on record is a cancelled liquid product, and it lists no approved indication.

The literature links uric acid to rheumatoid arthritis (RA) as a marker or comorbidity factor, not as a therapy. Reported associations include cardiovascular risk, prognosis of RA-associated interstitial lung disease, skeletal muscle status, and allantoin levels. Oxidized urate can also form reactive electrophiles during inflammation. Elevated uric acid is generally regarded as pro-inflammatory, which argues against a therapeutic role.

The high TxGNN score most likely reflects network proximity between purine metabolism and inflammation pathways, not a plausible treatment mechanism. The prediction should therefore be treated as a computational hypothesis only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03194204](https://clinicaltrials.gov/study/NCT03194204) | NA | Completed | 160 | Doxycycline as combination therapy in RA. Uric acid is not an intervention, so this gives no direct evidence for the drug-indication pair. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37627564](https://pubmed.ncbi.nlm.nih.gov/37627564/) | 2023 | Systematic review / meta-analysis | Antioxidants (Basel) | Examines the association of circulating uric acid and allantoin with RA (biomarker association, not treatment) |
| [35110331](https://pubmed.ncbi.nlm.nih.gov/35110331/) | 2022 | Review (recommendations) | Ann Rheum Dis | EULAR cardiovascular risk management recommendations in rheumatic diseases, including gout |
| [21115462](https://pubmed.ncbi.nlm.nih.gov/21115462/) | 2011 | Review | Rheumatology (Oxford) | Uric acid and cardiovascular risk in RA |
| [39968300](https://pubmed.ncbi.nlm.nih.gov/39968300/) | 2025 | Review | Front Endocrinol | Mechanisms linking serum urate to musculoskeletal disorders, including RA |
| [40710524](https://pubmed.ncbi.nlm.nih.gov/40710524/) | 2025 | Review | Metabolites | Uric acid, colchicine, and cardiovascular risk in chronic inflammatory diseases such as gout and RA |
| [38699124](https://pubmed.ncbi.nlm.nih.gov/38699124/) | 2024 | Review | Cureus | Compares adenosine deaminase, CRP, and uric acid levels in RA patients versus those without arthritis |
| [37650291](https://pubmed.ncbi.nlm.nih.gov/37650291/) | 2024 | Cohort | Clin Exp Rheumatol | Association of serum uric acid with all-cause and cardiovascular mortality in RA |
| [40837562](https://pubmed.ncbi.nlm.nih.gov/40837562/) | 2025 | Cohort | Front Med | Serum uric acid as a predictor of prognosis in RA-associated interstitial lung disease |
| [35314903](https://pubmed.ncbi.nlm.nih.gov/35314903/) | 2022 | Observational | Inflammation | Serum uric acid as a diagnostic biomarker for RA-associated interstitial lung disease |
| [38026718](https://pubmed.ncbi.nlm.nih.gov/38026718/) | 2023 | Observational | Open Access Rheumatol | Association between serum uric acid and RA disease activity |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Uric Acid | Liquid | No approved indication recorded |

The only authorization on record is cancelled, so no valid US product is currently marketed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. The only trial does not test uric acid, and the literature treats uric acid as a biomarker or risk factor in RA, often a pro-inflammatory one, not as a therapy. The only US authorization is cancelled and has no recorded indication.

**To proceed, the following is needed:**
- Mechanism of action data, plus a plausible hypothesis for how administering uric acid could benefit RA
- Package insert warnings and contraindications
- Preclinical evidence of a therapeutic, not merely associative, effect in RA models
- Clarification of whether the prediction reflects a true therapeutic direction or an artifact of purine-metabolism network proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

