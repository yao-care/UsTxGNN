---
layout: default
title: Griseofulvin
parent: Moderate Evidence (L3-L4)
nav_order: 762
evidence_level: L4
indication_count: 5
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Griseofulvin: From Antifungal Use to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal that is marketed in the US as tablets. The TxGNN model predicts it may be effective for **myiasis** (parasitic infestation by fly larvae) with a score of 99.41%. Support is very weak: **0 clinical trials** and **1 publication**, a 1970 veterinary review that is not specific to griseofulvin.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US label data provided (griseofulvin is generally known as an antifungal) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the authorizations listed are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, griseofulvin is a fungistatic agent that disrupts fungal microtubules and mitosis. It has no established activity against dipteran (fly) larvae.

The evidence review found no plausible mechanistic link between fungal infection and myiasis. The high TxGNN score most likely reflects proximity in the knowledge graph to other parasitic skin diseases, not a pharmacological rationale. Because the original indication and MOA fields are empty, the prediction could not be cross-checked against them.

The other four predictions are wound myiasis, creeping myiasis, furuncular myiasis and *Echinococcus granulosus* infection. All have scores of about 99.3% and evidence level L5 (prediction only), and none has trials or literature.
- The three myiasis subtypes appear to inherit their scores from the parent myiasis node.
- Griseofulvin's antimitotic effect is specific to fungal tubulin. Standard therapy for cystic echinococcosis uses benzimidazoles, which act on parasite beta-tubulin, so any similarity to griseofulvin is speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | "Parasitic skin diseases of dogs and cats." A veterinary overview; no abstract is available, and it does not show evidence for griseofulvin in myiasis. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091592 | Griseofulvin (Sandoz Inc) | Tablet | Not listed in the data provided |
| ANDA061996 | Ultramicrosize Griseofulvin (Chartwell RX, LLC) | Tablet | Not listed in the data provided |
| ANDA061996 | Fulvicin P/G 165 (Solubiomix, LLC) | Tablet | Not listed in the data provided |
| ANDA204371 | Ultramicrosize Griseofulvin (Amneal Pharmaceuticals of New York LLC) | Tablet, coated | Not listed in the data provided |
| ANDA061996 | Ultramicrosize Griseofulvin (Chartwell RX, LLC) | Tablet | Not listed in the data provided |

Available forms include oral tablets, coated tablets and a suspension.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial support, and the only literature is a 1970 veterinary review that does not address griseofulvin. There is also no plausible antiparasitic mechanism, so the score is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data from DrugBank
- Any preclinical or clinical evidence of griseofulvin activity against fly larvae, which is currently absent
- Confirmation of route compatibility, which is currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

