---
layout: default
title: Uric Acid
parent: 僅模型預測 (L5)
nav_order: 1277
evidence_level: L5
indication_count: 4
---

# Uric Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Uric Acid: From No Approved Indication to Rheumatoid Arthritis

## One-Sentence Summary

Uric acid (DrugBank DB08844) currently has no approved therapeutic indication and is not marketed in the United States; it is more commonly studied as an endogenous purine metabolism biomarker than administered as a drug. TxGNN predicts a possible link to **Rheumatoid Arthritis**, but the **56 clinical trials and 20 publications** reviewed show only correlative biomarker associations — no study has actually tested uric acid administration as a treatment for RA. This is a weak, model-only signal that should not proceed without substantial additional evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication (drug not marketed) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 (mechanistic/observational studies only, no interventional evidence) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for uric acid as a therapeutic agent (Data Gap DG002). Uric acid is the terminal product of human purine metabolism, normally circulating as a metabolite/biomarker rather than being formulated and administered as a drug. It has no approved indication and no US marketing history, which makes any "original indication → new indication" mechanistic narrative inherently unavailable.

The literature retrieved for this candidate consistently frames serum uric acid as an **observational biomarker** in rheumatoid arthritis — correlated with disease activity, interstitial lung disease risk, cardiovascular risk, and oxidative stress (via its degradation product allantoin) — rather than as a therapeutic intervention. No clinical trial in the evidence pack administers uric acid to RA patients; the RA-labeled trials in this pack are almost all unrelated biologic/DMARD studies (tocilizumab, abatacept, sarilumab, rituximab) that co-occur with "uric acid" only as a background lab value, not as a study intervention. Several gout trials (febuxostat, pegloticase) even test **urate-lowering** therapy — the opposite pharmacological direction from "giving uric acid."

For context, the other three TxGNN candidates for this drug (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, bronchitis) are rated **L5** with no supporting evidence at all, or evidence contaminated by an unrelated concept (avian infectious bronchitis virus in poultry, not human bronchitis). This pattern suggests the model's predictions for DB08844 overall carry a high noise rate and should be treated cautiously.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01258712](https://clinicaltrials.gov/study/NCT01258712) | Phase 3 | Completed | 86 | Tocilizumab + methotrexate in RA — biologic trial unrelated to uric acid intervention (graded C: irrelevant) |
| [NCT00048568](https://clinicaltrials.gov/study/NCT00048568) | Phase 3 | Completed | 1250 | Abatacept + methotrexate vs methotrexate alone in RA — unrelated to uric acid (graded C) |
| [NCT02373202](https://clinicaltrials.gov/study/NCT02373202) | Phase 3 | Completed | 91 | Sarilumab in Japanese RA patients — unrelated to uric acid (graded C) |
| [NCT04953533](https://clinicaltrials.gov/study/NCT04953533) | N/A | Unknown | 800 | Investigates abnormal intestinal uric acid excretion and gut microbiota SNPs in **gout** pathogenesis — mechanistic, not an RA treatment study |
| [NCT01078389](https://clinicaltrials.gov/study/NCT01078389) | Phase 2 | Completed | 314 | Febuxostat (urate-**lowering** agent) vs placebo on joint damage in hyperuricemic gout — opposite pharmacological direction, not RA |
| [NCT06186219](https://clinicaltrials.gov/study/NCT06186219) | Phase 1 | Completed | 2 | Rituximab pretreatment + methotrexate-pegloticase (urate-lowering) for refractory tophaceous gout — not RA, not uric acid administration |
| [NCT00461448](https://clinicaltrials.gov/study/NCT00461448) | Phase 1 | Completed | 36 | Potassium supplementation pilot in RA focused on cortisol/glucocorticoid receptor regulation — no uric acid intervention arm |
| [NCT03856190](https://clinicaltrials.gov/study/NCT03856190) | N/A | Terminated | 53 | Therapeutic fasting and diet change in RA to explore symptom/mechanism effects — no uric acid intervention |

**Caveat**: None of the trials above test uric acid itself as a treatment for rheumatoid arthritis. Most were retrieved because they co-occur with "uric acid" as a background lab parameter or because gout (a hyperuricemia-related disease) shares keyword overlap with RA in the underlying corpus.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37627564](https://pubmed.ncbi.nlm.nih.gov/37627564/) | 2023 | Meta-Analysis | Antioxidants (Basel) | Systematic review/meta-analysis of circulating uric acid and allantoin as markers of pro-oxidant state and CV risk in RA — association, not causation |
| [40837562](https://pubmed.ncbi.nlm.nih.gov/40837562/) | 2025 | Cohort | Frontiers in Medicine | Serum uric acid evaluated as a predictive/prognostic biomarker for RA-associated interstitial lung disease |
| [35314903](https://pubmed.ncbi.nlm.nih.gov/35314903/) | 2022 | Cohort/Biomarker | Inflammation | Serum and BALF uric acid levels proposed as diagnostic biomarker for RA-associated interstitial lung disease severity |
| [21115462](https://pubmed.ncbi.nlm.nih.gov/21115462/) | 2011 | Review | Rheumatology (Oxford) | Reviews uric acid's association with cardiovascular risk in RA patients |
| [38026718](https://pubmed.ncbi.nlm.nih.gov/38026718/) | 2023 | Cross-sectional | Open Access Rheumatology | Examines whether serum uric acid level correlates with RA disease activity |
| [38699124](https://pubmed.ncbi.nlm.nih.gov/38699124/) | 2024 | Review | Cureus | Compares adenosine deaminase, CRP, and uric acid as inflammatory/oxidative biomarkers in RA vs non-arthritis patients |
| [37650291](https://pubmed.ncbi.nlm.nih.gov/37650291/) | 2024 | Cohort | Clinical and Experimental Rheumatology | Serum uric acid associated with all-cause and cardiovascular mortality in an RA cohort |
| [40047989](https://pubmed.ncbi.nlm.nih.gov/40047989/) | 2025 | Cross-sectional | Clinical Rheumatology | NHANES-based cross-sectional analysis of the association between RA and hyperuricemia |
| [39968300](https://pubmed.ncbi.nlm.nih.gov/39968300/) | 2025 | Review | Frontiers in Endocrinology | Reviews mechanisms linking serum urate to musculoskeletal disorders, including RA, sarcopenia, and osteoporosis |
| [40561486](https://pubmed.ncbi.nlm.nih.gov/40561486/) | 2025 | Observational | Terapevticheskii Arkhiv | Association of uric acid levels with skeletal muscle mass, strength, and physical performance in women with RA |

**Caveat**: Every publication above treats uric acid as an **endogenous biomarker/risk indicator**, not as an administered therapeutic agent. There is no clinical or preclinical evidence in this pack of uric acid being used to *treat* RA.

---

## US Market Information

Uric acid (DB08844) has no US marketing authorization on record — `total_licenses = 0`, and no license entries are available. It is currently not a marketed pharmaceutical product in the United States.

---

## Safety Considerations

No key warnings, contraindications, or drug-drug interaction data are currently available for uric acid (Data Gap DG001 — blocking; TFDA/FDA labeling has not been located). Please refer to primary regulatory sources once labeling becomes available, as safety information could not be assessed from current inputs.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis signal is supported only by observational biomarker studies (serum uric acid correlating with RA disease activity, ILD risk, and mortality) — there is no interventional evidence that administering uric acid treats RA, and the drug itself is unmarketed with no available mechanism-of-action or safety data. The three lower-ranked candidates (L5) further indicate this drug's TxGNN output carries substantial noise.

**To proceed, the following is needed:**
- Resolve blocking Data Gap DG001 (TFDA/FDA label, warnings, contraindications) before any S1 safety screening can begin
- Resolve Data Gap DG002 (mechanism of action) to establish a plausible pharmacological rationale
- Identify any interventional (not observational) study administering uric acid or a uric-acid-modulating strategy specifically in RA patients
- Clarify why a metabolite with no approved formulation is being evaluated as a "drug" candidate — confirm this is not a data/entity mapping error in the DrugBank source
- Re-run relevance triage on the "bronchitis" candidate evidence pipeline, which is contaminated by avian infectious bronchitis virus literature unrelated to human disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

