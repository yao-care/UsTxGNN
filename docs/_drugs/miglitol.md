---
layout: default
title: Miglitol
parent: Moderate Evidence (L3-L4)
nav_order: 928
evidence_level: L3
indication_count: 10
---

# Miglitol
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Miglitol: From Type 2 Diabetes to Type 1 Diabetes

*Note: The five highest-scoring predictions (for example focal stiff limb syndrome and classic stiff person syndrome) have no trials or literature and no plausible mechanism. This report therefore covers type 1 diabetes mellitus, the only predicted indication with real supporting evidence.*

## One-Sentence Summary

Miglitol is an oral alpha-glucosidase inhibitor marketed for type 2 diabetes.
The TxGNN model predicts it may be useful as an add-on to insulin in **type 1 diabetes mellitus** (score 99.60%). Support is **1 completed Phase 3 open trial** (no results posted) and **about 15 publications**, mostly small and dated studies from 1986 to 2011.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes (inferred from the pack's rationale text, since the US license records list no indication text) |
| Predicted New Indication | Type 1 diabetes mellitus (rank 10 of 10 predictions) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all under ANDA203965) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Miglitol is known to be an intestinal alpha-glucosidase inhibitor. It delays carbohydrate digestion and absorption, which flattens the rise in blood glucose after meals.

Even with intensive insulin therapy, many people with type 1 diabetes have sharp postprandial glucose spikes. Slowing carbohydrate absorption can reduce these spikes and the insulin needed at meals. This is the same mechanism that makes miglitol useful in type 2 diabetes, so the prediction is biologically coherent.

The evidence supports miglitol only as an **adjunct to insulin**, not as a standalone therapy. Because miglitol is already marketed, its safety profile is known. The other high-scoring predictions (stiff person syndromes, lipodystrophies, opsismodysplasia, pancreatic agenesis, thiamine-responsive dysfunction syndrome) show no plausible mechanism and are likely graph-neighborhood artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3 | Completed | Not reported | Open (non-randomized) trial of miglitol in insulin-treated type 1 diabetes. It targets the exact drug and indication, but no results are provided. |

Five other trials returned by the search (NCT02475499, NCT02476760, NCT02456428, NCT06449235, NCT03492580) are observational or other-drug studies in type 2 diabetes. NCT01697592, a Phase 3 study of omarigliptin, was also returned, and its population could not be confirmed. None involves miglitol in type 1 diabetes, so none is counted as evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Clinical study | J Diabetes Investig | Miglitol plus insulin in type 1 diabetes, where postprandial spikes persist despite intensive insulin. |
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | Clinical study | Endocr J | 11 type 1 patients on intensive insulin took miglitol 25 mg, then 50 mg, three times daily. Outcomes were insulin dose, body weight, hypoglycemia and incretin responses. |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | Clinical study | Diabetes Care | Alpha-glucosidase inhibition as an insulin adjunct: effect on meal glucose tolerance and insulin timing. |
| [2180090](https://pubmed.ncbi.nlm.nih.gov/2180090/) | 1990 | Clinical study | S Afr Med J | 11 patients. Miglitol 50 mg significantly lowered post-meal glucose increments at 30 and 60 minutes versus placebo. |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) | 1989 | Clinical study | Diabetes Res | Single-blind crossover in 13 patients. Miglitol significantly reduced glucose area under the curve, with no change in fasting glucose. |
| [3653827](https://pubmed.ncbi.nlm.nih.gov/3653827/) | 1987 | Clinical study | Fortschr Med | Miglitol in insulin-dependent diabetes, reported as giving improved metabolic control and good tolerance. |
| [8261749](https://pubmed.ncbi.nlm.nih.gov/8261749/) | 1993 | Review | Diabet Med | Review of alpha-glucosidase inhibition as an adjunct in type 1 diabetes. |
| [12073790](https://pubmed.ncbi.nlm.nih.gov/12073790/) | 2002 | Review | Rev Med Liege | Pharmacological approaches to postprandial hyperglycemia, including acarbose and miglitol. |

Several 1986–1988 studies (for example PMIDs 3520133, 3130257 and 3311550) tested earlier alpha-glucosidase inhibitors (Bay compounds) in insulin-dependent diabetes, and they are consistent with this direction. A 2020 case report (PMID 33268615) describes SGLT2 inhibitors added to patients already on miglitol and does not test miglitol itself.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA203965 | Miglitol | Tablet, coated (oral) | Westminster Pharmaceuticals, LLC |
| ANDA203965 | Miglitol | Tablet, coated (oral) | Proficient Rx LP |

The pack lists six licenses in total but returns five records. All five are under ANDA203965 from these two labelers, so the table shows each labeler once.

## Safety Considerations

Please refer to the package insert for safety information.

One point from the pack's assessment applies to type 1 diabetes specifically. Hypoglycemia in patients taking an alpha-glucosidase inhibitor should be treated with oral glucose rather than sucrose, because sucrose absorption is delayed.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits, and many small studies show that miglitol lowers postprandial glucose and insulin needs in insulin-treated type 1 diabetes. However, the evidence is old and small-scale, and the only Phase 3 trial is an open-label study with no posted results. It is best treated as a research question for adjunctive use, not a ready-to-adopt indication.

**To proceed, the following is needed:**
- Results or publication from NCT00213109, or a modern randomized, controlled trial in type 1 diabetes, ideally with continuous glucose monitoring outcomes
- Package insert warnings and contraindications, which are needed before any safety screening
- Formal mechanism of action data
- A hypoglycemia management plan for type 1 patients, including use of oral glucose rather than sucrose

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

