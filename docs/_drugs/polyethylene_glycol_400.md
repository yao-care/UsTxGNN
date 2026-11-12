---
layout: default
title: Polyethylene Glycol 400
parent: Model Prediction Only (L5)
nav_order: 1061
evidence_level: L5
indication_count: 2
monitor_inn: "POLYETHYLENE GLYCOL 400"
predicted_indications: ["bronchitis", "congenital ichthyosiform erythroderma"]
last_modified_at: 2026-11-12
description: "Polyethylene Glycol 400: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Polyethylene Glycol 400
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Polyethylene Glycol 400: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Polyethylene glycol 400 (PEG 400) is a hydrophilic, osmotically active polymer, originally used for constipation and as a lubricant in eye drops for dry eye.
The TxGNN model predicts it may be effective for **Bronchitis**, but the prediction is based on the model alone: **0 clinical trials** and **0 publications** were found to support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| US Market Status | Marketed (no FDA-approved application; OTC monograph / unapproved listings: 123) |
| Number of FDA Applications | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, PEG 400 is a hydrophilic polymer that draws water osmotically. It is used as a laxative and as a lubricant in eye drops, and mechanistically it might be applicable to bronchitis.

One speculative link is airway surface hydration or changes in mucus rheology. No retrieved evidence supports this idea. The high TxGNN score (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

PEG 400 is also mainly used as an excipient or vehicle. This weakens the case for a specific therapeutic effect in bronchitis.

**Second predicted indication (for reference):** The model also predicted *congenital ichthyosiform erythroderma* (score 0.9910, also Evidence Level L5, Hold). The speculative rationale is that PEG 400 could act as a humectant or emollient base that hydrates the skin in a hyperkeratotic disorder. This would be supportive and topical at best. It would not address the underlying genetic cause, and no trials or literature were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 (cancelled) | blink tears (Bausch & Lomb Incorporated) | Solution/drops | Not specified |

Other dosage forms associated with this drug include a solution and a topical gel.

## Safety Considerations

The data compiled for this report contain no package insert warnings, contraindications, or drug interaction records for this drug. The knowledge graph does list the following conditions as contraindication-related. These come from a computational graph and are not label text, so they should be verified against the official package insert:

- **Cardiovascular and metabolic:** hypertension, congestive heart failure, cardiovascular disease, heart disease, diabetes mellitus, hyperglycemia, diabetic ketoacidosis, hypercalcemia, potassium deficiency, phosphorus metabolism disease
- **Renal and urinary:** kidney disease, anuria, nephrocalcinosis, pyoureter
- **Gastrointestinal:** ileus, paralytic ileus, intestinal obstruction, toxic megacolon, pyloric stenosis, familial visceral myopathy, appendicitis
- **Eye:** angle-closure glaucoma, eye infectious disease, conjunctivitis
- **Other:** epilepsy, hyperthyroidism, Graves disease, thyrotoxicosis

Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on a model score, with no clinical trials, no literature, and no documented mechanism of action. The evidence is not sufficient to justify further development at this time.

<!-- review:begin us-lic-20261031-polyethylene_glycol_400-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The bronchitis prediction rests only on a model score, with no clinical trials, no literature, and no documented mechanism of action. PEG 400 is mainly an excipient or vehicle, and its only US authorization has been cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 0 FDA applications or NDC listings for this drug, 0 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-polyethylene_glycol_400-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a testable hypothesis for airway effects
- Package insert warnings and contraindications from the FDA, to allow safety screening
- Preclinical or literature evidence that PEG 400 affects airway hydration, mucus properties, or inflammation
- Assessment of route compatibility, since an inhaled or oral route for bronchitis has not been evaluated and the existing products are not intended for it
- Assessment of similarity between the original indications and bronchitis

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "PEG 400 is mainly an excipient or vehicle, and its only US authorization has been cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

