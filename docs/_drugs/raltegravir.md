---
layout: default
title: Raltegravir
parent: Model Prediction Only (L5)
nav_order: 1106
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Raltegravir is an HIV-1 integrase strand transfer inhibitor, marketed in the US as ISENTRESS. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**. Support is limited to **1 withdrawn clinical trial (0 participants)** and **20 mostly animal or in vitro publications**. This is best read as a rediscovery of its known antiviral mechanism in a non-human model, not a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the input data (approved indication text is empty; the mechanism notes indicate the known use is HIV-1 infection) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (preclinical/animal studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Raltegravir blocks the strand transfer step of HIV-1 integrase, which prevents viral DNA from integrating into the host genome. SIV is a closely related lentivirus with a similar integrase enzyme, so the drug should work against it. Macaque studies support this. They show raltegravir-containing regimens suppressing SIV, and they also show resistance mutations emerging when therapy is not fully suppressive.

The prediction reflects the drug's known antiviral mechanism carried over to a non-human model virus, not a new therapeutic area for people. SIV in macaques is a research model of HIV. The high score is therefore expected, and it does not indicate a new human use.

The other two predictions carry even less repurposing value:
- **Feline acquired immunodeficiency syndrome (score 99.78%):** the only trials are two completed Phase 3 studies in human HIV-1, where raltegravir was the comparator against dolutegravir. No veterinary data were provided.
- **A rare neurodevelopmental disorder with ataxic gait and absent speech (score 99.77%):** no plausible mechanistic link and no evidence. It is likely a knowledge-graph artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Planned study of HIV decay kinetics with raltegravir. It studied HIV rather than SIV and enrolled no participants, so it produced no data. |

---

## Literature Evidence

No RCTs or reviews were found. All entries are animal or in vitro studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Animal study (NHP) | Retrovirology | Raltegravir plus two NRTIs was used as a new antiretroviral approach in SIVmac251-infected macaques and as a model of lentiviral persistence. |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study (NHP) | PLoS Pathog | A highly intensified multidrug ART regimen produced long-term viral suppression and restricted the viral reservoir in SIV-infected macaques. |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Animal study (NHP) | J Virol | Studied SIV 2-LTR circle dynamics, a marker of failed integration, in macaques treated with an integrase inhibitor, with and without CD8+ cells. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Animal study (NHP) | PLoS One | Two macaques on tenofovir/emtricitabine with raltegravir intensification had viral rebound and multiple resistance mutations, similar to HIV. |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Animal study (NHP) | J Virol | Evaluated the intactness of persistent viral genomes in SIV-infected macaques after ART started within one year of infection. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal study (NHP) | mBio | Lentiviral infection persisted in the brain despite effective ART and neuroimmune activation. |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Animal study (NHP) | Sci Transl Med | Topical integrase inhibitors given after exposure protected macaques from vaginal SHIV infection. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro | J Virol | Characterized resistance profiles of integrase inhibitors in SIVmac239, showing that mutations parallel those in HIV. |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro | J Virol | Tested how HIV integrase resistance mutations, once introduced into SIVmac239, change susceptibility to integrase inhibitors. |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In vitro | Clin Infect Dis | Dolutegravir and raltegravir showed proadipogenic and profibrotic effects and induced insulin resistance in human and simian adipose tissue and adipocytes. |

---

## US Market Information

The input listed no approved indication text for any authorization.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203045 | ISENTRESS (Merck Sharp & Dohme LLC) | Tablet, chewable | Not provided in the data |
| NDA022145 | ISENTRESS (Merck Sharp & Dohme LLC) | Tablet, film coated | Not provided in the data |
| NDA022145 | ISENTRESS (Proficient Rx LP) | Tablet, film coated | Not provided in the data |
| NDA022145 | ISENTRESS (A-S Medication Solutions) | Tablet, film coated | Not provided in the data |
| NDA205786 | ISENTRESS (Merck Sharp & Dohme LLC) | Granule, for suspension | Not provided in the data |

The pack reports 8 licenses in total, but only these 5 were listed.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

One literature signal: an in vitro and simian adipose tissue study reported that raltegravir and dolutegravir promoted adipogenic and profibrotic changes and insulin resistance (PMID 32166319). This has not been confirmed in patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only listed trial was withdrawn with no participants, and the literature is limited to macaque and in vitro work. SIV is a non-human model virus, and raltegravir is already marketed for HIV-1. The prediction confirms a known mechanism and does not open a new human indication.

**To proceed, the following is needed:**
- The original approved indication (HIV-1) and package insert warnings, contraindications and interactions, which are missing from the input
- Detailed mechanism of action data (MOA)
- A decision on whether SIV or feline AIDS has value as a research or veterinary target
- For any human indication, a new candidate with direct clinical evidence

Results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

