---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
monitor_inn: "ACYCLOVIR"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-10-28
description: "Acyclovir: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Acyclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Acyclovir: nucleoside analogue antiviral → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Acyclovir is a nucleoside-analogue antiviral that acts against herpesviruses.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials** and only **2 publications** were retrieved, and neither studies acyclovir in this disease, so the prediction is not supported by clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 16) |
| Number of NDAs | at least 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Acyclovir is active against herpesviruses. It is selectively activated by viral thymidine kinase and then blocks viral DNA synthesis. Detailed mechanism-of-action data are not available in the data compiled for this report, so this description reflects general knowledge of the drug class.

The link to punctate epithelial keratoconjunctivitis is weak. The only literature retrieved concerns microsporidial keratoconjunctivitis (a parasitic infection) and drug-induced corneal lipidosis in patients with AIDS. Neither is herpetic and neither involves acyclovir as a treatment. The high model score therefore rests on network-level similarity and is not backed by clinical data. Any plausibility would depend on a viral cause of the keratoconjunctivitis that acyclovir could target, which the retrieved data do not show.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Characteristics of microsporidial keratoconjunctivitis in an eastern Indian cohort; not related to acyclovir treatment |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case series | Am J Ophthalmol | Drug-induced corneal lipidosis in two AIDS patients treated for opportunistic infections; no acyclovir efficacy data |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075382 | Acyclovir | Tablet | Not recorded |
| ANDA074889 | Acyclovir | Capsule | Not recorded |
| ANDA215404 | Acyclovir | Injection, solution | Not recorded |
| ANDA212202 | Acyclovir | Ointment | Not recorded |
| ANDA212361 | Acyclovir | Cream | Not recorded |

The data include at least 16 licence records, and this list may be partial. Several records in the data are for valacyclovir products, and only the acyclovir-named records are listed above.

## Safety Considerations

Please refer to the package insert for safety information.

Drug-interaction screening returned 100 entries. The moderate-level interactions are with balsalazide, mesalazine, olsalazine, sulfasalazine and trospium. Other listed interactions (for example amphotericin B, mannitol, metformin and morphine) have an unknown severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9967), but no clinical trials exist and the retrieved literature does not study acyclovir in this disease. The evidence is at the model-prediction level only (L5).

**To proceed, the following is needed:**
- Evidence that a virus susceptible to acyclovir (for example HSV or VZV) causes this form of keratoconjunctivitis
- Clinical studies or case series of acyclovir in punctate epithelial keratoconjunctivitis
- Detailed mechanism-of-action data
- Package insert warnings and contraindications for review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

