---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is the active progestin used in long-acting reversible contraceptive implants (e.g., Implanon/Nexplanon), acting via ovulation suppression and endometrial thinning to prevent pregnancy. The TxGNN model predicts it may also be applicable for therapeutic **Amenorrhea** (menstrual suppression), currently supported by **1 clinical trial** and **2 publications**, with relevance grading still pending final review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (long-acting progestin-only implant) — inferred from clinical trial evidence; no formal TFDA/US label text on file |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the drug record (flagged as a High-severity data gap, DG002). Based on available evidence, etonogestrel is a third-generation progestin (the active metabolite of desogestrel) used in long-acting reversible contraceptive implants. It binds with high affinity to the progesterone receptor, suppressing the hypothalamic-pituitary-gonadal axis to inhibit ovulation, thickening cervical mucus, and inducing endometrial atrophy.

Endometrial atrophy is the direct pharmacological driver of amenorrhea, and it is already a well-documented, common accompanying effect of etonogestrel implants in real-world contraceptive use — not an incidental association. The TxGNN prediction therefore reframes a known drug effect (amenorrhea as a side effect of contraception) as a potential intentional therapeutic target, i.e., using etonogestrel for medical menstrual suppression (e.g., in patients seeking reduced menstrual bleeding).

No dedicated trial in the evidence pack was designed with amenorrhea as its primary endpoint; the supporting Phase 3 trial (NCT04626596) is a contraceptive extended-use study where bleeding pattern/amenorrhea is only a secondary safety observation. This mechanistic plausibility is therefore currently stronger than the direct clinical evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Single-arm study assessing contraceptive efficacy/safety of the etonogestrel (ENG) implant during years 4–5 of use; not primarily designed to evaluate amenorrhea, but bleeding pattern (including amenorrhea rate) is a standard secondary safety endpoint for this implant class. Relevance graded **B** (indirect support). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomized comparison of single-rod (Implanon) vs. six-capsule (Norplant) implants in 200 women; no pregnancies over ~340/329 woman-years; bleeding pattern data relevant to amenorrhea rates with etonogestrel implants. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT (flagged as likely unrelated) | Trials | Study protocol for a COVID-19 pneumonia treatment trial (BIO101). Does not concern etonogestrel or amenorrhea — appears to be a PubMed search false positive; included here for transparency but should not be weighted as supporting evidence. |

---

## US Market Information

Etonogestrel currently has **no marketed license** on file for this jurisdiction (market status: Not Marketed; total licenses: 0). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently on file; TFDA label warnings/contraindications are flagged as a **Blocking** data gap — DG001 — that must be resolved before any Stage 1 safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between etonogestrel's known endometrial-atrophy effect and amenorrhea is strong and well-established as a drug side effect, and one completed Phase 3 trial plus one older RCT provide indirect supporting data. However, no trial has evaluated amenorrhea as a primary therapeutic endpoint, and critical safety data (TFDA warnings/contraindications) are missing.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (Blocking gap, DG001)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- A dedicated trial or systematic review evaluating etonogestrel specifically for therapeutic menstrual suppression/amenorrhea
- Completion of pending relevance and similarity-to-original-indication assessments noted in the evidence pack
- DDI data (current query returned no results)

*Note: Four additional lower-confidence predictions (breast fibrocystic disease, apocrine adenosis, blunt duct adenosis, benign mammary dysplasia) were also flagged by TxGNN but carry no clinical trial or literature support (Evidence Level L5) and are recommended for **Hold** pending further data.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

