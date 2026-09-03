---
layout: default
title: Racepinephrine
parent: 僅模型預測 (L5)
nav_order: 1104
evidence_level: L5
indication_count: 7
---

# Racepinephrine
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

# Racepinephrine: From Vasoconstrictor/Adrenergic Therapy to Primary Hereditary Glaucoma

## One-Sentence Summary

> Racepinephrine (DB11124) is the racemic form of epinephrine, an adrenergic agonist historically used for its vasoconstrictive and bronchodilatory properties (e.g., nebulized therapy for croup, topical hemostasis); it is **not currently marketed in Taiwan**, so no official Taiwan-approved indication is on file.
> The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
> with **0 clinical trials** and **0 publications** currently directly supporting this specific drug-disease pair — the signal rests entirely on adrenergic mechanism reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Taiwan (0 licenses on file). Internationally, racemic epinephrine is used as an inhaled agent for croup/post-extubation stridor and as a topical vasoconstrictor/hemostatic. |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 (mechanism-based, no direct clinical trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for racepinephrine is not available (DrugBank MOA field is a confirmed data gap). Based on known pharmacology, racepinephrine is the racemic mixture of epinephrine enantiomers and acts as a non-selective α/β adrenergic receptor agonist — the same pharmacological class as epinephrine itself.

Adrenergic agonists have a well-established, if largely historical, mechanistic link to intraocular pressure (IOP) control: α-receptor activation reduces aqueous humor production, while β-receptor activation promotes uveoscleral outflow. Topical epinephrine and its prodrug dipivefrin were once used clinically for open-angle glaucoma before being largely superseded by prostaglandin analogs and β-blockers. The TxGNN model's top prediction — **primary hereditary glaucoma**, a rare genetic subtype of glaucoma — plausibly draws on this class-level mechanism. Notably, the model also ranked the related, more common phenotype **open-angle glaucoma** at rank 3 (score 99.56%) with an identical mechanistic rationale, reinforcing that the signal is being driven by the adrenergic-IOP pathway rather than a target unique to the hereditary subtype.

However, primary hereditary glaucoma involves distinct genetic and pathophysiological features (e.g., trabecular meshwork developmental abnormalities) that are not fully equivalent to the acquired/idiopathic open-angle glaucoma population in which adrenergic agents were historically studied. This is therefore a class-level mechanistic extrapolation rather than a disease-specific hypothesis, and no clinical or literature evidence currently exists for racepinephrine in either glaucoma phenotype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: rank-3 prediction "open-angle glaucoma" returned 6 clinical trials in the evidence pack, but all were graded "C" relevance — testing unrelated interventions such as suprachoroidal triamcinolone, bevacizumab, and glaucoma drainage devices, none involving racepinephrine or epinephrine-class agents. These do not constitute supporting evidence for this drug.)*

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Racepinephrine has no marketing authorization records in the Taiwan regulatory dataset (`market_status: 未上市`, 0 total licenses). No license table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in the evidence pack — flagged as **Blocking** data gap DG001, since TFDA label warnings/contraindications have not yet been retrieved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (primary hereditary glaucoma) is supported only by class-level adrenergic mechanism reasoning (L4), with zero clinical trials or literature directly evaluating racepinephrine in any glaucoma population. Combined with a **Blocking** safety data gap (no TFDA label, warnings, or contraindications available) and the fact that the drug is not currently marketed in Taiwan, there is insufficient evidence to advance past a research-question stage.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA (or equivalent regulatory) package insert for warnings/contraindications (resolves DG001, currently blocking S1 safety screening)
- Confirm mechanism of action via DrugBank API (resolves DG002)
- Identify any epinephrine/adrenergic-class precedent literature or trials in open-angle or hereditary glaucoma to establish at least indirect class evidence
- Assess route compatibility — ophthalmic/topical delivery data for racepinephrine is not yet characterized (`route_compatibility.status: pending`)
- Given the drug's adrenergic profile, prioritize cardiovascular safety review (arrhythmia, hypertension risk) before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

