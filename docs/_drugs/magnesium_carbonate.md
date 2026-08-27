---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 882
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: From Antacid (Symptomatic Hyperacidity) to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium carbonate is a classic acid-neutralizing antacid agent; no formal regulatory-approved indication text is on record, and it is currently **not marketed** in the reference market. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **0 clinical trials** and **4 publications** currently supporting this direction, three of which are randomized controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antacid (gastric acid neutralization / symptomatic hyperacidity) — no formal approved indication text on record |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this candidate. Based on known pharmacology, magnesium carbonate is a classic inorganic antacid: MgCO₃ + 2HCl → MgCl₂ + H₂O + CO₂. It neutralizes gastric hydrochloric acid on contact, raises intragastric pH, and reduces pepsin activity — the same mechanistic class documented for related magnesium/aluminum antacid combinations in the evidence pack's own rationale notes for adjacent indications.

Active peptic ulcer disease is, by definition, an acid-mediated mucosal injury, so acid neutralization is a direct, mechanistically appropriate intervention rather than a distant repurposing leap. Historically, antacids (including magnesium- and aluminum-based combination products such as Novaluzid and Caved-S) were a first-line ulcer treatment before H2-blockers and PPIs became standard, which supports the biological plausibility of this TxGNN prediction — though the supporting literature below largely studies antacid combination products rather than magnesium carbonate as a single agent, so drug-specificity is moderate rather than high.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | 72 patients with duodenal/prepyloric ulcers randomized to cimetidine, antacid suspension + anticholinergic, or placebo; 3-week healing rate was 67% (cimetidine) vs 50% (antacid/anticholinergic), both significantly better than placebo. |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | 80 patients with active duodenal ulcer received antacid tablets (1.1 g, 4×/day) alongside high- or low-fiber diets; 4-week healing rates were 67.5% (high-fiber) vs 60% (low-fiber), with no significant difference between diet arms — antacid effect not isolated. |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scandinavian Journal of Gastroenterology. Supplement | Companion report to the Ström et al. trial design, comparing antacid/anticholinergic, cimetidine, and placebo in active prepyloric and duodenal ulcer patients; abstract not available. |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro pharmacology | Medicine and Pharmacy Reports | Evaluated the acid-neutralizing capacity (ANC) and other physicochemical properties of antacid products marketed in Morocco; supports class-level mechanism but not clinical efficacy. |

---

## US Market Information

Currently not marketed in the reference market (market status: 未上市／Not Marketed). No NDA or license records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link is strong (acid neutralization directly addresses peptic ulcer pathophysiology) and three RCTs support antacid efficacy in active ulcer disease, but the trials studied antacid combination products rather than magnesium carbonate as a single agent, and the drug is unmarketed with no NDA on file. This warrants formal research investigation rather than immediate go/hold classification.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- DrugBank-sourced mechanism of action for magnesium carbonate specifically (currently a High-severity data gap)
- Drug interaction (DDI) data (current query returned no results)
- Trials or literature isolating magnesium carbonate as a single agent rather than combination antacid products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

