---
layout: default
title: Phenazopyridine
parent: Model Prediction Only (L5)
nav_order: 1036
evidence_level: L5
indication_count: 1
monitor_inn: "PHENAZOPYRIDINE"
predicted_indications: ["bronchitis"]
last_modified_at: 2026-10-31
description: "Phenazopyridine: predicted new indication Bronchitis (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Phenazopyridine
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

## Phenazopyridine: From Urinary Tract Pain Relief to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Phenazopyridine is an oral urinary tract analgesic. The only US product record compiled for this report is a cancelled tablet, and it carries no stated indication text.
The TxGNN model predicts it may be effective for **bronchitis**, but this rests on a model score alone, with **0 clinical trials** and **0 publications** currently supporting the direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the license record has no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 1) |
| Number of FDA Applications | at least 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenazopyridine is generally known as a urinary tract analgesic that acts locally on the urinary mucosa. The data compiled for this report documents no mechanism and no original indication.

Based on known pharmacology, there is no established link between a urinary mucosal analgesic and airway inflammation or infection in bronchitis. The high TxGNN score (0.9923) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. For context, the model ranked this prediction 16,929th, so the high score should be interpreted cautiously. No mechanistic hypothesis can be confirmed without further data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Preferred Urinary Pain Relief (Reese Pharmaceutical Co) | Tablet | Not available (status: cancelled) |

## Safety Considerations

- **Contraindications (knowledge-graph inferred, not label text)**: The TxGNN knowledge graph links phenazopyridine to contraindications in several disease areas. These are not drawn from a package insert and should be verified against the label:
  - Kidney and liver: kidney disease, pyoureter, liver disease, liver failure, hepatic coma, hepatic encephalopathy, gallbladder disease
  - Blood: hematologic disease, anemia (including macrocytic anemia), thrombocytopenia, neutropenia, agranulocytosis
  - Metabolic: inherited porphyria, porphyria, porphyrin metabolism disease
  - Cardiovascular and respiratory: hypertension, hypertensive disorder, coronary artery disease, COPD (including severe early onset), obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, Haddad syndrome
  - Other: benign prostatic hyperplasia, anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence

  Several of these (COPD, sleep apnea, hypoventilation syndromes) are respiratory conditions, which warrants particular attention for a bronchitis indication.

- **Drug Interactions**: 24 interactions were identified in total, and 20 are detailed in the data compiled for this report.
  - **Major**: Nitrous acid, Leflunomide
  - **Moderate**:
    - Local anesthetics and cocaine: lidocaine (topical and ophthalmic), benzocaine, tetracaine (topical and ophthalmic), oxybuprocaine, cinchocaine, cocaine (nasal and topical)
    - Oncology and immunology agents: asparaginase Escherichia coli, pegaspargase, brentuximab vedotin, clofarabine, idelalisib, methotrexate
    - Others: naltrexone, interferon beta-1a, interferon beta-1b

Package insert warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no documented mechanism linking the drug to bronchitis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA, which is a blocking gap for safety screening
- Mechanism of action data (for example, from DrugBank) to test whether any biologically plausible link to bronchitis exists
- The original approved indication, confirmed from a current label
- A literature and trial search specific to phenazopyridine in respiratory conditions
- Route compatibility and similarity assessment between the original and predicted indications, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

