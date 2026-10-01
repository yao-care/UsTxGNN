---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 754
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a pancreatic peptide hormone, marketed in the US mainly as an emergency treatment for severe hypoglycemia. The TxGNN model predicts it may help with **irritable bowel syndrome (IBS)**, with a very high score of 99.2%.
The **11 clinical trials** and **20 publications** retrieved almost all concern GLP-1 receptor agonists (a related peptide class) or non-drug interventions. **None tests glucagon itself in IBS.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records supplied; severe hypoglycemia is inferred from the marketed products (e.g., Gvoke, Zegalogue) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 (mechanistic and preclinical support only, from a related drug class) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glucagon is not available in the Evidence Pack. Glucagon and GLP-1 both derive from proglucagon, and both inhibit gastrointestinal smooth muscle motility. Glucagon is already used as a short-acting GI spasmolytic during diagnostic procedures.

IBS is driven largely by abnormal gut motility and visceral pain. A drug that relaxes gut muscle could plausibly reduce spasm and pain. The stronger support comes from GLP-1 analogs. For example, ROSE-010 reduced pain during IBS attacks and slowed gastric emptying in constipation-predominant IBS (IBS-C). Animal studies also show GLP-1 receptor activation improves gut dysfunction in IBS models.

This is an inference from a related peptide class, not direct evidence for glucagon. Glucagon's short half-life and its tendency to raise blood glucose and cause nausea would also limit chronic use in IBS.

---

## Clinical Trial Evidence

Most trials below study GLP-1 drugs, diet, or exercise, not glucagon.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (GLP-1 analog) on gut motor function in women with IBS-C; supports the GLP-1 pathway only |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs ROSE-010 on stomach and small-intestine motility; shows GLP-1 inhibits gut motility, not tested in IBS patients |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide vs placebo in ileal pouch patients with high bowel frequency; too small to be informative |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Two exercise programs and their effect on gut bacteria and GLP-1 levels in IBS; no drug tested |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Butyrate's mode of action in the human colon; loosely related through gut hormone readouts |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Fructo-oligosaccharide supplement in reactive hypoglycemia; nutritional, not glucagon-based |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Rye bread and the gut-brain axis in healthy people; nutrition study |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Fiber and polyphenol blend for gut barrier integrity at simulated high altitude; nutrition study |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-energy diet with or without intragastric balloon in obesity; not relevant to IBS |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Eating rate of ultra-processed foods and intake; not relevant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol Gastrointest Liver Physiol | Randomized, placebo-controlled dose-response study of ROSE-010 (GLP-1 analog) on GI motor function in women with IBS-C |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT (cross-analysis) | Scand J Gastroenterol | ROSE-010 reduced pain during IBS attacks; exploratory analysis to find the best-responding patient subgroup |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic review | Front Endocrinol | Meta-analysis on GLP-1 receptor agonists in IBS; GLP-1 and ROSE-010 inhibit gut motility in IBS patients |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Real-world prescribing and discontinuation of GLP-1 agonists in IBS patients; GI side effects are a concern |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Role of GLP-1-secreting L-cells in IBS pathophysiology |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 as a possible treatment for diabetes and IBS |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational | Clin Res Hepatol Gastroenterol | Lower GLP-1 levels correlate with abdominal pain in IBS-C |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical (rat) | Neurogastroenterol Motil | GLP-1 agonist exendin-4 improved gut dysfunction in a rat IBS model |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclinical (rat) | Int J Mol Med | GLP-1 involvement in gut motility and visceral hypersensitivity in rat IBS models |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Novel investigational drugs for IBS-C |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA201849 | Glucagon (Fresenius Kabi USA) | Injection, powder, lyophilized, for solution | Not specified in source data |
| NDA212097 | Gvoke HypoPen (Xeris) | Injection, solution | Not specified in source data |
| NDA212097 | Gvoke PFS (Xeris) | Injection, solution | Not specified in source data |
| NDA214231 | Zegalogue (Novo Nordisk) | Injection, solution | Not specified in source data |
| Not listed | Glucagon (Professional Complementary Health Formulas) | Liquid | Not specified in source data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the supporting clinical work tests GLP-1 analogs, not glucagon, so this remains a research question. Glucagon's short half-life, hyperglycemic effect, and nausea also make chronic IBS use unlikely without a new formulation or approach.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (needed for safety screening)
- Mechanism-of-action data for glucagon, and a comparison of glucagon and GLP-1 effects on gut motility and visceral pain
- Direct evidence for glucagon in IBS, such as a small proof-of-concept study of short-term use for acute pain or spasm attacks
- An assessment of route and formulation feasibility, since current products are injectables for emergency use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

