---
layout: default
title: Carteolol
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 1
---

# Carteolol
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

Based on the Evidence Pack, I'll now generate the evaluation report.

---

# Carteolol: From Chronic Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Carteolol is a non-selective β1/β2 adrenergic receptor blocker with intrinsic sympathomimetic activity (ISA), historically approved as an ophthalmic solution for chronic open-angle glaucoma, though it is no longer marketed in the US.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **0 clinical trials** and **0 publications** currently identified for this specific indication — the prediction is supported by mechanistic rationale alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic open-angle glaucoma (ophthalmic use; no active US NDA on file) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| US Market Status | ✗ Not marketed (0 NDAs) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carteolol is a non-selective β1/β2 adrenergic receptor blocker with intrinsic sympathomimetic activity (ISA). Its primary ocular mechanism operates through the following pathway: β-receptor blockade → suppression of cAMP in the ciliary body → reduced aqueous humor production (approximately 20–30%) → lowering of intraocular pressure (IOP). This mechanism directly addresses the core pathophysiological driver of most glaucoma subtypes — elevated IOP due to impaired aqueous drainage.

Primary hereditary glaucoma encompasses two major subtypes: primary congenital glaucoma (PCG) and juvenile open-angle glaucoma (JOAG). Both are characterized by structural or functional defects in the trabecular meshwork and Schlemm's canal, resulting in aqueous outflow obstruction and IOP elevation. Because carteolol reduces aqueous humor *production* rather than improving outflow, its mechanism remains pharmacologically valid even when the drainage apparatus is structurally compromised. In this sense, the mechanistic overlap with chronic open-angle glaucoma — the drug's historical approved indication — is direct and strong.

While the current data gap on formal MOA documentation (DrugBank record not fully retrieved) limits quantitative confidence, the repurposing rationale is mechanistically coherent. Carteolol ophthalmic solution did hold FDA approval for open-angle glaucoma, which shares IOP-lowering as the therapeutic goal with primary hereditary glaucoma. The TxGNN score of 99.92% reflects this biological plausibility. However, primary hereditary glaucoma often requires surgical intervention (e.g., goniotomy, trabeculotomy) as first-line treatment, and β-blockers typically serve adjunctive roles — a clinical nuance that must be addressed before any development decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for carteolol in primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for carteolol in primary hereditary glaucoma.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug interactions) were not retrievable in this evidence pack. Retrieval of the full prescribing information — particularly regarding β-blocker class contraindications (e.g., bronchospasm, bradycardia, heart block) and ophthalmic-specific warnings — is required before any clinical assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to model prediction and mechanistic reasoning (L4); no clinical trials or peer-reviewed literature specifically addressing carteolol in primary hereditary glaucoma were identified. Additionally, the drug is not currently marketed in the US, and all safety data fields are unresolved, preventing even a basic S1 safety screening.

**To proceed, the following is needed:**

- **Safety documentation**: Retrieve the full prescribing information (package insert) for carteolol to complete S1 safety screening — particularly β-blocker class contraindications, ophthalmic formulation warnings, and pediatric use data (critical for congenital glaucoma).
- **Formal MOA confirmation**: Obtain carteolol's DrugBank MOA record to confirm receptor selectivity profile and ISA classification.
- **Disease-specific literature search**: Expand PubMed search to include related terms (congenital glaucoma, JOAG, pediatric glaucoma) and β-blocker class evidence, rather than limiting to carteolol alone.
- **Clinical context assessment**: Determine the role of β-blockers in current standard-of-care guidelines for primary hereditary glaucoma (surgical vs. pharmacological management), especially for the pediatric population.
- **Formulation feasibility**: Confirm whether a suitable ophthalmic formulation can be developed or sourced, given the drug's withdrawn US market status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

