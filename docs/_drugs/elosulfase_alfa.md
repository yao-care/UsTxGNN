---
layout: default
title: Elosulfase Alfa
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Elosulfase Alfa: predicted new indication Scheie syndrome (evidence level L5). Approved use: Mucopolysaccharidosis (Morquio A syndrome, MPS IVA)"
monitor_inn: "ELOSULFASE ALFA"
predicted_indications: ["Scheie syndrome", "lysosomal storage disease with skeletal involvement", "Hurler syndrome", "Sanfilippo syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "ptosis-vocal cord paralysis syndrome", "ptosis-strabismus-ectopic pupils syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "congenital Horner syndrome (disease)"]
---

# Elosulfase Alfa
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

## Elosulfase Alfa: From Mucopolysaccharidosis to Scheie Syndrome
{: .text-alpha }

## One-Sentence Summary

Elosulfase alfa is an enzyme replacement therapy originally used to treat mucopolysaccharidosis (specifically Morquio A syndrome, MPS IVA).
The TxGNN model predicts it may be effective for **Scheie syndrome**, but **no clinical trials and no publications** directly support this prediction.
The prediction rests on model scoring alone and should be treated as a computational hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis (Morquio A syndrome, MPS IVA) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, elosulfase alfa is a recombinant form of N-acetylgalactosamine-6-sulfatase (GALNS). This enzyme degrades keratan sulfate and chondroitin-6-sulfate, which accumulate in Morquio A syndrome.

Scheie syndrome is an attenuated form of MPS I. It is caused by a deficiency of a different enzyme, alpha-L-iduronidase, so dermatan sulfate and heparan sulfate accumulate. The missing enzyme and the stored substrates both differ from those elosulfase alfa acts on, so there is **no direct mechanistic rationale**. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as the mucopolysaccharidoses and other lysosomal storage diseases, not biological evidence.

### Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Lysosomal storage disease with skeletal involvement | 0.9959 | L5 | Overlaps with the approved MPS IVA use; the publications support the original indication, not a new one |
| 3 | Hurler syndrome | 0.9943 | L5 | Different enzyme deficiency (MPS I); only an indirect Phase 1 prenatal ERT platform trial |
| 4 | Sanfilippo syndrome | 0.9942 | L5 | 13 publications, almost all on Morquio A; mainly central nervous system disease, and large enzymes do not cross the blood-brain barrier |

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, Scheie syndrome.

For reference, the only trial linked to any of the predictions is listed below (under Hurler syndrome, rank 3). It was graded low relevance (C):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL: prenatal enzyme replacement therapy platform for lysosomal storage disorders. It does not show that elosulfase alfa is tested in Hurler syndrome and provides no efficacy evidence for this drug. |

---

## Literature Evidence

Currently no related literature is available for Scheie syndrome.

The publications below were linked to other predictions. They concern Morquio A (the original indication) and therefore **do not support repurposing**. They are included for context on the drug's established profile:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24810369](https://pubmed.ncbi.nlm.nih.gov/24810369/) | 2014 | RCT | J Inherit Metab Dis | Phase 3 randomised placebo-controlled study of efficacy and safety in Morquio A |
| [25284089](https://pubmed.ncbi.nlm.nih.gov/25284089/) | 2015 | RCT post-hoc analysis | Mol Genet Metab | Multi-domain impact in the pivotal 24-week phase 3 trial |
| [27380995](https://pubmed.ncbi.nlm.nih.gov/27380995/) | 2016 | Long-term extension | Mol Genet Metab | Long-term endurance and safety over 96 weeks (120 weeks from baseline) |
| [27553181](https://pubmed.ncbi.nlm.nih.gov/27553181/) | 2016 | Long-term extension | J Inherit Metab Dis | Long-term respiratory function outcomes |
| [28535791](https://pubmed.ncbi.nlm.nih.gov/28535791/) | 2017 | Long-term extension | Orphanet J Rare Dis | Outcomes in adults with Morquio A compared with a natural history cohort |
| [25487082](https://pubmed.ncbi.nlm.nih.gov/25487082/) | 2015 | Immunogenicity analysis | Clin Ther | Immunogenicity profile from the phase III MOR-004 trial |
| [25234648](https://pubmed.ncbi.nlm.nih.gov/25234648/) | 2014 | Clinical pharmacology | Clin Pharmacokinet | Pharmacokinetics and pharmacodynamics in Morquio A patients |
| [41088244](https://pubmed.ncbi.nlm.nih.gov/41088244/) | 2025 | Review | Orphanet J Rare Dis | Recent advances in MPS IVA treatment; ERT is currently the only approved therapy |
| [42363262](https://pubmed.ncbi.nlm.nih.gov/42363262/) | 2026 | Cohort | Orphanet J Rare Dis | Long-term follow-up and response to elosulfase alfa in a Czech MPS IVA cohort |
| [42279040](https://pubmed.ncbi.nlm.nih.gov/42279040/) | 2026 | Cohort | J Clin Med | Growth patterns in MPS IVA and MPS IIIA, including association with ERT |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125460 | VIMIZIM (BioMarin Pharmaceutical Inc.) | Injection, solution, concentrate | Not specified in the compiled data (status: valid) |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, Scheie syndrome, has no clinical trial or literature support (evidence level L5). Its biology is also mismatched: the enzyme deficiency and stored substrates differ from those elosulfase alfa addresses. The literature linked to other predictions concerns the original Morquio A indication, so it does not constitute repurposing evidence. The US market status is also listed as cancelled only.

**To proceed, the following is needed:**
- Mechanism of action data, including any evidence of activity against dermatan or heparan sulfate substrates
- Preclinical or in vitro evidence that elosulfase alfa has any effect in alpha-L-iduronidase deficiency models
- FDA package insert warnings and contraindications to enable safety screening (currently a blocking gap)
- Clarification of the US regulatory status, since the license is recorded as cancelled
- Confirmation of the approved indication text for BLA125460
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

