---
layout: default
title: Lofexidine
parent: Model Prediction Only (L5)
nav_order: 866
evidence_level: L5
indication_count: 2
monitor_inn: "LOFEXIDINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-14
description: "Lofexidine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the compiled data"
---

# Lofexidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Lofexidine: From Opioid Withdrawal Symptoms to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Lofexidine is a central alpha-2 adrenergic agonist whose approval in the US is for opioid withdrawal symptoms, but the approved indication text is not included in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **1 publication** (a drug-approval news roundup that does not report any migraine data for lofexidine).
This prediction is a computational signal only and has no direct clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled data (the license records contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 4 authorizations are listed as cancelled) |
| Number of NDAs | 4 (1 NDA and 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, lofexidine is a central alpha-2 adrenergic receptor agonist that reduces noradrenergic outflow from the locus coeruleus.

A plausible link to migraine exists through modulation of sympathetic tone and central pain processing. The related alpha-2 agonist clonidine has been studied for migraine prophylaxis, with limited and inconsistent results. No lofexidine-specific clinical or mechanistic data support this indication.

The single literature record is a 2019 drug-news roundup. It lists lofexidine (approved for opioid withdrawal symptoms) next to fremanezumab and galcanezumab (approved for migraine prevention). The apparent association most likely comes from this co-listing rather than from any evidence of benefit.

A second predicted indication, **migraine with brainstem aura** (score 99.26%), has no trials and no publications. Its high score probably reflects its close ontological relationship to migraine disorder rather than independent evidence. An alpha-2 agonist effect on brainstem noradrenergic nuclei is speculative, and no established role exists for this drug class in this rare subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30580925](https://pubmed.ncbi.nlm.nih.gov/30580925/) | 2019 | Review (new drug approvals roundup) | Journal of the American Pharmacists Association | Lists lofexidine (opioid withdrawal) alongside two migraine-prevention antibodies; no abstract available and no evidence of lofexidine use in migraine |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209229 | Lofexidine hydrochloride (Prasco Laboratories) | Tablet, film coated | Not stated; status cancelled |
| ANDA218699 | Lofexidine hydrochloride (Novadoz Pharmaceuticals) | Tablet, film coated | Not stated; status cancelled |
| ANDA218613 | Lofexidine (Indoco Remedies) | Tablet, coated | Not stated; status cancelled |
| ANDA219917 | Lofexidine (ANI Pharmaceuticals) | Tablet | Not stated; status cancelled |

All products are oral tablets.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total, and 20 are shown in the compiled data. Most are rated Moderate. One is rated **Major**: **dolasetron**. Moderate-level examples include:
  - Opioids and related agents: morphine, difenoxin, diphenoxylate, loperamide, naltrexone
  - Antiemetics and cannabinoids: palonosetron, dronabinol, nabilone
  - Others: bupropion, clarithromycin, levofloxacin, famotidine
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - Laxatives and bowel preparations: bisacodyl, picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes

Please refer to the package insert for warnings and contraindications, as this information is not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials, and the single publication is a drug-news roundup with no migraine data for lofexidine. All US authorizations are also cancelled, and the package insert safety information is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Confirmation of the approved indication and current US market status
- Preclinical or clinical evidence specific to lofexidine in migraine, for example a review of the clonidine migraine-prophylaxis data and a small proof-of-concept study
- Assessment of cardiovascular safety (blood pressure and heart rate effects) in a migraine population, as well as the major interaction with dolasetron
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

