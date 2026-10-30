---
layout: default
title: Procaine
parent: Moderate Evidence (L3-L4)
nav_order: 1086
evidence_level: L4
indication_count: 10
monitor_inn: "PROCAINE"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa"]
last_modified_at: 2026-10-30
description: "Procaine: predicted new indication Methemoglobinemia (evidence level L4). Approved use: Local anaesthesia (e.g., dental surgery)"
---

# Procaine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Procaine: From Local Anaesthesia to Methemoglobinemia
{: .text-alpha }

## One-Sentence Summary

Procaine is a local anaesthetic (an ester-type "caine") that has been used for infiltration and nerve block, for example in dental surgery.
The TxGNN model predicts it may be effective for **methemoglobinemia**, but there are **no registered clinical trials** and only **5 publications**, and these mostly describe procaine as a *cause* of methemoglobinemia rather than a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (e.g., dental surgery); no approved indication text is listed in the US licence data |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L4 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on pharmacology records, procaine is a local anaesthetic that is thought to act on ryanodine receptors (RYR1 and RYR2), although no publicly available bioactivity data confirm a primary target. Its general anaesthetic effect is commonly attributed to sodium-channel blockade.

The prediction itself is hard to justify mechanistically. The available literature shows that procaine and related local anesthetics (such as lignocaine) are more likely to **induce** methemoglobinemia than to treat it. This includes a case report of methemoglobinemia after intravenous procaine (1970) and a case report following lignocaine (1965). The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a therapeutic relationship. Using procaine for this condition could worsen it.

Other predictions in the list point the same way. Alpha-type methemoglobinemia and methemoglobin reductase deficiency are closely related conditions in which the same safety concern applies. Predictions with some indirect supporting literature, such as fibromyalgia (trigger-point or intradermal injection) and tendinitis (a 2022 neural therapy study in supraspinatus tendinopathy), are mechanistically more plausible and could be considered research questions instead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report | Acta physiologica latino americana | Methemoglobinemia due to intravenous procaine (an adverse event, not a treatment) |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report | Lancet | Methemoglobinemia following lignocaine, a related local anaesthetic |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of the rational use of local anaesthetics |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Other | Zhonghua Wai Ke Za Zhi | Clinical observation of methemoglobin levels during intravenous procaine anaesthesia |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Other | Am J Obstet Gynecol | Placental passage of procaine and para-aminobenzoic acid (not related to treatment) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M017 | TXTK NUMB | Ointment | Not specified (valid) |
| NDA050138 | BICILLIN C-R 900/300 | Injection, suspension | Not specified (valid) |

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** These are drug-disease contraindication links, not package-insert wording. They include:
  - Cardiac and conduction conditions: long QT syndrome (including familial), torsades de pointes, atrioventricular block, cardiovascular and heart disease.
  - Haematological conditions: thrombocytopenia, agranulocytosis, neutropenia (including congenital and cyclic forms).
  - Neuromuscular conditions: myasthenia gravis and neuromuscular junction disease, butyrylcholinesterase deficiency.
  - Organ and other conditions: kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, potassium deficiency, hypotensive disorder, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions (17 records in total):**
  - Major: nitrous acid.
  - Moderate: sulfasalazine and other topical or ophthalmic local anaesthetics (lidocaine, benzocaine, cocaine, tetracaine, oxybuprocaine, cinchocaine).
  - Minor: laronidase, hyaluronidase, doxorubicin (including liposomal).
- **Allergy and adverse reactions (from the literature):** Procaine and procaine penicillin are linked to allergic contact dermatitis, pseudo-anaphylactic reactions (Hoigné's syndrome) and, rarely, anaphylaxis.
- **Methemoglobinemia:** Procaine has been linked to inducing methemoglobinemia, so it is a safety concern for this predicted indication.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature suggests procaine is more likely to cause methemoglobinemia than treat it. There are no clinical trials, the supporting publications are old case reports, and the US licences are all cancelled. The high TxGNN score is not supported by mechanistic or clinical evidence.

**To proceed, the following is needed:**
- A mechanistic rationale showing how procaine could reduce methemoglobin, which is currently implausible given the reports of induction
- Package insert warnings and contraindications for formal safety screening
- Mechanism of action data confirmed from DrugBank
- A decision on whether to shift attention to better-supported predictions, such as tendinitis (the 2022 neural therapy study) and fibromyalgia, which are research questions and would need controlled studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

