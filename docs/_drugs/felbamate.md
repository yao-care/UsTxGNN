---
layout: default
title: Felbamate
parent: Model Prediction Only (L5)
nav_order: 695
evidence_level: L5
indication_count: 2
---

# Felbamate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Felbamate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Felbamate is an antiepileptic drug. The provided data does not list an approved indication text, so this description comes from general pharmacology.
The TxGNN model ranks **trigeminal nerve neoplasm** first (score 99.62%), but **no clinical trials and no publications** support it, and the score appears to reflect knowledge-graph proximity rather than antitumour activity.
The second-ranked prediction, **trigeminal neuralgia**, is far more plausible, with **5 publications** including one case report of felbamate benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided data (felbamate is a known antiepileptic) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed as ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the dataset. Based on general pharmacology, felbamate is an antiepileptic that acts through NMDA receptor (glycine site) antagonism, GABAergic potentiation and sodium channel modulation. It has no known antineoplastic mechanism.

The evaluation found **no mechanistic link** between felbamate and trigeminal nerve neoplasm. The high score (0.996) is most likely driven by the drug's proximity in the knowledge graph to trigeminal nerve and neuralgia nodes, not by any effect on tumour biology. Treat this prediction as a likely model artefact.

The rank 2 prediction, **trigeminal neuralgia** (score 99.18%), is mechanistically plausible. Carbamazepine, the first-line drug for trigeminal neuralgia, is also an antiepileptic. Felbamate's sodium channel modulation and NMDA antagonism overlap with the mechanisms of other antiepileptics used for neuropathic pain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for trigeminal nerve neoplasm or trigeminal neuralgia).

---

## Literature Evidence

For the top prediction, trigeminal nerve neoplasm: currently no related literature available.

For the rank 2 prediction, trigeminal neuralgia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Review | CNS Drugs | Drug-choice guide for trigeminal neuralgia. Carbamazepine is the drug of choice. Baclofen, phenytoin and valproate are also effective. |
| [8877250](https://pubmed.ncbi.nlm.nih.gov/8877250/) | 1996 | Review | Clin Pharmacokinet | Carbamazepine drug-interaction update. It is used in trigeminal neuralgia, and felbamate is not its focus. |
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Case report | Clin J Pain | Felbamate analgesic efficacy evaluated in trigeminal neuralgia. It reported relief. |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Case report (safety) | Ann Pharmacother | Felbamate-induced delayed anaphylaxis. |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Preclinical (rat) | Indian J Pharmacol | Compares carbamazepine, gabapentin and lamotrigine for neuropathic pain. It does not evaluate felbamate. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA208970 | Felbamate | Tablet | Zydus Lifesciences Limited |
| ANDA211333 | Felbamate | Suspension | Novitium Pharma LLC |
| ANDA201680 | Felbamate | Tablet | Amneal Pharmaceuticals LLC |
| ANDA207093 | Felbamate | Tablet | Taro Pharmaceuticals U.S.A., Inc. |
| ANDA206314 | Felbamate | Suspension | Taro Pharmaceuticals U.S.A., Inc. |

Approved indication text is not provided for these listings. Routes: oral tablet and suspension.

---

## Safety Considerations

- **Key Warnings**: The dataset has no package insert warnings. The evaluation notes serious known concerns: aplastic anemia and hepatic failure. A delayed anaphylaxis case has also been reported (PMID 7633024).
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has no trials, no literature and no supported mechanism (L5), so it should not be pursued. Trigeminal neuralgia (L4, "Research Question") has only one case report supporting felbamate. Its serious safety risks and the availability of approved alternatives such as carbamazepine limit it to refractory cases at most.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which currently block safety screening
- Confirmed mechanism of action data from DrugBank
- For trigeminal neuralgia, a formal risk-benefit assessment versus approved alternatives, plus controlled clinical evidence beyond a single case report
- Route compatibility and similarity-to-original-indication analyses, both currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

