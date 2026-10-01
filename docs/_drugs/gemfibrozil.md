---
layout: default
title: Gemfibrozil
parent: Model Prediction Only (L5)
nav_order: 749
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a marketed oral lipid-lowering drug used for high triglycerides. The TxGNN model predicts it may be effective for **rheumatoid arthritis**. Support so far is thin: **0 registered clinical trials** and **4 retrieved publications**, mostly animal or mechanistic work, with only one paper on gemfibrozil itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidemia / hypertriglyceridemia (inferred from the retrieved trial and literature text; the license records contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (preclinical and mechanistic evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the records shown are generic ANDA filings) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gemfibrozil is not available in the source data. Gemfibrozil is a PPAR-alpha agonist, a fibrate-class drug whose efficacy in lowering triglycerides is well established. PPAR-alpha activity has anti-inflammatory and immunomodulatory effects, which is the mechanistic bridge to an inflammatory autoimmune disease like rheumatoid arthritis.

Lipid disorders and rheumatoid arthritis are not closely related diseases, so the link is indirect and rests on shared inflammatory pathways. A 2026 rat study showed that bezafibrate, a pan-PPAR agonist and fellow fibrate, reduced experimental arthritis through PPAR-dependent pathways. This is class-level evidence and does not show that gemfibrozil works. For gemfibrozil itself, the only supporting study is a rat model in which it was combined with a reduced prednisolone dose. The very high model score is a computational prediction and has not been confirmed by any human study.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (animal model, bezafibrate) | Int Immunopharmacol | Docking of fibrate-class compounds identified bezafibrate as a PPAR-γ-active candidate. It attenuated experimental arthritis by modulating inflammatory pathways. This is class-effect evidence, not gemfibrozil. |
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclinical (rat adjuvant-induced arthritis) | Mod Rheumatol | Gemfibrozil (30 mg/kg) combined with a reduced prednisolone dose gave a similar disease picture to the full steroid dose. The source data labels this "case report/series," but the abstract describes a 72-rat animal study. |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (mechanistic) | J Immunol | Myelin basic protein priming reduced Foxp3 in regulatory T cells via nitric oxide. It is a background immunology study, not directly about gemfibrozil or rheumatoid arthritis. |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review | Am J Clin Dermatol | Review of palmar erythema and its causes. It is not directly relevant to this prediction. |

## US Market Information

The retrieved license records contain no approved-indication text. The five main authorizations (of 20) are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA204189 | Gemfibrozil | Tablet | Viona Pharmaceuticals Inc |
| ANDA214603 | Gemfibrozil | Tablet | Proficient Rx LP |
| ANDA078012 | Gemfibrozil | Tablet | Bryant Ranch Prepack |
| ANDA077836 | Gemfibrozil | Tablet | REMEDYREPACK INC. |
| ANDA077836 | Gemfibrozil | Tablet, film coated | Aphena Pharma Solutions - Tennessee, LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No human study supports gemfibrozil for rheumatoid arthritis. The only gemfibrozil-specific evidence is one rat study, and the rest is class-level or background science. The high TxGNN score alone does not justify moving forward.

Other predicted indications in this Evidence Pack have much stronger support. **Hypoalphalipoproteinemia** (low HDL) is graded L2 with a "Proceed with Guardrails" recommendation, based on several small randomized clinical studies. **HIV-associated dyslipidemia** is graded L3 and includes a randomized, double-blind study. If the goal is to advance gemfibrozil, these two are better candidates than rheumatoid arthritis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Gemfibrozil-specific preclinical replication in arthritis models, ideally with a comparison against other fibrates
- Evidence from human studies, or at minimum a registered trial, before reconsidering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

