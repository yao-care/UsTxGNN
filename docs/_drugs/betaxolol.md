---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

The `txgnn-pipeline` skill covers pipeline operations and doesn't override the report generation format. I'll now generate the report according to the Evidence Pack v5 specification.

---

# Betaxolol: From Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a selective β1-adrenergic receptor antagonist that reduces intraocular pressure (IOP) by inhibiting aqueous humor production in the ciliary body, and has been used in the management of open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** (including juvenile open-angle glaucoma and primary congenital glaucoma), with a prediction score of **99.74%**.
However, **no clinical trials** and **no published literature** specifically supporting this indication were found — the prediction currently rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ocular hypertension / Open-angle glaucoma (derived from pharmacological class; no US NDA on record in this dataset) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 — Model prediction only, no clinical studies identified |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Betaxolol is a cardioselective β1-adrenergic receptor antagonist. In the eye, it acts on β receptors of the ciliary epithelium to inhibit cyclic AMP-mediated aqueous humor secretion, thereby lowering IOP. This is the same mechanism exploited by other topical beta-blockers (e.g., timolol, carteolol) in glaucoma management, and it is pharmacologically independent of the underlying cause of elevated IOP.

Primary hereditary glaucoma encompasses two major genetic subtypes: **juvenile open-angle glaucoma (JOAG)**, associated with *MYOC* and *OPTN* mutations, and **primary congenital glaucoma (PCG)**, linked to *CYP1B1* and *LTBP2* mutations. Although the root cause is a genetically determined abnormality in trabecular meshwork or anterior chamber angle development, **elevated IOP remains the dominant mechanism of optic nerve damage** in both subtypes. Betaxolol's ability to suppress aqueous production is therefore mechanistically applicable regardless of the genetic etiology — the drug does not need to correct the underlying gene defect to be clinically useful.

The TxGNN score of 0.997 is highly consistent with this mechanistic logic. That said, important caveats apply: PCG in neonates and infants is typically managed surgically (goniotomy, trabeculotomy) as first-line treatment, with pharmacotherapy serving only as a bridge; and JOAG, while more amenable to long-term medical management, lacks dedicated large-scale RCT evidence for betaxolol specifically. The prediction is therefore mechanistically compelling but clinically underdeveloped.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for betaxolol in primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for betaxolol in primary hereditary glaucoma.

---

## US Market Information

No US NDA licenses are on record for betaxolol in this dataset. The drug is not currently marketed in the US market according to the regulatory data available.

> **Note:** Betaxolol ophthalmic solution (brand: Betoptic®) was historically FDA-approved for open-angle glaucoma and ocular hypertension; oral betaxolol (Kerlone®) was approved for hypertension. These approvals are not reflected in the current Evidence Pack and should be verified against the FDA Orange Book for up-to-date status.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for betaxolol in primary hereditary glaucoma is sound — elevated IOP is the shared therapeutic target — but the evidence base is currently at L5 (model prediction only), with zero registered clinical trials and zero published studies specifically in this hereditary subtype. Without even observational or retrospective data, a "Go" or "Proceed with Guardrails" recommendation cannot be supported at this stage.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA):** Confirm β1 selectivity profile for ocular vs. systemic effects via DrugBank API query (remediation already identified in the Evidence Pack).
- **Package insert review:** Retrieve full US prescribing information (or historical Betoptic® labeling) to assess existing contraindications, ophthalmic-specific warnings, and age restrictions — critical given that PCG primarily affects neonates.
- **Retrospective chart review:** Identify whether JOAG patients on betaxolol have been included in any existing open-angle glaucoma registries or cohort studies.
- **Subtype stratification:** Separate the analysis for PCG (surgical-first, betaxolol likely adjunctive only) vs. JOAG (medical management viable; betaxolol may be a candidate for a prospective pilot study).
- **Pediatric pharmacokinetic/safety data:** If PCG is the target, systemic absorption from ophthalmic betaxolol in infants must be evaluated — β-blockers carry bradycardia and bronchospasm risk in neonates.
- **Comparator landscape:** Map current standard-of-care (prostaglandin analogues, carbonic anhydrase inhibitors) to define where betaxolol might add differentiated value in hereditary subtypes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

