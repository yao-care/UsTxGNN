---
layout: default
title: Stannous Fluoride
parent: Model Prediction Only (L5)
nav_order: 1181
evidence_level: L5
indication_count: 1
---

# Stannous Fluoride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Stannous Fluoride: From Topical Oral Care to Meningococcal Infection

## One-Sentence Summary

Stannous fluoride is a topical oral-care ingredient used in dentifrices (toothpastes), gels and rinses.
The TxGNN model predicts it may be effective for **meningococcal infection**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on the model score alone and should be treated as a hypothesis, not a finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory data (marketed as topical oral-care and dental products) |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and DrugBank lists no original indications for this drug.
Stannous fluoride is a topical oral-care agent. Its antibacterial activity is attributed to tin and fluoride ions, which affect bacterial metabolism and plaque formation.

Meningococcal infection is an invasive systemic disease caused by *Neisseria meningitidis*. Topical dental use gives no meaningful systemic exposure, so any antimicrobial rationale is speculative.
The very high score (0.997) more likely reflects knowledge-graph neighborhood effects, such as shared fluoride/tin or antibacterial-class associations, than a real therapeutic signal.
The link cannot be checked against a known pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The regulatory data lists 20 authorizations in total. The 5 main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M021 | Crest Pro Health | Paste, dentifrice | Not stated |
| M021 | Crest | Paste, dentifrice | Not stated |
| M021 | KIDS Crest | Paste, dentifrice | Not stated |
| M021 | Crest Pro-Health | Paste, dentifrice | Not stated |
| M022 | parodontax | Paste | Not stated |

Other dosage forms on the market include gel (topical), mouthwash and rinse.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score, with no clinical trials or literature (evidence level L5). The proposed use is an invasive systemic infection, while stannous fluoride is a topical product with no meaningful systemic exposure, so there is no plausible route to efficacy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed for any safety screening
- Mechanism of action data (for example, from DrugBank)
- Any *in vitro* evidence of activity against *Neisseria meningitidis*
- An assessment of route compatibility, since a systemic formulation would be needed and none is marketed
- Published or registered studies supporting this indication, before the candidate is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

