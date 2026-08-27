---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Using the report template you provided (the v5 Drug Repurposing Evaluation Report format from your prompt) to generate the report from the Evidence Pack JSON.

A note before the report: this Evidence Pack is a "multi" candidate file — the drug has 7 ranked TxGNN predictions, all clustered around movement disorders. Per the template's extraction rule, `predicted_indications[0]` (highest TxGNN score) is **"psychogenic movement disorders"**, which has **zero clinical trials and zero literature** — the model itself flags this as likely an embedding-similarity artifact rather than a genuine mechanistic signal. I've followed the template literally for the required sections, and added one extra (non-duplicative) section summarizing the other ranked candidates in this batch, since two of them (chronic tic disorder, tardive dyskinesia/orofacial dyskinesia) carry meaningfully stronger literature support and are more decision-relevant than rank #1.

---

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

> Donepezil is a reversible acetylcholinesterase inhibitor established for the treatment of Alzheimer's disease dementia.
> The TxGNN model's top-ranked prediction is **Psychogenic Movement Disorders**,
> but this specific pairing is currently supported by **0 clinical trials** and **0 publications** — the mechanistic rationale itself notes the pathology (functional neurocircuit dysregulation) does not align with a cholinergic deficit model, suggesting the high score may reflect embedding similarity to other movement-disorder nodes rather than a real signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (dementia) — inferred from known drug class; not present in this Evidence Pack (Taiwan license data unavailable) |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this Evidence Pack (flagged as a High-severity data gap). Based on known pharmacology, donepezil is a reversible, centrally-acting acetylcholinesterase inhibitor (AChEI) — its efficacy in Alzheimer's disease dementia is well established (this is consistently confirmed across the literature retrieved for other candidates in this batch, e.g., PMID 12611743, PMID 14564129), and it works by increasing synaptic acetylcholine availability in cortical and striatal circuits.

For the top-ranked prediction, **psychogenic movement disorders**, the model's own rationale is explicitly skeptical: this condition is understood to arise from functional neurocircuit dysregulation rather than a cholinergic deficit, and no clinical or preclinical evidence links AChEIs to this pathology. The rationale text states the high TxGNN score "may be due to KG embedding similarity with other movement-disorder nodes" rather than a genuine pharmacological signal — i.e., this is likely a false-positive artifact of the knowledge graph rather than a testable hypothesis.

By contrast, other predictions within this same batch (see "Other Predicted Indications" below) have a more plausible mechanistic story — increased striatal ACh via nicotinic/muscarinic modulation of dopamine release has some literature support for tic disorders and tardive dyskinesia — but these rank lower by TxGNN score than the headline prediction reviewed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Donepezil is not currently marketed in Taiwan under this Evidence Pack (0 licenses on file). No authorization records, product names, or approved-indication text are available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were queried but returned no results — TFDA label data is flagged as a Blocking data gap pending PDF retrieval and parsing.)*

---

## Other Predicted Indications in This Batch

This Evidence Pack contains 7 ranked TxGNN predictions for donepezil, all within the movement-disorder space. Two are more evidence-backed than the top-ranked candidate reviewed above and may warrant separate follow-up:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Key Support |
|------|---------|-------------|-----------------|------------------|------------------|--------------|
| 2 | Chronic tic disorder | 99.19% | L3 | S1 | Research Question | 5 publications, incl. an 18-week open-label dose-escalation study in children/adolescents (PMID 18343255) and preclinical Tourette-model data (PMID 14643839, 16045972) |
| 5 | Extrapyramidal and movement disease | 99.16% | L3 | S1 | Hold | 4 publications, but evidence direction is mixed — a systematic review (PMID 40224553) documents AChEIs as a *cause* of movement disorders in Alzheimer's patients, opposing the predicted therapeutic direction |
| 8 | Lingual-facial-buccal dyskinesia (tardive dyskinesia) | 99.02% | L3 | S2 | Research Question | 20 publications, including **2 Cochrane systematic reviews** on cholinergic drugs for antipsychotic-induced tardive dyskinesia (PMID 29553158, 12137608) — the most substantive evidence base in this batch |

These three signals reflect a coherent pharmacological theme (cholinergic modulation of hyperkinetic movement disorders) worth evaluating as a group, separate from the psychogenic movement disorders prediction, which lacks any supporting evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, psychogenic movement disorders, has no clinical trial or literature support, and the proposed mechanism (cholinergic enhancement) does not align with the condition's known functional/neurocircuit pathology. The model's own rationale flags this as a probable knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action detail from DrugBank — currently a High-severity data gap
- If pursuing the psychogenic movement disorders lead specifically: independent mechanistic or case-level evidence, since none currently exists
- Consider redirecting evaluation toward the two more evidence-backed candidates in this batch (chronic tic disorder; tardive/orofacial dyskinesia), where systematic-review-level literature already exists, as a more productive use of further research effort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

