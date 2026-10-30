---
layout: default
title: Vestronidase Alfa
parent: Model Prediction Only (L5)
nav_order: 1289
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Vestronidase Alfa: predicted new indication Scheie syndrome (evidence level L5). Approved use: Mucopolysaccharidosis (MPS VII)"
monitor_inn: "VESTRONIDASE ALFA"
predicted_indications: ["Scheie syndrome", "lysosomal storage disease with skeletal involvement", "Hurler syndrome", "Sanfilippo syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "ptosis-vocal cord paralysis syndrome", "ptosis-strabismus-ectopic pupils syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "congenital Horner syndrome (disease)"]
---

# Vestronidase Alfa
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

## Vestronidase Alfa: From Mucopolysaccharidosis to Scheie Syndrome
{: .text-alpha }

## One-Sentence Summary

Vestronidase alfa is a recombinant human beta-glucuronidase enzyme replacement therapy, originally used to treat mucopolysaccharidosis (MPS VII).
The TxGNN model predicts it may be effective for **Scheie syndrome**, but **no clinical trials and no publications** currently support this specific prediction (evidence level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis (MPS VII) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, vestronidase alfa is a recombinant beta-glucuronidase (GUSB) that replaces the enzyme deficient in MPS VII, helping break down glycosaminoglycans (GAGs).

Scheie syndrome is the attenuated form of MPS I and is caused by alpha-L-iduronidase deficiency. Both conditions are lysosomal GAG storage disorders, so the high TxGNN score probably reflects shared pathway and disease-class similarity.

However, the enzymes differ. Beta-glucuronidase does not replace iduronidase, so direct efficacy is mechanistically doubtful. The prediction should be treated as a hypothesis-generating signal, not as evidence of benefit.

**Other predictions in the list (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Lysosomal storage disease with skeletal involvement | 0.9959 | L5 | Broad category that includes MPS VII itself; likely overlap with the original indication, not a new signal |
| 3 | Hurler syndrome | 0.9943 | L5 | Same GAGs are involved, but the missing enzyme is not replaced; only an early prenatal ERT platform trial exists |
| 4 | Sanfilippo syndrome | 0.9942 | L5 | Only MPS VII publications are available; intravenous ERT is unlikely to cross the blood-brain barrier |
| 5–9 | Rare congenital ocular, craniofacial and neuromuscular syndromes (e.g., congenital Horner syndrome) | 0.9902–0.9909 | L5 | No plausible mechanism; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |

## Clinical Trial Evidence

Currently no related clinical trials are registered for Scheie syndrome.

For reference, one trial is linked to a related predicted indication (Hurler syndrome):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL: prenatal enzyme replacement therapy for lysosomal storage disorders, testing maternal and fetal safety and feasibility. The specific enzyme for each condition is not stated, and no efficacy results exist. |

## Literature Evidence

Currently no related literature is available for Scheie syndrome.

For reference, three publications are linked to Sanfilippo syndrome, but all concern vestronidase alfa in MPS VII and are therefore indirect evidence only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32063397](https://pubmed.ncbi.nlm.nih.gov/32063397/) | 2020 | Clinical study (Phase 3, randomized, placebo-controlled, blind-start) | Mol Genet Metab | Long-term safety and efficacy in 12 MPS VII subjects (ages 8–25) receiving 4 mg/kg IV for 24–48 weeks; urinary GAG was significantly reduced |
| [30467742](https://pubmed.ncbi.nlm.nih.gov/30467742/) | 2019 | PK/PD modeling | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic modeling to optimize vestronidase alfa dosing in MPS VII, based on three trials |
| [29478819](https://pubmed.ncbi.nlm.nih.gov/29478819/) | 2018 | Trial design report | Mol Genet Metab | Describes the novel Blind Start design used to study vestronidase alfa in ultra-rare MPS VII |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761047 | MEPSEVII (Ultragenyx Pharmaceutical Inc.) | Injection | Not listed (status: valid) |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Scheie syndrome prediction rests on model output alone (L5). The enzyme deficiency differs from that treated by vestronidase alfa, and no trials or publications address this use. The US biologics license is also listed as cancelled.

**To proceed, the following is needed:**
- Preclinical data (e.g., cell or animal models) testing whether beta-glucuronidase can reduce GAG accumulation in alpha-L-iduronidase deficiency
- Detailed mechanism-of-action data
- FDA package insert warnings and contraindications to enable safety screening
- Clarification of the current regulatory and supply status, given that the license is cancelled
- Route and dosing compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

