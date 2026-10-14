---
layout: default
title: Abemaciclib
parent: Moderate Evidence (L3-L4)
nav_order: 43
evidence_level: L4
indication_count: 10
---

# Abemaciclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is an oral CDK4/6 inhibitor, originally used in hormone receptor-positive, HER2-negative breast cancer. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials** and only **2 publications** (one observational study and one preclinical nanoplatform paper) currently relate to this direction, and neither shows a therapeutic benefit in patients.

> Note: The regulatory data compiled for this report contain no approved-indication text. The breast cancer use is taken from general knowledge of the drug, not from the US label data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled regulatory data (known use: HR+/HER2- breast cancer) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (the single listed NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, abemaciclib inhibits CDK4/6, which controls the cell-cycle transition from G1 to S phase. Its efficacy in breast cancer rests on this antiproliferative effect.

In rheumatoid arthritis, overgrowth of fibroblast-like synoviocytes and activated lymphocytes drives synovial hyperplasia. Blocking CDK4/6 could plausibly dampen this proliferation, which is the main reasoning behind the prediction.

This link is hypothetical. The only supporting paper is a preclinical nanoplatform study (Mn/Si-Abe@BSA) whose relevance to abemaciclib given as a drug is unclear. The other paper is an observational study of immune-mediated diseases in breast cancer patients on CDK4/6 inhibitors, and it does not show a therapeutic benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Examined pre-existing and emerging autoimmune diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors and endocrine therapy. CDK4/6 inhibitors may influence immune function, enhancing antitumour immunity but possibly triggering autoimmune reactions. No therapeutic benefit in RA shown. |
| [42289719](https://pubmed.ncbi.nlm.nih.gov/42289719/) | 2026 | Preclinical | Journal of Nanobiotechnology | A pH-responsive nanoplatform loaded with abemaciclib induces cell-cycle arrest and apoptosis in fibroblast-like synoviocytes for RA. Preclinical only. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208716 | Verzenio (Eli Lilly and Company) | Tablet | Not stated in the data; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral CDK4/6 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; a complete blood count and liver function monitoring are generally expected for this class |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded, and 20 are listed in the compiled data. Major-level interactions include:
  - Clarithromycin
  - Cobicistat
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Lumacaftor

  Moderate-level interactions include aprepitant, clotrimazole, dexamethasone, metformin, fluconazole, erythromycin, chloramphenicol, ticagrelor, roflumilast and others.
- **Cardiovascular signals (from literature)**: Pharmacovigilance studies, meta-analyses and case reports describe QTc prolongation, thromboembolic events, atrial arrhythmias and kidney injury with CDK4/6 inhibitors, including abemaciclib. These matter if the drug were considered for a non-oncology population such as RA.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and a plausible but untested mechanism. There are no clinical trials, and the literature includes one observational study and one preclinical paper. The US license is listed as cancelled, and cardiovascular and thromboembolic safety signals make benefit-risk in a chronic autoimmune disease uncertain.

**To proceed, the following is needed:**
- Mechanism of action data and mechanistic-link analysis
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical in vivo arthritis model data (for example collagen-induced arthritis) testing abemaciclib itself
- Evaluation of dose, exposure and long-term tolerability for a chronic inflammatory indication
- Comparison with established RA therapies, including JAK inhibitors and biologics
- Clarification of the current US regulatory status of the product

### Other Predicted Indications (for reference)

The remaining predictions (hyperthyroidism, multiple endocrine neoplasia, heart disease, amyotrophic lateral sclerosis, and others) are also rated Hold.

- **Amyotrophic lateral sclerosis** is the most notable. A preclinical study reports that abemaciclib decreases aggregate-prone TDP-43 accumulation by accelerating autophagic flux. It is flagged as a research question, but CNS exposure and in vivo efficacy are untested.
- **Multiple endocrine neoplasia** has one trial (NCT03878524), a terminated Phase 1 study with 2 participants. It yields no usable efficacy data.
- **Heart disease** literature mainly describes cardiotoxicity of CDK4/6 inhibitors, which argues against a benefit.
- The remaining predictions have no trials, no literature and no clear mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

