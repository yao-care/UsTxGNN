---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 1018
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: Toward Liposarcoma — A Multi-Indication Repurposing Screen

## One-Sentence Summary

> Pazopanib is a multi-target tyrosine kinase inhibitor (VEGFR-1/2/3, PDGFR-α/β, c-KIT) with an established anti-angiogenic profile in oncology; this evidence pack screened it against **10 candidate indications**, most of them rare renal and soft-tissue sarcoma subtypes.
> The TxGNN model's most actionable prediction is **Liposarcoma**, supported by **9 clinical trials** (including a randomized Phase 2 trial) and **20 publications**, making it the only candidate in this pack to reach decision stage S3 ("Proceed with Guardrails").
> The other 9 candidates range from moderately supported (unclassified RCC, dermatofibrosarcoma protuberans, fibroblastic neoplasms) to purely model-driven with no corroborating evidence (e.g., RCC with Xp11.2/TFE3 fusion, ovarian myxoid liposarcoma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded as a structured field in this evidence pack (drug not currently marketed in the evaluated jurisdiction); literature evidence within the pack repeatedly describes pazopanib as an established therapy for clear-cell renal cell carcinoma and non-adipocytic soft tissue sarcoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field for this drug is a documented data gap (DG002). However, the evidence pack's own literature and clinical-trial rationale text consistently describe pazopanib as a **multi-target tyrosine kinase inhibitor**, blocking VEGFR-1/2/3, PDGFR-α/β, and c-KIT — an anti-angiogenic, anti-proliferative mechanism that underlies its established role in vascularized solid tumors such as clear-cell renal cell carcinoma and non-adipocytic soft tissue sarcoma.

Liposarcoma is mechanistically adjacent to this established use: it belongs to the same broad soft-tissue sarcoma family, and several subtypes (dedifferentiated and pleomorphic liposarcoma in particular) show PDGFR pathway activation and angiogenesis dependency. A patient-derived orthotopic xenograft study (PMID 30060824) demonstrated that PDGFRA-amplified pleomorphic liposarcoma regressed under pazopanib, and a separate xenograft study (PMID 25500074) showed tumor growth suppression via anti-angiogenic activity in dedifferentiated liposarcoma models — direct preclinical support for the mechanistic link.

Notably, the pivotal PALETTE trial that established pazopanib for soft tissue sarcoma originally *excluded* adipocytic (liposarcoma) tumors due to uncertain sensitivity. The clinical trials identified here (two dedicated Phase 2 studies, NCT01506596 and NCT01692496, plus a randomized Phase 2 trial combining pazopanib with gemcitabine, NCT01532687) represent the subsequent, indication-specific evidence base that closes that gap — making liposarcoma a logical "label-expansion" candidate rather than a purely speculative one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-arm study of pazopanib monotherapy in unresectable or metastatic liposarcoma |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib activity/tolerability in advanced/metastatic liposarcoma relapsed after standard therapy |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomized, double-blind: gemcitabine ± pazopanib for refractory soft tissue sarcoma (includes liposarcoma) |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib + oral topotecan in metastatic/unresectable soft tissue and bone sarcomas |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | Oral regorafenib in selected sarcoma subtypes; cites pazopanib activity precedent in soft tissue sarcoma |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | Regorafenib vs. placebo in metastatic soft tissue sarcoma post-anthracycline, including a liposarcoma cohort |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Neoadjuvant chemoradiation ± pazopanib in non-rhabdomyosarcoma soft tissue sarcoma |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | Active, not recruiting | 333 | INT230-6 (intratumoral) vs. US standard of care in liposarcoma/UPS/leiomyosarcoma |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Risk-adapted study of maintenance pazopanib, dose-escalated radiotherapy, and selinexor in non-rhabdomyosarcoma soft tissue sarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Phase 2 Trial | The Lancet. Oncology | Pazopanib for advanced liposarcoma |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 Trial | Expert Opin Investig Drugs | Pazopanib activity in advanced intermediate/high-grade liposarcoma |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 Trial | British Journal of Cancer | Pazopanib with oral topotecan prolongs PFS in refractory soft tissue sarcoma |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | Randomized Trial (PAPAGEMO) | JAMA Oncology | Pazopanib ± gemcitabine in anthracycline/ifosfamide-refractory soft tissue sarcoma |
| [34356494](https://pubmed.ncbi.nlm.nih.gov/34356494/) | 2021 | Translational Cohort (GISG-04/NOPASS) | Biology | Molecular/pathological profiling of high-risk soft tissue sarcoma before/after neoadjuvant pazopanib |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Case Report / PDX Model | Tissue & Cell | PDGFRA-amplified pleomorphic liposarcoma regressed by pazopanib in a patient-derived xenograft |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclinical | Translational Oncology | Pazopanib suppresses tumor growth via angiogenesis inhibition in dedifferentiated liposarcoma xenografts |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncology Research and Treatment | Established and experimental systemic treatment options for advanced liposarcoma |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Current Treatment Options in Oncology | Systemic therapy options for dedifferentiated liposarcoma |
| [37298520](https://pubmed.ncbi.nlm.nih.gov/37298520/) | 2023 | Review | Int J Molecular Sciences | Treatment of dedifferentiated liposarcoma in the era of immunotherapy |

---

## US Market Information

Pazopanib is currently recorded as **Not Marketed** in this evidence pack (`total_licenses: 0`, no license records available). No NDA/authorization data could be extracted for this candidate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: VEGFR-1/2/3, PDGFR-α/β, c-KIT) |
| Myelosuppression Risk | Typically low-to-moderate for anti-angiogenic TKIs as a class; no drug-specific toxicity data available in this evidence pack — please refer to the package insert |
| Emetogenicity Classification | Typically low for oral TKIs as a class; please refer to the package insert for drug-specific data |
| Monitoring Items | Blood pressure, liver function tests, urinalysis (proteinuria), and CBC are generally relevant given the VEGFR/PDGFR mechanism; please refer to the package insert for definitive monitoring requirements |
| Handling Protection | No drug-specific handling data available in this evidence pack — please refer to the package insert and institutional hazardous oral oncolytic handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings, contraindications, and DDI data are flagged as a **Blocking** data gap — DG001 — in this evidence pack and could not be retrieved.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Liposarcoma is the only one of the 10 screened indications to reach decision stage S3, backed by two indication-specific Phase 2 trials and a randomized Phase 2 trial, plus preclinical mechanistic support (PDGFR pathway activation) — a reasonable evidentiary base for cautious advancement, but not yet sufficient for an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/label safety data (warnings, contraindications, DDI) — currently a **Blocking** gap (DG001)
- Formal, structured mechanism-of-action documentation (DG002)
- Taiwan/US regulatory and licensing status confirmation (currently 0 licenses on record)
- A dedicated randomized Phase 3 trial in liposarcoma to move beyond the current single-arm/small-RCT evidence base

---

## Appendix: Other Predicted Indications Screened (Same Drug)

For context, this evidence pack scored pazopanib against 9 additional candidate indications. None reached the evidence maturity of liposarcoma; two others reached "Research Question" status:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------|------|------|------|
| 1 | RCC w/ Xp11.2/TFE3 fusion | 99.63% | L5 | S0 | Hold |
| 2 | RCC associated with neuroblastoma | 99.63% | L5 | S0 | Hold |
| 3 | Unclassified renal cell carcinoma | 99.63% | L2 | S2 | Research Question |
| 5 | Childhood kidney cell carcinoma | 99.54% | L4 | S1 | Hold |
| 6 | Ovarian myxoid liposarcoma | 99.51% | L5 | S0 | Hold |
| 7 | Heart fibrosarcoma | 99.37% | L4 | S0 | Hold |
| 8 | Fibroblastic neoplasm (incl. desmoid tumor, SFT) | 99.35% | L2 | S2 | Research Question |
| 9 | Kidney fibrosarcoma | 99.33% | L5 | S0 | Hold |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | L2 | S2 | Research Question |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

