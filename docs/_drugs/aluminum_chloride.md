---
layout: default
title: Aluminum Chloride
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Aluminum Chloride
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

# Aluminum Chloride: From Topical Antiperspirant/Hemostatic to Seborrheic Keratosis

## One-Sentence Summary

Aluminum Chloride (AlCl3, DB11081) is a well-established topical astringent used clinically as first-line treatment for primary focal hyperhidrosis and as a hemostatic agent in dermatologic procedures.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis** (TxGNN score: 99.68%),
however **no clinical trials** and **no publications** currently directly support this specific indication, placing it at evidence level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No FDA-approved NDA on record; established clinical use as topical antiperspirant for primary focal hyperhidrosis |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (no registered products in database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (MOA) is currently unavailable from DrugBank. Based on established pharmacological knowledge, Aluminum Chloride is a topical astringent that works primarily by precipitating proteins within eccrine sweat duct epithelium, forming physical occlusive plugs that suppress sweat secretion. It also exhibits antimicrobial activity (inhibition of skin flora including *Malassezia*), vasoconstrictive effects, and mild keratolytic properties.

The mechanistic bridge to seborrheic keratosis is rooted in AlCl3's demonstrated ability to induce keratinocyte apoptosis (PMID 31567135). Seborrheic keratosis is a benign epidermal tumor characterized by dysregulated keratinocyte proliferation; AlCl3's protein-precipitating and pro-apoptotic effects on keratinocytes could theoretically disrupt the hyperproliferative process underlying these lesions, while its mild keratolytic action may facilitate desquamation of thickened keratotic surfaces. However, this mechanistic construct currently has no supporting clinical or preclinical data.

It is important to note that AlCl3 carries **L1-level evidence** for the broader skin disease category (specifically primary focal hyperhidrosis, TxGNN rank 6), where it is recognized as standard of care. This dermatological efficacy profile provides biological plausibility for topical skin indications generally. A forthcoming exploratory Phase 1 trial (NCT07401277, not yet recruiting) is investigating 5-fluorouracil combined with aluminum for actinic keratoses — a keratotic skin condition with partial pathophysiological overlap with seborrheic keratosis — which may provide indirect mechanistic insights.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for seborrheic keratosis.

---

## Literature Evidence

Currently no related literature available for seborrheic keratosis.

---

## US Market Information

No FDA NDA approvals on record for Aluminum Chloride as a stand-alone regulated pharmaceutical product.

> **Note:** AlCl3 is widely incorporated into OTC antiperspirant formulations (e.g., 12–20% concentrations) and is used in prescription-strength hemostatic preparations in dermatology and dentistry. These OTC and procedural applications are not captured as standalone NDA submissions in the current regulatory database query and may explain the discrepancy between the absence of registered licenses and the compound's broad clinical use.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.68%), there is a complete absence of clinical trials and published literature directly supporting the use of Aluminum Chloride for seborrheic keratosis. The prediction is based entirely on model output (L5 evidence), and while a keratinocyte-apoptosis-based mechanistic hypothesis is conceptually plausible, it remains entirely unvalidated in this specific disease context.

**To proceed, the following is needed:**
- **Preclinical evidence:** In vitro keratinocyte proliferation assays using AlCl3 on seborrheic keratosis cell models; ex vivo tissue experiments or animal model studies to establish proof of concept
- **Clinical signal:** Case series or pilot observational studies documenting topical AlCl3 application to seborrheic keratosis lesions
- **MOA data:** Retrieve full mechanism of action from DrugBank (Data Gap DG002 — currently blocking mechanistic analysis)
- **Safety review:** Obtain TFDA/FDA package insert to characterize warnings, contraindications, and skin irritation profile (Data Gap DG001 — currently blocking safety stage S1 entry)
- **Formulation planning:** Determine appropriate concentration, vehicle, and application protocol for lesion-directed use, distinct from antiperspirant applications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

