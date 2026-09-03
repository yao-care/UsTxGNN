---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 1276
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Upadacitinib: From Not Marketed in Taiwan to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib is a JAK1-selective inhibitor; however, no Taiwan market history or approved indication is recorded for this drug in the current evidence pack.
TxGNN predicts a possible link to **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital malformation syndrome, with a prediction score of **99.61%**.
However, **0 clinical trials** and **0 publications** currently support this direction, and the model's own mechanistic analysis suggests this is likely a knowledge-graph artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Taiwan (no TFDA license records) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed (in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for upadacitinib as a standalone field is not available in this evidence pack. Based on the model's own mechanistic notes, upadacitinib is understood to be a **selective JAK1 inhibitor**, acting on cytokine-driven signal transduction (IL-6, IL-13, IFN, and related pathways) — a mechanism typically relevant to inflammatory and immune-mediated diseases.

The predicted indication, however, is a **rare congenital developmental syndrome** combining ocular coloboma/microphthalmia with rhizomelic skeletal dysplasia. This condition is understood to arise from developmental patterning or peroxisomal/ciliary gene defects, not from cytokine-driven inflammation. There is no established biological pathway connecting JAK1 inhibition to the structural developmental defects underlying this syndrome.

The evidence pack's own repurposing rationale explicitly concludes that the high TxGNN score is most likely driven by **sparse graph connectivity** around this rare disease node in the knowledge graph, rather than a real mechanistic relationship — i.e., a probable model artifact rather than a credible biological hypothesis.

A second, lower-ranked prediction (brachydactyly-syndactyly syndrome, score 99.58%) shows the same pattern: a congenital limb-patterning disorder with no known JAK1-STAT involvement, and the same "likely artifact" conclusion in the model's rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorization records are available — upadacitinib is currently not marketed in Taiwan (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and confirmed MOA data are flagged as outstanding data gaps — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both candidate indications are rare congenital structural/developmental syndromes with no plausible mechanistic link to JAK1 inhibition, zero supporting clinical trials or literature, and the model's own rationale identifies the high scores as likely knowledge-graph artifacts rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Independent mechanistic plausibility review before considering any further evidence-collection effort, since no clinical or literature signal currently exists for either predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

