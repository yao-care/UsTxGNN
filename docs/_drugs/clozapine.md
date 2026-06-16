---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Clozapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Clozapine: From Treatment-Resistant Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Clozapine is an atypical antipsychotic distinguished by its broad multi-receptor pharmacology, originally approved for treatment-resistant schizophrenia and recognized by the FDA for its anti-suicidal properties.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
with **6 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Treatment-Resistant Schizophrenia |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| US Market Status | Not marketed (0 authorizations found in regulatory query) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current evidence pack. Based on established pharmacology, Clozapine is a multi-acting receptor-targeted antipsychotic (MARTA) whose therapeutic signature rests on three key pillars: (1) **D2/D4 dopamine antagonism** with unusually low receptor affinity and rapid dissociation kinetics ("fast-off" theory), which suppresses the hyperdopaminergic state driving manic episodes while producing far fewer extrapyramidal side effects than conventional antipsychotics; (2) **5-HT2A/2C serotonin antagonism**, providing mood-stabilizing and antidepressant-augmenting effects; and (3) **broad ancillary receptor blockade** (H1 histamine, α1 adrenergic, M1–M4 muscarinic) contributing to sedation, anxiolysis, and behavioral control during acute mania.

The relationship between treatment-resistant schizophrenia and manic bipolar affective disorder is one of overlapping neurobiology rather than distinct pathology. Both conditions involve dysregulation of the mesolimbic dopamine pathway — excessive dopaminergic drive in mania mirrors the positive symptom profile of psychosis — making the mechanistic extrapolation from schizophrenia to mania conceptually sound. This is further supported by the clinical reality that a significant proportion of manic patients present with psychotic features, and that second-generation antipsychotics are now guideline-endorsed for acute mania.

The TxGNN prediction is particularly well-grounded: a 2020 systematic review and meta-analysis (PMID 32182485) directly evaluated clozapine's clinical efficacy in bipolar disorder, and a completed Phase 2 double-blind RCT (NCT00029458) specifically examined clozapine in treatment-resistant mania. The ongoing Phase 3 trial NCT05603104 (n=1,254) covering bipolar depression and schizophrenia could, upon completion, elevate the evidence to L1. Clozapine's unique anti-suicidal effect — the only FDA-approved anti-suicidal pharmacotherapy — is also highly relevant, given that bipolar disorder carries the highest suicide mortality among psychiatric conditions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind RCT evaluating clozapine safety and effectiveness for treatment-resistant manic phase of bipolar disorder — the most direct existing RCT evidence |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1,254 | Largest ongoing RCT on intensified pharmacological treatment for schizophrenia, MDD, and bipolar depression after first-line failure; results could elevate evidence to L1 |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates combination of pharmacotherapy with recovery-oriented programs (RECOVERYTRSBDGR) for treatment-resistant bipolar disorder |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | Active, not recruiting | 107 | Pharmacotherapy combined with individual cognitive behavioral therapy for mental health disorders including bipolar; assesses augmentation strategy |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | Unknown | 200 | Longitudinal MRI study of ECT effects on schizophrenia and bipolar disorder brain structure and function; no direct Clozapine intervention |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | Recruiting | 100 | NHS observational phenotyping study of general adult psychiatry inpatients; no direct efficacy evaluation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic Review + Meta-analysis | Journal of Psychiatric Research | Directly assessed clinical efficacy and adverse effect profile of clozapine in bipolar disorder; highest-quality synthesis on this topic |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic Review | Bipolar Disorders | Evaluated efficacy and safety of clozapine specifically for treatment-resistant bipolar disorder (TRBD); foundational systematic evidence |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Narrative Review | Bipolar Disorders | Summarized current state of knowledge and future directions for clozapine use in bipolar disorder |
| [40174308](https://pubmed.ncbi.nlm.nih.gov/40174308/) | 2025 | Retrospective Cohort | Journal of Psychiatric Research | Nationwide Korean health insurance database study comparing anti-suicidal effectiveness of clozapine, lithium, and valproate in bipolar disorder patients |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Clinical Review | Psychiatria Danubina | Argued that clozapine's anti-suicidal, anti-aggressive, and anti-impulsive properties make it a promising treatment for suicidality in bipolar disorder |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | Multicenter Observational | Journal of Clinical Psychopharmacology | Asian Psychotropic Prescription Patterns Consortium study on real-world clozapine prescribing patterns in bipolar disorder; provided clinical characteristics and dosing comparisons |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Guidelines Review | Acta Psychiatrica Scandinavica | Reviewed evidence-based treatment options for bipolar mania and proposed clinical guidance on mood stabilizer and antipsychotic selection |
| [37800205](https://pubmed.ncbi.nlm.nih.gov/37800205/) | 2023 | Epidemiological Review | Psychiatria Danubina | Examined shared dopaminergic dysfunction between bipolar disorder and Parkinson's disease, contextualizing the mechanistic relevance of D2 antagonism in mood disorders |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Molecular Psychiatry | Reviewed pharmacotherapy landscape for treatment-resistant bipolar disorder, positioning clozapine alongside lithium, valproate, and newer anticonvulsants |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case Series | Clinical Neuropharmacology | Reviewed 36 patients treated with combined ECT and clozapine; 67% benefited; combination was generally safe and well-tolerated |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data including key warnings, contraindications, and drug-drug interactions were not retrievable from the current evidence pack (data gaps flagged for TFDA package insert and DDI database). Prior to clinical use, review of the full prescribing information is essential — clozapine carries well-characterized serious risks (including agranulocytosis requiring mandatory hematologic monitoring under REMS protocols) that are critical for treatment planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind RCT (NCT00029458, n=42) directly supports clozapine's efficacy in treatment-resistant mania, and a 2020 systematic review with meta-analysis (PMID 32182485) provides the highest-quality synthesis of its use in bipolar disorder — together establishing L2 evidence. The mechanistic link is biologically coherent, the clinical need is real (treatment-resistant bipolar mania remains an unmet medical need), and the ongoing Phase 3 trial NCT05603104 (n=1,254) could upgrade evidence to L1 upon completion.

**To proceed, the following is needed:**

- **Full safety data**: Obtain and review the complete package insert, including agranulocytosis risk (~0.8%), myocarditis warnings, metabolic syndrome liability, and seizure threshold lowering — all critical for a benefit-risk assessment in the bipolar population
- **Mechanism of action documentation**: Complete DrugBank MOA data to formally document receptor binding profile for mechanistic dossier
- **US FDA regulatory status confirmation**: Clarify current US market authorization status and applicable REMS requirements (mandatory hematologic monitoring program)
- **Treatment-resistance definition alignment**: Establish clear criteria for "treatment-resistant" bipolar mania to define the target patient population for any repurposing protocol
- **Comparative effectiveness data**: Assess clozapine against approved alternatives for bipolar mania (lithium, valproate, quetiapine, aripiprazole) to position repurposing value
- **Monitoring protocol**: Develop a patient safety monitoring plan covering CBC with differential (minimum weekly for 6 months, then bi-weekly), metabolic panel, cardiac monitoring, and drug-drug interaction screening given clozapine's narrow therapeutic index
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

