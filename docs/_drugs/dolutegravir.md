---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 620
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

Using the evidence pack provided, here is the evaluation report. Note upfront: I did **not** invoke a coding/pipeline skill here since this is a direct content-generation task fully specified by your prompt template — I'm producing the report itself.

One important analytical flag before the report: the top two TxGNN-predicted indications for this candidate (**feline acquired immunodeficiency syndrome** and **simian immunodeficiency virus infection**) are **animal diseases, not human conditions**, and the third is explicitly marked in the evidence pack itself as a likely false positive. This materially changes the recommended decision, and I've stated that plainly rather than glossing over it.

---

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir is an HIV-1 integrase strand-transfer inhibitor, originally developed for treatment of HIV-1 infection in humans.
The TxGNN model's top-ranked prediction for this drug is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a retroviral disease of domestic cats, not a human condition —
supported by **5 clinical trials** (all human Phase 2/3 HIV-1 studies, not FIV-specific trials) and **1 publication** describing a small preclinical study in cats.
Because the predicted indication is veterinary rather than human, this candidate sits outside the standard human drug-repurposing evaluation pathway that the rest of this report's fields (TFDA/US licensing, human contraindications) are built around.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack's regulatory data (licenses list is empty). Dolutegravir is publicly documented as an antiretroviral used for HIV-1 infection; this is stated as background context, not sourced from the pack. |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (Feline Immunodeficiency Virus infection) — **a veterinary/animal indication** |
| TxGNN Prediction Score | 99.85% (raw score 0.9985, rank 4507) |
| Evidence Level | L4 for the new indication specifically (see rationale below); note the trial list would satisfy L1 by trial-count alone, but those trials studied the *original* human indication, not FIV |
| US Market Status | 未上市 (Not Marketed) — per this evidence pack's query results; 0 matching license records found |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa` is a recorded data gap, DG002). Based on generally established pharmacology, dolutegravir inhibits the HIV integrase enzyme, blocking strand transfer during retroviral DNA integration into the host genome — the mechanism underlying its approved use against HIV-1 infection.

Feline Immunodeficiency Virus (FIV) is a lentivirus in the same broad retrovirus family as HIV, and is frequently used in veterinary and comparative virology as an animal model of AIDS-like disease. This shared mechanistic class (integrase-dependent retroviral replication) is the biologically plausible basis for TxGNN linking dolutegravir to FIV, and is corroborated by one literature report (PMID 37112803) directly testing a dolutegravir-containing antiretroviral regimen in FIV-infected cats.

However, this mechanistic plausibility does not translate into a human drug-repurposing opportunity. The clinical trial evidence attached to this prediction consists entirely of human HIV-1 studies — i.e., evidence for the drug's *original* indication, not new evidence for treating a human disease. If this candidate is to be pursued at all, it would follow a veterinary drug-development and regulatory pathway (e.g., companion-animal antiviral approval), which is a fundamentally different track from the human TFDA/FDA repurposing framework this evaluation is otherwise structured around.

---

## Clinical Trial Evidence

*Note: the trials below studied dolutegravir in human HIV-1 infection (the drug's original indication). They are listed here because the evidence pack attaches them to the FIV prediction, but they should be read as supporting evidence for the parent compound's antiretroviral profile, not as direct feline-disease trials.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla in ART-naïve HIV-1 adults, 96-week non-inferiority study |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir 50mg QD vs. raltegravir 400mg BID + dual NRTI, ART-naïve HIV-1 adults |
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir vs. raltegravir in integrase-inhibitor-naïve, ART-experienced HIV-1 adults |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of dolutegravir with ABC/3TC or TDF/FTC in ART-naïve HIV-1 adults |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Single-arm safety/PK study of dolutegravir + ABC/3TC, including CNS/CSF drug penetration, in ART-naïve HIV-1 adults |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/animal study | Viruses | Evaluated a combination antiretroviral regimen (dolutegravir 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) in specific-pathogen-free, FIV-infected domestic cats, assessing pharmacokinetics and immunophenotype outcomes |

---

## US Market Information

Currently no marketed products or license records were found in this evidence pack for the United States market (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all recorded as data gaps in this evidence pack; TFDA label data is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top two TxGNN-ranked predictions for this drug — feline AIDS (this report's focus) and simian immunodeficiency virus infection (rank 2) — are both **animal, not human, diseases**, so neither constitutes an actionable human drug-repurposing candidate despite genuine mechanistic plausibility and one supporting animal study.
- The third-ranked prediction (a rare pediatric neurodevelopmental disorder) is explicitly flagged within the evidence pack's own rationale as lacking any mechanistic, trial, or literature support and is likely a knowledge-graph false positive.
- No clinically actionable new **human** indication has been identified for dolutegravir in this prediction run.

**To proceed, the following is needed:**
- Clarification on whether veterinary drug development (FIV in cats) is in scope for this evaluation program; if so, this would require a separate veterinary regulatory pathway rather than the human TFDA/FDA framework used elsewhere in this report
- TFDA/US package insert data — key warnings, contraindications, drug interactions (currently a Blocking data gap, DG001)
- Verified mechanism-of-action documentation from DrugBank (DG002)
- If the goal remains identifying a human repurposing candidate, re-running or re-filtering the TxGNN output to exclude non-human disease ontology nodes before the next evaluation cycle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

