---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fluvastatin: From Atherosclerosis and Familial Combined Hyperlipidemia to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is a statin (HMG-CoA reductase inhibitor) originally used for atherosclerosis and familial combined hyperlipidemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, and this is close to its existing lipid-lowering use.
The data compiled for this report include **1 clinical trial** and **20 publications**, but the only trial tests a different drug (alirocumab), so direct fluvastatin trial evidence for this indication is missing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atherosclerosis, arteriosclerosis disorder, familial combined hyperlipidemia (from the TxGNN knowledge graph, because the US license records list no indication text) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (observational and small clinical studies and reviews; no fluvastatin Phase 3 trial for this indication) |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 5 licenses in total (1 NDA and 4 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Fluvastatin is a member of the statin class, which inhibits HMG-CoA reductase and lowers LDL cholesterol (LDL-C). Its efficacy in its original lipid-related indications is established.

Hyperlipoproteinemia is a disorder of lipoprotein levels, and the original indications already include familial combined hyperlipidemia. The predicted indication is therefore a near-label use rather than a true repurposing. The published literature includes fluvastatin-specific clinical studies from the 1990s and 2000s. They cover monotherapy, combinations with bezafibrate or fenofibrate, and extended-release versus immediate-release formulations.

The prediction is reasonable on mechanism, but the supporting evidence is older and mostly from small studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) on LDL-C in children and adolescents with homozygous familial hypercholesterolemia. It does not involve fluvastatin, so it is not direct evidence for this drug. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | Randomized trial | Clin Ther | Fluvastatin 80 mg extended-release vs immediate-release in primary hypercholesterolemia |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT (12-month, double-blind) | Clin Ther | Fluvastatin + fenofibrate vs fluvastatin alone in combined hyperlipidemia, type 2 diabetes and coronary heart disease |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | Randomized double-blind trial | Atherosclerosis | FACT study: fluvastatin and bezafibrate, alone and combined, in 333 patients with coronary artery disease and mixed hyperlipidaemia |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Double-blind clinical study | Eur J Clin Pharmacol | High-dose fluvastatin in 52 patients with familial hypercholesterolaemia |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | Pediatric clinical study | Acta Paediatr | Efficacy and safety of fluvastatin in children and adolescents with heterozygous familial hypercholesterolaemia |
| [7604794](https://pubmed.ncbi.nlm.nih.gov/7604794/) | 1995 | Clinical study | Am J Cardiol | One-year study of fluvastatin in 337 Japanese patients with hypercholesterolemia |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Clinical study | Am J Cardiol | Effects of fluvastatin on lipid profile and apolipoproteins in 31 Chinese patients |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Clinical study | Ter Arkh | Variability of the lipid-lowering action of simvastatin and fluvastatin in primary hyperlipoproteinemia |
| [8462180](https://pubmed.ncbi.nlm.nih.gov/8462180/) | 1993 | Review | Circulation | Review of drug treatment of dyslipoproteinemia, focusing on fluvastatin |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Review article on fluvastatin |

## US Market Information

All five US licenses are cancelled, and no currently valid license exists. The license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA078407 | Fluvastatin | Capsule | Teva Pharmaceuticals USA, Inc. | Cancelled |
| ANDA090595 | Fluvastatin Sodium | Capsule | Mylan Pharmaceuticals Inc. | Cancelled |
| ANDA079011 | Fluvastatin Sodium | Film-coated extended-release tablet | Teva Pharmaceuticals USA, Inc. | Cancelled |
| NDA021192 | Lescol | Extended-release tablet | Sandoz Inc | Cancelled |
| ANDA209397 | Fluvastatin Sodium | Film-coated extended-release tablet | Lannett Company, Inc. | Cancelled |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis and injury.
- **Drug interactions**: 100 interactions are recorded. Those rated Moderate include aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, glyburide and pectin. Other recorded interactions, such as calcitriol, doxycycline, cimetidine, famotidine, aspirin and pantoprazole, have an unknown severity level. The full list needs pharmacist or clinical review before any development.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism fits well and the original indications already include a related lipid disorder. However, the only trial listed tests alirocumab rather than fluvastatin, and the fluvastatin literature is mostly older small studies. All US licenses are cancelled, and package insert safety data are missing.

Among the other predictions, **familial hypercholesterolemia** has stronger support. It has a completed Phase 3 pediatric fluvastatin trial ([NCT00171236](https://clinicaltrials.gov/study/NCT00171236), n=84) and a published pediatric study (PMID 17062478), and it could be assessed separately as a candidate to proceed with guardrails. Most of the remaining predictions have no supporting evidence (several are veterinary or non-human disease terms), and the HIV-related prediction is only a research question.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications and approved indications) and the mechanism-of-action data
- Fluvastatin-specific randomized evidence for hyperlipoproteinemia, or a decision to prioritize the better-supported familial hypercholesterolemia indication
- Confirmation of product availability and formulation, since all US licenses are cancelled
- A review of the 100 recorded drug interactions, especially with other statins and CYP-related agents, and a muscle and liver safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

