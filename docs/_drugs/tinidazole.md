---
layout: default
title: Tinidazole
parent: Model Prediction Only (L5)
nav_order: 1229
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "TINIDAZOLE"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "apocrine adenosis of breast", "blunt duct adenosis of breast", "congenital human immunodeficiency virus", "AIDS related complex", "benign mammary dysplasia"]
description: "Tinidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tinidazole
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

## Tinidazole: Postmenopausal atrophic vaginitis
{: .text-alpha }

## One-Sentence Summary

Tinidazole is an oral 5-nitroimidazole antimicrobial, originally used for protozoal and anaerobic infections such as giardiasis, amoebiasis, trichomoniasis and bacterial vaginosis.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of FDA Applications | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tinidazole belongs to the 5-nitroimidazole class of antimicrobials. Its efficacy in infectious vaginitis and bacterial vaginosis is established.

The prediction is probably not mechanistically grounded. Atrophic vaginitis after menopause is caused by estrogen deficiency, not infection, so an antimicrobial offers no clear rationale. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as such until proven otherwise.

Other top-ranked predictions show a similar pattern. Ulceration of vulva and vulvar neoplasm follow the same anatomical-proximity logic. Several benign breast conditions have no plausible microbial driver. The AIDS-related predictions have only indirect relevance, through treatment of co-infections.

## Clinical Trial Evidence

Currently no related clinical trials registered for postmenopausal atrophic vaginitis.

For reference, one trial was found for a lower-ranked prediction (AIDS):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03412071](https://clinicaltrials.gov/study/NCT03412071) | NA | Unknown | 125 | Pilot study of four antimicrobial products (three topical, one systemic) on the foreskin microbiome and HIV susceptibility in Ugandan men. Tinidazole's role is not shown in the data, and the trial does not test treatment of AIDS. |

## Literature Evidence

Currently no related literature available for postmenopausal atrophic vaginitis.

The following publications were found for the lower-ranked AIDS prediction. They concern tinidazole in infections that commonly occur in people with HIV, not HIV outcomes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21931875](https://pubmed.ncbi.nlm.nih.gov/21931875/) | 2011 | Cohort | PLoS Negl Trop Dis | Retrospective analysis of 170 HIV-1-infected Japanese men with invasive amebiasis: clinical features and response to therapy |
| [31324206](https://pubmed.ncbi.nlm.nih.gov/31324206/) | 2019 | Trial protocol | Trials | Randomized trial protocol on systemic and topical antimicrobials, penile microbiota and HIV susceptibility |
| [34794678](https://pubmed.ncbi.nlm.nih.gov/34794678/) | 2022 | Review | Pediatr Clin North Am | Amebiasis and amebic liver abscess in children, including higher risk in people with HIV |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In vitro study | Microbiol Spectrum | Activity of 5-nitroimidazoles against 94 *T. vaginalis* clinical isolates compared with metronidazole |
| [30789955](https://pubmed.ncbi.nlm.nih.gov/30789955/) | 2019 | Review | PLoS One | Epidemiological and clinical features of amoebic colitis in Barcelona, 2007-2017 |
| [19632225](https://pubmed.ncbi.nlm.nih.gov/19632225/) | 2010 | Review | Exp Parasitol | Treatment options and prospects for new drugs against Cryptosporidium and Giardia |
| [21097745](https://pubmed.ncbi.nlm.nih.gov/21097745/) | 2010 | Case report | Int J STD AIDS | Trichomonas presenting as vulval ulceration, fully resolved with oral tinidazole |
| [16004628](https://pubmed.ncbi.nlm.nih.gov/16004628/) | 2005 | Case series | Int J STD AIDS | High-dose tinidazole plus a broad-spectrum antibiotic and clotrimazole for metronidazole-resistant trichomoniasis (11 cases) |
| [8442923](https://pubmed.ncbi.nlm.nih.gov/8442923/) | 1993 | Clinical study | AIDS | Preliminary study of tinidazole, thiabendazole and cotrimoxazole versus placebo for AIDS diarrhoea in Zambia |
| [33121364](https://pubmed.ncbi.nlm.nih.gov/33121364/) | 2021 | Case report | Int J STD AIDS | Successful tinidazole desensitization and treatment of trichomoniasis in a metronidazole-allergic patient |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021618 | Tinidazole (BioComp Pharma) | Film-coated tablet | Not available; status valid |
| ANDA202044 | Tinidazole (Chartwell RX) | Film-coated tablet | Not available; status valid |
| ANDA202489 | Tindazole (Rising Pharma) | Film-coated tablet | Not available; status valid |
| ANDA203808 | Tinidazole (Edenbridge) | Tablet | Not available; status valid |

All four authorizations on record are valid, and all products are oral.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: epilepsy, neutropenia, agranulocytosis, peripheral nervous system disease and peripheral neuropathy.
- **Drug Interactions**: 100 interactions were found, and the 20 listed are all Moderate. Notable examples include ethanol, amiodarone, capecitabine, paclitaxel, cabazitaxel, bortezomib, brentuximab vedotin, trastuzumab emtansine, ethinylestradiol, estradiol, atorvastatin, levodopa, amobarbital, butalbital and apalutamide.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model support (L5). Atrophic vaginitis is a hormone-deficiency condition with no clear antimicrobial rationale, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature exist, and all four US licenses are valid.

**To proceed, the following is needed:**
- Mechanism of action data and a rationale for a non-infectious indication
- Package insert warnings and contraindications
- Evidence that a microbial or dysbiosis component of atrophic vaginitis responds to tinidazole
- Comparison against standard care (local estrogen therapy)
- Review of the knowledge-graph safety flags (neutropenia, neuropathy, epilepsy) for the target population
- Route and formulation assessment, since a vaginal formulation is not among the listed products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

