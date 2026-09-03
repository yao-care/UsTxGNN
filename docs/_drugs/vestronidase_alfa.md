---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 1289
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Vestronidase Alfa: From Mucopolysaccharidosis VII to Scheie Syndrome (Low-Confidence Prediction)

## One-Sentence Summary

> Vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy; per the literature captured in this evidence pack, its established indication is Mucopolysaccharidosis type VII (MPS VII / Sly syndrome).
> TxGNN's top-ranked prediction for repurposing is **Scheie syndrome**, but this is supported by **0 clinical trials** and **0 publications**, and the drug's own review rationale flags the prediction as a likely category-level false positive rather than a genuine mechanistic match.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis type VII (MPS VII / Sly syndrome) — derived from literature evidence in this pack; no formal regulatory license text is available |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only — 0 trials, 0 literature) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for vestronidase alfa is not directly available in this pack (flagged as a Blocking/High-severity data gap). However, literature evidence retrieved under a different ranked candidate (PMID 30467742) confirms that vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy, approved for MPS VII, a lysosomal storage disorder caused by GUS deficiency.

Scheie syndrome, the top-ranked TxGNN prediction, is a subtype of MPS I, caused by deficiency of a different enzyme — α-L-iduronidase (IDUA) — not GUS. The rationale accompanying this prediction explicitly states there is no substrate overlap between IDUA and GUS: the two enzymes act on different glycosaminoglycan degradation steps, so vestronidase alfa would not be expected to have pharmacological activity in Scheie syndrome.

Given this, the TxGNN score most likely reflects a **category-level (embedding) similarity** — both diseases are lysosomal storage disorders — rather than a true substrate-level mechanistic relationship. This is corroborated by the complete absence of clinical trial or literature evidence directly linking vestronidase alfa to Scheie syndrome. On mechanistic grounds alone, this prediction should be treated as unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Scheie syndrome) has no supporting clinical trial or literature evidence and is contradicted on mechanistic grounds — it targets a different enzyme deficiency (IDUA) than the one vestronidase alfa treats (GUS). A broader review of all 9 TxGNN-predicted indications for this drug shows the same pattern: 6 of 9 candidates (including Scheie syndrome) have no evidence at all (L5), and the 2 candidates with literature/trial support show either indirect trial linkage only (Hurler syndrome, via a multi-disease Phase 1 basket trial where each subtype would use its own approved enzyme, not vestronidase alfa) or evidence that appears to be **mislabeled data pointing back to the drug's original MPS VII indication rather than genuine Sanfilippo syndrome evidence** (PMIDs 32063397, 30467742, 29478819 all describe MPS VII trials, not MPS III/Sanfilippo). No candidate in this set currently clears even a preliminary mechanistic or evidentiary bar for repurposing.

**To proceed, the following is needed:**
- Formal DrugBank/FDA-label MOA and approved-indication text for vestronidase alfa (currently a Blocking data gap)
- TFDA label warnings/contraindications (currently a Blocking data gap)
- Data-quality audit of the literature evidence pipeline for the Sanfilippo syndrome candidate, where retrieved abstracts appear to describe the drug's original MPS VII indication rather than the predicted new indication
- If any candidate is to be pursued further, disease-specific enzyme/substrate compatibility screening should precede any trial-evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

