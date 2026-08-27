---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 760
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Goserelin: From Hormone-Responsive Breast Cancer to Amenorrhea

## One-Sentence Summary

Goserelin is a GnRH (LHRH) agonist whose established clinical use — per the trial evidence in this pack — is in hormone-responsive breast cancer (ovarian suppression/protection during chemotherapy) and endometriosis-related pelvic pain. The TxGNN model predicts it may be effective for **Amenorrhea**, which is mechanistically consistent with its known pharmacology (pituitary desensitization → suppressed FSH/LH → induced reversible amenorrhea), and is supported by **7 clinical trials** (3 completed Phase 3 RCTs) and **19 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no Taiwan license data); trial context indicates hormone-responsive breast cancer / endometriosis |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Market Status (Taiwan) | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for Goserelin is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the mechanistic rationale attached to this prediction, however, Goserelin is a GnRH agonist: continuous administration causes pituitary desensitization, suppressing FSH/LH secretion, which in turn suppresses ovarian steroidogenesis and ovulation and directly induces reversible amenorrhea. This is an established pharmacological mechanism, not a speculative link — it is the same mechanism already exploited clinically to protect ovarian function during chemotherapy and to induce therapeutic amenorrhea in endometriosis/fibroid management.

Importantly, "amenorrhea" in this context is largely a **therapeutic/protective goal** (preventing chemotherapy-induced ovarian failure) rather than amenorrhea being treated as a disease endpoint in itself. This distinction matters for how the indication should be framed clinically and regulatorily — it is closer to a label-consistent extension of known use than a mechanistically novel repurposing.

Given the drug's demonstrated ability to induce ovarian suppression is already well documented across multiple large Phase 3 oncology trials, the TxGNN prediction is well grounded rather than a purely algorithmic artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | RCT evaluating goserelin for ovarian function preservation during chemotherapy in premenopausal breast cancer |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH analog during chemotherapy to reduce ovarian failure in early-stage, hormone-receptor-negative breast cancer |
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial — goserelin for prevention of early menopause during chemotherapy in stage I–III premenopausal breast cancer |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection with cyclophosphamide-containing chemotherapy; menstruation outcome endpoint |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Aromatase inhibitors vs. GnRH agonists for uterine adenomyosis management |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in HR-positive breast cancer with/without chemotherapy-induced amenorrhea |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | NA | Unknown | N/A | Single-arm study of Zoladex 3.6mg + CEF as neoadjuvant therapy in hormone-responsive premenopausal breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII — QOL and amenorrhea/hot flashes with chemo vs. goserelin vs. sequential combination |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study — goserelin vs. CMF chemotherapy as adjuvant therapy in node-positive premenopausal breast cancer |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | RCT | Ann Oncol | OPTION trial — GnRH agonist during chemotherapy protects against ovarian toxicity/premature ovarian insufficiency |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | Adjuvant chemotherapy followed by goserelin vs. either modality alone in node-negative premenopausal breast cancer |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs. low-dose oral contraceptive for endometriosis-associated pelvic pain |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Ovarian ablation with goserelin improves survival in stage II/III HR-positive breast cancer without chemo-induced amenorrhea |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort/Observational | J Clin Oncol | Discussion of estradiol monitoring necessity during ovarian suppression for breast cancer |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Review of methods to induce amenorrhea, including the GnRH analogue goserelin |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Review of ovarian ablation methods in adjuvant treatment of premenopausal/perimenopausal breast cancer |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists in early breast cancer — benefits of reversible ovarian ablation |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence Level L1 is met — three completed Phase 3 RCTs (NCT02483767, NCT00068601, NCT00427245) plus corroborating RCT-level literature (IBCSG Trial VIII, ZEBRA, OPTION) directly support goserelin-induced ovarian suppression/amenorrhea in a well-characterized clinical population. However, the drug is currently not marketed in Taiwan (0 licenses), and drug-level safety documentation (warnings, contraindications, DDI) is entirely a data gap.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — flagged as a **Blocking** gap (DG001); required before any S1 safety screening
- Formal DrugBank/MOA documentation to replace the inferred mechanistic rationale (DG002)
- Confirmation of original approved indication(s), since no Taiwan license records exist for this drug
- Clarification of intended clinical positioning — protective/therapeutic amenorrhea induction (e.g., during chemotherapy) vs. amenorrhea as a standalone treatment target
- DDI data (currently `not_found`) before combination-therapy use cases are considered

*Note: Two additional TxGNN-predicted candidates for this drug (renal hypoplasia, renal hypoplasia bilateral) were also screened but scored Evidence Level L5 with no supporting trials or literature and no plausible mechanistic link — both are recommended **Hold** and are not carried forward in this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

