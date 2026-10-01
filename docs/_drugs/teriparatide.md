---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 1215
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide is a parathyroid hormone (PTH 1-34) analog, used as a bone-building drug for osteoporosis.
The TxGNN model ranks **duodenal ulcer** as its top prediction (score 99.86%), but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (the license records contain no indication text; this comes from the pack's mechanism notes) |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Teriparatide is a PTH(1-34) analog that acts on bone remodeling through the PTH1 receptor. Detailed mechanism of action data is not available from DrugBank. Its established role is as a bone anabolic agent for osteoporosis.

No mechanistic link between this action and duodenal ulcer has been established. Duodenal ulcer is a gastrointestinal mucosal disease, and PTH1 receptor signaling in bone offers no clear rationale for treating it. The high TxGNN score reflects a pattern in the knowledge graph, not supporting trial or literature evidence. The prediction should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA211097 | Teriparatide (Apotex Corp.) | Injection, solution | Not listed in the records |
| NDA216490 | Yorvipath (Ascendis Pharma) | Injection, solution | Not listed in the records |
| NDA021318 | Teriparatide (Prasco Laboratories) | Injection, solution | Not listed in the records |
| NDA211939 | Teriparatide (Alvogen, Inc.) | Injection, solution | Not listed in the records |
| ANDA213641 | Teriparatide (Amphastar Pharmaceuticals) | Injection | Not listed in the records |

Ten authorizations exist in total; the five above are the main ones listed. All are injectable products.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the available data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction rests on a graph-based score alone, with no clinical trials, no literature, and no plausible mechanistic link to PTH1 receptor signaling. It is not a candidate for further investment at this time.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking PTH signaling to duodenal ulcer, plus any preclinical evidence
- The FDA package insert (warnings, contraindications) and detailed MOA data
- Any registered clinical trials or peer-reviewed literature in this indication

**Note on other predictions from the same pack:** The strongest candidate is not the top-ranked one. **Pregnancy-associated osteoporosis** (TxGNN score 99.55%) has L3 evidence and a "Proceed with Guardrails" recommendation. It is supported by a multicenter retrospective cohort of teriparatide in pregnancy- and lactation-associated osteoporosis (PMID 34132853), a 47-patient series (PMID 35903718), and several systematic reviews. However, the 2025 meta-analysis found the treatment-response data inconclusive (PMID 40205203), and no Phase 2/3 RCT exists. It would be the more productive direction to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

