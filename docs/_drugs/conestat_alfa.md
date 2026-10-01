---
layout: default
title: Conestat Alfa
parent: High Evidence (L1-L2)
nav_order: 549
evidence_level: L1
indication_count: 10
---

# Conestat Alfa
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Conestat Alfa: From Hereditary Angioedema (Approved Use) to C1 Inhibitor Deficiency

## One-Sentence Summary

Conestat alfa (Ruconest) is a recombinant human C1 esterase inhibitor, already marketed in the US for hereditary angioedema (HAE).
The TxGNN model's top prediction is **C1 inhibitor deficiency**, the disease that underlies HAE types I/II, so this is effectively the approved use rather than true repurposing.
It is supported by **41 clinical trials** and **20 publications**, but much of the trial evidence is class-level (other C1-INH products).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary angioedema (acute attacks). The US license record has no indication text, so this comes from the pack's mechanistic rationale. |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.999% (model rank 101) |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125495) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not recorded in the pack. Conestat alfa is a recombinant human C1 esterase inhibitor (a serpin) produced in transgenic rabbits. It replaces the missing or dysfunctional C1-INH and restores control of the classical complement, contact/kallikrein-kinin and fibrinolytic cascades. This limits bradykinin generation, which drives the swelling attacks.

C1 inhibitor deficiency is the root cause of HAE types I/II, so the prediction is direct protein replacement in the deficient state. It is not a distant mechanistic leap. Its short half-life limits use for routine prophylaxis. Its established role is treating acute attacks.

The same knowledge-graph link also appears as the rank 3 prediction, "hereditary angioedema with C1Inh deficiency", with the same evidence base and the same decision.

The other predictions (ranks 2 and 4-10) are weak. They include serpinopathy, Glanzmann thrombasthenia, Scott syndrome, pseudo-von Willebrand disease, and several platelet or thrombocytopenia disorders. They have no trials or literature and no plausible C1-INH mechanism, and they are likely graph-proximity artifacts. All are **Hold** (L5).

## Clinical Trial Evidence

The 10 most relevant of 41 registered trials are listed. Trials of plasma-derived C1-INH are class-level evidence, not conestat alfa itself. Product identity for trials not named in the pack was inferred from titles and should be verified.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06690047](https://clinicaltrials.gov/study/NCT06690047) | Phase 4 | Completed | 5 | Ruconest for the HAE prodrome, to prevent progression to acute attacks. Directly on-drug but very small. |
| [NCT00261053](https://clinicaltrials.gov/study/NCT00261053) | Phase 2 | Completed | 14 | Open-label recombinant human C1-INH for acute HAE attacks, exploring efficacy, safety and PK/PD. |
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Completed | 75 | Randomized, placebo-controlled, double-blind trial of recombinant C1-INH for acute HAE attacks. |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Phase 3 | Completed | 75 | Placebo-controlled trial with open-label extension of rhC1INH 50 U/kg, confirming efficacy, safety and immunogenicity. |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Completed | 77 | Randomized, placebo-controlled study of recombinant C1-INH in acute HAE attacks. |
| [NCT02247739](https://clinicaltrials.gov/study/NCT02247739) | Phase 2 | Completed | 32 | Placebo-controlled 3-period crossover of recombinant C1-INH for attack prophylaxis. |
| [NCT01359969](https://clinicaltrials.gov/study/NCT01359969) | Phase 2 | Completed | 57 | Open-label Ruconest 50 U/kg in children aged 2-13 with acute HAE attacks. |
| [NCT03697187](https://clinicaltrials.gov/study/NCT03697187) | N/A (registry) | Completed | 152 | Real-world safety registry of Ruconest in HAE. |
| [NCT06679426](https://clinicaltrials.gov/study/NCT06679426) | Phase 3 | Not yet recruiting | 24 | Conestat alfa vs placebo for ACE-inhibitor-induced angioedema, a possible expansion beyond HAE. |
| [NCT00289211](https://clinicaltrials.gov/study/NCT00289211) | Phase 3 | Completed | 83 | Placebo-controlled trial of plasma-derived C1-INH in acute HAE attacks (class-level). |

## Literature Evidence

The 10 most relevant of 20 publications are listed. The Lancet 2017 paper is a Phase 2 RCT, so it is typed RCT on the basis of its title. The 2018 paper is typed RCT in the source classification, but its title and abstract read as an expert review.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28754491](https://pubmed.ncbi.nlm.nih.gov/28754491/) | 2017 | RCT (Phase 2, crossover) | Lancet | Recombinant human C1-INH evaluated for prophylaxis of HAE attacks. |
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | RCT (per source classification) | Expert Rev Clin Immunol | Conestat alfa for prophylaxis in adults and adolescents with HAE. |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Review | BioDrugs | Efficacy shown in two similar randomized, double-blind, placebo-controlled trials in HAE attacks. |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic review | Pneumonol Alergol Pol | Compares conestat alfa, human C1-INH and icatibant for acute HAE attacks. |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Cohort | Allergy Asthma Proc | Home treatment of 65 edematous episodes in two patients, assessing real-life efficacy and safety. |
| [31982824](https://pubmed.ncbi.nlm.nih.gov/31982824/) | 2020 | Cohort | Int Immunopharmacol | Home use of rhC1-INH for attacks and short-term prophylaxis, evaluating efficacy and safety. |
| [22171564](https://pubmed.ncbi.nlm.nih.gov/22171564/) | 2012 | Cohort | BioDrugs | Effects of recombinant C1-INH on coagulation and fibrinolysis, addressing thromboembolic concern. |
| [27940765](https://pubmed.ncbi.nlm.nih.gov/27940765/) | 2016 | Guideline | Pediatrics | Management of children with HAE due to C1-INH deficiency. |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Review | Immunotherapy | Recombinant replacement therapy for HAE due to C1-INH deficiency. |
| [39675680](https://pubmed.ncbi.nlm.nih.gov/39675680/) | 2025 | Study | J Allergy Clin Immunol | Clinical response and blood transcriptome pathways before and after treatment of HAE prodromes vs active attacks. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125495 | Ruconest | Injection, powder, for solution (injectable) | Pharming Healthcare Inc. |

The license record contains no approved-indication text.

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.
- **Points flagged in the evidence review**:
  - Hypersensitivity, because the product is derived from rabbit milk.
  - Thromboembolic risk, which is a known concern with C1-INH products.
  - Labeled patient-selection limits.

No formal warnings or contraindications were captured in the pack. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
C1-INH replacement in C1-INH deficiency is mechanistically direct. There are several completed Phase 3 and Phase 2 trials of recombinant C1-INH, plus registry and real-world data. The drug is already marketed in the US. The evidence is strong, but much of the trial base is class-level, and the pack has no label text or safety data.

**To proceed, the following is needed:**
- The Ruconest package insert (indications, warnings, contraindications), to confirm the approved indication and complete the safety screen.
- Verification of product identity for trials graded on class-level evidence (for example NCT02247739).
- A monitoring plan for hypersensitivity and thromboembolic events.
- A separate evaluation of ACE-inhibitor-induced angioedema (NCT06679426) if that expansion is pursued.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

