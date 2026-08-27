---
layout: default
title: Hyaluronidase
parent: 僅模型預測 (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
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

# Hyaluronidase: From an Undocumented Original Indication to Esotropia

## One-Sentence Summary

Hyaluronidase (DB14740) is not currently marketed in the United States, and both its original approved indication and mechanism of action are undocumented in this evidence pack. The TxGNN model's top-ranked prediction is **Esotropia**, but the only supporting literature is a case report describing diplopia/strabismus as a complication of hyaluronidase-containing local anesthesia — not treatment evidence — so this is a **model-only signal with no clinical trial support**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no approved indication text available (US: not marketed, 0 licenses); MOA also undocumented |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for hyaluronidase is not available in this evidence pack (data gap DG002, High severity), and no original indication is on file (US market status: not marketed, 0 licenses). Without this baseline, no pharmacological rationale can be constructed connecting hyaluronidase to esotropia treatment.

More importantly, the single literature item supporting this prediction (PMID 16934027) is not therapeutic evidence at all — it is a case report of diplopia and strabismus occurring as a **complication of retrobulbar local anesthesia** in cataract surgery, where hyaluronidase was used as an anesthetic-diffusion adjuvant, not as a treatment for ocular misalignment. The model's own rationale flags this explicitly: the literature describes a potential adverse-event association, and the directionality runs opposite to a "treatment" claim. This prediction should be treated as a statistical artifact of the knowledge graph rather than a mechanistically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | Case report | Binocular Vision & Strabismus Quarterly | Reports diplopia/strabismus as a complication following retrobulbar local anesthesia (with hyaluronidase as diffusion adjuvant) in cataract surgery — an adverse-event association, not treatment evidence for esotropia |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all currently unavailable — data gap DG001, Blocking severity, meaning this candidate cannot yet pass an initial safety screen.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug-level foundation is missing (no MOA, no original indication, no US labeling/warnings — DG001 is Blocking), and the top-ranked predicted indication's only evidence is a case report describing an adverse reaction rather than a therapeutic effect. There is no clinical trial support and no plausible mechanistic link for esotropia.

**To proceed, the following is needed:**
- TFDA/FDA labeling data — warnings and contraindications (DG001, Blocking)
- Mechanism of action data via DrugBank API (DG002, High)
- Original indication documentation for hyaluronidase
- If pursuing this candidate further, reconsider which predicted indication to prioritize: within the same evidence pack, **diabetic retinopathy** (rank 6) has L1 evidence from two completed Phase 3 RCTs (though the ophthalmic-injection indication was ultimately not approved) and **severe nonproliferative diabetic retinopathy** (rank 3) has a supporting Phase 2 trial (L2) — both are mechanistically coherent (enzymatic vitreolysis) and substantially better evidenced than esotropia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

