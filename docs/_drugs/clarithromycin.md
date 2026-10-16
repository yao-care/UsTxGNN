---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 534
evidence_level: L5
indication_count: 5
monitor_inn: "CLARITHROMYCIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Clarithromycin: From Bacterial Respiratory and Soft-Tissue Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, originally used for respiratory tract and other bacterial infections such as pneumonia, sinusitis and otitis media.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (otitis media, streptococcal and staphylococcal infections, bacterial pneumonia, maxillary sinusitis, Mycoplasma and chlamydial pneumonia). The US license records contain no indication text, so this comes from the knowledge-graph indication list. |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 7 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clarithromycin is a macrolide antibiotic with some immunomodulatory properties, and its efficacy in bacterial respiratory infections is established.

However, no clear mechanistic link was identified between clarithromycin and polyclonal hyperviscosity syndrome, a condition driven by elevated polyclonal immunoglobulins. The high score (99.35%) reflects a graph-based prediction only. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

Other candidates in the prediction list show the same pattern:

- **Hyperamylasemia** (99.35%): a laboratory finding, not a treatment target. The single retrieved paper is a case report of *Mycobacterium abscessus* lung infection with macroamylasemia, which is probably a coincidental association.
- **Congenital analbuminemia** (99.21%): a rare genetic disorder of albumin synthesis, with no pharmacological rationale for a macrolide.
- **Punctate epithelial keratoconjunctivitis** (99.11%): the only plausible indirect link. Macrolides have anti-inflammatory and antibacterial effects and are used in meibomian gland dysfunction and blepharitis. This is a candidate for a research question, not a conclusion.
- **Blood group incompatibility** (99.07%): an alloimmune condition with no established role for clarithromycin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (polyclonal hyperviscosity syndrome).

---

## Literature Evidence

Currently no related literature available for the top predicted indication (polyclonal hyperviscosity syndrome).

For reference, the lower-ranked predictions have very limited literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | *M. abscessus* lung infection in a 76-year-old man, complicated by primary macroamylasemia (relevant to hyperamylasemia, rank 2). Hyperamylasemia appears to be a co-occurring finding, not a treatment outcome. |
| [38472959](https://pubmed.ncbi.nlm.nih.gov/38472959/) | 2024 | Retrospective observational (presumed from title) | Diagnostics (Basel) | Features and treatment outcomes of keratoepitheliopathy in meibomitis-related keratoconjunctivitis, 27 eyes of 18 patients (relevant to punctate epithelial keratoconjunctivitis, rank 4). Whether clarithromycin specifically was studied is unconfirmed. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065489 | Clarithromycin (A-S Medication Solutions) | Tablet, film coated | Not recorded; cancelled |
| ANDA203584 | Clarithromycin (Lannett Company) | Tablet, film coated | Not recorded; cancelled |
| ANDA210459 | Clarithromycin (Alembic Pharmaceuticals) | Tablet, film coated | Not recorded; cancelled |
| ANDA065384 | Clarithromycin (Chartwell RX) | Tablet, film coated | Not recorded; cancelled |
| ANDA065136 | Clarithromycin (PD-Rx Pharmaceuticals) | Tablet | Not recorded; cancelled |

Two further cancelled ANDAs exist: ANDA065283 (Sandoz, for suspension) and ANDA065145 (Actavis, extended-release tablet). All 7 licenses are cancelled, and none is currently valid.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

**Knowledge-graph contraindication signals** (these come from a drug-disease graph, not from label text, and need verification against the label):
- **Cardiac rhythm:** long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic polymorphic and incessant infant forms)
- **Liver and biliary:** liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease
- **Metabolic:** porphyria (including inherited porphyria and porphyrin metabolism disease)
- **Kidney and urinary:** kidney disease, pyoureter
- **Neuromuscular:** myasthenia gravis (including adult-onset), neuromuscular junction disease
- **Gastrointestinal:** *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- **Bone:** osteoporosis, postmenopausal osteoporosis, bone fracture
- **Infectious:** infectious mononucleosis, chronic Epstein-Barr virus infection syndrome

**Drug Interactions:** The interaction query returned 100 records, of which 20 were reviewed. Notable examples:
- **Major:** abemaciclib, fentanyl, acalabrutinib
- **Moderate:** abametapir (topical), abiraterone, paclitaxel, acarbose, tramadol, famotidine, formoterol, nifedipine, adenosine, trastuzumab emtansine, flunisolide, afatinib, ethinylestradiol, hydrocortisone
- **Minor:** dolutegravir, zidovudine, loratadine

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction has no clinical trials, no literature and no identified mechanistic link, so it rests on model output alone (Evidence Level L5).
- Across all five predictions, only punctate epithelial keratoconjunctivitis shows a plausible indirect rationale, and it is a research question rather than an actionable candidate.
- All US licenses are cancelled, and label safety data are missing, so a safety screen cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, obtained by downloading and parsing the FDA label (currently a blocking gap)
- Mechanism of action data from DrugBank, to support a mechanistic-link analysis
- A targeted literature search for macrolide use in polyclonal hyperviscosity syndrome, and a review of whether clarithromycin was studied in meibomitis-related keratoconjunctivitis
- Verification of the knowledge-graph contraindications (especially QT prolongation and the CYP3A4-related interactions) against the label
- Consideration of whether punctate epithelial keratoconjunctivitis should be pursued as a separate research question, since its evidence is stronger than that of the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

