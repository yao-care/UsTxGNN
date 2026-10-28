---
layout: default
title: Telavancin
parent: Model Prediction Only (L5)
nav_order: 1205
evidence_level: L5
indication_count: 9
monitor_inn: "TELAVANCIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "septicemic plague", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy", "monoclonal gammopathy", "congenital hematological disorder"]
last_modified_at: 2026-10-28
description: "Telavancin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial pneumonia"
---

# Telavancin
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

## Telavancin: From Bacterial Pneumonia to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Telavancin is a lipoglycopeptide antibiotic originally used to treat bacterial pneumonia, including *Staphylococcus aureus* pneumonia.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, but **no clinical trials and no publications** currently support this prediction.
The high score appears to be a TxGNN model (deep learning) artifact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia; *Staphylococcus aureus* pneumonia |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, telavancin is a lipoglycopeptide antibiotic that inhibits bacterial cell wall synthesis and disrupts bacterial membrane integrity. Its efficacy is established for Gram-positive bacterial infections.

For hyperamylasemia, a credible mechanistic link is **not apparent**. Hyperamylasemia is a laboratory finding, usually tied to pancreatic or salivary gland pathology, and is not a condition an antibiotic would treat. The high score (0.9963) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Telavancin's known toxicity profile (nephrotoxicity, QT prolongation) also makes it a poor fit for this use.

Other predictions generated for this drug show the same pattern. Eight of nine have no plausible mechanism (e.g., polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy). The one exception is **septicemic plague** (score 0.9948, evidence level L4), which has an anti-infective rationale. However, *Yersinia pestis* is Gram-negative, and glycopeptides penetrate the Gram-negative outer membrane poorly. Established agents (streptomycin, gentamicin, doxycycline, fluoroquinolones) remain the standard of care, and no data on *Y. pestis* were available.

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
| NDA022110 | VIBATIV (Cumberland Pharmaceuticals Inc.) | Injection, powder, lyophilized, for solution | Not listed (license status: valid) |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** Hypertensive disorder, hypertension, long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, impaired renal function disease, pyoureter, diabetes mellitus, diabetic ketoacidosis, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis.
- **Drug Interactions:** 100 interactions were identified in total. The listed examples include:
  - **Major:** Dolasetron
  - **Moderate:** Ondansetron, Palonosetron, Clarithromycin, Levofloxacin, Famotidine, Loperamide
  - **Moderate (laxatives and bowel preparations):** Bisacodyl, Picosulfuric acid, Lactulose, Lactitol, Polyethylene glycol, Sodium sulfate, Castor oil
  - **Moderate (aminosalicylates):** Mesalazine, Balsalazide, Olsalazine, Sulfasalazine
  - **Minor:** Metronidazole

  Many of these interactions involve QT-prolonging or electrolyte-altering agents, which is consistent with the QT-related signals above.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on model score alone (L5), with no clinical trials or literature. Hyperamylasemia is a laboratory finding rather than a treatable disease, and no mechanistic link to telavancin exists. The drug's nephrotoxicity and QT-prolongation risks add to the unfavorable risk-benefit picture. The US license is also cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications
- Any preclinical or clinical evidence linking telavancin to hyperamylasemia (none currently exists)
- If pursuing the only anti-infective candidate (septicemic plague): in vitro and in vivo activity data against *Yersinia pestis*, and a comparison against current standard-of-care agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

