---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 951
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "NAFARELIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "pelvic organ prolapse", "syndrome with a Dandy-Walker malformation as major feature", "female genital tuberculosis", "physiological sexual disorder", "isolated genetic hair shaft abnormality", "dysplasia of cervix"]
description: "Nafarelin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Nafarelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Nafarelin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Nafarelin is a GnRH (gonadotropin-releasing hormone) agonist, originally used to treat endometriosis and central precocious puberty.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, nafarelin is a peptide GnRH agonist that acts on the GnRH receptor (GNRHR). Continuous exposure suppresses gonadotropin release and therefore sex steroid production. This is why it works in hormone-dependent conditions such as endometriosis and central precocious puberty.

The predicted indication, Ambras syndrome, is a congenital hypertrichosis linked to genomic rearrangements affecting regulation of the *TRPS1* gene. Its cause is developmental and genetic rather than driven by sex hormones. No established mechanistic link to GnRH-agonist-mediated hormonal suppression was identified. The high score appears to be a network-based association with no supporting clinical or literature data, so this prediction should be viewed as **speculative**.

For context, the other top-ranked predictions are similarly weak:
- **Hypertrichosis (rank 3):** Androgen suppression could in theory reduce androgen-dependent hair growth, but hypertrichosis is generally androgen-independent.
- **Central precocious puberty 1 (rank 9):** This is already an original indication, so it is a rediscovery of a known use, not a new opportunity.
- **Physiological sexual disorder (rank 7):** The only supporting paper is a 1994 study of endometriosis pain with nafarelin versus danazol, which is an existing indication rather than direct evidence for sexual dysfunction.
- **Pelvic organ prolapse (rank 4):** Nafarelin-induced hypoestrogenism would be expected to worsen pelvic tissue integrity, so benefit is biologically unlikely.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the lead prediction.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019886 (cancelled) | Synarel (Pfizer Laboratories Div Pfizer Inc) | Metered spray | Not listed in the compiled data |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertensive disorder, hypertension, hyperglycemia, osteoporosis, postmenopausal osteoporosis, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, obesity disorder, monogenic obesity. These should be verified against the official label.
- **Drug interactions:** No drug-drug interactions were identified. The only pharmacology entry is the drug's target, the GnRH1 receptor (GNRHR).

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a network-based score, with no clinical trials, no literature, and no plausible mechanistic link between GnRH agonism and a genetically driven congenital hypertrichosis.

**To proceed, the following is needed:**
- Mechanistic evidence connecting GnRH-axis suppression to the *TRPS1*-related pathology of Ambras syndrome
- Preclinical or case-level data in hypertrichosis or related hair disorders
- Official FDA package insert warnings and contraindications for a full safety review
- Mechanism of action data from DrugBank
- Confirmation of current regulatory and supply status, given that the NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

