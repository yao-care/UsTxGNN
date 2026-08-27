---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 821
evidence_level: L5
indication_count: 9
---

# Ivermectin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an avermectin-class antiparasitic agent; its formal original-indication and regulatory MOA records are not available in this evidence pack, but its established pharmacology targets invertebrate glutamate-gated chloride channels. The TxGNN model predicts potential activity against **Vulvovaginal Candidiasis**, but this ranking is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no mechanistic or empirical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established from source data (drug not marketed; `original_indications` and `original_moa` are unrecorded). Known globally as an antiparasitic/anthelmintic agent per evidence-pack rationale text. |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ivermectin is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacology, ivermectin is an avermectin-class macrocyclic lactone that activates glutamate-gated chloride channels found in invertebrates (nematodes, arthropods), producing its antiparasitic/antiscabietic effect — a mechanism with no known intersection with fungal pathogenesis.

Vulvovaginal candidiasis is caused by *Candida* species, a fungal pathogen with a fundamentally different cell biology (no glutamate-gated chloride channel target) from the helminths and arthropods ivermectin is designed against. There is no pharmacological or clinical precedent connecting antiparasitic activity to antifungal efficacy for this compound.

Notably, 8 of the 9 diseases TxGNN ranked highest for ivermectin in this pack are *Candida*-related conditions (vulvovaginal, esophageal, neonatal, congenital, invasive candidiasis, *C. glabrata*) plus two unrelated gynecologic entities (HPV infection, atrophic vaginitis with no infectious component at all). This clustering suggests the high score reflects a graph-embedding similarity pattern rather than a biologically grounded signal — the model itself provides no mechanistic rationale, and the evidence pack's own analysis explicitly states the score "reflects knowledge-graph embedding similarity only, with no mechanistic support."

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Ivermectin currently has no licensed products on record in this market (`total_licenses = 0`, market status: Not Marketed). No approved indication text is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent label warnings/contraindications are marked as a Blocking data gap — this alone prevents the candidate from entering the S1 safety pre-screen, independent of efficacy evidence.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's embedding score (L5), with zero clinical trials or literature specific to vulvovaginal candidiasis, and no plausible mechanistic link between ivermectin's known antiparasitic pharmacology and antifungal activity. Separately, a Blocking data gap (missing label/warning data) already prevents this candidate from clearing the S1 safety pre-screen regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings/contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Preclinical/in-vitro evidence of antifungal activity against *Candida* spp. to establish a mechanistic hypothesis
- At minimum, an observational study or case series directly addressing this indication before advancing past L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

