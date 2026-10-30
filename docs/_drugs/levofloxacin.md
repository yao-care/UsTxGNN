---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal and staphylococcal infections…"
monitor_inn: "LEVOFLOXACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as pneumonia, sinusitis, pyelonephritis, anthrax and bacterial conjunctivitis.
The TxGNN model ranks **punctate epithelial keratoconjunctivitis** as its top prediction (score 0.9992), but there are **0 clinical trials** and only **1 publication** (an outbreak report that does not support efficacy), so the prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal and staphylococcal infections, bacterial pneumonia, anthrax, maxillary sinusitis, conjunctivitis, pyelonephritis, and others) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | 11 (all ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Levofloxacin is known to be a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial conjunctivitis is already established, so activity on the ocular surface is plausible.

However, the connection is weak. The only retrieved paper describes an outbreak of microsporidial keratoconjunctivitis linked to swimming pool water in Taiwan. Microsporidia are not susceptible to fluoroquinolones, so this paper does not support efficacy. The very high TxGNN score is a model output only and has no clinical backing.

## Other Predictions Reviewed

Ten predictions were screened. Most have no usable evidence. The ones with some literature are summarized below.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 7 | Monoclonal gammopathy | 0.9981 | L5 | Strongest literature, but it concerns infection prophylaxis in myeloma, not the gammopathy itself. Research question. |
| 9 | Septicemic plague | 0.9980 | L5 | Strong mechanism and animal data, but already label-adjacent rather than true repurposing. Research question. |
| 5 | Blood group incompatibility | 0.9985 | L5 | One case report on an infectious complication. Indirect. |
| 2, 3, 4, 6, 8, 10 | Polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, premalignant hematological disease, hematological disease with acquired peripheral neuropathy, congenital hematological disorder | 99.72–0.9990 | L5 | No plausible mechanism and no evidence. Rank 8 conflicts with the known fluoroquinolone neuropathy warning, and rank 3 conflicts with the rare link to pancreatitis. |

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication.

For monoclonal gammopathy, the multicentre, double-blind, placebo-controlled Phase 3 TEAMM trial ([PMID 31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/)) tested levofloxacin prophylaxis in newly diagnosed myeloma. It addressed myeloma infection prevention, not monoclonal gammopathy as a disease, so it is treated as indirect evidence.

## Literature Evidence

**Punctate epithelial keratoconjunctivitis (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Microsporidial keratoconjunctivitis outbreak from swimming pool water in Taiwan. Does not support levofloxacin efficacy. |

**Selected indirect evidence (monoclonal gammopathy / myeloma)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT | Lancet Oncol | TEAMM: levofloxacin prophylaxis in newly diagnosed myeloma, reporting fewer febrile episodes and deaths in the first 12 weeks. |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT summary | Health Technol Assess | Health technology assessment report of the TEAMM trial. |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Supportive care in myeloma, including infection management. |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transpl Infect Dis | Infectious complications after autologous transplant in myeloma, with or without levofloxacin prophylaxis. |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Cohort | Clin Transplant | Ciprofloxacin vs levofloxacin prophylaxis in transplant patients with myeloma (297 patients). |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biol Blood Marrow Transplant | Levofloxacin prophylaxis and bloodstream infection or fever in neutropenic myeloma patients. |

**Selected indirect evidence (septicemic plague)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal (primate) | PLoS Negl Trop Dis | Levofloxacin cured experimental pneumonic plague in African green monkeys. |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal (primate) | Clin Infect Dis | Effect of delaying treatment on ciprofloxacin and levofloxacin efficacy in pneumonic plague. |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review | Clin Infect Dis | African green monkey model and FDA approval of antimicrobials under the Animal Rule. |
| [21574421](https://pubmed.ncbi.nlm.nih.gov/21574421/) | 2010 | Animal (mouse) | Antibiot Khimioter | Lack of efficacy against nalidixic acid-resistant Y. pestis mutants. |

## US Market Information

All 11 listed authorizations are generic applications with a cancelled status. Approved indication text was not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA077652 | Levofloxacin | Film-coated tablet | Coupler LLC | Valid |
| ANDA202801 | Levofloxacin | Film-coated tablet | A-S Medication Solutions | Valid |
| ANDA076710 | Levofloxacin | Film-coated tablet | Northwind Health Company, LLC | Valid |
| ANDA076890 | Levofloxacin | Tablet | Chartwell RX, LLC | Valid |
| ANDA090343 | Levofloxacin | Injection, solution | WG Critical Care, LLC | Valid |

Six further authorizations (oral solution, tablets and injections from Hikma, Macleods, Lannett, Gland, Eugia and PD-Rx) are also cancelled.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
Long QT syndrome, torsades de pointes, epilepsy, liver disease, tendinitis, peripheral neuropathy, myasthenia gravis, diabetes mellitus, rhabdomyolysis, Clostridium difficile colitis, impaired renal function, thrombocytopenia, leukopenia, pancytopenia, and coronary artery disease, among others.

**Drug Interactions:** 100 interactions were found. Major-level examples are:
- Tramadol
- Hydrocortisone

Moderate-level examples include abiraterone, acarbose, famotidine, formoterol, ketorolac, ibuprofen, metformin, pioglitazone and alfuzosin.

Please refer to the package insert for official warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, and its only paper concerns a microsporidial outbreak against which fluoroquinolones are not active. The high TxGNN score has no clinical support. Of the other predictions, monoclonal gammopathy (via myeloma infection prophylaxis) and septicemic plague are worth follow-up as research questions at L4. The plague indication is already label-adjacent rather than true repurposing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking for safety screening)
- Mechanism of action data
- For keratoconjunctivitis: evidence of activity against the relevant pathogens, or a clearly defined bacterial subtype, before any further work
- For monoclonal gammopathy: studies in MGUS or smoldering disease, with benefit-risk analysis covering resistance, C. difficile, tendinopathy and QT risk
- Route compatibility assessment (for ocular use, an ophthalmic formulation would be needed; none is in the data compiled)
- Clarification of the cancelled market status of all listed authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

