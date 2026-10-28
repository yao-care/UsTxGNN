---
layout: default
title: Bismuth Subsalicylate
parent: Model Prediction Only (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
monitor_inn: "BISMUTH SUBSALICYLATE"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "salmonellosis", "typhoid fever", "conjunctivitis", "relapsing fever", "acute contagious conjunctivitis", "gingivitis", "punctate epithelial keratoconjunctivitis", "otitis externa"]
last_modified_at: 2026-10-28
description: "Bismuth Subsalicylate: predicted new indication Paratyphoid fever (evidence level L5). Approved use: Diarrheal disease, dyspepsia"
---

# Bismuth Subsalicylate
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

## Bismuth Subsalicylate: From Diarrheal Disease and Dyspepsia to Paratyphoid Fever
{: .text-alpha }

## One-Sentence Summary

Bismuth subsalicylate was originally used to treat diarrheal disease and dyspepsia.
The TxGNN model predicts it may be effective for **paratyphoid fever**, but **no clinical trials and no publications** currently support this specific prediction.
The data compiled for this report show the strongest (still only indirect) support for two lower-ranked predictions, **salmonellosis** and **gingivitis**, which are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dyspepsia (the license records contain no approved indication text) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bismuth subsalicylate is a poorly soluble compound widely used for gastrointestinal disorders. A laboratory study found that it binds diverse bacteria and subsequently kills them, and reviews describe it as an antisecretory agent that reduces stool number by about 50% in acute diarrhea.

A plausible link to paratyphoid fever is its antibacterial and anti-secretory action against enteric *Salmonella*. However, this reasoning is inferred from its use in diarrheal disease and is not supported by any data on paratyphoid fever. Paratyphoid fever is a systemic infection, and a gut-acting, minimally absorbed agent would not be expected to treat it adequately. The very high score is therefore best read as a model signal, not as evidence of efficacy.

Other predictions fall into three groups:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Salmonellosis | 0.9995 | L5 | In vitro bacterial killing plus older reviews and a veterinary study; no human trials |
| Gingivitis | 0.9975 | L5 | Preclinical dental antibacterial work and two 1946 historical reports; no modern trials |
| Diffuse scleroderma, typhoid fever, conjunctivitis, relapsing fever, acute contagious conjunctivitis, punctate epithelial keratoconjunctivitis, otitis externa | 0.9968–0.9996 | L5 | Prediction only; no supporting data and weak or speculative mechanistic links |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for paratyphoid fever. The table below lists the most relevant publications for the closest supported prediction, **salmonellosis**. These are indirect and none is a trial in salmonellosis patients.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2694949](https://pubmed.ncbi.nlm.nih.gov/2694949/) | 1989 | In vitro | Antimicrob Agents Chemother | Bismuth subsalicylate bound diverse bacteria and killed them; a 4-log10 reduction of *E. coli* occurred within 4 hours |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Describes bismuth subsalicylate as an antisecretory agent that reduces stool number by about 50% in acute diarrhea |
| [2655632](https://pubmed.ncbi.nlm.nih.gov/2655632/) | 1989 | Review | Annu Rev Public Health | General review of diarrheal disease control |
| [1760758](https://pubmed.ncbi.nlm.nih.gov/1760758/) | 1991 | Veterinary review | Vet Clin North Am Food Anim Pract | Treatment of neonatal calf diarrhea; antisecretory agents including bismuth subsalicylate are discussed |

For **gingivitis** (second supported prediction), the literature is preclinical or historical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28837052](https://pubmed.ncbi.nlm.nih.gov/28837052/) | 2017 | Preclinical (in vitro) | Nanotechnology | Bismuth subsalicylate nanoparticles showed antibacterial activity against oral anaerobic bacteria |
| [34038883](https://pubmed.ncbi.nlm.nih.gov/34038883/) | 2021 | Preclinical (biomaterial) | Biomed Mater | Bismuth subsalicylate incorporated into electrospun membranes to prevent bacterial colonization in periodontal therapy |
| [20994674](https://pubmed.ncbi.nlm.nih.gov/20994674/) | 1946 | Historical report | Eye Ear Nose Throat Mon | Bismuth subsalicylate in oil described as the treatment of choice in Vincent's angina |
| [21012833](https://pubmed.ncbi.nlm.nih.gov/21012833/) | 1946 | Historical report | Illinois Med J | Same author and topic as above |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M001 | Stomach | Liquid | Not specified (valid) |
| M008 | Stomach Relief | Liquid | Not specified (valid) |
| M002 | GNP Pink Bismuth | Chewable tablet | Not specified (valid) |

The drug is marketed in the US, and all three authorizations are valid.

## Safety Considerations

- **Contraindications (reported associations, not label text)**: The drug is associated with liver failure, liver disease, kidney disease, gallbladder disease, epilepsy, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, gout, peripheral neuropathy and other peripheral nervous system disease, blood coagulation disease, brain disease, non-infectious meningitis, substance abuse/dependence, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and pyoureter. These should be verified against official labeling.
- **Drug Interactions**: 64 interactions were identified, all in the moderate category among those listed. The main groups are:
  - Tetracycline antibiotics (doxycycline, tetracycline, minocycline)
  - Antidiabetic agents, including sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide), meglitinides (repaglinide, nateglinide) and many insulins (aspart, degludec, detemir, glargine, glulisine, human isophane/regular/inhaled)
  - Morphine and fenfluramine

Label-based warnings were not available for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, paratyphoid fever, rests on model score alone (L5) with no trials or literature, and a non-absorbed gut-acting agent is unlikely to treat a systemic infection. The drug is marketed in the US with three valid authorizations, and label safety data are missing. Salmonellosis and gingivitis are worth treating as research questions (L4), but their support is limited to in vitro, veterinary, and historical sources.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Human clinical data for enteric infections such as salmonellosis, and for any systemic enteric fever, before further investment
- For gingivitis, modern controlled studies and a suitable topical or oral-care formulation
- Confirmation of the contraindication signals listed above against official labeling
- Confirmation of current US regulatory status, given that the drug is marketed with three valid authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

