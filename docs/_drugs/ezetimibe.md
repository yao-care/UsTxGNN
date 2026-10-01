---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 690
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
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

# Ezetimibe: From Lipid Lowering to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is an oral cholesterol-absorption inhibitor that is already marketed in the US as generic tablets. The US license records supplied here do not state an indication.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with **50 clinical trials** and **19 publications** currently supporting this direction.
This is most likely an approved lipid-lowering use rather than true repurposing, so the label should be confirmed before treating it as new.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (all approved-indication fields are blank); ezetimibe is a marketed lipid-lowering agent |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on the repurposing rationale supplied, ezetimibe inhibits NPC1L1-mediated intestinal cholesterol absorption, which lowers LDL cholesterol (LDL-C). That fits the very high TxGNN score.

Hyperlipoproteinemia is a disorder of elevated circulating lipoproteins, and lowering LDL-C is the core therapeutic goal. Completed Phase 3 trials test ezetimibe in this setting. They include coadministration with a statin, with fenofibrate, and in homozygous familial hypercholesterolemia.

The original-indication and MOA fields are empty in the record, so the evidence cannot show whether this counts as true repurposing. Ezetimibe is already a marketed lipid-lowering drug, so the predicted indication probably overlaps with its existing label.

---

## Clinical Trial Evidence

The Evidence Pack lists 50 trials for this indication. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous familial hypercholesterolemia; direct evidence, small sample |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia (companion study) |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate in mixed hyperlipidemia |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis in heterozygous FH |
| [NCT00268697](https://clinicaltrials.gov/study/NCT00268697) | Phase 3 | Completed | 1267 | Lapaquistat ± ezetimibe vs ezetimibe alone in primary dyslipidemia |
| [NCT00195793](https://clinicaltrials.gov/study/NCT00195793) | Phase 3 | Completed | 174 | Fenofibrate or ezetimibe added to atorvastatin in combined hyperlipidemia |
| [NCT03337308](https://clinicaltrials.gov/study/NCT03337308) | Phase 3 | Completed | 382 | Bempedoic acid + ezetimibe fixed-dose combination vs each component and placebo on top of statins |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib + ezetimibe fixed-dose combination vs placebo in HeFH and/or ASCVD |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | Completed | 11332 | Japanese 12-week post-marketing study of Zetia; real-world, non-randomized |

---

## Literature Evidence

The Evidence Pack lists 19 publications for this indication. The 10 most relevant are shown below. RCTs are listed first, then reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM: phase 3 placebo-controlled trial of an obicetrapib + ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH; disease context, not an ezetimibe trial |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: inclisiran in homozygous FH; disease context, not an ezetimibe trial |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Overview of current drugs targeting hyperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C-lowering therapies on top of statins, ezetimibe and PCSK9 inhibitors |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Familial hypercholesterolemia; lists ezetimibe among LDL-lowering treatments |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis and treatment of postprandial hyperlipidemia |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circ Res | Cholesterol-lowering agents, including PCSK9-targeting therapies |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Drug bulletin | Drug Ther Bull | Ezetimibe update: lowers LDL-C alone or with a statin; no evidence of cardiovascular outcome benefit at the time of review |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Editorial | N Engl J Med | Commentary on cholesterol lowering and ezetimibe; no abstract available |

---

## US Market Information

The record lists 20 authorizations in total; 5 are shown below. The indication text is blank in every license record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA209838 | Ezetimibe (Proficient Rx LP) | Tablet | Not stated in record |
| ANDA209234 | Ezetimibe (Bryant Ranch Prepack) | Tablet | Not stated in record |
| ANDA207311 | Ezetimibe (Golden State Medical Supply, Inc.) | Tablet | Not stated in record |
| ANDA200831 | Ezetimibe (Bryant Ranch Prepack) | Tablet | Not stated in record |
| ANDA215693 | Ezetimibe (Orient Pharma Co., Ltd.) | Tablet | Not stated in record |

All authorizations shown are ANDA (generic) approvals for oral tablets.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials support ezetimibe in hyperlipidemia and related lipid disorders, and the mechanism (NPC1L1 inhibition and LDL-C lowering) is consistent with the prediction. However, this is most likely an already-approved use, and the label and safety data are missing from the record.

**To proceed, the following is needed:**
- The approved label text, to confirm whether hyperlipoproteinemia is already covered.
- Package insert warnings, contraindications and drug-interaction data, which are currently missing.
- Mechanism-of-action data from DrugBank.
- Confirmation of the original indication, since the record is blank.

**Other predictions for this drug:**
- **Familial hypercholesterolemia:** L1, Proceed with Guardrails. The response is expected to be partial in homozygous and severe heterozygous disease.
- **Hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency:** L4, Research Question. There are no clinical trials.
- **Cholesterol-ester transfer protein deficiency:** L5, Hold. The mechanistic link is weak and there is no direct evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

