---
layout: default
title: Phenol
parent: 僅模型預測 (L5)
nav_order: 1038
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Using the drug-repurposing report skill implicitly follows the fixed template requested; producing the report now.

# Phenol: From No Approved Indication to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

> Phenol (DrugBank DB03255) has no approved indication or original mechanism-of-action data on file — it is not currently marketed as a drug product in this jurisdiction.
> The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**, a Borrelia-associated chronic skin atrophy condition,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure algorithmic (model-only) prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorization or approved indication on file for phenol |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for phenol is not currently available in this evidence pack, and no original approved indication is on file — DrugBank lists it only as a small molecule/reagent. What is generally known about phenol pharmacologically is its use as a topical keratolytic, antiseptic, and local anesthetic/caustic agent (e.g., in chemical peels and destructive procedures), but none of this is formally documented here as an "original indication."

Based on the model's own rationale, no plausible mechanistic bridge could be identified between phenol's known local pharmacological actions and the pathophysiology of acrodermatitis chronica atrophicans, which is a chronic Borrelia-infection-associated dermal atrophy disorder involving systemic infectious and immunologic processes — not a condition phenol's topical keratolytic/antiseptic properties would be expected to address. The high TxGNN score (99.95%) reflects graph-embedding similarity in the knowledge graph rather than any established or hypothesized clinical/biological mechanism, and is not corroborated by any clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorizations were found for phenol in this jurisdiction — the compound is currently **not marketed** (0 licenses on record). No product name, dosage form, or approved-indication data is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all marked as data gaps — notably, TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) that prevents even an initial safety assessment (S1) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN algorithmic score is high, but this specific prediction (acrodermatitis chronica atrophicans) has zero clinical trials, zero literature support, and no identifiable mechanistic rationale — it is evidence level L5, model-prediction-only. Combined with the absence of any original indication, MOA, or safety/label data for phenol, there is currently no basis to advance this candidate beyond initial screening.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Mechanism-of-action characterization via DrugBank or other pharmacology sources (DG002)
- A targeted literature/trial search specifically for "phenol" + "acrodermatitis chronica atrophicans" (none of the reviewed data sources returned matches)
- Consideration of re-scoping this evaluation toward a mechanistically more plausible candidate from the same prediction set — e.g., rank 5 "acne keloid" (L4 evidence, Research Question stage), which is grounded in phenol's documented use as a chemical peeling agent in dermatology, unlike the top-ranked candidate assessed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

