---
layout: default
title: Brodalumab
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Brodalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Brodalumab: From Plaque Psoriasis to Strongyloidiasis

## One-Sentence Summary

Brodalumab (Siliq) is an injectable IL-17 receptor A blocker. The Evidence Pack does not include its label indication text, so the original use here is taken from general knowledge: moderate-to-severe plaque psoriasis.
The TxGNN model predicts it may be effective for **strongyloidiasis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is most likely a knowledge-graph artifact, and the drug is more likely a safety concern than a treatment for this infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the pack's license data; plaque psoriasis per general knowledge |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761032) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brodalumab blocks IL-17RA, the shared receptor for the IL-17 cytokine family. That is why it suits immune-mediated inflammatory diseases. The pack's detailed MOA field is empty, so this description comes from the mechanistic assessment in the pack.

**The prediction is not mechanistically reasonable.** IL-17 signaling contributes to mucosal and antimicrobial defense. Blocking it in a patient with *Strongyloides* infection carries a risk of immunosuppression-related hyperinfection. The high TxGNN score is likely a graph-proximity artifact rather than a therapeutic signal.

Other predicted indications look more plausible, though still weak. The pack lists "eye disease" (L4, research question only) and several immune-mediated optic nerve conditions (optic neuritis and related entities), where a Th17/IL-17 role is biologically plausible. None of them has clinical data for brodalumab.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for strongyloidiasis.

---

## Literature Evidence

Currently no related literature available for strongyloidiasis.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761032 | Siliq (Bausch Health US LLC) | Injection | — |

---

## Safety Considerations

- **Key Warnings (from the mechanistic assessment):**
  - Immunosuppression in *Strongyloides* infection carries a hyperinfection risk.
  - Brodalumab carries a boxed warning for suicidal ideation and behavior.
- **Drug Interactions:** No interactions were found in the queried data.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support, and it conflicts with brodalumab's immunosuppressive effect on antimicrobial defense. The evidence level is L5 (model prediction only), and the safety signal argues against pursuing this indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed label indication text and MOA data
- Any preclinical or clinical rationale for IL-17RA blockade in strongyloidiasis, which is currently absent
- If the team wants to pursue this drug, redirect effort to a specific immune-mediated ocular or optic indication rather than this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

