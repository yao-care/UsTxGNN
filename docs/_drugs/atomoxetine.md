---
layout: default
title: Atomoxetine
parent: Model Prediction Only (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Atomoxetine
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

# Atomoxetine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Atomoxetine is an oral selective norepinephrine reuptake inhibitor already marketed in the US, and the Evidence Pack links it to ADHD, although the US license records do not state an indication.
The TxGNN model predicts it may be effective for **Specific Developmental Disorder**, a broad graph term.
Currently **7 clinical trials** and **15 publications** are attached to this prediction, but they concern ADHD (including ADHD with autism), so this is closer to on-label confirmation than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (the Evidence Pack indicates ADHD; label mapping needs verification) |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L1 (as assigned in the Evidence Pack; see caveat below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled records are all ANDAs, i.e., generics) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atomoxetine is a selective norepinephrine transporter inhibitor. It raises norepinephrine and dopamine in the prefrontal cortex, which is the accepted basis for its effect on ADHD core symptoms. The drug's own mechanism-of-action field is not populated in this Evidence Pack, so this description comes from the repurposing rationale.

"Specific developmental disorder" is a broad graph term. The trials and literature attached to it address ADHD, including ADHD comorbid with autism spectrum disorder. The evidence therefore supports neurodevelopmental, ADHD-type indications. It does not support learning or speech disorders in the strict sense.

Because atomoxetine is already marketed for ADHD, this prediction mainly confirms an existing use. The original-indication field is empty in the source data, so the label mapping should be verified before this is treated as a repurposing finding.

**Evidence level caveat:** The strict L1 rule requires at least 2 completed Phase 3 RCTs. Only one completed Phase 3 trial is listed (NCT00498173, n=60). The L1 rating rests on several completed Phase 4 randomized trials and on meta-analyses, so it should be read as "strong direct ADHD evidence" and not as a strict L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | Completed | 445 | Double-blind atomoxetine vs placebo in young adults with ADHD, including functional outcomes. Large and directly relevant (Grade A). |
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | Completed | 60 | Double-blind placebo-controlled trial of atomoxetine for ADHD symptoms in children with autism, Asperger's or PDD-NOS. Direct but small (Grade A). |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | Completed | 97 | Randomized double-blind atomoxetine vs placebo for ADHD symptoms in children and adolescents with autism spectrum disorder. |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | Completed | 128 | Atomoxetine with and without Parent Management Training vs placebo in children with autism-spectrum conditions and ADHD symptoms. |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | Completed | 396 | Guanfacine prolonged-release study in children and adolescents with ADHD, with atomoxetine as an active comparator. The main aim is long-term guanfacine treatment. |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1398 | ADDUCE project on chronic adverse effects of ADHD drugs (focus on methylphenidate). Indirect evidence. |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Mechanistic study of smoking reinforcement in adult ADHD. The endpoint is smoking behavior, not developmental disorder efficacy. |

NCT05635318 (qEEG neurofeedback add-on for ADHD, n=102, status unknown) was also retrieved. It is not an atomoxetine study, so it is left out of the table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Network meta-analysis | Lancet Psychiatry | Compares efficacy and acceptability of drug, psychological and neurostimulation interventions for adult ADHD. |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Systematic review/Meta-analysis | Autism Res | Atomoxetine for ADHD symptoms in children with autism. Three placebo-controlled RCTs, 241 children. |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Systematic review | Ther Adv Psychopharmacol | Efficacy of atomoxetine in ADHD with common comorbidities (oppositional, mood, anxiety, pervasive developmental and substance-use disorders). |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Systematic review | PLoS One | Sex differences in prescription rates and efficacy of ADHD pharmacotherapy in girls and women. |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohort | Neuropsychopharmacol Rep | Retrospective cohort identifying factors associated with atomoxetine efficacy in adult ADHD. |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | Clin EEG Neurosci | Quantitative EEG in childhood ADHD and learning disabilities. |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Case report | J Dev Behav Pediatr | Teletherapy and medication management (atomoxetine) in an 11-year-old with ADHD, anxiety, depression and suicidality. |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Preprint | bioRxiv | White-matter connectivity deviations in youths with ADHD predict symptom and treatment outcomes. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA079021 | Atomoxetine (Bryant Ranch Prepack) | Capsule | Not stated in the data |
| ANDA079016 | Atomoxetine (Rising Pharma Holdings, Inc.) | Capsule | Not stated in the data |
| ANDA079016 | Atomoxetine (American Health Packaging) | Capsule | Not stated in the data |
| ANDA078983 | Atomoxetine Hydrochloride (Golden State Medical Supply, Inc.) | Capsule | Not stated in the data |

Bryant Ranch Prepack appears twice under ANDA079021, and only the first entry is listed. All products are oral capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct randomized evidence supports atomoxetine in ADHD, including ADHD with autism, which is what "specific developmental disorder" maps to here. The strict L1 threshold is not met, and the graph term is broader than the evidence, so this is best treated as on-label confirmation and not as a new-indication discovery.

**To proceed, the following is needed:**
- Verify the label mapping: the original indication and the approved indication text are missing from the US license records.
- Obtain the package insert (warnings, contraindications) so safety screening can start.
- Obtain drug-level mechanism-of-action data from DrugBank.
- Confirm whether "specific developmental disorder" is meant to include learning or speech disorders. No evidence covers them.

The other predictions in the Evidence Pack (faciodigitogenital syndrome, chondromyxoid fibroma, trichotillomania, restless legs syndrome, manic bipolar disorder, transient tic disorder, both cerebellar ataxias) are rated Hold. Tourette syndrome is rated as a research question only.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

