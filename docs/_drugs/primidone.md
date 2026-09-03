---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 1083
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

> Primidone is a classical barbiturate-derived anticonvulsant, historically used to treat epilepsy and essential tremor (based on general pharmacological knowledge; this dataset contains no confirmed original-indication record for this market).
> TxGNN's top-ranked prediction is **Trigeminal Nerve Neoplasm**, but this specific signal is flagged by the model's own rationale as likely knowledge-graph noise (a "trigeminal" string-matching artifact confused with *trigeminal neuralgia*), and it is supported by **0 clinical trials and 0 publications**.
> A broader cluster of 6 lower-ranked predictions — all in the **reflex epilepsy syndrome** family (startle, audiogenic, reading, eating, thinking, micturition-induced seizures) — has a mechanistically coherent rationale and modest preclinical/case-level literature support, and is the more credible signal in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (0 licenses on file); Primidone is generally known as a barbiturate-class anticonvulsant / essential tremor agent |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% (rank 307 of model output) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, primidone is metabolized to two active compounds — phenobarbital and phenylethylmalonamide (PEMA) — both of which are positive allosteric modulators of the GABA-A receptor, producing broad-spectrum CNS depressant and anticonvulsant activity. This mechanism has no established link to tumor suppression or neoplastic pathways.

The evidence pack's own rationale explicitly cautions that the top-ranked prediction (Trigeminal Nerve Neoplasm) is "極可能為知識圖譜上 'trigeminal' 字面共病節點的雜訊連結" — i.e., very likely a string-matching artifact where the knowledge graph confused "trigeminal nerve neoplasm" with the mechanistically unrelated but lexically similar "trigeminal neuralgia." There is no clinical, preclinical, or mechanistic evidence connecting GABA-A potentiation to neoplasm growth control, and this candidate should not be advanced without independent validation of the underlying KG edge.

A more defensible signal exists further down the ranked list: seven predictions (ranks 2–8) all fall within the **reflex epilepsy** spectrum — seizures triggered by startle, sound, reading, eating, micturition, or cognitive activity. These share a plausible pathophysiology (cortical hyperexcitability triggered by sensory/cognitive stimuli) for which primidone's GABA-A-potentiating action is mechanistically consistent with its established use in generalized and partial epilepsies (see the pivotal Mattson et al. 1985 NEJM RCT, PMID 3925335, comparing primidone with carbamazepine, phenytoin, and phenobarbital). Several classic animal audiogenic-seizure screening studies (e.g., PMID 5824929, 184518) directly tested primidone's anticonvulsant efficacy against reflex-triggered seizures, lending indirect preclinical support to this indication cluster — though none of these studies targeted the specific reflex-epilepsy subtypes flagged here, and no dedicated human trials exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(This applies to all 10 predicted indications in this evidence pack — no clinical trials were identified for any candidate.)*

---

## Literature Evidence

For the top-ranked prediction (Trigeminal Nerve Neoplasm): Currently no related literature available.

### Supplementary: Reflex Epilepsy Cluster — Strongest Supporting Literature (Ranks 2–8)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3925335](https://pubmed.ncbi.nlm.nih.gov/3925335/) | 1985 | RCT | N Engl J Med | Landmark 10-center RCT (n=622) comparing carbamazepine, phenobarbital, phenytoin, and primidone in partial/secondarily generalized tonic-clonic seizures |
| [5824929](https://pubmed.ncbi.nlm.nih.gov/5824929/) | 1969 | Preclinical (Animal Screen) | Br J Pharmacol | Audiogenic seizure screening model in mice used to detect anticonvulsant activity, including barbiturate-class compounds |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Preclinical (Animal) | Neurologie et psychiatrie | Direct effect of primidone (with phenobarbital, diphenylhydantoin) on brain enzyme activity in mice with audiogenic epilepsy |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case Report | Chinese Med J (Free China ed) | Pediatric case of startle epilepsy presenting as drop attacks |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clin Neurosci | Primidone (500–1000 mg/day) listed among effective agents for cortical stimulus-sensitive myoclonus |
| [116632](https://pubmed.ncbi.nlm.nih.gov/116632/) | 1979 | Case Report | Arch Neurol | Reflex epilepsy triggered by drawing/concentration-requiring activity |
| [14151214](https://pubmed.ncbi.nlm.nih.gov/14151214/) | 1964 | Review | Lancet | Early classification of movement-induced reflex epilepsy |

---

## US Market Information

Primidone currently has **0 active NDAs** on file and is listed as **Not Marketed** in this dataset. No product/dosage-form information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This evidence pack flags TFDA/FDA label warnings and contraindications as a Blocking data gap, DG001 — this must be resolved before any safety-relevant decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Trigeminal Nerve Neoplasm) has zero supporting trials or literature and is explicitly flagged in its own rationale as a likely knowledge-graph artifact confusing "trigeminal nerve neoplasm" with "trigeminal neuralgia." No mechanistic pathway connects primidone's GABA-A-mediated anticonvulsant action to neoplasm suppression, so this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA/FDA label warnings and contraindications before any safety-relevant evaluation
- Resolve High-severity data gap DG002: obtain confirmed MOA data from DrugBank to properly assess mechanistic plausibility
- Independent validation of the KG edge for "trigeminal nerve neoplasm" (e.g., check whether it reflects a mislabeled or duplicate node for trigeminal neuralgia)
- If pursuing the reflex-epilepsy cluster instead (ranks 2–8, evidence level L4, "Research Question" stage): design or identify targeted clinical studies in specific reflex-epilepsy subtypes, since current support is limited to a general anticonvulsant RCT and older animal audiogenic-seizure screens rather than subtype-specific trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

