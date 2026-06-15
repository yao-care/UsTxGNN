---
layout: default
title: Amanita Muscaria Fruiting Body American Ginseng Ch
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 0
---

# Amanita Muscaria Fruiting Body American Ginseng Ch
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Nine-Ingredient Botanical Compound (Yohimbine / Saw Palmetto / American Ginseng et al.): No Approved Indication — TxGNN Repurposing Assessment Not Feasible

## One-Sentence Summary

This candidate is a complex mixture of nine botanical and mineral ingredients — including yohimbine, saw palmetto, American ginseng, damiana (*Turnera diffusa*), skullcap (*Scutellaria lateriflora*), chaste tree, *Amanita muscaria*, selenium, and phosphoric acid — with no regulatory approval in any jurisdiction on record.
The TxGNN model was unable to generate any repurposing predictions for this combination, most likely because multi-ingredient botanical blends of this type are not represented as unified entities in the knowledge graph.
As a result, **no evidence level can be assigned** and no repurposing direction is currently assessable.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory approval on record) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable (no prediction generated) |
| US/TW Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why Assessment Is Not Feasible

This submission contains nine distinct active substances bundled into a single compound entry:

| Ingredient | Known Pharmacological Role |
|---|---|
| Yohimbine | α₂-adrenergic antagonist; traditionally used for sexual dysfunction |
| Saw palmetto (*Serenoa repens*) | 5α-reductase inhibitory properties; BPH/androgenic conditions |
| American ginseng | Adaptogen; immune modulation |
| Chaste tree (*Vitex agnus-castus*) | Dopaminergic / prolactin-modulating herb |
| Damiana (*Turnera diffusa* leafy twig) | Traditional aphrodisiac; anxiolytic |
| Skullcap (*Scutellaria lateriflora* whole) | GABAergic / anxiolytic herb |
| *Amanita muscaria* fruiting body | Muscarinic receptor modulator; psychoactive at higher doses |
| Selenium | Essential trace mineral; antioxidant cofactor |
| Phosphoric acid | Acidifying excipient / stabiliser |

The TxGNN knowledge graph is built around single-molecule DrugBank entities. A nine-ingredient botanical blend cannot be mapped to a single DrugBank ID, so the prediction pipeline has no entry point. This is a structural data limitation, not a clinical judgement about the ingredients themselves.

Individually, several ingredients (especially yohimbine and saw palmetto) do have DrugBank records and published clinical evidence. A meaningful repurposing analysis would require **decomposing this compound into individual components** and running TxGNN on each separately.

---

## US/TW Market Information

No regulatory authorisations are on record for this exact combination in Taiwan or the United States.

---

## Safety Considerations

> Several ingredients in this mixture carry clinically significant safety signals that must be addressed before any further evaluation:
>
> - **Yohimbine**: Narrow therapeutic index; documented risks of hypertensive crisis, tachycardia, anxiety, and interactions with MAOIs and antihypertensives.
> - **Amanita muscaria**: Contains ibotenic acid and muscimol; toxic and psychoactive at non-micro doses; regulatory status varies by jurisdiction.
> - **Phosphoric acid**: Corrosive excipient; safe only within tightly controlled pH ranges.
>
> Formal safety data (package insert warnings, contraindications, DDI profile) are not available for this combination. Please consult primary literature for each individual ingredient before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline cannot process a nine-ingredient botanical mixture as a unified entity, and no original indication, regulatory approval, or repurposing prediction exists to evaluate. The presence of *Amanita muscaria* and yohimbine also raises independent safety concerns that require resolution before any development pathway is considered.

**To proceed, the following is needed:**

- **Decompose into individual components**: Run TxGNN repurposing analysis separately for each of the nine ingredients using their individual DrugBank IDs (where available — yohimbine: DB01392; saw palmetto: DB12880; selenium: DB01593; American ginseng: DB15699).
- **Clarify the intended indication**: Identify the clinical rationale for combining these nine ingredients — the profile (yohimbine + saw palmetto + damiana) strongly suggests a sexual health / andrological target, but this must be confirmed by the submitter.
- **Amanita muscaria safety review**: Determine the dose level and extract type; this ingredient requires a standalone regulatory and toxicological assessment before any human use pathway.
- **DDI assessment per component**: Run individual DDI queries for yohimbine (especially MAOIs, antihypertensives, stimulants) and ginseng (especially anticoagulants).
- **Regulatory feasibility check**: Confirm whether this combination can be registered as a botanical drug (e.g., FDA Botanical Drug Guidance) or dietary supplement, and whether *Amanita muscaria* is permissible as an ingredient in the target market.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

