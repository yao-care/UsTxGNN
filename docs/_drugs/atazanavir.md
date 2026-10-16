---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 6
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "AIDS related complex", "congenital human immunodeficiency virus"]
---

# Atazanavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Atazanavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome** (a veterinary disease), with **0 clinical trials** and **0 publications** supporting it.
The only indication with meaningful observational evidence is **congenital HIV** (7 publications), which largely overlaps with the original indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS (the US license records provided contain no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 7 (NDA and ANDA authorizations, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, atazanavir is a protease inhibitor whose efficacy in HIV infection is established, and mechanistically it may be applicable to related lentiviral diseases.

Feline immunodeficiency virus (FIV) is a lentivirus whose protease is structurally related to HIV-1 protease, so a protease inhibitor could plausibly act on it. The very high score (99.98%) is likely driven by the disease's similarity to HIV in the knowledge graph. It is also a veterinary indication, outside the scope of human drug repurposing.

Other predictions in the top six:
- **Simian immunodeficiency virus infection**: an animal model of HIV. The only evidence is a 2010 macaque study of combination antiretroviral therapy, which does not isolate atazanavir's contribution.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter**: no plausible mechanistic link; likely a knowledge-graph artifact.
- **Obsolete familial combined hyperlipidemia**: protease inhibitors are known to cause dyslipidemia, so benefit is unsupported and the prediction may point in the wrong direction. The disease term is also obsolete.
- **AIDS related complex**: a historical term for symptomatic HIV disease, essentially the original indication under another name.
- **Congenital HIV**: the most clinically meaningful prediction, relating to prevention of vertical transmission (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other five predictions.

---

## Literature Evidence

No literature is available for the top-ranked prediction (feline AIDS). The table below covers the most relevant publications across the other predictions, with congenital HIV (rank 6, evidence level L3) the most substantial.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort | Antiviral Therapy | Atazanavir exposure during pregnancy was effective regardless of tenofovir use (congenital HIV) |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohort | Frontiers in Immunology | PHACS SMARTT study assessing safety of in utero antiretroviral exposure (congenital HIV) |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Congenital anomalies and in utero antiretroviral exposure in HIV-exposed uninfected infants |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/non-case pharmacovigilance | Eur J Clin Pharmacol | Risk of congenital anomalies after antiretroviral exposure in pregnancy, European registry data |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohort | J Acquir Immune Defic Syndr | Antiretroviral regimens and AIDS-defining neurological conditions (AIDS related complex) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Gastrointestinal adverse events in HIV-treated and untreated patients (AIDS related complex) |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | Preclinical in vitro/rat | Reproductive Toxicology | Atazanavir and ritonavir interact with ABCB1, ABCG2 and ABCC2 transporters affecting placental transfer in rats |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Preclinical animal | J Infect Dis | In macaques, HAART reduced CNS viral replication and inflammation but viral DNA persisted (SIV infection) |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | Preclinical in vitro | Antimicrob Agents Chemother | Fluorine-modified protease inhibitors showed potent activity against drug-resistant HIV-1 (AIDS related complex) |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cohort | J AIDS Immune Res | Newborn hearing screening in HIV-exposed uninfected infants (congenital HIV) |

Most of this literature concerns safety of antiretroviral exposure rather than treatment efficacy for the predicted indication. One paper (PMID 31595301) concerns dolutegravir rather than atazanavir and is omitted.

---

## US Market Information

All seven US authorizations are cancelled, and the records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021567 | REYATAZ | Capsule, gelatin coated | Not available |
| NDA206352 | REYATAZ | Powder | Not available |
| NDA206353 | EVOTAZ | Tablet | Not available |
| ANDA212278 | Atazanavir | Capsule | Not available |
| ANDA204806 | Atazanavir Sulfate | Capsule | Not available |

Two additional generic capsule authorizations are also cancelled (ANDA091673, Teva; ANDA212579, Laurus Labs).

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

**Contraindication-related conditions (knowledge graph, not label text):** liver failure, liver disease, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C virus infection, hemophilia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), nephrolithiasis, acute urate nephropathy, atrioventricular block, and lactic acidosis.

**Drug Interactions:** 100 interactions were identified. Examples from the first 20 reviewed:
- **Major:** famotidine, ranitidine, rabeprazole, omeprazole (acid-reducing agents), loperamide, triamcinolone, budesonide
- **Moderate:** acarbose, metformin, pioglitazone, alogliptin, albiglutide, acetohexamide (antidiabetic agents), hydrocortisone, betamethasone, aprepitant, alosetron, aluminum hydroxide, calcium carbonate

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline AIDS) is a veterinary indication with no trials or literature, and its high score likely reflects similarity to HIV in the knowledge graph. The most credible human-relevant signal, congenital HIV, is supported only by observational, mostly safety-focused studies and overlaps with the original indication. All US authorizations are cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Clarification of whether a veterinary indication falls within the repurposing scope; if not, shift focus to congenital HIV
- For congenital HIV, efficacy data specific to infant or perinatal treatment rather than exposure safety
- Review of why the US authorizations were cancelled and whether any product remains available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

