---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 699
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-lowering drug, long used to treat hyperlipidemia (mixed dyslipidemia and hypertriglyceridemia). The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but the supporting evidence is currently thin — **1 registered clinical trial** (which actually tests a different drug, alirocumab, not fenofibrate) and **11 publications**, none providing direct fenofibrate efficacy data in HoFH patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia — hypercholesterolemia (Fredrickson type IIa/IIb) and hypertriglyceridemia (type IV/V); no TFDA/US license record is on file in this dataset |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (per current dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacology, fenofibrate is a PPAR-alpha agonist that activates lipoprotein lipase (LPL) and lowers apoC-III, primarily reducing triglycerides and raising HDL-C, with only a modest effect on LDL-C. This mechanism underlies its established efficacy in mixed hyperlipidemia and hypertriglyceridemia.

HoFH, however, is caused by near-total loss of functional LDL receptors, so effective therapies must work through LDL-receptor-independent pathways — PCSK9 inhibitors, lomitapide, evinacumab, LDL apheresis, or liver transplantation. Fenofibrate's TG/HDL-centric mechanism does not directly address this receptor deficiency, which is why the evidence base for this specific prediction is weak: the one clinical trial pulled into this evidence pack (NCT03510715) actually studies alirocumab (a PCSK9 inhibitor), not fenofibrate, and most of the literature is guideline or review material rather than direct fenofibrate-in-HoFH data. One older case series (PMID 6593751) does report a single HoFH patient responding to fenofibrate, but this is anecdotal and far from confirmatory. The mechanistic mismatch and lack of direct evidence are reflected in the L4 evidence level and "Hold" recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of **alirocumab** (not fenofibrate) in children/adolescents with HoFH, evaluating LDL-C reduction at Week 12 on top of background therapy. Included here only as background on the HoFH treatment landscape — not direct fenofibrate evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical study | Pharmacological Research Communications | Long-term fenofibrate (300 mg/day) in 22 type II hyperlipoproteinemia patients; the single HoFH patient in the cohort showed the greatest fall in total and LDL cholesterol — the only direct (anecdotal) fenofibrate-in-HoFH data point |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Reviews pharmacologic/surgical treatment of dyslipidemic children, noting fenofibrate among agents used in familial hypercholesterolemia with variable success |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK study (lomitapide) | Pharmacotherapy | Characterizes pharmacokinetic interactions of lomitapide (an approved HoFH drug) with commonly co-used lipid drugs including fenofibrate |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Reviews liver transplantation for HoFH in the era of emerging lipid-lowering therapies; standard lipid-lowering drugs and apheresis framed as often insufficient |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management and cardiovascular prevention guideline |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Reviews non-statin lipid-lowering drugs; notes fenofibrate's definite indication is severe hypertriglyceridemia, not LDL-driven disease |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidemia management in pregnancy; general background, not HoFH-specific |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews statins and PCSK9 inhibitors for LDL-C reduction; general background |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Reviews atorvastatin pharmacology in hyperlipidaemia management; not fenofibrate-specific |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review (ezetimibe) | Pharmacotherapy | Reviews ezetimibe as a selective cholesterol absorption inhibitor; not fenofibrate-specific |

## US Market Information

No US market authorization record is currently available for fenofibrate in this dataset (0 licenses on file, status: Not Marketed). This does not necessarily reflect real-world market status — it reflects a gap in the current data collection for this product.

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-interaction data are currently on file for this candidate.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered trial linked to this prediction studies a different drug (alirocumab), and the literature offers no controlled evidence of fenofibrate efficacy in HoFH — only one 1984 case series with a single HoFH patient. Mechanistically, fenofibrate's TG/HDL-centric PPAR-alpha action is a poor fit for a disease driven by LDL receptor deficiency, which argues against pursuing this indication further without new data.

**To proceed, the following is needed:**
- Direct clinical evidence (trial or real-world) of fenofibrate efficacy specifically in HoFH patients
- TFDA/FDA-sourced MOA, warnings, and contraindication data (currently Data Gap, flagged Blocking in the evidence pack)
- Drug-drug interaction data (current DDI query returned no results)
- Consideration of the stronger-evidence candidate in this same evidence pack — "hyperlipoproteinemia" (rank 2, evidence level L1, recommendation "Proceed with Guardrails") — which is closer to fenofibrate's established mechanism and may be a more productive target for further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

