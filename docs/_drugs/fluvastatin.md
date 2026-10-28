---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 6
monitor_inn: "FLUVASTATIN"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "fibroma of prostate"]
last_modified_at: 2026-10-28
description: "Fluvastatin: predicted new indication HIV infectious disease (evidence level L5). Approved use: Arteriosclerosis disorder, atherosclerosis…"
---

# Fluvastatin
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

## Fluvastatin: From Atherosclerosis and Familial Combined Hyperlipidemia to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Fluvastatin is a statin (HMG-CoA reductase inhibitor).
The TxGNN model predicts it may be relevant to **HIV infectious disease**, but **no clinical trials** are registered for this use, and the **13 publications** found mostly concern managing lipid problems in people with HIV, not treating HIV itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arteriosclerosis disorder, atherosclerosis, familial combined hyperlipidemia (relations recorded in the knowledge graph; the US licence records provide no indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Number of Approvals | 1 NDA and 4 ANDAs (5 in total) |
| Recommended Decision | Hold |

The evidence level is L5 because no cited study directly examines fluvastatin as a treatment for HIV infection itself. The studies address lipid lowering in people with HIV, drug interactions, HCV co-infection, and a mouse kidney model.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fluvastatin is known to belong to the statin class, which lowers cholesterol by inhibiting HMG-CoA reductase.

Fluvastatin is not an antiviral agent. The literature compiled for this report suggests the link to HIV is indirect:

- **Lipid management in HIV:** Antiretroviral therapy, especially protease inhibitors, often causes dyslipidemia. Fluvastatin is mainly metabolized through CYP2C9 rather than CYP3A4, so it is considered to interact less with protease inhibitors than some other statins. That makes it a reasonable lipid-lowering option in this population, which is an extension of its original use.
- **Possible secondary effects:** Statins have anti-inflammatory and immunomodulatory properties. A cohort study examined statin use and inflammation markers in people with HIV, and a mouse study suggested fluvastatin protects kidney podocytes in HIV-associated nephropathy. Both are indirect and not evidence of treating the infection.

The very high TxGNN score is best read as a computational association, not proof of antiviral benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | Open-label randomized controlled study | J Antimicrob Chemother | Tested fluvastatin as an add-on to pegylated interferon and ribavirin in HIV/HCV genotype 1 co-infected patients; targets HCV, not HIV |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | Clinical study | Infection | Compared fluvastatin and pravastatin for lipid lowering in HIV patients on antiretroviral therapy, including interaction with indinavir |
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | Clinical study | AIDS | Efficacy and safety of fluvastatin in hyperlipidemic HIV patients treated with protease inhibitors |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | Randomized clinical study | AIDS | In 20 HIV patients, fluvastatin 80 mg/day lowered LDL-cholesterol by 24%, similar to ezetimibe (20%); the focus was ezetimibe |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | Cohort | AIDS Res Hum Retroviruses | Association of statin use with inflammation and immune-activation markers in HIV patients on effective antiretroviral therapy |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | Pilot study | J Viral Hepat | Examined whether fluvastatin affects HCV replication in HIV/HCV co-infected patients |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Review | Clin Pharmacokinet | Reviews drug-drug interactions between statins and antiviral protease inhibitors |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Review | AIDS | Role of statins and fibrates for hyperlipidemia in HIV patients on HAART |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | Preclinical (mouse model) | Nephrol Dial Transplant | Fluvastatin prevented podocyte injury in a mouse model of HIV-associated nephropathy |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | Randomized trial | AIDS | Rosuvastatin vs pravastatin in dyslipidemic HIV patients; fluvastatin was not studied (indirect) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021192 | Lescol (Sandoz Inc) | Tablet, extended release | Not stated in the data compiled |
| ANDA078407 | Fluvastatin (Teva Pharmaceuticals USA, Inc.) | Capsule | Not stated in the data compiled |
| ANDA090595 | Fluvastatin Sodium (Mylan Pharmaceuticals Inc.) | Capsule | Not stated in the data compiled |
| ANDA079011 | Fluvastatin Sodium (Teva Pharmaceuticals USA, Inc.) | Tablet, film coated, extended release | Not stated in the data compiled |
| ANDA209397 | Fluvastatin Sodium (Lannett Company, Inc.) | Tablet, film coated, extended release | Not stated in the data compiled |

All five records are single-ingredient products. All forms are oral.

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, and injury.
- **Drug interactions:** The interaction query returned 100 records. Those listed as Moderate include aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, glyburide and pectin. Combining fluvastatin with other statins is a notable concern. Interactions with antiretroviral protease inhibitors are discussed in the literature above and should be reviewed for any HIV use.

Please refer to the package insert for label warnings, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no clinical trial or publication tests fluvastatin as a treatment for HIV infection. The literature supports only its use for lipid management in people with HIV, which is a related comorbidity, not the predicted indication. The other predictions (CETP deficiency, a rare neurodevelopmental disorder, feline and simian immunodeficiency, and prostatic fibroma) have no supporting evidence at all.

**To proceed, the following is needed:**
- Preclinical evidence of an antiviral or immunomodulatory effect on HIV itself
- Clarification of whether the intended goal is HIV treatment or lipid and inflammation management in people with HIV
- FDA package insert warnings and contraindications
- Detailed mechanism of action data
- A review of interactions with antiretroviral regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

