---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 1037
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

> Phenobarbital is a classic barbiturate, established for the long-term treatment of epilepsy and seizure disorders.
> The TxGNN model's top-ranked new indication is **Trigeminal Nerve Neoplasm**,
> but this prediction is currently supported by only **1 unrelated case series** and **0 clinical trials** — evidence is not yet meaningful.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / Seizure disorders (based on established pharmacological classification; no formal label text available — this evidence pack contains no `original_indications` or license data for this drug) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` = Data Gap). Based on information embedded elsewhere in this evidence pack, phenobarbital is understood to be a GABA-A receptor positive allosteric modulator with central nervous system depressant and anticonvulsant activity — the pharmacological basis for its established use in epilepsy.

For this specific top-ranked prediction, however, the evidence pack's own rationale explicitly flags the pairing as likely **knowledge-graph noise**: there is no known biological link between phenobarbital's GABA-A-mediated CNS-suppressant/anticonvulsant mechanism and tumour growth suppression relevant to a trigeminal nerve neoplasm. The single supporting publication is a 1997 case series on Sturge-Weber syndrome (a vascular/seizure disorder), which does not address nerve tumour treatment and is only tangentially connected through shared neurological terminology.

It is worth noting that several lower-ranked candidates in this evidence pack (e.g., audiogenic seizures, rank 6) have substantially stronger and more mechanistically coherent support — multiple preclinical studies directly testing phenobarbital in reflex-seizure animal models — and may warrant separate evaluation as they represent extensions of phenobarbital's existing antiepileptic mechanism rather than an unrelated oncology application.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españoles de pediatría | Reviews 14 cases of Sturge-Weber syndrome over a 25-year period; does not address trigeminal nerve neoplasm treatment or phenobarbital efficacy against tumour growth |

## US Market Information

Phenobarbital is not currently marketed in the US per this evidence pack (`market_status`: 未上市 / Not Marketed), and no NDA or license records are available (`total_licenses`: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a single, thematically unrelated case series (L5, model-prediction-only evidence), and the evidence pack's own mechanistic assessment identifies this drug-disease pairing as likely a false-positive knowledge-graph association rather than a biologically plausible repurposing candidate.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/FDA label warnings and contraindications) before any safety evaluation can begin
- Resolve DG002 (confirmed mechanism of action documentation) to properly assess mechanistic plausibility
- Disease-specific preclinical or clinical evidence directly linking phenobarbital to trigeminal nerve neoplasm, if this candidate is to be pursued further
- Consider re-scoping evaluation toward higher-evidence candidates in this pack (e.g., audiogenic seizures, L3/S2) that align with phenobarbital's known antiepileptic mechanism, rather than this L5 oncology candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

