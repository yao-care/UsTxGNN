---
layout: default
title: Nifurtimox
parent: 僅模型預測 (L5)
nav_order: 964
evidence_level: L5
indication_count: 7
---

# Nifurtimox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nifurtimox: From Chagas Disease to Congenital Analbuminemia

## One-Sentence Summary

Nifurtimox is a nitrofuran-class antiparasitic historically used to treat Chagas disease (American trypanosomiasis) and, in combination therapy, African trypanosomiasis. The TxGNN model predicts a possible link to **Congenital Analbuminemia**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal with no identifiable biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chagas disease (American trypanosomiasis) — based on known drug identity; no Taiwan/US license records are present in this Evidence Pack |
| Predicted New Indication | Congenital Analbuminemia |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nifurtimox belongs to the nitrofuran class of antiparasitic agents; its efficacy in Chagas disease has been established, acting through nitroreductase-mediated activation to generate free radicals/oxidative stress and inhibit trypanothione reductase in the parasite.

Congenital analbuminemia is a monogenic disorder (ALB gene defect) causing a hepatic protein-synthesis deficiency — a pathophysiology with no known overlap with antiparasitic oxidative-stress mechanisms. The evidence pack's own mechanistic assessment concludes there is **no identifiable biological pathway** connecting nifurtimox's pharmacology to this disease, and judges the high TxGNN score as most likely a knowledge-graph embedding coincidence rather than a genuine mechanistic signal.

Notably, six other TxGNN-predicted indications for this drug (polyclonal hyperviscosity syndrome, hyperamylasemia, blood group incompatibility, monoclonal gammopathy, premalignant hematological disease, and hematological disease associated with acquired peripheral neuropathy) were also screened, all scoring similarly high (~99%) with equally weak or absent mechanistic support. One of these — peripheral neuropathy-associated hematological disease — is flagged as a **potential inverse signal**, since peripheral neuropathy is a known adverse effect of nifurtimox, and the model may have learned a drug-causes-disease association rather than a treatment relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Nifurtimox is not currently marketed and no NDA/license records are present in this Evidence Pack (`taiwan_regulatory.total_licenses = 0`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by any clinical trial, literature, or plausible mechanistic link (Evidence Level L5, model prediction only). A TFDA label/warnings data gap is also flagged as **Blocking**, meaning safety cannot be assessed at all for this candidate.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings, contraindications) — currently a Blocking data gap
- Confirmed original mechanism of action (MOA) from DrugBank or primary literature
- Preclinical or case-level evidence establishing a biological rationale for congenital analbuminemia specifically
- Re-evaluation of the peripheral-neuropathy-associated candidate to rule out an inverse (adverse-effect) signal before any further screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

