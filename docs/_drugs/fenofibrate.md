---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Fenofibrate: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia…"
monitor_inn: "FENOFIBRATE"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "hypercholesterolemia, autosomal dominant"]
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a PPAR-alpha agonist originally used to treat hypertriglyceridemia and other forms of hyperlipidemia.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia**, but the direct evidence is very thin: the only registered trial is of a different drug (alirocumab), and the only fenofibrate-specific literature is a **1984 observational report**.
Of the other predicted indications, **Hyperlipoproteinemia** has far stronger support (**more than 20 clinical trials**, many of them Phase 3), but it overlaps with the drug's existing lipid uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia, familial combined hyperlipidemia, hypoalphalipoproteinemia (the US approved-indication text is not available in the data, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (see the note below the table) |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 16 authorizations in total (1 NDA and 15 ANDAs), all cancelled |
| Recommended Decision | Hold |

For this top-ranked indication, the data compiled for this report assign evidence level L4 and a "Hold" recommendation. Under the standard rules, a model-only prediction would be L5. L4 is used here because only indirect, mechanism-level or small observational support exists.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general pharmacology, fenofibrate activates PPAR-alpha. This increases lipoprotein lipase activity and fatty-acid oxidation and reduces hepatic VLDL production. The result is lower triglycerides, higher HDL-C, and a modest reduction in LDL-C.

The link to the predicted indication is weak. Homozygous familial hypercholesterolemia is driven by LDL receptor dysfunction, and PPAR-alpha activation is not expected to correct that core defect. Support is indirect: a 1984 study in type II hyperlipoproteinemia included one homozygous FH patient who showed the greatest fall in total and LDL cholesterol. There are also general lipid-lowering reviews. This is not enough to establish efficacy.

The model's score is likely driven by the broad similarity between lipid disorders rather than a specific mechanistic match. Other predicted indications are better supported:

- **Hyperlipoproteinemia** (score 99.65%): the indication overlaps with the drug's approved uses. It is better described as an on-label or near-label use than as true repurposing. It is rated L1 with a "Proceed with Guardrails" recommendation.
- **Familial hypercholesterolemia** (99.62%) and **autosomal dominant hypercholesterolemia** (99.05%): older studies show fenofibrate, alone or with colestipol, changes lipid profiles. The effect is modest and it is mainly an adjunct. Both are L3 "Research Question".
- **Hyperlipidemia due to hepatic triglyceride lipase deficiency** (99.42%): a small 2005 kinetic study in two patients. L3 "Research Question".
- **CETP deficiency** (99.61%) and **CYP7A1-deficiency hypercholesterolemia** (99.52%): only preclinical evidence or none. Hold.

---

## Clinical Trial Evidence

Only one registered trial is linked to the top-ranked indication, and it does not test fenofibrate:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) in children and adolescents with HoFH. No evidence on fenofibrate. |

For context, the strongest fenofibrate trials sit under the related indication **Hyperlipoproteinemia / mixed hyperlipidemia**:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00349375](https://clinicaltrials.gov/study/NCT00349375) | Phase 3 | Completed | 1040 | Fenofibrate 145 mg + simvastatin vs simvastatin alone in mixed dyslipidemia |
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Phase 3 | Completed | 630 | Fenofibrate vs pravastatin in HIV-infected patients with lipid abnormalities |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00362934](https://clinicaltrials.gov/study/NCT00362934) | Phase 3 | Completed | 516 | Fenofibrate + simvastatin vs atorvastatin in mixed dyslipidemia |
| [NCT00459745](https://clinicaltrials.gov/study/NCT00459745) | Phase 3 | Completed | 481 | Pravastatin vs fenofibrate vs the combination (Pravafen) in combined hyperlipidemia; double-blind with a 52-week open-label extension |
| [NCT01956201](https://clinicaltrials.gov/study/NCT01956201) | Phase 3 | Unknown | 476 | Fenofibrate added to atorvastatin vs atorvastatin alone in mixed hypercholesterolemia; results should be verified |
| [NCT00352183](https://clinicaltrials.gov/study/NCT00352183) | Phase 3 | Completed | 450 | Fenofibrate 145 mg + simvastatin 40 mg vs simvastatin alone |
| [NCT00362206](https://clinicaltrials.gov/study/NCT00362206) | Phase 3 | Completed | 423 | Fenofibrate + simvastatin vs pravastatin alone in mixed dyslipidemia |
| [NCT01878227](https://clinicaltrials.gov/study/NCT01878227) | Phase 3 | Completed | 420 | Head-to-head comparison of a coenzyme A capsule with fenofibrate in Chinese patients with moderate dyslipidemia |

These trials support fenofibrate for mixed hyperlipidemia, not for HoFH.

---

## Literature Evidence

Literature linked to homozygous familial hypercholesterolemia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | In 22 patients with type II hyperlipoproteinemia on fenofibrate 300 mg/day, LDL-C fell about 24% (31% in familial hypercholesterolemia). One homozygous FH patient showed the greatest fall in total and LDL cholesterol. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin drugs review. The most definite fenofibrate indication is fasting triglyceride >500 mg/dl, to reduce acute pancreatitis risk. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidemic children; fenofibrate is among agents that reduced lipids in familial hypercholesterolemia |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide (approved for HoFH) pharmacokinetic interactions with lipid-lowering drugs including fenofibrate |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL cholesterol, statins and PCSK9 inhibitors |

Most of the remaining retrieved items are general reviews on statins, ezetimibe or pregnancy-related dyslipidemia and add no direct support.

---

## US Market Information

All 16 US authorizations are listed as cancelled; none is currently active. The approved-indication text was not available for any of them. Five representative entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021695 | ANTARA (Lupin Pharmaceuticals) | Capsule | Not available |
| ANDA076509 | Fenofibrate (Amneal) | Tablet | Not available |
| ANDA209660 | Fenofibrate (Alembic) | Tablet, film coated | Not available |
| ANDA211407 | Fenofibrate (Chartwell RX) | Capsule | Not available |
| ANDA202252 | Fenofibrate (Apotex) | Capsule | Not available |

All available formulations are oral (tablet, film-coated tablet, capsule).

---

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report; please refer to the current package insert.

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, liver disease, pancreatitis, gallbladder disease and cholelithiasis, myopathy and rhabdomyolysis, impaired renal function, and blood-cell disorders (thrombocytopenia, anemia, leukopenia, agranulocytosis, neutropenia and related congenital neutropenia syndromes).
- **Drug interactions**: 100 interactions were found; the 20 listed are all rated Moderate. They include sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro and others), chenodeoxycholic acid and esomeprazole. The sulfonylurea and insulin interactions suggest monitoring of glucose control when combined.

---

## Conclusion and Next Steps

**Decision: Hold** (for homozygous familial hypercholesterolemia)

**Rationale:**
- The model score is very high (99.91%), but no trial tests fenofibrate in HoFH, and the only supporting literature is a 1984 report that included a single homozygous patient. Fenofibrate does not address the LDL receptor defect, and approved options for HoFH already target LDL directly.
- By contrast, the **Hyperlipoproteinemia** indication has L1 evidence (multiple completed Phase 3 randomized trials) and a "Proceed with Guardrails" recommendation. It is largely an on-label use, so it offers little true repurposing value.

**To proceed, the following is needed:**
- Mechanism-of-action data, to evaluate any rationale beyond triglyceride and HDL effects
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Any controlled or case-series data of fenofibrate as an add-on therapy in HoFH
- Clarification of why all 16 US licenses are cancelled and whether the drug is still marketed under other labels
- Dedicated safety monitoring planning for liver, kidney, muscle and blood-count effects, and for glucose-lowering drug co-use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

