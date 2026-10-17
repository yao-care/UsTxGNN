---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "ETRAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
---

# Etravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Etravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The evidence rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (1 NDA and 3 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, etravirine is an NNRTI that acts on HIV-1 reverse transcriptase, and its efficacy in HIV infection is established.

The predicted indication is feline immunodeficiency virus (FIV) disease. FIV is a lentivirus related to HIV, which is the likely source of the prediction. However, FIV reverse transcriptase is generally considered intrinsically resistant to NNRTIs, so the mechanistic basis is weak. The high score most likely reflects closeness to HIV/AIDS in the knowledge graph rather than demonstrated antiviral activity against FIV.

**Other predictions in the top 10**

- **Simian immunodeficiency virus infection (99.98%):** SIV, like HIV-2, is typically not susceptible to NNRTIs, so activity is mechanistically uncertain. There is one preclinical publication on nanoparticle antiretroviral combinations against HIV, which is only indirect evidence.
- **Congenital HIV (99.79%) and AIDS-related complex (99.79%):** These are essentially the original indication in other settings, so the mechanism applies directly. They are extensions of the existing indication rather than true repurposing. Their literature is indirect (see below).
- **Neurodevelopmental disorder with ataxic gait, fibroma of prostate, Brenner tumor, benign reproductive system neoplasm, benign prostate phyllodes tumor, and obsolete familial combined hyperlipidemia:** No plausible mechanistic link was identified, and no trials or literature exist. These look like computational artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication or for any of the other nine predictions.

## Literature Evidence

No publications are available for the top predicted indication (feline AIDS). The publications below relate to lower-ranked predictions and provide only indirect support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Case series | Antiviral Therapy | Two cases of darunavir and etravirine, with or without raltegravir, used in pregnant, highly treatment-experienced women with HIV (congenital HIV) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Risk factors for gastrointestinal adverse events in treated and untreated HIV patients (AIDS-related complex) |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | Preclinical / in vitro | AIDS Research and Human Retroviruses | Novel L228I and Y232H reverse transcriptase mutations cause NNRTI resistance in combination (AIDS-related complex) |
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical / in vitro | Molecular Pharmaceutics | Nanoparticle-based antiretroviral combinations show synergistic inhibition of cell-free and cell-cell HIV transmission (SIV infection) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022187 | Intelence (Janssen Products LP) | Tablet | Not stated; license cancelled |
| ANDA219152 | Etravirine (Bionpharma Inc.) | Tablet | Not stated; license cancelled |
| ANDA215402 | Etravirine (Carnegie Pharmaceuticals LLC) | Tablet | Not stated; license cancelled |
| ANDA214196 | Etravirine (Amneal Pharmaceuticals NY LLC) | Tablet | Not stated; license cancelled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN graph, not label text): chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease, and peripheral neuropathy.
- **Drug Interactions:** 100 interactions were found. Most of those listed are Moderate. The main ones include:
  - Acid suppressants: rabeprazole, omeprazole, cimetidine (ranitidine is Minor).
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone.
  - Antidiabetics: pioglitazone, saxagliptin, linagliptin, glimepiride, chlorpropamide.
  - Others: clarithromycin, aprepitant, metronidazole, dronabinol, eliglustat, naldemedine, naloxegol.

Please refer to the package insert for warnings and contraindications, as label data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (feline AIDS) has no clinical or literature support, and its mechanistic basis is weak because FIV reverse transcriptase is generally NNRTI-resistant. The strongest-scoring alternatives (congenital HIV, AIDS-related complex) are extensions of the existing HIV indication rather than new uses. All four US licenses are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- In vitro activity data of etravirine against FIV reverse transcriptase before any further consideration
- Confirmation of why the US licenses were cancelled (commercial or safety reasons)
- If an HIV-related extension is of interest, controlled efficacy data for the perinatal and pediatric setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

