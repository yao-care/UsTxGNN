---
layout: default
title: Sofosbuvir
parent: Model Prediction Only (L5)
nav_order: 1172
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Sofosbuvir: From Chronic Hepatitis C to Hepatitis E Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide-analog inhibitor of the hepatitis C virus (HCV) polymerase, originally used to treat chronic hepatitis C.
The TxGNN model's top-ranked prediction is **hepatitis B virus infection**, but the mechanistic and clinical review does not support it. The best-supported candidate is **hepatitis E virus infection**, with **1 completed Phase 2 pilot trial (n=10)** and several in vitro and case-level publications. Its clinical results have been mixed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (no approved-indication text is available in the US licence records) |
| Predicted New Indication | Top TxGNN prediction: hepatitis B virus infection (rank 1). Best-supported candidate after evidence review: hepatitis E virus infection (rank 2) |
| TxGNN Prediction Score | Hepatitis B virus infection: 99.77%. Hepatitis E virus infection: 99.49% |
| Evidence Level | L2 for hepatitis E (one completed Phase 2 pilot, no Phase 3 data); L2 for hepatitis B (co-infection data only) |
| US Market Status | Cancelled only (all 7 licences cancelled) |
| Number of NDAs | 7 |
| Recommended Decision | Hold (hepatitis E may proceed as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, sofosbuvir is a prodrug whose triphosphate metabolite inhibits the viral RNA-dependent RNA polymerase (NS5B in HCV).

**Hepatitis B (top-ranked prediction):** This link is weak. HBV replicates through a DNA polymerase/reverse transcriptase, which is a different mechanism from HCV NS5B. HBV changes seen in trials occur mainly in HCV/HBV co-infected patients and most likely reflect HCV clearance, not direct anti-HBV activity. HBV reactivation during direct-acting antiviral (DAA) therapy is a recognized safety concern. The high TxGNN score probably reflects network proximity among hepatitis viruses rather than true efficacy.

**Hepatitis E (best-supported):** HEV is a positive-strand RNA virus with its own RNA polymerase, so a nucleotide-analog mechanism is plausible. Cell-culture studies show sofosbuvir inhibits HEV replication, with an additive effect when combined with ribavirin, and a rabbit model showed inhibition at high doses. In patients, however, results were mixed: a pilot trial reduced viral RNA initially but did not produce a sustained virologic response, and resistance-associated variants emerged during treatment. Reports in ribavirin-refractory patients are inconsistent.

**Other predictions** (hepatitis A, Kyasanur forest disease, Omsk hemorrhagic fever, nonspecific animal viral hepatitis, HIV) rest on in vitro or enzyme-level data, or on no data at all. For HIV, sofosbuvir has no recognized activity, and the trials found only treat HCV in co-infected patients.

---

## Clinical Trial Evidence

Trials below are for the two leading candidates.

**Hepatitis E virus infection**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03282474](https://clinicaltrials.gov/study/NCT03282474) | Phase 2 | Completed | 10 | HepNet single-arm pilot of sofosbuvir in chronic hepatitis E. Directly relevant but small and uncontrolled |

**Hepatitis B virus infection (co-infection and related studies)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Ledipasvir/sofosbuvir for 12 weeks in HBV-infected subjects. Small, single-arm, and no clear evidence of direct anti-HBV efficacy |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAAs in HCV/HBV co-infection, focused on HBV reactivation. Effect confounded by HCV clearance |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | Sofosbuvir/velpatasvir with prophylactic tenofovir alafenamide (TAF) in HCV/HBV co-infection. Addresses HBV reactivation prevention, not sofosbuvir efficacy |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | Ledipasvir/sofosbuvir in HCV-associated indolent B-cell lymphoma. Small pilot, limited interpretability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label trial | J Med Virol | Ledipasvir/sofosbuvir in HBV mono-infection, testing for HBsAg and HBV DNA decline at week 12 |
| [37334496](https://pubmed.ncbi.nlm.nih.gov/37334496/) | 2023 | Clinical analysis | Hepatology | In the sofosbuvir pilot in chronic HEV, viral RNA fell initially but no sustained response; resistance-associated variants emerged |
| [35814503](https://pubmed.ncbi.nlm.nih.gov/35814503/) | 2022 | Review | J Clin Exp Hepatol | Review of in vitro and in vivo evidence for sofosbuvir in HEV |
| [35247472](https://pubmed.ncbi.nlm.nih.gov/35247472/) | 2022 | Animal study | Antiviral Res | High-dose sofosbuvir, alone or with ribavirin, inhibited HEV replication in a rabbit model |
| [26408347](https://pubmed.ncbi.nlm.nih.gov/26408347/) | 2016 | In vitro | Gastroenterology | Sofosbuvir inhibits HEV genotype 3 replication, with an additive effect with ribavirin |
| [36942308](https://pubmed.ncbi.nlm.nih.gov/36942308/) | 2023 | Case report | IDCases | Ledipasvir/sofosbuvir plus ribavirin cleared ribavirin-refractory persistent HEV in a patient |
| [31404927](https://pubmed.ncbi.nlm.nih.gov/31404927/) | 2019 | Case series | Open Forum Infect Dis | Sofosbuvir added to ribavirin in 3 transplant recipients did not eliminate HEV |
| [29653132](https://pubmed.ncbi.nlm.nih.gov/29653132/) | 2018 | In vitro | Antiviral Res | Sofosbuvir inhibits hepatitis A virus replication in a cell-based reporter assay |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Cohort | J Clin Med | HBV-DNA and HBsAg kinetics in HCV co-infected patients on DAAs, reflecting virological interplay and reactivation risk |
| [36521285](https://pubmed.ncbi.nlm.nih.gov/36521285/) | 2023 | Biochemical in vitro | Biochem Biophys Res Commun | Sofosbuvir and its triphosphate inhibit Kyasanur forest disease virus polymerase activity (enzyme level only) |

---

## US Market Information

All seven US licences are cancelled. The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204671 | Sovaldi | Tablet, film coated | Not available |
| NDA212480 | Sovaldi | Pellet | Not available |
| NDA205834 | Ledipasvir and Sofosbuvir | Tablet, film coated | Not available |
| NDA214187 | Epclusa | Pellet | Not available |
| NDA208341 | Sofosbuvir and Velpatasvir | Tablet, film coated | Not available |

Two further licences are not listed here: NDA212477 (Harvoni, pellet) and NDA209195 (Vosevi, tablet, film coated).

---

## Safety Considerations

- **Drug Interactions** (8 interactions recorded):
  - Major: apalutamide, enzalutamide, lorlatinib
  - Moderate: fostamatinib, warfarin, dicoumarol, encorafenib
  - Minor: cyclosporine
- **HBV reactivation:** The literature documents HBV reactivation in patients with HBV co-infection or prior HBV exposure who receive sofosbuvir-based DAA therapy. HBV screening and monitoring are therefore important in any repurposing study.
- **Resistance:** Resistance-associated variants emerged during sofosbuvir treatment in chronic HEV patients.

For label warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold** (hepatitis E virus infection may continue as a research question)

**Rationale:**
- The top TxGNN prediction (hepatitis B) is not mechanistically supported, and observed HBV effects most likely reflect HCV clearance. Reactivation risk is a safety concern, not a benefit.
- Hepatitis E has a plausible RdRp mechanism and supportive in vitro and animal data, but the only clinical trial is a 10-patient pilot with no sustained virologic response and emerging resistance.
- Hepatitis A, Kyasanur forest disease, Omsk hemorrhagic fever and the nonspecific viral hepatitis category rest on in vitro, enzyme-level or no data. HIV evidence concerns HCV treatment in co-infected patients and is not repurposing evidence.
- All US licences are cancelled, which may complicate any US development path.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing)
- Detailed mechanism-of-action data
- For hepatitis E: a larger controlled study, dose optimisation, and evaluation of combination use with ribavirin
- HBV screening and reactivation monitoring plan for any study population
- Review of the US regulatory pathway given the cancelled licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

