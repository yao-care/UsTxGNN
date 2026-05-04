---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the `txgnn-pipeline` skill to ensure alignment with the TxGNN reporting workflow, and the system prompt's **Drug Repurposing Evaluation Report Prompt v5** to structure the output. Now generating the report.

---

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) established as a treatment for major depressive disorder.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **30 clinical trials** and **16 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| US Market Status | No records found in current database (possible data gap — Celexa is an established SSRI) |
| Number of NDAs | 0 (no records retrieved; recommend FDA Orange Book verification) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not captured in the current evidence pack. Based on established pharmacology, citalopram is an SSRI that selectively blocks the serotonin transporter (SERT), increasing synaptic 5-HT concentrations in the brain. This mechanism underlies its efficacy across depression and anxiety-spectrum conditions and is directly relevant to OCD pathophysiology.

OCD's core pathology involves hyperactivation of the orbitofrontal cortex–striatum–thalamus feedback circuit. Boosting serotonergic tone via SERT inhibition dampens this dysfunctional loop. The strongest indirect validation comes from the FDA's own approval record: all four pharmacotherapies currently approved for OCD (fluvoxamine, fluoxetine, sertraline, and paroxetine) are SSRIs from the same drug class as citalopram, establishing a clear class-level mechanism.

Citalopram's active S-enantiomer, escitalopram, has been directly studied in OCD across multiple Phase 3 and Phase 4 RCTs with demonstrated efficacy and dose-response data. Additionally, two published open-label trials have directly investigated citalopram itself in OCD patients — including treatment-resistant cases — with clinically meaningful Y-BOCS score improvements. These converging lines of evidence make the TxGNN prediction mechanistically sound and empirically grounded.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | **Directly tests citalopram** vs placebo in children with autism and high-level repetitive/compulsive behaviors — provides efficacy and safety data specific to citalopram in OCD-spectrum symptoms |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | fMRI proof-of-concept study of **citalopram's effect** on restricted repetitive behaviors in autism spectrum disorders — neuroimaging evidence of citalopram's modulation of compulsive behavior circuits |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized, double-blind, multi-center RCT comparing conventional (20 mg) vs high-dose (40 mg) escitalopram in OCD; evaluated with Y-BOCS, HAM-D, CGI — robust dose-finding trial for the active enantiomer |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assesses efficacy and optimal dose of escitalopram for OCD — direct bridge from active enantiomer to citalopram |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | 18-week open-label prospective study of high-dose escitalopram (20–50 mg/d) for OCD outpatients — evaluates tolerability at supratherapeutic doses often needed in OCD |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Tests whether CBT augmentation improves outcomes in pediatric OCD patients with partial SRI response — confirms SSRI as the pharmacological backbone requiring optimization |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Randomized open trial comparing quetiapine vs clomipramine augmentation of SSRI for OCD non-responders — validates SSRI as the standard first-line treatment requiring augmentation strategy |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compares SSRI alone, ERP alone, and combination therapy for OCD in Chinese patients; identifies biological and psychological predictors of response |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Randomized comparison of escitalopram vs clomipramine (vs duloxetine) to predict OCD medication response — identifies biomarkers relevant to citalopram-class treatments |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Large multinational naturalistic follow-up of OCD patients (NIH-funded); evaluates clinical, neurocognitive, and neuroimaging predictors of treatment response across international sites |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Comprehensive Psychiatry | Long-term safety and tolerability of off-label high-dose SRIs in OCD — supports dose escalation as a strategy for refractory patients across the SRI class including citalopram |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | Journal of Affective Disorders | OCD demonstrates a smaller placebo and antidepressant response than other anxiety disorders — critical for designing adequately powered OCD trials and interpreting effect sizes |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-analysis | Journal of Psychiatric Research | Network meta-analysis of pharmacological and psychological treatments for pediatric OCD — confirms SSRIs are efficacious across age groups, supports class-level evidence |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opinion on Pharmacotherapy | Systematic review of RCTs for OCPD pharmacotherapy — highlights SRI class as the most-studied pharmacotherapy in OCD-spectrum conditions |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Meta-review of antidepressants in children/adolescents across disorders including OCD — summarizes SSRI efficacy, tolerability, and suicidality signal relevant to prescribing decisions |
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Systematic Review | Nordic Journal of Psychiatry | Fluoxetine systematic review in pediatric OCD — demonstrates the SSRI class effect; findings transferable to citalopram as a same-class agent |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Open-label Trial | International Clinical Psychopharmacology | **Citalopram directly tested in OCD** — foundational paper titled "Beyond depression: citalopram for OCD"; establishes citalopram's efficacy and contextualizes the serotonin hypothesis of OCD |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Open-label Trial | European Psychiatry | **Citalopram for treatment-resistant OCD** — 16-patient randomized open-label trial comparing citalopram alone vs citalopram + clomipramine in patients who had failed prior SRI treatment; Y-BOCS outcomes reported |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Narrative Review | BMJ Clinical Evidence | Comprehensive overview of OCD epidemiology (~1–1.5% adult prevalence) and evidence-based treatment — confirms SSRIs as first-line pharmacotherapy with established long-term efficacy |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World Journal of Biological Psychiatry | "OCD: serotonin and beyond" — reviews the neurobiology of OCD and the centrality of serotonergic pharmacotherapy; directly supports the mechanistic rationale for citalopram repurposing |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for formulary review:** Clinicians should be aware that SSRIs as a class carry established warnings for QT-interval prolongation (particularly relevant for citalopram at higher doses), serotonin syndrome risk with co-medications, increased suicidality in patients under 25, and discontinuation syndrome. These should be formally retrieved from the FDA-approved labeling before clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The serotonergic mechanism of citalopram is mechanistically identical to all four currently FDA-approved OCD pharmacotherapies, and its active enantiomer (escitalopram) has demonstrated efficacy in multiple completed Phase 3/4 RCTs. Two open-label trials have directly tested citalopram itself in OCD patients with positive results, providing an evidence base sufficient to move forward under structured monitoring.

**To proceed, the following is needed:**

- **Regulatory verification**: Retrieve citalopram's official US FDA authorization status from the FDA Orange Book or DailyMed (the current evidence pack returned 0 records, which is likely a data collection gap)
- **Full safety dossier**: Obtain complete warnings, contraindications, and drug interactions — particularly QT prolongation risk at OCD-range doses, serotonin syndrome interactions, and pediatric suicidality black box warning
- **MOA documentation**: Pull formal mechanism of action from DrugBank (DB00215) to complete the mechanistic narrative
- **Direct OCD RCT**: Commission or identify a prospective, placebo-controlled RCT for citalopram specifically in OCD (adults ± children) to upgrade from bridging evidence (L2) to direct evidence (L1)
- **Dose-ranging guidance**: OCD typically requires higher SSRI doses than depression; a dose-optimization protocol should be defined before clinical implementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

