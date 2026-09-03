---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 1095
evidence_level: L5
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (RTH)

## One-Sentence Summary

> Propylthiouracil (PTU) is a thionamide antithyroid drug, historically used to treat hyperthyroidism/Graves' disease (as documented throughout the supporting literature, though not captured in structured regulatory indication text).
> The TxGNN model predicts it may be relevant to **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-β)**,
> but this is currently supported only by **0 clinical trials** and **6 case report/preclinical publications** — several of which describe PTU being used *ineffectively* in misdiagnosed RTH patients rather than as a validated therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism / Graves' disease (inferred from literature context; not recorded in structured regulatory license data) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 (case reports and preclinical/mechanistic studies only; no clinical trials or RCTs) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap, item DG002). Based on known information from the supporting literature, propylthiouracil is a thionamide-class antithyroid agent whose efficacy in hyperthyroidism/Graves' disease is well established, and TxGNN links it to thyroid hormone receptor-beta (THRB) biology, which is the same molecular pathway implicated in RTH.

However, the mechanistic relationship here is more complex than a simple disease-similarity extension. RTH is caused by *loss-of-function/dominant-negative mutations* in THRB that make target tissues insensitive to thyroid hormone, typically presenting with **elevated** (not deficient) circulating thyroid hormone levels and a clinical picture that can mimic hyperthyroidism. Several of the retrieved publications (e.g., PMID 10724359, PMID 3097618-type cases) describe patients with RTH who were **misdiagnosed as having thyrotoxicosis and treated with PTU without benefit** — in one case the patient's goiter enlarged during PTU therapy. This suggests the literature co-occurrence driving the TxGNN score may reflect historical diagnostic confusion between hyperthyroidism and RTH, rather than genuine therapeutic evidence for PTU in RTH.

Given the absence of MOA data and the presence of literature actively describing PTU treatment failure in RTH, this prediction should be interpreted as a **hypothesis requiring careful reassessment**, not a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case Report | Exp Clin Endocrinol Diabetes | Turkish family with THRB P453A mutation causing RTH; thyroid function tests suggestive of hormone resistance |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case Report | Endocrine Journal | Thai woman with de novo THRB L330S mutation; previously misdiagnosed with thyrotoxicosis and treated with PTU for 9 months, with **worsening goiter** — illustrates PTU's lack of benefit in RTH |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clinical Endocrinology | Family with TRβ M313T mutation; neonatal thyrotoxicosis and maternal infertility linked to RTH |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Preclinical (mouse model) | Endocrinology | Cardiac-targeted mutant TRβ mouse model demonstrates dominant-negative RTH effects on cardiac gene expression |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Preclinical (mouse model) | Endocrinology | Thrb(PV/PV) mutant mice show TSH-dependent development of RTH-associated thyroid carcinoma |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Preclinical (mouse model) | Oncogene | Thrb(PV/PV) mouse model links mutant TRβ receptor signaling to follicular thyroid carcinoma proliferation |

---

## US Market Information

No FDA licenses/NDAs are currently on file for this drug in the dataset (market status: **Not Marketed**, total licenses: 0).

---

## Safety Considerations

TFDA/FDA-level warnings, contraindications, and drug-drug interaction data are not currently available for this drug (data gap DG001, marked as **Blocking severity** — this data gap explicitly prevents entry into the S1 safety pre-screening stage). Please refer to the official package insert for safety information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by case reports and preclinical mouse studies (L4), with zero clinical trials, and part of the literature evidence actually documents PTU being used *without benefit* in misdiagnosed RTH patients. Combined with a Blocking-severity safety data gap (no TFDA warnings/contraindications available) and the drug's non-marketed status, there is insufficient basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (resolve DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (resolve DG002)
- Clarification of whether TxGNN's signal reflects genuine pharmacological rationale or historical diagnostic confounding between hyperthyroidism and RTH
- Any prospective or controlled evidence (beyond case reports) specifically evaluating PTU in confirmed RTH patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

