---
layout: default
title: Telotristat Ethyl
parent: Model Prediction Only (L5)
nav_order: 1207
evidence_level: L5
indication_count: 2
monitor_inn: "TELOTRISTAT ETHYL"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
last_modified_at: 2026-10-14
description: "Telotristat Ethyl: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Diarrheal disease"
---

# Telotristat Ethyl
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

## Telotristat Ethyl: From Diarrheal Disease to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Telotristat ethyl was originally used to treat diarrheal disease (in the US it was marketed as Xermelo).
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9938 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, telotristat ethyl is a tryptophan hydroxylase inhibitor that reduces peripheral serotonin synthesis, which is how it helps control diarrhoea.

No established biological link was identified between lowering peripheral serotonin and cauda equina syndrome. Cauda equina syndrome is a compressive injury of the lumbosacral nerve roots. The drug is not expected to cross the blood-brain barrier appreciably and would not be expected to relieve nerve root compression.

The high score (0.9938) is a computational prediction from the TxGNN model (deep learning) only. It may reflect similarities the model learned between related diseases, such as shared bowel and bladder dysfunction features, not biological evidence or a true therapeutic mechanism. The prediction should be treated as a hypothesis, not as evidence of efficacy.

A second prediction, "obsolete neurogenic bladder (disease)" (score 0.9915), is also at the model-prediction-only stage. Serotonin signalling does play a role in bladder and bowel function, so a speculative link is conceivable, but no supporting data exist. The term is also obsolete in the ontology and should be mapped to a current term (e.g., neurogenic lower urinary tract dysfunction) before any further assessment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208794 (cancelled) | Xermelo (Lexicon Pharmaceuticals, Inc.) | Tablet (oral) | Not listed |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database; the 19 below are the ones listed in the data compiled for this report, all rated Moderate:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, prednisone
  - Antiemetics and related agents: aprepitant, rolapitant, ondansetron, granisetron
  - Other: bupropion, clarithromycin, saxagliptin, linagliptin, eliglustat, naldemedine, naloxegol, nitisinone, repaglinide, simvastatin, cisapride

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and no plausible mechanism links peripheral serotonin reduction to nerve root compression. The only US authorization is cancelled. The model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data, and a mechanistic rationale connecting the drug to cauda equina syndrome
- Package insert warnings and contraindications (currently missing, which blocks safety screening)
- Any preclinical or clinical evidence in the predicted indication
- For the neurogenic bladder prediction, remapping to a current disease term and a fresh evidence search
- Clarification of the cancelled US market status and route compatibility for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

