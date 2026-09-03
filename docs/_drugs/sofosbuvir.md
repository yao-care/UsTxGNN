---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 1172
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Sofosbuvir is a nucleotide analog NS5B polymerase inhibitor originally developed for chronic hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**,
> but the surrounding evidence pack (50 clinical trials, 19 publications referencing this pairing) is dominated by reports of HBV *reactivation* during sofosbuvir-based HCV therapy rather than direct antiviral efficacy against HBV, with only one small Phase 2 pilot trial testing the drug in HBV-monoinfected patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection *(well-established drug identity; local license-level indication text unavailable — see below)* |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the regulatory record for this product. Based on well-established pharmacology, sofosbuvir is a nucleotide prodrug that is metabolized intracellularly to its active triphosphate form, which acts as a chain terminator when incorporated by the HCV NS5B RNA-dependent RNA polymerase (RdRp). This mechanism is specific to viruses that replicate their genome using an RdRp — a hallmark of RNA viruses such as HCV and other Flaviviridae members.

Hepatitis B virus, however, is a DNA virus that replicates via reverse transcription of an RNA pregenome using a viral reverse transcriptase, not an RdRp. This is a fundamental structural mismatch with HCV's replication machinery, and the evidence pack itself flags this mismatch as the primary concern for this prediction ("HBV為DNA病毒，複製依賴反轉錄酶而非RdRp，與sofosbuvir主要作用標的機轉不匹配").

Despite this mismatch, one open-label Phase 2 pilot study (NCT03312023 / PMID 36045503) tested ledipasvir/sofosbuvir in HBV-monoinfected patients, motivated by a retrospective observation of modest HBsAg decline in HBV/HCV-coinfected patients treated for HCV. It reported a measurable but modest reduction in HBsAg and HBV DNA at 12 weeks — not a cure. Meanwhile, a larger and more consistent body of literature in this same evidence pack describes the **opposite** phenomenon: HBV reactivation during or after sofosbuvir-based DAA therapy for HCV in coinfected patients. This suggests any HBsAg changes seen may reflect complex coinfection/immune dynamics rather than a direct antiviral effect on HBV, and that much of the "evidence" attached to this predicted indication is actually a safety signal rather than an efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label pilot of ledipasvir/sofosbuvir for 12 weeks in **HBV-monoinfected** patients; assessed decline in HBsAg and HBV DNA — the only direct test of antiviral activity against HBV in this pack. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Ledipasvir/sofosbuvir FDC for 12 weeks in HCV genotype 1/2 patients coinfected with HBV (Taiwan); efficacy/safety in the coinfection setting, not HBV monotherapy. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of incidence, morbidity and predictors of **HBV reactivation** during direct-acting antiviral treatment of HCV/HBV-coinfected patients. |
| [NCT02349048](https://clinicaltrials.gov/study/NCT02349048) | Phase 2 | Completed | 68 | Simeprevir + daclatasvir + sofosbuvir in HCV genotype 1 patients; the evidence pack links this trial to HBV literature (PMID 36045503), but the trial population itself is HCV, not HBV — relevance uncertain. |

*Note: The remaining ~46 trials captured for this indication in the evidence pack are HCV mono-infection studies with no direct bearing on HBV and were excluded from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 (single-arm) | Journal of Medical Virology | Open-label pilot of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; modest decline in HBsAg and HBV DNA at week 12. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Role of HBV antiviral therapy in patients with HBV reactivation after DAA treatment in HCV/HBV coinfection. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | Journal of Clinical Gastroenterology | Risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV infection. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective cohort | Journal of Viral Hepatitis | HBV reactivation in cancer patients receiving DAAs for HCV infection with HBV/HCV coinfection. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of Medical Case Reports | HBV reactivation via an HBsAg immune-escape mutant in an anti-HBc-positive patient during sofosbuvir/velpatasvir treatment for HCV. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Case report / ADR feature | Hospital Pharmacy | Reported case of hepatitis B reactivation with hepatitis C treatment using simeprevir and sofosbuvir. |

---

## US Market Information

Sofosbuvir currently has **no active marketing authorization** on file in this jurisdiction — market status is recorded as "Not marketed," with 0 licenses. No product listing, brand name, dosage form, or approved-indication text is available to summarize in a table.

---

## Safety Considerations

No formal key warnings, contraindications, or drug–drug interaction data are available in this record for sofosbuvir.

Please refer to the package insert for safety information.

**Note from the evidence base:** although not part of the formal safety dataset, the literature and trial evidence attached to this specific predicted indication (HBV) repeatedly documents **HBV reactivation** in HBV/HCV-coinfected patients during or after sofosbuvir-based DAA therapy for HCV (PMIDs 33031326, 29334502, 31632097, 33523503, 31542053, 27621502). This is a clinically important signal that should inform any future safety evaluation of sofosbuvir in HBV-related populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The proposed mechanism is biologically implausible as a direct antiviral effect — sofosbuvir targets an RNA-dependent RNA polymerase, but HBV replicates via reverse transcriptase, not RdRp.
- The bulk of available evidence for this indication describes a safety concern (HBV reactivation risk during sofosbuvir-based HCV therapy) rather than a therapeutic benefit signal; the single efficacy-oriented Phase 2 pilot (NCT03312023) showed only a modest, non-curative reduction in HBsAg/HBV DNA.

**To proceed, the following is needed:**
- Nonclinical/mechanistic studies clarifying whether sofosbuvir has any direct activity against HBV replication (e.g., polymerase or cccDNA assays), given the RdRp/reverse-transcriptase mismatch
- A larger, randomized, adequately powered trial in HBV-monoinfected patients with virologic-cure endpoints (HBsAg seroconversion)
- TFDA/DrugBank-sourced MOA and package-insert warnings data (currently unavailable) to support an S1 safety pre-screening
- A dedicated safety review addressing HBV reactivation risk, since this currently appears more clinically significant than any efficacy signal
- A local regulatory dossier, as the product is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

