---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Fexofenadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis (also vasomotor rhinitis, atopic…"
monitor_inn: "FEXOFENADINE"
predicted_indications: ["rosacea conjunctivitis"]
---

# Fexofenadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fexofenadine is an antihistamine originally used to treat allergic rhinitis, allergic and other forms of conjunctivitis, and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (also vasomotor rhinitis, atopic, papillary and vernal conjunctivitis, idiopathic urticaria) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 26 of 36; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 36 (active: 26) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, fexofenadine is a selective peripheral histamine H1-receptor antagonist. Its efficacy in allergic, atopic, papillary and vernal conjunctivitis suggests a possible, indirect link to histamine-mediated inflammation of the ocular surface.

However, the mechanistic rationale for rosacea conjunctivitis is weak. Ocular rosacea is driven mainly by meibomian gland dysfunction, Demodex colonization, innate immune activation and neurovascular dysregulation, with limited histamine involvement. The very high TxGNN score (0.9985) is a computational result that likely reflects network proximity to the approved conjunctivitis indications. It is not backed by clinical or literature evidence. Route compatibility and similarity to the original indications have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076447 | FEXOFENADINE HYDROCHLORIDE HIVES | TEVA | Tablet; oral | Valid |
| ANDA076502 | FEXOFENADINE HYDROCHLORIDE ALLERGY | DR REDDYS LABS LTD | Tablet; oral | Valid |
| ANDA079112 | FEXOFENADINE HYDROCHLORIDE ALLERGY | PHARMAZONE | Tablet; oral | Valid |
| ANDA091567 | FEXOFENADINE HYDROCHLORIDE ALLERGY | SUN PHARM INDS | Tablet; oral | Valid |
| ANDA202039 | FEXOFENADINE HYDROCHLORIDE ALLERGY | AUROBINDO PHARMA LTD | Tablet; oral | Valid |

Showing 5 of 37 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The drug is marketed.

<!-- review:begin us-lic-20261106-fexofenadine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Five valid licenses are on record in the compiled data, and the drug is marketed." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 36 FDA applications or NDC listings for this drug, 26 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-fexofenadine-1 -->

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph (not label text)**: hypertension/hypertensive disorder, kidney disease, pyoureter, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease, coronary atherosclerosis, arteriosclerosis/atherosclerosis, angle-closure glaucoma, hyperthyroidism, Graves disease and thyrotoxicosis. These come from a computational knowledge graph and should be verified against the package insert.
- **Drug Interactions** (100 interactions recorded; examples shown):
  - Moderate: eliglustat, eluxadoline, rolapitant, magnesium hydroxide, aluminum hydroxide, magaldrate, magnesium carbonate. The antacids are notable because aluminum- and magnesium-containing products may reduce fexofenadine absorption.
  - Minor: clarithromycin, miconazole, clotrimazole.
  - Severity not classified: calcitriol, doxycycline, cimetidine, levocarnitine, epinephrine, dolasetron, dicyclomine, chlorhexidine, famotidine, acetylsalicylic acid.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the mechanistic link to rosacea-associated conjunctivitis is weak, and the drug is marketed.

<!-- review:begin us-lic-20261106-fexofenadine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials or publications, the mechanistic link to rosacea-associated conjunctivitis is weak, and the drug is marketed with five valid US licenses in the data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 36 FDA applications or NDC listings for this drug, 26 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-fexofenadine-2 -->

**To proceed, the following is needed:**
- Retrieval and review of the FDA package insert warnings and contraindications
- Confirmed mechanism of action data (DrugBank)
- A literature and trial search specific to ocular rosacea and antihistamines
- Assessment of route compatibility (oral drug versus the ocular surface target) and similarity to the original indications
- Preclinical or mechanistic evidence for any histamine role in ocular rosacea

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Five valid licenses are on record in the compiled data, and t" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with five valid US licenses in the data" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

