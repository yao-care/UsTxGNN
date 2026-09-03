---
layout: default
title: Zinc Oxide
parent: 僅模型預測 (L5)
nav_order: 1308
evidence_level: L5
indication_count: 5
---

# Zinc Oxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Zinc Oxide: From Topical Skin Protectant to Acne

## One-Sentence Summary

> Zinc Oxide (DrugBank DB09321) has no formally recorded original indication in this dataset, but is widely known as a topical skin protectant and astringent used in dermatology and wound care.
> The TxGNN model predicts it may be effective for **Acne**,
> with **0 clinical trials** and **7 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in dataset; commonly used as a topical skin protectant/astringent (e.g., diaper rash, minor wound care) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for zinc oxide in this dataset. Based on known dermatological use, zinc oxide is an established topical agent with antibacterial (including activity against *Cutibacterium acnes*), anti-inflammatory, astringent, and sebum-modulating properties. These pharmacological characteristics are the traditional rationale for its long-standing inclusion in OTC acne care and skin-protectant formulations.

Because no formal original indication is recorded for this drug in the dataset, a direct indication-to-indication comparison cannot be made. However, the predicted link to acne is mechanistically plausible given zinc oxide's well-documented topical antimicrobial and anti-inflammatory activity, and its extensive real-world OTC usage history in skin conditions — even though this dataset does not contain registered clinical trials specifically evaluating zinc oxide monotherapy for acne.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29193602](https://pubmed.ncbi.nlm.nih.gov/29193602/) | 2018 | Review | Dermatologic Therapy | Reviews the role of zinc (including topical formulations) in acne treatment as an alternative to antibiotics/retinoids with a favorable safety profile |
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Review | International Journal of Dermatology | Discusses zinc oxide nanoparticles as an investigational topical treatment for acne vulgaris and other dermatologic conditions |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohort | Skin Research and Technology | Split-face clinical/bioinstrumental assessment of mild inflammatory catamenial acne |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Preclinical/Formulation | Science Advances | Zinc-porphyrin nanoparticle microneedle patch for bacterial acne treatment targeting *C. acnes* |
| [41033952](https://pubmed.ncbi.nlm.nih.gov/41033952/) | 2025 | Preclinical/In vitro | Science Bulletin | ZnO-based piezoelectric heterojunction for selective regulation of acne-associated skin microbiota |
| [31322532](https://pubmed.ncbi.nlm.nih.gov/31322532/) | 2019 | Preclinical/Formulation | Georgian Medical News | Development of powder formulations (incl. zinc-based) for acne treatment |
| [29284390](https://pubmed.ncbi.nlm.nih.gov/29284390/) | 2018 | Preclinical/Formulation | Current Medicinal Chemistry | Review of nanoparticle-functionalized textiles, including zinc-based coatings, for skin/wound care such as acne |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction is supported by a plausible, well-established mechanism (topical antibacterial/anti-inflammatory activity) and a body of review-level and preclinical literature, but lacks any registered clinical trials specifically testing zinc oxide for acne — placing the evidence at L3 with no confirmatory RCT data.

**To proceed, the following is needed:**
- TFDA (or relevant regulatory) label warnings and contraindications — currently a **Blocking** data gap (DG001)
- Formal mechanism of action (MOA) documentation from DrugBank or equivalent source — **High** priority gap (DG002)
- Prospective clinical trial data evaluating zinc oxide (monotherapy or combination) specifically in acne vulgaris
- Confirmation of route/dosage form suitability for a topical acne indication, given the drug is currently unmarketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

