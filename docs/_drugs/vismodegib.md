---
layout: default
title: Vismodegib
parent: Model Prediction Only (L5)
nav_order: 1294
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "VISMODEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
description: "Vismodegib: predicted new indication Medulloblastoma with extensive nodularity (evidence level L5). Approved use: Not recorded in the local data"
---

# Vismodegib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Vismodegib: Medulloblastoma with extensive nodularity
{: .text-alpha }

## One-Sentence Summary

Vismodegib is an oral Hedgehog pathway inhibitor, originally used for basal cell carcinoma and other skin cancers.
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**,
but **no clinical trials** and **no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the compiled data. Based on the available analysis, vismodegib is a Smoothened (SMO) inhibitor that blocks the Hedgehog signaling pathway. Aberrant activation of this pathway drives most basal cell carcinomas.

Medulloblastoma, especially the SHH (Sonic Hedgehog) subgroup, is also driven by Hedgehog signaling. Medulloblastoma with extensive nodularity is a histological subtype of this tumor. This makes the prediction biologically plausible: the same pathway that vismodegib blocks in basal cell carcinoma is a known driver in this brain tumor.

However, this link is a hypothesis. No trials or publications were retrieved for this specific subtype, and the high score is a model output, not clinical proof. Pathway activity can also differ between tumor subtypes and molecular groups.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203388 (cancelled) | ERIVEDGE (Genentech, Inc.) | Capsule (oral) | Not listed in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / SMO inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert; the drug is known to be teratogenic, so exposure precautions for people who are or may become pregnant should be confirmed |

## Safety Considerations

- **Known adverse effects (from related analysis of the on-label skin cancer use):** muscle spasms, alopecia, and dysgeusia (taste disturbance). Teratogenicity (risk of fetal harm) is also a recognized concern.
- **Drug Interactions:** 56 interactions were recorded. Among the 20 listed, one is Moderate (**clarithromycin**). The other 19 are Minor and mostly involve acid-reducing agents: H2 blockers (famotidine, ranitidine, cimetidine, nizatidine), proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), and antacids (aluminum hydroxide, calcium carbonate, magnesium salts, sodium bicarbonate, sodium citrate, magaldrate).

Formal package-insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Hedgehog-pathway rationale for medulloblastoma is plausible, but the prediction is supported only by the model score (Evidence Level L5), with no trials or literature for this subtype. The only US license is also cancelled, so availability would need to be verified.

**To proceed, the following is needed:**
- A systematic search for clinical and preclinical evidence of Hedgehog inhibitors in SHH-subgroup medulloblastoma, including the nodular subtype
- Molecular and subgroup analysis to define which patients would have pathway-driven disease
- Detailed mechanism-of-action data and the FDA package insert (warnings and contraindications)
- A safety plan covering embryo-fetal toxicity and the drug interaction with clarithromycin
- Confirmation of current drug availability, since the US license is cancelled

**Note on other predictions:** In the same analysis, the prediction for **skin cancer** has the strongest support (Evidence Level L2, with several Phase 2 trials, a registry study, and European guidelines). That is largely the drug's original use rather than true repurposing, and it is rated "Proceed with Guardrails". Among the other predictions, xeroderma pigmentosum is supported only by case reports (L4), and the rest have no clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

