---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 917
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a synthetic glucocorticoid used broadly as a systemic anti-inflammatory/immunosuppressive agent (no single original indication is recorded in this evidence pack). The TxGNN model predicts it may be effective for **Alopecia Areata**, and the search returned **18 clinical trials** and **20 publications** on this drug-disease pair — though on closer review only a small subset directly evaluates methylprednisolone in alopecia areata, with the rest being off-target hits (different drugs tested for systemic lupus erythematosus, an unrelated prostate cancer trial, etc.).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indications or license records are present in this evidence pack; methylprednisolone is a broadly used systemic glucocorticoid (anti-inflammatory/immunosuppressant) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the rationale captured alongside the prediction, methylprednisolone is a broad-spectrum glucocorticoid with immunosuppressive and anti-inflammatory activity, a pharmacological class whose effects are well established in autoimmune and inflammatory conditions generally.

Alopecia areata (AA) is a T-cell–mediated autoimmune attack on the hair follicle. Systemic glucocorticoids such as methylprednisolone suppress the perifollicular lymphocytic infiltrate that drives this attack, giving a direct mechanistic link between the drug's known immunosuppressive action and the disease process.

Importantly, this is not a novel hypothesis generated purely by the model — oral and intravenous "pulse" methylprednisolone is already an established, if second-line, option in dermatology practice for severe or treatment-resistant AA (including alopecia totalis/universalis). The TxGNN prediction here largely recovers an existing clinical practice rather than proposing an untested mechanism.

## Clinical Trial Evidence

The evidence-pack search returned 18 trials for this drug-disease pair, but most were graded low relevance (Grade C) because they tested a different drug (e.g., efavaleukin alfa, baricitinib, sirolimus, olaparib) for a different disease (systemic lupus erythematosus, prostate cancer) — likely knowledge-graph disease-linkage noise rather than genuine AA evidence. The trials below are the ones actually relevant to methylprednisolone (or a closely related corticosteroid regimen) in alopecia areata:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral "mega pulse" methylprednisolone tested in severe, therapy-resistant alopecia areata, using higher doses and more frequent pulses than standard regimens (Grade A — direct drug/indication match) |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (Observational) | Completed | 296 | Safety/effectiveness of tofacitinib in alopecia, with some participants receiving adjuvant prednisolone (corticosteroid-adjacent evidence) |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared intralesional steroid injection delivery methods (Dermojet vs. syringe) for alopecia areata |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Cyclosporine with and without systemic corticosteroids in alopecia areata treatment |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Efficacy and adverse effects of corticosteroid pulse therapy in alopecia areata |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Methylprednisolone alone vs. methylprednisolone + methotrexate in extensive alopecia areata; combination not clearly superior |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort/Case Series | Indian J Dermatol Venereol Leprol | IV methylprednisolone pulse therapy evaluated in severe alopecia areata |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Cohort | J Dermatological Treatment | Combination cyclosporine + methylprednisolone in severe alopecia areata |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Cohort | Open Access Maced J Med Sci | Methotrexate + mini-pulse methylprednisolone in severe AA (Vietnamese cohort) |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective Cohort | Indian J Dermatol | Sex differences in AA response to steroid pulse therapy |
| [36681881](https://pubmed.ncbi.nlm.nih.gov/36681881/) | 2023 | Cohort (patient-reported) | J Eur Acad Dermatol Venereol | Long-term patient-reported outcomes of methylprednisolone pulse ± methotrexate in AA |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777767/) | 1998 | Open Prospective Study | J Am Acad Dermatol | Pulse methylprednisolone in 45 patients with severe AA |
| [21592197](https://pubmed.ncbi.nlm.nih.gov/21592197/) | 2011 | Clinical Study | The Journal of Dermatology | Prognostic factors for response to methylprednisolone pulse therapy in AA (70 patients) |

## US Market Information

No marketing authorization records are present in this evidence pack (0 licenses), consistent with the recorded market status of "Not marketed." Regulatory/label data for this drug entity was not available at the time of this evaluation.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack (DG001 — TFDA label/warnings data is flagged as a **Blocking** gap for safety review).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 4 completed trial and multiple cohort studies/reviews support pulse methylprednisolone as an existing, clinically practiced option for severe/treatment-resistant alopecia areata — this is refinement of established practice rather than an unvalidated hypothesis. However, the absence of formal drug-label safety data and MOA detail (DG001, DG002) means safety-side evaluation cannot yet be completed.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Confirmation of licensing/marketing status, since 0 licenses are on file despite established off-label clinical use
- A monitoring plan for corticosteroid-specific risks (e.g., adrenal suppression, glucose/bone effects) given repeated pulse dosing regimens described in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

