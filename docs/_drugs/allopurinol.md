---
layout: default
title: Allopurinol
parent: Moderate Evidence (L3-L4)
nav_order: 225
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor marketed in the US as an oral tablet. It is generally used for gout and hyperuricemia, although the retrieved US labeling data does not state an indication.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are **0 clinical trials** and only **2 loosely related publications**, neither of which tests allopurinol in porphyria patients.
Preclinical literature also hints that allopurinol could worsen porphyria instead of treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the retrieved US labeling data (generally used for gout and hyperuricemia) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (includes ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Allopurinol is known as a xanthine oxidase inhibitor, and it is a long-established oral product with many US authorizations. Its efficacy in its usual uric-acid-related uses is well established, but that does not by itself explain a benefit in porphyria.

The proposed link to hepatic porphyria is speculative. It runs through heme metabolism and 5-aminolevulinate synthase (ALAS), the rate-limiting enzyme of heme biosynthesis. A 2019 hypothesis paper proposes that acute hepatic porphyrias could be treated by metabolically targeting ALAS, either through tryptophan or through inhibitors of heme utilisation by tryptophan 2,3-dioxygenase. That paper does not test allopurinol.

The direction of effect is unresolved. Preclinical literature on allopurinol and hepatic heme or cytochrome P450 turnover suggests it could be porphyrinogenic (capable of provoking porphyria attacks) instead of therapeutic. This should be checked before any repurposing consideration.

The score of 99.95% should be read with caution. The other nine predictions for this drug are mostly at L5 (prediction only), and several liver and portal-vascular diseases share tied scores. This pattern suggests a shared knowledge-graph neighborhood and not disease-specific signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes targeting liver ALAS by blocking heme use by tryptophan 2,3-dioxygenase, or by giving tryptophan, as a therapy for acute hepatic porphyrias. Does not test allopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (rat) | Biochemical Pharmacology | Very low-dose carbamazepine acted as a porphyria exacerbator in rat liver by depleting heme. Only indirectly relevant, and does not test allopurinol. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214443 | Allopurinol | Tablet | Not stated in source data |
| ANDA210117 | Allopurinol | Tablet | Not stated in source data |
| NDA016084 | Allopurinol | Tablet | Not stated in source data |
| ANDA018659 | Allopurinol | Tablet | Not stated in source data |
| NDA018877 | Allopurinol | Tablet | Not stated in source data |

An injectable form (lyophilized powder for solution) is also listed in the source data. The oral tablet is the main marketed form.

---

## Safety Considerations

- **Possible porphyrinogenic effect**: Preclinical literature on allopurinol and hepatic heme turnover suggests it may provoke porphyria attacks instead of relieving them. This is unconfirmed and needs review before any repurposing.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, and no retrieved paper tests allopurinol in porphyria. The available preclinical hints point toward possible harm, so the direction of effect is unresolved.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- A dedicated literature review on allopurinol's effect on heme biosynthesis, ALAS and porphyria attacks, including any case reports of porphyria exacerbation
- Preclinical or in vitro evidence that allopurinol reduces ALAS induction or heme depletion, and does not worsen it
- Confirmation of the original US labeled indication, since the source data lists none

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

