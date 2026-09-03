---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 1232
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Tipranavir is a non-peptidic protease inhibitor used in antiretroviral therapy for HIV-1 infection.
> The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
> with a very high prediction score but **no clinical trials or published literature** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (pharmacological classification; TFDA-approved indication text not available in this evidence pack) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological classification, tipranavir belongs to the HIV protease inhibitor class, and its efficacy in HIV-1 infection is well established in treatment-experienced patients.

Simian Immunodeficiency Virus (SIV) is a lentivirus closely related to HIV-1, sharing significant structural homology in its viral protease enzyme. This phylogenetic and structural similarity is the most plausible mechanistic basis for the TxGNN model linking a human HIV protease inhibitor to an SIV indication — the knowledge graph likely captured shared "lentivirus / protease inhibitor" relationships rather than any direct clinical evidence.

However, it is important to note that SIV infection is a veterinary/primate model disease, not a human clinical indication. Even if mechanistically plausible, there is currently zero clinical trial or literature evidence directly supporting this specific prediction, and no established regulatory pathway exists for repurposing a human antiretroviral into this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications are currently a Blocking data gap (DG001) — this evidence pack cannot support a full safety (S1) assessment until this data is obtained.*

---

## Additional Context: Other Candidate Indications

Beyond the top-ranked prediction, this evidence pack includes 9 additional candidate indications for tipranavir. Most were internally flagged as likely false positives (evidence level L5, decision stage S0, recommendation Hold) due to lack of biological plausibility with protease-inhibitor pharmacology — e.g., fibroma of prostate, Brenner tumor, and a rare neurodevelopmental disorder, none of which have any supporting evidence.

One candidate worth noting separately is **rank 5, "congenital human immunodeficiency virus"** (score 99.83%), which is linked to 9 Phase 2/3 clinical trials on HIV-1 antiretroviral regimens. However, these trials concern general adult HIV-1 virologic suppression, not specifically congenital/perinatal transmission, and their relevance grading is still marked "pending" — this candidate may warrant follow-up evidence review before the top-ranked SIV prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) has no clinical trial or literature support and targets a non-human disease model with no clear human repurposing pathway. Combined with a Blocking data gap on TFDA safety labeling and the drug's current non-marketed status in this jurisdiction, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action (MOA) detail from DrugBank (DG002)
- Clarification of clinical relevance/translatability of the SIV-infection signal to any human indication
- Relevance grading and follow-up evidence review for the "congenital HIV" candidate (rank 5), which has the strongest existing trial base among all listed candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

