---
layout: default
title: Elagolix
parent: 僅模型預測 (L5)
nav_order: 645
evidence_level: L5
indication_count: 1
---

# Elagolix
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

# Elagolix: From an Unrecorded Original Indication to Amenorrhea

## One-Sentence Summary

Elagolix is an oral GnRH receptor antagonist; the evidence pack does not record its original approved indication or product label, and it is currently not marketed under a Taiwan/US-tracked license (0 NDAs on file).
The TxGNN model predicts it may be effective for **Amenorrhea (disease)**, with a prediction score of **99.75%**, supported by **3 completed Phase 2 clinical trials** and **4 publications**.
Importantly, the underlying studies actually target *heavy menstrual bleeding (HMB) associated with uterine fibroids/endometriosis*, where drug-induced amenorrhea is a treatment response rather than the primary diagnosis — this mapping gap should be manually verified before advancing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal MOA documentation is not available in this evidence pack. However, the repurposing rationale field indicates that elagolix is an oral GnRH receptor antagonist that dose-dependently suppresses LH/FSH secretion, thereby lowering estradiol levels and suppressing endometrial proliferation and menstrual blood loss. At higher doses, this mechanism can induce therapeutic amenorrhea as an expected pharmacological effect when treating conditions like heavy menstrual bleeding from uterine fibroids — this is a treatment response, not a cure for a distinct amenorrhea disease entity.

All three supporting clinical trials and most of the literature actually studied elagolix for **HMB associated with uterine fibroids or endometriosis**, not primary/secondary amenorrhea as the target diagnosis. The TxGNN model's high score for the "amenorrhea (disease)" node likely reflects this indirect pharmacological connection (elagolix *causes* amenorrhea as a side effect/therapeutic endpoint) rather than a direct disease-treatment relationship. This is a meaningful mechanistic mapping gap: before proceeding, the disease node definition and clinical intent (is "amenorrhea" being treated, or induced as a marker of therapeutic response?) should be confirmed by manual review.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2a | Completed | 271 | Proof-of-concept study assessing elagolix vs. placebo to reduce uterine bleeding, fibroid volume, and uterine volume in premenopausal women with heavy uterine bleeding and fibroids. |
| [NCT00797225](https://clinicaltrials.gov/study/NCT00797225) | Phase 2 | Completed | 174 | Randomized, double-blind, placebo- and active-controlled (leuprorelin) study evaluating elagolix efficacy/safety in endometriosis over 3 months, with an additional 3-month extension. |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2b | Completed | 571 | Randomized, double-blind, placebo-controlled study of elagolix alone and with add-back therapy vs. placebo for heavy menstrual bleeding in premenopausal women with uterine fibroids. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37769311](https://pubmed.ncbi.nlm.nih.gov/37769311/) | 2023 | RCT | Obstetrics and Gynecology | Evaluated safety/efficacy of low-dose elagolix 150 mg once-daily monotherapy for heavy menstrual bleeding in uterine leiomyoma patients. |
| [31695514](https://pubmed.ncbi.nlm.nih.gov/31695514/) | 2019 | Review/Short Report | International Journal of Women's Health | Summarizes emerging efficacy data on oral elagolix for treatment of uterine fibroids, addressing bleeding, anaemia, pelvic discomfort, and fertility concerns. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstetrics and Gynecology | Overview of oral GnRH antagonists (incl. elagolix), co-administered with add-back steroid hormones, for management of uterine leiomyomas. |
| [32702363](https://pubmed.ncbi.nlm.nih.gov/32702363/) | 2021 | Cohort (predictors of response) | American Journal of Obstetrics and Gynecology | Identifies predictors of response to elagolix with add-back therapy for heavy menstrual bleeding associated with uterine fibroids. |

## US Market Information

No licenses or product registrations are on file for this drug (market status: not marketed, 0 total licenses).

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DDI query returned no results).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 2/2b RCTs (L2 evidence) demonstrate elagolix's GnRH-antagonist mechanism reliably induces a hypoestrogenic, amenorrhea-like state as part of treating HMB/uterine fibroids, supporting biological plausibility. However, the mismatch between the studied indication (HMB from fibroids/endometriosis) and the TxGNN-predicted node ("amenorrhea (disease)") — plus the absence of TFDA labeling and MOA documentation — means this cannot proceed without further verification.

**To proceed, the following is needed:**
- TFDA product label / warnings and contraindications (currently blocking; required for S1 safety evaluation)
- Confirmed formal mechanism-of-action documentation from DrugBank or manufacturer labeling
- Manual review of the "amenorrhea (disease)" node definition to clarify whether it represents a treatment target or a pharmacological side effect of elagolix
- Assessment of regulatory pathway, since the drug currently holds no Taiwan/US license on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

