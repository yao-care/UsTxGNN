---
layout: default
title: Enzalutamide
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an oral androgen receptor (AR) inhibitor marketed in the US as Xtandi, and it is used in prostate cancer (the supplied data do not list an original indication).
The TxGNN model predicts it may be effective for **prostate cancer/brain cancer susceptibility**, but **0 clinical trials** and **0 publications** support this specific prediction.
This term describes a genetic predisposition phenotype rather than a treatable disease, so the prediction is best read as a model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (general knowledge; all approved-indication fields in the supplied data are empty) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 license records (2 unique NDAs: NDA213674, NDA203415) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Enzalutamide blocks AR signaling. It inhibits ligand binding, nuclear translocation and DNA binding of the receptor. Detailed mechanism-of-action data are not available in the supplied record, so this description relies on general pharmacology.

The link to the predicted term exists only through its "prostate cancer" component, where AR signaling drives tumor growth. The term itself describes an inherited predisposition, not an active disease. A drug can treat an established cancer, but it does not treat a susceptibility state. The high score (0.997) most likely reflects proximity in the knowledge graph rather than clinical support.

The relationship to the original indication is therefore weak. The prediction overlaps with prostate cancer, where enzalutamide is already used. It adds nothing that can be tested as a new indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

For context, the same evidence pack contains many enzalutamide trials under other predicted terms. The most relevant is a randomized Phase 2 study in localized prostate cancer on active surveillance ([NCT02799745](https://clinicaltrials.gov/study/NCT02799745), n=227, completed). It does not support this susceptibility term.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The five license records contain only two unique NDAs. The source data list no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213674 | Xtandi (Astellas Pharma US, Inc.) | Tablet | Not listed in source data |
| NDA203415 | Xtandi (Astellas Pharma US, Inc.) | Capsule | Not listed in source data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (AR inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The evidence pack rationale for related predictions notes seizure, fall and fracture risks. These are weighed against a benign or non-disease target. No warnings, contraindications or drug-interaction records were retrieved.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted term is a genetic susceptibility phenotype, not a treatable disease. It has no trials, no literature, and only model-based (L5) support. The high TxGNN score is not clinical evidence.

**To proceed, the following is needed:**
- Resolve the umbrella term to a specific, treatable disease. Otherwise drop this candidate.
- Obtain the FDA package insert (warnings, contraindications, approved indications), which is currently missing and blocks safety screening.
- Obtain detailed mechanism-of-action data from DrugBank.
- Note that another prediction in this pack, "male reproductive organ cancer" (rank 6), has stronger support. It reaches L2 with a randomized Phase 2 trial, but this is mostly label confirmation for prostate cancer rather than true repurposing. It should be evaluated in its own report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

