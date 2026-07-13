---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine (Pristiq) is a serotonin-norepinephrine reuptake inhibitor (SNRI) — the active metabolite of venlafaxine — FDA-approved in the United States for major depressive disorder, though it currently holds no marketing authorisation in Taiwan.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **2 clinical trials** and **4 publications** currently identified — however, neither trial tested desvenlafaxine as a primary OCD treatment, making all available evidence indirect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (US FDA-approved as Pristiq; no Taiwan licence on record) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Desvenlafaxine is the major active metabolite of venlafaxine, sharing the same core pharmacology: potent and balanced inhibition of both the serotonin (SERT) and norepinephrine (NET) transporters. Although detailed mechanism-of-action data from DrugBank were not retrieved in this evidence pack, the SNRI classification is well-established in the clinical literature (see PMID 14624187, 24766145, 37032427). Its serotonin reuptake inhibition is particularly pronounced and is considered the primary driver of antidepressant efficacy.

OCD is one of the psychiatric disorders most tightly linked to serotonergic dysregulation, specifically in the cortico-striato-thalamo-cortical (CSTC) circuit. First-line pharmacotherapy consists of SSRIs and the tricyclic clomipramine — both of which work primarily through serotonin reuptake inhibition. SNRIs are a mechanistically logical next step, and critically, **venlafaxine — desvenlafaxine's parent compound — has direct Phase 2/3 RCT evidence in OCD** (PMID 14624187), demonstrating comparable efficacy to paroxetine in 150 patients. Since desvenlafaxine is the pharmacologically active form that venlafaxine is converted to in vivo, a class-effect extrapolation is biologically defensible.

That said, desvenlafaxine has not been studied as a primary OCD treatment. NCT03299166 permitted desvenlafaxine as a background therapy while testing troriluzole as an adjunct, and NCT01527786 studied postpartum depression and was misclassified to this indication. The mechanistic case is promising, but the clinical evidence gap between the parent compound (venlafaxine) and desvenlafaxine in OCD remains to be directly bridged.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Randomised double-blind trial of troriluzole vs. placebo as adjunctive therapy in OCD patients with inadequate response to SSRI, clomipramine, venlafaxine, **or desvenlafaxine**; desvenlafaxine served as an eligible standard background treatment, not the investigational drug — constitutes indirect OCD-setting evidence |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Pilot study of functional outcomes in postpartum depression treated with desvenlafaxine; not an OCD trial — classified here due to PPD–OCD comorbidity literature linkage, not primary indication relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | Journal of Clinical Psychopharmacology | First double-blind RCT comparing an SNRI (venlafaxine) vs. paroxetine in 150 OCD patients; venlafaxine showed comparable efficacy — the most directly relevant proxy evidence for desvenlafaxine's potential in OCD via class effect |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of double-blind trials testing serotonergic antidepressants in OCD, including SNRI data; contextualises the mechanistic rationale for the 5-HT agent class in OCD pharmacotherapy |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression noting that OCD can emerge as a downstream complication of PPD; limited direct relevance to desvenlafaxine–OCD efficacy |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical Study | Psychiatry and Clinical Psychopharmacology | Risperidone augmentation in antidepressant-resistant somatic symptom disorder, mentioning OCD augmentation context incidentally; peripheral relevance to desvenlafaxine–OCD |

---

## Taiwan Market Information

Desvenlafaxine is **not licensed or marketed in Taiwan**. No TFDA New Drug Applications (NDAs) were found in the regulatory database as of the data cutoff (2026-06-21).

> **Note:** Desvenlafaxine is FDA-approved in the United States under the brand name **Pristiq** (Pfizer) for the treatment of major depressive disorder in adults, as confirmed by clinical trial references (NCT01537068 brief summary: *"Desvenlafaxine [trade name Pristiq] has been approved by the FDA for the treatment of major depression"*).

---

## Safety Considerations

Please refer to the package insert for safety information.

> TFDA package insert data were not retrieved in this evidence pack (Data Gap DG001: Blocking severity). US FDA label for Pristiq should be consulted for warnings, contraindications, and drug interaction profiles before any clinical use or protocol design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial has directly tested desvenlafaxine as a primary treatment for OCD; the strongest mechanistic link runs through venlafaxine (parent compound) rather than desvenlafaxine itself, and current evidence does not meet the minimum threshold for advancing to a formal repurposing evaluation. The L4 evidence classification reflects preclinical/mechanism-level support only.

**To proceed, the following is needed:**
- A dedicated Phase 2 pilot RCT or open-label study evaluating desvenlafaxine monotherapy or augmentation specifically in OCD patients
- Retrieval and parsing of the US FDA Pristiq label (and TFDA application if pursued) to document key warnings, contraindications, and drug interactions
- DrugBank API query to obtain complete MOA data, including receptor binding affinities and transporter selectivity profile
- Targeted literature search for desvenlafaxine (not venlafaxine as proxy) in OCD — including case series, naturalistic studies, and pharmacovigilance signals
- Drug interaction assessment for OCD co-medications commonly used alongside SNRIs (clomipramine, atypical antipsychotics, benzodiazepines)
- TFDA marketing authorisation pathway assessment, given current 未上市 status in Taiwan

> **💡 Higher-priority candidates identified in this evidence pack:** The dysthymic disorder indication (Rank 8, L3 evidence, 3 direct clinical trials including a Phase 4 RCT) and melancholia/MDD indication (Rank 10, L2 evidence, 19 publications including multiple meta-analyses and a head-to-head RCT) both carry substantially stronger evidence bases and are recommended as higher-priority targets for accelerated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

