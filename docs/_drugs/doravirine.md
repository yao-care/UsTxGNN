---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 622
evidence_level: L5
indication_count: 3
monitor_inn: "DORAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-14
description: "Doravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS"
---

# Doravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Doravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, doravirine is an NNRTI that acts on HIV-1 reverse transcriptase, and its efficacy in HIV infection and AIDS is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV. The high TxGNN score likely reflects network proximity to the approved HIV/AIDS indications rather than direct biological evidence.

This prediction should be treated with caution. NNRTIs are generally inactive against FIV because the FIV reverse transcriptase differs structurally in the NNRTI binding pocket. No supporting data were available, so the link remains a computational hypothesis.

Two other predictions share this limitation:
- **Simian immunodeficiency virus infection** (score 99.93%): SIV is closely related to HIV, but SIVmac is intrinsically resistant to many NNRTIs. The only linked publication (PMID 31658118) concerns islatravir, a different drug, and is not supportive.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.91%): no plausible mechanistic link was identified, and the score appears to be a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For the second-ranked prediction (simian immunodeficiency virus infection), one publication was linked, but it does not support doravirine:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Discusses islatravir, a reverse transcriptase translocation inhibitor, for HIV-1 treatment and prevention. It concerns a different drug and is indirect evidence only. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210806 (cancelled) | PIFELTRO (Merck Sharp & Dohme LLC) | Film-coated tablet (oral) | Not specified in the data |

## Safety Considerations

- **Drug Interactions**: 59 interactions were identified. Those shown here are from the first 20 records returned, and the full list was not reviewed.
  - **Major**: Dexamethasone and lumacaftor. Both are likely to lower doravirine exposure through CYP3A induction, which is a plausible mechanism but is not stated in the data.
  - **Moderate**: Glycerol phenylbutyrate, metreleptin, troglitazone, deferasirox, praziquantel, griseofulvin.
  - **Minor**: Aprepitant, cimetidine, clarithromycin, clotrimazole, miconazole, cobicistat, ticagrelor, ivacaftor, zafirlukast, chloramphenicol, erythromycin, fluconazole.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (evidence level L5), with no clinical trials and no direct literature. Known pharmacology suggests FIV and SIV are poorly susceptible to NNRTIs, so the prediction is likely a network artifact. In addition, the only US authorization is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for doravirine
- In vitro antiviral activity data against FIV reverse transcriptase, and against SIV for comparison
- Package insert warnings and contraindications
- Clarification of whether a veterinary indication is of any development interest, since feline AIDS is a veterinary disease
- Review of the remaining DDI records, with attention to the two Major interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

