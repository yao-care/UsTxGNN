---
layout: default
title: Valine
parent: 僅模型預測 (L5)
nav_order: 1279
evidence_level: L5
indication_count: 10
---

# Valine
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

# Valine: From No Established Indication to Sclerosing Cholangitis

## One-Sentence Summary

Valine is an essential branched-chain amino acid (BCAA) with no approved therapeutic indication on record in this evidence pack, and it is currently **not marketed** in the reviewed jurisdiction. The TxGNN model predicts a possible association with **Sclerosing Cholangitis**, but this is supported only by **0 clinical trials** and **2 loosely related publications**, neither of which studies valine as a therapeutic intervention.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established (no approved indication on record; valine is a nutritional/essential amino acid) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Valine is a naturally occurring essential branched-chain amino acid, used clinically mainly as a nutritional/metabolic substrate rather than a drug with a defined disease indication — no original indication is recorded in this dataset, and the drug is not currently marketed.

Critically, the evidence pack's own analysis flags a **systematic false-positive pattern** across nearly all ten predicted indications: because "valine" is abbreviated as "Val" or "V" in genetics literature (e.g., point mutations such as V509A, L346V, Val109), text-mining-derived literature associations repeatedly pick up papers about amino-acid *substitution mutations* in unrelated proteins (TSH receptor, thyroid hormone receptor beta, transthyretin, PRPH2, TIGR/MYOC) rather than papers about the amino acid valine as a pharmacological agent. This applies directly to the top-ranked candidate, sclerosing cholangitis: one cited paper concerns *tyrosine* (not valine) and fatigue in PBC/PSC, and the other is a Mendelian randomization study of general metabolites with no valine-specific causal signal identified.

One partial exception in the broader candidate list is rank 3 (hyperthyroidism, L4, "Research Question"), where two papers (PMID 39195533, 35256693) report genuine associations between circulating BCAA/valine levels and thyroid function — though these are observational metabolomic correlations, not therapeutic interventions, and directionality is unresolved. No such genuine mechanistic signal exists for the top-ranked sclerosing cholangitis prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma **tyrosine** (not valine) concentration and fatigue in PBC/PSC patients; no valine-specific finding |
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian Randomization | Frontiers in Medicine | General blood-metabolite causal analysis for cholestatic liver disease risk; does not specifically implicate valine |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (sclerosing cholangitis) is supported by zero clinical trials and two publications that do not actually study valine as a therapeutic agent — one examines a different amino acid (tyrosine), the other is a non-specific metabolomic causal-inference study. Combined with missing MOA data (DG002) and missing safety/label data (DG001, Blocking severity — required before any S1 safety pre-assessment), there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/FDA label warnings and contraindications) — currently blocking
- Resolve DG002 (confirmed mechanism of action for valine)
- Manual literature re-screening to exclude genetic-nomenclature false positives ("Val"/"V" mutation notation) across all ten predicted indications
- If pursuing further, prioritize re-evaluation of the hyperthyroidism signal (rank 3, L4), which has the only literature showing a genuine (if directionally unclear) BCAA–thyroid function association, over the current top-ranked sclerosing cholangitis candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

