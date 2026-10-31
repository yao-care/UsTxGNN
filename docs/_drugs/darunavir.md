---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 4
monitor_inn: "DARUNAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-31
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Darunavir: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model's top predictions are veterinary or animal-model retroviral diseases, and the most evidence-supported one is **Simian Immunodeficiency Virus (SIV) Infection**, backed by **0 clinical trials** and **4 preclinical publications** in nonhuman primates. Overall evidence is weak and largely indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (SIV infection); L5 for the other three predictions |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | at least 10 |
| Recommended Decision | Hold |

Note: the four predictions are tied or nearly tied on score. The first two, feline AIDS and SIV infection, both score 0.99969. This report focuses on SIV infection because it is the only one with any literature.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, darunavir is an HIV-1 protease inhibitor. It blocks cleavage of viral polyproteins and prevents the production of mature, infectious virus particles. Its efficacy in HIV/AIDS is established.

SIV is a close lentiviral relative of HIV, and its protease is broadly sensitive to HIV protease inhibitors, so a mechanistic link is plausible. However, SIV is mainly a research model for HIV rather than a distinct human disease. The "new" indication therefore largely overlaps with the existing one and adds little repurposing value.

The other predictions are weaker:
- **Feline AIDS (FIV):** FIV is related to HIV-1, but its protease differs in substrate specificity and inhibitor sensitivity. Nothing in the data shows darunavir activity against it. It is also a veterinary indication, so human development does not apply.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter:** No plausible mechanistic link. This is a rare genetic disorder, and darunavir's CNS penetration is limited.
- **Obsolete familial combined hyperlipidemia:** Protease inhibitors are associated with dyslipidemia as an adverse effect, so therapeutic benefit is unlikely. The term is also obsolete in the ontology.

The high TxGNN scores reflect network proximity to the original HIV/AIDS indication and are not independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All four publications are nonhuman primate (SIV/rhesus macaque) studies of combination antiretroviral therapy (cART). Darunavir is likely part of these regimens, but the available information does not show its individual contribution.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (NHP) | PLoS Pathogens | A highly intensified multidrug ART regimen in SIVmac251-infected macaques induced long-term viral suppression and restricted the viral reservoir |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical (NHP) | AIDS Res Hum Retroviruses | Compared two coformulated injectable cART regimens (including a triple regimen with emtricitabine and tenofovir) for suppressing SIV replication in rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (NHP) | PLoS ONE | Intensive cART plus 3 weeks of the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques, as a model for studying viral reservoirs |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical (NHP) | AIDS | The gold compound auranofin restricted the viral reservoir in the monkey AIDS model and helped contain viral load after ART suspension |

---

## US Market Information

All 10 authorizations listed below are in valid status. The data compiled for this report contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021976 | PREZISTA (Janssen Products LP) | Tablet, film coated | Not available in the data |
| NDA202895 | PREZISTA (Janssen Products LP) | Suspension | Not available in the data |
| ANDA216168 | Darunavir (Camber Pharmaceuticals) | Tablet, film coated | Not available in the data |
| ANDA206288 | Darunavir 600 and 800 mg (Cipla USA) | Tablet | Not available in the data |
| ANDA202073 | Darunavir (Lupin Pharmaceuticals) | Tablet, film coated | Not available in the data |

Five further generic ANDAs (Viona, Amneal, Dr. Reddy's, a second Camber, and NuCare) are also cancelled.

---

## Safety Considerations

No package-insert warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

- **Disease-level contraindication signals (from the knowledge graph, not label text):** liver failure, liver disease, cirrhosis, chronic hepatitis B and C virus infection, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, and hemophilia.
- **Drug Interactions:** 100 interactions were found in total. The 20 retrieved are mostly Moderate. They include:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, albiglutide, chlorpropamide, acetohexamide
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Others: aprepitant, clarithromycin
  - **Major:** cisapride (avoid co-administration)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only supporting literature is four indirect, regimen-level nonhuman primate studies, and there are no clinical trials. SIV infection is a research model rather than a distinct human disease, and the other predictions are veterinary, mechanistically implausible, or obsolete. The drug is marketed, with 10 valid US licenses.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism-of-action data
- Evidence of darunavir's individual contribution in the SIV studies, and any direct data on activity against FIV protease
- A clear definition of the target population and the added value beyond the existing HIV indication
- Clarification of the cancelled US market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

