---
layout: default
title: Pretomanid
parent: Model Prediction Only (L5)
nav_order: 1080
evidence_level: L5
indication_count: 5
monitor_inn: "PRETOMANID"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
last_modified_at: 2026-10-14
description: "Pretomanid: predicted new indication Candidiasis (evidence level L5). Approved use: Not available in the license record (known use: drug-resistant pulmon…"
---

# Pretomanid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Pretomanid: From Drug-Resistant Tuberculosis to Candidiasis
{: .text-alpha }

## One-Sentence Summary

Pretomanid is an oral nitroimidazooxazine antibiotic used against drug-resistant tuberculosis, and it is part of the BPaL regimen (bedaquiline, pretomanid, linezolid). The TxGNN model ranks **candidiasis** as its top predicted new indication, but **no clinical trials and no publications** support this prediction. The "Predicted New Indication" shown below is the top-ranked one; the only candidate with any related literature is leprosy, and that literature is indirect.

> Note: The US regulatory record compiled for this report has no approved-indication text. The tuberculosis context comes from the literature and the drug's known pharmacology, not from the license record.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the license record (known use: drug-resistant pulmonary tuberculosis as part of BPaL) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 0.9969 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pretomanid is known to be a prodrug activated by the Ddn nitroreductase of *Mycobacterium tuberculosis*, and it has no established antifungal activity.

For candidiasis, the supplied data support **no mechanistic link**. The very high TxGNN score (0.9969) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. A fungal infection caused by *Candida* is biologically distant from mycobacterial infection, so this prediction should be treated as a computational hypothesis.

**Other predicted indications (for context):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Leprosy | 0.9927 | L5 | Biologically plausible but untested. *M. leprae* is related to *M. tuberculosis*, but it may lack or have a divergent Ddn/F420 activation pathway because of extensive genome reduction. This needs verification. |
| 3 | Coronary artery disease | 0.9925 | L5 | No identifiable mechanistic rationale. |
| 4 | Myocardial ischemia | 0.9917 | L5 | No mechanistic rationale; likely driven by network proximity to coronary artery disease. |
| 5 | Anomalous left coronary artery from the pulmonary artery | 0.9908 | L5 | A congenital structural anomaly treated surgically; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for candidiasis. No trials were found for the other predicted indications either.

---

## Literature Evidence

Currently no related literature available for candidiasis.

For reference, the eight publications retrieved for the second-ranked prediction (leprosy) are listed below. **None of them addresses leprosy.** All concern drug-resistant tuberculosis and are indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41876996](https://pubmed.ncbi.nlm.nih.gov/41876996/) | 2026 | Cohort | BMC Infect Dis | Effectiveness and safety of BPaLM in drug-resistant TB in Ethiopian hospitals (multicenter retrospective study) |
| [41080099](https://pubmed.ncbi.nlm.nih.gov/41080099/) | 2025 | Cohort | Pan Afr Med J | Treatment outcomes with BPaL/BPaLM in drug-resistant TB in southeast Nigeria |
| [41263908](https://pubmed.ncbi.nlm.nih.gov/41263908/) | 2025 | Review | Arch Microbiol | Comprehensive review of pretomanid for drug-resistant pulmonary TB |
| [41354901](https://pubmed.ncbi.nlm.nih.gov/41354901/) | 2025 | Genomic study | Commun Med | Whole-genome sequencing to detect XDR-TB in Ethiopia |
| [38180980](https://pubmed.ncbi.nlm.nih.gov/38180980/) | 2024 | Modelling | PLoS One | Projected global uptake of 6-month DR-TB regimens by 2026 |
| [37291443](https://pubmed.ncbi.nlm.nih.gov/37291443/) | 2023 | Preclinical | AAPS PharmSciTech | Inhaled adjunct formulations including a pretomanid analog (TBA-354) for MDR-TB |
| [34992077](https://pubmed.ncbi.nlm.nih.gov/34992077/) | 2022 | Budget analysis | BMJ Glob Health | Budget impact of BPaL for XDR-TB in Indonesia, Kyrgyzstan and Nigeria |
| [34271884](https://pubmed.ncbi.nlm.nih.gov/34271884/) | 2021 | Implementation study | BMC Public Health | Acceptability and feasibility of BPaL among stakeholders |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212862 (cancelled) | Pretomanid (Viatris Specialty LLC) | Tablet | Not available in the record |

---

## Safety Considerations

- **Drug Interactions**: 14 interactions were recorded in the DDInter database.
  - **Major (7):** dexamethasone, lumacaftor, apalutamide, dabrafenib, mitotane, lorlatinib, enzalutamide
  - **Moderate (7):** empagliflozin, sitagliptin, somatropin, somatrem, baricitinib, clofarabine, methotrexate

Please refer to the package insert for warnings and contraindications, because these data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction rests on a model score alone, with no trials, no literature, and no known antifungal activity of pretomanid. The only biologically plausible alternative, leprosy, is still an untested research question (L4) supported only by indirect tuberculosis literature. The cardiovascular predictions have no plausible rationale. In addition, the US NDA is recorded as cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- In vitro testing of pretomanid against *Candida* species, if candidiasis remains of interest
- For leprosy, confirmation that *M. leprae* has a functional Ddn/F420 activation pathway, followed by in vitro or animal-model susceptibility testing
- Confirmation of the current US regulatory status and the approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

