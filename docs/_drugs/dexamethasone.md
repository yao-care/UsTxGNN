---
layout: default
title: Dexamethasone
parent: Model Prediction Only (L5)
nav_order: 590
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Systemic Corticosteroid Use to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a widely marketed systemic corticosteroid, available in the US as tablets and injections.
The TxGNN model predicts it may be effective for **Alopecia Areata**.
No registered clinical trial tests this use, but about **13 of the 20 retrieved publications** directly address dexamethasone in alopecia areata, including **1 small randomized trial** and **1 network meta-analysis**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (systemic corticosteroid) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (borderline: one small open-label RCT, phase not specified, plus cohorts and a meta-analysis) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dexamethasone is not available in the input. The rationale below comes from general glucocorticoid pharmacology, not from the supplied data.

Alopecia areata is a T-cell-mediated autoimmune attack on the hair follicle. Dexamethasone is a potent glucocorticoid that suppresses this kind of immune inflammation, so the mechanistic link is plausible.

The literature also shows this use in practice. Oral or intravenous dexamethasone "mini-pulse" regimens are used off-label for moderate to severe alopecia areata. They are especially used when JAK inhibitors, the main comparator, are unavailable or unsuitable. The very high TxGNN score is consistent with this, though many other hair-loss diseases score almost as high (see Conclusion), so the score alone is not very discriminating.

## Clinical Trial Evidence

Currently no related clinical trials registered for alopecia areata.

The 14 trials retrieved were all judged unrelated or were not graded. Most are oncology studies in which dexamethasone is a background agent, such as multiple myeloma combinations. They provide no evidence for alopecia areata and are not listed here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatol Ther | Open-label comparison of low-dose oral dexamethasone mini-pulse vs DPCP contact sensitization in 30 children with severe non-progressive alopecia areata. Outcome figures are not in the supplied excerpt. |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic review / network meta-analysis | Arch Dermatol Res | Compares systemic steroids, oral JAK inhibitors and contact immunotherapy in severe alopecia areata. The abstract notes a lack of evidence on which is superior. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | Reviews pulse corticosteroid dosing regimens and side effects in children with alopecia areata. Dosing regimens are not well established. |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective cohort | J Clin Med | Real-world study of the effectiveness and safety of oral mini-pulse corticosteroids, and of factors linked to response. |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Multicenter clinical study | Dermatol Ther | Oral dexamethasone mini-pulse in moderate to severe alopecia areata, motivated by limited access to JAK inhibitors. |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Retrospective cohort | Eur J Dermatol | 19 patients with severe alopecia areata on baricitinib plus topical steroids. Pulse dexamethasone was added as rescue in non-responders. |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospective cohort | Dermatol Ther | 73 children given monthly 1-day vs 3-day IV dexamethasone pulses plus topical clobetasol for 6 to 12 months. |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Long-term follow-up cohort | Dermatol Ther | 65 children and adolescents on monthly oral dexamethasone pulses plus topical steroid, followed for a median of 96 months. |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Uncontrolled series | J Dermatol | 30 patients with extensive alopecia areata given 5 mg dexamethasone on two consecutive days each week. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case report with focused review | J Dermatolog Treat | Durable remission of severe alopecia areata with oral mini-pulse dexamethasone in a patient for whom JAK inhibitors were not an option. |

## US Market Information

Twenty authorizations are recorded; the five main ones are shown. The approved indication text is not stated in the supplied data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203129 | Dexamethasone Sodium Phosphate | Injection, solution | Not stated in the supplied data |
| ANDA215654 | Dexamethasone Sodium Phosphate | Injection | Not stated in the supplied data |
| ANDA084612 | Dexamethasone | Tablet | Not stated in the supplied data |
| ANDA217538 | Dexamethasone | Tablet | Not stated in the supplied data |
| ANDA040802 | Dexamethasone Sodium Phosphate | Injection, solution | Not stated in the supplied data |

Both oral (tablet) and injectable forms are available in the US. These match the oral and intravenous pulse regimens described in the literature.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexamethasone has the strongest support among the predicted indications for alopecia areata. It is backed by one small RCT, several cohort studies and a network meta-analysis. However, no registered trial tests it, most studies are small or uncontrolled, and the FDA package insert warnings and contraindications are missing. The proposal should be treated as a research question, not a ready-to-implement indication.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications), which is currently a blocking gap for safety screening
- Mechanism-of-action data from DrugBank
- Full-text review of the RCT (PMID 36086930) and the network meta-analysis (PMID 39042154), covering outcomes, relapse rates and steroid adverse effects
- A dosing and safety monitoring plan for mini-pulse regimens, including children
- A drug interaction check, since the interaction query returned no results

The other nine predicted indications (for example alopecia mucinosa, telogen effluvium, folliculitis decalvans) are evidence level L5 with no supportive trials or literature. They should stay on **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

