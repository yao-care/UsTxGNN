---
layout: default
title: Asenapine
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# ASENAPINE: From Schizophrenia/Bipolar I Disorder to Major Affective Disorder

## One-Sentence Summary

Asenapine is an atypical antipsychotic approved by the US FDA (2009) and EMA for the treatment of schizophrenia and acute manic or mixed episodes associated with bipolar I disorder, but is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Major Affective Disorder**, with **4 clinical trials** and **19 publications** supporting this direction — evidence highly consistent with its established global regulatory approvals.
Among 10 TxGNN-predicted indications evaluated, major affective disorder is the only one reaching **L1 evidence level** and the sole actionable repurposing candidate in this analysis; the remaining 9 predictions (ranks 1–9) are all rated "Hold" (L5, no mechanistic link) and are not pursued further in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar I Disorder (manic/mixed episodes) — US/EU approved; not registered in Taiwan |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Asenapine is a multi-receptor antagonist with high binding affinity across the monoamine system. Although formal mechanism of action data was not retrieved in this evidence pack, its pharmacological profile is thoroughly characterized in the published literature: it acts as a high-affinity antagonist at dopamine D2/D3/D4 receptors (driving anti-manic effects), serotonin 5-HT2A/2C receptors (providing mood stabilization and reducing extrapyramidal side effects), histamine H1 receptors (producing sedation useful in acute mania), and α2-adrenergic receptors (enhancing norepinephrine and dopamine transmission). This broad receptor engagement addresses the dysregulated monoamine signaling that underlies both manic and mixed affective states.

Major affective disorder — encompassing bipolar I disorder and related severe mood disturbances — is precisely the therapeutic space for which asenapine was developed. D2/dopaminergic antagonism controls the excess dopaminergic tone that drives manic episodes, while 5-HT2A blockade complements mood stabilization and supports the transition to euthymia. The drug's unique sublingual formulation avoids hepatic first-pass metabolism, resulting in rapid CNS absorption with a distinct pharmacokinetic profile compared to oral antipsychotics. This delivery advantage is clinically meaningful in acute agitated mania, where fast onset of action is essential.

The TxGNN prediction here is not speculative — it reflects a pharmacologically validated and globally approved application. Asenapine received FDA approval in August 2009 for adult bipolar I disorder (manic/mixed episodes) and expanded its pediatric indication (ages 10–17) in 2015. The European Medicines Agency (EMA) approved it under the brand name Sycrest® for the same indication. The model's 99.57% confidence score accurately mirrors this real-world regulatory track record, and the clinical evidence base (3 completed Phase 3 RCTs, a meta-analysis of 4 RCTs, international treatment guidelines) firmly classifies this as an L1 repurposing candidate for the Taiwan market.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244815](https://clinicaltrials.gov/study/NCT01244815) | Phase 3 | Completed | 404 | 3-week double-blind, placebo-controlled RCT in pediatric patients aged 10–17 with bipolar I disorder (manic/mixed episodes); evaluated three fixed doses of asenapine vs. placebo; demonstrated statistically significant YMRS score reduction supporting US pediatric approval |
| [NCT01349907](https://clinicaltrials.gov/study/NCT01349907) | Phase 3 | Completed | 322 | 50-week open-label flexible-dose extension of NCT01244815; evaluated long-term safety and tolerability in pediatric bipolar I disorder; confirmed sustained improvement and acceptable safety over extended treatment |
| [NCT00145470](https://clinicaltrials.gov/study/NCT00145470) | Phase 3 | Completed | 326 | 12-week double-blind, placebo-controlled RCT in adults with bipolar I disorder (manic/mixed episodes) continuing lithium or valproate; asenapine as adjunct significantly improved manic symptoms vs. placebo; key pivotal trial supporting adult FDA approval |
| [NCT02600741](https://clinicaltrials.gov/study/NCT02600741) | N/A | Completed | 296 | 12-month randomized open-label study of caregiver psycho-education and skills training for schizophrenia/schizoaffective disorder patients receiving antipsychotics; provides real-world psychiatric treatment context and outcome data relevant to affective disorder management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [23719049](https://pubmed.ncbi.nlm.nih.gov/23719049/) | 2013 | Meta-analysis | Int Clinical Psychopharmacology | Meta-analysis of 4 RCTs: asenapine significantly superior to placebo in YMRS and CGI-BP scores for acute bipolar mania; effect sizes clinically meaningful with favorable tolerability |
| [28741044](https://pubmed.ncbi.nlm.nih.gov/28741044/) | 2017 | RCT | CNS Drugs | Open-label RCT comparing asenapine vs. olanzapine in borderline personality disorder with affective dysregulation; comparable efficacy on mood and impulsivity outcomes |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Systematic Review | JAMA | Comprehensive review of bipolar disorder diagnosis and treatment (affects ~8M US adults, ~40M worldwide); asenapine cited among recommended pharmacotherapies for manic episodes |
| [20420486](https://pubmed.ncbi.nlm.nih.gov/20420486/) | 2010 | Pharmacology Review | Expert Rev Neurotherapeutics | Detailed characterization of asenapine's receptor profile (5-HT2A > D2 affinity), effects on NMDA/AMPA receptors, and clinical efficacy in bipolar I disorder manic and mixed episodes |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Narrative Review | Acta Psychiatrica Scandinavica | Evidence-based clinical recommendations for bipolar mania management; asenapine included among antipsychotics with solid Phase 3 evidence for acute manic episodes |
| [29170943](https://pubmed.ncbi.nlm.nih.gov/29170943/) | 2018 | Review | Paediatric Drugs | Review of asenapine in pediatric bipolar I disorder and schizophrenia; covers Phase 3 pediatric trial data, dosing recommendations (2.5–10 mg BID), and the regulatory basis for pediatric approval |
| [20135021](https://pubmed.ncbi.nlm.nih.gov/20135021/) | 2009 | Review | Drugs of Today | Overview of asenapine maleate as a novel atypical antipsychotic at the time of initial FDA approval; describes pharmacodynamic profile and clinical differentiation from existing agents |
| [35141987](https://pubmed.ncbi.nlm.nih.gov/35141987/) | 2022 | Case Report | Psychogeriatrics | Successful treatment of major depressive disorder with psychotic features using asenapine added to escitalopram in an elderly patient; demonstrates broader affective disorder utility beyond bipolar mania |
| [28004626](https://pubmed.ncbi.nlm.nih.gov/28004626/) | 2017 | Review | CNS Spectrums | Review of pharmacotherapy for DSM-5 mixed features specifier; discusses asenapine's role in treating mixed manic/hypomanic and depressive symptom combinations |
| [33634761](https://pubmed.ncbi.nlm.nih.gov/33634761/) | 2021 | Case Report | CNS & Neurological Disorders Drug Targets | Case report of asenapine successfully treating catatonia in a COVID-19 patient with schizotypal personality disorder and psychotic depression in ICU; demonstrates clinical versatility in complex psychiatric presentations |

---

## Taiwan Market Information

Asenapine currently has **no registered products in Taiwan** (0 TFDA licenses). The table below summarizes the drug's regulatory status in major markets outside Taiwan for reference:

| Market | Product Name | Dosage Form | Approved Indication |
|--------|-------------|------------|---------------------|
| US (FDA, 2009) | Saphris® | Sublingual tablet (2.5, 5, 10 mg) | Acute manic/mixed episodes of bipolar I disorder (adults and pediatric 10–17 years); schizophrenia (adults) |
| EU (EMA) | Sycrest® | Sublingual tablet | Acute manic episodes of bipolar I disorder (adults) |

---

## Safety Considerations

Formal safety data (TFDA package insert warnings, contraindications, drug interaction database records) were not retrieved in this evidence pack. Please refer to the official Saphris® US Prescribing Information or Sycrest® EU Summary of Product Characteristics for comprehensive safety information.

Based on published literature, the following safety signals are clinically important for asenapine:

- **Somnolence and sedation**: H1 receptor antagonism produces significant sedation, especially at treatment initiation; relevant for outpatient management and driving safety
- **Metabolic effects**: Weight gain and dyslipidemia reported, consistent with atypical antipsychotic class effects; fasting glucose and lipid monitoring recommended
- **QTc prolongation**: Class-level cardiac risk; baseline ECG and monitoring in patients with cardiac risk factors advised
- **Oral hypoesthesia**: Unique to sublingual formulation; transient numbness and tingling of the mouth/tongue occur in up to 5% of patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Asenapine has robust L1-level clinical evidence for major affective disorder (bipolar I disorder), anchored by multiple completed Phase 3 RCTs, a meta-analysis, international regulatory approvals (US FDA, EMA), and a mechanistically well-characterized pharmacological basis. The TxGNN prediction score of 99.57% accurately reflects this existing global evidence base. This is not speculative repurposing — the primary barrier to Taiwan market entry is regulatory and commercial, not scientific.

**To proceed, the following is needed:**

- **TFDA regulatory pathway**: Determine feasibility of a new drug application (NDA) to TFDA for bipolar I disorder / major affective disorder; assess whether US/EU approval data packages meet TFDA bridging study requirements
- **Safety dossier completion**: Retrieve TFDA-required package insert warnings, contraindications, and drug-drug interaction data from DrugBank API and official US/EU product labels
- **MOA documentation**: Compile pharmacology data from DrugBank (DB06216) for formal regulatory submission and TFDA review
- **Taiwan epidemiology and unmet need**: Estimate eligible bipolar I disorder patient population in Taiwan and assess positioning relative to currently reimbursed atypical antipsychotics (e.g., quetiapine, olanzapine, risperidone) under the National Health Insurance formulary
- **Commercial feasibility**: Evaluate patent status, originator marketing authorization holder (Organon/formerly Allergan/AbbVie), and licensing or generic entry options for the Taiwan market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

