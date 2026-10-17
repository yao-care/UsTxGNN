---
layout: default
title: Tiopronin
parent: Model Prediction Only (L5)
nav_order: 1231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tiopronin: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Cystinuria"
monitor_inn: "TIOPRONIN"
predicted_indications: ["renal tubular acidosis", "adult polyglucosan body disease", "tricarboxylic acid cycle disorder", "disease of transporter activity", "pyruvate metabolism disorder", "inborn disorder of fatty acid oxidation and ketone body metabolism"]
---

# Tiopronin
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

# Tiopronin: From Cystinuria to Renal Tubular Acidosis

## One-Sentence Summary

Tiopronin is a thiol compound originally used for cystinuria (and listed with related inherited metabolic conditions in the knowledge graph).
The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystinuria (the compiled US license records contain no indication text; the original indications come from the knowledge graph: cystinuria, glycogen storage disease, G6PD deficiency, galactosemia) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 licenses in total (2 NDAs and 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known chemistry, tiopronin is a thiol compound that forms soluble mixed disulfides with cysteine. This is the basis for its use in cystinuria, a renal tubular transport disorder.

Renal tubular acidosis (RTA) also involves renal tubular dysfunction, so the model may be linking the two through a shared tubular-disease space. However, the thiol-exchange mechanism does not address the bicarbonate reabsorption or acid secretion defects that cause RTA. The high score (0.996) is a computational output only, with no supporting clinical or literature evidence, so the mechanistic link should be considered weak.

The other nine top predictions are mostly glycogen branching enzyme deficiency subtypes (including adult polyglucosan body disease), plus broad metabolic categories such as tricarboxylic acid cycle disorder, pyruvate metabolism disorder, and fatty acid oxidation disorders. These appear to be driven by proximity to "glycogen storage disease" and general inborn-error annotations in the knowledge graph. The "disease of transporter activity" prediction likely reflects the already established cystinuria association rather than a new indication. None has trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019569 | Thiola | Tablet, sugar coated | Not available (cancelled) |
| NDA211843 | Tiopronin (BioComp Pharma) | Tablet, delayed release | Not available (cancelled) |
| ANDA216990 | VENXXIVA | Tablet, delayed release | Not available (cancelled) |
| ANDA216456 | Tiopronin (Teva Pharmaceuticals, Inc.) | Tablet, delayed release | Not available (cancelled) |
| ANDA217219 | Tiopronin (Endo USA, Inc.) | Tablet, delayed release | Not available (cancelled) |

Two further licenses are not shown: ANDA216278 (Amneal, delayed-release tablet) and ANDA214326 (Teva, sugar-coated tablet). All 7 licenses are cancelled.

## Safety Considerations

No label-based warnings or contraindications were available. The following comes from knowledge-graph drug-disease contraindication associations and is not label text:

- **Kidney and urinary conditions:** kidney disease, pyoureter, nephrotic syndrome (including familial forms and lipoid nephrosis), proteinuria, anti-glomerular basement membrane disease, granulomatosis with polyangiitis
- **Liver and gallbladder conditions:** liver disease, gallbladder disease
- **Blood disorders:** thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including cyclic and congenital forms), aplastic anemia
- **Neuromuscular conditions:** myasthenia gravis, neuromuscular junction disease

No drug interaction data were found. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or publications, the proposed mechanism does not match the pathophysiology of renal tubular acidosis, and the drug currently has no valid US licenses. The knowledge-graph contraindications (renal, hepatic, hematologic) are also a concern for patients with tubular or metabolic disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A literature and trial search for tiopronin in renal tubular acidosis, with preclinical evidence of a plausible mechanism
- Clarification of why all US licenses are cancelled, and confirmation of current availability
- Route and dosage-form compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

