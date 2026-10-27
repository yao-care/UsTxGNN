---
layout: default
title: Histidine
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 2
monitor_inn: "HISTIDINE"
predicted_indications: ["gastroparesis (disease)", "sclerosing cholangitis"]
last_modified_at: 2026-10-14
description: "Histidine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not available"
---

# Histidine
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

## Histidine: From an Unspecified Original Indication to Gastroparesis
{: .text-alpha }

## One-Sentence Summary

Histidine is an essential amino acid. The only U.S. product record compiled for this report is a cancelled liquid product, and it lists no approved indication.
The TxGNN model predicts it may be effective for **gastroparesis**, but **0 clinical trials** and only **1 loosely related publication** support this prediction. The evidence is model-prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the single U.S. record has no approved indication text) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Histidine is an amino acid and the precursor of histamine, but no approved original indication is recorded, so no mechanistic bridge to gastroparesis can be drawn from the compiled data.

The one publication retrieved (PMID 42668409) describes gastric amyloid pathology and mucosal denervation in hereditary ATTR amyloidosis. It did not test histidine and shows no histidine-related mechanism in gastric motility. The high TxGNN score reflects a graph-based association only. No direct or plausible link between histidine and gastroparesis has been established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Preclinical/clinical mixed (patients and mice) | Amyloid | Describes gastric amyloid pathology and mucosal denervation in ATTRv amyloidosis with gastrointestinal autonomic dysfunction. Histidine was not tested. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | L-Histidine High (Professional Complementary Health Formulas) | Liquid | Not listed |

---

## Safety Considerations

- **Disease contraindication signals (knowledge-graph based, not from label text):** The TxGNN knowledge graph links histidine to contraindication with several conditions:
  - Kidney: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis (including the SLC26A1-related form), nephrocalcinosis, acute urate nephropathy, pyoureter
  - Calcium and phosphorus: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Cardiac: heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
  - Metabolic: phenylketonuria, disorders of phenylalanine metabolism

Please refer to the package insert for further safety information. No drug interaction data were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score. There are no clinical trials, the single publication does not involve histidine, and no mechanistic link is evident. The only U.S. product record is cancelled and has no indication.

**To proceed, the following is needed:**
- Mechanism of action data for histidine
- Package insert warnings and contraindications
- Evidence that histidine influences gastric motility, from preclinical or clinical studies
- A review of the knowledge-graph contraindications (renal, cardiac, calcium-related) against the likely gastroparesis population

---

## Supplementary Note: Second-Ranked Prediction (Sclerosing Cholangitis)

The second prediction, **sclerosing cholangitis** (TxGNN score 99.27%, evidence level L4), has 8 publications and no clinical trials.

- **Mechanism:** Histidine is the precursor of histamine via L-histidine decarboxylase. Preclinical studies show that mast cell-derived histamine drives biliary proliferation and fibrosis in primary sclerosing cholangitis models (PMIDs 27351144, 35799467, 32054995, 29601088).
- **Direction of effect:** Reducing histamine signaling was beneficial in these models. Supplemental histidine could therefore be neutral or potentially harmful, so the evidence does not support repurposing histidine for this condition.
- **Status:** Treat it as a research question only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

