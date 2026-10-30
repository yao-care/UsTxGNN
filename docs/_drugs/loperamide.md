---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "LOPERAMIDE"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "conjunctival folliculosis", "parasitic conjunctivitis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "Angelucci syndrome"]
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Loperamide
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

## Loperamide: Acute contagious conjunctivitis (rank 1); amebic dysentery (acute contagious conjunctivitis)
{: .text-alpha }

## One-Sentence Summary

Loperamide is a peripheral mu-opioid receptor agonist originally used to treat diarrheal disease and dysentery symptoms.
The TxGNN model's top-ranked prediction is **acute contagious conjunctivitis**, but it has **0 clinical trials** and **0 publications**. The best-supported candidate in the top 10 is **amebic dysentery**, with **0 clinical trials** and **2 publications** (a review and a case report), and the case report points to a safety concern rather than a benefit.

> Note: The title uses amebic dysentery, the top-10 prediction with the most relevant literature and a plausible link to the original indication. The detailed tables below follow the rank-1 prediction (acute contagious conjunctivitis), as specified by the report format, and the other predictions are summarized afterward.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute contagious conjunctivitis (rank 1); amebic dysentery (acute contagious conjunctivitis) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (acute contagious conjunctivitis); L4 (amebic dysentery) |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, loperamide is a peripheral mu-opioid receptor agonist that slows gut motility. Its efficacy in diarrheal disease is established.

**Acute contagious conjunctivitis (rank 1):** There is no credible mechanism. Loperamide acts on the gut, and opioid receptors in the cornea do not support an anti-infective or anti-inflammatory role in an infectious ocular surface disease. The high score (0.9997) comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, not biological evidence or pharmacology. The same applies to conjunctivitis (rank 3), pseudomembranous conjunctivitis (rank 5), conjunctival folliculosis (rank 6), parasitic conjunctivitis (rank 7), chronic follicular conjunctivitis (rank 8), serous conjunctivitis except viral (rank 9) and Angelucci syndrome (rank 10). Ranks 6 to 9 share an identical score, which suggests ontology-propagated predictions rather than independent signals.

**Amebic dysentery (rank 2):** This is conceptually close to the original indication, since loperamide relieves diarrhea. However, loperamide has no anti-amebic activity. In invasive amebic infection, slowing motility may impair parasite clearance and raise the risk of toxic megacolon. Any use would be at most adjunctive to amebicidal therapy.

**Gastroduodenitis (rank 4):** Symptom control of diarrhea is anatomically plausible, but loperamide has no known anti-inflammatory effect on gastric or duodenal mucosa.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

No literature is available for acute contagious conjunctivitis (rank 1). The following publications relate to other top-10 predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Nonfluid therapy of acute diarrhea. Oral fluids are the cornerstone, and nonspecific agents can reduce diarrhea and other symptoms of enteric infection (amebic dysentery prediction). |
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | J Travel Med | Fulminant amoebic colitis (toxic megacolon) in a patient with heavy loperamide use. The course may have been influenced by loperamide. This is a safety signal (amebic dysentery prediction). |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related gastrointestinal inflammation. A damaged gut barrier may increase systemic absorption and central opioid effects (gastroduodenitis prediction). |

---

## US Market Information

All 10 licenses are valid, and no approved indication text is recorded.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021855 | Anti-diarrheal (Albertsons Companies) | Capsule, liquid filled | Not recorded |
| ANDA072741 | Loperamide Hydrochloride (Bryant Ranch Prepack) | Capsule | Not recorded |
| ANDA091292 | Equate Loperamide Hydrochloride (Wal-Mart) | Suspension | Not recorded |
| ANDA206548 | Loperamide Hydrochloride (Amerisource Bergen) | Tablet | Not recorded |
| ANDA076497 | Anti-Diarrheal (First Aid Direct) | Tablet, coated | Not recorded |

---

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for label safety information. The following items come from other sources.

- **Knowledge graph contraindications (not label text):** liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrheal disease, infectious diarrheal disease, intestinal infectious disease.
- **Case-report safety signals:** toxic megacolon or fulminant colitis in invasive amebic infection, and respiratory depression when the gut barrier is compromised by severe inflammation.
- **Drug interactions:** 100 interactions were recorded, and the first 20 retrieved include several Major ones:
  - Abiraterone
  - Ranitidine
  - Fosamprenavir
  - Gemfibrozil
  - Moderate interactions include other opioids and CNS depressants (codeine, dihydrocodeine, tramadol, ethanol) and several antihistamines (chlorpheniramine, cetirizine, acrivastine, phenyltoloxamine).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (acute contagious conjunctivitis) and the other ocular predictions come only from the TxGNN model (deep learning) (L5), with no trials, no literature and no plausible mechanism. The two predictions with literature (amebic dysentery and gastroduodenitis, L4) show safety signals rather than efficacy. Antimotility agents are generally avoided in invasive dysentery. Also, the drug is marketed in the US, with 10 valid licenses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for loperamide
- Any preclinical or clinical evidence for the predicted indications, and a clear route and dosage form rationale for any ocular use
- Review of whether the prediction reflects TxGNN model (deep learning) artifacts, given the identical scores among the conjunctivitis subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

