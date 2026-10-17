---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 2
monitor_inn: "BIOTIN"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
last_modified_at: 2026-10-14
description: "Biotin: predicted new indication Dyspepsia (evidence level L5). Approved use: Nutritional biotin deficiency"
---

# Biotin
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

# Biotin: From Nutritional Biotin Deficiency to Dyspepsia

## One-Sentence Summary

Biotin is a B-vitamin that was originally used to treat nutritional biotin deficiency.
The TxGNN model predicts it may be effective for **dyspepsia**, but there are currently **0 clinical trials** and only **6 loosely related publications** (none showing that biotin treats dyspepsia), so this prediction rests almost entirely on the computational model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional biotin deficiency |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, biotin is a cofactor for carboxylase enzymes involved in carbohydrate, fat, and amino acid metabolism. Its efficacy in correcting biotin deficiency is established.

Biotin deficiency can cause gastrointestinal symptoms such as nausea and anorexia. Any benefit in dyspepsia would therefore most likely be limited to people whose symptoms stem from a deficiency state, not functional dyspepsia in general. No established mechanistic link between biotin and dyspepsia was found. The high TxGNN score is a model-based prediction only.

A second predicted indication, gastroparesis (score 99.42%), has no clinical trials or literature and no plausible mechanism linking biotin to gastric motility. It is not evaluated further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | The Journal of Dermatology | A 5-month-old infant, diagnosed with dyspepsia as a neonate and fed only amino acid formula, developed biotin deficiency with alopecia and dermatitis. This shows dyspepsia-related feeding led to deficiency, not that biotin treats dyspepsia. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Stomach antral endocrine cells in 76 IBS patients vs. 43 healthy controls; biotin not the subject. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Endocrine cells in the oxyntic stomach mucosa of IBS patients; biotin not the subject. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathol | IL-10 in *H. pylori* gastritis; no biotin link. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Clinical study | Eksp Klin Gastroenterol | A prebiotic and vitamin supplement (including biotin) for gut microbiota in patients with lung disease on antibiotics; biotin is only one ingredient. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney Int | Small bowel T cells and stress proteins in IgA nephropathy; no biotin link. |

None of these studies tests biotin as a treatment for dyspepsia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA nan | Biotin Drops | Liquid | Not specified (cancelled) |
| M032 | AVEYA BIOTIN HAIR GROWTH | Liquid | Not specified (cancelled) |
| 505G(a)(3) | 5% Minoxidil Hair Growth Foam with Biotin | Aerosol, foam | Not specified (cancelled) |

All three authorizations are cancelled, and none lists an approved indication.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The TxGNN knowledge graph links biotin to contraindication-type edges for kidney disease, nephrolithiasis (including SLC26A1-related susceptibility), nephrocalcinosis, acute urate nephropathy, pyoureter, sarcoidosis, hyperparathyroidism, osteitis fibrosa, hypercalcemia, phosphorus metabolism disease, constipation disorder, and lytic metastatic bone lesion. These come from the model's graph and should be verified against official labeling.

No drug interaction records were found. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature, and no established mechanism, so it sits at evidence level L5. The US market status shows only cancelled authorizations, and safety review cannot proceed without label data.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Evidence on whether dyspepsia symptoms respond to biotin, such as in patients with documented deficiency
- Review of the kidney, calcium, and bone-related safety associations listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

