---
layout: default
title: Remdesivir
parent: Model Prediction Only (L5)
nav_order: 1116
evidence_level: L5
indication_count: 6
monitor_inn: "REMDESIVIR"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
last_modified_at: 2026-10-30
description: "Remdesivir: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not recorded in the local data"
---

# Remdesivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Remdesivir: Multiple endocrine neoplasia
{: .text-alpha }

## One-Sentence Summary

Remdesivir is a nucleotide analog antiviral, supplied in the US as an intravenous injection (Veklury), and the data compiled for this report do not list a specific approved indication text for it.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction without supporting evidence, so it should be treated with caution.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase.

Multiple endocrine neoplasia (MEN) is a hereditary tumor syndrome driven by genes such as MEN1 and RET, and has no viral cause. No mechanistic link between remdesivir and MEN could be identified. The high score (0.9950) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For context, the other top predictions are also weakly supported:
- **HIV infectious disease** (score 0.9932, L4): Remdesivir targets viral RdRp, while HIV depends on reverse transcriptase, so mechanistic overlap is weak. The retrieved trial and literature concern COVID-19, not HIV.
- **Simian immunodeficiency virus infection** and **feline acquired immunodeficiency syndrome** (both 0.9907, L5): The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as HIV, not biological evidence. They are non-human indications with no supporting studies.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (0.9903, L5) and **homozygous familial hypercholesterolemia** (0.9903, L5): No plausible mechanistic link and no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered for multiple endocrine neoplasia.

For reference, the only trial retrieved among the top predictions was for the second-ranked prediction (HIV infectious disease). It is not direct evidence for that indication either:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04385719](https://clinicaltrials.gov/study/NCT04385719) | Phase 2 | Completed | 24 | Pharmacokinetic study in healthy Ugandan volunteers of how tenofovir/lamivudine or atazanavir/ritonavir affect remdesivir blood levels. It did not test remdesivir in HIV patients. |

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA214787 | Veklury (Gilead Sciences, Inc.) | Lyophilized powder for injection solution | Not listed in the data compiled for this report; status: valid |

## Safety Considerations

- **Drug Interactions**: The DDI query returned 100 interactions in total; the first 20 returned are all rated Moderate. Examples include:
  - Antibiotics: doxycycline, minocycline, tetracycline, clarithromycin, vancomycin, kanamycin, neomycin, levofloxacin
  - Antifungals: amphotericin B (including the lipid complex)
  - Other: acarbose, pioglitazone, bupropion, naltrexone, mesalazine, balsalazide, olsalazine, chenodeoxycholic acid, oxandrolone, oxymetholone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for multiple endocrine neoplasia is supported only by the model score. There are no clinical trials, no literature, and no plausible mechanistic link between a viral RdRp inhibitor and a hereditary tumor syndrome. The US authorization is also listed as cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking remdesivir to MEN1/RET-driven disease
- Preclinical evidence (for example, cell or animal models of MEN) to move beyond L5
- FDA package insert warnings and contraindications (blocking for safety screening)
- Review of route compatibility, since remdesivir is available only as an injectable
- Consideration of the other predictions only after dedicated evidence is generated, as none currently has direct supporting studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

