---
layout: default
title: Hyoscyamine
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 1
monitor_inn: "HYOSCYAMINE"
predicted_indications: ["gastroduodenitis"]
last_modified_at: 2026-10-28
description: "Hyoscyamine: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Peptic ulcer disease"
---

# Hyoscyamine
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

## Hyoscyamine: From Peptic Ulcer Disease to Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Hyoscyamine is an antimuscarinic (anticholinergic) drug, originally used to treat peptic ulcer disease.
The TxGNN model predicts it may be effective for **Gastroduodenitis**,
but currently there are **0 registered clinical trials** and only **1 publication** (a general review with little direct relevance), so the prediction rests almost entirely on computational inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 1) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hyoscyamine is a non-selective antimuscarinic agent. Gastric acid secretion and gastrointestinal motility and spasm are both modulated by muscarinic receptors, which is the basis of its use in peptic ulcer disease.

Gastroduodenitis is an inflammatory condition of the same anatomical region. Reduced secretion and reduced spasm could therefore plausibly relieve symptoms. However, this link is symptomatic only: antimuscarinics do not treat the underlying inflammation or causes such as *H. pylori* infection. The high TxGNN score (0.9959) is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review | Endoscopy | A general review of premedication, sedation (e.g., propofol), and patient surveillance for endoscopy. It does not directly evaluate hyoscyamine for gastroduodenitis. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Hyoscyamine Sulfate (ANI Pharmaceuticals, Inc.) | Tablet, extended release | Not available (status: cancelled) |

Other dosage forms recorded for hyoscyamine include oral tablets, orally disintegrating tablets, elixir, and injectable solution.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph links hyoscyamine to contraindications in several conditions, including:
  - Cardiovascular: hypertension, congestive heart failure
  - Respiratory: chronic obstructive pulmonary disease
  - Hepatic and renal: liver failure, liver disease, cirrhosis, hepatic coma and encephalopathy, kidney disease
  - Gastrointestinal: gastritis, gastric ulcer
  - Genitourinary: benign prostatic hyperplasia
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, porphyria
  - Haematological: thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disorders, haemophilia
  - Psychiatric: anxiety disorder, substance abuse or dependence

  Notably, gastritis and gastric ulcer appear in this list, which warrants clarification before any use in gastroduodenitis.

- **Drug Interactions**: 100 interactions were recorded; the 20 reviewed are mostly Moderate, with a few Minor.
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergic or antimuscarinic agents: aclidinium, amitriptyline, amoxapine, amantadine
  - Antihistamines: chlorpheniramine, acrivastine, phenyltoloxamine
  - Others: botulinum toxin type A, phenylephrine, acebutolol, acetylcholine, ambenonium, ethanol
  - Minor: acetaminophen, hydrochlorothiazide

Package insert warnings and contraindications were not available for this report; please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no registered clinical trials and no directly relevant literature (L5, model prediction only). The mechanism is plausible but only symptomatic, the only US authorization on record is cancelled, and the knowledge graph lists gastritis and gastric ulcer among its contraindications.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A targeted literature search on antimuscarinics in gastroduodenitis or gastritis, and review of whether any trials exist
- Clarification of the knowledge-graph gastritis and gastric ulcer contraindication signals
- Confirmation of the regulatory pathway, given the cancelled US status, and of route and formulation compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

