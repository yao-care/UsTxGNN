---
layout: default
title: Tazarotene
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tazarotene: From Acne & Psoriasis to Seborrheic Dermatitis

## One-Sentence Summary

Tazarotene is a third-generation topical retinoid (RAR-β/γ agonist) primarily established for acne vulgaris and plaque psoriasis, though no Taiwan regulatory licenses are on record.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**, currently supported by only **1 tangentially related clinical trial** (targeting acne, not seborrheic dermatitis) and **no directly relevant published literature**.
Evidence sits at the mechanistic reasoning level (L4); dedicated clinical investigation is required before any development decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris; plaque psoriasis (not captured in Taiwan regulatory dataset) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the regulatory dataset. Based on established pharmacological knowledge, tazarotene belongs to the third-generation retinoid class and selectively activates retinoic acid receptors β and γ (RAR-β/γ). Through this receptor pathway, it normalizes abnormal keratinocyte proliferation, induces terminal differentiation, and suppresses pro-inflammatory cytokines including IL-1β and TNF-α. These properties underpin its proven efficacy in acne vulgaris and plaque psoriasis.

Seborrheic dermatitis shares some pathophysiological features with tazarotene's known targets: it involves aberrant keratinocyte turnover and a chronic inflammatory skin microenvironment. The anti-proliferative and anti-inflammatory mechanisms of RAR-β/γ agonism could in principle reduce the keratinocyte abnormalities and barrier dysfunction observed in seborrheic dermatitis, making the TxGNN prediction biologically plausible at the mechanistic level.

However, the primary driver of seborrheic dermatitis — *Malassezia* yeast overgrowth and the downstream immune dysregulation — falls outside the known target range of retinoids. The mechanistic link is therefore indirect at best, and direct clinical translation cannot be assumed. This prediction should be treated as an early-stage hypothesis requiring dedicated experimental validation before further development investment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | NA | Unknown | 40 | Compared PRP versus unspecified topical retinoids in acne vulgaris; does not target seborrheic dermatitis and does not name tazarotene specifically |

> **Note:** The sole identified trial addresses acne vulgaris, not seborrheic dermatitis, and uses generic "topical retinoids" without specifying tazarotene. This constitutes indirect background context for the retinoid class in dermatology, not direct evidence for the predicted indication. Trial phase is unclassified and current status is unknown, further limiting its weight.

---

## Literature Evidence

Currently no related literature available for tazarotene in seborrheic dermatitis.

---

## Market Authorization Information

Tazarotene has no approved licenses registered in Taiwan. There are no authorization records to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for tazarotene in seborrheic dermatitis is confined to indirect mechanistic reasoning (L4) — there are no clinical trials directly testing this indication and no supporting publications. Critically, the primary pathogenic driver (*Malassezia*) is not addressed by retinoid pharmacology, which substantially weakens the translational case.

**To proceed, the following is needed:**
- Dedicated preclinical studies (in vitro or animal models) demonstrating tazarotene activity in *Malassezia*-driven inflammation or seborrheic dermatitis-like skin phenotypes
- Class-level literature review: assess whether any retinoid (tretinoin, adapalene, tazarotene) has shown benefit in seborrheic dermatitis, to determine if evidence can be extrapolated
- Complete MOA documentation via DrugBank API query (DG002 remediation)
- Taiwan FDA product monograph to capture full warnings, contraindications, and label-level safety data (DG001 remediation)
- If preclinical signals are positive, design a small proof-of-concept pilot trial in seborrheic dermatitis patients with tazarotene cream/gel as the study intervention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

