---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 1129
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor, originally developed and widely used (often as a pharmacokinetic booster) in combination antiretroviral therapy for human HIV-1 infection. The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV-associated feline AIDS)**, a veterinary retroviral disease, but this prediction is currently supported by only **1 clinical trial** (which does not actually study the predicted disease) and **no dedicated literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (not explicitly recorded in this evidence pack's regulatory data; inferred from known pharmacology and supporting trial context, e.g. "naïve HIV-1 infected subjects", "Lopinavir/Ritonavir") |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only — the one associated trial studies human HIV-1 therapy, not feline AIDS) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (DG002, DrugBank MOA lookup pending). Based on known pharmacology, Ritonavir is an HIV-1 aspartic protease inhibitor, historically used both as a direct antiretroviral agent and — more commonly today — as a low-dose CYP3A4 inhibitor that "boosts" plasma levels of other protease inhibitors (e.g., darunavir, lopinavir) in combination antiretroviral therapy for HIV-1 infection.

The predicted new indication, feline AIDS, is caused by Feline Immunodeficiency Virus (FIV), a lentivirus that is taxonomically related to HIV and also encodes a retroviral aspartic protease essential for viral maturation. This shared protease-dependent replication strategy is the most plausible basis for TxGNN linking ritonavir to FIV disease in its knowledge graph — both diseases sit near "retroviral infection / protease inhibitor" concept clusters. Supporting this cross-species analogy (though not the primary predicted indication in this pack), literature on the related "simian immunodeficiency virus infection" prediction shows ritonavir has measurable in vitro inhibitory activity against SIV protease (PMID 12709355) and has been used in combination regimens in SIV-infected macaque models (PMID 12951220).

However, this mechanistic link should be treated cautiously: HIV-1 protease inhibitors are known to differ substantially in efficacy against non-HIV lentivirus proteases due to structural divergence in the protease active site, and species-specific pharmacokinetics in cats have not been characterized here. The predicted indication is therefore biologically plausible but clinically unverified, and represents a veterinary rather than human repurposing opportunity — a distinction that should be explicitly clarified before any further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared ritonavir-boosted darunavir + lamivudine vs. boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in ARV-naïve **human** HIV-1 patients. **Note: this trial studies ritonavir's established role in human HIV-1 therapy and does not investigate feline AIDS; it is indirect supporting evidence only.** |

---

## Literature Evidence

Currently no related literature available for the predicted indication (Feline Acquired Immunodeficiency Syndrome).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A Blocking data gap (DG001) exists — TFDA label warnings and contraindications for ritonavir have not yet been retrieved. This must be resolved before any S1 safety pre-assessment can proceed. Drug interaction data (DDI query) also returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is a veterinary disease (feline AIDS) rather than a human indication, and its only associated clinical trial actually studies ritonavir's established human HIV-1 use rather than the predicted disease itself — meaning there is no direct clinical or literature evidence for this specific repurposing hypothesis. Combined with a Blocking safety data gap (missing TFDA warnings/contraindications), the evidence base is currently insufficient to advance.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001 — Blocking; required before any safety pre-assessment)
- Confirmed mechanism of action via DrugBank API (DG002)
- Direct in vitro or in vivo evidence of ritonavir activity against FIV protease specifically (not HIV/SIV analogy alone)
- Clarification of intended use case — human vs. veterinary application — since feline AIDS is not a human indication and may fall outside this program's scope
- If pursuing the human-relevant analog (SIV/HIV-related indications from rank 2), reclassify and re-evaluate using that evidence set instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

