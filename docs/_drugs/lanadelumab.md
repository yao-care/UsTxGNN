---
layout: default
title: Lanadelumab
parent: Model Prediction Only (L5)
nav_order: 832
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema Prophylaxis to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (Takhzyro) is a monoclonal antibody that blocks plasma kallikrein and is already marketed to prevent hereditary angioedema (HAE) attacks.
The TxGNN model predicts it may be effective for **C1 inhibitor deficiency**, supported by **22 clinical trials** and **20 publications**.
This prediction largely restates the approved use, because HAE types I and II are C1 inhibitor deficiency. The real repurposing question is the acquired form of C1-INH deficiency, which rests only on small case series.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the US license entries; the drug is marketed for HAE prophylaxis |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L1 as scored in the Evidence Pack (strictly L2, since only the HELP trial is a randomized Phase 3) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 listings (all under BLA761090) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism data is missing from the record, but the mechanism is well understood. Lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein. In C1 inhibitor deficiency, the body lacks enough functional C1-INH, so plasma kallikrein goes unchecked. This drives excess bradykinin, a vasodilator that causes the swelling attacks. Blocking kallikrein directly targets this pathway.

The predicted indication and the approved use overlap almost completely. HAE type I/II is C1-INH deficiency, and the pivotal trials studied it. The prediction is therefore best read as a data artifact (the record lists no original indications) rather than true repurposing. The genuinely new use is acquired C1-INH deficiency. Two case series (2021 and 2023) report efficacy there, but no prospective trial exists.

## Clinical Trial Evidence

Shown are the 10 most relevant of 22 trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study: randomized, double-blind, placebo-controlled trial of long-term prevention of attacks in type I/II HAE |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension: open-label long-term safety and efficacy |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING: open-label safety, PK and PD in children aged 2 to <12 |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Open-label, 26-week safety, PK and efficacy study in Chinese HAE patients |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Open-label efficacy and safety in Japanese HAE patients |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program for HAE type I/II |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety and efficacy in non-histaminergic angioedema with normal C1-INH, a different condition from C1-INH deficiency |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE: 3-year real-world study comparing attack numbers before and after starting lanadelumab |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER: observational study of HAE attack rates before and after lanadelumab in the US and Canada |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | Completed | 115 | Real-world effectiveness and safety of lanadelumab and icatibant in China |

## Literature Evidence

Shown are the 10 most relevant of 20 publications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab versus placebo for preventing HAE attacks (HELP trial) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label extension of Phase 3 RCT | Allergy | HELP OLE: long-term effectiveness and safety in patients aged 12 and older with HAE 1/2 |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational | J Allergy Clin Immunol Pract | INTEGRATED: multicountry real-world effectiveness in HAE |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic review | Clin Rev Allergy Immunol | Breakthrough attacks in type I/II HAE patients on long-term prophylaxis |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network meta-analysis | Drugs R D | Indirect comparison of long-term prophylaxis options (garadacimab, lanadelumab, SC C1-INH, berotralstat) |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect treatment comparison | J Comp Eff Res | Lanadelumab versus a C1-esterase inhibitor in children under 12 with HAE |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case series | J Allergy Clin Immunol Pract | Efficacy of lanadelumab in acquired angioedema with C1-inhibitor deficiency |
| [36379410](https://pubmed.ncbi.nlm.nih.gov/36379410/) | 2023 | Case series | J Allergy Clin Immunol Pract | Efficacy of lanadelumab in angioedema due to acquired C1 inhibitor deficiency |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | Overview of hereditary angioedema |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Preclinical and Phase I studies of lanadelumab for HAE with C1-INH deficiency |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761090 | TAKHZYRO (Takeda Pharmaceuticals America, Inc.) | Solution | — |
| BLA761090 | TAKHZYRO (Takeda Pharmaceuticals America, Inc.) | Solution | — |
| BLA761090 | TAKHZYRO (Takeda Pharmaceuticals America, Inc.) | Injection, solution | — |

The three rows are separate listings under a single BLA. The record contains no indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is clear, and a completed randomized Phase 3 trial (HELP) plus several Phase 3 open-label studies and real-world cohorts support use in C1-INH-deficient HAE, which is already marketed. The other nine predictions (serpinopathy, pancreatitis, platelet and myopathy disorders and others) have no trials, no literature and no plausible mechanism. They stay at Hold.

**To proceed, the following is needed:**
- The current US package insert, to confirm the labeled indication and to fill in warnings and contraindications
- DrugBank mechanism-of-action data to complete the record
- A prospective study before any use in acquired C1-INH deficiency, which is off-label and supported only by small case series
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

