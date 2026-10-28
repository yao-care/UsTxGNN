---
layout: default
title: Acetohydroxamic Acid
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
monitor_inn: "ACETOHYDROXAMIC ACID"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-14
description: "Acetohydroxamic Acid: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection"
---

# Acetohydroxamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Acetohydroxamic Acid: From Urinary Tract Infection to Ureaplasma Urethritis
{: .text-alpha }

## One-Sentence Summary

Acetohydroxamic acid (AHA) was originally used as an adjunct treatment for urinary tract infection, where it inhibits bacterial urease.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, AHA is an irreversible inhibitor of bacterial urease. It is not an antimicrobial in the usual sense. By blocking urease, it reduces ammonia production and urinary alkalinization, which is why it has been used in urinary infections involving urease-producing bacteria.

*Ureaplasma urealyticum* also produces urease, so the mechanism is biologically plausible. However, Ureaplasma urethritis is a mucosal infection of the lower genital tract. It is not an upper-tract struvite stone condition, so the benefit of urease inhibition is less clear. The high score (0.9963) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This mechanistic reasoning is inferred rather than drawn from the supplied data.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Mechanistic Assessment | Evidence Level |
|------|------|------|------|------|
| 2 | Gonococcal urethritis | 0.9963 | *Neisseria gonorrhoeae* is not a recognized urease-producing pathogen, so there is no clear mechanistic link. The score likely reflects network proximity to the original indication. Effective antibiotics already exist. | L5 |
| 3 | Uterine inflammatory disease | 0.9954 | No clear link. The disease is usually polymicrobial and not urease-driven. | L5 |
| 4 | Xanthogranulomatous pyelonephritis | 0.9946 | The most plausible of the four, because it is associated with obstructing stones and urease-producing organisms such as *Proteus mirabilis*. It usually requires surgery plus antibiotics. | L5 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018749 (cancelled) | Lithostat | Tablet (oral) | Not stated |

The drug is marketed in the US, and the one US license, held by Mission Pharmacal Company, is valid.

## Safety Considerations

- **Contraindications and warnings from the knowledge graph** (these come from drug-disease relationship data, not package insert text): thrombocytopenia, substance abuse/dependence, anemia, macrocytic anemia, leukopenia, hemolytic anemia and phlebitis. Hematologic toxicity is the main theme. Blood-count monitoring would be essential in any further development.
- **Drug Interactions** (5 recorded):

| Interacting Drug | Severity |
|------|------|
| Cladribine | **Major** |
| Alemtuzumab | Moderate |
| Ocrelizumab | Moderate |
| Omacetaxine mepesuccinate | Moderate |
| Ustekinumab | Moderate |

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (evidence level L5), and the mechanistic link to a lower genital tract mucosal infection is weak. The only US product is cancelled, and the hematologic safety signals are notable. Effective antibiotic therapy also already exists for these conditions.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data
- Laboratory evidence that urease inhibition has an effect against *Ureaplasma*
- Any clinical or observational data in the predicted indication
- If any indication is pursued, xanthogranulomatous pyelonephritis is the most mechanistically plausible candidate, and a hematologic safety monitoring plan would be needed
- Clarification of the regulatory and supply pathway, given that the only US product is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

