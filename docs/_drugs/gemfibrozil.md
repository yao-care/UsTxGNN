---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 749
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Gemfibrozil: From Dyslipidemia (Fibrate Class) to Rheumatoid Arthritis

## One-Sentence Summary

> Gemfibrozil is a classic fibrate-class PPAR-α agonist used internationally for hypertriglyceridemia and mixed dyslipidemia (it holds no current Taiwan marketing authorization).
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but currently only **0 clinical trials** and **4 publications** (mostly case reports and indirect animal models) support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not TFDA-approved in Taiwan (0 licenses on file); internationally used as a fibrate for hypertriglyceridemia/mixed dyslipidemia |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on information available elsewhere in this evidence pack, gemfibrozil is a **fibrate-class PPAR-α agonist** — its classic pharmacology lowers triglycerides and raises HDL-C, and it is not currently marketed in Taiwan.

The rationale for a link to rheumatoid arthritis is mechanistic rather than direct: PPAR-α activation can inhibit the NF-κB pathway and reduce pro-inflammatory cytokine production, giving fibrates theoretical anti-inflammatory potential. However, the supporting literature in this pack largely concerns **bezafibrate** (a related but distinct fibrate) in animal arthritis models, not gemfibrozil itself, and the one gemfibrozil-specific study is a small rat adjuvant-arthritis model rather than clinical data. Direct evidence for gemfibrozil in RA is therefore indirect and class-based rather than drug-specific.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Case Report / animal study | Modern Rheumatology | Combined gemfibrozil (PPAR-α agonist) + reduced-dose steroid gave comparable disease control to full-dose steroid in a rat adjuvant-induced arthritis model |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (animal) | International Immunopharmacology | Bezafibrate (pan-PPAR agonist, same drug class as gemfibrozil) attenuated experimental RA via PPAR-γ-dependent modulation of inflammatory pathways |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (animal, EAE model) | Journal of Immunology | Nitric oxide/Foxp3 crosstalk in Tregs in an autoimmune (EAE) model — mechanistic, not RA-specific, no gemfibrozil intervention |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Case Report | American Journal of Clinical Dermatology | Review of palmar erythema etiologies; tangential relevance, not a treatment study |

---

## Taiwan Market Information

Currently not marketed in Taiwan — no NDA/許可證 records on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings, contraindications, and DDI data are all currently unavailable — Data Gap DG001, Blocking.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for gemfibrozil specifically in rheumatoid arthritis is preclinical/case-report level (L4), with no registered clinical trials, and most supporting literature refers to a related fibrate (bezafibrate) rather than gemfibrozil itself. The mechanistic plausibility (PPAR-α/NF-κB) exists but drug-specific efficacy data is lacking.

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications (DG001, Blocking — currently blocks safety pre-screening)
- Detailed mechanism of action data from DrugBank (DG002)
- Gemfibrozil-specific (not bezafibrate-class) preclinical or clinical evidence in RA

**Note:** This evidence pack also contains a substantially stronger repurposing signal for the same drug — **hypoalphalipoproteinemia/low-HDL** (rank 4: Evidence Level L2, decision stage S3, recommendation **Proceed with Guardrails**), supported by multiple RCTs directly testing gemfibrozil. That candidate warrants separate evaluation as the priority indication for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

