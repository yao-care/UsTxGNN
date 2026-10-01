---
layout: default
title: Hemin
parent: Model Prediction Only (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Hemin
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

# Hemin: From Acute Porphyria to Thrombocytopenic Purpura

## One-Sentence Summary

Hemin (marketed as Panhematin) is an intravenous heme product. The supplied data does not list its approved indication, but the retrieved literature describes intravenous hemin use in acute hepatic porphyria.
The TxGNN model predicts it may be effective for **thrombocytopenic purpura**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied regulatory data (the Panhematin label should be checked; acute porphyria is the use described in the retrieved literature) |
| Predicted New Indication | Thrombocytopenic purpura |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (a BLA: BLA101246) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hemin is a heme-based biologic product, and its known use centers on heme-pathway disorders. No mechanistic link to thrombocytopenic purpura is supported by the supplied data.

The high score (99.79%) comes from the knowledge graph alone. It reflects graph proximity between hemin and blood or coagulation disorders, not demonstrated pharmacology. Nine other blood, coagulation and complement-related conditions also scored above 99%, which suggests a shared graph signal rather than a disease-specific finding.

One of these other predictions has a faint biological lead. Hemin is a known inducer of heme oxygenase-1 (HO-1), and a mouse study (PMID 19890094) showed that HO-1 induction reduced the immune response to therapeutic factor VIII in hemophilia A. This is preclinical, concerns hemophilia rather than thrombocytopenic purpura, and does not show any hemostatic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA101246 | Panhematin (Recordati Rare Diseases, Inc.) | Powder, for solution | Not provided in the supplied data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5) and no supplied mechanistic rationale. Safety data is also missing, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank)
- A targeted literature and trial search on heme or hemin in immune thrombocytopenia and thrombotic thrombocytopenic purpura
- A route and formulation compatibility review (currently only an intravenous powder for solution is available)
- Optionally, the hemophilia lead (rank 2, HO-1 and factor VIII immunogenicity) could be explored as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

