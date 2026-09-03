---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 1078
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

> Prednisone is a systemic corticosteroid with broad anti-inflammatory and immunosuppressive activity, and has long been used off-label in dermatology for autoimmune hair-loss conditions.
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **1 directly relevant completed Phase 3 trial** and **21 supporting publications** currently identified in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved regulatory indication text was provided in this evidence pack |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacology, prednisone is a systemic glucocorticoid whose anti-inflammatory and immunosuppressive effects are well characterized in clinical practice.

Alopecia areata is a T-cell–mediated autoimmune disease in which lymphocytes attack the hair follicle. Prednisone's immunosuppressive/anti-inflammatory mechanism can directly dampen this pathological process. Importantly, this is not a novel hypothesis — systemic corticosteroids, including prednisone (alone or combined with methotrexate), are already used off-label in dermatology practice for severe alopecia areata, which strengthens the biological plausibility of the TxGNN prediction.

It should be noted that this evidence pack also contains a large number of clinical trials on systemic lupus erythematosus (SLE) testing unrelated investigational drugs (e.g., rozibafusp alfa, voclosporin, ustekinumab). These trials do not test prednisone and are not specific to alopecia areata; they were treated as indirect/low-relevance evidence (grade "C" or "pending" in the source data) and were excluded from the tables below to avoid overstating the evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | Randomized double-blind multicenter trial testing methotrexate alone vs. methotrexate + low-dose prednisone vs. placebo in patients with severe alopecia areata (grave pelade); assessed safety and efficacy of adding low-dose prednisone to methotrexate. |

*Note: Numerous additional trials in the source dataset (mostly Phase 2/3/4 SLE trials testing other biologics) were excluded here because they neither test prednisone nor target alopecia areata directly; they only provide indirect disease-mechanism support.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 2-step double-blind RCT: methotrexate alone vs. methotrexate + low-dose prednisone in alopecia totalis/universalis, the most severe AA subtypes. |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Cohort | Archives of Dermatology | Immunologic studies of alopecia areata and treatment outcomes with prednisone. |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Real-world/Cohort | Italian J Dermatology and Venereology | Real-world characterization of hospitalized AA patients in Italy, including treatment patterns. |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort/Comparative | Dermatology (Basel) | Efficacy and safety of methotrexate combined with low- to moderate-dose corticosteroids for severe AA. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Follow-up Cohort | Archives of Dermatology | Long-term follow-up of 18 patients treated with alternate-day prednisone for AA; documents efficacy and steroid-related adverse effects. |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Cohort | International Journal of Dermatology | Severe alopecia areata treated with systemic corticosteroids; demonstrates efficacy in difficult-to-treat disease. |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Cohort | Annales de Dermatologie et de Venereologie | Evaluation of efficacy and safety of once-monthly oral pulsed prednisone for AA. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Cohort | Medical Times | Early treatment series of AA (partialis and totalis) with cortisone, hydrocortisone, prednisone, and prednisolone. |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Cohort | Journal of the American Academy of Dermatology | Clinical and immunopathologic evaluation of systemic cyclosporine plus low-dose prednisone in chronic severe AA. |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Archives of Dermatology | Review of AA therapies including corticosteroids, summarizing efficacy, safety, and mechanism across studies. |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a Blocking-severity data gap, DG001 — TFDA label warnings/contraindications).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT (NCT02037191) directly tests prednisone (combined with methotrexate) in severe alopecia areata, supported by multiple cohort studies and a long clinical-practice history of off-label corticosteroid use for this indication — meeting L2 evidence criteria. However, key safety data (label warnings, contraindications, DDI) and formal MOA documentation are missing, so guardrails are needed before advancing.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (DG001 — Blocking)
- Documented mechanism of action from DrugBank or equivalent source (DG002 — High)
- Confirmation of original approved indication(s) and current market/license status
- Safety monitoring plan specific to long-term/pulsed corticosteroid use in dermatology populations (e.g., bone density, glucose, adrenal suppression)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

