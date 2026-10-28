---
layout: default
title: Potassium Nitrate
parent: Model Prediction Only (L5)
nav_order: 1071
evidence_level: L5
indication_count: 2
monitor_inn: "POTASSIUM NITRATE"
predicted_indications: ["meningococcal infection", "sclerosing cholangitis"]
last_modified_at: 2026-10-28
description: "Potassium Nitrate: predicted new indication Meningococcal infection (evidence level L5). Approved use: Not recorded in the local data"
---

# Potassium Nitrate
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

## Potassium Nitrate: Meningococcal infection
{: .text-alpha }

## One-Sentence Summary

Potassium nitrate is a nitrate salt. In the US it appears only in cancelled products (a dentifrice paste and a homeopathic pellet), and no approved indication is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **meningococcal infection**, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction, and the data compiled for this report do not support a plausible therapeutic role.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded for potassium nitrate. Based on general chemistry, it is a nitrate salt that can be reduced to nitrite and nitric oxide. Nitric oxide has general antimicrobial properties in some contexts.

That link is speculative. No trial or publication connects potassium nitrate to *Neisseria meningitidis* infection. Meningococcal infection is a severe invasive bacterial disease, treated with established antibiotics and prevented by vaccines, so a nitrate salt has no plausible therapeutic role without supporting data. The high TxGNN score is a computational prediction only and cannot replace clinical evidence.

A second prediction, **sclerosing cholangitis** (score 0.9921), is also Level L5 with no trials or literature. It has only a theoretical rationale: nitrate-nitrite-nitric oxide signaling might affect vascular tone, inflammation and biliary epithelial function. It is likewise a **Hold**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M022 | SprinJene Natural | Paste, dentifrice | Not recorded (valid) |
| Not available | Kali Nitricum | Pellet | Not recorded (cancelled) |

Other dosage forms associated with this ingredient include dentifrice gel (topical) and paste.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph lists **dental fluorosis** as a contraindicated disease. This comes from drug-disease graph edges, not from label text.
- **Drug Interactions**: No interactions were found in the queried data.

Please refer to the package insert for any further safety information. Label warnings and contraindications were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, no mechanism of action data and no recorded original indication. The biological rationale for treating meningococcal infection with a nitrate salt is implausible, and the drug is marketed in the US, with 2 valid licenses of 2.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- Package insert warnings and contraindications (blocking for safety screening)
- Any preclinical or clinical evidence of activity against *Neisseria meningitidis*, with comparison against established antibiotic therapy and vaccination
- Route-of-administration compatibility assessment for any systemic use
- Clarification of the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

