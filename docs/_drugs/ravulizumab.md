---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 1112
evidence_level: L5
indication_count: 10
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
last_modified_at: 2026-11-12
description: "Ravulizumab: predicted new indication Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency (evidence level L5). Approved use: Paroxysmal nocturnal hemoglobinuria"
---

# Ravulizumab
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

## Ravulizumab: From Paroxysmal Nocturnal Hemoglobinuria to Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency
{: .text-alpha }

## One-Sentence Summary

Ravulizumab is a long-acting C5 complement inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria (PNH).
The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, ravulizumab is a long-acting inhibitor of complement component C5. Its efficacy in PNH, a disease of complement-mediated hemolysis, is the basis of its original indication.

The predicted disease is different in nature. G6PC3 deficiency is a defect in glucose-6-phosphatase catalytic subunit 3, which causes neutrophil apoptosis and endoplasmic reticulum stress. No established link exists between terminal complement activation and this neutropenia. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. These include cyclic hematopoiesis, severe congenital neutropenia, CXCR2 deficiency, primary hyperoxaluria, and pseudo-von Willebrand disease. None has a recognized role for C5 inhibition, and none has supporting trials or literature. Primary hyperoxaluria is the only one with even a speculative indirect link, through complement-related secondary renal injury from calcium oxalate crystals. Its primary disease driver is not addressed by C5 blockade.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761108 | Ultomiris (Alexion Pharmaceuticals Inc.) | Solution, concentrate | Not listed in the compiled data (status: valid) |

## Safety Considerations

- **Contraindication signal from the knowledge graph**: Meningococcal infection is listed as a contraindicated disease. This comes from knowledge graph edges, not from package insert text. It is consistent with the known infection risk from terminal complement blockade, and the risk is greater in patients with immunodeficiency.
- **Drug Interactions**: Four interactions were found, all rated Minor. They involve human immunoglobulin G in its intravenous, subcutaneous, intramuscular, and combined intravenous/subcutaneous forms.

Please refer to the package insert for other warnings and contraindications. The label text was not available when this report was compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5), and no plausible mechanistic link between C5 inhibition and G6PC3-deficiency neutropenia. Complement blockade also carries a serious risk of meningococcal and other encapsulated-organism infection, which is a particular concern in neutropenic or immunodeficient patients.

<!-- review:begin us-lic-20261031-ravulizumab-1 -->

> **Review correction (2026-10-31)**: Originally stated: "Complement blockade also carries a serious risk of meningococcal and other encapsulated-organism infection, which is a particular concern in neutropenic or immunodeficient patients. In addition, the only US license is listed as cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-ravulizumab-1 -->

**To proceed, the following is needed:**
- Mechanistic evidence for complement involvement in G6PC3-deficiency neutropenia, such as preclinical or biomarker studies
- Detailed mechanism-of-action data for ravulizumab
- The full package insert, to review warnings and contraindications
- Clarification of the US regulatory status
- A risk-benefit assessment of infection risk (including meningococcal vaccination and prophylaxis) in neutropenic patients

<!-- review:begin us-lic-20261106-ravulizumab-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the US regulatory status and the reason for cancellation" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ravulizumab-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "In addition, the only US license is listed as cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and the reason for cancellation" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

