---
layout: default
title: Sodium Fluoride
parent: 僅模型預測 (L5)
nav_order: 1170
evidence_level: L5
indication_count: 7
---

# Sodium Fluoride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Sodium Fluoride: From Dental/Diagnostic Use to Epiglottitis (Prediction Not Supported by Evidence)

## One-Sentence Summary

> Sodium fluoride (DrugBank DB09325) is not currently licensed for any indication in Taiwan; its known uses elsewhere are limited to topical dental caries prevention and as the ¹⁸F-NaF PET bone-imaging tracer.
> The TxGNN model's top prediction is **epiglottitis**, but this candidate has **zero supporting clinical trials and zero supporting literature**, and the model's rationale itself flags the score as a likely embedding-space artifact.
> None of the seven top-ranked predicted indications for this drug are supported by real-world evidence — all are model-output only (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not licensed/marketed in Taiwan (0 NDAs on file); known off-label/global uses are dental enamel remineralization and ¹⁸F-NaF PET bone imaging |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US/Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sodium fluoride is not available in this evidence pack. Based on generally known information referenced within the evidence itself, sodium fluoride's established roles are (1) topical anti-caries action via enamel remineralization, and (2) as the ¹⁸F-labeled tracer (¹⁸F-NaF) used in PET/CT bone imaging — a diagnostic, not therapeutic, application.

Neither of these known roles offers a plausible pharmacological link to epiglottitis, which is typically an acute bacterial infection/inflammation of the epiglottis (historically *H. influenzae* type b, streptococci) requiring antimicrobial and airway management. Sodium fluoride has no documented antimicrobial or anti-inflammatory activity that would explain efficacy in this setting.

The evidence pack's own mechanistic analysis for this candidate concludes: "No known mechanistic link. Sodium fluoride's known activity is limited to dental remineralization and use as an ¹⁸F-NaF PET bone-imaging agent, with no antimicrobial or anti-inflammatory mechanism to explain efficacy in epiglottitis (commonly caused by Hib, streptococci, etc.). The high TxGNN score is suspected to be an artifact of the embedding space rather than biologically plausible." This same pattern (high score, no biological rationale) repeats across all seven top-ranked predictions for this drug, including urinary tract infection, Ureaplasma urethritis, gonococcal urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, and laryngitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for epiglottitis.

*(Note: A secondary candidate, laryngitis (rank 7, score 99.49%), did return 5 PubMed hits, but on review none constitute therapeutic evidence — one is a poultry toxicology study on high-dietary-fluoride intestinal effects, one is an unrelated diphtheria-toxin cell mechanism study, and three are incidental case reports of ¹⁸F-NaF PET/CT imaging uptake in cancer patients with cartilage metastases. These reflect NaF's role as a PET tracer, not a treatment for laryngeal inflammation, and were assessed as keyword-matching artifacts rather than genuine mechanistic support.)*

---

## US Market Information

Sodium fluoride currently holds no marketing licenses on record (0 NDAs); no license or product data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA labeling data (warnings/contraindications) has not yet been retrieved for this candidate — this is flagged as a **blocking data gap** that must be resolved before any safety-based decision can be made (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the model's top-ranked predicted indications for sodium fluoride — including the top-ranked epiglottitis candidate — are supported by clinical trials or literature, and the drug's known pharmacology (topical dental remineralization, PET imaging tracer) offers no plausible mechanism for any of the infectious/inflammatory conditions predicted. The evidence pack's own analysis assesses the high TxGNN scores as likely embedding-space artifacts rather than genuine signal. Combined with the absence of MOA data and a blocking gap in TFDA safety labeling, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA (or equivalent regulator) prescribing information — warnings, contraindications — to close the blocking data gap (DG001)
- Confirmed mechanism of action data via DrugBank API (DG002)
- Independent biological/mechanistic rationale connecting sodium fluoride to any of the predicted indications before further evidence collection is warranted
- If no such rationale emerges, this candidate should be deprioritized rather than actively pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

