---
layout: default
title: Darolutamide
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 3
monitor_inn: "DAROLUTAMIDE"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease"]
---

# Darolutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Darolutamide: From Prostate Cancer (Original Indication Not Documented) to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is a non-steroidal androgen receptor antagonist marketed under the brand name NUBEQA. The indication text is not included in the data compiled for this report.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia** (top-ranked prediction), but **0 clinical trials** and **0 publications** support this direction.
The evidence rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (1 NDA, cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Darolutamide is known to be a non-steroidal androgen receptor antagonist.

There is no established biological pathway linking androgen receptor blockade to the defective LDL receptor function that causes homozygous familial hypercholesterolemia. The high TxGNN score (0.991) most likely reflects a network-based artifact rather than a true mechanistic relationship. The score is also not a strong discriminator here: this prediction ranks 19,390th overall, and the other top-ranked predictions have similar scores.

Two other predictions were also generated, both with equally weak support:
- **Multiple endocrine neoplasia** (score 99.06%, L4): The two linked trials concern prostate cancer settings, not MEN syndromes, so the link is indirect.
- **HIV infectious disease** (score 99.04%, L5): No recognized mechanism connects androgen receptor antagonism to HIV treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for homozygous familial hypercholesterolemia.

For reference, the second-ranked prediction (multiple endocrine neoplasia) has two loosely related trials, neither of which provides direct evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07795177](https://clinicaltrials.gov/study/NCT07795177) | Phase 2 | Not yet recruiting | 40 | Observational spatial multi-omics study to predict response to androgen deprivation plus second-generation endocrine agents in metastatic hormone-sensitive prostate cancer. Not specific to MEN, and no results. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision oncology platform trial. Not specific to MEN, and enrollment was too small to yield interpretable data. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212099 (cancelled) | NUBEQA (Bayer HealthCare Pharmaceuticals Inc.) | Film-coated tablet (oral) | Not available in the data compiled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (androgen receptor antagonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The 20 listed in the compiled data include:
  - **Major**: Dexamethasone, Eluxadoline, Rosuvastatin
  - **Moderate**: Clarithromycin, Empagliflozin, Glyburide, Glycerol phenylbutyrate, Metreleptin, Repaglinide, Rifaximin, Simvastatin, Sulfasalazine, Troglitazone, Cobicistat, Deferasirox, Eltrombopag, Lusutrombopag
  - **Minor**: Aprepitant, Cimetidine, Miconazole

  The statin interactions (rosuvastatin, simvastatin) are particularly relevant to the predicted hypercholesterolemia indication, because patients would likely be on lipid-lowering therapy. Cobicistat and clarithromycin interactions would also complicate use alongside antiretroviral regimens.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanism linking androgen receptor antagonism to homozygous familial hypercholesterolemia. The US market status is also "Cancelled only", and the package insert safety data has not been obtained, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank) to assess any biological link
- Approved indication text, to confirm the original indication
- Clarification of the cancelled NDA status
- Preclinical or mechanistic evidence linking androgen receptor signalling to LDL receptor function or lipid metabolism before any clinical investigation
- Review of the statin interactions if lipid-lowering use is ever pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

