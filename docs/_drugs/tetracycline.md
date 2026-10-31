---
layout: default
title: Tetracycline
parent: Model Prediction Only (L5)
nav_order: 1219
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "TETRACYCLINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
description: "Tetracycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tetracycline
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

## Tetracycline: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Tetracycline is a broad-spectrum antibiotic originally used for infections such as urinary tract infection, bronchitis, acne, gonorrhea, pneumonia and conjunctivitis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but currently **0 clinical trials** and only **1 publication** (a case report) support this direction, so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | at least 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tetracycline is a member of the tetracycline class of antibiotics, its efficacy in bacterial conjunctivitis and other infections is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

Tetracycline is already used for chlamydial and other bacterial conjunctivitis, and its activity against *Chlamydia trachomatis* is plausibly relevant to keratoconjunctival disease. Tetracyclines are also reported to have anti-inflammatory and matrix metalloproteinase (MMP) inhibiting effects that could help ocular surface inflammation.

However, the only retrieved paper describes persistent punctate keratitis that appeared *after* chlamydial conjunctivitis had been treated with tetracycline or doxycycline. This is indirect evidence and does not test tetracycline as a treatment for this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the existing conjunctivitis indications, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients with chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline had follicles resolve, but later developed recurrent bilateral punctate epithelial keratitis. Indirect evidence only. |

## US Market Information

The drug is marketed in the United States, with 7 valid licenses. The data compiled for this report contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050278 | Tetracycline hydrochloride (Heritage/Avet) | Capsule | Not available |
| ANDA062752 | Tetracycline hydrochloride (Heritage/Avet) | Capsule | Not available |
| ANDA210674 | Tetracycline hydrochloride (Amneal) | Capsule | Not available |
| ANDA210662 | Tetracycline hydrochloride (Breckenridge) | Capsule | Not available |
| ANDA061837 | Tetracycline hydrochloride (Preferred Pharmaceuticals) | Capsule | Not available |

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver failure and liver disease, kidney disease/kidney failure, uremia, glomerulonephritis, epilepsy, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, gout, peripheral neuropathy, blood coagulation disease, *Clostridium difficile* colitis, G6PD deficiency, respiratory failure, atrial fibrillation, atrioventricular block, and others. These are graph-derived signals and need verification against the package insert.
- **Drug Interactions** (100 interactions recorded; selected examples):
  - **Major**: isotretinoin, acitretin, aminolevulinic acid
  - **Moderate**: ethinylestradiol, amoxicillin, ampicillin, aluminum hydroxide, bismuth subcitrate potassium, aminophylline, atracurium, atovaquone, balsalazide, sodium citrate, asparaginase (*E. coli* and *Erwinia*), attapulgite, topical aminolevulinic acid
  - **Minor**: acetazolamide, hydrochlorothiazide, amiloride

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on one indirect case report and no registered trials. The high TxGNN score (deep learning model) may reflect similarities the model learned between related diseases, such as the existing conjunctivitis indications, not biological evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data
- Direct clinical evidence (controlled studies) of tetracycline for punctate epithelial keratoconjunctivitis
- Evaluation of the ocular route and formulation, since only oral and other non-ocular forms appear in the license records
- A comparison with other tetracycline-class agents such as doxycycline, which have more supporting data

---

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Summary |
|------|------|------|------|------|------|
| 2 | Chronic ethmoidal sinusitis | 0.9915 | L5 | Hold | Only an in vitro antibiotic susceptibility study; no clinical efficacy data. Streptococcal resistance limits reliability. |
| 3 | Chronic rhinosinusitis | 0.9915 | L5 | Research Question | Strongest of the four: a 2016 Cochrane review, a 2020 review, and a 2023 meta-analysis of doxycycline, plus a 2026 omadacycline case series. The evidence concerns other tetracycline-class agents rather than tetracycline itself, benefit is modest and heterogeneous, and resistance raises stewardship concerns. |
| 4 | Paranasal sinus neoplasm | 0.9910 | L5 | Hold | No trials or literature; the rationale is speculative. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

