---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Celecoxib: From Arthritis and Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Celecoxib is a COX-2 selective NSAID, used mainly for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis and acute pain.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data provided. Published reviews describe osteoarthritis, rheumatoid arthritis, juvenile arthritis, ankylosing spondylitis and acute pain |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed records are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. From general knowledge, celecoxib selectively inhibits COX-2 and reduces prostaglandin-mediated inflammation and pain.

The predicted disease is a monogenic skeletal dysplasia caused by loss of function in CDMP1/GDF5, which impairs limb growth. COX-2 inhibition does not act on this genetic or developmental defect, so **no credible mechanistic link was found**.

The very high TxGNN score (99.88%) most likely reflects proximity to musculoskeletal terms in the knowledge graph, not a pharmacological rationale. It should be treated as a model artifact unless independent evidence appears.

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
| ANDA205129 | Celecoxib (Radha Pharmaceuticals) | Capsule | Not provided in source data |
| ANDA204776 | Celecoxib (Northwind Health Company) | Capsule | Not provided in source data |
| ANDA204519 | Celecoxib (Alembic Pharmaceuticals) | Capsule | Not provided in source data |
| ANDA206827 | Celecoxib (Vangard Labs) | Capsule | Not provided in source data |
| ANDA204590 | Celecoxib (RedPharm Drug) | Capsule | Not provided in source data |

All listed products are oral capsules (5 of 20 licenses shown).

---

## Other Predicted Candidates (Same Drug)

The evidence pack contains 10 predictions. Only two others have any supporting data.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.86% | L5 | No credible link, likely a knowledge-graph artifact |
| 3 | Rheumatoid vasculitis | 99.85% | L4 | Weak, indirect link. Only one case report, and NSAIDs are not disease-modifying here |
| 4 | Myosclerosis | 99.85% | L5 | No credible disease-modifying link |
| 5 | Hypermobility of coccyx | 99.83% | L5 | Nonspecific analgesia only, no celecoxib-specific data |
| 6 | Brachyolmia | 99.83% | L5 | No credible link |
| 7 | Rheumatoid nodulosis | 99.83% | L5 | Indirect at best |
| 8 | RF-positive polyarticular juvenile idiopathic arthritis | 99.82% | L3 | Plausible. The single publication is a Phase 4 registry of safety vs nonselective NSAIDs (PMID [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/)) |
| **9** | **Inflammatory spondylopathy (ankylosing spondylitis / axial spondyloarthritis)** | **99.80%** | **L1** | **Strongest signal. Details below** |
| 10 | WHIM syndrome | 99.80% | L5 | No credible link (CXCR4 gain-of-function) |

### Rank 9: Inflammatory Spondylopathy (Strongest Candidate)

COX-2 inhibition reduces prostaglandin E2-driven inflammation and pain, and NSAIDs are first-line therapy in guidelines. This is closer to indication confirmation or expansion than true repurposing. Evidence Level L1 is supported by two completed Phase 3 trials. The pack recommends **Proceed with Guardrails**.

| Trial | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week comparison of celecoxib 200 mg QD, 200 mg BID and diclofenac in ankylosing spondylitis |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib vs diclofenac SR in Chinese ankylosing spondylitis patients, with 6-week extension |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Two celecoxib doses vs diclofenac over 12 weeks in ankylosing spondylitis |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | Celecoxib added to golimumab vs golimumab alone on 2-year spinal structural progression (CONSUL) |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Etanercept and celecoxib alone or combined in active ankylosing spondylitis |

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | J Rheumatol | Celecoxib efficacious and well tolerated for signs and symptoms of ankylosing spondylitis |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella review | Drugs | Synthesis of celecoxib safety evidence in chronic musculoskeletal conditions |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT analysis (CONSUL) | Ann Rheum Dis | Effect of adding celecoxib to TNF inhibitor on 2-year radiographic spinal progression |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Cohort | Scand J Rheumatol | Cardiovascular and GI bleeding risk comparable between celecoxib and nonselective NSAIDs in AS |
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Cohort | BMB Rep | Celecoxib reported as the only NSAID inhibiting bone progression in spondyloarthritis |

Several publications suggest celecoxib may slow radiographic or bone progression. This remains hypothesis-level. The US label may not include ankylosing spondylitis, so regional label verification is needed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (for the lead prediction, acromesomelic dysplasia, Hunter-Thompson type)

**Rationale:**
The lead prediction has no trials, no literature and no plausible mechanism. The high score looks like a knowledge-graph artifact. The only candidate worth advancing is inflammatory spondylopathy (rank 9), which has two completed Phase 3 trials and is better handled as indication confirmation than repurposing.

**To proceed, the following is needed:**
- For the lead prediction: a mechanistic rationale linking COX-2 inhibition to GDF5/CDMP1 pathways. Without one, deprioritize it.
- For rank 9: verify the US label for ankylosing spondylitis, and assess cardiovascular and GI risk at the lowest effective dose.
- Package insert warnings and contraindications, which are missing from the pack and block safety screening.
- Detailed mechanism of action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

