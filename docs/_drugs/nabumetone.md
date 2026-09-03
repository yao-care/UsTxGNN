---
layout: default
title: Nabumetone
parent: 僅模型預測 (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
---

# Nabumetone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nabumetone: From Osteoarthritis/Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is a naphthylalkanone-class NSAID prodrug, metabolized to 6-methoxy-2-naphthylacetic acid (6-MNA), traditionally used for symptomatic relief of osteoarthritis and rheumatoid arthritis. The TxGNN model predicts a possible link to **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare GDF5-mutation skeletal disorder, but this direction is currently supported by **0 clinical trials** and **0 publications** — the signal exists only at the model-prediction level.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis / Rheumatoid Arthritis (NSAID class; not documented as a formal license in this evidence pack) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, Nabumetone belongs to the NSAID (naphthylalkanone) class and acts as a prodrug converted in vivo to 6-MNA, which inhibits cyclooxygenase (COX), with a relative preference for COX-2. Its anti-inflammatory and analgesic efficacy in osteoarthritis and rheumatoid arthritis is well established.

Acromesomelic Dysplasia, Hunter-Thompson Type, however, is a rare autosomal recessive skeletal dysplasia caused by GDF5 gene mutations, resulting in structural/developmental limb shortening rather than an inflammatory or pain-driven pathology. There is no known pathophysiological overlap between GDF5-mediated skeletal development and the COX/prostaglandin pathway that Nabumetone targets.

Given this, the mechanistic plausibility of this specific prediction is low. The most likely explanation is that the TxGNN knowledge-graph embedding placed this disease near Nabumetone's profile due to structural similarity in the graph (e.g., shared association with skeletal/joint-related nodes) rather than a genuine pharmacological relationship. This should be treated as a candidate signal requiring mechanistic scrutiny, not a validated hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Nabumetone is currently not marketed in Taiwan (market status: 未上市/Not Marketed), and no NDA or marketing authorization records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is very high (99.99%), but the target indication is a rare genetic skeletal dysplasia with no established pathological connection to Nabumetone's COX-inhibition mechanism. There are zero clinical trials, zero publications, and the drug is not currently marketed — evidence level is L5 (prediction only), and the pattern is consistent with a possible knowledge-graph embedding artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any safety pre-screening)
- Detailed mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical or mechanistic evidence linking COX/prostaglandin pathways to GDF5-related skeletal pathology, to confirm or rule out the biological plausibility of this signal
- Expert clinical/genetics review given the rarity and non-inflammatory nature of the target disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

