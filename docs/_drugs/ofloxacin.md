---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 984
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (typhoid fever, salmonellosis…"
monitor_inn: "OFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
---

# Ofloxacin
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

## Ofloxacin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic, originally used to treat bacterial infections such as typhoid fever, urinary tract infection, bronchitis, and bacterial pneumonia.
The TxGNN model gives its top prediction, **hyperamylasemia**, a very high score, but there are **0 clinical trials** and **0 publications** supporting it.
The prediction rests on the model alone. The only predicted indication with meaningful supporting data is **septicemic plague** (preclinical studies only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (typhoid fever, salmonellosis, urinary tract infection, bronchitis, bacterial pneumonia, and others) |
| Predicted New Indication | Hyperamylasemia (top-ranked prediction) |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of FDA Applications | 12 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ofloxacin is a fluoroquinolone antibacterial, and this class is generally known to inhibit bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is established.

For hyperamylasemia, **no plausible mechanistic link** was identified. An antibacterial mechanism has no obvious bearing on elevated serum amylase. The high score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Other top-ranked predictions (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant and congenital hematological conditions) show the same pattern: high scores, no trials, and no mechanistic rationale.

Among the ten predictions, the most biologically coherent is **septicemic plague** (rank 8). Ofloxacin is active in vitro against *Yersinia pestis* and has shown efficacy in mouse models of experimental plague. This extends its existing antibacterial use to a related pathogen rather than introducing a new mechanism. The evidence is preclinical, with no human trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia or for any of the other nine predicted indications.

---

## Literature Evidence

No literature was found for hyperamylasemia, the top-ranked prediction.

For reference, the best-supported prediction is septicemic plague. All of these studies are preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Among 78 *Y. pestis* strains, ofloxacin was among the most active agents, behind ceftriaxone and ciprofloxacin |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Ofloxacin and levofloxacin were highly active against 100 human *Y. pestis* isolates (MIC90 < 0.03 µg/mL) |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal | Antimicrob Agents Chemother | Ofloxacin was active in a mouse model of systemic *Y. pestis* infection, compared with beta-lactams, aminoglycosides, and doxycycline |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal | Antimicrob Agents Chemother | Mouse model of pneumonic plague used to compare antibiotic treatments |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal | Antibiot Khimioter | Ofloxacin was effective for prophylaxis and treatment of experimental plague, with lower efficacy against strains lacking fraction I and mouse toxin |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal | Antibiot Khimioter | Fluoroquinolones, including ofloxacin, interfered with vaccine-induced immunity in mice, which supports combining emergency and specific prevention |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Animal | Antibiot Khimioter | Primate model of bubonic plague developed to evaluate antibacterial efficacy |

Several other retrieved papers concern resistance mechanisms or other organisms and are only tangentially relevant.

---

## US Market Information

The drug is marketed in the US, with 12 valid licenses. No approved-indication text is available. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076622 | Ofloxacin | Solution/drops | A-S Medication Solutions |
| ANDA217904 | Ofloxacin | Solution | Leading Pharma, LLC |
| ANDA091656 | Ofloxacin | Coated tablet | Nivagen Pharmaceuticals, Inc. |
| ANDA076527 | Ofloxacin Otic | Solution | Bryant Ranch Prepack |
| ANDA211525 | Ofloxacin | Solution | A-S Medication Solutions |

---

## Safety Considerations

No label warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

- **Contraindication signals from the knowledge graph (not label text)**: These include long QT syndrome, torsades de pointes, liver failure and liver disease, epilepsy, kidney disease and impaired renal function, myasthenia gravis, tendinitis, peripheral neuropathy, diabetes mellitus and diabetic ketoacidosis, rhabdomyolysis, thrombocytopenia, leukopenia, anemia, *Clostridium difficile* colitis, and drug-induced liver injury.
- **Drug interactions**: The interaction search returned 100 entries. Major interactions in the displayed sample include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), bupropion, and chlorpropamide. Moderate interactions include antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, aspirin, and calcium and potassium salts.

The knowledge-graph contraindication of peripheral neuropathy argues against the prediction for hematological disease associated with acquired peripheral neuropathy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hyperamylasemia, has no clinical trials, no literature, and no plausible mechanistic link. The drug is marketed in the US with 12 valid licenses, and the label safety data are missing. Of the ten predictions, only septicemic plague has biologically coherent preclinical support (L4), and that remains a research question rather than a development-ready indication.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For hyperamylasemia, a mechanistic hypothesis and any clinical or observational data. Without them, the prediction should not advance.
- For septicemic plague, a review of current guideline-recommended therapies and of any human data
- Clarification of current US regulatory and market status, since the drug is marketed with 12 valid licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

