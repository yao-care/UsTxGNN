---
layout: default
title: Chlorpromazine
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 9
monitor_inn: "CHLORPROMAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
last_modified_at: 2026-10-30
description: "Chlorpromazine: predicted new indication retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Not recorded in the local data"
---

# Chlorpromazine
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

## Chlorpromazine: Dopamine D2 receptor–antagonist antipsychotic → retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Chlorpromazine is a phenothiazine antipsychotic marketed in the United States as tablets and injections.
The TxGNN model predicts it may be relevant to **retinal dystrophy with or without extraocular anomalies**, but the data compiled for this report contain **no clinical trials** and only **1 publication**, a 1967 report of phototoxic adverse reactions, which argues against a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of NDAs | at least 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Chlorpromazine is generally known as a dopamine D2 receptor antagonist, but this report cannot draw a mechanistic link to retinal disease from the available data.

The only publication found (PMID 5336672, 1967) describes phototoxic reactions induced by high doses of chlorpromazine and thioridazine. That is an adverse-effect signal, involving photosensitivity and pigmentary changes, and it points away from use in retinal disease. The high TxGNN score (0.9995) is most likely an artefact of shared nodes in the model's network (for example retinal or pigment-related features) and not evidence of benefit.

No study directly examines chlorpromazine as a treatment for this disease, so the evidence level is L5, a model prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Review / case reports (toxicity) | JAMA | Phototoxic reactions induced by high doses of chlorpromazine and thioridazine; an adverse-effect report, not evidence of therapeutic benefit |

---

## US Market Information

The data compiled for this report list 11 US generic (ANDA) records for single-ingredient chlorpromazine. The list may be partial. Dosage forms include:

- Oral: tablets, sugar-coated tablets, film-coated tablets, coated tablets
- Injectable: injection

---

## Cytotoxicity

Chlorpromazine is not an antineoplastic drug, so this section does not apply.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Examples include:
  - **Major**: bupropion, morphine
  - **Moderate**: acarbose, famotidine, epinephrine, hydrocortisone, albiglutide, alogliptin, metformin, pioglitazone, amphotericin B, hyoscyamine, loperamide, atropine, lorcaserin, bisacodyl, glycopyrronium, canagliflozin, chlorpropamide
- **Phototoxicity**: the one retrieved publication reports photosensitivity-type reactions at high doses, which is directly relevant to eye and skin safety.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only. There are no clinical trials, and the sole publication describes toxicity, not benefit. No plausible mechanism has been identified, so the evidence does not support moving forward.

**To proceed, the following is needed:**
- Mechanism-of-action data and a plausible biological rationale linking chlorpromazine to this retinal dystrophy
- Preclinical evidence (for example retinal cell or animal model studies) showing benefit
- A review of ocular phototoxicity and pigmentary risks, using the package insert warnings and contraindications
- A route and dosage-form assessment for any ocular use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

