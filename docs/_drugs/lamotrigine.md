---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 831
evidence_level: L5
indication_count: 9
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "thinking seizures", "audiogenic seizures", "orgasm-induced seizures", "eating seizures", "startle epilepsy", "micturation-induced seizures", "reading seizures"]
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is an anticonvulsant originally used for epilepsy, including partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **2 loosely related publications**, both about trigeminal neuralgia rather than a tumour.
The prediction is therefore best treated as a model signal without direct supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial epilepsy, Lennox-Gastaut syndrome (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 13 licenses (1 NDA, 12 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lamotrigine is not available in the compiled data. Based on known pharmacology, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release. This is the basis of its efficacy in epilepsy.

The link to a trigeminal nerve neoplasm is weak. The supporting literature concerns **trigeminal neuralgia**, a facial pain syndrome, and a case report of Gamma Knife radiosurgery for neuralgia caused by a cavernous malformation. Neither studies lamotrigine as a treatment for a neoplasm.

The high score most likely reflects graph proximity to trigeminal neuralgia. In that condition, sodium channel blockade may dampen ectopic firing of trigeminal nerve fibres and reduce neuropathic pain. It does not suggest anti-tumour activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Overview of medical and surgical treatments for trigeminal neuralgia. It discusses vascular compression of the nerve root as the likely cause. It does not address a neoplasm. |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotactic and Functional Neurosurgery | First reported Gamma Knife radiosurgery for trigeminal neuralgia caused by a brainstem cavernous malformation. It does not involve lamotrigine. |

Both papers are only tangentially related to the predicted indication.

---

## US Market Information

All 13 US licenses for single-ingredient lamotrigine are cancelled. The records contain no approved-indication text. Five representative entries are shown.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA 020764 | LAMICTAL | Tablet, for suspension | Cancelled |
| ANDA 078947 | SUBVENITE | Tablet | Cancelled |
| ANDA 206382 | Lamotrigine | Tablet, orally disintegrating | Cancelled |
| ANDA 207497 | Lamotrigine | Tablet, film coated, extended release | Cancelled |
| ANDA 213271 | Lamotrigine | Tablet, orally disintegrating | Cancelled |

All dosage forms are oral.

---

## Safety Considerations

- **Contraindications / disease associations (from the TxGNN knowledge graph, not label text):** liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), pancytopenia, aplastic anaemia, non-infectious meningitis, anxiety disorder, neurotic disorder and dysthymic disorder.
- **Drug Interactions:** The interaction database lists 100 entries. The moderate-level interactions shown are morphine (including liposomal morphine), opium, dronabinol, nabilone, metoclopramide and orlistat. Metformin is listed as minor. Several others, such as omeprazole, pantoprazole, doxycycline and vancomycin, are listed with an unknown severity level.

Label-based warnings and contraindications were not compiled for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and no literature showing lamotrigine activity against a trigeminal nerve neoplasm. The prediction appears to be driven by the drug's association with trigeminal neuralgia, which is a different condition. All US licenses are also cancelled.

**To proceed, the following is needed:**
- Preclinical or clinical evidence that lamotrigine has anti-tumour activity or symptomatic benefit in trigeminal nerve tumours
- Detailed mechanism-of-action data
- FDA package insert warnings and contraindications for a full safety screen

**Note on other predictions for this drug:** The second-ranked prediction, **trigeminal neuralgia** (score 99.89%), has far stronger support. It has two completed small trials, NCT00913107 (Phase 2/3 versus carbamazepine, n=21) and NCT00203229 (placebo-controlled add-on study, n=20). Guidelines list lamotrigine as an alternative or add-on when carbamazepine fails or is not tolerated. This is a better candidate for follow-up. **Startle epilepsy** also has small case-series support for lamotrigine (Level L3).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

