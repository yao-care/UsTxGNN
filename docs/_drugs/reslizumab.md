---
layout: default
title: Reslizumab
parent: 僅模型預測 (L5)
nav_order: 1117
evidence_level: L5
indication_count: 2
---

# Reslizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Reslizumab: From Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

> Reslizumab is a biologic (anti-IL-5 monoclonal antibody) known for use in severe eosinophilic asthma, though this original indication is not confirmed in the current evidence pack.
> The TxGNN model predicts it may be effective for **Thrombocytopenia Due to Immune Destruction**,
> but **no clinical trials** and **no literature** currently support this specific direction — the prediction is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory license data (drug is not marketed in this jurisdiction); known drug-class use is eosinophilic asthma, per mechanistic narrative in the evidence pack rather than an official label |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no clinical or preclinical support) |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is officially marked as a data gap (DG002) in this evidence pack. However, the model's own rationale text identifies reslizumab as an anti-IL-5 monoclonal antibody that suppresses eosinophil proliferation and activation, consistent with its known use in eosinophilic asthma.

Critically, the evidence pack's own mechanistic assessment states that this pathway has **no direct biological link** to the core mechanism of immune thrombocytopenia (autoantibody-mediated platelet destruction and impaired megakaryopoiesis). The high TxGNN score (99.53%) is interpreted as likely reflecting indirect graph connections between eosinophil/immune-modulation nodes in the knowledge graph, rather than a causal or pharmacologically plausible relationship. No supporting clinical or translational evidence currently exists.

Given the absence of mechanistic plausibility and supporting evidence, this prediction should be treated as a low-confidence, purely data-driven signal rather than a scientifically supported repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No license or NDA records are available — the drug is not currently marketed in this jurisdiction, so no approved indication text can be extracted.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent warnings/contraindications for this drug are marked as a blocking data gap — see Next Steps.)*

---

## Additional Predicted Indication (Secondary, Not Elaborated)

The evidence pack also includes a second, weaker candidate: **Primary Release Disorder of Platelets** (TxGNN score 99.25%, rank 16467, Evidence Level L5). The single supporting reference (PMID [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/), a 2010 review on hypereosinophilic syndrome management) discusses a *different* anti-IL-5 antibody (mepolizumab) and does not specifically address platelet release disorders — it is class-level, indirect evidence at best. Recommendation for this candidate is also **Hold**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by TxGNN model scores with no corroborating clinical trials or disease-specific literature, and the evidence pack's own mechanistic analysis finds no credible biological pathway connecting reslizumab's anti-IL-5 activity to immune-mediated platelet disorders. Evidence Level L5 and the absence of any experimental or clinical signal do not support advancing to further evaluation stages (currently S0).

**To proceed, the following is needed:**
- TFDA-equivalent warnings, contraindications, and label data (DG001 — blocking; required before any safety pre-screen/S1 stage)
- Confirmed mechanism of action via DrugBank API query (DG002 — high priority; needed to properly assess mechanistic plausibility)
- Disease-specific preclinical or translational evidence directly linking IL-5/eosinophil biology to immune thrombocytopenia or platelet release disorders, if this candidate is to be reconsidered
- Continued monitoring for new clinical trial registrations or publications specific to reslizumab in either predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

