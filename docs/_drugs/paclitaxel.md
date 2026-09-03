---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 1007
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Established Chemotherapy Use to Predicted Female Breast Carcinoma

## One-Sentence Summary

> Paclitaxel is a taxane-class microtubule-stabilizing cytotoxic agent used broadly in oncology.
> The TxGNN model's top prediction for this drug is **Female Breast Carcinoma**, supported by **62 clinical trials**, but breast cancer is already a well-established, globally approved indication for paclitaxel — meaning this "prediction" largely reconfirms known clinical practice rather than identifying a genuinely novel repurposing opportunity.
> A more clinically distinct signal appears at rank 5 (**hormone-resistant breast carcinoma**), where a Phase 3 RCT directly supports sequencing paclitaxel after endocrine-therapy failure.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the source dataset (0 Taiwan/US regulatory licenses on file — see Data Gap DG001/DG002). Paclitaxel is a globally established taxane chemotherapy already indicated for ovarian, breast, and non-small cell lung cancer, and Kaposi sarcoma. |
| Predicted New Indication | Female Breast Carcinoma *(⚠ already a standard approved use — see caveat below)* |
| TxGNN Prediction Score | 99.99% (rank 250 of all candidates) |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per dataset; 0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold — Not a Novel Repurposing Candidate** (see rationale below) |

**⚠ Key Caveat:** The evidence pack's own mechanistic annotation for this candidate states explicitly: *"This is not a novel repurposing candidate but an existing standard-of-care use; the KG prediction merely reproduces a known fact."* This is reflected in the recommendation above, which diverges from the raw scoring-engine output ("Proceed with Guardrails") because that score reflects treatment efficacy evidence, not repurposing novelty.

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data (DrugBank MOA field) was not available in this evidence pack (Data Gap DG002, High severity). Based on the pharmacological literature and the model's own annotations, paclitaxel is a taxane that binds and stabilizes microtubules, preventing spindle depolymerization and thereby blocking mitosis in rapidly proliferating cells — a classic broad-spectrum cytotoxic mechanism.

Breast cancer is one of the core, long-established indications for paclitaxel worldwide (used across neoadjuvant, adjuvant, and metastatic settings, often combined with anthracyclines, platinum agents, or HER2-targeted therapy). Because of this, the mechanistic link between paclitaxel and breast carcinoma is not merely "plausible" — it is already clinically validated and guideline-endorsed. The high TxGNN score for this pairing most likely reflects the density of existing drug–disease co-occurrence in the knowledge graph rather than a novel biological hypothesis.

The more informative signal in this evidence pack is the **breast cancer subtype/context stratification** the model surfaces — particularly rank 5, "hormone-resistant breast carcinoma." Here paclitaxel's non-hormone-dependent, direct cytotoxic mechanism offers a genuine rationale for treatment-sequencing after endocrine-therapy failure, which is a more clinically actionable framing than the generic "breast carcinoma" prediction.

---

## Clinical Trial Evidence

*(Evidence for the top-ranked prediction: Female Breast Carcinoma)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00016406](https://clinicaltrials.gov/study/NCT00016406) | Phase 3 | Completed | 399 | AC → weekly paclitaxel ± filgrastim in inflammatory/locally advanced breast cancer; direct comparator RCT (Grade A) |
| [NCT00014222](https://clinicaltrials.gov/study/NCT00014222) | Phase 3 | Completed | 2,104 | Large adjuvant trial comparing EC+filgrastim+epoetin→paclitaxel vs. AC→paclitaxel vs. CEF in node-positive/high-risk breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel + carboplatin + trastuzumab in HER2-overexpressing metastatic breast cancer (Grade B) |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Nab-paclitaxel + carboplatin vs. nab-paclitaxel + capecitabine in advanced triple-negative breast cancer |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Paclitaxel-trastuzumab adjuvant therapy for stage II/IIIA HER2-overexpressing breast cancer |
| [NCT01705691](https://clinicaltrials.gov/study/NCT01705691) | Phase 2 | Completed | 50 | Weekly paclitaxel vs. eribulin → AC as neoadjuvant therapy, HER2-negative breast cancer (NSABP FB-9) |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly paclitaxel + trastuzumab in metastatic breast cancer |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Carboplatin+docetaxel or carboplatin+paclitaxel → AC in stage I-III triple-negative breast cancer |
| [NCT04440930](https://clinicaltrials.gov/study/NCT04440930) | NA | Completed | 88 | White tea mouthwash for prevention of paclitaxel-induced oral mucositis (supportive care, not efficacy; Grade C) |
| [NCT00589238](https://clinicaltrials.gov/study/NCT00589238) | Phase 2 | Terminated | 16 | Neoadjuvant weekly paclitaxel+carboplatin vs. paclitaxel alone → AC in basal-like breast cancer |

## Literature Evidence

Currently no related literature available for this specific candidate (female breast carcinoma) in the evidence pack — all citation evidence for this prediction was clinical-trial based.

*(Note: a Tier-1 RCT does exist for the related, more clinically distinct candidate "hormone-resistant breast carcinoma" — [PMID 20462978](https://pubmed.ncbi.nlm.nih.gov/20462978/), SELECT BC trial, taxane vs. TS-1 in metastatic/recurrent hormone-resistant breast cancer — see Conclusion for follow-up recommendation.)*

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class); this section is included per antineoplastic-drug criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is a well-recognized dose-limiting toxicity; several trials in this dataset paired paclitaxel with growth-factor support (e.g., filgrastim in NCT00016406, NCT00014222) |
| Emetogenicity Classification | Low to Moderate (standard oncology classification for IV paclitaxel) |
| Monitoring Items | CBC with differential, liver and renal function, infusion-related hypersensitivity reactions, peripheral neuropathy assessment |
| Handling Protection | Requires standard hazardous/cytotoxic drug handling precautions (closed-system transfer devices, PPE per institutional cytotoxic handling policy) |

*Please refer to the package insert warnings and precautions for the definitive, product-specific toxicity profile — formal TFDA label data was not available in this dataset (Data Gap DG001, Blocking severity).*

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DG001: TFDA warnings/contraindications — Blocking; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold — Not a Novel Repurposing Candidate**

**Rationale:**
- The top TxGNN prediction (female breast carcinoma) is already a long-established, globally approved indication for paclitaxel; the evidence pack's own mechanistic annotation confirms this is a reproduction of known clinical fact rather than a new therapeutic hypothesis. Advancing this as a "repurposing candidate" would be evaluatively misleading despite the strong (L1) trial evidence base.
- A more genuinely distinct and clinically actionable signal exists at rank 5, "hormone-resistant breast carcinoma" (L2 evidence, including a Tier-1 RCT, PMID 20462978), which reflects a specific treatment-sequencing rationale (chemotherapy after endocrine-therapy failure) rather than a duplicate of the base indication.
- Two other predictions (Ehrlich tumor, rank 3; nipple carcinoma, rank 8) are supported only by animal-model or case-report-level evidence, and two (parameningeal/vaginal embryonal rhabdomyosarcoma, ranks 9–10) have zero clinical trial or literature support — none of these should proceed without substantial additional evidence.

**To proceed, the following is needed:**
- Confirm paclitaxel's actual approved indications (TFDA/FDA label) to properly benchmark novelty of any candidate against current standard of care
- Obtain formal DrugBank/regulatory MOA documentation (Data Gap DG002)
- Obtain TFDA package insert warnings, contraindications, and DDI data (Data Gap DG001, Blocking — required before any S1 safety review)
- If pursuing a genuinely differentiated research question, reframe evaluation around the "hormone-resistant breast carcinoma" subgroup (rank 5) rather than generic "breast carcinoma"
- Disregard the parameningeal/vaginal rhabdomyosarcoma and Ehrlich tumor candidates pending any real-world clinical or preclinical corroboration beyond the KG similarity score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

