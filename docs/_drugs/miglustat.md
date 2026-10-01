---
layout: default
title: Miglustat
parent: Model Prediction Only (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Autosomal Ichthyosis Syndrome with Fatal Disease Course

## One-Sentence Summary

Miglustat is an oral glucosylceramide synthase inhibitor, originally used for type 1 Gaucher disease. The TxGNN model predicts it may be effective for **autosomal ichthyosis syndrome with fatal disease course**, but **no clinical trials and no publications** currently support this prediction. It is a model-only signal (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 Gaucher disease (taken from the literature; the US label indication text was not provided) |
| Predicted New Indication | Autosomal ichthyosis syndrome with fatal disease course |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 licenses (1 brand NDA, Zavesca; the rest are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. From general pharmacology, miglustat inhibits glucosylceramide synthase, which lowers the synthesis of glucosylceramide and related glycosphingolipids (substrate reduction therapy). Its efficacy in Gaucher disease is established, and mechanistically it may be applicable to other sphingolipid disorders.

Ichthyosis syndromes often involve disrupted epidermal lipid or ceramide metabolism, so a sphingolipid-pathway connection is conceivable. However, the specific molecular defect in this disease is unspecified, and the link is speculative. The high score should be read as a model output, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021348 | Zavesca (Actelion Pharmaceuticals US) | Capsule | Not provided |
| ANDA209821 | Yargesa (Edenbridge Pharmaceuticals) | Capsule | Not provided |
| ANDA208342 | Miglustat (ANI Pharmaceuticals) | Capsule | Not provided |
| ANDA219111 | Miglustat (Navinta) | Capsule | Not provided |
| ANDA219111 | Miglustat (Zydus Pharmaceuticals USA) | Capsule | Not provided |

All listed products are oral capsules.

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contained no drug interaction records for miglustat.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials or literature for this indication, the disease's molecular defect is unspecified, and the mechanistic link is speculative.

**Better-supported prediction in the same pack:** Tay-Sachs disease (rank 7, score 99.75%, L2) is the only prediction with clinical evidence. It has miglustat trials in GM2 gangliosidosis (NCT00672022, NCT00418847, NCT03822013, NCT02030015) and a randomized late-onset study (PMID 19346952). However, that study and a 2023 systematic review (PMID 37209042) do not show a clear neurological benefit. It is best treated as a research question rather than a Go candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Identification of the specific genetic and biochemical defect in this ichthyosis syndrome, to test whether glucosylceramide synthase inhibition is relevant
- Preclinical or literature evidence in ichthyosis models before any clinical consideration
- Route compatibility assessment (oral capsule only is currently available)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

