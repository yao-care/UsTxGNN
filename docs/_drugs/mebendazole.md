---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 888
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Mebendazole: From Anthelmintic Use to Acne (Disease)

## One-Sentence Summary

Mebendazole is a benzimidazole-class anthelmintic (deworming) drug used to treat parasitic infections; official original-indication data is not on file for this evidence pack.
The TxGNN model predicts it may be effective for **Acne (Disease)**, with **no clinical trials** and only **1 tangentially related case report** currently identified.
Both the mechanism-of-action data and the safety/label data needed to evaluate this prediction are marked as blocking gaps, so the evidentiary basis is essentially the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in licenses data (drug not marketed in Taiwan); mechanistic notes describe it as a benzimidazole-class anthelmintic |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available (flagged as a High-severity data gap, DG002). Based on the information available in this evidence pack, mebendazole is a benzimidazole-class anthelmintic whose known mechanism is inhibition of parasitic β-tubulin polymerization, which disrupts microtubule formation in helminths.

This mechanism has separately been explored in oncology contexts for potential anti-mitotic and anti-angiogenic activity, but there is no established pharmacological link between this mechanism and acne, which is driven by sebaceous gland inflammation and *Cutibacterium (Propionibacterium) acnes*-related pathology. No shared pathway between the original anthelmintic use and the predicted dermatological indication has been identified in the source data.

Because the drug-level MOA record itself is a data gap, no compound-level mechanistic reasoning can be constructed to support this prediction. The TxGNN score of 0.99 reflects a knowledge-graph link prediction only and should not be interpreted as mechanistic or clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case Report | The American Journal of Tropical Medicine and Hygiene | Case report of human proliferative sparganosis (a parasitic infection) presenting with acne-like nodular/papular skin lesions; "acne-like" is used descriptively for lesion appearance, not as a treated indication. No data on mebendazole efficacy in acne. |

## US Market Information

Currently no marketing authorization on file (market status: Not Marketed; 0 licenses recorded).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no genuinely relevant literature supporting mebendazole for acne — the single retrieved publication is a case report on an unrelated parasitic disease that only uses "acne-like" as a lesion descriptor. Combined with two blocking/high-severity data gaps (TFDA label/warnings data and mechanism-of-action data), there is insufficient evidence to proceed past model prediction (L5).

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank to establish a plausible pharmacological rationale (DG002)
- TFDA label warnings/contraindications to complete a baseline safety assessment (DG001, blocking)
- A targeted literature search specifically evaluating mebendazole (or benzimidazoles) in dermatologic/acne-relevant contexts
- Preclinical or mechanistic studies linking β-tubulin inhibition to sebaceous gland or *C. acnes*-related pathways, if this direction is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

