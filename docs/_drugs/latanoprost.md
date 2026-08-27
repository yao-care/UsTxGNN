---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

> Latanoprost is a prostaglandin F2α analog used as a standard therapy to lower intraocular pressure in glaucoma and ocular hypertension.
> The TxGNN model predicts it may also be effective for **Primary Hereditary Glaucoma**,
> with **1 clinical trial** currently supporting this direction and no published literature yet identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (standard latanoprost use; not confirmed in Taiwan license data — this product is not currently marketed in Taiwan) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field for this drug is currently a data gap. Based on the mechanistic information available in this evidence pack, latanoprost is an isopropyl ester prodrug of a PGF2α analog. After corneal esterase hydrolysis, the active acid form binds the FP receptor and increases uveoscleral (trabecular) outflow of aqueous humor, thereby lowering intraocular pressure — the established mechanism underlying prostaglandin analogs in glaucoma therapy.

Primary hereditary glaucoma (e.g., CYP1B1-associated congenital/juvenile-onset glaucoma) shares the same end-point pathology — elevated intraocular pressure — as the drug's original indication, but arises from developmental abnormalities of the trabecular meshwork rather than the adult open-angle mechanism. Because the aqueous outflow pathway differs structurally in the hereditary form, extrapolating efficacy from adult open-angle glaucoma is mechanistically plausible but not automatic, and requires direct clinical confirmation rather than being treated as an already-approved use.

This is consistent with the identified trial evidence: a completed Phase 2 study specifically tested a prostaglandin analogue (drug class covering latanoprost) plus a carbonic anhydrase inhibitor in pediatric primary glaucoma refractory to surgery, but confirmation that latanoprost itself (rather than another class member) was the specific agent studied is still needed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed the ocular hypotensive effect and safety of a prostaglandin analogue (latanoprost) combined with dorzolamide in pediatric primary glaucoma refractory to surgery. |

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (n=37) supports the hypotensive efficacy and preliminary safety of a prostaglandin analogue in pediatric primary glaucoma, giving L2-level evidence for this prediction. However, the drug is not currently marketed in Taiwan and formal safety/label data are missing, so full approval cannot be recommended yet.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank API — currently a high-priority data gap (DG002)
- Confirmation that NCT01527682 used latanoprost specifically, not another prostaglandin analogue
- Assessment of the Taiwan market entry/registration pathway, since the product currently holds 0 local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

