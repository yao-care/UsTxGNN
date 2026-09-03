---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 969
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

Using the drug-repurposing-evaluation-report format directly (no other skill applies to this content-generation task).

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

> Nitisinone (DB00348) is used to treat Hereditary Tyrosinemia Type 1 (HT-1) by blocking the tyrosine degradation pathway.
> The TxGNN model predicts it may also be effective for **Renal Tubular Acidosis**,
> with **0 clinical trials** and **2 publications** currently supporting this direction — largely reflecting a known secondary benefit of HT-1 therapy rather than a novel mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT-1) — inferred from repurposing rationale; not confirmed via Taiwan license records |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text for nitisinone is not available in this Evidence Pack. However, the literature-derived rationale provides a clear mechanistic picture: nitisinone inhibits **4-hydroxyphenylpyruvate dioxygenase (HPPD)**, an enzyme upstream in the tyrosine catabolism pathway. By blocking this enzyme, nitisinone prevents the accumulation of **succinylacetone**, the toxic downstream metabolite responsible for both the hepatic and renal tubular damage seen in HT-1.

Renal tubular acidosis — specifically Fanconi-syndrome-type proximal tubular dysfunction — is a well-documented complication of untreated or undertreated HT-1, driven directly by succinylacetone toxicity. This means the "new indication" is not mechanistically novel; it is a **known secondary therapeutic effect** of nitisinone within its original disease context (HT-1), rather than an independent repurposing hypothesis in an unrelated disease area.

This distinguishes renal tubular acidosis from the other TxGNN-predicted candidates in this pack (e.g., galactosemia, glycogen storage disease, C1 inhibitor deficiency), which the rationale text explicitly flags as likely artifacts of knowledge-graph node proximity (co-occurrence in "pediatric metabolic liver disease" review articles) rather than genuine mechanistic links.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular Genetics and Metabolism | Describes early effect of NTBC (nitisinone) on renal tubular dysfunction in patients with hereditary tyrosinemia type 1 |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case Series | Indian Journal of Gastroenterology | Case series of 4 children with tyrosinemia treated with NTBC; reports resolution of renal tubular abnormalities alongside normalized liver function |

---

## US Market Information

Nitisinone is currently **not marketed in Taiwan** (market status: 未上市), and no license records are available in the regulatory dataset. No approved Taiwan product information can be cited at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA warnings, contraindications, and drug interaction data are currently unavailable and represent a **blocking data gap (DG001)** for formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between nitisinone and renal tubular acidosis is biologically well-grounded — it reflects an established secondary effect of HT-1 treatment rather than a speculative new pathway. However, evidence is limited to one cohort and one case-series study (no RCTs or trials specifically targeting RTA as a primary endpoint), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Formal DrugBank MOA documentation (DG002)
- Dedicated studies or larger cohorts evaluating renal tubular acidosis as a primary treatment endpoint (current evidence is secondary/observational within HT-1 cohorts)
- Confirmation of Taiwan marketing authorization pathway, given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

