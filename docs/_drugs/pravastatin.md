---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 1076
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Pravastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Hyperlipidemia, atherosclerosis, stroke and cerebrovascular disorders"
monitor_inn: "PRAVASTATIN"
predicted_indications: ["homozygous familial hypercholesterolemia", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hypoalphalipoproteinemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Pravastatin: From Hyperlipidemia and Atherosclerosis to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) originally used for hyperlipidemia, atherosclerosis and stroke-related conditions.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia**,
but the supporting evidence is indirect: **1 clinical trial** (which tests a different drug) and **12 publications** (mostly reviews of other lipid-lowering agents).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, atherosclerosis, stroke and cerebrovascular disorders (the FDA licence records have no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all 5 listed ANDAs are cancelled) |
| Number of NDAs | 5 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Pravastatin is a well-known HMG-CoA reductase inhibitor. It lowers LDL cholesterol by reducing hepatic cholesterol synthesis and upregulating LDL receptors, and it has an established role in hyperlipidemia and atherosclerosis.

Familial hypercholesterolemia is a closely related lipid disorder, so the TxGNN prediction is biologically plausible. There is an important caveat, however. Homozygous FH is characterized by severe LDL receptor deficiency, and statin efficacy depends on residual receptor activity. One review in the data states that statins are not very effective in homozygous FH. The expected benefit is therefore likely limited compared with heterozygous FH.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab study in children and adolescents (8–17 years) with HoFH. It does not test pravastatin and provides disease context only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Review | Cochrane Database Syst Rev | Earlier version of the review of statins in children with FH |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT | Lancet HIV | INTREPID: pitavastatin vs pravastatin in HIV-related dyslipidaemia (not an FH population) |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Review | Endocr Pract | AACE/ACE guidelines for dyslipidemia management |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Commentary | Prescrire Int | Notes pravastatin and simvastatin are reference statins for heterozygous FH, and that statins are not very effective in homozygous FH |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin indicated for HoFH (other drug) |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review, superior to pravastatin in lipid improvement |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe review |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Ezetimibe as a cholesterol absorption inhibitor |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin review |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077793 | Pravastatin sodium (Aurobindo Pharma) | Tablet | Not recorded (cancelled) |
| ANDA077987 | Pravastatin Sodium (A-S Medication Solutions) | Tablet | Not recorded (cancelled) |
| ANDA209869 | Pravastatin sodium (Golden State Medical Supply) | Tablet | Not recorded (cancelled) |
| ANDA076341 | Pravastatin sodium (RemedyRepack) | Tablet | Not recorded (cancelled) |
| ANDA076714 | Pravastatin sodium (Dr. Reddy's Laboratories) | Tablet | Not recorded (cancelled) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for authoritative safety information.

- **Knowledge-graph contraindication signals** (not label text): kidney disease, liver disease, gallbladder disease, myopathy and other muscle disease, rhabdomyolysis, thrombocytopenia, peptic ulcer disease, gout, hemophilia, anemia, nephrolithiasis, hypercalcemia, and others. These should be verified against the label.
- **Drug Interactions**: 100 interactions were identified. The moderate-level ones listed include metronidazole, clarithromycin, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin and tinidazole. Combining pravastatin with other statins (rosuvastatin, simvastatin) deserves particular attention.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only linked trial tests a different drug (alirocumab), and the literature does not directly evaluate pravastatin in homozygous FH. Statins are also expected to have limited efficacy in this disease because of LDL receptor deficiency. All US licences are cancelled, and the label safety data is missing.

**To proceed, the following is needed:**
- Pravastatin-specific efficacy data in homozygous FH patients (for example, LDL-C response in receptor-negative vs receptor-defective patients)
- Comparison with established HoFH therapies
- Package insert warnings and contraindications from the FDA label
- Mechanism of action data and clarification of the market and licensing situation

**Other predictions of note:** Two other predictions have more substantial evidence. **Familial hypercholesterolemia** (heterozygous; L2, with pediatric pravastatin pharmacokinetic and randomized studies) and **HIV-associated dyslipidemia** (L2, with a Phase 3 fenofibrate-vs-pravastatin trial and several Phase 4 trials) are better candidates for follow-up. Both are about positioning within an established drug class rather than true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

