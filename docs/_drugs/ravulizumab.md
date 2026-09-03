---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 1112
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Diseases (PNH/aHUS) to Autosomal Recessive Severe Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

> Ravulizumab is a long-acting anti-C5 monoclonal antibody globally approved for complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS).
> TxGNN predicts a possible link to **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale itself is assessed as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan license data (drug not marketed); per embedded rationale, globally approved for complement-mediated diseases (PNH, aHUS) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal `original_moa` field in this evidence pack is a data gap. However, the repurposing rationale attached to the top prediction discloses that ravulizumab is a long-acting anti-C5 monoclonal antibody that inhibits terminal complement activation (formation of the C5b-9 membrane attack complex), and that its approved mechanism targets complement-mediated diseases such as PNH and aHUS.

The predicted new indication — congenital neutropenia due to G6PC3 deficiency — has a fundamentally different pathophysiology: neutropenia in this condition arises from ER stress-induced apoptosis of bone marrow myeloid progenitors, not from complement-driven cell lysis. The evidence pack's own mechanistic analysis explicitly flags this gap, stating there is "no known direct association" between the G6PC3 pathway and terminal complement activation, and suggests the high TxGNN score may reflect indirect graph proximity around "neutropenia"-related nodes rather than a genuine mechanistic relationship.

This same pattern repeats across ranks 2–10 in this candidate set (cyclic hematopoiesis, primary hyperoxaluria, various congenital neutropenia subtypes, pseudo-von Willebrand disease, platelet release disorders, megaloblastic anemia) — all scored L5 with rationale text noting the absence of a credible complement-mediated mechanism. This suggests the prediction cluster reflects a shared knowledge-graph signal rather than independently validated biology, and should be treated as hypothesis-generating only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA-equivalent label warnings/contraindications (DG001) are marked as a **Blocking** data gap in this evidence pack, meaning a formal S1 safety evaluation cannot proceed until this data is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-driven (L5) prediction with no supporting clinical trials or literature, and the drug's own embedded mechanistic rationale explicitly questions the biological plausibility of a complement-C5-to-G6PC3-neutropenia link. Combined with the drug's non-marketed status in this jurisdiction, there is insufficient basis to advance beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA (or equivalent) approved label — warnings, contraindications, and DDI data (DG001, blocking)
- Confirmed mechanism of action via DrugBank API query (DG002)
- Preclinical or translational studies testing whether complement activation contributes to G6PC3-deficient neutropenia pathophysiology
- Any case reports or off-label use data of ravulizumab in congenital neutropenia populations
- Regulatory pathway assessment, given zero existing local market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

