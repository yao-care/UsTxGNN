---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Anaerobic bacterial infections (e.g., peritonitis, endocarditis…"
monitor_inn: "METRONIDAZOLE"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Metronidazole: From Bacterial and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antibiotic originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis and rosacea.
The TxGNN model predicts it may be effective for **pneumocystosis**, but **no clinical trials** are registered and the **10 retrieved publications** are only reviews and case reports, with none showing that metronidazole treats pneumocystosis.
The model score is very high, but the evidence is weak and the biological rationale is poor.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial infections (e.g., peritonitis, endocarditis, intracranial abscess), giardiasis, bacterial vaginosis, rosacea |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 15 licenses are cancelled) |
| Number of NDAs | 15 (14 ANDAs and 1 NDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Metronidazole is a nitroimidazole that is generally known to act against anaerobic bacteria and protozoa. Its efficacy in anaerobic infections, giardiasis and bacterial vaginosis is established.

The prediction for pneumocystosis is hard to justify mechanistically. *Pneumocystis* is a fungus and lacks the nitroreductase-dependent activation pathway that nitroimidazoles rely on. The very high score most likely reflects the drug's network proximity to antiparasitic and anti-infective drug classes in the knowledge graph, not actual biology. The retrieved literature supports this view: the papers are general reviews of antiparasitic therapy and HIV opportunistic infections, and case reports in which metronidazole was given for a coexisting condition such as amebiasis. Pneumocystis pneumonia is treated with other agents, such as trimethoprim-sulfamethoxazole.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Overview of antiparasitic agents, resistance and toxicity issues |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Drugs of choice: metronidazole for amebiasis and trichomoniasis; trimethoprim-sulfamethoxazole for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic basis of antiprotozoal therapy and US treatment recommendations |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Therapies for infectious complications of AIDS, including Pneumocystis carinii pneumonia |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant in 2015 |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Pneumocystis and CMV pneumonia in a previously healthy adult who had earlier received metronidazole and tetracycline |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | AIDS patients; amebic dysentery treated with metronidazole, later PCP |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Colon perforation with peritonitis in an AIDS patient with CMV and amoebic colitis |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Rep | Streptococcus intermedius cerebellar abscess as first presentation of sarcoidosis |

None of these papers reports metronidazole as a treatment for pneumocystosis.

---

## US Market Information

All licenses below are cancelled; no active US authorization was found.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076408 | Metronidazole (Fougera) | Cream | Not available |
| ANDA205245 | Metronidazole (NuCare) | Tablet | Not available |
| ANDA079067 | Metronidazole (AvPAK) | Tablet | Not available |
| ANDA203458 | Metronidazole (Redpharm Drug) | Tablet, film coated | Not available |
| NDA216755 | LIKMEZ (Saptalis) | Suspension | Not available |

These are 5 of 15 licenses (the others include oral capsules, gels and injectable solutions).

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: liver failure and liver disease, epilepsy, kidney disease, hematologic disease (neutropenia, agranulocytosis, leukopenia, blood coagulation disease), peripheral neuropathy and other nervous system diseases, brain disease, optic nerve disease, congestive heart failure, diabetes mellitus and diabetic ketoacidosis, gout, gallbladder disease, dermatitis, substance abuse/dependence, and others.
- **Drug Interactions**: 100 interactions were found. The most significant is **ethanol (Major)**. Moderate interactions include paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, butalbital, amiodarone, celecoxib, amobarbital and loperamide.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone: there are no clinical trials, no supporting studies, and no plausible mechanism, since *Pneumocystis* is a fungus without the nitroimidazole activation pathway. Established therapies for pneumocystosis already exist.

**Other predictions in this data set:**
- **Cap polyposis** is the best-supported prediction (L4, case reports and small series suggesting remission with metronidazole, possibly through anti-inflammatory action). It is better suited to follow-up as a research question.
- Ulcerative proctosigmoiditis, myiasis and ulceration of vulva (all L4) have indirect support only.
- Nocardiosis, atrophic vaginitis, cryptococcal meningitis, papillary conjunctivitis and punctate epithelial keratoconjunctivitis have no meaningful support.

**To proceed, the following is needed:**
- Mechanism of action data and in vitro activity against *Pneumocystis*, or reprioritization toward cap polyposis
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Clarification of the current US regulatory status, since all listed licenses are cancelled
- Any prospective clinical data before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

