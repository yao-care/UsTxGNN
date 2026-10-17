---
layout: default
title: Nizatidine
parent: Model Prediction Only (L5)
nav_order: 975
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Nizatidine: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "NIZATIDINE"
predicted_indications: ["duodenal obstruction", "multiple endocrine neoplasia"]
---

# Nizatidine
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

# Nizatidine: From Gastric Ulcer to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is an H2-receptor antagonist originally used for gastric ulcer, duodenal ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis and dyspepsia.
The TxGNN model's top prediction is **active peptic ulcer disease**, supported by **0 registered clinical trials** and **20 publications**, including several randomized trials.
This prediction largely recovers an indication the drug already has, so it is not a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia, duodenal ulcer (the licence records contain no indication text, so this list comes from the knowledge-graph indication data) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (the data compiled for this report include several randomized, placebo-controlled trials published in journals; no trials are registered) |
| US Market Status | Cancelled only (all licences cancelled) |
| Number of NDAs | 4 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, nizatidine is an H2-receptor antagonist that inhibits basal, nocturnal and stimulated gastric acid secretion. Its efficacy in ulcer disease has been established.

Active peptic ulcer disease (gastric and duodenal) already falls within the drug's original indications. The high TxGNN score therefore reflects recovery of a known indication rather than a new discovery. Placebo-controlled and active-comparator randomized trials support the efficacy, for example in benign gastric ulcer (PMID 1526089) and against ranitidine (PMID 1982108).

Other lower-ranked predictions in the data (gastrojejunal ulcer, gastroduodenitis) are mechanistically plausible because they are acid-dependent, but the evidence is indirect. Predictions such as peptic ulcer perforation, duodenal obstruction, duodenogastric reflux and multiple endocrine neoplasia rest on model scores alone or have weak mechanistic links.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled trial of nizatidine 150 mg twice daily in active duodenal ulcer, covering healing and recurrence |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | Eight-week, double-blind comparison of nizatidine and placebo in benign gastric ulcer; twice-daily and bedtime dosing compared |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | One-year maintenance in 513 patients with healed duodenal ulcer; 12-month recurrence 34% with nizatidine versus 64% with placebo |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepato-gastroenterology | Nizatidine (twice daily or bedtime) versus ranitidine in 101 patients with active gastric ulcer over 8 weeks |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | Randomized, placebo-controlled trial | Isr J Med Sci | Nizatidine 300 mg at night versus placebo for 4 weeks in 55 patients with active duodenal ulcer, with mucosal inflammatory mediators measured |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Preliminary review of pharmacology and use of nizatidine in peptic ulcer disease; more potent than cimetidine in animal studies |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy of peptic ulcer; nizatidine described as safe and effective |
| [7863254](https://pubmed.ncbi.nlm.nih.gov/7863254/) | 1994 | Clinical study | Scand J Gastroenterol Suppl | Open 12-month maintenance therapy in healed duodenal ulcer, with quality of life assessed |

## US Market Information

All four licences are cancelled and the data contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076178 | Nizatidine (Epic Pharma) | Capsule | Not available (cancelled) |
| ANDA090576 | Nizatidine (Amneal) | Solution | Not available (cancelled) |
| ANDA075616 | Nizatidine (Actavis) | Capsule | Not available (cancelled) |
| ANDA077314 | Nizatidine (Dr Reddy's) | Capsule | Not available (cancelled) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): liver disease, gallbladder disease, impaired renal function, and gastric cancer and related gastric neoplasms (gastric neoplasm, diffuse gastric adenocarcinoma, linitis plastica, gastric carcinoma).
- **Drug Interactions**: 100 interactions were found. Examples from the data reviewed:
  - **Major**: atazanavir, dasatinib
  - **Moderate**: acalabrutinib, bosutinib, brigatinib, ceritinib, dabrafenib, dacomitinib, cefditoren, cefpodoxime, cefuroxime, chlorpropamide
  - **Minor**: ketorolac, ibuprofen, diclofenac, alendronic acid, axitinib, cyanocobalamin, magnesium oxide, oxaprozin
- Many of the interacting kinase inhibitors and antiretrovirals probably involve acid-dependent absorption. The data do not state the mechanism.

Please refer to the package insert for warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, active peptic ulcer disease, is already an established indication of nizatidine. It is not a true repurposing opportunity, and no repurposing action is needed. All US licences are cancelled. The other predicted indications have indirect or no supporting evidence, and PPIs are generally preferred in those settings.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Targeted evidence for any lower-ranked indication of interest. Gastrojejunal ulcer and gastroduodenitis have the most plausible mechanistic links.
- Confirmation of whether any US product is still marketed, given that all licences are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

