---
layout: default
title: Raxibacumab
parent: 僅模型預測 (L5)
nav_order: 1113
evidence_level: L5
indication_count: 8
---

# Raxibacumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Raxibacumab: From Inhalational Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

Raxibacumab is a monoclonal antibody originally developed to neutralize *Bacillus anthracis* protective antigen (PA) for the treatment and post-exposure prophylaxis of inhalational anthrax. TxGNN's top-ranked prediction suggests possible efficacy in **postinfectious vasculitis**, but this signal is supported by **zero clinical trials** and **zero publications**, and the model's own rationale states no known mechanistic link exists — this is a graph-based (L5) prediction only, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory data (drug is not marketed locally); publicly known original indication is inhalational anthrax (treatment and post-exposure prophylaxis) |
| Predicted New Indication | Postinfectious Vasculitis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available as a structured field, but the evidence pack's rationale confirms raxibacumab acts as a monoclonal antibody that binds and neutralizes the protective antigen (PA) component of *B. anthracis* toxin — a highly pathogen-specific mechanism with no known role in general immune-complex-mediated vasculitis.

Postinfectious vasculitis is a systemic immune-complex process that can follow a wide range of infections, but it is not driven by anthrax toxin or PA. The repurposing rationale explicitly states: *"與感染後血管炎（免疫複合物介導之全身性血管炎）無已知機轉關聯。TxGNN 高分屬圖譜共現訊號，無生物學基礎支持"* — i.e., the model's high score reflects knowledge-graph co-occurrence patterns rather than any established or plausible biological mechanism.

**Important context on the broader prediction set:** All eight ranked predictions in this evidence pack were reviewed. Ranks 1, 2, 4, 5, 6, 7, and 8 (postinfectious vasculitis, post-infectious syndrome, infective urethral stricture, otitis externa, Chagas cardiomyopathy, infection-related HUS, drug-induced osteoporosis) each explicitly lack mechanistic plausibility per their own rationale text, and none have any clinical trial or literature evidence — all are scored L5/Hold. Rank 3 ("post-bacterial disorder") is the only entry with strong evidence (L1, 3 clinical trials), but its own rationale flags that this is a **semantic restatement of the original anthrax indication**, not a genuine new indication — the trials listed (NCT02339155, NCT07478471, NCT02177721) all concern anthrax treatment/prophylaxis directly. It should therefore be treated as confirmation of the known label, not a repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Raxibacumab currently has no license/authorization records in this jurisdiction (total_licenses: 0; market_status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate indication (postinfectious vasculitis) has no clinical trial or literature support, and the model's own mechanistic rationale confirms no biological basis for the association — this reflects knowledge-graph noise rather than a credible repurposing signal. The only prediction with substantive evidence (rank 3) is mechanistically identical to raxibacumab's existing anthrax indication and does not represent a novel therapeutic direction.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action and TFDA label data (currently blocked per data gap DG001/DG002) before any safety evaluation can begin
- A genuine mechanistic hypothesis linking PA-neutralizing antibody activity to a non-anthrax disease process, independent of graph co-occurrence scoring
- If pursued further, reclassify rank 3 ("post-bacterial disorder") as label-confirmation evidence rather than a new-indication candidate, and exclude ranks 1, 2, 4–8 from further review given L5 status and explicit lack of biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

