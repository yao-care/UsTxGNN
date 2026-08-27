---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 893
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
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

Using the report template directly on the evidence pack — no code changes needed here, so I'll skip straight to authoring the report.

# Mefenamic Acid: From NSAID Analgesic/Anti-inflammatory Use to Rheumatoid Arthritis

## One-Sentence Summary

> Mefenamic acid is a fenamate-class NSAID that inhibits COX-1/COX-2 to reduce prostaglandin synthesis, giving it analgesic and anti-inflammatory activity; specific original-indication and label data for this drug are not on file in this evidence pack (drug is currently **not marketed in Taiwan**).
> The TxGNN model's top-ranked prediction is **Rheumatoid Arthritis**, supported by **20 PubMed publications** (including three double-blind RCTs from the 1970s) but **no currently registered clinical trials**.
> The literature indicates this is a re-affirmation of a historically established fenamate use in RA rather than a novel mechanistic hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug not marketed in Taiwan, no approved-indication records; generically known as an NSAID analgesic/anti-inflammatory agent |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record captured in this pack. Based on the information that is available, mefenamic acid is a fenamate-class NSAID that competitively inhibits COX-1/COX-2, reducing prostaglandin synthesis and producing analgesic, anti-inflammatory, and antipyretic effects — directly relevant to the inflammatory pathway driving joint damage in rheumatoid arthritis.

Notably, the literature evidence in this pack is not describing a novel repurposing hypothesis: mefenamic acid was studied head-to-head against other NSAIDs (ibuprofen, aspirin, phenylbutazone, sulindac, flurbiprofen) specifically in RA populations as early as 1966–1979. The TxGNN model's high score therefore reflects rediscovery of a well-established, classic fenamate indication rather than a mechanistically novel signal — useful for confidence, but it also means the supporting trials predate modern RA standard-of-care (DMARDs/biologics) and cannot speak to mefenamic acid's role relative to current treatment paradigms.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP both returned 0 results for mefenamic acid + rheumatoid arthritis).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | Double-blind crossover trial (n=24): mefenamic acid, flurbiprofen and sulindac all significantly superior to placebo on pain score, joint tenderness, and morning stiffness. |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | The Journal of International Medical Research | Randomized double-blind study (n=40): mefenamic acid and ibuprofen had comparable analgesic/anti-inflammatory effect; similar side-effect profile. |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | The Medical Journal of Australia | Double-blind crossover trial: mefenamic acid (1500 mg/day) compared favorably with ibuprofen (1200 mg/day); side effects mild, mostly GI. |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Cohort/Open-label | Annals of the Rheumatic Diseases | Early open-label/cohort study establishing mefenamic acid use in RA (no abstract on file). |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Review on the place of mefenamic acid in RA treatment (no abstract on file). |
| [20668](https://pubmed.ncbi.nlm.nih.gov/20668/) | 1977 | Review | Seminars in Arthritis and Rheumatism | General review of anti-inflammatory drugs including mefenamic acid (no abstract on file). |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Pending classification | British Medical Journal | Comparative study of mefenamic acid and flufenamic acid vs. aspirin and phenylbutazone in RA (no abstract on file). |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Pending classification | Annals of the Rheumatic Diseases | Evaluation-methods study for out-patient RA drug trials, comparing mefenamic/flufenamic acid with phenylbutazone and aspirin (no abstract on file). |
| [4890710](https://pubmed.ncbi.nlm.nih.gov/4890710/) | 1967 | Pending classification | Reumatismo | Double-blind clinical/biohumoral study of mefenamic acid in RA therapy (preliminary observations; no abstract on file). |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Pending classification | The Journal of Rheumatology | Single-blind non-crossover assessment of 10 antirheumatic drugs (incl. mefenamic acid) across 684 RA patients using daily pain charts. |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction queries all returned no data in this evidence pack — TFDA label data is flagged as a **Blocking** data gap (DG001) and must be resolved before any S1 safety review.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Mechanistic plausibility is strong and directly supported by multiple double-blind RCTs (1976–1979) comparing mefenamic acid to established NSAIDs specifically in RA populations, but all supporting evidence predates modern DMARD/biologic-based RA standard-of-care, and no active/recent trials exist to confirm continued relevance.

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications (DG001, Blocking — required before any safety review)
- DrugBank mechanism-of-action detail (DG002, High)
- Confirmation of current regulatory/market status and available dosage forms/routes, since the drug is presently unmarketed in Taiwan
- An updated literature or guideline check positioning mefenamic acid against current RA standard-of-care, given the evidence base is entirely pre-1980
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

