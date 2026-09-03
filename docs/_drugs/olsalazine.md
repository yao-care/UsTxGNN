---
layout: default
title: Olsalazine
parent: 僅模型預測 (L5)
nav_order: 990
evidence_level: L5
indication_count: 10
---

# Olsalazine
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

Using the report evidence and required section order, since none of these candidates have MOA, trial, literature, or safety data, this report will surface the data gaps explicitly rather than filling them.

# Olsalazine: From Intestinal Anti-Inflammatory Use to Myelodysplastic Syndrome (Prediction Only)

## One-Sentence Summary

Olsalazine is a salicylate dimer prodrug of 5-ASA (mesalamine), pharmacologically known for local intestinal anti-inflammatory activity, though no structured original-indication or mechanism-of-action record exists in the current dataset. TxGNN's top prediction links olsalazine to **Myelodysplastic Syndrome (MDS)** with a 99.91% score, but this is currently backed by **zero clinical trials** and **zero publications** — a pure knowledge-graph signal with no independent corroboration.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no indication records in dataset |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the known information present in this evidence pack, olsalazine is classified as a 5-ASA (mesalamine) prodrug — a salicylate dimer whose established activity is local intestinal anti-inflammatory action (inhibition of prostaglandin/leukotriene synthesis in the gut). No original indication record was returned in the dataset, so its formally approved use cannot be stated here.

There is no established pathophysiological link between local intestinal anti-inflammatory activity and myelodysplastic syndrome, which arises from hematopoietic stem cell mutations and bone marrow dysplasia. The prediction's own rationale explicitly flags this: the score likely reflects graph-topology proximity (e.g., shared comorbidity or gene nodes between the two entities) rather than a genuine mechanistic hypothesis. Notably, the same pattern repeats across all 10 top-ranked candidates for this drug (rank 2–10 include hypotrichosis, alopecia, 5q-deletion, refractory cytopenia, and sideroblastic anemia) — none have any supporting trial or literature evidence, suggesting this may be a systematic artifact of the drug's graph neighborhood rather than 10 independent biological signals.

Given the complete absence of mechanistic, clinical, or literature support, this prediction should be treated as hypothesis-generating only, not as a basis for further clinical action at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No approved authorizations are on record. Olsalazine's market status in the evaluated jurisdiction is **not marketed** (0 licenses on file), so no product/dosage-form/indication data can be reported.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available in this dataset (DDI query returned no results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial, no literature, no MOA, and no safety data to support this candidate — it fails at the earliest evidence stage (S0/L5). The drug is also not currently marketed, so there is no regulatory or real-world usage baseline to draw on.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/FDA label warnings and contraindications before any safety pre-screen (S1) can occur
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to test the mechanistic plausibility of the MDS link
- Targeted literature/trial search specifically for "olsalazine" + "myelodysplastic syndrome" or "5-ASA" + "bone marrow" to check for any signal missed by current collectors
- Investigate whether the shared high scores across all 10 top predictions (hematologic + hair-related diseases) indicate a graph-embedding artifact specific to this drug node, before treating any single candidate as prioritized
- Basic pharmacovigilance data (marketed-country label, post-marketing reports) once market status is clarified, since this drug shows 0 licenses in the current jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

