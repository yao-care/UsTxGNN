---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 2
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-30
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Not recorded in the local data"
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Colchicine: Microtubule-disrupting agent → Plasmodium falciparum malaria
{: .text-alpha }

## One-Sentence Summary

Colchicine is a microtubule-disrupting agent that is marketed in the United States as oral tablets and capsules. The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but the data compiled for this report contain **0 clinical trials** and only **2 preclinical publications**, neither of which tests colchicine as a malaria treatment. This is a model prediction with a mechanistic rationale only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | at least 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Colchicine is generally known as a microtubule-disrupting agent that binds tubulin and interferes with cell division and cell movement.

The mechanistic link to malaria is a plausible biological idea: if the parasite's tubulin can be targeted, a tubulin binder might slow parasite growth. The two retrieved papers touch on this only indirectly. One studies how curcumin disrupts *P. falciparum* microtubules, and the other studies how the parasite transporter pfmdr1 changes drug susceptibility in mammalian cells. Neither shows that colchicine treats malaria.

A major concern is selectivity. Colchicine has a narrow therapeutic index, and doses needed for antiparasitic activity could cause toxicity in the human host. The high TxGNN score is a computational signal, not proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro / preclinical | PLoS One | Curcumin disrupts microtubules in *P. falciparum*; supports parasite microtubules as a possible target, but does not test colchicine as a treatment |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / preclinical | Mol Cell Biol | Expressing the parasite pfmdr1 gene in mammalian cells increased susceptibility to chloroquine; relates to drug resistance mechanisms, not colchicine efficacy |

## US Market Information

Colchicine is marketed in the United States as single-ingredient oral products in film-coated tablet, tablet and capsule forms, from multiple manufacturers (11 records in the data compiled for this report; the list may be partial). The records carry no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA209470 | Colchicine | Tablet, film coated | Mylan Pharmaceuticals Inc. |
| NDA204820 | Colchicine | Capsule | Hikma Pharmaceuticals USA Inc. |
| ANDA217620 | Colchicine | Capsule | Camber Pharmaceuticals, Inc. |
| ANDA208678 | Colchicine | Capsule | Endo USA, Inc. |
| NDA022352 | Colchicine | Tablet, film coated | Bryant Ranch Prepack |

## Cytotoxicity

Colchicine is an antimitotic agent, but it is not classified as an anticancer drug in the data compiled for this report, so a full cytotoxic-drug profile is not provided. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Contraindication-related conditions (conditions linked to colchicine as contraindicated or to be avoided):** liver failure, impaired renal function, blood disorders (thrombocytopenia, leukopenia, agranulocytosis, neutropenia including congenital forms, aplastic anemia), peptic ulcer disease, muscle disorders (myopathy, rhabdomyolysis, familial periodic paralysis), and diarrheal disease. These are not taken from label text and should be checked against the package insert.
- **Drug Interactions:** 100 interactions were found. Major-level examples include aprepitant, clarithromycin, cobicistat, deferiprone, eliglustat, rolapitant, rosuvastatin and simvastatin. Moderate-level examples include chloroquine (also a malaria drug, so directly relevant to this indication), metronidazole, cimetidine, ticagrelor and disulfiram.

Package insert warnings were not available in the data compiled for this report; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication tests colchicine against *P. falciparum* malaria, so the evidence level is L5 and the case rests on a model score and a speculative tubulin-targeting idea. Colchicine's narrow therapeutic index and its interaction with chloroquine add further concern.

**To proceed, the following is needed:**
- In vitro testing of colchicine against *P. falciparum* (including chloroquine-resistant strains), with selectivity versus human cells
- Mechanism of action data and confirmation of parasite tubulin binding
- Review of the FDA package insert for warnings and contraindications
- A toxicity and dosing assessment showing that antiparasitic exposure is achievable at tolerable doses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

