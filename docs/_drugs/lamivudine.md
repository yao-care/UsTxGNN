---
layout: default
title: Lamivudine
parent: Moderate Evidence (L3-L4)
nav_order: 830
evidence_level: L4
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Lamivudine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor already marketed in the US, and the label text in the data is empty. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, an animal model of HIV. This direction has **no registered clinical trials** and **20 publications**, all preclinical or background work. The prediction mostly restates lamivudine's known anti-retroviral activity and is not a new human repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the mechanistic rationale, because the label text in the data is empty) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lamivudine is a nucleoside reverse transcriptase inhibitor, and this class blocks the reverse transcriptase enzyme that lentiviruses need to replicate. SIV is a primate lentivirus closely related to HIV. Macaque studies use lamivudine in combination regimens with zidovudine, indinavir, tenofovir or efavirenz.

The relationship to the original indication is therefore very close. SIV infection in macaques is the standard animal model of HIV infection, so the prediction reflects a link between lamivudine's known HIV-1 use and the model virus. The high score (0.999) most likely comes from this on-label knowledge-graph connection.

SIV infection is not a human disease. It has no clinical development path of its own, and it does not open a new patient population. The findings are useful as preclinical context, such as how the M184V resistance mutation behaves in SIV and how post-exposure prophylaxis works in macaques. The original indication and MOA fields are both empty in the data, so they should be checked against the current label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All entries are preclinical, in vitro, or review papers. There are no RCTs.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Preclinical (macaque) | AIDS | Tested post-exposure prophylaxis with zidovudine, lamivudine and indinavir after vaginal SIV exposure |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Preclinical (macaque) | J Virol | HAART with efavirenz, lamivudine and tenofovir in rhesus macaques infected with RT-SHIV, a virus carrying HIV-1 reverse transcriptase |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | J Virol | Quadruple antiretroviral therapy produced rapid viral decay in SIVmac251-infected macaques |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Preclinical (macaque) | J Virol | The M184V resistance mutation emerged within 5 weeks in newborn macaques treated with lamivudine or emtricitabine, mimicking HIV-1 |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | Preclinical (SIV RT) | J Virol | Tenofovir selected for reversion of M184V, even in the presence of lamivudine |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Preclinical (macaque) | Retrovirology | Short-term HAART effect on SIV load in tissues depends on time of initiation and antiviral diffusion |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Compared the susceptibility of HIV-2, SIV and SHIV to approved anti-HIV-1 drugs |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Preclinical (macaque) | J Virol | Studied lymphocyte proliferation in SIV-infected macaques and the effect of early post-exposure antiviral therapy; lamivudine's specific role is unclear |
| [12804006](https://pubmed.ncbi.nlm.nih.gov/12804006/) | 2003 | Preclinical (primate) | AIDS Res Hum Retroviruses | Infection and HAART (zidovudine, lamivudine, indinavir) changed expression of P-glycoprotein and cellular kinases |
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Curr Opin HIV AIDS | Discusses islatravir for HIV-1 treatment and prevention; it is not specific to lamivudine or SIV |

---

## US Market Information

The approved-indication text is empty for all listed products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091606 | LAMIVUDINE | Tablet, film coated | Golden State Medical Supply, Inc. |
| ANDA077464 | Lamivudine | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA205217 | Lamivudine | Tablet, film coated | Lupin Pharmaceuticals, Inc. |
| ANDA091606 | Lamivudine | Tablet, film coated | American Health Packaging |
| ANDA090457 | Lamivudine | Tablet, film coated | Strides Pharma Science Limited |

Available dosage forms: oral film-coated tablets and a solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is preclinical only (L4), with no clinical trials. SIV infection is an animal model of HIV, and lamivudine is already marketed for HIV-1. The high TxGNN score therefore reflects an existing on-label mechanism and does not point to a new human indication.

**To proceed, the following is needed:**
- Confirm the original indications and mechanism of action against the current FDA label and DrugBank, since both are empty in the data
- Obtain the package insert warnings and contraindications, which are a blocking gap for safety screening
- Decide whether SIV or another animal lentivirus model has any development relevance, as opposed to being a background mechanism finding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

