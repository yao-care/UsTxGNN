---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic Bacterial and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial used against anaerobic bacterial and protozoal infections such as amebiasis and trichomoniasis. The TxGNN model predicts it may be effective for **Pneumocystosis** with a very high score, but **no clinical trial** and **no publication** actually tests metronidazole for this disease. The prediction is best read as a likely model artifact and should not be pursued without new evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial and protozoal infections (approved-indication text is not provided in the source data; this is inferred from the literature) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are all ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available. From general pharmacology, metronidazole is activated in anaerobic organisms into nitro radicals that damage DNA. This explains its activity against anaerobic bacteria and protozoa.

Pneumocystis is a fungus and lacks this activation pathway. Standard therapy is trimethoprim-sulfamethoxazole (TMP-SMX), and the retrieved literature confirms this (PMID 7355683). The mechanistic link is therefore not credible.

The very high TxGNN score most likely reflects the graph structure. Metronidazole shares antiparasitic and anti-infective neighbors with drugs that treat pneumocystosis, so the model links them. It does not reflect a real pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

The search returned 24 registered studies, but all were judged unrelated or had no relevance assessment. They cover primary care payment models, dementia care, depression apps, diabetes management and similar topics. None tests metronidazole or studies pneumocystosis.

---

## Literature Evidence

None of the retrieved publications shows that metronidazole works against pneumocystosis. They are general reviews or case reports in which metronidazole is mentioned incidentally.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Drug-of-choice list: metronidazole for amebiasis and trichomoniasis, TMP-SMX for pneumocystis pneumonia |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | General overview of antiparasitic agents, resistance and toxicity |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale of US antiprotozoal regimens |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | HIV-related opportunistic infections and guideline updates |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Infectious complications of AIDS, with Pneumocystis pneumonia the most common |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Drugs used against protozoan infections (no abstract available) |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Healthy adult who developed Pneumocystis and CMV pneumonia after metronidazole and tetracycline for diarrhea |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; amebic dysentery responded to metronidazole, but Pneumocystis pneumonia occurred separately |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | AIDS patient with amebic colitis and CMV, with no metronidazole efficacy data for Pneumocystis |

---

## US Market Information

Of the 20 registered licenses, 5 main ones are shown. The source data does not include approved-indication text for these entries.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076408 | Metronidazole | Cream | Fougera Pharmaceuticals, LLC |
| ANDA205245 | Metronidazole | Tablet | NuCare Pharmaceuticals, Inc. |
| ANDA205245 | Metronidazole | Tablet | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA079067 | Metronidazole | Tablet | AvPAK |
| ANDA203458 | Metronidazole | Tablet, film coated | Redpharm Drug |

Other marketed forms include capsule, gel, injection solution and suspension.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pneumocystosis prediction rests on model score alone (L5). Pneumocystis is a fungus that metronidazole does not target, standard therapy is TMP-SMX, and no trial or publication supports efficacy. The 99.99% score is very likely a graph-topology artifact.

Among the other predictions in this pack, only **cap polyposis** and **ulceration of vulva** have a plausible, evidence-supported mechanism. Both remain research questions and rest mainly on case reports.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence of metronidazole activity against Pneumocystis (none currently exists)
- Package insert warnings and contraindications from the FDA label (currently missing and blocking safety screening)
- Mechanism-of-action data from DrugBank
- If the team wants to prioritize this drug, redirect effort to cap polyposis or the etiology-specific vulvar ulceration indication, starting with a prospective controlled study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

