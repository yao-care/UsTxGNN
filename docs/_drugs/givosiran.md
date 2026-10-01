---
layout: default
title: Givosiran
parent: Model Prediction Only (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Hepatoportal Sclerosis

## One-Sentence Summary

Givosiran (marketed as GIVLAARI) is a GalNAc-conjugated siRNA that silences hepatic ALAS1. The published literature describes its use in acute hepatic porphyria.
The TxGNN model's top prediction is **hepatoportal sclerosis**, but there are **0 clinical trials** and **0 publications** for it, and no plausible mechanistic link. The prediction looks like a graph-proximity artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hepatic porphyria (taken from the literature; the US license record has no indication text) |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 99.9986% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From the literature, givosiran is an siRNA taken up by hepatocytes. It degrades ALAS1 mRNA and lowers the neurotoxic heme-pathway intermediates ALA and PBG, which drive acute porphyria attacks.

**For the top-ranked prediction, the rationale is weak.** Hepatoportal sclerosis is a portal-venous vascular disorder with no known dependence on ALAS1 or porphyrin precursors. The same score (99.9986%) was given to five portal-hypertension and liver terms, which points to graph proximity rather than biology. Delivery to the liver alone does not justify the indication.

**One lower-ranked prediction stands out:** porphyria due to ALA dehydratase deficiency (rank 9, score 99.9119%, L4). It is the only prediction with literature support, and it has a real mechanistic basis. ALA accumulates upstream of the enzyme block, so lowering ALAS1 should reduce it. However, the Phase 3 ENVISION program mainly enrolled AIP, HCP and VP patients. One case report describes a lack of response to givosiran in ALAD porphyria, so the expectation is not confirmed clinically.

### All Top-10 Predictions

| Rank | Predicted Indication | Score | Evidence | Assessment |
|------|------|------|------|------|
| 1 | Hepatoportal sclerosis | 99.9986% | L5 | No plausible link |
| 2 | Primitive portal vein thrombosis | 99.9986% | L5 | No plausible link |
| 3 | Hepatopulmonary syndrome | 99.9986% | L5 | No plausible link |
| 4 | Idiopathic copper-associated cirrhosis | 99.9986% | L5 | No plausible link |
| 5 | Early-onset familial noncirrhotic portal hypertension | 99.9986% | L5 | No plausible link |
| 6 | Chronic hepatitis C virus infection | 99.9703% | L5 | Weak, non-specific; curative antivirals already exist |
| 7 | Glycogen storage disease (hepatic glycogen synthase deficiency) | 99.9550% | L5 | No plausible link |
| 8 | Chronic hepatitis B virus infection | 99.9357% | L5 | Weak, non-specific; HBV siRNAs target viral transcripts, not ALAS1 |
| 9 | Porphyria due to ALA dehydratase deficiency | 99.9119% | L4 | Strong mechanistic rationale, indirect evidence, discordant case report |
| 10 | Disorder of phenylalanine metabolism | 99.9001% | L5 | No plausible link |

## Clinical Trial Evidence

Currently no related clinical trials registered for hepatoportal sclerosis.

## Literature Evidence

Currently no related literature available for hepatoportal sclerosis.

The table below covers the rank-9 candidate, ALAD deficiency porphyria. Most of these papers are about acute hepatic porphyria in general and are indirect evidence for it.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT post-hoc analysis | Orphanet J Rare Dis | Disease burden in patients with acute hepatic porphyria from the Phase 3 ENVISION study |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Commentary on RCT | J Intern Med | Givosiran RNAi therapy significantly reduces attack rates in acute intermittent porphyria (ENVISION) |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Cohort | Sci Rep | Open-label expanded access study in 10 Japanese AHP patients on monthly givosiran 2.5 mg/kg; assessed safety and efficacy |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK-PD modeling | CPT Pharmacometrics Syst Pharmacol | Semimechanistic model of urinary ALA reduction after givosiran, using pooled Phase 1-3 data |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case report | Front Genet | Lack of response to givosiran in a patient with ALAD porphyria |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | RNA interference therapy in acute hepatic porphyrias, with ALAS1 upregulation and ALA as the neurotoxic mediator |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Des Devel Ther | Design, development and place in therapy of givosiran for adults with AHP |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Review | Rev Clin Esp | Therapeutic approach to acute crises of hepatic porphyrias, including ALAD deficiency |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA212194 | GIVLAARI | Injection, solution | Alnylam Pharmaceuticals, Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hepatoportal sclerosis, has no clinical or literature evidence (L5) and no plausible mechanistic link to ALAS1 silencing. The identical scores across several liver terms suggest a model artifact. The rank-9 ALAD porphyria candidate is mechanistically sound (L4, "Research Question"), but its only direct evidence is a case report of non-response.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- Approved indication text for NDA212194
- For ALAD porphyria: a targeted evaluation of ADP patients' response to givosiran, including the discordant case report
- No further work on the other L5 predictions unless a new mechanistic hypothesis emerges

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

