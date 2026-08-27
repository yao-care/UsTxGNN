---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 754
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon (DrugBank DB00040) is a peptide hormone conventionally used to treat severe hypoglycemia; no other approved indications are recorded in this evidence pack. The TxGNN model predicts a possible role in **Irritable Bowel Syndrome (IBS)**, with **11 clinical trials** and **20 publications** retrieved — but nearly all of this evidence concerns **GLP-1 receptor agonists**, a related but pharmacologically distinct peptide, not Glucagon itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no TFDA/FDA license records or `original_indications` data available); Glucagon's conventional use is severe hypoglycemia rescue treatment |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Glucagon is not available in this evidence pack (`original_moa: [Data Gap]`), and there is no recorded US marketing authorization or approved indication text to compare against.

More importantly, a review of all 11 clinical trials and 20 publications retrieved for this candidate shows that the supporting evidence is almost entirely about **GLP-1 receptor agonists** (liraglutide, ROSE-010, exendin-4, native GLP-1) and their effects on gut motility in IBS — not about Glucagon (DB00040) itself. Glucagon and GLP-1 are both derived from the preproglucagon gene but act on **different receptors with opposing physiological effects** (glucagon raises blood glucose via glucagonolytic signaling; GLP-1 lowers it via incretin signaling, and the two also affect GI motility differently).

This pattern is consistent with a likely **entity confusion in the underlying knowledge graph** — the high TxGNN score (99.24%) appears to be driven by graph proximity between "glucagon" and "GLP-1" nodes rather than by direct pharmacological evidence for Glucagon in IBS. No trial or publication in this pack directly tests Glucagon as an IBS treatment. This should be treated as a low-confidence, indirect signal rather than a genuine repurposing candidate until verified against the source knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a synthetic GLP-1 receptor agonist, not Glucagon) studied for effects on gastric emptying and colonic transit in constipation-predominant IBS (IBS-C) women |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1RA) vs placebo for chronic high bowel frequency after ileal pouch-anal anastomosis; trial terminated early |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Compared native GLP-1 vs its analogue ROSE-010 on prandial gastrointestinal motility inhibition; mechanistic study, not IBS patients specifically |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Prevalence of idiopathic reactive hypoglycemia and effect of fructo-oligosaccharide supplementation on glucose variability; not a drug intervention trial |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Mode of action of butyrate (a microbial metabolite) in the human colon in relation to IBS; not a drug trial |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise training effects on gut dysbiosis and GLP-1 hormone levels in pre-diabetic, obese IBS patients; behavioral intervention, no drug |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Effect of eating rate of ultra-processed foods on dietary intake and metabolic response; not related to Glucagon or IBS drug treatment |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Whole grain rye bread effects on gut-microbiota-brain axis in healthy subjects; dietary intervention, not IBS drug trial |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Gut-microbiota-targeted nutritional intervention for gut barrier integrity under hypobaric hypoxia; unrelated to Glucagon |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Small intestinal organoid model to study nutrient antigens/therapeutic agents; preclinical model-building study |

*Note: none of the above trials tested Glucagon (DB00040) directly; most involve GLP-1 receptor agonists or unrelated dietary/behavioral interventions.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review/Meta-analysis | Frontiers in Endocrinology | GLP-1 receptor agonists and analog ROSE-010 inhibit migrating motor complex and decrease GI motility in IBS patients |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1RA) reduces pain during IBS attacks; cross-analysis identifies suitable subpopulations |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | American Journal of Physiology (GI and Liver) | Randomized, double-blind, placebo-controlled study of ROSE-010 (GLP-1 analog) on GI motor function in IBS-C |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Annals of Gastroenterology | Real-world prescription and discontinuation patterns of GLP-1RAs among IBS patients, focused on GI adverse effects |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical | Neurogastroenterology and Motility | Exendin-4 (GLP-1RA) improved GI dysfunction in a rat model of IBS |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical/Correlational | Clinics and Research in Hepatology and Gastroenterology | Decreased serum GLP-1 correlates with abdominal pain in IBS-C patients; GLP-1 receptor expression in colon studied |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclinical | International Journal of Molecular Medicine | Role of GLP-1 in pathogenesis of experimental IBS-C and IBS-D rat models |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Reviews L-cell/GLP-1 endocrine regulation of gut function in IBS pathophysiology |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews novel investigational drugs, including GLP-1 analogs, for IBS-C |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical | Frontiers in Nutrition | Low FODMAP diet increases circulating GLP-1 in IBS patients |

*Note: as with the trial evidence, essentially all literature concerns GLP-1 (receptor agonists or endogenous GLP-1 physiology), not Glucagon itself.*

---

## US Market Information

No NDA/BLA or marketing authorization records were found for Glucagon in this evidence pack (`total_licenses: 0`, `market_status: 未上市`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The apparent TxGNN prediction score (99.24%) is not supported by direct evidence — all 11 trials and 20 publications concern GLP-1 receptor agonists rather than Glucagon itself, suggesting the knowledge graph may be conflating these two related but pharmacologically distinct preproglucagon-derived peptides. Combined with missing MOA data and no US marketing history, this candidate does not currently meet the bar to advance.

**To proceed, the following is needed:**
- Verification of the TxGNN knowledge graph entity mapping to confirm whether "Glucagon" (DB00040) and "GLP-1/GLP-1 receptor agonists" are being treated as distinct nodes
- Glucagon-specific mechanism of action (MOA) data from DrugBank
- FDA/TFDA label warnings and contraindications for Glucagon (currently a Blocking data gap per DG001)
- If the prediction is confirmed to be a genuine (non-confused) signal, direct preclinical or clinical evidence testing Glucagon — not GLP-1 analogs — in IBS models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

